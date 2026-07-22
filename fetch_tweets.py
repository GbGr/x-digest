#!/usr/bin/env python3
"""
X Feed Digest — сборщик сырых данных ленты.

Забирает свежие посты подписок (accounts.txt) через twitterapi.io и складывает:
  data/latest.json           — полные данные (машинный формат, на будущее)
  data/archive/<дата>.json   — история
  data/feed/<дата>/index.md  — индекс для утренней задачи Claude
  data/feed/<дата>/part-NN.md— компактные шарды (читаются через WebFetch)
  data/feed/latest/…         — копия сегодняшнего под стабильным путём

Дата — по Asia/Saigon (UTC+7). Зависимостей нет, только stdlib.
Ключ API — в переменной окружения TWITTERAPI_KEY (GitHub Secret, не коммитить!).
Самопроверка без сети: TWITTERAPI_SELFTEST=1 python fetch_tweets.py
"""

import json
import os
import shutil
import sys
import time
import urllib.parse
import urllib.request
from datetime import datetime, timedelta, timezone
from pathlib import Path

API_BASE = "https://api.twitterapi.io"
KEY = os.environ.get("TWITTERAPI_KEY", "")
SELFTEST = os.environ.get("TWITTERAPI_SELFTEST") == "1"
WINDOW_HOURS = int(os.environ.get("WINDOW_HOURS", "26"))   # окно с запасом к 24ч
MAX_PAGES_PER_USER = int(os.environ.get("MAX_PAGES_PER_USER", "6"))
SHARD_LIMIT = 9000        # байт на шард — безопасно для дословного WebFetch
KEEP_FEED_DAYS = 10       # сколько дневных папок feed держать
KEEP_ARCHIVE_DAYS = 45    # сколько дневных json держать

ROOT = Path(__file__).resolve().parent
SAIGON = timezone(timedelta(hours=7))
NOW = datetime.now(timezone.utc)
SINCE = NOW - timedelta(hours=WINDOW_HOURS)
DATE = NOW.astimezone(SAIGON).strftime("%Y-%m-%d")


def log(*a):
    print(*a, flush=True)


def tget(d, *keys, default=None):
    """Достаёт первое существующее поле (защита от вариаций схемы API)."""
    for k in keys:
        if isinstance(d, dict) and d.get(k) is not None:
            return d[k]
    return default


def api_get(path, **params):
    url = f"{API_BASE}{path}?{urllib.parse.urlencode(params)}"
    req = urllib.request.Request(
        url, headers={"X-API-Key": KEY, "User-Agent": "x-digest/1.0"}
    )
    last = None
    for attempt in range(4):
        try:
            with urllib.request.urlopen(req, timeout=30) as r:
                return json.loads(r.read().decode("utf-8"))
        except Exception as e:  # noqa: BLE001 — ретраим всё, включая 429/5xx
            last = e
            time.sleep(1.6 ** (attempt + 1))
    raise RuntimeError(f"GET {path} не удался после ретраев: {last}")


def parse_time(s):
    """createdAt вида 'Tue Dec 10 07:00:30 +0000 2024' (или ISO — на всякий)."""
    s = str(s or "")
    for fmt in ("%a %b %d %H:%M:%S %z %Y",):
        try:
            return datetime.strptime(s, fmt)
        except ValueError:
            pass
    try:
        return datetime.fromisoformat(s.replace("Z", "+00:00"))
    except ValueError:
        return None


def extract_links(tw):
    links = []
    ent = tget(tw, "entities", default={}) or {}
    for u in ent.get("urls") or []:
        exp = tget(u, "expanded_url", "url")
        if exp and "t.co/" not in exp:
            links.append(exp)
    return links


