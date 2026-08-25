# X-FEED 2026-08-25 part 4/8 | items: 9

## @lateinteraction — 10 шт.

T=2091944125431988638 | @lateinteraction | 2026-08-24T17:42+00:00 | L1181 RT128 C41 V108844 | rt
URL=https://x.com/lateinteraction/status/2091944125431988638
RT-OF @a1zhang (L1181): Introducing Speculative Programmatic Tool Calling (sPTC)!

A general class of technique for speculating on tool calls during code generation in a harness and queuing them early to overlap with token generation + REPL execution time.

Blog: https://t.co/0nzkLvTXNy https://t.co/SVH8D2JyEg
RT-URL=https://x.com/a1zhang/status/2091938825580716079
TEXT: RT @a1zhang: Introducing Speculative Programmatic Tool Calling (sPTC)!

A general class of technique for speculating on tool calls during c…
LINKS: https://alexzhang13.github.io/blog/2026/spec-ptc/
--
T=2091958530475516179 | @lateinteraction | 2026-08-24T18:39+00:00 | L16 RT3 C1 V1182 | rt
URL=https://x.com/lateinteraction/status/2091958530475516179
RT-OF @dbreunig (L16): Had a great chat with @Dpbrinkm on the Agentic Conversations about Winchester Mystery Houses, how frontier models are becoming more like applications than infrastructure, why @DSPyOSS matters, and more. 

(Spoiler: I am not the one spending $100k/month!)

https://t.co/4NSSmFdYRa https://t.co/DYJsJFxVat
RT-URL=https://x.com/dbreunig/status/2091957728646504655
TEXT: RT @dbreunig: Had a great chat with @Dpbrinkm on the Agentic Conversations about Winchester Mystery Houses, how frontier models are becomin…
LINKS: https://home.mlops.community/public/videos/the-winchester-mystery-house-problem-in-ai-development
--
T=2091962111811305753 | @lateinteraction | 2026-08-24T18:53+00:00 | L6 RT4 C2 V756 | rt
URL=https://x.com/lateinteraction/status/2091962111811305753
RT-OF @weaviatepodcast (L6): Weaviate Podcast #141 with Mathew Jacob (@mat_jacob1002) and Connor Shorten (@CShorten30)! This episode covers:

• An Overview of Drowning in Documents
• Reranking Deeper Pools
• Phantom Hits from Cross Encoders
• Listwise Rerankers
• Next-Generation Cross Encoders
• Ranking Cascades
• Exciting Directions for AI
• Understanding Coding Agents with SyFI TraceLab

YouTube: https://t.co/bBMWZerAR3
Spotify: https://t.co/Egkn7cALIe
RT-URL=https://x.com/weaviatepodcast/status/2091881285408972803
TEXT: RT @weaviatepodcast: Weaviate Podcast #141 with Mathew Jacob (@mat_jacob1002) and Connor Shorten (@CShorten30)! This episode covers:

• An…
LINKS: https://www.youtube.com/watch?v=fWuavBcoTzk ; https://spotifycreators-web.app.link/e/R85Y5Se9F5b
--
T=2091962089883472383 | @lateinteraction | 2026-08-24T18:53+00:00 | L86 RT7 C1 V5694 | rt
URL=https://x.com/lateinteraction/status/2091962089883472383
RT-OF @LakshyAAAgrawal (L86): Beautiful article, with a model generating beautiful images!

The article reinforces an emerging pattern where seeding RL runs with a strong prompt leads to better outcomes. But it emphasizes another key point: A strong prompt is not necessarily the one containing a lot more information, or details. In this case, GEPA helped delete information like API specs: "The first time three out of three generations produced visible hibiscus blobs was on the version written after throwing the 400-line reference out entirely."

Amazing work!
RT-URL=https://x.com/LakshyAAAgrawal/status/2091937446028316877
TEXT: RT @LakshyAAAgrawal: Beautiful article, with a model generating beautiful images!

The article reinforces an emerging pattern where seeding…
--
T=2091975260845244768 | @lateinteraction | 2026-08-24T19:45+00:00 | L218 RT8 C6 V22879 | post
URL=https://x.com/lateinteraction/status/2091975260845244768
TEXT: afaict alex came up with this idea, built a version of it, and wrote a solo blog on it that y'all are reading, all in 72 hours🤯

and the name speculative here is quite precise: like CPU speculative execution, work is done optimistically and thus (rarely) discarded iff necessary
QUOTED @a1zhang: Introducing Speculative Programmatic Tool Calling (sPTC)!

