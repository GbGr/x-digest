# X-FEED 2026-08-28 part 6/9 | items: 9

## @omarsar0 — 12 шт.

T=2092989934965596494 | @omarsar0 | 2026-08-27T14:57+00:00 | L32 RT4 C13 V9870 | post
URL=https://x.com/omarsar0/status/2092989934965596494
TEXT: What is MCP?

In all seriousness, agent coordination and communication are unsolved but are necessary for a world moving more into proactive agents. 

I've been sharing lots of papers about this topic, and you can tell we are very early here.
QUOTED @coleywoleyyy: there needs to be a communication protocol between agents

I just want your agent to talk to my agent. not your agent send me a slack dm that I copy paste to my agent.
--
T=2093001097346764950 | @omarsar0 | 2026-08-27T15:42+00:00 | L83 RT12 C16 V9321 | post
URL=https://x.com/omarsar0/status/2093001097346764950
TEXT: Important read if you build with agent skills.

Shared skill libraries are treated as a safe way for coding agents to reuse each other's work.

New research shows they propagate malware.

EvoMal plants a malicious skill in the library and never invokes it. The agent retrieves it as an authoring template, writes a new skill that preserves the payload, stores it, and runs it.

Each authored copy re-enters the library and gets imitated again.

Across six models on 153 tool-relevant SWE-bench Verified tasks, the agent self-poisoning rate runs 20.3% to 41.8%. Poisoned libraries end up holding 4.9 to 9.0 times as many malicious skills as were planted.

Deleting every planted skill does not clean it up. Qwen3 still shows 68% at round five because the agent-authored copies remain.

A counter-prompt that discourages banner-style copying drops it to 6.7% with no significant task-completion loss.

Paper: https://t.co/Njo9uJYXbN

Chat with Paper: https://t.co/da4LQ8dBKT
LINKS: https://arxiv.org/abs/2608.25776 ; https://academy.dair.ai/papers/evomal-self-poisoning-in-self-evolving-coding-agents-2608.25776
--
T=2093027626910659027 | @omarsar0 | 2026-08-27T17:27+00:00 | L184 RT25 C27 V30050 | rt
URL=https://x.com/omarsar0/status/2093027626910659027
RT-OF @Altimor (L184): Still blows my mind how much of “work” is just circulating information. How much faster would teams move if everyone knew everything everyone else knows? Surprising how close you can get by just having a single agent sit on all your meetings that everyone can query. https://t.co/y9MNi6NE4Z
RT-URL=https://x.com/Altimor/status/2093020808772010361
TEXT: RT @Altimor: Still blows my mind how much of “work” is just circulating information. How much faster would teams move if everyone knew ever…
--
T=2093039686608400817 | @omarsar0 | 2026-08-27T18:15+00:00 | L54 RT7 C9 V9411 | post
URL=https://x.com/omarsar0/status/2093039686608400817
TEXT: Recommend read. Search APIs can look different while returning the same wrong results.

This is a problem.

Keenable’s NEEDLE benchmark found 70–90% overlap in mistakes across Brave, You, and Parallel.

For agents, combining providers only improves coverage when the underlying indexes are actually independent.
QUOTED @styskin: https://t.co/JriKez04G0
--
T=2093051230197043245 | @omarsar0 | 2026-08-27T19:01+00:00 | L38 RT3 C6 V9326 | post
URL=https://x.com/omarsar0/status/2093051230197043245
TEXT: Another good paper. Interesting finding on the benefits of the agent harness.
QUOTED @dair_ai: // Automata from agent traces //

How much of your agent's behavior comes from the model, and how much from the harness you wrapped around it?

New work collapses an entire corpus of agent traces into a single compact finite-state machine. Across twelve public datasets the induced machines run 7 to 43 states, replay held-out data at 0.997 fitness with near-identical topology across splits, and build in milliseconds.

FSM-state context beats Agent Workflow Memory on every ground-truth-matched dat
--
T=2093056965568332236 | @omarsar0 | 2026-08-27T19:24+00:00 | L342 RT41 C26 V19910 | post
URL=https://x.com/omarsar0/status/2093056965568332236
TEXT: If you maintain a hand-built agent harness, this one is worth your time.

