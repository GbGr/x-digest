# X-FEED 2026-07-24 part 8/10 | items: 11

## @mitsuhiko — 5 шт.

T=2080225925283659789 | @mitsuhiko | 2026-07-23T09:38+00:00 | L266 RT19 C41 V61925 | post
URL=https://x.com/mitsuhiko/status/2080225925283659789
TEXT: I think this is a very bad move, and the people behind Codeberg should re-consider there stance. https://t.co/mTsq4K4Hso
LINKS: https://blog.codeberg.org/protecting-our-floss-commons-from-llms.html
--
T=2080243367535898707 | @mitsuhiko | 2026-07-23T10:47+00:00 | L635 RT60 C19 V111916 | post
URL=https://x.com/mitsuhiko/status/2080243367535898707
TEXT: We've recently made Pi's cache behavior more visible. This site has been debating whether agent harnesses are helping or quietly torching their caches. That seemed like a good excuse to explain how KV caches actually work and how Pi helps (or doesn't). https://t.co/fXwUFHLAD6
LINKS: https://earendil.com/posts/prompt-caching/
--
T=2080311683612823756 | @mitsuhiko | 2026-07-23T15:18+00:00 | L69 RT2 C6 V8787 | post
URL=https://x.com/mitsuhiko/status/2080311683612823756
TEXT: We don’t have any real data about pi at scale btw. Which is why we want to look into opt-in analytics to learn a bit. Cache rates and tool failures are obviously of interest.
QUOTED @mitsuhiko: We've recently made Pi's cache behavior more visible. This site has been debating whether agent harnesses are helping or quietly torching their caches. That seemed like a good excuse to explain how KV caches actually work and how Pi helps (or doesn't). https://t.co/fXwUFHLAD6
--
T=2080398848875213004 | @mitsuhiko | 2026-07-23T21:05+00:00 | L99 RT0 C2 V7585 | post
URL=https://x.com/mitsuhiko/status/2080398848875213004
TEXT: It's the small things, but I'm so happy that committing to Pi no longer generates random TS files with model updates, but that we found a way to generate this on the fly. A much more enjoyable experience now :)
--
T=2080406690889941316 | @mitsuhiko | 2026-07-23T21:36+00:00 | L51 RT0 C0 V5554 | post
URL=https://x.com/mitsuhiko/status/2080406690889941316
TEXT: I have the suspicion that @pidotdev's Twitter account is going to outgrow me in no time.
--
## @natolambert — 3 шт.

T=2080300577901428974 | @natolambert | 2026-07-23T14:34+00:00 | L271 RT21 C15 V12824 | thread(2)
URL=https://x.com/natolambert/status/2080300577901428974
TEXT: To anyone that accuses me of being a China shill on distillation -- I've been worried about this for a long time and we're just starting to feel the pain of being behind on open models, and it'll only get worse from here if we don't find ways to support building them in the US. https://t.co/jqfTvxHH7c
[->] one year ago: https://t.co/ChhNkP0IKL
LINKS: https://atomproject.ai/
--
T=2080306805595684990 | @natolambert | 2026-07-23T14:59+00:00 | L156 RT17 C11 V23124 | thread(6)
URL=https://x.com/natolambert/status/2080306805595684990
TEXT: If you're looking for the latest adoption data on open models in US v China v globally, we built a small dashboard with the big picture and per-org numbers. Updates daily.

US's role is slowly growing, but still way behind China/Qwen. https://t.co/JA2dIKsQFK
[->] @NVIDIAAI China also dominates in measures of how many models are being finetuned, and from which base models. https://t.co/fSw84VX1pT
[->] https://t.co/h2XSTTId7e

e.g. you can see @NVIDIAAI catching OpenAI as one of the emerging model makers https://t.co/DZMmYqVSZp
[->] @NVIDIAAI Built on our curation at @interconnectsai -- we maintain a public list of models we think are the core LLMs and will be launching more ontop of this data soon https://t.co/dm3oYL6gKx
[->] @NVIDIAAI @interconnectsai Thanks to @huggingface for having open data + apis to make this possible.
[->] @NVIDIAAI @interconnectsai @huggingface eg gemma 4 made a meaningful shift in Google's trajectory. https://t.co/JndWb4AVAi
LINKS: https://dashboard.interconnects.ai/ ; https://github.com/Interconnects-AI/tracked-models
--
T=2080379686287516114 | @natolambert | 2026-07-23T19:49+00:00 | L173 RT6 C4 V17343 | post
URL=https://x.com/natolambert/status/2080379686287516114
TEXT: OpenAI did this for the sycophancy model, was a wonderful post, I hope they repeat that trend!
QUOTED @johnschulman2: OpenAI should release a detailed transcript from the Hugging Face hacking incident -- it would be helpful for the field learn from. Did the top-level agent know about the hacking, or was there some "value drift" between it and its subagents? How did it rationalize its behavior?
--
## @omarsar0 — 3 шт.

T=2080296884187652381 | @omarsar0 | 2026-07-23T14:20+00:00 | L408 RT78 C28 V23333 | post
URL=https://x.com/omarsar0/status/2080296884187652381
TEXT: Great paper on self-improving agent harnesses.

(bookmark it)

If you maintain a production agent harness, finding every file behind one behavior is often harder than writing the edit.

Harness Handbook builds a three-level map from runtime behaviors to source locations using static analysis and LLM-assisted structuring.

Its BGPD workflow guides coding agents from the system overview to relevant stages, functions, and files, then verifies every candidate against current source.

Across 60 modification requests on Codex and Terminus-2, handbook guidance raised planning win rates from 28.3% to 38.3% and from 26.7% to 45.6%.

Planner token use fell 12.7% and 8.6%.

File- and symbol-level F1 improved in all 24 comparisons against GPT-5.5 and Opus 4.8 reference plans. Complete localization misses fell by as much as 25.9 points.

This is a strong pattern for coding agents that need to evolve large harnesses without losing scattered or rarely executed behavior.

Paper: https://t.co/DW7mIEuPr5

Learn to build effective AI agents in our academy: https://t.co/1e8RZKs4uX
LINKS: https://arxiv.org/abs/2607.13285 ; https://academy.dair.ai/
--
T=2080323178119786642 | @omarsar0 | 2026-07-23T16:04+00:00 | L295 RT31 C29 V21820 | thread(3)
URL=https://x.com/omarsar0/status/2080323178119786642
TEXT: Dynamic workflows are a generalization of harnesses,  automations, loops, routing, and graphs.

It's the most powerful feature I have built into my agent orchestrator.

Supports all kinds of patterns that leverage different agent backends (claude, codex, pi, hermes,...).

It's a meta-harness approach that unlocks new forms of test-time compute. 

Example of use cases it supports:

> LLM councils to get different perspectives from LLMs or plan more intensively

> Dynamically routing tasks to different agents based on needs (e.g., cost efficiency and optimal intelligence)

> Advisor/Judge + executor workflows and pretty much any complex graph-based pattern required by the task. I find it especially useful for long-running work and code reviewing.

> Agent teams that talk to each other if needed for the task. I like to use this for AI editing, artifact creation, and other creative tasks.

And I am sure it supports so many things that I haven't discovered yet. 

I got inspired by the dynamic workflow feature released by the Claude Code team. I had actually built it earlier this year but wanted to generalize it across different agent backends. I think this is going to become more popular in the coming days. I will share more of my findings soon.
[->] It's clear to me that a lot of these ideas are very early. But having built my own agent orchestrator has allowed me to experiment with agents in ways that are still hard to comprehend. I am still on the hunt for the most generalized form of an agent harness, but this might be close to it. I am doing intensive AI research in the background to benchmark these ideas, and it's a lot of work, but I am learning so much, and it's fun to share these ideas early here.
[->] Peter knows something, of course. But all these loops and graphs are just terms that will consolidate into one interface that allows the complex agentic workflows and interactions that the task demands. And it should work dynamically and automatically. 

https://t.co/FxrzToUp46
LINKS: https://x.com/steipete/status/2078277297791189132?s=20
--
T=2080340696842539204 | @omarsar0 | 2026-07-23T17:14+00:00 | L95 RT7 C10 V13291 | post
URL=https://x.com/omarsar0/status/2080340696842539204
TEXT: The hard part of multi-agent systems is getting agents to stay quiet.

Put five agents on one task, and they duplicate work and burn tokens talking to each other.

Offloop trained a dispatcher model called D1 that decides which agent moves next and when the right move is to do nothing. They achieve state-of-the-art performance on GDPval at a fraction of the usual cost.

You can bring your own AI subscription. https://t.co/Q4wgI9mbM7
QUOTED @Offloop: Introducing Offloop!

We're a team of four. Today our multi-agent harness hit state of the art on GDPval, ahead of Claude code and Codex across jobs that pay $2.4 trillion a year in the US.

Offloop gives every knowledge worker what the Fortune 500 spends billions on: a high-performing agent army that runs itself and grows the business.
LINKS: http://offloop.org
--
