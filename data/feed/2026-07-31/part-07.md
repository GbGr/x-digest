# X-FEED 2026-07-31 part 7/12 | items: 7

## @omarsar0 — 6 шт.

T=2082858249242439997 | @omarsar0 | 2026-07-30T15:57+00:00 | L48 RT7 C9 V8295 | thread(3)
URL=https://x.com/omarsar0/status/2082858249242439997
TEXT: AI tutors are something else when using voice agents.

(🔊sound on)

Just built this math tutor with Fable 5. Voice powered by Grok Voice Think Fast 2.0.

This is rough, but just imagine how much better this will get with newer models. https://t.co/sPnrAunEss
[->] If you want to try this out, join the community here. https://t.co/UV7NNI887f

I will announce it there when it's ready for testing.
[->] I am building this out for my kid at the moment. But let me know if this is a tool that you would love your kid to access. I will be opening it to beta soon.
LINKS: https://academy.dair.ai/dashboard/community
--
T=2082884266019467691 | @omarsar0 | 2026-07-30T17:41+00:00 | L145 RT27 C13 V9989 | rt
URL=https://x.com/omarsar0/status/2082884266019467691
RT-OF @dair_ai (L145): Finally a good paper testing if file-system based memory for LLM agents is worth it.

First, what does this look like?

Deployed agents keep long-term memory as a folder of markdown files they read and reorganize with ordinary file tools.

Two assumptions had never been checked. That an agent can keep a growing store organized as memories accumulate, conflict, and go stale. And whether the organization pays for itself.

Organized stores roughly halve retrieval cost when the material is large. No agent in the study converted organization into better answers, and in the growth study the store degraded for every management agent except the strongest one.

Changing the tool set alone reshapes the memory store as strongly as swapping the model.

Paper: https://t.co/WC6EtdQBfB

Track more trending AI papers in our academy: https://t.co/LRnpZN7L4c
RT-URL=https://x.com/dair_ai/status/2082883931582713893
TEXT: RT @dair_ai: Finally a good paper testing if file-system based memory for LLM agents is worth it.

First, what does this look like?

Deploy…
LINKS: https://arxiv.org/abs/2607.26637 ; https://academy.dair.ai/
--
T=2082925090715418810 | @omarsar0 | 2026-07-30T20:23+00:00 | L72 RT6 C15 V9252 | thread(2)
URL=https://x.com/omarsar0/status/2082925090715418810
TEXT: Intelligence too cheap to meter, they said!

Jokes aside, this is great news. I use this pattern a lot, so I now benefit more from the cheaper GPT-5.6 Terra and the now faster GPT-5.6-Sol. 

This is so underestimated. https://t.co/t6Wv84xGz5
[->] I hear from others that Luna can't be used as a subagent. Well, that's if you are using Codex directly, I guess. In my orchestrator, it works great. 

https://t.co/uBUOFSHWkM
QUOTED @OpenAI: We are committed to pushing the model frontier across cost efficiency, capability, and speed.

Starting today, we are reducing prices for GPT-5.6 Luna by 80% and GPT-5.6 Terra by 20% , and offering a faster option for GPT-5.6 Sol in the API.

Luna and Terra’s lower prices are reflected in how usage is counted in Codex and ChatGPT Work, so your usage goes further.
LINKS: https://x.com/cherry_mx_reds/status/2082889746523603148?s=20
--
T=2082942567352815862 | @omarsar0 | 2026-07-30T21:33+00:00 | L55 RT10 C15 V6887 | post
URL=https://x.com/omarsar0/status/2082942567352815862
TEXT: We have to be careful to not offload our understanding to agents.

I think there is also a good opportunity to build agentic applications that encourage deeper understanding.

For example, coding agents might make developers faster at the task in front of them. But this could leave them unable to extend the code afterward.

Here is what they find in this work:

54 students built a website with either an agent that edits their code or a chatbot where they write the code themselves. Understanding was measured two ways, through comprehension questions and through an extension task performed with no AI at all.

Agents helped with initial completion and hurt comprehension enough that users could not extend their own work.

