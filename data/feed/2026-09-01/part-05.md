# X-FEED 2026-09-01 part 5/7 | items: 8

## @omarsar0 — 10 шт.

T=2094432587821482036 | @omarsar0 | 2026-08-31T14:30+00:00 | L298 RT42 C24 V23153 | post
URL=https://x.com/omarsar0/status/2094432587821482036
TEXT: This WikiSkill paper from Google is a must-read.

At a high level, it shows the effectiveness of persistent agents, knowledge bases, and skills.

@karpathy popularized LLM Wikis.

But this paper provides an actual framework for how agents can tap into a wiki of skills that evolve.

What's fascinating to me is how this can complement your agents.

LLMs can only learn so much about the world. External knowledge is crucial to get agents to do tasks efficiently and accurately in the real world.

So this is why I think this paper is an important one, as it tries to fix some of the common issues you face when building and maintaining skills.

It automatically leverages your agent runs, persists that knowledge into a wiki, and uses all of that to keep skills properly tuned for reusability.

The most impressive part of WikiSkill is that it appears to be model-agnostic. In other words, it works across different tasks and models.

The evolved skills can even transfer to smaller models that sometimes outperform bigger models. This hints at the effectiveness of persistent agents, via persistent knowledge bases and evolved skills.

The big question for me is how evolved skills coming out of WikiSkill transfer to the next generation of models. I think they will provide a huge advantage and be leveraged in more interesting ways by smarter models.

The practical takeaway here is that we should all be thinking about how to build persistent knowledge bases across our companies and projects. And how to use that to upgrade and evolve our skills.

Join our community to discuss this paper more: https://t.co/AsWbH4jzgn
LINKS: https://academy.dair.ai/papers/wikiskill-compiles-agent-experience-into-a-persistent-wiki-2608.27454
--
T=2094444179824710086 | @omarsar0 | 2026-08-31T15:16+00:00 | L31 RT0 C11 V12887 | post
URL=https://x.com/omarsar0/status/2094444179824710086
TEXT: I get Gavin here. I used to operate like this as a CS PhD. 

With recent advances in AI and how it is accelerating discoveries and progress, I've had to change how I approach discussing technological progress.

I argue that an important skill today is learning to quickly adapt to change and be willing to update your opinion and thoughts on certain subjects. 

It's okay to be a skeptic; that's what being a PhD is about, but you also need an open mind, especially given the rapid pace of progress across the board. 

I have learned this the hard way. I have learned to listen to different perspectives to make more sense out of what's happening. It's hard, but it's part of the job as someone who specializes in developing deep expertise around a subject.
QUOTED @GavinSBaker: Talking to brilliant physicists who have thought about orbital compute for 3 hours and are convinced it will never work makes me think of this Keanu Reeves quote:

“I'm at that stage in life where I stay out of arguments. Even if you say 1+1=5, you're right. Have fun."
--
T=2094477636667945110 | @omarsar0 | 2026-08-31T17:29+00:00 | L44 RT6 C8 V10841 | post
URL=https://x.com/omarsar0/status/2094477636667945110
TEXT: Good paper on long-horizon scalable agent skills.
QUOTED @dair_ai: Great paper from Google and colleagues.

It proposes an interesting approach to improve agents on long-horizon tasks.

Long-running agents slow down and start poisoning their own context.

Both symptoms come from the same design choice, which is keeping execution alive by appending every observation, action, and reasoning trace to a growing conversation.

SKILL.state replaces that history with an explicit mutable execution state.

At each step the model sees only the immutable skill specificatio
--
T=2094499914281566241 | @omarsar0 | 2026-08-31T18:57+00:00 | L202 RT17 C33 V27674 | post
URL=https://x.com/omarsar0/status/2094499914281566241
TEXT: Next to evals, harness engineering is quickly becoming one of the most important skills for AI engineers to have today.
--
T=2094505508850032852 | @omarsar0 | 2026-08-31T19:20+00:00 | L99 RT15 C15 V8957 | post
URL=https://x.com/omarsar0/status/2094505508850032852
TEXT: Interesting paper from Tencent.

