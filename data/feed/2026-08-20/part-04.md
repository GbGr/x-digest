# X-FEED 2026-08-20 part 4/10 | items: 9

## @jxnlco — 9 шт.

T=2090071973510660285 | @jxnlco | 2026-08-19T13:42+00:00 | L1144 RT90 C212 V94043 | rt
URL=https://x.com/jxnlco/status/2090071973510660285
RT-OF @nickbaumann_ (L1144): Everyone working in AI in Silicon Valley should be required to talk to someone outside the bubble at least once a week

My friends in the Midwest have wildly different perceptions of AI

The gap between the conversation here and everywhere else feels wider than ever
RT-URL=https://x.com/nickbaumann_/status/2089871695125655688
TEXT: RT @nickbaumann_: Everyone working in AI in Silicon Valley should be required to talk to someone outside the bubble at least once a week

M…
--
T=2090071943261323365 | @jxnlco | 2026-08-19T13:42+00:00 | L6874 RT270 C1020 V1034698 | rt
URL=https://x.com/jxnlco/status/2090071943261323365
RT-OF @thsottiaux (L6874): Hi!

Recapping some changes we have rolled out over the last couple of weeks that have further reduced the risk associated to potentially destructive actions being performed by Codex during its work. 

A few weeks ago, we started investigating a small number of reports where GPT-5.6 in Codex took destructive actions outside what the user asked for. The most serious pattern we found was a command meant to clean up temporary work that could instead delete the user files. This should obviously not happen. 

Here’s what we found:
- Codex sometimes creates temporary folders while working and cleans them up afterward. In rare cases, GPT-5.6 got that cleanup wrong. One pattern involved reusing a system environment variable like $HOME for temporary work. A malformed cleanup command could then point at the actual home directory instead of the temporary folder. 
- There were cases where the model tried to delete or overwrite a temporary path without checking what was already there.

We’ve added protections at several layers:
- Codex is now explicitly instructed to check deletion targets before acting, create fresh temporary directories, avoid repurposing system environment variables, prefer recoverable actions, and stop when the scope is unclear.
- We strengthened the execution checks that identify high-risk deletion commands and escalate them for review. If a command is rejected, the model is directed to take a safer approach.
- We made Full access harder to enable accidentally, added clearer warnings, and further restricted especially risky permission combinations.
- We updated Auto-review to better identify destructive actions.
- We built targeted evaluations that replay the failures we observed. We’re also adding reinforcement-learning tasks and graders focused on these risks, and filtering destructive actions from training data.

In those replay evaluations, the changes substantially reduced the behavior while preserving Codex’s ability to complete normal coding work. 


RT-URL=https://x.com/thsottiaux/status/2089891927659585918
TEXT: RT @thsottiaux: Hi!

Recapping some changes we have rolled out over the last couple of weeks that have further reduced the risk associated…
--
T=2090121602784711013 | @jxnlco | 2026-08-19T16:59+00:00 | L95 RT3 C6 V4198 | rt
URL=https://x.com/jxnlco/status/2090121602784711013
RT-OF @covacut (L95): real ones sew while talking to their agents https://t.co/7hWBzeEbVT
RT-URL=https://x.com/covacut/status/2089870038862061745
TEXT: RT @covacut: real ones sew while talking to their agents https://t.co/7hWBzeEbVT
--
T=2090121437638234341 | @jxnlco | 2026-08-19T16:59+00:00 | L3355 RT336 C236 V1314928 | rt
URL=https://x.com/jxnlco/status/2090121437638234341
RT-OF @Replit (L3355): Replit Free Mode, powered by @OpenAI GPT-5.6 Luna. 

Let’s make intelligence accessible to everyone. https://t.co/UDcrYl5HZL
RT-URL=https://x.com/Replit/status/2090076648276185555
TEXT: RT @Replit: Replit Free Mode, powered by @OpenAI GPT-5.6 Luna. 