The damage traces to specific interaction patterns. Copy-and-paste prompting and auto-accepted edits both correlate with lower comprehension, which makes this a harness design problem rather than a verdict on coding agents.

Students reported weaker understanding and still preferred the agent because it was quick and easy. The authors point at dissuading low-effort prompting, generating more readable code, and promoting active engagement.

Paper: https://t.co/wCjDzIWsEu

Track more trending AI research papers at https://t.co/1e8RZKs4uX
LINKS: https://arxiv.org/abs/2607.26375 ; https://academy.dair.ai/
--
T=2082946752189980689 | @omarsar0 | 2026-07-30T21:49+00:00 | L19 RT0 C13 V5990 | post
URL=https://x.com/omarsar0/status/2082946752189980689
TEXT: I don't have any issues with building more efficient software for AI. 

However, I would also like to see more focus on building AI interfaces and experiences that augment humans.
QUOTED @yacineMTB: instead of making software for humans, you should be making software for AIs
--
T=2082972109190435181 | @omarsar0 | 2026-07-30T23:30+00:00 | L918 RT161 C54 V71538 | rt
URL=https://x.com/omarsar0/status/2082972109190435181
RT-OF @omarsar0 (L918): Super interesting new work from NVIDIA.

(bookmark it)

They suggest building agents as Python objects.

Very cool idea and I think it could a lot with agent reliability.

More below:

Agent development today spreads across prompt templates, tool schemas, callback code, and workflow graphs. NOOA replaces all four with one abstraction.

An agent is a Python object. Its methods are the actions the model can take, its fields hold state, its docstrings are the prompts, and its type annotations act as contracts.

A method whose body is "..." gets completed at runtime by a validated LLM loop. A method with a normal body stays deterministic Python.

That single convention puts the boundary between probabilistic and deterministic behavior right in the source.

Agent behavior becomes testable, traceable, and refactorable with the same tools you already use on the rest of your codebase.

NVIDIA reports six model-facing ideas combined on one surface, including pass-by-reference over live objects and model-callable harness APIs for context and events, evaluated on SWE-bench Verified, Terminal-Bench 2.0, and ARC-AGI-3.

Paper: https://t.co/PCtFtVY8rT

Learn to build effective AI agents in our academy: https://t.co/1e8RZKs4uX
RT-URL=https://x.com/omarsar0/status/2082602113558077599
TEXT: RT @omarsar0: Super interesting new work from NVIDIA.

(bookmark it)

They suggest building agents as Python objects.

Very cool idea and I…
LINKS: https://arxiv.org/abs/2607.20709 ; https://academy.dair.ai/
--
## @rasbt — 1 шт.

T=2082855363154497880 | @rasbt | 2026-07-30T15:46+00:00 | L416 RT42 C46 V51418 | thread(2)
URL=https://x.com/rasbt/status/2082855363154497880
TEXT: Consistent with what I found with Qwen3.6 a while back: Claude Code uses 2-3x as many tokens than (many) other harnesses at similar success rate.

- Unoptimized?
- Buggy?
- Deliberate (coz that helps it in more challenging cases)?

Need to find some time to investigate more...
[->] Just for reference, from what I observed in my Using Local Coding Agents blog article last month: 
https://t.co/jyt7JS9N7c

"I tried to analyze why Claude Code uses more tokens, and it seems that the difference mainly comes from input tokens rather than output tokens. In other words, Claude is not writing twice as much. The logs suggest that Claude is repeatedly feeding more context back into the model across turns, including previous messages, tool calls, command outputs, and file contents. For example, one Claude run used about 578k input tokens but only about 4.5k output tokens across 25 turns. So the likely explanation is that Claude’s harness accumulates or accounts for a larger prompt-side history during multi-step agent runs.”
QUOTED @composio: We ran Kimi K3 through 3 agent harnesses (Claude Code, Hermes, Kimi Code) on 28 identical tasks.

All 3 harnesses completed the tasks at similar success rates, but the interesting story is token efficiency: the same task cost up to 30x more tokens depending on the harness. 🧵🧵
LINKS: https://x.com/rasbt/status/2070518167399698490?s=20
--
