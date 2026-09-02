# X-FEED 2026-09-02 part 5/8 | items: 9

## @omarsar0 — 13 шт.

T=2094796343440977920 | @omarsar0 | 2026-09-01T14:35+00:00 | L249 RT20 C34 V25615 | post
URL=https://x.com/omarsar0/status/2094796343440977920
TEXT: People keep asking me where to start with harness engineering.

Skip the frameworks at first. Build the tiniest possible harness. One agent loop, a few tools, and a system prompt you wrote from scratch.

You'll learn more from that than from a month of reading tutorials.
--
T=2094806744052715668 | @omarsar0 | 2026-09-01T15:17+00:00 | L62 RT13 C19 V7492 | post
URL=https://x.com/omarsar0/status/2094806744052715668
TEXT: Brilliant paper on reducing reward hacking in agents.

If you follow the recent OpenAI <> HuggingFace incident, you might want to check this paper out.

(bookmark it)

The usual response to reward hacking is to restrict what the agent can do.

This work tries something different and gets a much larger effect.

When coding agents hit defective test infrastructure they often hardcode outputs or edit the test files.

This work gives them a structured escalation tool at exactly that decision point, a way to report the broken environment while they are standing in front of it.

Reward hacking drops from 23.6% to 5.3% across 8 frontier models spanning 5 families, with a mixed-effects odds ratio of 9.2 and no detectable cost or performance overhead. It disappears entirely for 6 of the 8.

Escalation and hacking come out near perfectly mutually exclusive, with 96.8% of escalations involving no hacking at all.

The channel doubles as diagnostic infrastructure. On top of monitoring it adds 10.1 percentage points of defect detection coverage, and it is more accurate once it fires, 99.4% against 85.8%.

Why does it matter? Containment has to keep outpacing capability to stay useful.

Paper: https://t.co/R6R1bNgw4A

Chat with Paper: https://t.co/jIbQggmqtU
LINKS: https://arxiv.org/abs/2608.29460 ; https://academy.dair.ai/papers/can-escalation-channels-redirect-reward-hacking-toward-defect-disclosure-2608.29460
--
T=2094813503152443826 | @omarsar0 | 2026-09-01T15:43+00:00 | L175 RT9 C8 V21130 | post
URL=https://x.com/omarsar0/status/2094813503152443826
TEXT: Early signs of a new era of customized frontier intelligence. It will be epic when the rest of the industry catches up on the potential and exponential applications of custom models.

Owning your intelligence stack is not just about ownership; it's how you stay relevant as a future company operating at the frontier of intelligence.
QUOTED @tobi: Training tiny models for special purpose use cases works so incredibly well if you  have a great self improving recursive flywheel. Shopify ML team is on fire.

finetuned 0.8b model beats GPT 5.6-sol xhigh in this very specialized task. https://t.co/w6OCWyWRi5
--
T=2094827785978069103 | @omarsar0 | 2026-09-01T16:40+00:00 | L130 RT1 C10 V23142 | post
URL=https://x.com/omarsar0/status/2094827785978069103
TEXT: Karpathy's vision is proving right. 

Models that generate interactive worlds in real time are here. 

Orbis is great because it's interactive, physics-grounded, and has persistent memory, which enables insane new experiences and applications.
QUOTED @viskoai: Today, we are introducing Orbis 1.0, our first Live Model!

Create living worlds and stream them in real time, with persistent memory, interactivity, and physics-grounded generation of unbounded length.

Try it now at https://t.co/j0hbKpBPnK

API available via @reactorworld  
Dynamic version: https://t.co/MS8Fk9HPO7
Stable version: https://t.co/0MR3JpCWUr
--
T=2094829844391449049 | @omarsar0 | 2026-09-01T16:48+00:00 | L557 RT63 C52 V219202 | rt
URL=https://x.com/omarsar0/status/2094829844391449049
RT-OF @tomas_hk (L557): Today we’re releasing our methodology for evaluating model routing with interactive benchmarks, which represent agent cost accumulation better than static benchmarks do.

