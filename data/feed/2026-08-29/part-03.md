# X-FEED 2026-08-29 part 3/4 | items: 11

## @mitchellh — 2 шт.

T=2093451043661316217 | @mitchellh | 2026-08-28T21:29+00:00 | L4034 RT159 C230 V307630 | post
URL=https://x.com/mitchellh/status/2093451043661316217
TEXT: Quick Superlogical demo to end the week. This demo is just of the basic functionality, but I want to highlight just how FAST it is. There's a WHOLE lot more functionality already present and coming but I wanted to keep the demo short. But seriously, check out that speed.

I'm showing the macOS app here and I get asked a lot so let me just say up front: its not macOS only. We're still figuring out exactly what platforms will be stable enough for the initial public release, but we're working on others. In particular, the web interface is very functional but I'll demo that another time (or someone else will).

This is also all showing off the architecture I previously talked about for terminal multiplexing which is significantly different from other mainstream multiplexers: this is all a custom binary protocol where the server is maintaining N replica distributed terminal state machines. It works!

Tons of hard work going into this by the team @almonk @dizzyup @pearkes. Hope we can bring you something you can use soon. ❤️ Happy to answer questions in the replies.
--
T=2093456226810200230 | @mitchellh | 2026-08-28T21:50+00:00 | L1918 RT31 C115 V95518 | post
URL=https://x.com/mitchellh/status/2093456226810200230
TEXT: I can't tell you the number of people over my career that have said "I tried learning tmux" First problem: the fact you have to "learn it" at all. The world's best multiplexer is the one you don't have to learn. It just works. That's what we're building (and then some 😜).
--
## @mitsuhiko — 3 шт.

T=2093370895347642445 | @mitsuhiko | 2026-08-28T16:11+00:00 | L147 RT6 C13 V28045 | post
URL=https://x.com/mitsuhiko/status/2093370895347642445
TEXT: Friends don’t let friends use httpx. https://t.co/V4S2cWap1G
LINKS: https://github.com/openai/openai-python/blob/main/httpx2.md
--
T=2093626687950930019 | @mitsuhiko | 2026-08-29T09:07+00:00 | L7 RT0 C2 V2890 | post
URL=https://x.com/mitsuhiko/status/2093626687950930019
TEXT: Even after all that time, I still cannot stand #foo to mark a private elements in JavaScript. Also doesn't help that plenty of syntax highlighters do not mark the # as part of the name.
--
T=2093637297354748219 | @mitsuhiko | 2026-08-29T09:50+00:00 | L7 RT0 C1 V688 | post
URL=https://x.com/mitsuhiko/status/2093637297354748219
TEXT: Debian voted to neither reject or endorse LLMs. Seems sensible? https://t.co/AQO4dt4rlW
LINKS: https://www.debian.org/vote/2026/vote_002#texte
--
## @omarsar0 — 5 шт.

T=2093309547154649519 | @omarsar0 | 2026-08-28T12:07+00:00 | L48 RT3 C21 V9437 | thread(2)
URL=https://x.com/omarsar0/status/2093309547154649519
TEXT: The more I embrace open and cheaper models, the more automation I can afford.

Frontier models for orchestration and coordination. 

Open and cheaper models for execution. Token usage rapidly increasing here.

This allows me to lean more into proactive agents like never before.
[->] This is why I continue to be excited about the progress around tiny open models. I have experimented with this a lot over the past year, and for most tasks you really don't need the most capable models.
--
T=2093323034195378306 | @omarsar0 | 2026-08-28T13:01+00:00 | L320 RT49 C16 V32531 | post
URL=https://x.com/omarsar0/status/2093323034195378306
TEXT: Impressive new paper from Google DeepMind.

(bookmark it)

It takes Co-Scientist out of simulation and into real-world experiments.

A summary of the results:

In computer science, it found an inference-time scaling architecture that beat six frontier models on HealthBench Hard and Professional under blinded physician review.

The system designed a safe precursor route for MXenes and drove a semi-automated chemical vapor deposition reactor, producing a lamellar 2D material with structural similarities to the Ti3C2Tx lattice.

