# X-FEED 2026-09-17 part 5/8 | items: 6

## @omarsar0 — 12 шт.

T=2100193930335637813 | @omarsar0 | 2026-09-16T12:03+00:00 | L109 RT16 C8 V38659 | rt
URL=https://x.com/omarsar0/status/2100193930335637813
RT-OF @dair_ai (L109): Interesting safety paper from Microsoft.

They find that a weaker, unaligned model can split a harmful task into harmless-looking subquestions, ask an aligned frontier model each one in a separate session, and combine the answers locally.

The authors call this capability laundering.

Each request passes on its own, because no single answer from the frontier model is a harmful task.

They tested GPT-5.5, Claude Opus 4.8 and Grok-4.3 as the consulted models. On CyBench, Gemma-4-31B recovered 8 of 14 tasks it failed alone when it consulted GPT-5.5. On a CBRN attack chain, consultation raised its mean rubric score from 62.3 to 83.1.

Paper: https://t.co/7WXEIbG7x2
RT-URL=https://x.com/dair_ai/status/2100167820135059579
TEXT: RT @dair_ai: Interesting safety paper from Microsoft.

They find that a weaker, unaligned model can split a harmful task into harmless-look…
LINKS: https://academy.dair.ai/papers/divide-consult-conquer-capability-laundering-through-aligned-llms-2609.15383
--
T=2100219606405431391 | @omarsar0 | 2026-09-16T13:45+00:00 | L137 RT10 C61 V20974 | post
URL=https://x.com/omarsar0/status/2100219606405431391
TEXT: If you build agent harnesses, this is important.

Should you avoid subagents, or can they be useful?

My thoughts as a harness builder:

I remember using subagents in Claude Code, and I mostly found them useful for parallelizing research. I didn't trust them for other things like coding. 

In fact, I think parallelization, monitoring/tracking, and better context management are two of the best arguments for using subagents.

But are those reasons enough to justify the cost? 

It depends. For code review, I think subagents are amazing and a great fit. And I like that you can do this efficiently with subagents.

Subagents work well if the orchestrator (manager) agent can coordinate the task and the subagents (executors) properly.

Like Eric, I have found that combining one orchestrator agent and one executor subagent typically works best right now. If you try, for instance, to add another subagent to the mix, things start to collapse. 

What's been interesting is that these patterns work even when mixing model families. It feels like frontier models are trained to do this well. 

Coordination is where multi-subagent architectures fall apart, and I think that's what Eric is pointing to. And the cost is just not worth it in most cases. 

So when you see someone on X bragging bout their 100+, 2+ levels deep multi-agent system, you almost certainly know it's made up. 

But it's surprised me that we haven't made much progress on subagents. 

Although I have seen a few papers and engineering blogs sharing success using a form of message board or scratchpad with multi-agent systems. It's incredible how far harness engineering can take you. This tells me that maybe subagents could be a context engineering problem, i.e., frontier models don't do so well when context is too diverse.

This is interesting, as it might be that frontier models simply haven't been trained enough to be robust to this. 

Which brings me to a point I have been raising more recently on avoiding using models to generate harnesses on the fly. They are cost-prohibitive and really hard to make them work on domain-specific tasks (see dynamic workflows from ant). But more on this another day.

I still think subagents are a useful primitive for agent harnesses. For long-horizon, complex tasks, I think they could be extremely useful for improving efficiency. For instance, subagents can explore experiments in parallel in research automation tasks. 

For agent teams, I also think subagents remain relevant. But until we solve the cost or coordination problem, it will take time for the subagent pattern to be widely adopted. 

I have more to share, but what has your experience been? Curious to know.
QUOTED @pvncher: I hate to say it, but if you’re running more than 2 sub agents at time, you’re almost certainly burning tokens for 0 quality gain.

Agents don’t trust each other enough to avoid double-checking everyone’s homework.
--
T=2100235516918849661 | @omarsar0 | 2026-09-16T14:49+00:00 | L139 RT14 C17 V10899 | post
URL=https://x.com/omarsar0/status/2100235516918849661
TEXT: Banger paper from NVIDIA.

It's on the topic of choosing which models go into a multi-agent system.

