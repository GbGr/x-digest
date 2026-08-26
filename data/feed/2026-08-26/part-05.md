# X-FEED 2026-08-26 part 5/7 | items: 8

## @omarsar0 — 11 шт.

T=2092084945044820047 | @omarsar0 | 2026-08-25T03:01+00:00 | L114 RT15 C11 V19832 | rt
URL=https://x.com/omarsar0/status/2092084945044820047
RT-OF @omarsar0 (L114): Recommended reading and a really cool idea. 

There are a lot of interesting harness designs that are starting to emerge around tool calling and code execution. RLM is one of them. But so is this Speculative Programmatic Tool Calling approach (from the same author of RLM). 

There are plenty of ways to gain efficiencies at the harness layer. 

Harnesses make agents wait: the model streams a block of code, and tool calls inside it only run once generation finishes. sPTC launches the safe calls early against a copy of the environment, so tool latency overlaps with token generation instead of adding on top of it. Bad guesses get thrown away. So far it's 1 to 1.2x speedup. Very promising.
RT-URL=https://x.com/omarsar0/status/2091989634783862906
TEXT: RT @omarsar0: Recommended reading and a really cool idea. 

There are a lot of interesting harness designs that are starting to emerge arou…
--
T=2092246879702769956 | @omarsar0 | 2026-08-25T13:45+00:00 | L170 RT28 C15 V12171 | post
URL=https://x.com/omarsar0/status/2092246879702769956
TEXT: Impressive new paper from Microsoft and colleagues.

Harness design is still hand-tuned almost everywhere. This work present an automated loop to optimize the harness.

They introduce AutoSaddler, which treats the agent harness as code and learns to patch it offline from failure traces.

It runs mini batches of tasks, diagnoses what broke, generates structured patches to prompts, tool configurations, and control logic, then keeps an update only if it survives validation.

Gains of 9.0 points on GAIA2, 9.6 on SWE-Bench Pro, and 10.0 on Terminal-Bench 2.0 over the corresponding base harnesses.

Deep debugging beats shallow reflection, targeted edits beat unconstrained editing, and generalization-aware selection beats repairing the one trajectory in front of you.

Paper: https://t.co/PoDahO6rmz

Track more trending AI papers in our academy: https://t.co/1e8RZKs4uX
LINKS: https://arxiv.org/abs/2608.23041 ; https://academy.dair.ai/
--
T=2092261479055548692 | @omarsar0 | 2026-08-25T14:43+00:00 | L45 RT5 C5 V8893 | post
URL=https://x.com/omarsar0/status/2092261479055548692
TEXT: Recommended read. There are a few interesting harness ideas emerging for recursive self-improvement.
QUOTED @dair_ai: Very interesting new work from Prime Intellect.

Prime Agent is an impressive open-source self-improving harnesses.

It's a harness for long-horizon agent work. A persistent IPython REPL lets the model process its own context programmatically, and a Continual Harness carries histories, memories, skills, prompts, and subagent specifications across trajectories, so improvements compound instead of resetting on every run.

Same model class, ARC-AGI-3 RHAE Best@1 moves from 30% to 95.5%. It also mat
--
T=2092264782791389409 | @omarsar0 | 2026-08-25T14:56+00:00 | L138 RT5 C5 V18989 | post
URL=https://x.com/omarsar0/status/2092264782791389409
TEXT: Recommended read. Proactive agents are a whole new and underexplored category. This microharness is about having a persistent, always-on agent that's always thinking and doing important work.

Proactive agents are exciting because they unlock new ways to work with agents and unlock productivity. 

My proactive harness has a similar functionality that stays running in the background, monitoring and tracking work across projects/tasks, and then, when it has a genuinely useful idea or suggestion, it activates. It learns my preferences as I interact with it over time, so it gets better at recommendations with every interaction.
QUOTED @andykonwinski: Introducing Headlong, an open source microharness for persistent agents: self-guided agents that think continuously.

