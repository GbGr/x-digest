# X-FEED 2026-07-26 part 5/6 | items: 12

## @omarsar0 — 6 шт.

T=2080995500040323303 | @omarsar0 | 2026-07-25T12:36+00:00 | L82 RT9 C27 V10995 | rt
URL=https://x.com/omarsar0/status/2080995500040323303
RT-OF @omarsar0 (L82): Open source AI must win.
RT-URL=https://x.com/omarsar0/status/2080843933286793507
TEXT: RT @omarsar0: Open source AI must win.
--
T=2081075060270363136 | @omarsar0 | 2026-07-25T17:52+00:00 | L47 RT2 C6 V10605 | post
URL=https://x.com/omarsar0/status/2081075060270363136
TEXT: Julian is an incredible researcher, but this really misses the mark.

Last week, someone shouted, "Open-weight models are inherently decelerationist," and now this.

What worries me is what exactly is triggering these responses now. Quite the toxic topic (unnecessarily) open-weight models have become. Something that all of these companies have benefitted from.
QUOTED @Mononofu: I’m so excited that @JensenHuang is a believer in open source now, looking forward to the CUDA and GPU driver open source release!
--
T=2081078830341464464 | @omarsar0 | 2026-07-25T18:07+00:00 | L36 RT13 C8 V7202 | thread(9)
URL=https://x.com/omarsar0/status/2081078830341464464
TEXT: A diffusion LLM built for agentic work, from the inclusionAI team at Ant Group (@ant_oss). 

The weights and code are open.
Model: https://t.co/f0OUWOrwhD 
Code. https://t.co/ZXF1dLPmD3
[->] On agentic benchmarks, LLaDA2.2-flash comes out ahead of Ling-2.6-flash on τ²-Bench (592.80 vs 334.90).

Furthermore, LLaDA2.2-flash (fast mode) achieves 705.30. https://t.co/NflikDxd3p
[->] On speed, it averages 1.64x BF16 throughput over Ling-2.6-flash.

FP8 quantization adds another 18.6% on top. https://t.co/nSw2CYCXBV
[->] The practical side holds up as well.

Native 128K context, trained on a progressive schedule from 8K up to 128K.

It's a Mixture-of-Experts (MoE) model, so only a slice of its parameters runs per token, which is part of what makes it fast. A Block Routing strategy trims that routing work further and keeps long-context inference cost predictable.
[->] The RL stage builds on the same mechanism.

L-EBPO extends block-level policy optimization with the editing operations, so the model learns from environment feedback when to cut a defective span and when to fill a gap.

That blocks error propagation at the trajectory level, a structural fix for model collapse in long-horizon agents.
[->] On SWE-bench Verified, LLaDA2.2-flash scores 49.28. https://t.co/yVLHSsAZHl
[->] LLaDA 2.2 addresses this with Levenshtein editing.

On top of filling in masked tokens, the model applies four primitive operations (KEEP, SUBSTITUTE, DELETE, INSERT) to its own output, trained through longest common subsequence alignment.

It can delete a broken span or insert a missing one mid-generation, so errors stop locking in.
[->] Quick background. 

Diffusion LLMs generate many tokens in parallel, which makes them fast.

In long-horizon agent runs, an early mistake gets written into context as a hard constraint and compounds across every later step. That is the model collapse problem, and earlier diffusion models had no clean way to recover once a bad token was placed.
[->] Diffusion LLMs can now handle real agentic work.

LLaDA 2.2 is the first large-scale diffusion LLM built to operate as a real agent, planning, calling tools, and self-correcting across long multi-turn trajectories, and it keeps the speed advantage of block-parallel decoding.

Lots of technical decisions here that stand out:
LINKS: https://huggingface.co/inclusionAI/LLaDA2.2-flash ; https://github.com/inclusionAI/LLaDA2.X
--
T=2081082152939114566 | @omarsar0 | 2026-07-25T18:20+00:00 | L8261 RT982 C303 V919433 | rt
URL=https://x.com/omarsar0/status/2081082152939114566
RT-OF @miramurati (L8261): The knowledge that makes AI useful is diffused. It lives with scientists, engineers, clinicians, firms. For AI to benefit from distributed knowledge, it must itself be distributed. Agree with Jensen that this is a future worth building.
RT-URL=https://x.com/miramurati/status/2080715390179766646
TEXT: RT @miramurati: The knowledge that makes AI useful is diffused. It lives with scientists, engineers, clinicians, firms. For AI to benefit f…
--
T=2081085236641747104 | @omarsar0 | 2026-07-25T18:32+00:00 | L20 RT1 C2 V7169 | post
URL=https://x.com/omarsar0/status/2081085236641747104
TEXT: Surely, they can't all be wrong. 

