# X-FEED 2026-09-12 part 6/9 | items: 6

## @omarsar0 — 9 шт.

T=2098426608793362916 | @omarsar0 | 2026-09-11T15:01+00:00 | L339 RT54 C23 V21539 | post
URL=https://x.com/omarsar0/status/2098426608793362916
TEXT: Harness engineering is a top skill right now

This new Meta paper is a good production example.

Auto-RecSys runs autonomous research on Meta's industry-scale recommendation models, where one training run can take days.

It runs experiments in parallel across servers, keeps a shared memory so work survives failures and new sessions, and splits guidance into natural-language skill files for reasoning and deterministic scripts for anything operational.

Two loops improve it over time.

Model-specific playbooks record failed attempts and keep working pipelines. Experimental results feed the next round of ideas.

As the playbook matured, major fixes per iteration fell from 4.0 to 1.3, and the failures fell into repeatable categories.

Paper: https://t.co/8my21BqF5X

Chat with Paper: https://t.co/gxv6LWAvug
LINKS: https://arxiv.org/abs/2609.10922 ; https://academy.dair.ai/papers/auto-recsys-harnessing-autonomous-research-agents-for-industry-scale-recommender-2609.10922
--
T=2098433294551417100 | @omarsar0 | 2026-09-11T15:27+00:00 | L91 RT11 C20 V7615 | rt
URL=https://x.com/omarsar0/status/2098433294551417100
RT-OF @dair_ai (L91): Interesting paper from Microsoft.

If you run persistent memory for a production agent, this one is worth your time. (bookmark it)

Memory curators usually read only the finished trajectory.

That lets them save the agent's mistakes, overgeneralize from partial evidence, and keep facts that have gone stale.

Microsoft researchers give the curator a few read-only tools to check each candidate memory against the live environment before it is saved. The task agent, retriever and memory format stay the same, and nothing is retrained.

In a GitHub Copilot harness on CLBench, pass rate goes from 39% to 73%. Queries per question drop from 8.8 to 4.7 and task-agent cost falls from $3.38 to $1.68.

On 90 consulting tasks across six environments, every memory configuration beats the baseline, and tool calls fall by 16 to 75%.

Paper: https://t.co/ZLbYu7B3JA

Chat with Paper: https://t.co/CKvxFW4g0r
RT-URL=https://x.com/dair_ai/status/2098431126343929985
TEXT: RT @dair_ai: Interesting paper from Microsoft.

