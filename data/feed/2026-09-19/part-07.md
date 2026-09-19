# X-FEED 2026-09-19 part 7/7 | items: 13

## @thorstenball — 10 шт.

T=2100858434904109099 | @thorstenball | 2026-09-18T08:04+00:00 | L1616 RT55 C29 V86108 | thread(3)
URL=https://x.com/thorstenball/status/2100858434904109099
TEXT: Jev picking the next command from shell history https://t.co/7xnbK0duD6
[->] Here's the code (didn't once look at it): https://t.co/sWZ0vfnr0u
[->] Also, didn't record the demo, that was all in Amp: https://t.co/7fSTnprZIY
LINKS: https://github.com/mrnugget/jev-shell-history
--
T=2100862791129129455 | @thorstenball | 2026-09-18T08:21+00:00 | L36 RT0 C1 V3858 | post
URL=https://x.com/thorstenball/status/2100862791129129455
TEXT: Two small additions today, added to news post:

• --discover-dirs can be repeated, and can take a path
• --discover-depth determines depth of search https://t.co/iJPz09k9aq
QUOTED @thorstenball: Time to leave one `amp --no-tui` running on your Mac mini and forget about it.

It now serves every repo on the machine, and keeps itself updated.

https://t.co/czmkFVBH9G https://t.co/wRbzo5VYEz
--
T=2100878772299817134 | @thorstenball | 2026-09-18T09:25+00:00 | L71 RT1 C10 V7572 | post
URL=https://x.com/thorstenball/status/2100878772299817134
TEXT: Delicious meta thought from this morning:

The table pounding from the AI-skeptical software engineers, shouting "they can't build proper, scalable, performant programs!", sounds especially thin when you consider that right now nearly everyone is looking for where this is going and no one knows yet.

Building something "proper" and "scalable" and "performant" before you have PMF is a tricky thing to pull off (there's exceptions, of course, where PMF comes from being one of the three) and now it seems like most companies are looking for PMF every 3 months.
--
T=2100937399433838635 | @thorstenball | 2026-09-18T13:18+00:00 | L74 RT0 C12 V4944 | post
URL=https://x.com/thorstenball/status/2100937399433838635
TEXT: Create new dirs and projects on the runner, right from the picker.

Any interest in that? https://t.co/ZnrlBisVTg
--
T=2100961252692349273 | @thorstenball | 2026-09-18T14:52+00:00 | L106 RT0 C8 V12880 | post
URL=https://x.com/thorstenball/status/2100961252692349273
TEXT: Someone built a load-balancer with Jev yet?

If speed requirements aren't that strict, I bet it could beat some heuristics.
--
T=2100997975325507814 | @thorstenball | 2026-09-18T17:18+00:00 | L86 RT1 C7 V10842 | post
URL=https://x.com/thorstenball/status/2100997975325507814
TEXT: Never bet against orbs.

It's happening. https://t.co/PIgUAU6JnS
--
T=2101046461802680527 | @thorstenball | 2026-09-18T20:31+00:00 | L191 RT6 C3 V36817 | rt
URL=https://x.com/thorstenball/status/2101046461802680527
RT-OF @MarcJBrooker (L191): The "mixed mode" where humans look at some code reviews, assisted by review tools, is also valuable today. But probably even more transient.

The idea that humans will reliably look through code to find the increasingly rare issues that automated tools miss seems like a fantasy.
RT-URL=https://x.com/MarcJBrooker/status/2101005957300125710
TEXT: RT @MarcJBrooker: The "mixed mode" where humans look at some code reviews, assisted by review tools, is also valuable today. But probably e…
--
T=2101169411902119975 | @thorstenball | 2026-09-19T04:40+00:00 | L198 RT1 C7 V15733 | rt
URL=https://x.com/thorstenball/status/2101169411902119975
RT-OF @MarcJBrooker (L198): @copyconstruct Long-term I suspect you're going to end up caring about those things about as much as you care about your compiler's register allocation decisions.

Could you do better? Maybe. Is it worth doing better? Only for a tiny fraction of code.
RT-URL=https://x.com/MarcJBrooker/status/2101022224790823167
TEXT: RT @MarcJBrooker: @copyconstruct Long-term I suspect you're going to end up caring about those things about as much as you care about your…
--
T=2101206192315920479 | @thorstenball | 2026-09-19T07:06+00:00 | L9 RT1 C0 V1304 | rt
URL=https://x.com/thorstenball/status/2101206192315920479
RT-OF @purefunctor (L9): wait a minute... https://t.co/ctkVXa32Jg
RT-URL=https://x.com/purefunctor/status/2101170737172373782
TEXT: RT @purefunctor: wait a minute... https://t.co/ctkVXa32Jg
--
T=2101215311953313815 | @thorstenball | 2026-09-19T07:42+00:00 | L9 RT0 C2 V628 | thread(2)
URL=https://x.com/thorstenball/status/2101215311953313815
TEXT: Jev predicting which line to jump to after an edit https://t.co/cSc26ZBtEx
[->] As always: I didn't do anything. Amp built the whole thing, recorded the video, all in an orb.

There's the obvious thing here that, wow, you can build a Copilot using Jev, wow.

But also: it was done by another model, fully autonomously. https://t.co/To7xpZLmXs
--
## @Tim_Dettmers — 1 шт.

T=2101212492009476143 | @Tim_Dettmers | 2026-09-19T07:31+00:00 | L737 RT90 C50 V81607 | rt
URL=https://x.com/Tim_Dettmers/status/2101212492009476143
RT-OF @madiator (L737): Introducing Bespoke Nimble: an open data, open model, open recipe for an open Jev.

Code and info: https://t.co/aC7kPejrcj
Model: https://t.co/snwKGdhn1I

Data:
* A new data curation recipe called contrastive data curation.
* Slightly change facts to generate negative data. This pushes the model to discriminate better and become a better decision maker. The calibration is implicit.
* Didn't do ablations but I think this is a critical piece!
* This also means training data doesn't need probabilities.
* Data covered 10 categories, and is fully synthetic.
* This data is split into train and eval.

Training
* LoRA finetune of Qwen3.5-9B.
* Distillation-free: we use Jev to only evaluate.
* No RL yet!

Serving
* Parallel constrained decoding as suggested by  @NielsRogge and @harshagundal.

Results:
* The post-trained Qwen (Nimble) became substantially better on our curated eval: 66% for Qwen to 90% for Nimble. Jev is at 93%.
* 100ms on H100 and free to use on your macbook! Feel the AGI for free.
* 2 days of building in public. :)

