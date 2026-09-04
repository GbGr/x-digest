# X-FEED 2026-09-04 part 9/11 | items: 9

## @omarsar0 — 13 шт.

T=2095507069788889536 | @omarsar0 | 2026-09-03T13:39+00:00 | L28 RT2 C12 V8080 | post
URL=https://x.com/omarsar0/status/2095507069788889536
TEXT: Hugging Face is in great hands. 

Big win for open source. And do not underestimate NVIDIA in its open-source efforts. 

They have been shipping great open models, and I think this amplifies their efforts.
QUOTED @JensenHuang: Exciting day for NVIDIA and @huggingface.

Open models strengthen safety and cybersecurity, accelerate innovation and diffusion, and enable sovereignty. They allow every developer, startup, university, industry and country to build with, customize and benefit from AI.

Thank you @ClementDelangue for coming to me.

NVIDIA is going to be a great home for Hugging Face, its community and the future of open models. 🤗

https://t.co/q8Om2Xc5ye
--
T=2095518433865777600 | @omarsar0 | 2026-09-03T14:25+00:00 | L226 RT41 C15 V25782 | post
URL=https://x.com/omarsar0/status/2095518433865777600
TEXT: Massive paper from Meta.

I like this one because it shows the use of agent harnesses for production-grade recommender systems.

Details below:

This is one of the more convincing agent deployments I've seen.

It runs against a live production recommender serving billions of people and reports A/B results.

Sustaining a recommender is continual optimization work. Content shifts, user behavior shifts, upstream models shift, and the choices governing retrieval, ranking and serving have to be revisited.

Human engineers test those changes through online experiments, which is slow enough that parts of the system go unrevised.

In CORAL, each cycle the agent observes operating signals, reasons over a memory of past decisions and their measured outcomes, and invokes tools including a numerical optimizer that keeps every change inside a fixed operating budget.

The policy improves in context from its own prior actions, with no parameter updates.

Across two large social platforms, the same harness improves engagement at no additional serving cost on one and reduces serving cost without degrading engagement on the other.

Performance improves as the loop iterates.

The guardrail design carries as much weight as the agent. A bounded change budget makes this safe to run against production.

Paper: https://t.co/G46EgVuPMR

Chat with Paper: https://t.co/KlYFT8dAFD
LINKS: https://arxiv.org/abs/2609.02730 ; https://academy.dair.ai/papers/coral-an-llm-native-harness-for-production-recommender-systems-2609.02730
--
T=2095522980566614065 | @omarsar0 | 2026-09-03T14:43+00:00 | L15 RT0 C0 V8791 | post
URL=https://x.com/omarsar0/status/2095522980566614065
TEXT: An agent is only as useful as the environment it can act in.

Zite MCP gives Claude, ChatGPT, and Cursor a place to build and publish a working app with a database, team logins, and roles.

The build runs on your existing Claude or ChatGPT subscription with zero Zite credits.
QUOTED @domwhyte42: Today we’re turning your Claude subscription into a full AI app builder.

Connect Claude, ChatGPT or Cursor to Zite MCP and ask for an app. It goes live with its own database, logins for your whole team, roles for who sees what.

Zero Zite credits. https://t.co/ubbGdbOX2h
--
T=2095525271625441607 | @omarsar0 | 2026-09-03T14:52+00:00 | L195 RT5 C30 V28540 | thread(2)
URL=https://x.com/omarsar0/status/2095525271625441607
TEXT: both codex and claude down? what the heck?!!

open models it is, then
[->] glm-5.3 and deepseek-v4 holding down the fort
--
T=2095536220239478855 | @omarsar0 | 2026-09-03T15:35+00:00 | L28 RT0 C1 V8422 | post
URL=https://x.com/omarsar0/status/2095536220239478855
TEXT: Pay attention to persistent agents and memory.

@coworkerapp just launched a great solution for persistent memory for your company.

Extremely efficient, cheap, and fast.

https://t.co/cl8yr3QFIr
QUOTED @coworkerapp: Today we're launching OM2.

Your AI re-reads your entire company from scratch every time you ask it something.

It’s why more than 50% of your token bill isn't in the answer, but in the search for it.

