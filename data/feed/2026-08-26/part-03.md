# X-FEED 2026-08-26 part 3/7 | items: 10

## @lateinteraction — 8 шт.

T=2092091320256885120 | @lateinteraction | 2026-08-25T03:26+00:00 | L18 RT3 C0 V1786 | rt
URL=https://x.com/lateinteraction/status/2092091320256885120
RT-OF @ManningBooks (L18): Prompt optimization is one thing in theory. What happens when you actually put it to work?

On Sept. 7th, Serj Smorodinsky and Brett Kennedy, authors of Building LLM Applications with DSPy, are going hands-on with @DSPyOSS and coding agents. They'll be writing code, running experiments, and optimizing prompts live.

Register for the 11am ET event: https://t.co/Jv1o6C1A8S
RT-URL=https://x.com/ManningBooks/status/2091956430676938757
TEXT: RT @ManningBooks: Prompt optimization is one thing in theory. What happens when you actually put it to work?

On Sept. 7th, Serj Smorodinsk…
LINKS: https://hubs.la/Q04v4n3b0
--
T=2092205085556158692 | @lateinteraction | 2026-08-25T10:58+00:00 | L41 RT8 C0 V2694 | rt
URL=https://x.com/lateinteraction/status/2092205085556158692
RT-OF @_reachsumit (L41): Chimera: Efficient Multi-Vector Retrieval via GPU-CPU Co-Processing

Introduces a GPU-CPU system that skips vector transfer at query time, reaching up to 16x higher throughput than prior GPU retrieval systems.

📝 https://t.co/BMgGkTbYEn
👨🏽‍💻 https://t.co/k85cBkjSPm
RT-URL=https://x.com/_reachsumit/status/2092133495888113974
TEXT: RT @_reachsumit: Chimera: Efficient Multi-Vector Retrieval via GPU-CPU Co-Processing

Introduces a GPU-CPU system that skips vector transfe…
LINKS: https://arxiv.org/abs/2608.23553 ; https://github.com/iidyc/Chimera
--
T=2092204990194397642 | @lateinteraction | 2026-08-25T10:58+00:00 | L132 RT22 C0 V37161 | rt
URL=https://x.com/lateinteraction/status/2092204990194397642
RT-OF @_reachsumit (L132): Retrieval Needs Multivectors: An Exponential Separation

Microsoft formally proves that multi-vector embeddings can be exponentially more compact than single-vector ones for ranking documents.

📝 https://t.co/fiqz4dBR2B
RT-URL=https://x.com/_reachsumit/status/2092133369467547734
TEXT: RT @_reachsumit: Retrieval Needs Multivectors: An Exponential Separation

Microsoft formally proves that multi-vector embeddings can be exp…
LINKS: https://arxiv.org/abs/2608.21494
--
T=2092226396709937254 | @lateinteraction | 2026-08-25T12:23+00:00 | L287 RT16 C8 V27888 | thread(3)
URL=https://x.com/lateinteraction/status/2092226396709937254
TEXT: Allow me to say that retrieval is the only ML problem in which we still cling to the assumption that an inert scoring function (a meager dot product!), which couples your “search-time compute” with the dimensionality of the representation, can be sensible.

Who would have guessed this forces you to have exponentially larger embeddings just to do basic things. Instead, if this makes it sound more modern, you need “inference scaling for retrieval”, also known as late interaction from 2019/2020:
[->] imo a significant part of the problem is the insistence of the community on misnaming the paradigm as “multi-vector retrieval”, we called it late interaction for a reason

the problem isn’t in having one vector; the problem is in the scoring function!

https://t.co/QupzaHoiSd
[->] @tomaarsen Because of this, "as index size shrinks" is not quite meaningful. For typical applications, a very standard PLAID index is already smaller or roughly as big than the >4000-dim single-vector representations most people use today. The problem is diffusion of good infra, not a technical challenge.

