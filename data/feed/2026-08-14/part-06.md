# X-FEED 2026-08-14 part 6/10 | items: 8

## @omarsar0 — 6 шт.

T=2087924171976126746 | @omarsar0 | 2026-08-13T15:28+00:00 | L216 RT72 C73 V43479 | rt
URL=https://x.com/omarsar0/status/2087924171976126746
RT-OF @coderabbitai (L216): Attackers use AI to find vulnerabilities faster. Your defenses should too.

Introducing CodeRabbit Security.

Map out your repository, hunt vulnerabilities in production code, verify each against real code, and ship fixes as PRs.

No speculation. No noise. https://t.co/UkmlkmXx8g
RT-URL=https://x.com/coderabbitai/status/2087888534753488909
TEXT: RT @coderabbitai: Attackers use AI to find vulnerabilities faster. Your defenses should too.

Introducing CodeRabbit Security.

Map out you…
--
T=2087925529076711481 | @omarsar0 | 2026-08-13T15:33+00:00 | L32 RT1 C6 V7949 | post
URL=https://x.com/omarsar0/status/2087925529076711481
TEXT: Recommended to check out. 

It's a good start to see that DeepSeek Harness focuses on making everything a plugin. It's about like how Pi is built and why it's so darn useful and effective.
QUOTED @deepseek_ai: 🧩 DeepSeek Harness v0.1 is now available in Developer Preview!

🔹 We’re opening it up to developers building agent harnesses worldwide and open-sourcing the codebase in MIT license.
🔹 Powered by the Cordis meta-framework, DeepSeek Harness is an agent harness built around one core idea: Everything is a plugin. Models, tools, skills, sessions, sandboxes, filesystems, loops, orchestration, and UI are ALL implemented as plugins, and can be mixed, matched, replaced, and extended.

Try it now!
https:/
--
T=2087926158432309306 | @omarsar0 | 2026-08-13T15:36+00:00 | L147 RT22 C10 V9944 | post
URL=https://x.com/omarsar0/status/2087926158432309306
TEXT: Very interesting new paper from Microsoft and colleagues.

(bookmark it)

Skill libraries are used in every major harness on the assumption that more guidance is free. This work measures what a bad skill actually costs you.

They attribute 307 agent failures to specific loaded skills, 125 functional failures and 182 efficiency regressions, by comparing each skill-guided run against a matched reference run that solves the same task.

The failures rarely come from irrelevant skills. Seemingly relevant skills push the agent to incorrectly implement or omit something the task required.

Cost regressions are not explained by prompt length either. The largest source is excessive verification at 67 cases, followed by heavy implementation pipelines at 30 cases. It turns out that skills quietly turn validation checklists into mandatory work.

Paper: https://t.co/hQGxuiE7of

Track more trending AI papers in our academy: https://t.co/1e8RZKs4uX
LINKS: https://arxiv.org/abs/2608.11888 ; https://academy.dair.ai/
--
T=2087949444272558282 | @omarsar0 | 2026-08-13T17:08+00:00 | L36 RT4 C4 V8098 | post
URL=https://x.com/omarsar0/status/2087949444272558282
TEXT: Gemini 3.7 Flash is here!

Improved capabilities for long-horizon software engineering tasks, but also great at PDF understanding. https://t.co/lpN3TJq9E9
QUOTED @GoogleDeepMind: Gemini 3.7 Flash is here.

It’s stronger for coding, knowledge work, and web development. 🧵
--
T=2087962456572498142 | @omarsar0 | 2026-08-13T18:00+00:00 | L105 RT11 C13 V8497 | post
URL=https://x.com/omarsar0/status/2087962456572498142
TEXT: If you write rules in an AGENTS.md, this one is worth your time.

When a coding agent follows your rule, it may have been going to do that anyway.

Harness-IF separates the two by scoring 256 rules one at a time from execution evidence, then re-running every task with the rule withheld across nine probe builds to find which rules actually oppose the model's defaults.

Across 12 frontier models, raw accuracy runs 72.1 to 85.9%, and Against-Prior Accuracy runs 66.1 to 78.6%. Every model gets worse once coincidence is stripped out, by 3.6 to 7.4 points.

One finding worth flagging. Precedence does not follow prompt depth. System prompts, project files, and user instructions all outrank tool and skill descriptions.

Paper: https://t.co/97ltVTYHF8

Track more trending AI papers in our academy: https://t.co/1e8RZKs4uX
LINKS: https://arxiv.org/abs/2608.11727 ; https://academy.dair.ai/
--
T=2087993754628042766 | @omarsar0 | 2026-08-13T20:04+00:00 | L69 RT12 C6 V7014 | rt
URL=https://x.com/omarsar0/status/2087993754628042766
RT-OF @dair_ai (L69): A great read if you an AI dev.

Current context compactors retain 17% of the standing rules users give them.

Session Constraints are instructions like "do not delete any emails until I confirm" that bind the agent for the rest of the session. It turns out that compaction drops them silently.

Their evaluation suite, COMPINT, tests three settings, multi-turn chat, agentic trajectory, and long-horizon research. Compactors often leave the task worse off than running it without compaction at all.

Retention swings with the compactor, the prompt, the context length, the phrasing, and where the constraint was injected, so the loss is structural.

The fix is small. An SC-aware extractor running alongside the compactor recovers over 90% retention without touching the compactor or the model.

Paper: https://t.co/SQr9Uz7ek5

Track more trending AI papers in our academy: https://t.co/LRnpZN7L4c
RT-URL=https://x.com/dair_ai/status/2087930434323959894
TEXT: RT @dair_ai: A great read if you an AI dev.

Current context compactors retain 17% of the standing rules users give them.

Session Constrai…
LINKS: https://arxiv.org/abs/2608.11242 ; https://academy.dair.ai/
--
## @sh_reya — 2 шт.

T=2088001415478468999 | @sh_reya | 2026-08-13T20:35+00:00 | L15 RT5 C0 V3458 | post
URL=https://x.com/sh_reya/status/2088001415478468999
TEXT: It was great to present our data agent benchmark in the summer of evals series! Slides courtesy of co first author @ruiyingm1120, a second year PhD student at UC Berkeley!!
QUOTED @HamelHusain: New session w/@sh_reya where she goes over a useful new eval called the Data Agent Benchmark (DAB).  

Data agents answer business questions like “which cohort had the highest churn?” that a data analyst would normally answer.  

DAB recreates the mess of a real data warehouse. Each task spreads data across at least two database systems, with inconsistent join keys, key values buried in free text, and ambiguous or ill-defined schemas. 

Timestamps from the talk:

00:00:52 What a data agent actua
--
T=2088012334409355631 | @sh_reya | 2026-08-13T21:18+00:00 | L153 RT19 C4 V6239 | rt
URL=https://x.com/sh_reya/status/2088012334409355631
RT-OF @andy_pavlo (L153): New @CMUDB Seminar Series: Whatever Andy Found Interesting While Out At Sea
An eclectic collection of database technical talks. Mondays @ 4:30pm ET starting Sep 21 over Zoom. Youtube afterwards. https://t.co/SykepIn6dM https://t.co/0WglP3rbDS
RT-URL=https://x.com/andy_pavlo/status/2088002932453024175
TEXT: RT @andy_pavlo: New @CMUDB Seminar Series: Whatever Andy Found Interesting While Out At Sea
An eclectic collection of database technical ta…
LINKS: https://db.cs.cmu.edu/seminars/fall2026/
--