It also tailored growth recipes to laboratory constraints in minutes, enabling single-attempt growth of monolayer MoS2, MoSe2, and WS2. In biology, it predicted E. coli swarming phenotypes across inducer gradients from sparse imaging data, matching unpublished real-world measurements.

30 domain experts wrote 450 reviews on end-to-end generated papers, and the reliability modules reduced hallucination and plagiarism.

Paper: https://t.co/M2NHPCJ5so

Chat with Paper: https://t.co/JlWJLDnaUv
LINKS: https://arxiv.org/abs/2608.26701 ; https://academy.dair.ai/papers/co-scientist-runs-closed-loop-experiments-in-real-labs-2608.26701
--
T=2093325637821878575 | @omarsar0 | 2026-08-28T13:11+00:00 | L106 RT11 C11 V22310 | post
URL=https://x.com/omarsar0/status/2093325637821878575
TEXT: A great paper from Google on maintaining agent skills through persistent knowledge.
QUOTED @dair_ai: Banger paper from Google.

If you maintain a skill library for your agents, you might want to check this out.

(bookmark it)

This work separates three things that skill-evolution systems usually collapse into one. Raw execution traces, a persistent wiki of accumulated knowledge, and the executable skills themselves.

Experience gets consolidated into the wiki, and every later skill update builds on that wiki instead of on a scattered optimization history.

Ablations confirm the wiki is what car
--
T=2093350462229487760 | @omarsar0 | 2026-08-28T14:50+00:00 | L188 RT20 C17 V15321 | post
URL=https://x.com/omarsar0/status/2093350462229487760
TEXT: The DeepSeek harness is engineering at its finest. 

202K stars on GitHub. Damn!

Clearly, they built this harness with future AI needs and capabilities in mind. 

Everything is a plugin and customizable, which is exactly how harnesses of the future need to be. https://t.co/pLSGtIuDR8
--
T=2093437178386747657 | @omarsar0 | 2026-08-28T20:34+00:00 | L2962 RT248 C63 V277709 | rt
URL=https://x.com/omarsar0/status/2093437178386747657
RT-OF @dair_ai (L2962): Banger paper from Google.

If you maintain a skill library for your agents, you might want to check this out.

(bookmark it)

This work separates three things that skill-evolution systems usually collapse into one. Raw execution traces, a persistent wiki of accumulated knowledge, and the executable skills themselves.

Experience gets consolidated into the wiki, and every later skill update builds on that wiki instead of on a scattered optimization history.

Ablations confirm the wiki is what carries a lot of the gain. Two results stand out in particular. Smaller models with evolved skills beat substantially larger models without them. And skills evolved by one model transfer across families, where skills evolved elsewhere sometimes beat self-evolved ones.

Paper: https://t.co/6qftGirTpE

Chat with Paper: https://t.co/rrVzkkR1ij
RT-URL=https://x.com/dair_ai/status/2093324233158045788
TEXT: RT @dair_ai: Banger paper from Google.

If you maintain a skill library for your agents, you might want to check this out.

(bookmark it)…
LINKS: https://arxiv.org/abs/2608.27454 ; https://academy.dair.ai/papers/wikiskill-compiles-agent-experience-into-a-persistent-wiki-2608.27454
--
## @RLanceMartin — 1 шт.

T=2093544453160186112 | @RLanceMartin | 2026-08-29T03:41+00:00 | L5683 RT267 C285 V2276826 | rt
URL=https://x.com/RLanceMartin/status/2093544453160186112
RT-OF @NotTomBrown (L5683): Cursor has been a trusted partner of Anthropic since Sonnet 3.5. We’ll continue to increase compute to support Claude models in Cursor and are excited for what comes next with them at SpaceX.
RT-URL=https://x.com/NotTomBrown/status/2093541294027280657
TEXT: RT @NotTomBrown: Cursor has been a trusted partner of Anthropic since Sonnet 3.5. We’ll continue to increase compute to support Claude mode…
--
