# X-FEED 2026-09-09 part 7/11 | items: 12

## @lateinteraction — 11 шт.

T=2097383244551364700 | @lateinteraction | 2026-09-08T17:55+00:00 | L59 RT1 C6 V2960 | post
URL=https://x.com/lateinteraction/status/2097383244551364700
TEXT: i think i got it - is the trick in the Luna, Terra, Sol, Astra sequence that

the next major model release will be GPT-7 Galaxy Brain https://t.co/sGSjw9xPYd
--
T=2097416253849649558 | @lateinteraction | 2026-09-08T20:06+00:00 | L107 RT3 C1 V16806 | post
URL=https://x.com/lateinteraction/status/2097416253849649558
TEXT: what did jacob see 3d ago
QUOTED @jacobli99: @nurijunsu Navier stokes
--
T=2097417382545244438 | @lateinteraction | 2026-09-08T20:10+00:00 | L68 RT2 C0 V12801 | rt
URL=https://x.com/lateinteraction/status/2097417382545244438
RT-OF @a1zhang (L68): this is so cool!
RT-URL=https://x.com/a1zhang/status/2097405871403753877
TEXT: RT @a1zhang: this is so cool!
--
T=2097424881746939934 | @lateinteraction | 2026-09-08T20:40+00:00 | L38 RT2 C3 V2422 | rt
URL=https://x.com/lateinteraction/status/2097424881746939934
RT-OF @jacobli99 (L38): https://t.co/OtoKp6kIRJ
RT-URL=https://x.com/jacobli99/status/2097385373429105090
TEXT: RT @jacobli99: https://t.co/OtoKp6kIRJ
--
T=2097424844681871660 | @lateinteraction | 2026-09-08T20:40+00:00 | L296 RT9 C10 V33465 | rt
URL=https://x.com/lateinteraction/status/2097424844681871660
RT-OF @xeophon (L296): astra is so obviously trained to be a rlm
RT-URL=https://x.com/xeophon/status/2097224530225721451
TEXT: RT @xeophon: astra is so obviously trained to be a rlm
--
T=2097447020415832392 | @lateinteraction | 2026-09-08T22:08+00:00 | L835 RT94 C34 V84266 | rt
URL=https://x.com/lateinteraction/status/2097447020415832392
RT-OF @johnschulman2 (L835): This isn't the most notable aspect of today's news, but on the user data issue, there are different kinds of *training on user data* with very different privacy/IP implications. Sadly, AI cos don't like to disclose what they're doing.

- pretrain on user data, with users' tokens as prediction targets: high regurgitation risk, improper
- use user prompts to distill large models into small ones: low regurg. risk, some companies probably do this
- use user traces to construct RL tasks: low regurg. risk, because RL has low memorization abilities, but can extract customer IP, depending on how it's done. Ranges from benign "use explicit user feedback in reward model training" to invasive "upload user's coding environment and commit history to turn into rl envs"

"De-identification" is weak -- you can identify someone with a small number of bits, and long traces have more than enough. And it doesn't affect IP leakage concerns.
RT-URL=https://x.com/johnschulman2/status/2097440545853637108
TEXT: RT @johnschulman2: This isn't the most notable aspect of today's news, but on the user data issue, there are different kinds of *training o…
--
T=2097447702808195550 | @lateinteraction | 2026-09-08T22:11+00:00 | L358 RT33 C11 V45937 | rt
URL=https://x.com/lateinteraction/status/2097447702808195550
RT-OF @harvey (L358): We partnered with @baseten to post-train recursive language model (RLM) agents for M&A diligence.

We found that model-harness co-optimization meaningfully improves agent performance in long-horizon environments, bringing us closer to agents that can complete M&A diligence end-to-end.

We started by building an RLM harness that lets a root agent search a data room, delegate document review to sub-agents, and orchestrate the sub-agents' work to produce a final diligence memo.

By distributing document review across sub-agents, the RLM harness can work through thousands of documents in data rooms containing up to 80M tokens.

On LAB Diligence, our synthetic M&A diligence benchmark, the RLM harness raised average rubric criteria pass rate across models from 23% to 62%.

Despite the root agent processing just 1-4% of the tokens in diligence (with sub-agents processing 96-99%), the choice of root agent had a much larger effect on performance than choice of sub-agents.

This led us to focus on the root agent, training two models separately to improve diligence performance.

First, we trained a GLM-5.2 root model in the RLM harness using self-distillation SFT. We selected GLM-5.2 diligence runs with high data room coverage and fine-tuned the model on these trajectories. This increased benchmark performance from 46% to 60%.

Second, we trained a base Qwen3.5-122B-A10B using GRPO within the RLM harness, keeping the sub-agent models fixed. This raised rubric criteria pass rate from 30% to 63% on 50 held-out data rooms.