def norm(tw, owner):
    """Приводит твит к компактной записи."""
    author = tget(tw, "author", default={}) or {}
    handle = tget(author, "userName", "username", "screen_name", default=owner)
    ts = parse_time(tget(tw, "createdAt", default=""))
    tid = str(tget(tw, "id", default=""))
    rt = tget(tw, "retweeted_tweet")
    qt = tget(tw, "quoted_tweet")
    rec = {
        "id": tid,
        "url": tget(tw, "url", default=f"https://x.com/{handle}/status/{tid}"),
        "author": handle,
        "owner": owner,
        "time": ts.astimezone(timezone.utc).isoformat(timespec="minutes") if ts else "",
        "text": (tget(tw, "text", default="") or "").strip(),
        "is_reply": bool(tget(tw, "isReply", default=False)),
        "reply_to": tget(tw, "inReplyToUsername", default="") or "",
        "conv": str(tget(tw, "conversationId", default="")),
        "likes": int(tget(tw, "likeCount", default=0) or 0),
        "rts": int(tget(tw, "retweetCount", default=0) or 0),
        "replies": int(tget(tw, "replyCount", default=0) or 0),
        "views": int(tget(tw, "viewCount", default=0) or 0),
        "links": extract_links(tw),
        "rt_of": None,
        "quoted": None,
    }
    if isinstance(rt, dict):
        ra = tget(rt, "author", default={}) or {}
        rec["rt_of"] = {
            "id": str(tget(rt, "id", default="")),
            "author": tget(ra, "userName", "username", default="?"),
            "text": (tget(rt, "text", default="") or "").strip(),
            "url": tget(rt, "url", default=""),
            "likes": int(tget(rt, "likeCount", default=0) or 0),
        }
        rec["links"] = rec["links"] or extract_links(rt)
    if isinstance(qt, dict):
        qa = tget(qt, "author", default={}) or {}
        rec["quoted"] = {
            "author": tget(qa, "userName", "username", default="?"),
            "text": (tget(qt, "text", default="") or "").strip()[:500],
            "url": tget(qt, "url", default=""),
        }
    return rec


def fetch_user(handle):
    """Твиты аккаунта за окно. Страницы идут от новых к старым; закреплённый
    (старый) твит может стоять первым, поэтому стоп — только когда вся
    страница целиком старше окна."""
    out, cursor = [], ""
    for _page in range(MAX_PAGES_PER_USER):
        resp = api_get(
            "/twitter/user/last_tweets",
            userName=handle, cursor=cursor, includeReplies="true",
        )
        container = resp if isinstance(resp.get("tweets"), list) else (resp.get("data") or {})
        page = container.get("tweets") or []
        if not page:
            break
        page_times = []
        for tw in page:
            ts = parse_time(tget(tw, "createdAt", default=""))
            if ts is None:
                continue
            page_times.append(ts)
            if ts >= SINCE:
                out.append(norm(tw, handle))
        has_next = bool(tget(resp, "has_next_page", default=tget(container, "has_next_page", default=False)))
        cursor = tget(resp, "next_cursor", default=tget(container, "next_cursor", default="")) or ""
        page_all_old = bool(page_times) and max(page_times) < SINCE
        if page_all_old or not has_next or not cursor:
            break
        time.sleep(0.25)
    return out


def keep_item(rec, handles_lower):
    """Фильтр: выкидываем реплаи чужим (диалоги) и всё старше окна,
    оставляем посты, свои треды, цитаты и ретвиты."""
    if rec["is_reply"] and rec["reply_to"] and rec["reply_to"].lower() != rec["owner"].lower():
        return False
    if not rec["text"] and not rec["rt_of"]:
        return False
    if rec["time"]:
        try:
            if datetime.fromisoformat(rec["time"]) < SINCE:
                return False
        except ValueError:
            pass
    return True


def merge_threads(items):
    """Твиты одного автора с одним conversationId склеиваются в тред."""
    by_key, order = {}, []
    for r in items:
        key = (r["conv"], r["owner"]) if r["conv"] else (r["id"], r["owner"])
        if key not in by_key:
            by_key[key] = []
            order.append(key)
        by_key[key].append(r)
    merged = []
    for key in order:
        group = sorted(by_key[key], key=lambda r: r["time"])
        if len(group) == 1:
            g = dict(group[0])
            g["kind"] = "rt" if g["rt_of"] else "post"
            merged.append(g)
            continue
        root = group[0]
        g = dict(root)
        g["kind"] = f"thread({len(group)})"
        g["text"] = "\n[->] ".join(x["text"] for x in group if x["text"])
        g["likes"] = max(x["likes"] for x in group)
        g["rts"] = max(x["rts"] for x in group)
        g["replies"] = max(x["replies"] for x in group)
        g["views"] = max(x["views"] for x in group)
        links, seen = [], set()
        for x in group:
            for u in x["links"]:
                if u not in seen:
                    seen.add(u)
                    links.append(u)
        g["links"] = links
        merged.append(g)
    return merged


def dedupe_rts(items, collected_ids):
    """Один и тот же ретвитнутый пост показываем один раз."""
    seen_rt, out = set(), []
    for r in items:
        if r.get("rt_of"):
            oid = r["rt_of"]["id"]
            if oid in seen_rt or oid in collected_ids:
                continue
            seen_rt.add(oid)
        out.append(r)
    return out