ST might be a great case study. Understanding why ST is not PLAID-native (or WARP-native, or TACHIOM-native for that matter) might shed some light on the underlying reason.
QUOTED @_reachsumit: Retrieval Needs Multivectors: An Exponential Separation

Microsoft formally proves that multi-vector embeddings can be exponentially more compact than single-vector ones for ranking documents.

📝 https://t.co/fiqz4dBR2B
LINKS: https://youtu.be/Z2TmdcylyEc?si=hrtqsEUa6Lh2UxlW
--
T=2092361701584707696 | @lateinteraction | 2026-08-25T21:21+00:00 | L10 RT1 C2 V1544 | rt
URL=https://x.com/lateinteraction/status/2092361701584707696
RT-OF @Julian_a42f9a (L10): Glad to see continued work on the theory supporting Late-Interaction/Multi-Vector as more powerful than inner product. If you’re interested in this kind of work you should checkout our paper: Quantifying and Expanding the Theoretical Capacity of Late-Interaction Retrieval Models.
RT-URL=https://x.com/Julian_a42f9a/status/2092360775893655632
TEXT: RT @Julian_a42f9a: Glad to see continued work on the theory supporting Late-Interaction/Multi-Vector as more powerful than inner product. I…
--
T=2092361674405626158 | @lateinteraction | 2026-08-25T21:21+00:00 | L18 RT2 C4 V1784 | rt
URL=https://x.com/lateinteraction/status/2092361674405626158
RT-OF @SilvioMartinico (L18): Keep scaling multivector once I'm done with some other stuff 🤓
RT-URL=https://x.com/SilvioMartinico/status/2092232159377391898
TEXT: RT @SilvioMartinico: Keep scaling multivector once I'm done with some other stuff 🤓
--
T=2092361657641054632 | @lateinteraction | 2026-08-25T21:21+00:00 | L34 RT2 C2 V3445 | rt
URL=https://x.com/lateinteraction/status/2092361657641054632
RT-OF @aaxsh18 (L34): we do not only need multi vector storage, we also need the model. at mixedbread we saw the first time something like scaling laws working for retrieval and went all in into late interaction. we build our vector db silo around late interaction with the co-design of our li retrieval model wholembed.
RT-URL=https://x.com/aaxsh18/status/2092297534379352501
TEXT: RT @aaxsh18: we do not only need multi vector storage, we also need the model. at mixedbread we saw the first time something like scaling l…
--
T=2092400270596583679 | @lateinteraction | 2026-08-25T23:54+00:00 | L86 RT3 C11 V6282 | post
URL=https://x.com/lateinteraction/status/2092400270596583679
TEXT: ok fine, just for fun and after years of realizing how much inertia exists even in 'fast-moving' ML of all places, i'm taking matters into my own (codex?) hands.. stay tuned
QUOTED @lateinteraction: Allow me to say that retrieval is the only ML problem in which we still cling to the assumption that an inert scoring function (a meager dot product!), which couples your “search-time compute” with the dimensionality of the representation, can be sensible.

Who would have guessed this forces you to have exponentially larger embeddings just to do basic things. Instead, if this makes it sound more modern, you need “inference scaling for retrieval”, also known as late interaction from 2019/2020:
--
## @mattpocockuk — 2 шт.

T=2092173181075223016 | @mattpocockuk | 2026-08-25T08:52+00:00 | L367 RT6 C98 V64536 | post
URL=https://x.com/mattpocockuk/status/2092173181075223016
TEXT: Anyone using Codex/Copilot CLI

Do you guys have tricks you use to shrink the built-in system prompt?

Claude Code gives you some levers you can pull - disabling built-in tools and features.

Does Codex/Copilot have the same?
--
T=2092221475881140713 | @mattpocockuk | 2026-08-25T12:04+00:00 | L415 RT7 C19 V33817 | post
URL=https://x.com/mattpocockuk/status/2092221475881140713
TEXT: FYI if you need to build any automations around new skill releases from me...

My skills have an RSS feed:

https://t.co/M3zbnNZOeA
LINKS: https://www.aihero.dev/skills/rss.xml
--