In both cases we saw major qualitative shifts in agent behavior. The trained root agent learned to delegate more thoroughly and write its memo incrementally as sub-agent findings came back. Data room coverage rose from 62% to 96%. And the root agent learned to scale the size of its agent team proportionally to the size of the data room.

We are now scaling RL training with GLM-5.3, a frontier open-weight model, as the root agent. A small amount of training giv
RT-URL=https://x.com/harvey/status/2097372371195953272
TEXT: RT @harvey: We partnered with @baseten to post-train recursive language model (RLM) agents for M&amp;A diligence.

We found that model-harness…
--
T=2097456782306054403 | @lateinteraction | 2026-09-08T22:47+00:00 | L17 RT4 C1 V1342 | rt
URL=https://x.com/lateinteraction/status/2097456782306054403
RT-OF @dbreunig (L17): Can't wait to share how I'm using DSPy to optimize MCP tool use…

GPT-5.6-Luna continually fumbles many Playwright calls, as they're defined. Just a bit of optimization rewrites the tool guidance for runs with zero errors. Join us! https://t.co/3qcdEI05xm https://t.co/ImL5rbi8Q8
RT-URL=https://x.com/dbreunig/status/2097443925535690793
TEXT: RT @dbreunig: Can't wait to share how I'm using DSPy to optimize MCP tool use…

GPT-5.6-Luna continually fumbles many Playwright calls, as…
LINKS: https://globalai.community/e/bay9vh24
--
T=2097473698739466290 | @lateinteraction | 2026-09-08T23:54+00:00 | L131 RT15 C5 V30724 | rt
URL=https://x.com/lateinteraction/status/2097473698739466290
RT-OF @nikogrupen (L131): Model-harness co-optimization is helping us solve end-to-end legal use cases like M&A diligence.

Together with @baseten and @baselabs, we built an RLM harness for M&A Diligence and are sharing initial results from post-training on top of it.

The RLM harness lets a root agent delegate document review to sub-agents and aggregates their findings. 

A few initial results to highlight that we ran over LAB Diligence tasks:

1. Harness design — Across seven models, moving from a standard tool loop to our RLM harness increased mean criteria pass rate from 23.3% to 62.4%.

2. Post-training — In a separate experiment, RL over Qwen3.5 in the RLM harness more than doubled rubric pass rate, from 29.9% to 63.0%, and increased document review coverage from 62% to 96%. This makes the much smaller Qwen 3.5 competitive with the closed frontier in the RLM harness.

We’re now doing a scaled  RL run with GLM-5.3 and are excited about the potential to bring more capable models closer to completing these tasks end to end.

Thanks to @oneill_c @mudithj and the @baseten @baselabs teams for the collab here!
RT-URL=https://x.com/nikogrupen/status/2097370187674869803
TEXT: RT @nikogrupen: Model-harness co-optimization is helping us solve end-to-end legal use cases like M&amp;A diligence.

Together with @baseten an…
--
T=2097473680674545749 | @lateinteraction | 2026-09-08T23:54+00:00 | L181 RT18 C9 V146022 | rt
URL=https://x.com/lateinteraction/status/2097473680674545749
RT-OF @nikogrupen (L181): https://t.co/Fg8FniKQv3
RT-URL=https://x.com/nikogrupen/status/2097369705791307952
TEXT: RT @nikogrupen: https://t.co/Fg8FniKQv3
LINKS: https://x.com/i/article/2097344107303825408
--
T=2097474690075799897 | @lateinteraction | 2026-09-08T23:58+00:00 | L132 RT10 C12 V9750 | rt
URL=https://x.com/lateinteraction/status/2097474690075799897
RT-OF @mervenoyann (L132): training open model agents is here to stay 
if you want the moat 🙌🏻

"We post-trained a Qwen3.5-122B-A10B orchestrator and found that post-training increased rubric criteria pass rate from 29.9% to 63.0% on 50 held-out LAB Diligence data rooms." 
outperforms Claude Code &amp; Codex https://t.co/f1SOePpGAi
RT-URL=https://x.com/mervenoyann/status/2097420163968635113
TEXT: RT @mervenoyann: training open model agents is here to stay 
if you want the moat 🙌🏻

"We post-trained a Qwen3.5-122B-A10B orchestrator and…
--
## @mattpocockuk — 1 шт.

T=2097238983226868194 | @mattpocockuk | 2026-09-08T08:21+00:00 | L2571 RT69 C138 V107746 | post
URL=https://x.com/mattpocockuk/status/2097238983226868194
TEXT: If you give me a drawer, I will eventually fill it with cables

If you give an agent a markdown file, it will eventually fill it with:

- unnecessary implementation details
- session-specific observations
- stale docs
--
