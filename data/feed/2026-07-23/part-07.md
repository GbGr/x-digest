# X-FEED 2026-07-23 part 7/9 | items: 12

## @omarsar0 — 11 шт.

T=2079890456855326925 | @omarsar0 | 2026-07-22T11:25+00:00 | L79 RT5 C5 V19053 | rt
URL=https://x.com/omarsar0/status/2079890456855326925
RT-OF @omarsar0 (L79): I was a bit too early on this. 

But I highly recommend reading it. 

It essentially packages two ideas mentioned by both Claude (recording skills) and Andrej Karpathy (rich multimodal prompting) today. 

Lots of people seem to be picking this up now.
RT-URL=https://x.com/omarsar0/status/2079726383496826940
TEXT: RT @omarsar0: I was a bit too early on this. 

But I highly recommend reading it. 

It essentially packages two ideas mentioned by both Cla…
--
T=2079890834950967615 | @omarsar0 | 2026-07-22T11:26+00:00 | L110 RT11 C17 V17203 | rt
URL=https://x.com/omarsar0/status/2079890834950967615
RT-OF @omarsar0 (L110): Here is how I use agent teams for AI research.

I use an LLM Council.

It’s not just about creating multiple agents. You need to set roles and goals carefully.

Here's how I built it with @raft_hq: https://t.co/XBmsngikmh
RT-URL=https://x.com/omarsar0/status/2077765052434633023
TEXT: RT @omarsar0: Here is how I use agent teams for AI research.

I use an LLM Council.

It’s not just about creating multiple agents. You need…
--
T=2079930722232754623 | @omarsar0 | 2026-07-22T14:05+00:00 | L76 RT14 C10 V9746 | post
URL=https://x.com/omarsar0/status/2079930722232754623
TEXT: I agree with what this AI paper suggests.

Self-improving agents should evolve their benchmarks too.

(bookmark it)

Self-improving agents are one of the most important directions in AI right now, and most of them optimize against a fixed benchmark. This paper argues the benchmark should evolve alongside the agent.

The setup is a self-evolving Lean proof agent. A small trusted runtime wraps a fully mutable workspace of workflow, prompts, and tools, so the agent can rewrite how it decomposes proofs, uses compiler feedback, and repairs failures.

What makes it different is coevolution. Between generations the champion revises the active task distribution through a mastery-throttled curriculum that adds harder proof obligations only after the current level is mastered.

All of it stays inside a Lean-grounded loop, so a success counts only when the behavior yields verified proofs under a trusted snapshot. Over 15 generations the best coevolving agent reaches 45.1% held-out solve rate on miniF2F, versus 12.7% for the seed and 32.0% for the best fixed-benchmark agent.

Grounding every reward in a formal verifier is how you get self-modification without reward hacking, and coevolving the curriculum pushes the ceiling higher.

Paper: https://t.co/NDiN8RMcXO

Learn to build effective AI agents in our academy: https://t.co/1e8RZKs4uX
LINKS: https://arxiv.org/abs/2607.17352 ; https://academy.dair.ai/
--
T=2079932253421867301 | @omarsar0 | 2026-07-22T14:11+00:00 | L78 RT9 C7 V13273 | post
URL=https://x.com/omarsar0/status/2079932253421867301
TEXT: Recommended reading. 

"Gigatoken can tokenize the entire internet in &lt;7 hours on one machine."

It can tokenize data at GB/s. That's a big deal. 

&gt; pip install gigatoken
QUOTED @marcelroed: Introducing the world's fastest tokenizer implementation, Gigatoken!

Gigatoken is ~500-1000x faster than HuggingFace, and ~100x faster than OpenAI's tiktoken for most tokenizer definitions on most machines.

These baselines are already multithreaded Rust implementations! 🧵 https://t.co/zxzXPFBCHv
--
T=2079956798816063818 | @omarsar0 | 2026-07-22T15:48+00:00 | L4 RT1 C2 V1373 | post
URL=https://x.com/omarsar0/status/2079956798816063818
TEXT: It looks like it only works for Claude Cowork. That's really annoying. I think it's really worth it to build your own orchestrator tool and build these features out yourself. This is the future of how to work with agents, so you can't just be waiting for someone to build this out for you. There are many interesting variants of this as well.
--
T=2079959935031591112 | @omarsar0 | 2026-07-22T16:01+00:00 | L75 RT12 C13 V8663 | post
URL=https://x.com/omarsar0/status/2079959935031591112
TEXT: Are structured outputs in agents always good?

This paper suggests that you might have to take a closer look.

Your product's structured output surface is measurably more homogeneous than the chat surface you benchmarked it on.

