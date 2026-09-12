# X-FEED 2026-09-12 part 8/9 | items: 10

## @swyx — 3 шт.

T=2098467486878560288 | @swyx | 2026-09-11T17:43+00:00 | L9 RT3 C2 V3882 | rt
URL=https://x.com/swyx/status/2098467486878560288
RT-OF @bradwmorris (L9): still think this is/was one of the best takes of the year @eisokant with @swyx and @vibhuuuus on @latentspacepod 

very much aligned with the thesis - build your own agent infrastructure. 
https://t.co/wGGiUAumzb

give the agent an isolated sandbox with a thin set of tools and workflows, and the ability to write and execute code. Keep the harness thin.
RT-URL=https://x.com/bradwmorris/status/2098286813500850304
TEXT: RT @bradwmorris: still think this is/was one of the best takes of the year @eisokant with @swyx and @vibhuuuus on @latentspacepod 

very mu…
LINKS: https://x.com/bradwmorris/status/2098282961062015411?s=20
--
T=2098507015253573687 | @swyx | 2026-09-11T20:20+00:00 | L22 RT5 C1 V4655 | rt
URL=https://x.com/swyx/status/2098507015253573687
RT-OF @aiDotEngineer (L22): congratulations to Jonathan and Cognition! more on the ambitious software this team is building at AIE World's Fair: https://t.co/BmnSvt8aXp https://t.co/GTZId8banp
RT-URL=https://x.com/aiDotEngineer/status/2098501840228782474
TEXT: RT @aiDotEngineer: congratulations to Jonathan and Cognition! more on the ambitious software this team is building at AIE World's Fair: htt…
LINKS: https://www.youtube.com/watch?v=H7vFrcNWXzs
--
T=2098507903921713573 | @swyx | 2026-09-11T20:24+00:00 | L37 RT6 C3 V5887 | rt
URL=https://x.com/swyx/status/2098507903921713573
RT-OF @cerebras (L37): Connecting the dies and working around defects were fundamental challenges for wafer-scale computing. Making it work also came down to power, cooling, and reliability.

@seanlie explains how those lessons are shaping @cerebras’ approach to stacking DRAM.

From @seanlie’s conversation with @swyx on @latentspacepod.
RT-URL=https://x.com/cerebras/status/2098505357475594506
TEXT: RT @cerebras: Connecting the dies and working around defects were fundamental challenges for wafer-scale computing. Making it work also cam…
--
## @thorstenball — 7 шт.

T=2098319678946886124 | @thorstenball | 2026-09-11T07:56+00:00 | L418 RT2 C141 V81851 | thread(3)
URL=https://x.com/thorstenball/status/2098319678946886124
TEXT: Okay, maybe I'm being dumb here, so:

2 Chrome profiles, private &amp; work. 2 Chrome windows, one per profile.

50% of the time I click a link it opens in the wrong profile. Because macOS uses last-used window and ... that's not always the right now.

