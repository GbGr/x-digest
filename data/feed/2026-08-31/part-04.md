# X-FEED 2026-08-31 part 4/6 | items: 5

## @omarsar0 — 9 шт.

T=2094029957391401208 | @omarsar0 | 2026-08-30T11:50+00:00 | L85 RT13 C15 V20296 | rt
URL=https://x.com/omarsar0/status/2094029957391401208
RT-OF @omarsar0 (L85): Insane observations on the emergent behavior of agents.

Agents can build a world of their own that becomes a part of their intelligence.

We are just not ready for persistent agents. But they are starting to show up everywhere in AI products. 

Crazy finding:

“We find division of labor, multi-author engineering, deep generation invention lineages, and machines that vastly outlive their original creators.”

Here is another wild observation that emerged:

When they remove every AI agent, the technologies they created continue operating and are tested against unseen disturbances.

Based on these early findings, I think once recursive self-improving (RSI) arrives and embodied AI is solved (with true understanding of the physical world), intelligence will explode in ways that will fundamentally change our understanding of the world we live in.
RT-URL=https://x.com/omarsar0/status/2093761700558229523
TEXT: RT @omarsar0: Insane observations on the emergent behavior of agents.

Agents can build a world of their own that becomes a part of their i…
--
T=2094029923228778888 | @omarsar0 | 2026-08-30T11:50+00:00 | L62 RT5 C15 V10126 | rt
URL=https://x.com/omarsar0/status/2094029923228778888
RT-OF @omarsar0 (L62): You do not need frontier models for everything.

For example, open models are great for automations. 

If you are not sure where to adopt open models, start there. 

It's one of the biggest changes I've made that contributed to a large percentage of my token usage moving to local or open models.

A huge percentage of my automations consist of repetitive tasks steered via self-tuned skills. 

These skills become useful automations that work really well with these open models. I don't even need to tune the models, but that's also an option I am currently exploring for more complex tasks. The skill essentially takes care of that. And it works because of the in-context learning capabilities of these models. 

If you don't run automations, it might be hard to figure this out. But I highly recommend you start somewhere. 

Besides ending up with more efficient automations, I've managed to significantly reduce costs. I then use that extra budget to leverage more closed frontier intelligence for other creative and research-heavy tasks. 

That's right! I use both closed and open frontier intelligence. This is not about vendor loyalty; this is about leveraging the best of all worlds. 

Something I heavily advocate for is owning the harness and the model, and this practice I feel will allow me to better tap into all flavors of intelligence (open & closed).

Maybe too early, but I suspect this is going to become best practice when AI ROI dominates the discussion. 

Model routing doesn't solve this. This requires tedious engineering, evals, and decision-making on your part. If you are developing your own harness, you are in the driver's seat and have more control over this important decision. This is why I strongly believe that companies will start to hire rapidly for harness engineering.

I am sharing a little snapshot of one example of an automation I run daily to track AI trending stories on HN. And I have a bunch of similar ones for different sources like arXiv, X, and so on.
RT-URL=https://x.com/omarsar0/status/2093786788628185328
TEXT: RT @omarsar0: You do not need frontier models for everything.

For example, open models are great for automations. 

If you are not sure wh…
--
T=2094080366919188843 | @omarsar0 | 2026-08-30T15:10+00:00 | L47 RT2 C10 V15397 | post
URL=https://x.com/omarsar0/status/2094080366919188843
TEXT: Recommended read. It's an opinion, but increasingly I find myself doing the same. 

I've optimized for using minimal harnesses like Pi and have found it easier to switch to newer models or alternate between open and closed ones without sacrificing performance. 

Be careful what you optimize for and how you do it, especially with the velocity of things today. 

And if you are hardcore like I prefer, build and optimize your own harness and set up evals and loops to optimize the setup autonomously.
QUOTED @kunchenguid: while maintaining my open source projects i noticed many people started using something called Oh My Pi

out of curiosity i took a look and gave it a go myself, and oh my.. 

it’s a giant pile of harness tricks bundled into one. each trick seems to do well on benchmarks. but…

this is EXACTLY what the bitter lesson told us to avoid. it may indeed work well at the time it’s evaluated, but every model release can invalidate a bunch of these results

unless every single part of the package gets rig
--
T=2094087165827305846 | @omarsar0 | 2026-08-30T15:37+00:00 | L95 RT15 C8 V21174 | rt
URL=https://x.com/omarsar0/status/2094087165827305846
RT-OF @dair_ai (L95): The Top AI Papers of the Week (August 24 - 30):

- Skill Lift
- JIT-Agent
- Prime Agent
- Judges as a Lifecycle
- Co-Scientist in Real Labs
- What Compaction Destroys
- Context Management as Code

Read on for more:
RT-URL=https://x.com/dair_ai/status/2094086014536978591
TEXT: RT @dair_ai: The Top AI Papers of the Week (August 24 - 30):

- Skill Lift
- JIT-Agent
- Prime Agent
- Judges as a Lifecycle
- Co-Scientist…
--
T=2094109398604099888 | @omarsar0 | 2026-08-30T17:06+00:00 | L127 RT23 C16 V12414 | post
URL=https://x.com/omarsar0/status/2094109398604099888
TEXT: Banger paper from Stanford on efficient test-time scaling.

If you run agents that think for a long time, this one is worth your time.

(bookmark it)

Long reasoning keeps the entire trace in memory through full attention.

This means that the hardest problems, the ones that need the most thinking, are also the ones that cost the most to run.

The authors measured what the middle of a reasoning trace is actually worth.

Intermediate tokens steadily lose importance as the model keeps going.

Their new approach, Prefix Sliding, drops those tokens. It keeps the prefix, which holds the instructions and the available tools, plus a window of the last few thousand tokens. Everything in between gets discarded during generation.

Total memory stays capped no matter how long the model reasons.

Without any training, this runs existing models 3x faster while matching full-attention performance, and it enables RL rollouts past 100,000 tokens.

Paper: https://t.co/HzwSZ7fCdh

Chat with Paper: https://t.co/OfjtVjamIC
LINKS: https://arxiv.org/abs/2608.26070 ; https://academy.dair.ai/papers/prefix-sliding-for-efficient-test-time-scaling-2608.26070
--