def fmt_item(r):
    metric = f"L{r['likes']} RT{r['rts']} C{r['replies']} V{r['views']}"
    lines = [f"T={r['id']} | @{r['author']} | {r['time']} | {metric} | {r.get('kind', 'post')}"]
    lines.append(f"URL={r['url']}")
    if r.get("rt_of"):
        ro = r["rt_of"]
        lines.append(f"RT-OF @{ro['author']} (L{ro['likes']}): {ro['text'][:2000]}")
        if ro.get("url"):
            lines.append(f"RT-URL={ro['url']}")
    if r["text"]:
        txt = r["text"]
        if len(txt) > 6000:
            txt = txt[:6000] + " …[обрезано — полный текст по ссылке]"
        lines.append(f"TEXT: {txt}")
    if r.get("quoted"):
        q = r["quoted"]
        lines.append(f"QUOTED @{q['author']}: {q['text']}")
    if r["links"]:
        lines.append("LINKS: " + " ; ".join(r["links"][:5]))
    lines.append("--")
    return "\n".join(lines)


def build_shards(items):
    """Группируем по авторам, жадно пакуем в части ≤ SHARD_LIMIT байт."""
    by_author = {}
    for r in items:
        by_author.setdefault(r["owner"], []).append(r)
    blocks = []
    for author in sorted(by_author, key=str.lower):
        rows = sorted(by_author[author], key=lambda r: r["time"])
        head = f"## @{author} — {len(rows)} шт.\n\n"
        sec = head + "\n".join(fmt_item(r) for r in rows) + "\n"
        if len(sec.encode()) <= SHARD_LIMIT:
            blocks.append(sec)
            continue
        buf = head  # плодовитый автор — режем по элементам
        for r in rows:
            item = fmt_item(r) + "\n"
            if len((buf + item).encode()) > SHARD_LIMIT and buf != head and not buf.endswith("(продолжение)\n\n"):
                blocks.append(buf)
                buf = f"## @{author} (продолжение)\n\n"
            buf += item
        blocks.append(buf)
    parts, cur = [], ""
    for sec in blocks:
        if cur and len((cur + sec).encode()) > SHARD_LIMIT:
            parts.append((cur, count_items(cur)))
            cur = ""
        cur += sec
    if cur:
        parts.append((cur, count_items(cur)))
    return parts


def count_items(text):
    return sum(1 for line in text.splitlines() if line.startswith("T="))


def write_outputs(items, errors, total_accounts):
    feed_dir = ROOT / "data" / "feed" / DATE
    latest_dir = ROOT / "data" / "feed" / "latest"
    archive_dir = ROOT / "data" / "archive"
    for d in (feed_dir, latest_dir, archive_dir):
        d.mkdir(parents=True, exist_ok=True)
    for old in feed_dir.glob("*"):
        old.unlink()
    for old in latest_dir.glob("*"):
        old.unlink()

    parts = build_shards(items)
    err_line = "none" if not errors else "; ".join(f"@{h}: {m}" for h, m in errors.items())
    index = [
        f"# X-FEED INDEX {DATE}",
        f"fetched_at_utc: {NOW.isoformat(timespec='seconds')}",
        f"window_utc: {SINCE.isoformat(timespec='minutes')} .. {NOW.isoformat(timespec='minutes')}",
        f"accounts_ok: {total_accounts - len(errors)}/{total_accounts}",
        f"errors: {err_line}",
        f"items_total: {len(items)}",
        f"parts: {len(parts)}",
    ]
    for i, (text, _n) in enumerate(parts, 1):
        index.append(f"part-{i:02d}.md: {count_items(text)} items")
    index_text = "\n".join(index) + "\n"

    (feed_dir / "index.md").write_text(index_text, encoding="utf-8")
    for i, (text, _n) in enumerate(parts, 1):
        header = f"# X-FEED {DATE} part {i}/{len(parts)} | items: {count_items(text)}\n\n"
        (feed_dir / f"part-{i:02d}.md").write_text(header + text, encoding="utf-8")
    for f in feed_dir.glob("*"):
        shutil.copy2(f, latest_dir / f.name)

    payload = {
        "meta": {
            "date": DATE,
            "fetched_at_utc": NOW.isoformat(timespec="seconds"),
            "window_hours": WINDOW_HOURS,
            "accounts_total": total_accounts,
            "errors": errors,
            "items": len(items),
        },
        "items": items,
    }
    (ROOT / "data" / "latest.json").write_text(
        json.dumps(payload, ensure_ascii=False, indent=1), encoding="utf-8"
    )
    shutil.copy2(ROOT / "data" / "latest.json", archive_dir / f"{DATE}.json")

    # Чистка старья, чтобы репозиторий не пух
    feeds = sorted((ROOT / "data" / "feed").glob("20*"))
    for old in feeds[:-KEEP_FEED_DAYS]:
        shutil.rmtree(old, ignore_errors=True)
    archives = sorted(archive_dir.glob("20*.json"))
    for old in archives[:-KEEP_ARCHIVE_DAYS]:
        old.unlink()

    log(f"OK: {len(items)} элементов, {len(parts)} шардов, аккаунтов с ошибками: {len(errors)}")


