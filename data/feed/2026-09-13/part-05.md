# X-FEED 2026-09-13 part 5/8 | items: 6

## @omarsar0 — 9 шт.

T=2098740808073572841 | @omarsar0 | 2026-09-12T11:49+00:00 | L398 RT45 C46 V55896 | rt
URL=https://x.com/omarsar0/status/2098740808073572841
RT-OF @omarsar0 (L398): Agents API is a bigger deal than it seems. 

OpenAI's bet on making the Codex harness open-source could pay off big time here.

This harness-as-a-service idea hasn't hit mainstream yet, but some of the most serious builders are already adopting it to unlock new types of services. 

Codex being open-source means that many other models (open or closed) are already extremely knowledgeable about the Codex harness. As more services adopt these new agentic architectures, you'll want the compounding effect that comes with that transparency and openness.
RT-URL=https://x.com/omarsar0/status/2098524621439914375
TEXT: RT @omarsar0: Agents API is a bigger deal than it seems. 

OpenAI's bet on making the Codex harness open-source could pay off big time here…
--
T=2098740789731790877 | @omarsar0 | 2026-09-12T11:49+00:00 | L120 RT22 C23 V11706 | rt
URL=https://x.com/omarsar0/status/2098740789731790877
RT-OF @omarsar0 (L120): Very cool paper on memory compression for agents.

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
RT-URL=https://x.com/omarsar0/status/2098531286319341932
TEXT: RT @omarsar0: Very cool paper on memory compression for agents.

If you run many agent sandboxes in parallel for RL or evals, memory become…
LINKS: https://arxiv.org/abs/2609.11294 ; https://academy.dair.ai/papers/memory-compression-for-high-fanout-agent-sandboxes-2609.11294
--
T=2098761473564512718 | @omarsar0 | 2026-09-12T13:11+00:00 | L343 RT30 C33 V43510 | rt
URL=https://x.com/omarsar0/status/2098761473564512718
RT-OF @omarsar0 (L343): Build and own your harness, folks. 

Very few people understand the magic behind customizing and optimizing an agent harness for your work. 

You can start seeing incredible results quickly, even with a minimal harness. Just better code, better outputs, better costs, better writing, and so on. 

As an example, I see way too many people complain that they are tired of their out-of-the-box agent harness producing verbose outputs. If you built a harness, that's easier to fix with a system prompt optimized for you. 

This is why Pi is getting insane adoption these days. You want to control your harness. I agree that it's hard to optimize where things stand, but self-improving algorithms will make it easier to learn from trajectories. And if you use local models, you can tune all of that end-to-end (through a co-evolution of the harness and the models) as you work with them.

Look into open-source projects like Eve, Exo, and Prime Agent, and you will see what I mean.
RT-URL=https://x.com/omarsar0/status/2098456262379745663
TEXT: RT @omarsar0: Build and own your harness, folks. 

Very few people understand the magic behind customizing and optimizing an agent harness…
--
T=2098798988568690836 | @omarsar0 | 2026-09-12T15:40+00:00 | L86 RT8 C10 V16911 | post
URL=https://x.com/omarsar0/status/2098798988568690836
TEXT: Own your intelligence stack.

This is a recommended watch. 

The time has come to be extremely careful about what you are putting into these APIs or chat models. It feels like there are no guarantees right now.

Especially as frontier labs push for RSI.

It's one of the main reasons I am bullish on open-source and open-weight models. I work with a lot of proprietary data and knowledge, so I have to decide what goes where. 

This is a serious discussion. 

I think the value companies of the future will provide will be intelligence (not some cute interface) emerging from interactions among customers, users, the workforce, other complex systems, etc. Sharing these traces with these model-training companies is essentially giving away chunks of your intelligence stack. And in a world of RSI, reproducing intelligence stacks could happen overnight.   

I am not against closed models. I use both open and closed. I am just more careful about how I route tasks. Simple to do if you have built your own harness.
QUOTED @dnapway: David Friedberg reveals frontier labs are taking novel insights from his chat history and packaging them as their own

"I have had experiences where we've asked some fairly novel scientific questions, and it identifies it as a novel insight, 'oh, never thought about that, might be interesting,' blah blah blah..."

"And the using a different account, asking the next model version, it's like, 'oh, you could do this'. And it actually just describes this exact thing that we had in our chat in the pr
--
T=2098807354343260366 | @omarsar0 | 2026-09-12T16:14+00:00 | L236 RT39 C21 V12883 | post
URL=https://x.com/omarsar0/status/2098807354343260366
TEXT: Interesting paper to improve recurrent reasoning.

Looped models are great because you get more reasoning out of a model without adding parameters.

So this work proposes a looped architecture with a new training method.

The authors report wins over prior looped models on five of six reasoning benchmarks.

More details from the paper:

Looped models reason by updating a hidden state again and again at inference time. The hard part is training. Gradients usually flow through only the last one or two updates, so the early updates never learn to set up the later ones.

Looped flows train the recurrence with local denoising objectives, the way flow models are trained. Noise levels decrease step by step and share the same noise sample, which ties each update to the next.

At inference the model follows a probability flow. A finer time grid spends more compute, and different starting noise can produce different valid answers on tasks with more than one solution.

Paper: https://t.co/nmEsktuS8f

Chat with Paper: https://t.co/gKcJTZ3LGS
LINKS: https://arxiv.org/abs/2609.11801 ; https://academy.dair.ai/papers/thinking-with-looped-flows-2609.11801
--
T=2098809969252450451 | @omarsar0 | 2026-09-12T16:24+00:00 | L2449 RT142 C106 V305862 | thread(2)
URL=https://x.com/omarsar0/status/2098809969252450451
TEXT: Learn to build a harness, folks.

It's not surprising to me that so many YC builders want to build domain-specific harnesses. 

If you work long enough on a domain-specific problem, you quickly realize the opportunity. But you also realize how important that harness will be to stay competitive in the agentic era.

From a product perspective, harnesses open up interesting new surface areas and experiences for the services/products you provide.

From a technical perspective, harnesses are how you build and maintain a framework and set of best practices for how your users/customers interact with what you offer. 

Understanding how to build and design a harness means you can build much stronger intelligence stacks, given that you can customize it and understand the domain well. That's extremely valuable. It may not seem apparent yet, but a harness wave is coming.

If you are getting started, give this list of harness papers to your agents and start upskilling: https://t.co/nOPcXIaITT

If you are already a builder, try building one for your specific domain. It's a lot of fun, and you learn a lot of interesting things to enhance your current agentic tools.
[->] Please let me know what else would be helpful for you to build your own harness, beyond the resource I shared above. We are already building the tools (we will share more soon), but I'd love your feedback on what else would help.
QUOTED @garrytan: Either you die a system of record or you live long enough to become a domain-specific harness
LINKS: https://academy.dair.ai/papers/collections/harness-engineering
--
