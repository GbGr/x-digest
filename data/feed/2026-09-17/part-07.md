# X-FEED 2026-09-17 part 7/8 | items: 9

## @sh_reya — 4 шт.

T=2100258064557351066 | @sh_reya | 2026-09-16T16:18+00:00 | L48 RT3 C5 V5928 | thread(2)
URL=https://x.com/sh_reya/status/2100258064557351066
TEXT: Good take. A couple things to add. One, you can build a specialized inference engine while reusing components of vLLM or SGLang (e.g., the model loader and forward pass). Two, historically, applications have required fine-grained control over the buffer pool, and the KV cache is the inference analog. I suspect many applications and domains will need specialized KV cache management (e.g., data processing).
[->] Another thought: if you build a declarative DSL with inference in an operator, the “batch of independent string prompts” abstraction à la OpenAI API may not be the right intermediate layer to represent the domain specific program. The original sglang programming model seemed interesting here but not sure who is using it; if it’s actively supported
QUOTED @JiaZhihao: I think this comes down to a classic systems tradeoff: generality vs. specialization. vLLM/SGLang cover a huge space of models × hardware × workloads. It’s hard for a single system to be best at every combination, and focusing on a narrower set gives you more room to optimize.

Historically, the challenge was engineering cost: optimizations for one configuration often need substantial rework for another. Coding agents are lowering that cost, which I suspect is one reason we’re seeing more specia
--
T=2100286433114067022 | @sh_reya | 2026-09-16T18:11+00:00 | L86 RT9 C11 V16808 | rt
URL=https://x.com/sh_reya/status/2100286433114067022
RT-OF @debnilsur (L86): I used the Breakout List in my new grad recruiting (almost a decade ago!), so this feels very cool. DMs are open - we’ll share more soon and are hiring!
RT-URL=https://x.com/debnilsur/status/2100268767037342131
TEXT: RT @debnilsur: I used the Breakout List in my new grad recruiting (almost a decade ago!), so this feels very cool. DMs are open - we’ll sha…
--
T=2100359277294592192 | @sh_reya | 2026-09-16T23:00+00:00 | L615 RT118 C16 V191523 | rt
URL=https://x.com/sh_reya/status/2100359277294592192
RT-OF @TmlrOrg (L615): TMLR has faced a deluge of submissions, necessitating stricter desk rejection policies due to limited reviewer capacity

Co-EiC Nihar Shah reached out to authors of 10 papers slated for desk reject. Could they answer questions about their *own* submission?
https://t.co/vhX5w6gcx2
RT-URL=https://x.com/TmlrOrg/status/2100322125491966241
TEXT: RT @TmlrOrg: TMLR has faced a deluge of submissions, necessitating stricter desk rejection policies due to limited reviewer capacity

Co-Ei…
LINKS: https://medium.com/@TmlrOrg/asking-authors-about-their-own-papers-3d2e04e5dee0
--
T=2100366219807260776 | @sh_reya | 2026-09-16T23:28+00:00 | L3 RT1 C0 V1228 | rt
URL=https://x.com/sh_reya/status/2100366219807260776
RT-OF @1a1a11a (L3): Unpopular opinion—we should not publish system design papers any more (given that most papers have "untold story", instead, we should focus on (1) the problem (2) why the solution from AI does not work. How many disagree?
RT-URL=https://x.com/1a1a11a/status/2100360299236704392
TEXT: RT @1a1a11a: Unpopular opinion—we should not publish system design papers any more (given that most papers have "untold story", instead, we…
--
## @simonw — 1 шт.

T=2100311378171154492 | @simonw | 2026-09-16T19:50+00:00 | L73 RT5 C71 V18273 | post
URL=https://x.com/simonw/status/2100311378171154492
TEXT: Echoes of OpenAI renaming the Codex desktop app to "ChatGPT" here - everyone's racing to establish themselves as a general agent now
QUOTED @mikeyk: Claude Cowork and Chat are now one Claude, starting today.

The most common thing we hear: people aren't sure which product to start with. That friction gets in the way of getting the best from what these models can do.

I've been on the unified version for a few weeks and really enjoy it. Claude does the deciding about how to get there, while I get to keep my thinking on the work itself.

Let us know what you think! We'll be getting it dialed in over the coming weeks.
--
## @swyx — 4 шт.

T=2100354778392080429 | @swyx | 2026-09-16T22:42+00:00 | L90 RT9 C10 V6116 | rt
URL=https://x.com/swyx/status/2100354778392080429
RT-OF @thaiscbranco_ (L90): How do we end AI slop? To fix it, you gotta measure it first.

Thanks for having me @swyx @aiDotEngineer!
 
 https://t.co/5o66MpJX1i https://t.co/WG7wli5zzM
RT-URL=https://x.com/thaiscbranco_/status/2100353478216601636
TEXT: RT @thaiscbranco_: How do we end AI slop? To fix it, you gotta measure it first.

Thanks for having me @swyx @aiDotEngineer!
 
 https://t.c…
LINKS: https://www.youtube.com/watch?v=sDMGWK4wZ_w
--
T=2100354864274653190 | @swyx | 2026-09-16T22:43+00:00 | L4 RT0 C4 V848 | post
URL=https://x.com/swyx/status/2100354864274653190
TEXT: @thaiscbranco_ @aiDotEngineer pod offer stands!!! you were great and congrats on also getting married :)
--
T=2100400419113746726 | @swyx | 2026-09-17T01:44+00:00 | L4 RT0 C1 V310 | post
URL=https://x.com/swyx/status/2100400419113746726
TEXT: @ivanburazin and podcasts
--
T=2100426129530310845 | @swyx | 2026-09-17T03:26+00:00 | L77 RT4 C1 V9453 | rt
URL=https://x.com/swyx/status/2100426129530310845
RT-OF @pbakaus (L77): If you're interested in the origin story of Impeccable and the philosophy of it, here's my talk on the subject from @aiDotEngineer world fair a couple months back (finally online!): https://t.co/L0q4COkNLH
RT-URL=https://x.com/pbakaus/status/2098218157202944269
TEXT: RT @pbakaus: If you're interested in the origin story of Impeccable and the philosophy of it, here's my talk on the subject from @aiDotEngi…
LINKS: https://www.youtube.com/watch?v=v42opQpCy60&list=PLcfpQ4tk2k0VSUinKVkozYixYWE5eMdDv&index=4
--