Tencent trains an agent to manage its own working context, and assigns credit at the level of individual context edits.

Long-horizon tasks force a model to retrieve, integrate and maintain scattered information across many turns, and keeping every interaction history makes the working context grow without bound.

Recent proactive methods let a model edit its own context with tools, but the toolset stops at search, deletion and summarization.

ContextPilot adds global planning, long-term memory and adaptive soft compression, so the agent can offload information rather than only discard it.

The training side is where it gets interesting. Standard RL hands the final trajectory reward to every intermediate edit equally. ContextPilot uses context and entropy variation to find which editing decisions actually mattered, samples branches at those points, and estimates action-level advantages from all branched trajectories passing through that edit.

On long-context QA and deep search it beats existing baselines across several base models while holding a more compact working context. Code is available.

Paper: https://t.co/buM6galu4x

Chat with Paper: https://t.co/VN5J5PO4Rt
LINKS: https://arxiv.org/abs/2608.28476 ; https://academy.dair.ai/papers/contextpilot-teaching-agents-for-proactive-context-management-via-fine-grained-r-2608.28476
--
T=2094516128366174631 | @omarsar0 | 2026-08-31T20:02+00:00 | L78 RT10 C12 V7295 | rt
URL=https://x.com/omarsar0/status/2094516128366174631
RT-OF @dair_ai (L78): Loop engineering has emerged as a new skill for AI engineers

But there is very little research measuring how effective it is.

The best results on full tasks in a new benchmark is ~25%.

LoopArena from AMAP evaluates the outer loop rather than the coding agent.

A Controller model receives a structured summary after each round and instructs a separate fixed Worker agent on what to do or verify next, or decides to stop. Holding the Worker constant makes the result readable, since an end-to-end run cannot tell you whether success came from the guidance or from the agent carrying it out.

The named failure modes will be familiar to anyone running long agent sessions:

- Trusting a stale progress note
- Skipping needed verification
- Spending budget in the wrong direction
- Stopping before the task is safe to submit

Paper: https://t.co/ZGiooDsN34

Chat with Paper: https://t.co/jSeFFp3CBc
RT-URL=https://x.com/dair_ai/status/2094511549306315189
TEXT: RT @dair_ai: Loop engineering has emerged as a new skill for AI engineers

But there is very little research measuring how effective it is.…
LINKS: https://arxiv.org/abs/2608.28281 ; https://academy.dair.ai/papers/looparena-benchmarking-models-as-runtime-controllers-for-loop-engineering-2608.28281
--
T=2094521097613881559 | @omarsar0 | 2026-08-31T20:21+00:00 | L33 RT2 C7 V8241 | thread(2)
URL=https://x.com/omarsar0/status/2094521097613881559
TEXT: The interfaces you see in the clip are generated directly by the model. 

Generated in real time without code or HTML.

That's nuts!

Just thinking to myself all the things you could build with an interface world model like this. Simulators, games, etc.
[->] This also got me thinking about this tweet from @karpathy a few months back. 

Not entirely interactive neural videos/simulation but I think somewhere between 3 and n (much closer to n). https://t.co/Yu1mSflOjE
QUOTED @runwayml: Today, we're sharing new research on Solaris, our first Interface World Model.

Solaris is a new kind of operating system that generates interactive interfaces frame by frame, in real time, with no code. We find that Solaris outperforms frontier LLMs when generating new interfaces, across structural similarity and information retention. Read more and request early access at the link below.
--
T=2094543409738285473 | @omarsar0 | 2026-08-31T21:50+00:00 | L114 RT11 C12 V17951 | post
URL=https://x.com/omarsar0/status/2094543409738285473
TEXT: Persistent agents are coming.

Just take a closer look at the agent functionalities in this Hermes Agent Pantheon release. 

I am so impressed with how fast the Hermes Agent team ships.
QUOTED @Teknium: Hermes Agent v0.21.0 is now out!

- Bots Mode
- Agent 2 Agent Comms
- Persistent Multi-Gateway Connections
- Subagent Steering
- Expanded Connectors Access 

and a lot more!

Check out the release notes below
--
