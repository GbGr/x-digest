# X-FEED 2026-08-25 part 7/8 | items: 8

## @omarsar0 — 9 шт.

T=2091854106809819257 | @omarsar0 | 2026-08-24T11:44+00:00 | L135 RT16 C7 V33080 | rt
URL=https://x.com/omarsar0/status/2091854106809819257
RT-OF @dair_ai (L135): https://t.co/phmv7KQC0l
RT-URL=https://x.com/dair_ai/status/2091553924725502324
TEXT: RT @dair_ai: https://t.co/phmv7KQC0l
LINKS: http://x.com/i/article/2091553328425582592
--
T=2091869893339812222 | @omarsar0 | 2026-08-24T12:47+00:00 | L270 RT40 C33 V24115 | post
URL=https://x.com/omarsar0/status/2091869893339812222
TEXT: Very interesting new paper from NVIDIA.

(bookmark it)

It takes a closer look at evaluating agent skills.

Enterprise teams are starting to leverage shared skill libraries, and the review gate is typically a scanner that checks structure, style, and security.

NVIDIA measured whether that gate predicts anything.

Across 145 real skills from internal and public catalogs, structural scan scores correlate with LLM-judge quality at a Spearman rho of 0.14.

ACES proposes Skill Lift instead.

In other words, run the same task twice under the same model, sandbox, workspace, and scorer, once with the skill loaded and once without. Then you measure the difference in what the agent completed.

They scored 947 paired cases from 58 production skills across four harnesses, normalizing trajectories into a shared Agent Trajectory Interchange Format, so results compare across harnesses.

They fins that the largest process-metric gains appear in skill execution, behavior check, and skill efficiency.

Paper: https://t.co/NDIO8yF3nr

Track more trending AI papers in our academy: https://t.co/1e8RZKs4uX
LINKS: https://arxiv.org/abs/2608.20614 ; https://academy.dair.ai/
--
T=2091871093401272773 | @omarsar0 | 2026-08-24T12:51+00:00 | L24 RT6 C7 V7152 | post
URL=https://x.com/omarsar0/status/2091871093401272773
TEXT: Own your intelligence stack. 

That’s what I would advise anyone building today. Whether you are starting or in the process.

Part of that is understanding how to build the foundational technology and the application/experiences on top of it.
QUOTED @paulg: Someone asked what I'd do if I were 17. I'd learn how to build LLMs from scratch, and then train ones as powerful as I could with whatever hardware I could get access to.
--
T=2091904961403601076 | @omarsar0 | 2026-08-24T15:06+00:00 | L33 RT0 C2 V9024 | post
URL=https://x.com/omarsar0/status/2091904961403601076
TEXT: It's a great model. I've been having fun using it with Pi.

You can test Ox Alpha with Pi or Hermes Agent for free in our harness playground: https://t.co/7ivyJJ9xu2
QUOTED @pidotdev: Ox Alpha is currently the most popular model on @OpenRouter and is free to use! 

A reasoning model designed for coding, sustained agentic work and production workloads. 1M token context window, with support for text, image and video input. 

Try it out in Pi today https://t.co/5joP3ayfnA
LINKS: https://academy.dair.ai/dashboard/playground
--
T=2091915910680395794 | @omarsar0 | 2026-08-24T15:49+00:00 | L52 RT10 C11 V12501 | thread(2)
URL=https://x.com/omarsar0/status/2091915910680395794
TEXT: If you are curious to learn more about exo, I've built a free hands-on lab on it. Use the real exo CLI in a live terminal with no API key needed.

https://t.co/cyxKWt7M7X https://t.co/7FhHaxhyrf
[->] Solving recursive self-improvement with a harness.

The big question with the agent harnesses I use is: how does it support RSI and compound on every iteration?

What capabilities do I need to own the harness? 

What are the best solutions right now?

Something important to understand when using harnesses. Once an agent starts rewriting its own prompts, tools, and memory, you need durable state underneath it that the agent cannot modify, plus a way to roll a run back to an earlier checkpoint.

exo is a new open-source agent harness built to solve exactly that. It splits an agent into three layers.

1) The exoharness stores everything durable. Conversation history is an append-only event log the agent cannot alter, and it holds artifacts, secrets, and sandbox lifecycle alongside it.

