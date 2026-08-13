# X-FEED 2026-08-13 part 1/12 | items: 10

## @_philschmid — 4 шт.

T=2087437231396884895 | @_philschmid | 2026-08-12T07:13+00:00 | L206 RT3 C26 V14635 | post
URL=https://x.com/_philschmid/status/2087437231396884895
TEXT: Excited to be back!
--
T=2087451557772107997 | @_philschmid | 2026-08-12T08:10+00:00 | L1 RT0 C5 V68 | thread(3)
URL=https://x.com/_philschmid/status/2087451557772107997
TEXT: @EverwhereApp let me check
[->] @EverwhereApp Can you share a prompt with me that reproduces that error on your side?
[->] @EverwhereApp Thank you for the samples! and don't worry. Would love to improve your experience.
--
T=2087589594590036009 | @_philschmid | 2026-08-12T17:18+00:00 | L51 RT3 C5 V4793 | post
URL=https://x.com/_philschmid/status/2087589594590036009
TEXT: We shipped a small Gemini API Update! You can now combine  Google Maps and Google Search tool at the same time with Gemini to build cool location apps. 

https://t.co/NTV2kKVc2t
QUOTED @_philschmid: https://t.co/UpN8YgfMbI
LINKS: https://x.com/_philschmid/status/2087589486800654821?s=20
--
T=2087589486800654821 | @_philschmid | 2026-08-12T17:18+00:00 | L38 RT3 C0 V7523 | post
URL=https://x.com/_philschmid/status/2087589486800654821
TEXT: https://t.co/UpN8YgfMbI
LINKS: http://x.com/i/article/2087588209605726208
--
## @addyosmani — 5 шт.

T=2087427868343373919 | @addyosmani | 2026-08-12T06:36+00:00 | L827 RT96 C30 V352234 | thread(9)
URL=https://x.com/addyosmani/status/2087427868343373919
TEXT: https://t.co/Gkd5qvcrAk
[->] @HKrackDev @coderabbitai @dexhorthy Yes! Big fan of Dex's writing and there's a snippet from software factories mentioned lower down.
[->] @Whaler526151 Yes! and @GeoffreyHuntley has been making some great points about the importance of back pressure and constraints too. Hope it gets discussed more.
[->] @huxlab Yes and worth asking what evidence a change carries with it when it reaches you, not just whether it got there.
[->] Big Dex fan (loved that talk) and I think we're describing two halves of the same system. I similarly don't think we're ready for dark software factories yet. I'm in the ~be intentional with what requires code review vs. not camp atm.

Otherwise I think Dex's phases are constraints often applied before the code exists. Mine mostly land after it does: tests, mutation testing, complexity budgets, security gates, CI back-pressure. Upstream constraints reduce the number of bad proposals while the downstream ones catch what still gets through.
[->] @mutewinter Ah, thank you!
[->] @angus1192 UI is a harder problem. You can use deterministic checks (lint rules against a design system, accesibility/perf in CI, make sure the agent has "eyes" (screenshots/browser access) etc. But taste for UI experiments is a harder thing to codify and still needs a human in loop imo.
[->] @axeng200 Thanks for the comment! Where Bob and I differ is whether the residual goes to zero. Constraints can help carry correctness but I do still read code - I'm just more deliberate about what classes of changes need it and this is definitely nuanced on non-toy projects :)
[->] @alphabatcher Thank you!
LINKS: http://x.com/i/article/2087205551038230528
--
T=2087587090662056068 | @addyosmani | 2026-08-12T17:08+00:00 | L3 RT0 C1 V542 | post
URL=https://x.com/addyosmani/status/2087587090662056068
TEXT: @r_alx_z Yes! I anticipate we're going to see this pattern of setting up those deterministic constraints and rules early to become more common.
--
T=2087595500715590022 | @addyosmani | 2026-08-12T17:42+00:00 | L3 RT0 C0 V457 | post
URL=https://x.com/addyosmani/status/2087595500715590022
TEXT: @coderabbitai Congrats on the round folks!
--
T=2087632588945170498 | @addyosmani | 2026-08-12T20:09+00:00 | L7 RT0 C1 V677 | post
URL=https://x.com/addyosmani/status/2087632588945170498
TEXT: @threepointone Yes! I wonder if multiplayer collaborative agent environments will solve this but they're nascent. Directionally interested in Claude Tag etc.
--
T=2087652928035123694 | @addyosmani | 2026-08-12T21:30+00:00 | L7 RT0 C1 V860 | post
URL=https://x.com/addyosmani/status/2087652928035123694
TEXT: Thanks for reading! Constructive disagreement is always appreciated.

Yeah the thing that helps me with 1 and 3 is making the agent's reasoning an artifact I store alongside its code. Before implementation I ask for two lists: what already exists that it considered and rejected and what assumptions it had to make to proceed. Both take a minute to read.

The third one compounds itself in ways. An invented invariant sitting in the context window becomes self-reinforcing, so the agent that wrote it makes a kind of poor reviewer of it. Running the review in a fresh session with no history or against a different model/harness, recovers some ground. Less a second judge than a second context.

Complexity calibration I have no good answer for yet :) Blunt budgets help a little but its also why I keep a human residual instead of driving it to zero.
--
## @bcherny — 1 шт.

T=2087752313700319456 | @bcherny | 2026-08-13T04:05+00:00 | L273 RT16 C27 V22692 | rt
URL=https://x.com/bcherny/status/2087752313700319456
RT-OF @adocomplete (L273): Your sessions have names and can DM each other in Claude Code.

claude --name backend
claude --name frontend

&gt; tell frontend the orders endpoint moved to /v2

it's very effective. https://t.co/5nGgSOsjCN
RT-URL=https://x.com/adocomplete/status/2087728817012162973
TEXT: RT @adocomplete: Your sessions have names and can DM each other in Claude Code.

claude --name backend
claude --name frontend

&gt; tell front…
--