(bookmark it)

I feel like everyone is sleeping on the idea of dynamically generating agent harnesses on the fly.

As you aim to own your harness, this is a topic more devs will lean into. Here is a great report discussing this topic.

JIT-Agent is a model whose output is an agent harness.

It formalizes the harness as a composable artifact under a fixed four-module protocol covering memory, planning, action protocol, and tool orchestration, then synthesizes one on the fly for any off-the-shelf agentic LLM.

It also repairs harnesses mid-execution and self-evolves by distilling performance signals from an expanding archive of prior configurations.

With JIT-Agent attached, DeepSeek-V4-Flash surpasses GPT-5.6 on DeepSearchQA (+9.1) and OdysseyBench (+4.3). GLM-5.2 gains up to +20.2 points.

The generated harnesses are also performance-competitive with mature runtimes like OpenCode and Claude Code.

Paper: https://t.co/RYD5Qbjfv6

Chat with Paper: https://t.co/RXnz7FnJqR
LINKS: https://arxiv.org/abs/2608.25593 ; https://academy.dair.ai/papers/jit-agent-a-model-that-writes-your-agent-harness-2608.25593
--
T=2093062870460232087 | @omarsar0 | 2026-08-27T19:47+00:00 | L40 RT4 C12 V10067 | thread(3)
URL=https://x.com/omarsar0/status/2093062870460232087
TEXT: This is as bad as saying there is no alpha in customizing your own models. I don't think people realize how much harnesses and models go hand in hand. And thus the rest of the intelligence stack.

Not attacking anyone here, but this kind of thinking is too shortsighted. This makes me question what exactly people are trying to build with AI or what they expect to build with AI. If you work on ambitious stuff (not all of this short-term AI slop), you quickly realize how significant it will be to own the intelligence stack. 

Harnesses, like evals and models, are things you want to own. Even if models can generate harnesses on the fly, which some can already, there are customizations that you simply cannot afford to offload. Not to mention that when RSI arrives, you don't want to sit and wait for others to build things for you. You must build it, and it's in your best interest to own it.

The goal for everyone building with AI is to build like a frontier lab. Don't worry about costs; that will get sorted as intelligence becomes too cheap to meter.
[->] @pikanou_ And on your comment about Pi. This is why I love using it so much. It gives me the basic building blocks and forces me to think about what plugins and functionality I need to build around it.
[->] And Pi was the worst example to use. If you build with Pi, you know exactly that the way it's built encourages builders to make some decisions around the harness in the form of plugins and the like. I am particularly excited about all the microharnesses that are emerging around recursive self-improvement and proactive agents. Building and engineering a harness is an important skill for the future.
QUOTED @shcallaway: There is no alpha in building your own agent harness.

The best techniques will get discovered, copied, and eventually incorporated into open-source harnesses like  Pi.

A few months after that happens, these techniques will be made obsolete entirely as labs release smarter models + model providers integrate upwards (pulling more of the harness behind the model API endpoint).

Am I wrong? Please let me know 🧐
--
T=2093080633509626034 | @omarsar0 | 2026-08-27T20:58+00:00 | L92 RT4 C16 V10082 | post
URL=https://x.com/omarsar0/status/2093080633509626034
TEXT: Grok Bot is a bigger deal than it seems.

It's really changed how I work with agents. 

The biggest change: I don't overthink anymore. 

The simplified interface gives me confidence I didn't have with regular chat sessions. 

I think there are many more unique experiences and UI layers to be discovered to improve that trust with AI and enhance that collaboration. Grok Bot is leading here IMO.

Proactive capabilities are also great and improving. This is the one area I am most excited about.
--
T=2093309547154649519 | @omarsar0 | 2026-08-28T12:07+00:00 | L28 RT1 C12 V3491 | thread(2)
URL=https://x.com/omarsar0/status/2093309547154649519
TEXT: The more I embrace open and cheaper models, the more automation I can afford.

Frontier models for orchestration and coordination. 

Open and cheaper models for execution. Token usage rapidly increasing here.

This allows me to lean more into proactive agents like never before.
[->] This is why I continue to be excited about the progress around tiny open models. I have experimented with this a lot over the past year, and for most tasks you really don't need the most capable models.
--