2) The executor decides how the agent behaves. It assembles the prompt, calls the model, dispatches tools, and manages memory. The agent can rewrite any of that, and you can swap the executor for another harness.

3) The sandbox runs the important work. Packages, files, and commands execute in an isolated machine you can snapshot and rewind.

You can do many things with that setup.

- Fork a conversation from any event and run two versions of the same task

- Roll back to the event right before an agent broke itself

- Resume a conversation weeks later with its full history and its own mount

- Read which commands actually ran from tool_requested and tool_result

Agents will keep taking on more of their own configuration, and that raises the bar for the harness underneath them. It reaches a point where an event log, forking, and rollback are must-haves.
LINKS: https://academy.dair.ai/labs/intro-to-exo
--
T=2091951905291284614 | @omarsar0 | 2026-08-24T18:12+00:00 | L28 RT3 C5 V6767 | post
URL=https://x.com/omarsar0/status/2091951905291284614
TEXT: Very cool launch from the @agentsky_dev team. Agent Playground lets you give Claude Code, Codex, and DeepSeek the identical task in one browser and compare time, cost, and tokens side by side. 

I run same-task harness tests constantly, and I think this is one of the first places agents can be compared under truly identical conditions. It's great because you can make a better decision about which agent harness is best for the desired task.
QUOTED @quxiaoyin: I ran the same task on Claude Code and DeepSeek's new agent harness. One cost $150. The other cost $2.
 Today we're launching https://t.co/twx6etZb3X (@agentsky_dev), the "OpenRouter for Agents" — one API → Claude Code, Codex, DeepSeek, Kimi, OpenCode, and every major agent in the cloud.  
And Agent Playground on top: race them on your own task, with your real tools (GitHub, Gmail, more), side by side in a browser: time, cost, tokens burnt.  

Guess which one was $2.
--
T=2091967838135148931 | @omarsar0 | 2026-08-24T19:16+00:00 | L51 RT8 C13 V6875 | rt
URL=https://x.com/omarsar0/status/2091967838135148931
RT-OF @dair_ai (L51): // Applying Anthropic Primitives at Large Enterprises //

Frontier models collapsed the cost of writing custom code.

But they did not reduce the cost of reviewing and maintaining it.

Each bespoke solution drifts from the next. This means that there is a huge tax that goes into understanding them because this means reading their codebase from scratch.

The usual answers, an off the shelf product, a graph orchestration framework wired per use case, or a low code platform used as orchestrator, are custom every time and limited in scope.

This position paper argues for the harness paradigm instead. One coding agent harness runs unmodified as the backbone, with identical code across every deployment.

It builds on three recent findings. Harnesses suffice at the task level and outperform more elaborate architectures on enterprise work. Harness choice accounts for more variance in agent benchmark results than model choice does.

Paper: https://t.co/xVXZEZUwfb

Track more trending AI papers in our academy: https://t.co/LRnpZN7L4c
RT-URL=https://x.com/dair_ai/status/2091896571730493746
TEXT: RT @dair_ai: // Applying Anthropic Primitives at Large Enterprises //

Frontier models collapsed the cost of writing custom code.

But they…
LINKS: https://arxiv.org/abs/2608.20622 ; https://academy.dair.ai/
--
T=2091989634783862906 | @omarsar0 | 2026-08-24T20:42+00:00 | L74 RT9 C9 V12360 | post
URL=https://x.com/omarsar0/status/2091989634783862906
TEXT: Recommended reading and a really cool idea. 

There are a lot of interesting harness designs that are starting to emerge around tool calling and code execution. RLM is one of them. But so is this Speculative Programmatic Tool Calling approach (from the same author of RLM). 

There are plenty of ways to gain efficiencies at the harness layer. 

Harnesses make agents wait: the model streams a block of code, and tool calls inside it only run once generation finishes. sPTC launches the safe calls early against a copy of the environment, so tool latency overlaps with token generation instead of adding on top of it. Bad guesses get thrown away. So far it's 1 to 1.2x speedup. Very promising.
QUOTED @a1zhang: Introducing Speculative Programmatic Tool Calling (sPTC)!

A general class of technique for speculating on tool calls during code generation in a harness and queuing them early to overlap with token generation + REPL execution time.

Blog: https://t.co/0nzkLvTXNy https://t.co/SVH8D2JyEg
--