Open-weight models were the past, are the present, and will shape the future. Like it or not. https://t.co/PiOeffJIIe
--
T=2081086786084770119 | @omarsar0 | 2026-07-25T18:38+00:00 | L14 RT2 C5 V7102 | post
URL=https://x.com/omarsar0/status/2081086786084770119
TEXT: "For AI to benefit from distributed knowledge, it must itself be distributed."

Indeed! That's the future worth building.
QUOTED @miramurati: The knowledge that makes AI useful is diffused. It lives with scientists, engineers, clinicians, firms. For AI to benefit from distributed knowledge, it must itself be distributed. Agree with Jensen that this is a future worth building.
--
## @RLanceMartin — 1 шт.

T=2081054874163437950 | @RLanceMartin | 2026-07-25T16:32+00:00 | L298 RT25 C13 V22046 | rt
URL=https://x.com/RLanceMartin/status/2081054874163437950
RT-OF @Whats_AI (L298): Big news from our internal writing benchmark (early results): Claude Opus 5 by @AnthropicAI is now #1 for writing in our editorial voice, at 2817 Elo, surpassing Claude Fable 5 and Kimi. Already!

That is a jump from #15 to #1 over its predecessor (if we take all thinking variants into account), Opus 4.8, at the same API price.

Reasoning effort actually matters this time. At default effort it lands #6. At max effort it takes the top spot, thinking for over three minutes per script. Seems obvious, but it wasn’t the case for 4.8, though it is for Fable.
RT-URL=https://x.com/Whats_AI/status/2080817747462607315
TEXT: RT @Whats_AI: Big news from our internal writing benchmark (early results): Claude Opus 5 by @AnthropicAI is now #1 for writing in our edit…
--
## @sh_reya — 1 шт.

T=2080982912434872666 | @sh_reya | 2026-07-25T11:46+00:00 | L102 RT6 C6 V12325 | post
URL=https://x.com/sh_reya/status/2080982912434872666
TEXT: This problem has gotten significantly worse. As Twitter and other social media have become primary channels for sharing research, academics are now expected to make the same ideas legible and appealing to both the general public (to go "viral") and senior scholars (to get the paper accepted). These audiences evaluate and reward almost opposite things, and there is little common ground between them. The result is truly the worst of both words (catchy and sales-y with no regard for prior work, and lots of jargon)
QUOTED @allgarbled: Computer science people have developed an unintentional form of gatekeeping by virtue of being extremely bad at explaining/naming things, which results in simple concepts sounding far more complex than they are.
--
## @simonw — 1 шт.

T=2081153980294648186 | @simonw | 2026-07-25T23:05+00:00 | L238 RT14 C19 V25010 | post
URL=https://x.com/simonw/status/2081153980294648186
TEXT: Ruff 0.16.0 - @astral_sh's fast Python linter - came out a few days ago and increased the number of default-enabled rules from 59 to 413, which highlighted all sorts of problems across my projects (1618 in sqlite-utils alone) https://t.co/QTtemT1KtI
LINKS: https://simonwillison.net/2026/Jul/25/ruff/
--
## @swyx — 2 шт.

T=2081122841102340550 | @swyx | 2026-07-25T21:02+00:00 | L0 RT0 C0 V2410 | post
URL=https://x.com/swyx/status/2081122841102340550
TEXT: @cormacb cormac's latest at @aidotengineer is now live!
https://t.co/Bzr9e7KQFC
LINKS: https://www.youtube.com/watch?v=hacEQHHhu2Q
--
T=2081142196510843374 | @swyx | 2026-07-25T22:19+00:00 | L42 RT2 C8 V11992 | post
URL=https://x.com/swyx/status/2081142196510843374
TEXT: lmao @ClementDelangue doing the 🇳🇴 https://t.co/K4fzvccUFA
QUOTED @eraqian: 🎉 Today’s the day! About 500 open-source builders are coming together

Join us to support the Open Weights Movement. Bring friends and good vibes! Meet all the gladiators pushing the open AI frontier 💪🏻 https://t.co/X5RgRj8klJ
--
## @thorstenball — 1 шт.

T=2081256432616276145 | @thorstenball | 2026-07-26T05:52+00:00 | L5 RT0 C0 V437 | post
URL=https://x.com/thorstenball/status/2081256432616276145
TEXT: No newsletter today! 

Back from my bike trip, reading Wikipedia articles on asphalt and wishing a long-ass article on asphalt's influence on civilization titled Where the Rubber Hits the Road existed, chilling and preparing Laracon talk.
--