Most agent harnesses are reactive: you send a task, the agent completes it, and then it sits frozen until the next request. Cron jobs and heartbeats wake it up to run a checklist and put it back to sleep.

A Headlong agent is never asleep. It keeps generating thoughts about whatever it decides is interesting, in a self-guided loop inspired by human inner monologue. Your message d
--
T=2092270101097500954 | @omarsar0 | 2026-08-25T15:17+00:00 | L61 RT1 C8 V12541 | post
URL=https://x.com/omarsar0/status/2092270101097500954
TEXT: Glad Tobi posted about this.

This issue has resurfaced countless times, and they have done nothing about it. It's ridiculous that we have to put up with this stuff. I don't blame Tobi's frustration. I would also like to see that change now.
QUOTED @tobi: I’m thinking about banning Claude code at Shopify until they change their mind and read AGENTS.md and .agents/skills etc. 

Insisting on only reading CLAUDE.md sometimes leads to split brain problems when different team members use different tools. Just unnecessary.
--
T=2092274559898755485 | @omarsar0 | 2026-08-25T15:35+00:00 | L147 RT22 C4 V10211 | post
URL=https://x.com/omarsar0/status/2092274559898755485
TEXT: Impressive work from Alibaba.

(bookmark it)

If you build long-running agents and keep rewriting your memory schema, take a look at this approach.

It basically treats agent context management as a programming task.

Here is how it works:

It backs each agent session with an append-only event log and a sandboxed, persistent Python kernel.

Tool outputs, retrieved history, and derived state bind to typed variables across model calls instead of being serialized into the prompt every turn.

Model-written code searches and transforms that state, and only explicitly printed projections enter the working view.

The event log keeps lossless ground truth, so nothing has to be committed to a compressed form before you know what will matter later.

When the working view nears its budget, stale spans are evicted but stay recoverable. An eviction index keeps compact landmarks tied to exact event-log addresses, so the agent navigates straight back to a region instead of searching the whole log.

Results: with Qwen3.8-Max, 94.8% on LongMemEval_S, 73.1% on BEAM_10M (5.1 points over the best published memory system), and 86.7% on LOCA_256K.

Treating context management as a programming task means it inherits every future improvement in model coding ability.

Paper: https://t.co/RyWaefr67Z

Track more trending AI papers in our academy: https://t.co/1e8RZKs4uX
LINKS: https://arxiv.org/abs/2608.21690 ; https://academy.dair.ai/
--
T=2092277350993895906 | @omarsar0 | 2026-08-25T15:46+00:00 | L34 RT4 C7 V7480 | post
URL=https://x.com/omarsar0/status/2092277350993895906
TEXT: Can't wait to have always-on agents running locally 24x7. Local agents are something Perplexity seems to be chasing these days aggressively, and it makes a ton of sense. There is a huge market for personalized AI agents.
QUOTED @nvidia: Meet Portable Computer, Perplexity's new local-first agent stack on NVIDIA DGX Spark.

When running locally, Portable Computer offers one-click local inference setup and an optimized agentic experience for DGX Spark.

Learn more and get started today: https://t.co/0UElxhCnkY https://t.co/W07ZafKYdC
--
T=2092283622652793134 | @omarsar0 | 2026-08-25T16:11+00:00 | L17 RT2 C1 V7130 | post
URL=https://x.com/omarsar0/status/2092283622652793134
TEXT: Big launch from @KeenableAI. The team built its own crawler, index, and query language for agents in under a year. I think owning the full search stack gives them room to improve quality, latency, and cost together as agent workloads grow. Worth checking out.
QUOTED @styskin: Today we are announcing @KeenableAI, an AI-native index of the best human knowledge we have, starting with the open web.

AI seems to know just about everything until you ask it about something you know deeply. The answer isn’t wrong, but it's just very average.

We started Keenable to fix this problem: every model and every agent should be able to query, reason over, and continuously learn from the living web.

Backed by a $26M Seed from @Accel and @conviction. Built by the team that took on Go
--