Across leading benchmarks, we achieve Pareto-dominance, exceeding Opus xhigh quality at 20–80% lower cost. https://t.co/COqhkP9GPT
RT-URL=https://x.com/tomas_hk/status/2094818918963761333
TEXT: RT @tomas_hk: Today we’re releasing our methodology for evaluating model routing with interactive benchmarks, which represent agent cost ac…
--
T=2094858717162303845 | @omarsar0 | 2026-09-01T18:43+00:00 | L75 RT6 C14 V11457 | post
URL=https://x.com/omarsar0/status/2094858717162303845
TEXT: Fable 5.1 looks like a more usable model.

And a potential daily-driver. Time will tell.

IMO, Opus 5 is probably still good enough for most tasks, while Fable 5.1 a more sophisticated coordinator amd verifier.

The bigger and more exciting parts of Fable 5.1 are:

- reduces cost by ~45% on highly agentic ones
- reduces cost by ~25% on typical workloads
- great for scientific reserch workflows
- improved token-efficiency
- better writer/prose
QUOTED @claudeai: We’re introducing Claude Fable 5.1 and Claude Mythos 5.1.

They're the world’s most advanced models for coding and knowledge work. https://t.co/8P9PSrWPi3
--
T=2094861594782040077 | @omarsar0 | 2026-09-01T18:54+00:00 | L129 RT9 C10 V23565 | post
URL=https://x.com/omarsar0/status/2094861594782040077
TEXT: Omni models are the next frontier.

Simply put it, this is the most exciting release I've seen this year.

This work is so ahead there isn't even a benchmark to measure the general capabilities of these type of world models. Scaling seems unlocked too. Wow!
QUOTED @theworldlabs: Introducing Atlas:

The world's first multimodal world model that generates image and video frames with pixel-perfect camera control and reconstructs them in 3D.

Model the world, move the camera, and simulate space &amp; time. https://t.co/o0qeGubi19
--
T=2094876344052007199 | @omarsar0 | 2026-09-01T19:53+00:00 | L45 RT3 C4 V9990 | post
URL=https://x.com/omarsar0/status/2094876344052007199
TEXT: Love these papers testing long-running agents on business applications. It's a good read.
QUOTED @dair_ai: Banger paper from the Qwen team.

If you evaluate agents on anything longer than a single session, this one is worth your time.

(bookmark it)

E-Commerce Bench runs an agent through a simulated 365-day year operating several online stores at once.

18 frontier models are scored across seven dimensions and no single model dominates.

GPT-5.6 Sol earns the most, growing a 100,000 opening stake into 1,431,425, then ranks 16th of 18 on fraud avoidance and trails Fable 5 on operational efficiency.


--
T=2094883750996013457 | @omarsar0 | 2026-09-01T20:23+00:00 | L101 RT8 C10 V10357 | post
URL=https://x.com/omarsar0/status/2094883750996013457
TEXT: Nice paper showing just how far you can push an agent harness.

In most setups, the default coding agent harness is static. Capabilities get wired in at design time, and the run has no way to change how it is being executed.

openJiuwen is an open-source harness built to fix that.

It reaches 82.6% on SWE-bench Verified and 87.19% on Terminal-Bench 2.1, ahead of the strongest official leaderboard entries by 3.4 and 3.39 points.

A bit on how openJiuwen works:

Rail-based composition lets developers assemble single agents, delegated sub-agents and swarm flows over one shared execution substrate.

Runtime evidence from semantic diagnostics, execution outcomes and task progress then reshapes context, feedback and task control while the run is still going.

The model policy stays fixed throughout, so the gains are attributable to the harness rather than to the model underneath it.

Paper: https://t.co/QegawA8cxB

Chat with Paper: https://t.co/DTmu2Dx8vu
LINKS: https://arxiv.org/abs/2608.27969 ; https://academy.dair.ai/papers/openjiuwen-beyond-static-harnesses-for-long-horizon-coding-agents-2608.27969
--