def selftest_data():
    t0 = (NOW - timedelta(hours=2)).strftime("%a %b %d %H:%M:%S +0000 %Y")
    old = (NOW - timedelta(days=30)).strftime("%a %b %d %H:%M:%S +0000 %Y")
    mk = lambda i, u, txt, **kw: {  # noqa: E731
        "id": str(1947000000000000000 + i), "text": txt, "createdAt": t0,
        "author": {"userName": u}, "conversationId": kw.get("conv", str(1947000000000000000 + i)),
        "likeCount": 100 + i, "retweetCount": 10, "replyCount": 5, "viewCount": 9000,
        "isReply": kw.get("is_reply", False), "inReplyToUsername": kw.get("reply_to"),
        "entities": {"urls": [{"expanded_url": kw["link"]}]} if kw.get("link") else {},
        "retweeted_tweet": kw.get("rt"), "quoted_tweet": kw.get("qt"),
        "url": f"https://x.com/{u}/status/{1947000000000000000 + i}",
    }
    pinned = mk(99, "simonw", "старый закреп — должен отфильтроваться")
    pinned["createdAt"] = old
    return {
        "simonw": [
            pinned,
            mk(1, "simonw", "Разбор нового приёма контекст-инжиниринга", link="https://simonwillison.net/x"),
            mk(2, "simonw", "продолжение треда, часть 2", conv=str(1947000000000000001), is_reply=True, reply_to="simonw"),
            mk(3, "simonw", "ответ незнакомцу — выкинуть", is_reply=True, reply_to="someone"),
        ],
        "karpathy": [mk(4, "karpathy", "Пост с цитатой", qt={"author": {"userName": "lilianweng"}, "text": "оригинал про агентов", "url": "https://x.com/lilianweng/status/1"})],
        "swyx": [mk(5, "swyx", "", rt={"id": "42", "author": {"userName": "rasbt"}, "text": "RT: свежая статья про LoRA", "url": "https://x.com/rasbt/status/42", "likeCount": 500})],
    }


def main():
    handles = [h.strip().lstrip("@") for h in (ROOT / "accounts.txt").read_text().split() if h.strip()]
    log(f"Аккаунтов: {len(handles)}; окно: {WINDOW_HOURS}ч; дата дайджеста: {DATE}")
    if not SELFTEST and not KEY:
        log("FATAL: нет TWITTERAPI_KEY"); sys.exit(1)

    raw_by_user, errors = {}, {}
    if SELFTEST:
        data = selftest_data()
        raw_by_user = {h: [norm(t, h) for t in data.get(h, [])] for h in data}
    else:
        for h in handles:
            try:
                raw_by_user[h] = fetch_user(h)
                log(f"  @{h}: {len(raw_by_user[h])}")
            except Exception as e:  # noqa: BLE001
                errors[h] = str(e)[:120]
                log(f"  @{h}: ОШИБКА {e}")
            time.sleep(0.2)

    handles_lower = {h.lower() for h in handles}
    items, collected_ids = [], set()
    for h, recs in raw_by_user.items():
        kept = [r for r in recs if keep_item(r, handles_lower)]
        for r in kept:
            collected_ids.add(r["id"])
        items.extend(merge_threads(kept))
    items = dedupe_rts(items, collected_ids)

    write_outputs(items, errors, len(handles) if not SELFTEST else len(raw_by_user))

    if not SELFTEST and errors and len(errors) == len(handles):
        log("FATAL: не удался ни один аккаунт (ключ? баланс?)"); sys.exit(1)


if __name__ == "__main__":
    main()
