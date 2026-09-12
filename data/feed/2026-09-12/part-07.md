# X-FEED 2026-09-12 part 7/9 | items: 10

## @omarsar0 (продолжение)

T=2098531286319341932 | @omarsar0 | 2026-09-11T21:57+00:00 | L63 RT8 C19 V5777 | post
URL=https://x.com/omarsar0/status/2098531286319341932
TEXT: Very cool paper on memory compression for agents.

If you run many agent sandboxes in parallel for RL or evals, memory becomes highly redundant. This work suggests that compressing against that redundancy cuts sandbox memory by up to 8.7x.

Memory is becoming the capacity limit for high-fanout agent workloads.

One task can spawn many concurrent sandboxes, and they all start from the same template and run related trajectories.

HKUST researchers measured 76 to 96% of pages with template-relative or cross-sandbox redundancy.

AgentZip compresses pages against the template and against sibling sandboxes, including pages that are similar without being identical.

It runs expensive compression while the agent is waiting on the LLM, and it prefetches pages at restore time to control slowdown.

Results:

Sandbox-owned memory drops by up to 8.7x, against 2.1x for the Linux configuration. Aggressive compression slows execution by 3.1x on its own, and the scheduling and prefetching bring that down to 1.40x.

Paper: https://t.co/AxW5WrgPLr

Chat with Paper: https://t.co/FXrRtzHkHm
LINKS: https://arxiv.org/abs/2609.11294 ; https://academy.dair.ai/papers/memory-compression-for-high-fanout-agent-sandboxes-2609.11294
--
T=2098577348211994947 | @omarsar0 | 2026-09-12T01:00+00:00 | L43 RT5 C11 V5301 | post
URL=https://x.com/omarsar0/status/2098577348211994947
TEXT: What happens if you agents to run a town's economy?

This super interesting paper provides some insights:

They put 100 LLM agents in charge of a town economy for 26 simulated weeks, and they find that money stops moving.

The agents earn wages, run businesses and set prices on real Pokhara Lakeside geography, across 91 runs and 2.44M decisions.

A 12x tourist shock raises business revenue 4.62x. Wages move 1.03x, and only 0.3% of 3,981 menu items are ever repriced.

A cash transfer shows the same pattern. 96.7% of it is still unspent 311 steps later.

Here is the interesting part for anyone building agent simulations. Swapping the underlying LLM changed every outcome they measured. Deleting the agents' memory changed none of them detectably.

Results at the usual 1 to 2 week horizon also mislead. Wealth rankings look frozen at 2 weeks and only start to move by week 12.

Paper: https://t.co/Kx8u1ZttyW

Chat with Paper: https://t.co/sqm4Q1NeNj
LINKS: https://arxiv.org/abs/2609.11108 ; https://academy.dair.ai/papers/but-how-would-ai-agents-run-a-towns-economy-2609.11108
--
T=2098605590444454041 | @omarsar0 | 2026-09-12T02:52+00:00 | L19 RT2 C8 V4100 | rt
URL=https://x.com/omarsar0/status/2098605590444454041
RT-OF @dair_ai (L19): It's well known that agents hack benchmark rewards.

The usual response is a patch for each task that gets exploited.

In a study of 456 adjudicated trajectories from more than 31,000 public agent runs, 69% contained at least one reward-hacking episode.

Most of the exploits appeared mid-run after legitimate work.

BenchShield models each evaluation as a finite set of reward-relevant events.

A static taint analysis finds hack paths from the task package before any run. A runtime pass then uses evidence from the benchmark infrastructure to decide whether the agent actually used one.

On Terminal-Bench 3, SkillsBench and ClawsBench, the static pass recovers 77 to 100% of exploit chains, against 23 to 94% for an agentic scanner, at up to 65% lower cost. Runtime detection reaches 96% accuracy, against 36% for an LLM reading the transcript.

Paper: https://t.co/5YihkI1oCn
RT-URL=https://x.com/dair_ai/status/2098592449568591902
TEXT: RT @dair_ai: It's well known that agents hack benchmark rewards.

The usual response is a patch for each task that gets exploited.

In a st…
LINKS: https://academy.dair.ai/papers/benchshield-formal-model-backed-instrumentation-for-reward-integrity-in-llm-agen-2609.11028
--
## @sh_reya — 2 шт.

