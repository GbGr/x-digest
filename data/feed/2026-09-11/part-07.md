# X-FEED 2026-09-11 part 7/9 | items: 8

## @omarsar0 (продолжение)

T=2098112753659527254 | @omarsar0 | 2026-09-10T18:13+00:00 | L9 RT1 C3 V7779 | post
URL=https://x.com/omarsar0/status/2098112753659527254
TEXT: Interesting read on how Pocket FM scaled.

Pocket FM makes serialized audio fiction. AI now writes and voices much of it, taking annual output past 2.5M hours.

Daily listening time went from ~25 mins to >150 mins.

More than 500,000 people now write on the platform, and a lot of them started as listeners.
QUOTED @RohanNayak2: We grew from ~0 to $500M ARR, adding $250M last year alone while being EBITDA profitable.

1,300-word post on every growth tactic that worked for us:

1. What got us from 0-$400M ARR in the US works in every country.
2. Retention and Monetisation Hacks.
3. Localization > Translation.
4. Experiment with $1M internal seed checks.
5. Pivoting to only AI content production unlocked 100% ARR growth.

Pocket FM is like Netflix for audio-only dramas, with our own pool of one-person studios.

1. Acquisi
--
T=2098113750377087266 | @omarsar0 | 2026-09-10T18:17+00:00 | L34 RT3 C3 V4346 | rt
URL=https://x.com/omarsar0/status/2098113750377087266
RT-OF @dair_ai (L34): Recommended read. Interaction horizon scheduling is an underexplored control problem in agentic RL

This paper from the Qwen team takes a closer look at the problem.

Scaling the maximum number of environment interactions per episode improves long-horizon agents, and curriculum methods that expand the horizon beat fixed-horizon training.

But those schedules are open-loop.

They increase monotonically to a manually specified maximum with no way to detect that expansion stopped helping.

The authors propose the effective interaction frontier, a dynamic boundary past which extra interactions give diminishing returns while cost keeps growing linearly. Fixed-horizon sweeps on AppWorld and BFCL show clear saturation plateaus.

Elastic Horizon is a closed-loop controller that tracks the boundary using the 90th percentile of successful trajectory lengths, a statistic already available during training.

It settles inside the saturation band from both under-capacity and over-capacity starts, gets the best success rates across 7B and 14B backbones, and saves up to 25% of per-step trajectory tokens.

Paper: https://t.co/VEVaFn8K8y
RT-URL=https://x.com/dair_ai/status/2098109386568925397
TEXT: RT @dair_ai: Recommended read. Interaction horizon scheduling is an underexplored control problem in agentic RL

This paper from the Qwen t…
LINKS: https://academy.dair.ai/papers/elastic-horizon-discovering-the-effective-interaction-frontier-in-agentic-reinfo-2609.07247
--
T=2098140712504332411 | @omarsar0 | 2026-09-10T20:05+00:00 | L110 RT22 C14 V9461 | post
URL=https://x.com/omarsar0/status/2098140712504332411
TEXT: This is a brilliant paper.

It's of the cleanest long-context agent designs I have seen in the past couple of months.

Sequential memory agents read chunks one after another while maintaining a compact memory state.

This behavior ties reasoning depth to document traversal and makes accuracy sensitive to where the evidence sits. It also makes latency grow linearly with document length.

PARSER decouples the two.

A bank of lightweight subagents, each bound to a single chunk, reads the whole document in parallel.

A lead agent reasons through iterative scatter-gather rounds, broadcasting a query to all subagents, aggregating the returned evidence, and forming a deeper follow-up query conditioned on what it has found.

All the learnable behavior is build into the lead agent, which is trained with RL. The subagents stay frozen off-the-shelf models.

On multi-hop QA from 7K to 896K tokens, a 4B PARSER beats the strongest sequential memory baseline by 5.7 points on average and 12.0 points at 896K. At 9B it passes DeepSeek-V4-Pro by 6.3 points.

Controlled experiments show it holds up under perturbations to evidence position, order and distance, which cause large accuracy swings in sequential methods, while cutting inference latency by up to 11x.

Paper: https://t.co/lpCsLALdDv
LINKS: https://academy.dair.ai/papers/parser-read-in-parallel-reason-in-depth-for-long-context-llm-agents-2609.06702
--
T=2098159960819421308 | @omarsar0 | 2026-09-10T21:21+00:00 | L66 RT12 C4 V5877 | rt
URL=https://x.com/omarsar0/status/2098159960819421308
RT-OF @dair_ai (L66): Another interesting approach to self-evolve agent skills.