Teams treat structured output as a formatting choice with no effect on content. This new work from Cornell tests that assumption across 44 models and finds the format itself reshapes the answers.

On an open-ended pick-a-word prompt, simply requesting JSON pushes the modal answer from 41% to 64% of responses and cuts distinct answers from 52 to 36.

The collapse shows up for JSON and XML, the formats models were post-trained to emit, and disappears for YAML and CSV. Enforcing a schema at the decoder compresses nothing further, which points the narrowing back to how the model answers the register itself.

Why does it matter?

Any pipeline leaning on JSON mode for variety is sampling from a smaller pool than it thinks.

Paper. https://t.co/xUIlDNtgWy

Learn to build effective AI agents in our academy. https://t.co/1e8RZKs4uX
LINKS: https://arxiv.org/abs/2607.18476 ; https://academy.dair.ai/
--
T=2079982491578827214 | @omarsar0 | 2026-07-22T17:30+00:00 | L41 RT10 C3 V17482 | post
URL=https://x.com/omarsar0/status/2079982491578827214
TEXT: https://t.co/juAGYwoKIE
LINKS: http://x.com/i/article/2079981292108582912
--
T=2079983214588731629 | @omarsar0 | 2026-07-22T17:33+00:00 | L83 RT13 C11 V11390 | thread(2)
URL=https://x.com/omarsar0/status/2079983214588731629
TEXT: Karpathy's point about long voice rambles goes further when you add more modalities.  

My favorite way to prompt agents lately is a bigger unit I've been calling a task.  

A task bundles a long voice note, the current screen, annotations, and exact text into a single turn. The agent reconstructs my intent from all of those signals, so most of the correction loops disappear and I can hand off larger pieces of work.
[->] I will be doing a live session on this for our community. Join us here: https://t.co/aG0VzVZyhP
QUOTED @omarsar0: https://t.co/juAGYwoKIE
LINKS: https://academy.dair.ai/events/czm9avwd8imz28tk9hi699dei
--
T=2079991914841997430 | @omarsar0 | 2026-07-22T18:08+00:00 | L16 RT2 C3 V6945 | post
URL=https://x.com/omarsar0/status/2079991914841997430
TEXT: It sucks that with most coding agents you have to call out the skill every single time. 

The agent should just know when and what set of skills to use. @boltdotnew Skills solves this with skill auto-matching.

This compounds nicely when you build with agents as a team.
QUOTED @boltdotnew: There's a whole new way to use skills in Bolt.

Every skill your teammates build is now yours too. And they stack: one prompt triggers all of them, automatically.

Here's how it works 🧵 https://t.co/lS1TpDmW8L
--
T=2080034479020593525 | @omarsar0 | 2026-07-22T20:57+00:00 | L36 RT2 C9 V6526 | thread(2)
URL=https://x.com/omarsar0/status/2080034479020593525
TEXT: Recommended reading. Cursor Router routes tasks to the right model. 

Is anyone building this as open-source? It feels like this is something you don't want to offload to an API. We all work with different trade-offs, so we need the ability to achieve custom routing. https://t.co/Vw2xyMy1jp
[->] In addition, something I have been building in my orchestrator system is to dynamically route to several models at once when needed. Or split the task to be handled by different models. I will share something similar I have been working on sometime this week.
QUOTED @cursor_ai: Introducing Cursor Router, our intelligent model router that selects the right model for the task at hand.

Router delivers frontier-quality results at 60% lower cost. https://t.co/R0YABowFKg
--
T=2080039840200978917 | @omarsar0 | 2026-07-22T21:18+00:00 | L23 RT1 C5 V5761 | post
URL=https://x.com/omarsar0/status/2080039840200978917
TEXT: Just implemented a new interface for our @dair_ai  community.

I first brainstormed a concept design with Fable 5 using an HTML artifact (attached image). Then I gave it to GPT-5.6-Sol to build it.

Artifacts work great as prompts. Combining models gives you efficiency gains. https://t.co/QnKfodMfWx
--
## @RLanceMartin — 1 шт.

T=2079810042489094518 | @RLanceMartin | 2026-07-22T06:05+00:00 | L3606 RT319 C83 V420372 | rt
URL=https://x.com/RLanceMartin/status/2079810042489094518
RT-OF @ClaudeDevs (L3606): https://t.co/rx3FQSosu0
RT-URL=https://x.com/ClaudeDevs/status/2079654423828304282
TEXT: RT @ClaudeDevs: https://t.co/rx3FQSosu0
LINKS: http://x.com/i/article/2077886850262503424
--