If you run persistent memory for a production agent, this one is worth your time. (bookmark…
LINKS: https://arxiv.org/abs/2609.11060 ; https://academy.dair.ai/papers/grounding-agent-memory-environment-probing-curation-for-enterprise-agents-2609.11060
--
T=2098435397894246793 | @omarsar0 | 2026-09-11T15:36+00:00 | L36 RT3 C10 V13196 | post
URL=https://x.com/omarsar0/status/2098435397894246793
TEXT: I am extremely bullish on the Pareto frontier of collective intelligence. 

While everyone works on the frontier curve of single models, there is an emerging layer of compounding systems operating way above that. This is the layer you want to be operating on. Why? Well, you can swap out and swap in any model you want (closed or open). You have more control over price, performance, models to use, and how much of that intelligence stack you want to own.
QUOTED @hardmaru: Introducing Fugu Max and Fugu Ultra v2: Orchestrating the Pareto Frontier

The AI industry has spent a decade optimizing along a single axis: build bigger, more expensive models. But intelligence has never been a monolith. It is a collective, distributed system. Humanity itself is a collective intelligence.

We built Sakana Fugu on this conviction: the most powerful AI systems will not be isolated giants, but collaborative ecosystems that learn to coordinate. Evolution innovates under constraint
--
T=2098456262379745663 | @omarsar0 | 2026-09-11T16:58+00:00 | L290 RT22 C28 V34261 | thread(4)
URL=https://x.com/omarsar0/status/2098456262379745663
TEXT: Build and own your harness, folks. 

Very few people understand the magic behind customizing and optimizing an agent harness for your work. 

You can start seeing incredible results quickly, even with a minimal harness. Just better code, better outputs, better costs, better writing, and so on. 

As an example, I see way too many people complain that they are tired of their out-of-the-box agent harness producing verbose outputs. If you built a harness, that's easier to fix with a system prompt optimized for you. 

This is why Pi is getting insane adoption these days. You want to control your harness. I agree that it's hard to optimize where things stand, but self-improving algorithms will make it easier to learn from trajectories. And if you use local models, you can tune all of that end-to-end (through a co-evolution of the harness and the models) as you work with them.

Look into open-source projects like Eve, Exo, and Prime Agent, and you will see what I mean.
[->] And if you are just getting started with harnesses, check out this list of seminal papers: https://t.co/hSkMMHjf1L
[->] @JainAI29 I've found that building from scratch has helped me translate that into productivity gains across our custom and out-of-the-box harnesses.
[->] To be clear, I don't necessarily agree with the post I am quoting. I see a growing trend of people saying that the models will figure out harnesses on their own. To some extent, yes. Just look into dynamic workflows, and you will see it. If you use them extensively, you will also notice how terrible models are at this. And it makes sense because models are generalized and fail miserably on highly specialized contexts or where a lot of prior knowledge and data is used. My point is that harnesses still matter enormously. We need more fluid harnesses that self-improve or continually improve as new models and capabilities land. This is indeed part of your intelligence stack as it stands. The best harnesses are minimal and adaptive: strong context, tools, memory, verifiers, and evals, with room for the model to reason.
QUOTED @unclebobmartin: OK.  It's time to rethink this. 

I've spend the last several weeks working on a harness that tightly constrains the agents to work the way that I want them to work.  I set up all kinds of gates, and tests, and tools, and protocols, and ...

And while I was heads-down getting that to work, the agents got a LOT better.  So much so that when I came up for air, the need for my harness was obviated.  Indeed, the need for _any_ but the most liberal of harnesses may be obviated.

Just how good these t
LINKS: https://academy.dair.ai/papers/collections/harness-engineering
--
T=2098505720316530875 | @omarsar0 | 2026-09-11T20:15+00:00 | L206 RT33 C10 V15584 | rt
URL=https://x.com/omarsar0/status/2098505720316530875
RT-OF @madmadhere (L206): I run all design @higgsfield. 

This procedural animation would normally take a week of my time in After Effects.

Our new GPT-6 Astra plugin in AE just brought that down to 20 minutes. Here’s how.

I open GPT-6 Astra and call: @higgsfield /use-after-effects

That brings in Higgsfield AI Motion Designer. Then I describe the movement I want.

For this scene: 3,000 particles forming letters, reacting to a moving controller and settling back into shape.

GPT-6 Astra builds the scene and writes the expressions directly inside my After Effects project.

Then comes the part that usually eats up the week: getting the motion to actually feel right.

The plugin lets GPT-6 Astra inspect rendered frames and make corrections inside the project.

The layers, expressions and controls stay editable. I can get in and adjust anything myself.

That means more time trying different directions and actually polishing the result.

Bookmark it.
RT-URL=https://x.com/madmadhere/status/2098480068423192664
TEXT: RT @madmadhere: I run all design @higgsfield. 

This procedural animation would normally take a week of my time in After Effects.

Our new…
--
T=2098524621439914375 | @omarsar0 | 2026-09-11T21:30+00:00 | L239 RT25 C35 V28405 | thread(2)
URL=https://x.com/omarsar0/status/2098524621439914375
TEXT: Agents API is a bigger deal than it seems. 

OpenAI's bet on making the Codex harness open-source could pay off big time here.

This harness-as-a-service idea hasn't hit mainstream yet, but some of the most serious builders are already adopting it to unlock new types of services. 

Codex being open-source means that many other models (open or closed) are already extremely knowledgeable about the Codex harness. As more services adopt these new agentic architectures, you'll want the compounding effect that comes with that transparency and openness.
[->] @ishaansehgal @omnaraai will check out what you shared
QUOTED @stevendcoffey: Today we're launching the Agents API, a brand new way to build Agents in the cloud, backed by the Codex harness. Bring along all your favorite tools and connectors, connect it to any sandbox, and let Astra cook.

Can't wait to see what you whip up 👨‍🍳

https://t.co/T5ORJPgpwQ
--