OM2 gives your AI a permanent memory of your company. 🧠 https://t.co/wzRD6f8PXi
LINKS: https://x.com/coworkerapp/status/2095527138791219620?s=20
--
T=2095541284010160174 | @omarsar0 | 2026-09-03T15:55+00:00 | L78 RT15 C5 V8369 | rt
URL=https://x.com/omarsar0/status/2095541284010160174
RT-OF @dair_ai (L78): Banger paper from BAAI.

If you are building research agents, this one is worth your time.

(bookmark it)

They find that adding skills scores 134.3% higher on MLE-bench, 34.4% higher on PaperBench, 9.2% higher on FrontierCS and 14.0% higher on PassNet.

More details on the approach:

The agent has a strong backbone and a harness for planning, execution, memory and verification, and it still does not know how to make a given method actually work.

That know-how lives in repositories and papers, written for human readers and far too large to load during a task.

DisCo distills it. Task-agnostic distillation condenses 1,000 widely used ML repositories into the AREX-Skill Library, over 5,000 verified skills organized into 20 areas and 178 capability families. Task-oriented distillation writes the skills a concrete task calls for.

Paper: https://t.co/Raljjde8Gc

Chat with Paper: https://t.co/5NcvwGRMqJ
RT-URL=https://x.com/dair_ai/status/2095539831141220620
TEXT: RT @dair_ai: Banger paper from BAAI.

If you are building research agents, this one is worth your time.

(bookmark it)

They find that addi…
LINKS: https://arxiv.org/abs/2609.02749 ; https://academy.dair.ai/papers/repo-to-skill-distilling-github-repositories-into-ai4ai-skills-2609.02749
--
T=2095559818337538556 | @omarsar0 | 2026-09-03T17:09+00:00 | L288 RT13 C594 V46866 | thread(5)
URL=https://x.com/omarsar0/status/2095559818337538556
TEXT: The @bot team gave me 50 codes to hand out to my followers, each worth $200.

That's a month free of the $200/month plan, or $200 in credits.

Just comment with your best/most fun use cases or things you’d like to try in Grok Bot.

Grok Bot changed how I work with agents. I stopped overthinking. I hand a task to a bot, and it manages most of the work from there.

My favorite bot so far:

My orchestrator bot runs my higher-level agent team. It assigns work across specialized bots and keeps everything organized, so I run many tasks in parallel instead of babysitting one at a time.
[->] @lemon07r @bot can't dm you for some reason. dm first so i can share code thanks
[->] @bot Keep them coming. I will update the thread when I am out of codes.
[->] @bot Me sending codes. Keep them coming. A few more left. https://t.co/Q0jrI2XhwA
[->] @bot You all are cooking. I tried my best to keep up with replies. 

All 50 codes have been shared already.
--
T=2095576401709531416 | @omarsar0 | 2026-09-03T18:15+00:00 | L40 RT5 C8 V8849 | post
URL=https://x.com/omarsar0/status/2095576401709531416
TEXT: Impressive tool to explore frontier AI capabilities.

Martian's AI Frontier lets you compare 44 LLMs by measured cost, quality, and reliability, then see how routing and repeated sampling change the frontier.

I like this because builders can choose model combinations using real tradeoffs across coding, reasoning, factuality, and agentic tasks.
QUOTED @withmartian: We got 46% fewer errors than the single best LLM across the 16 most used benchmarks (TerminalBench, LiveCodeBench, etc).

Here's how that's possible and what each model can achieve when used optimally (every benchmarks misses the majority of model capabilities) 👇

Interactive Site: https://t.co/6ZqljIhKBh
Academic Paper: https://t.co/AX7QEMtEF5
--
T=2095591106482180167 | @omarsar0 | 2026-09-03T19:13+00:00 | L83 RT0 C64 V10006 | post
URL=https://x.com/omarsar0/status/2095591106482180167
TEXT: You all are building some cool stuff. 

Should I try to get some more codes from the Grok @bot team?
QUOTED @omarsar0: The @bot team gave me 50 codes to hand out to my followers, each worth $200.

That's a month free of the $200/month plan, or $200 in credits.

Just comment with your best/most fun use cases or things you’d like to try in Grok Bot.

Grok Bot changed how I work with agents. I stopped overthinking. I hand a task to a bot, and it manages most of the work from there.

My favorite bot so far:

My orchestrator bot runs my higher-level agent team. It assigns work across specialized bots and keeps everyt
--