But it's important to know that skill self-evolution loops fail in two specific ways:

1. Direction instability. Effective corrections get overwritten by iteration-local feedback instead of accumulating, so the loop keeps undoing its own fixes.

2. Fixed update scope. Every revision changes about the same amount regardless of whether recent case-level improvements were consistent or noisy.

SkillAdam addresses both by porting Adam's two moment estimates to discrete, non-differentiable skill documents.

As a functional analogue of the first moment, an optimization memory records identified problems and the outcomes of prior solution attempts, which stabilizes the update direction. As an analogue of the second moment, a volatility-driven edit budget tracks the history-weighted variation of recent case-level improvements and controls how large each revision is allowed to be.

Across seven benchmarks spanning short and long-horizon tasks it reaches state of the art with more stable optimization dynamics, and it gets there in substantially fewer iterations and at lower cost than prior methods.

Paper: https://t.co/mwMvfycpVF
RT-URL=https://x.com/dair_ai/status/2098154641854992676
TEXT: RT @dair_ai: Another interesting approach to self-evolve agent skills.

But it's important to know that skill self-evolution loops fail in…
LINKS: https://academy.dair.ai/papers/skilladam-stable-and-efficient-skill-evolution-for-agents-2609.08944
--
T=2098168545393701327 | @omarsar0 | 2026-09-10T21:55+00:00 | L23 RT2 C6 V6077 | post
URL=https://x.com/omarsar0/status/2098168545393701327
TEXT: Recommended read. As the world becomes more agentic, we will start to see world models of different shapes.

As an example, I find this “business world model” from @lightfld fascinating as a way to model the complexity of a business and make it convenient and easier for agents to derive value from. 

They are going for CRM first, but you can easily see how, with the right agent infrastructure, this can potentially mutate and expand to other adjacencies. 

This is just a really interesting and futuristic approach to leveraging agents. It's worth taking notes if you are building and operating in this space.
QUOTED @hliriani: Yesterday we announced our series A to reimagine CRM as a business world model. 

I wanted explain what we mean by that, and why the CRM is the practical place to start building something much larger. https://t.co/j760peA0B2
--
## @rasbt — 2 шт.

T=2098129926708707824 | @rasbt | 2026-09-10T19:22+00:00 | L357 RT18 C12 V46702 | post
URL=https://x.com/rasbt/status/2098129926708707824
TEXT: Nice showcase that interesting LLM work can be done on single GPU!
QUOTED @gpjt: I extended the GPT-2-style code from @rasbt's "Build a Large Language Model (from Scratch)" so that it was a 6-expert (2 active) mixture-of-experts, and trained it from scratch over 8 days.  It worked well!  Full writeup with maths and code at https://t.co/7YsQifjWDk
--
T=2098142625819672603 | @rasbt | 2026-09-10T20:12+00:00 | L1368 RT124 C32 V57187 | thread(2)
URL=https://x.com/rasbt/status/2098142625819672603
TEXT: Big overhaul on DeepSeek V4.1 using an encoder-decoder setup.
Tbh they should have called it DeepSeek V5!
Super cool and refreshing, though! https://t.co/r00s3Cl29m
[->] I know, sorry, but it's hard to resist https://t.co/BPiwraXscP
QUOTED @deepseek_ai: 🚀 Introducing DeepSeek-V4.1-Flash: smarter, faster, more efficient.

🔹 Introducing the smallest model in our new architecture family, with native visual understanding.
🔹 Designed for greater capability, faster inference, higher throughput, and scaling to larger models.

1/6
--
## @sh_reya — 1 шт.

T=2098092642316021804 | @sh_reya | 2026-09-10T16:54+00:00 | L34 RT3 C2 V6653 | post
URL=https://x.com/sh_reya/status/2098092642316021804
TEXT: Really stoked to soft launch what my new group is working on at SF Systems!!
QUOTED @ShadajL: SF Systems is back with a night of talks from researchers bringing their work to the real world! 

@sh_reya will share her latest work on domain-specific inference engines and @parker_ziegler will show us what programming can look like beyond text!

https://t.co/PruIpAvonI
--