The team compared eight selection strategies, based on size, accuracy, answer diversity and error diversity, across routing, majority vote and LLM-as-judge setups on hard science benchmarks.

Larger pools of different open models raised the theoretical best-case accuracy. Achieved accuracy often fell below the single best model in the pool.

Using several copies of one model worked better.

Majority vote over the best single model raised HLE accuracy from 29.4% to 32.2%, while nearly every mixed-model group declined.

Choosing candidates from a single model family gave the largest improvement over a standalone model of all eight strategies.

Before adding another model to a router or ensemble, measure what it adds.

Paper: https://t.co/CzF2l8AOI7

Chat with Paper: https://t.co/ozsgU5cOZn
LINKS: https://arxiv.org/abs/2609.17306 ; https://academy.dair.ai/papers/mo-models-mo-problems-how-to-best-select-model-pools-when-designing-multi-agent-2609.17306
--
T=2100240914732155284 | @omarsar0 | 2026-09-16T15:10+00:00 | L97 RT16 C6 V9677 | rt
URL=https://x.com/omarsar0/status/2100240914732155284
RT-OF @dair_ai (L97): Banger paper from Google Research.

This one is on how LLM assistants reason about the people in a user's life.

People ask assistants for social advice constantly, and the assistant only hears the user's version of events.

Measuring whether it reads the situation correctly is hard, because other people's intentions have no ground truth.

Fuse builds that ground truth with simulation.

A target agent with a hidden motive interacts with other agents, including one playing the user. The user agent then describes what happened to the assistant, which has to infer the motive.

The team validated the simulations with 24k human annotations and tested 12 LLMs.

Hearing events through the user makes the task harder. Biased framing from the user shifts the assistant's answer. Models sometimes need more detail than humans do, and longer conversations with room for clarifying questions did not reliably help.

They release the framework and 21k examples.

Paper: https://t.co/duhlHESQai
RT-URL=https://x.com/dair_ai/status/2100235768975511752
TEXT: RT @dair_ai: Banger paper from Google Research.

This one is on how LLM assistants reason about the people in a user's life.

People ask as…
LINKS: https://academy.dair.ai/papers/verifiable-social-reasoning-for-llm-assistants-2609.17496
--
T=2100245953278279715 | @omarsar0 | 2026-09-16T15:30+00:00 | L18 RT1 C10 V8610 | post
URL=https://x.com/omarsar0/status/2100245953278279715
TEXT: This will matter a lot as agent work gets more complex.

We version-control the code agents produce. 

But the next step is reserving the session behind that code.

AgentGit lets you save, resume, share, and hand off agent sessions for seamless context collaboration.
QUOTED @EinsiaAI: An AI agent spends hours on a task. Why should all that work disappear when someone else takes over?

Einsia AI’s answer is AgentGit—an open-source platform for collaborating on agent sessions, so work can be saved, handed off, and continued by the next person.

Explore how others solve problems, and share your agent experience with the world.

Try AgentGit 👇
https://t.co/wUvTWyXnYY

#OpenSource #AIAgents #DeveloperTools #DevTools
--
T=2100298017664623088 | @omarsar0 | 2026-09-16T18:57+00:00 | L40 RT6 C9 V7711 | post
URL=https://x.com/omarsar0/status/2100298017664623088
TEXT: Proactive agents remain an unsolved problem. 

Agents are much more useful when they can act on their own.

Delos gives each AI worker its own email, phone number, and Microsoft or Google account. Your team reaches it on Slack, Teams, email, or phone, and it follows up on work without waiting for a prompt.

It's already running in 300+ companies. I've been writing about proactive agents all year, and this is the direction I'm most excited about.
QUOTED @pierre_dlgr: We just raised €10M to build the biggest AI workforce in the world : AI workers.  

Real AI colleagues, with a face, a job and a professional identity : mail, phone, Microsoft or Google account.   

✉️ 📞💬 Reachable by any channel 
💪 Working proactively 
🏪 Learning 24/7 with the ability to self-configure.   

Already in production in 300+ companies

Huge thanks to @Bpifrance @c4ventures @foundersfuture for this amazing round. 🔥  

The next generation of companies won’t  have AI tools, they’ll hav
--
