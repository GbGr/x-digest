# X-FEED 2026-08-15 part 2/7 | items: 11

## @HamelHusain — 9 шт.

T=2088316719601447163 | @HamelHusain | 2026-08-14T17:27+00:00 | L118 RT12 C9 V8250 | thread(2)
URL=https://x.com/HamelHusain/status/2088316719601447163
TEXT: If you do any kind of classification with LLMs, you'll want to pay attention to this talk from @sh_reya  . A model cascade is a clever way to reduce costs while maintaining performance of a bigger model.   

It works by having a larger model label ~500 records and test observed confidence values to find a routing threshold that meets your target agreement. Shreya reports 𝘁𝗵𝗶𝘀 𝗮𝗰𝗵𝗶𝗲𝘃𝗲𝘀 𝗰𝗼𝘀𝘁 𝘀𝗮𝘃𝗶𝗻𝗴𝘀 𝗼𝗳 𝟵𝟬% 𝗼𝗿 𝗺𝗼𝗿𝗲 𝗮𝗰𝗿𝗼𝘀𝘀 𝗮 𝗿𝗮𝗻𝗴𝗲 𝗼𝗳 𝗰𝗹𝗮𝘀𝘀𝗶𝗳𝗶𝗰𝗮𝘁𝗶𝗼𝗻 𝘁𝗮𝘀𝗸𝘀.

Shreya walks through exactly how it works in this talk.  (BTW no slides, just drawing 🥰!) Here's what's covered:

00:00:43 What a classification problem actually is
00:01:57 The Oracle plan: run the big model on everything
00:05:11 The model cascade architecture
00:08:04 The algorithm: finding the confidence threshold
00:10:51 Simulating thresholds for accuracy and cost
00:14:48 Why a lower threshold means lower cost
00:17:52 Running the cascade 
00:20:39 How well it works: cutting 90%+ of cost
00:20:54 Cascades vs black-box model routers
00:22:48 Can you trust a nano model's confidence score?

Notes and video here: https://t.co/zsaYEMBKdh
[->] Also this was her earlier talk in the series:

https://t.co/6G6ukT4WMR
LINKS: https://hamel.dev/notes/llm/ai-product-engineering/evals-model-cascades.html ; https://x.com/HamelHusain/status/2087994596899028998?s=20
--
T=2088345126813020191 | @HamelHusain | 2026-08-14T19:20+00:00 | L24 RT0 C2 V1725 | post
URL=https://x.com/HamelHusain/status/2088345126813020191
TEXT: Browser use going wild https://t.co/TlKKjT3dYH
--
T=2088390647107780892 | @HamelHusain | 2026-08-14T22:21+00:00 | L26 RT1 C4 V2200 | post
URL=https://x.com/HamelHusain/status/2088390647107780892
TEXT: There is no blog post that will win over developers re: watermarking AI
--
T=2088392435047272651 | @HamelHusain | 2026-08-14T22:28+00:00 | L31 RT5 C7 V2365 | thread(2)
URL=https://x.com/HamelHusain/status/2088392435047272651
TEXT: “overcast” describes cloud cover precisely, while “grey” might describe the light, sky, mood,etc.

Yes, I care, and it matters. https://t.co/X67yH1MWwm
[->] Also notice how emphasis is on readers not authors.
--
T=2088397703814516865 | @HamelHusain | 2026-08-14T22:49+00:00 | L10 RT1 C3 V1594 | post
URL=https://x.com/HamelHusain/status/2088397703814516865
TEXT: The model "just needs encouragement" is a UX issue.  It's not something to be proud of
--
T=2088408416805171382 | @HamelHusain | 2026-08-14T23:32+00:00 | L9 RT1 C2 V720 | rt
URL=https://x.com/HamelHusain/status/2088408416805171382
RT-OF @isaac_flath (L9): @HamelHusain I can't believe that Anthropic's take is that word choice doesn't matter in writing....
RT-URL=https://x.com/isaac_flath/status/2088398636686213390
TEXT: RT @isaac_flath: @HamelHusain I can't believe that Anthropic's take is that word choice doesn't matter in writing....
--
T=2088417091254981013 | @HamelHusain | 2026-08-15T00:06+00:00 | L22 RT1 C5 V2404 | post
URL=https://x.com/HamelHusain/status/2088417091254981013
TEXT: Grok Bot is cool because it is "self-driving" (like Codex desktop).  It can create new threads/tasks and communicate b/w them

It's also a simple interface and decent computer use + nice iOS app.   

I found computer use lagging behind Codex slightly but its worth trying it, especially if you have a Cursor Ultra sub

 https://t.co/zKGOk8KKwl
LINKS: https://x.ai/bot
--
T=2088433001252470932 | @HamelHusain | 2026-08-15T01:10+00:00 | L2 RT1 C1 V610 | rt
URL=https://x.com/HamelHusain/status/2088433001252470932
RT-OF @isaac_flath (L2): Amp orbs are actually pretty useful.  Here's an example.

I started a thread in the cli working on my blog.  Had it use a portal to host the site to show me the changes.  

I'm working on a technical post and wanted it to render jupyter notebooks nicer so it did that and I saw it work in the site portal.

I moved to to the web UI because it was just kinda nice to have my website preview and coding agent both in chrome in the same app.

I went back to work on my post, so I told it to make another portal for jupyter.   This was nice because I don't have jupyter on this machine and I don't really like telling agents to just go install stuff on my local computer, but in an orb sandbox it's fine.

It's on same machine so save of notebook reloads the preview site.

And it all just worked.  I could have done all this on localhost like I usually do.  

But it was nice because it was just a bit less friction than normal
RT-URL=https://x.com/isaac_flath/status/2088432258495508777
TEXT: RT @isaac_flath: Amp orbs are actually pretty useful.  Here's an example.

I started a thread in the cli working on my blog.  Had it use a…
--
T=2088438265271693468 | @HamelHusain | 2026-08-15T01:30+00:00 | L46 RT0 C2 V2451 | post
URL=https://x.com/HamelHusain/status/2088438265271693468
TEXT: https://t.co/n5mIgwug4F
QUOTED @XFreeze: Grok 4.6 just ranked #1 on CursorBench 3.2

Outperforming Claude Fable 5, Opus 5 and GPT-5.6 Sol on real-world coding performance

And what makes this even crazier is the efficiency....the chart gives CursorBench performance against average cost per task, and Grok 4.6 is sitting right at the top of the frontier

Grok 4.6 is insanely capable at coding....delivering frontier coding performance at ridiculous efficiency
--
## @jxnlco — 2 шт.

T=2088093792758866416 | @jxnlco | 2026-08-14T02:42+00:00 | L54 RT0 C5 V7031 | post
URL=https://x.com/jxnlco/status/2088093792758866416
TEXT: Externally I want to be the Rick Rubin 
Internally I want to be erdos.
--
T=2088324320921596294 | @jxnlco | 2026-08-14T17:58+00:00 | L688 RT21 C94 V64014 | rt
URL=https://x.com/jxnlco/status/2088324320921596294
RT-OF @SIGKITTEN (L688): Get your “finally” replies in.

Codex Remote notifications are now working. When you start a turn or open up a thread in progress, you’ll get a notification when the turn finishes or needs approval, etc https://t.co/10gt6rlPhN
RT-URL=https://x.com/SIGKITTEN/status/2088267586655997966
TEXT: RT @SIGKITTEN: Get your “finally” replies in.

Codex Remote notifications are now working. When you start a turn or open up a thread in pro…
--
