# X-FEED 2026-07-30 part 4/9 | items: 12

## @lateinteraction — 5 шт.

T=2082569291304431880 | @lateinteraction | 2026-07-29T20:49+00:00 | L132 RT11 C5 V25459 | rt
URL=https://x.com/lateinteraction/status/2082569291304431880
RT-OF @turbopuffer (L132): tpuf now supports late interaction [beta]

use models like ColBERT to represent text as a set of vectors (1 per token)

tpuf uses a single-vector ANN index for a fast first pass, then reranks hits using exact late interaction scoring to boost recall

docs: https://t.co/D0jVyGcx2A https://t.co/y9vQUBJQcg
RT-URL=https://x.com/turbopuffer/status/2082467300142350706
TEXT: RT @turbopuffer: tpuf now supports late interaction [beta]

use models like ColBERT to represent text as a set of vectors (1 per token)

tp…
LINKS: http://turbopuffer.com/docs/query#late-interaction
--
T=2082569387261808774 | @lateinteraction | 2026-07-29T20:50+00:00 | L29 RT1 C1 V3374 | rt
URL=https://x.com/lateinteraction/status/2082569387261808774
RT-OF @antoine_chaffin (L29): I really wonder which model you could plug into this…
RT-URL=https://x.com/antoine_chaffin/status/2082489296775172511
TEXT: RT @antoine_chaffin: I really wonder which model you could plug into this…
--
T=2082569375362478579 | @lateinteraction | 2026-07-29T20:50+00:00 | L99 RT5 C7 V10887 | rt
URL=https://x.com/lateinteraction/status/2082569375362478579
RT-OF @Sirupsen (L99): BM25 (least compute)
sparse vector
regex
dense vector
late interaction (most compute)

we will index every byte. you simply choose how much compute you want to spend indexing, based on your read:write ratio.
RT-URL=https://x.com/Sirupsen/status/2082475482465947940
TEXT: RT @Sirupsen: BM25 (least compute)
sparse vector
regex
dense vector
late interaction (most compute)

we will index every byte. you simply c…
--
T=2082575304975946134 | @lateinteraction | 2026-07-29T21:13+00:00 | L36 RT9 C5 V5541 | rt
URL=https://x.com/lateinteraction/status/2082575304975946134
RT-OF @mixedbreadai (L36): New: mxbai-rerank-v3.1-listwise

An upgrade to our listwise reranker.

→ GPT-5.6-sol (high) ranking quality at 61× the speed
→ up to 54% faster than v3 on long docs

Built for:
- recency-aware ranking
- source-priority resolution
- multi-step composite instructions

Available today in Mixedbread.
RT-URL=https://x.com/mixedbreadai/status/2082476149372772638
TEXT: RT @mixedbreadai: New: mxbai-rerank-v3.1-listwise

An upgrade to our listwise reranker.

→ GPT-5.6-sol (high) ranking quality at 61× the sp…
--
T=2082689553626701839 | @lateinteraction | 2026-07-30T04:47+00:00 | L48 RT6 C5 V4465 | thread(2)
URL=https://x.com/lateinteraction/status/2082689553626701839
TEXT: The answer is deceptively simple imo.

There’s a notion of a general-purpose harness (like, say, CoT reasoning, proper compaction, or an RLM) that’s essentially just what *the* model should become. A better “model” in the API will eventually wrap it and train accordingly.

And a separate notion of a harness that’s last-mile specification over the underlying bland model. This is irreducible to the extent that your task/context diverges from the mode, regardless of capability. Here, the closer your complexity to the minimum number of bits required, the better.
[->] I wrote often on the latter. Recently @a1zhang and I argued that the line between a general harness and neural architectures is rapidly blurring. A trained harness is a non-differentiable architecture that can induce much better generalization properties:

https://t.co/iQ6REuVnpt
QUOTED @martin_casado: On harnesses, I vacillate between three beliefs:

- the less harness, the better. Models are the magic
- post training a model and harness is dramatically better and the model providers win
- harnesses have real independent value from the model

I have no idea which is right.
LINKS: https://alexzhang13.github.io/blog/2026/harness/
--
## @mattpocockuk — 7 шт.

T=2082353644368711707 | @mattpocockuk | 2026-07-29T06:32+00:00 | L852 RT32 C20 V86697 | rt
URL=https://x.com/mattpocockuk/status/2082353644368711707
RT-OF @johnrengwu (L852): i gave @mattpocockuk's /wayfinder skill its own harness, with an interactive star-map you start tickets off of https://t.co/8hM8q7qk47
RT-URL=https://x.com/johnrengwu/status/2082061701856575966
TEXT: RT @johnrengwu: i gave @mattpocockuk's /wayfinder skill its own harness, with an interactive star-map you start tickets off of https://t.co…
--
T=2082418101916741978 | @mattpocockuk | 2026-07-29T10:48+00:00 | L2056 RT57 C129 V176211 | post
URL=https://x.com/mattpocockuk/status/2082418101916741978
TEXT: Fuck I just told my agent it was absolutely right
--
T=2082428884570538345 | @mattpocockuk | 2026-07-29T11:31+00:00 | L638 RT6 C101 V38431 | post
URL=https://x.com/mattpocockuk/status/2082428884570538345
TEXT: Debating adding emojis to /grilling to make handling batches of questions more readable.

You can quickly see the question + recommendation. Much better than trying to squint at a wall of text. https://t.co/bT2DlO8kkT
--
T=2082456028717654525 | @mattpocockuk | 2026-07-29T13:19+00:00 | L293 RT6 C24 V34920 | thread(2)
URL=https://x.com/mattpocockuk/status/2082456028717654525
TEXT: Another absolute BEAST of a spec, produced from doing /to-spec on a /wayfinder map

Do your specs look like this?

https://t.co/rX4KZrhChf
[->] @_Torikh_ We can think of waterfall as just 'planning at the wrong fidelity'

Whereas agile is planning at the right fidelity - with actual working code, adjusting your sails as you go

Wayfinder should feel more like the latter
LINKS: https://github.com/mattpocock/course-video-manager/issues/1455
--
T=2082528210319745433 | @mattpocockuk | 2026-07-29T18:06+00:00 | L416 RT11 C18 V63112 | post
URL=https://x.com/mattpocockuk/status/2082528210319745433
TEXT: I have it on good authority that sales of A Philosophy Of Software Design have skyrocketed recently

Long may it continue, @JohnOusterhout
QUOTED @unclebobmartin: People keep on telling me that my message about AI is undercutting my own books.  Those people do not understand how agents work and who actually controls them.  You can't tell an agent to be clean.  You have to measure the cleanliness that they produce and have them correct failures of cleanliness.  

Without such constraints agents are more than happy to build big balls of mud that they can't maintain.
--
T=2082545875922882718 | @mattpocockuk | 2026-07-29T19:16+00:00 | L245 RT5 C25 V21207 | post
URL=https://x.com/mattpocockuk/status/2082545875922882718
TEXT: Now I've got all of my 'input' work channels syncing into a private wiki

The next obvious step is to have an agent control my calendar

Starting tomorrow, I'm doing a daily morning standup to plan my whole week

Powered by a custom CLI + a month's worth of wiki data

LFG
--
T=2082562900258852901 | @mattpocockuk | 2026-07-29T20:24+00:00 | L384 RT10 C17 V21845 | post
URL=https://x.com/mattpocockuk/status/2082562900258852901
TEXT: Added icons to my custom @tldraw diagram app

Funny how a small thing makes a big difference https://t.co/tjF5VZd9Ii
--