Big caveat is that there is no standard benchmark to measure performance, and it's possible Nimble is much worse on other benchmarks compared to Jev. But it should be better than Qwen!

We thank @typesafeai for making Jev and the inspiring discussions in the community. Hope this release lifts all the boats and encourages more research and activity in this space.
RT-URL=https://x.com/madiator/status/2100990591215783946
TEXT: RT @madiator: Introducing Bespoke Nimble: an open data, open model, open recipe for an open Jev.

Code and info: https://t.co/rBzpX3KpHt
Mo…
LINKS: https://github.com/bespokelabsai/nimble
--
## @trq212 — 1 шт.

T=2101009395052343462 | @trq212 | 2026-09-18T18:04+00:00 | L26212 RT2225 C1698 V3397265 | thread(3)
URL=https://x.com/trq212/status/2101009395052343462
TEXT: You can see the source for the mod here! https://t.co/ZGJxRbh33b
[->] AGENTS.md support is built off of Claude Code mods, our upcoming way to customize the Claude Code harness.

This is a built-in mod, but you’ll be able to build custom versions of project instructions yourself as you’d like too.
[->] We're adding support for AGENTS.md to Claude Code. 

Starting today in version 2.1.277, if there is no CLAUDE.md in a folder, Claude will check for and use AGENTS.md.

You can toggle this behavior in /config.
LINKS: https://github.com/anthropics/claude-code/tree/main/mods/agents-md
--
## @wunderwuzzi23 — 1 шт.

T=2100897680696447259 | @wunderwuzzi23 | 2026-09-18T10:40+00:00 | L22 RT0 C1 V1307 | post
URL=https://x.com/wunderwuzzi23/status/2100897680696447259
TEXT: Had a great time at Bluehat Asia
QUOTED @MSFTBlueHat: What happens when an AI assistant inherits the privileges of the user it's helping?

At BlueHat Asia, Johann Rehberger (@wunderwuzzi23) discussed how SQL Copilot in SQL Server Management Studio can become a powerful target when connected to highly privileged accounts. Through his demos, he showed how "read-only" assumptions can break down, how prompt injection techniques can influence AI behavior, and why security boundaries matter just as much as model instructions.

The talk offered a deep div
--