How do others handle this?
[->] This might be it: https://t.co/gZc8acF59V
[->] Wild times: https://t.co/Z72VNjZnwR
LINKS: https://x.com/_laurynas/status/2098321875520667826?s=20 ; https://x.com/thorstenball/status/2098327328845656224
--
T=2098327328845656224 | @thorstenball | 2026-09-11T08:26+00:00 | L163 RT3 C22 V47306 | post
URL=https://x.com/thorstenball/status/2098327328845656224
TEXT: I pointed Amp at Velja (https://t.co/z2NzD7jUao, $8) and Choosy (https://t.co/1Rp72sPyU5, $10) and asked it build a personal option.

It did it using Fable 5.1 for $5.

I now have a tiny menu bar app that routes to the correct browser. https://t.co/BtaFhMtM2J
QUOTED @thorstenball: Okay, maybe I'm being dumb here, so:

2 Chrome profiles, private &amp; work. 2 Chrome windows, one per profile.

50% of the time I click a link it opens in the wrong profile. Because macOS uses last-used window and ... that's not always the right now.

How do others handle this?
LINKS: https://sindresorhus.com/velja ; https://choosy.app/
--
T=2098327783596232921 | @thorstenball | 2026-09-11T08:28+00:00 | L10 RT3 C0 V2002 | rt
URL=https://x.com/thorstenball/status/2098327783596232921
RT-OF @abraguilera (L10): Ok here's another one. @AmpCode orbs can spawn other orbs (h/t @thorstenball for the cool demos) so I can create a main orb to design the feature and then it coordinates and oversees the implementation.

In this case the main orb is in Ultra mode and all the worker orbs are medium mode. Then main orb reviews what the workers did, makes edits (or requests them) and commits the changes. 

You can steer the work as it happens but you don't have to create all the new "chats" by hand. 

It's all handled by the main agent. In some cases it spawned parallel orbs for separate concerns, then reconciled everything and kept pushing. 

And for this worked, it paused every time it had a shippable slice, showed proof of work (screenshots of the feature being used in the dashboard app), asked for clarification or confirmation on some of its decisions.

And this (kinda complex) feature is now production ready in a few hours, half of it dictated from my phone in between house chores, taking out the dog or putting my daughter to bed last night.

Orbs are awesome
RT-URL=https://x.com/abraguilera/status/2098326894126973317
TEXT: RT @abraguilera: Ok here's another one. @AmpCode orbs can spawn other orbs (h/t @thorstenball for the cool demos) so I can create a main or…
--
T=2098415334839505100 | @thorstenball | 2026-09-11T14:16+00:00 | L371 RT25 C26 V162648 | post
URL=https://x.com/thorstenball/status/2098415334839505100
TEXT: I recorded how I use agents day to day.

In this video:

• Agents spawn other agents to check whether performance improvements actually helped in production.
• I have an agent fix UI flicker and test the result in a portal.
• We investigate and fix an `amp clone` bug for a Nix user.
• I toggle feature flags directly from the remote machine.
• I ask an agent for "irrefutable proof" that its fix works.

You can see all the prompts, what the agents do, and how I review their work (or don't).

Timestamps:

0:15 Shipping and monitoring performance improvements
2:11 Investigating an amp clone bug in Nix
3:51 Fixing UI flicker and testing in a portal
5:55 Starting an agent to promote Recap to an opt-in experimental feature
7:45 Previewing the sidebar flicker fix in a portal
9:38 Reviewing production performance canaries
11:45 Checking in on the production fix and granting read-only log access
12:47 Check Recap Experimental Setting Copy
13:39 Check in on amp clone Nix fix
14:49 Sidebar fix deployment check schedule
15:35 Checking in on performance fix thread's log analysis
16:14 Asking the agent for irrefutable proof of its fix
17:00 Checking Recap experimental setting
18:31 Testing a mechanical refactor of the CLI
21:48 Checking amp clone nix fix agent evidence
23:20 Checking feedback from Slack
--
T=2098441525138956443 | @thorstenball | 2026-09-11T16:00+00:00 | L19 RT2 C6 V7479 | rt
URL=https://x.com/thorstenball/status/2098441525138956443
RT-OF @iannuttall (L19): I use them a lot in Conductor but the Amp push-to-main flow in an Orb is smoother than worktrees. 

Just need to figure out how to do parallel stuff on my Mac Mini without worktrees now.
RT-URL=https://x.com/iannuttall/status/2098439485964918798
TEXT: RT @iannuttall: I use them a lot in Conductor but the Amp push-to-main flow in an Orb is smoother than worktrees. 

Just need to figure out…
--
T=2098451482819379295 | @thorstenball | 2026-09-11T16:39+00:00 | L77 RT1 C7 V5291 | post
URL=https://x.com/thorstenball/status/2098451482819379295
TEXT: Whenever I think "oh wow the coding agent space is crazy"

I remind myself that at least I'm not in the personal assistant space
--
T=2098459685082857502 | @thorstenball | 2026-09-11T17:12+00:00 | L30 RT0 C1 V3693 | post
URL=https://x.com/thorstenball/status/2098459685082857502
TEXT: New Raising An Agent!
QUOTED @AmpCode: What is the computer for now?

In Raising an Agent S2E4, @sqs and @thorstenball explore how agents can do more than just ship code, discuss recent outages, and ask what happens to our computers when more work moves into Orbs.

00:00 Intro: What is the computer for now?
01:32 New models & aiming higher with agents
04:42 An agent's job after the code ships
10:19 Mini evals & keeping the team's context in threads
13:38 Performance testing & production canaries
18:36 Amp's recent outages & what went
--