A general class of technique for speculating on tool calls during code generation in a harness and queuing them early to overlap with token generation + REPL execution time.

Blog: https://t.co/0nzkLvTXNy https://t.co/SVH8D2JyEg
--
T=2092005024104689887 | @lateinteraction | 2026-08-24T21:43+00:00 | L20 RT1 C1 V3931 | rt
URL=https://x.com/lateinteraction/status/2092005024104689887
RT-OF @LaudeInstitute (L20): A Laude / MIT collaboration we've been cooking. 👀
RT-URL=https://x.com/LaudeInstitute/status/2091991366100189225
TEXT: RT @LaudeInstitute: A Laude / MIT collaboration we've been cooking. 👀
--
T=2092004907620479005 | @lateinteraction | 2026-08-24T21:43+00:00 | L788 RT85 C59 V110199 | rt
URL=https://x.com/lateinteraction/status/2092004907620479005
RT-OF @andykonwinski (L788): Introducing Headlong, an open source microharness for persistent agents: self-guided agents that think continuously.

Most agent harnesses are reactive: you send a task, the agent completes it, and then it sits frozen until the next request. Cron jobs and heartbeats wake it up to run a checklist and put it back to sleep.

A Headlong agent is never asleep. It keeps generating thoughts about whatever it decides is interesting, in a self-guided loop inspired by human inner monologue. Your message doesn't start a session. It's one more observation that lands in the agent's thought stream, and the agent decides if and when to reply.

Headlong is built on the idea of persistent agency: continuous inner thought generation between external interactions. The agent sets its own interests and priorities, comes up with its own projects, and sometimes pings you unprompted with progress.

To keep our prototype as simple and small as possible, we implemented Headlong as a microharness: a complete agent harness in under 10K lines of Bash, organized as a handful of small executables. It includes a loop that generates the next thought, shellm (a recursive language model written in Bash), a trajectory stored as a DAG of jsonl files, and context as a projection of that trajectory.

We've been running one Headlong agent internally at Laude for several weeks. The whole team talks to it over Slack and Telegram, and every conversation lands in its single stream of thought. It works in its own fork of Headlong and we've pulled over 50 of its commits into main.

One night, with nobody talking to it, it went back to check whether a recall process it had built was actually wired into its mind, found that it wasn't, diagnosed and fixed the bug, and verified the fix end to end. 48 minutes, no human asked for the fix or was in the loop at any point. Every step is a timestamped line in its log.

Things broke too, and we wrote those up. Background thinking costs us $1 to $2 an hour, our agent stopp
RT-URL=https://x.com/andykonwinski/status/2091990178638496195
TEXT: RT @andykonwinski: Introducing Headlong, an open source microharness for persistent agents: self-guided agents that think continuously.

Mo…
LINKS: https://headlong.ai/install.sh ; https://www.laude.org/updates/headlong-a-microharness-for-persistent-agents ; https://github.com/laude-institute/headlong
--
T=2092005098998079594 | @lateinteraction | 2026-08-24T21:44+00:00 | L176 RT10 C1 V36094 | rt
URL=https://x.com/lateinteraction/status/2092005098998079594
RT-OF @AlexGDimakis (L176): Here come *persistent* agents — very cool work
RT-URL=https://x.com/AlexGDimakis/status/2092001664383566152
TEXT: RT @AlexGDimakis: Here come *persistent* agents — very cool work
--
T=2092006547836510719 | @lateinteraction | 2026-08-24T21:50+00:00 | L65 RT7 C1 V8222 | thread(2)
URL=https://x.com/lateinteraction/status/2092006547836510719
TEXT: In AI, subtle differences in interfaces &amp; affordances have disproportionate impact.

"A message from a human [is] one more observation that lands in the agent’s thought stream. [It] experiences everything that happens to it in one timeline [and] decides who to reply to and when."
[->] lots of really cool ideas brewing in Headlong, including persistent agency via exponential backoff and context management via a *hierarchical* hybrid between recursion and compaction, specifically where the entire trajectory stays in context at exponentially decaying resolution
QUOTED @andykonwinski: Introducing Headlong, an open source microharness for persistent agents: self-guided agents that think continuously.

Most agent harnesses are reactive: you send a task, the agent completes it, and then it sits frozen until the next request. Cron jobs and heartbeats wake it up to run a checklist and put it back to sleep.

A Headlong agent is never asleep. It keeps generating thoughts about whatever it decides is interesting, in a self-guided loop inspired by human inner monologue. Your message d
--