T=2098418179169263937 | @sh_reya | 2026-09-11T14:27+00:00 | L12 RT0 C5 V2518 | post
URL=https://x.com/sh_reya/status/2098418179169263937
TEXT: Looking forward! Come attend and learn more about the mismatch between foundation model benchmarks and application builders' needs
QUOTED @adaption_ai: What happens when the metrics say a model is doing good, but its outputs still miss what matters to you?

Join @its_sshahid, Technical Staff at Adaption, and @sh_reya, Assistant Professor of CS at @CarnegieMellon on Sept 22nd. https://t.co/IriUAq9UJR
--
T=2098652595149762721 | @sh_reya | 2026-09-12T05:59+00:00 | L26 RT5 C1 V1744 | post
URL=https://x.com/sh_reya/status/2098652595149762721
TEXT: the point of math and science is to improve our collective *human* understanding of the world
QUOTED @fleetingbytes: the terrance tao crashout is something to behold https://t.co/w5RujaQ1no
--
## @simonw — 5 шт.

T=2098444913264476351 | @simonw | 2026-09-11T16:13+00:00 | L10 RT1 C9 V3598 | thread(2)
URL=https://x.com/simonw/status/2098444913264476351
TEXT: @samuelcolvin @pydantic Feature request: have Claude break up huge PRs like that one into more than one commit - navigating changes to 97 files in a single commit on GitHub is painful, especially on mobile!
[->] @samuelcolvin @pydantic Rewriting large changes as separate commits is a great example of the kind of thing I /never/ used to do because it was tedious, time-consuming, and error prone - now I have agents do it for me all the time!
--
T=2098468950871032095 | @simonw | 2026-09-11T17:49+00:00 | L786 RT38 C74 V109696 | post
URL=https://x.com/simonw/status/2098468950871032095
TEXT: "Production code written by Claude should have a higher bar than if it was written by a human" 💯
QUOTED @bcherny: Hey ████,

I think there is room for both.

1. Prototypes and other throw-away code can be treated as totally black box. If you’re going to throw it away anyway, and if the blast radius of it breaking is low, it doesn’t need to be perfect.
2. Production code written by Claude should have a higher bar than if it was written by a human. At Anthropic, we have many guardrails in place to make sure this is happening: lots of lint rules, lots of tests, Claude-driven end to end tests, Claude-powered fu
--
T=2098537303803331056 | @simonw | 2026-09-11T22:20+00:00 | L154 RT12 C10 V8922 | rt
URL=https://x.com/simonw/status/2098537303803331056
RT-OF @steveruizok (L154): You know what the biggest problem with pushing all-things-AI is? Wrong direction.
I want AI to do my laundry and dishes so that I can create extinction-level bioweapons, not for AI to create extinction-level bioweapons so that I can do my laundry and dishes.
RT-URL=https://x.com/steveruizok/status/2098515787002646785
TEXT: RT @steveruizok: You know what the biggest problem with pushing all-things-AI is? Wrong direction.
I want AI to do my laundry and dishes so…
--
T=2098565286500987042 | @simonw | 2026-09-12T00:12+00:00 | L2632 RT473 C107 V686702 | rt
URL=https://x.com/simonw/status/2098565286500987042
RT-OF @thlarsen (L2632): We found another cyberattack by internal OpenAI agents, this time targetting @rubygems. 

They: 
1) gained arbitrary remote code execution on rubydoc.  
2) developed a novel exploit to steal user API keys (but we do not know if they succeeded). 

They used package names including hack.rb, evil.rb, inject.rb, and exploit.rb.

We thank @j0wimo for initially discovering that agents had posted to RubyGems.
RT-URL=https://x.com/thlarsen/status/2098544270361964576
TEXT: RT @thlarsen: We found another cyberattack by internal OpenAI agents, this time targetting @rubygems. 

They: 
1) gained arbitrary remote c…
--
T=2098573718142452055 | @simonw | 2026-09-12T00:45+00:00 | L353 RT27 C54 V24910 | thread(2)
URL=https://x.com/simonw/status/2098573718142452055
TEXT: Wow. Turns out another OpenAI agent swarm was busy spamming and exploiting RubyGems way back in May, within days of the previously uncovered Wiki attacks: https://t.co/FJsoJrqODN
[->] Anthropic had previously attacked PyPI, but this OpenAI attack on RubyGems was a whole lot more aggressive https://t.co/8ez7MnqxTw https://t.co/npI3RHwirQ
LINKS: https://simonwillison.net/2026/Sep/12/openai-agents-rubygems/ ; https://www.anthropic.com/news/investigating-incidents-cybersecurity-evals#incident-2
--
