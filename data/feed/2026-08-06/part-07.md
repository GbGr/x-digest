# X-FEED 2026-08-06 part 7/12 | items: 15

## @mattpocockuk (продолжение)

T=2085064808374644880 | @mattpocockuk | 2026-08-05T18:06+00:00 | L441 RT17 C38 V82928 | thread(2)
URL=https://x.com/mattpocockuk/status/2085064808374644880
TEXT: FYI someone seems to be pretending to be an official npm package of my skills

Avoid at all costs

If this is you, DM me and we can figure it out

https://t.co/naCTPbcTGR
[->] @rcssdy I work out

how to write good markdown files
LINKS: https://www.npmjs.com/package/mattpocock-skills
--
T=2085100222175178965 | @mattpocockuk | 2026-08-05T20:26+00:00 | L28 RT0 C2 V2364 | post
URL=https://x.com/mattpocockuk/status/2085100222175178965
TEXT: @trashh_dev Let me show you

We never actually ended up streaming together, did we
--
## @mitchellh — 6 шт.

T=2085034829318656113 | @mitchellh | 2026-08-05T16:06+00:00 | L933 RT42 C55 V97131 | thread(2)
URL=https://x.com/mitchellh/status/2085034829318656113
TEXT: Been fighting the Great Firewall of America all day (Fable too, though this screenshot is from Codex). I truly believe this is resulting in software being less secure because we can't find and fix security issues in our own software that we control without a bunch of red tape. https://t.co/2cXIw0Wcqr
[->] @CadamSAFC Doing it now. I always was turned off by the huge form that I figured put me into some slow queue.
--
T=2085035369977049281 | @mitchellh | 2026-08-05T16:09+00:00 | L358 RT5 C22 V39057 | post
URL=https://x.com/mitchellh/status/2085035369977049281
TEXT: In many cases working around this is rather trivial, albeit annoying, which further reinforces my point this is dumb. I'm not going to share my specific tactics but through simple word replacement and social engineering (the agent), I've gotten around this almost every time.
QUOTED @mitchellh: Been fighting the Great Firewall of America all day (Fable too, though this screenshot is from Codex). I truly believe this is resulting in software being less secure because we can't find and fix security issues in our own software that we control without a bunch of red tape. https://t.co/2cXIw0Wcqr
--
T=2085039951184597411 | @mitchellh | 2026-08-05T16:27+00:00 | L26 RT0 C1 V3569 | post
URL=https://x.com/mitchellh/status/2085039951184597411
TEXT: @teej_m I haven't seen this happen yet but that sounds pretty fucking awful lol.
--
T=2085051815746560013 | @mitchellh | 2026-08-05T17:14+00:00 | L2 RT0 C0 V131 | post
URL=https://x.com/mitchellh/status/2085051815746560013
TEXT: @RobKnight__ @bitwise0X2A Tmux itself doesn't so it can't unless they forked it. Ghostty supports unicode placeholders (the only terminal other than Kitty too) so compliant Kitty graphics producing applications can use that and it works. https://t.co/xxZrezr7Fj
LINKS: https://sw.kovidgoyal.net/kitty/graphics-protocol/#unicode-placeholders
--
T=2085063661685711290 | @mitchellh | 2026-08-05T18:01+00:00 | L366 RT9 C12 V21253 | thread(2)
URL=https://x.com/mitchellh/status/2085063661685711290
TEXT: OSC8 is the terminal sequence for linking arbitrary text (similar to `a` tags in HTML). It is mandatory for a modern terminal experience but prone to malicious use. The next version of Ghostty contains the strongest protections for malicious OSC8 short of disabling it entirely.

In the next version of Ghostty, we've added a classifier for OSC8 URLs (any hidden URL, really) that classifies a URL as: trusted, requires-confirmation, or deny. The screenshots below show the separate requires-confirmation and deny alerts.

We also now show hidden characters in the URL preview in the bottom of the window (previously we interpreted the Unicode directly which allowed maliciously crafted URLs to hide themselves). Hidden characters immediately trigger the `deny` classification, too.

These are the strongest, most comprehensive protections for OSC8 across terminals. As a comparison:

* Alacritty, Kitty, iTerm2, WezTerm: enabled by default with zero filtering at all. Can directly open executables or maliciously crafted schemes without any filter. Can hide the real URL through Unicode tricks.

* Gnome Terminal: enables all OSC8, no configuration I could find to disable. Only rejects remote-host `file://` URLs. No other sanitization, confirmation, etc.

* VS Code Terminal: Allowlist of safe protocols, prompts for unknown, silently replaces whitespace characters. Very good!

* Windows Terminal: Allowlist, prompts for anything executable, prompts for any custom schemes. Very good!
[->] @omengue All http/https is trusted since the preview is visible and browsers have their own security barriers. Local files are trusted if they're non-executable and readable and advertise a text format. etc.
--
T=2085197661599306206 | @mitchellh | 2026-08-06T02:53+00:00 | L2 RT0 C0 V1523 | post
URL=https://x.com/mitchellh/status/2085197661599306206
TEXT: @i0n1c GitHub security advisory for now
--
## @mitsuhiko — 7 шт.

T=2084959293493719177 | @mitsuhiko | 2026-08-05T11:06+00:00 | L1 RT0 C0 V333 | post
URL=https://x.com/mitsuhiko/status/2084959293493719177
TEXT: @michael_timbs Has to be WASM given how workers work
--
T=2084991499851169996 | @mitsuhiko | 2026-08-05T13:14+00:00 | L21 RT0 C5 V6316 | thread(3)
URL=https://x.com/mitsuhiko/status/2084991499851169996
TEXT: @steipete It’s unclear what exactly codex does differently
[->] @steipete I keep looking into Codex all the time to figure out if there is something that applies to Pi and it's very hard to say. My expectation is that a model does not need extra nudges to actually start doing work, regardless of the stuff the harness stuffs into it.
[->] @__tosh Happens with all of them. Yes I have traces, but they are not really useful. There is no signal in them from what I can tell
--
T=2085026634394976293 | @mitsuhiko | 2026-08-05T15:34+00:00 | L83 RT1 C10 V7116 | post
URL=https://x.com/mitsuhiko/status/2085026634394976293
TEXT: Watching Sol trying to figure out why Pi is laggy on Windows is fun. Apparently it found out how to open more Windows Terminal windows, but not sure it has any clue what it's doing. https://t.co/72Y4zVqRaM
--
T=2085040549661212864 | @mitsuhiko | 2026-08-05T16:29+00:00 | L354 RT10 C6 V32251 | post
URL=https://x.com/mitsuhiko/status/2085040549661212864
TEXT: The rust project continues to be reasonable. Much more reasonable than you would think if you read people’s opinions of Rust on this hellsite.
QUOTED @AstraKernel: 🦀 rust-lang/rust is adopting an LLM policy

&gt; Because Rust governance doesn't work that way. We do not have a benevolent dictator who can say "No LLM-generated content, whether it be code or prose." or "AI is a tool, just like other tools we use"

https://t.co/yNDNjAIG3w
--
T=2085042868700209313 | @mitsuhiko | 2026-08-05T16:38+00:00 | L78 RT1 C9 V4637 | post
URL=https://x.com/mitsuhiko/status/2085042868700209313
TEXT: https://t.co/JO3sqzFNqI
--
T=2085057846413062240 | @mitsuhiko | 2026-08-05T17:38+00:00 | L50 RT0 C5 V5536 | post
URL=https://x.com/mitsuhiko/status/2085057846413062240
TEXT: @HamelHusain Use handy
--
T=2085085592262451544 | @mitsuhiko | 2026-08-05T19:28+00:00 | L18 RT0 C5 V9159 | post
URL=https://x.com/mitsuhiko/status/2085085592262451544
TEXT: I still hold that opinion. https://t.co/wKK8LymoL4
QUOTED @mitsuhiko: IMO XDG and following platform standards for config files for dev tools is horrible. It drives up complexities for everybody (now you need to update scripts, docs etc. for all platforms). Wish that standard would never have happened.
LINKS: https://x.com/mitsuhiko/status/2046492175190351921?s=20
--