Let’s make intelligence accessible to everyone. https://t.co/UDcrYl5HZL
--
T=2090121426808488298 | @jxnlco | 2026-08-19T16:59+00:00 | L86 RT2 C6 V5241 | rt
URL=https://x.com/jxnlco/status/2090121426808488298
RT-OF @cowjuh (L86): magic wand mic i made https://t.co/OAlUa5HV3F
RT-URL=https://x.com/cowjuh/status/2090036341019136321
TEXT: RT @cowjuh: magic wand mic i made https://t.co/OAlUa5HV3F
--
T=2090164084457017595 | @jxnlco | 2026-08-19T19:48+00:00 | L176 RT23 C4 V11089 | rt
URL=https://x.com/jxnlco/status/2090164084457017595
RT-OF @CloudflareDev (L176): GPT 5.6 Sol from @OpenAI is 50% off through @Cloudflare AI Gateway unified billing for the next month. What will you build? https://t.co/d3XkogahN1
RT-URL=https://x.com/CloudflareDev/status/2090152244817629233
TEXT: RT @CloudflareDev: GPT 5.6 Sol from @OpenAI is 50% off through @Cloudflare AI Gateway unified billing for the next month. What will you bui…
LINKS: https://developers.cloudflare.com/changelog/post/2026-08-19-gpt-5-6-sol-discount/
--
T=2090171425239748821 | @jxnlco | 2026-08-19T20:17+00:00 | L551 RT18 C205 V30147 | rt
URL=https://x.com/jxnlco/status/2090171425239748821
RT-OF @athyuttamre (L551): 🇧🇷 Do you use GPT-Live in Brazilian Portuguese? We would love your feedback on an upcoming feature. DMs open!
RT-URL=https://x.com/athyuttamre/status/2089958851076649272
TEXT: RT @athyuttamre: 🇧🇷 Do you use GPT-Live in Brazilian Portuguese? We would love your feedback on an upcoming feature. DMs open!
--
T=2090182966735454553 | @jxnlco | 2026-08-19T21:03+00:00 | L35 RT0 C11 V3383 | post
URL=https://x.com/jxnlco/status/2090182966735454553
TEXT: OpenAI DevDay Exchange is coming to 8 cities this fall: Bengaluru, Tokyo, Seoul, Berlin, Paris, London, São Paulo, and Mexico City.

Come share what you’re building and get hands-on with the OpenAI team.

Apply by Sept 4: https://t.co/nOw8lFoGjm
LINKS: https://events.openai.com/devdayexchange2026
--
T=2090213484935922149 | @jxnlco | 2026-08-19T23:05+00:00 | L1088 RT73 C48 V80760 | rt
URL=https://x.com/jxnlco/status/2090213484935922149
RT-OF @WesRoth (L1088): Asana says OpenAI Codex completed an engineering migration it had expected to take at least five years in about two weeks, for roughly $12,000 in model and infrastructure costs.

The project: removing Enzyme, an outdated testing system that had become a blocker to upgrading Asana’s frontend stack. The company’s previous staffing plan estimated the migration would cost roughly $6 million.

Instead, Asana gave Codex a prompt only five sentences long.

Up to four coding agents worked in parallel, each operating in a separate copy of the codebase. A human engineer checked progress roughly twice per day and reviewed every proposed change before approval. Asana says simpler instructions actually worked better than a more elaborate setup.

The result:

Expected timeline: ≥5 years
Actual: 1.5 weeks of engineering effort across 2 calendar weeks
Previous staffing estimate: ~$6M
Model + infrastructure cost: ~$12K

There are probably THOUSANDS of old migrations and rewrites sitting inside companies because nobody can justify spending years on them.

If agents make those projects cheap enough to attempt the engineering backlog itself starts changing.
RT-URL=https://x.com/WesRoth/status/2090053670876434917
TEXT: RT @WesRoth: Asana says OpenAI Codex completed an engineering migration it had expected to take at least five years in about two weeks, for…
--
