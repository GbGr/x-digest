# X-FEED 2026-07-28 part 4/13 | items: 7

## @mattpocockuk — 7 шт.

T=2081655893427450117 | @mattpocockuk | 2026-07-27T08:20+00:00 | L218 RT6 C12 V8782 | thread(8)
URL=https://x.com/mattpocockuk/status/2081655893427450117
TEXT: This is a good post and obviously hits a nerve with folks. I think folks are rightly concerned about 'heaviness' of skills, and I have criticised other skill libraries/frameworks for being too heavy-handed.

My goal is always to make the skills as light as they can possibly be. Not only within the skills themselves, but lowering the context load of the overall approach. Small skills are easier to maintain, audit, and survive model changes better. Recent guidance on prompting Fable seems to back that up - say less to the model, and it does better.

Documents are for the model, not the human

Here's where I think you got something wrong. Every 'document' I use is designed for the constraints of models, not for humans.

Why have a spec at all? To clearly define the destination in an artifact which can then later be checked via /code-review.

Why have tickets? So that you can split work into smart zone-shaped sizes.

I'm using the terms 'spec' and 'tickets' because they are familiar to devs - not because I am trying to mimic Jira.

Wayfinder, similarly, is designed for the constraints of models. It breaks down planning into context-window shaped chunks of work.

The smart zone

If there is a bitter lesson in AI coding, it's about the "smart zone". My skills assume that working with irrelevant information in your context window is bad, and so they break work into session-sized chunks via /to-tickets.

This is strictly an AFK agent optimization - AFK agents do better with chunks scoped ahead of time. I've experimented with just a spec and /goal, but the results were worse.

As you can tell, your itch is something I think about every release of my skills. I am always trying to reduce my maintenance surface, to make the skills smaller and more useful. I often do a no-op pass on my skills to check for things the models now do out of the box.

Thanks for giving me an opportunity to articulate this! A really well-phrased question.
[->] @minid @DanielMiessler Good codebases are easy to make changes in without breaking things
[->] @minid @DanielMiessler And no, it really can't
[->] @ljbuilds @DanielMiessler Yep, difference between stateful (humans) and stateless (models)
[->] @DanielMiessler One thing I don't like about this is that showing the agent the final state too quickly leads to it rushing. This is the main issue with most issues of plan mode - a sycophantic rush to create an asset means the real value, alignment, gets skipped.
[->] It feels like to me that you're asking me "how can I make your skills smaller" when they're already (mostly) as small as they can be.

Everyone's basically landing on the same primitives, which is a relatively minimal "plan, then build, then review".

There are some extra steps to parallelize across workers (like there have always been) but that's the main thrust.

To me, I see human -> AI interaction as a communication barrier, just like human -> human interaction. The communication barrier is baked in, you can't dodge it.

So it doesn't feel like plan/implement/review is going away.
[->] @DanielMiessler What you're describing is a SDLC, just given a fancy name

It feels to me like you're trying to make fetch happen
[->] I see my skills as empowering people to use agents to build better apps, not empowering agents to own more of the process.

I.e. I don't mind increasing the cognitive load on users a bit as long as it gets better results from AI.

(and bear in mind, we're really talking about 5 core skills here, it's not a lot)

So this goal of 'unification' feels more tied to making powerful agents. Most skills packages, like superpowers, work this way.
--
T=2081672829016084727 | @mattpocockuk | 2026-07-27T09:27+00:00 | L309 RT0 C16 V19438 | thread(5)
URL=https://x.com/mattpocockuk/status/2081672829016084727
TEXT: @theo Make it "grill mode"
[->] @theo Genuinely, this is what I'd do if I had my own harness. The issue with plan mode is the rush towards a plan - the rush to create an asset.
[->] @yousefrol @theo &gt; yours make the model hallucinate

Could you expand a bit? And maybe raise an issue?
[->] @AdamHoltererer @theo Here's my sign:

https://t.co/eVyFxO2tI6
[->] @AdamHoltererer @theo Ah, misunderstood then. I haven't used it.
LINKS: https://www.aicodingdictionary.com/?term=harness
--
T=2081685158915109161 | @mattpocockuk | 2026-07-27T10:16+00:00 | L22 RT0 C1 V3052 | post
URL=https://x.com/mattpocockuk/status/2081685158915109161
TEXT: @robpalmer2 @acutmore @TechAtBloomberg @TC39 Ash smashing it again
--
T=2081702807753703823 | @mattpocockuk | 2026-07-27T11:26+00:00 | L1 RT0 C1 V99 | thread(2)
URL=https://x.com/mattpocockuk/status/2081702807753703823
TEXT: @KazakisThanos Yes, most def

Code is the environment your agents operate in

Garbage in, garbage out
[->] @KazakisThanos /codebase-design
--
T=2081708568743473238 | @mattpocockuk | 2026-07-27T11:49+00:00 | L3 RT0 C1 V273 | thread(2)
URL=https://x.com/mattpocockuk/status/2081708568743473238
TEXT: @dorianzlatan Can't you disable that?
[->] @maximehugodupre Yep, batching is coming to all grillings in 1.2
--
T=2081762573670613421 | @mattpocockuk | 2026-07-27T15:24+00:00 | L18 RT0 C5 V3176 | thread(2)
URL=https://x.com/mattpocockuk/status/2081762573670613421
TEXT: @trashh_dev Which MTG set is this from?
[->] @trashh_dev Ah, not another Universes Beyond
--
T=2081766847477666147 | @mattpocockuk | 2026-07-27T15:41+00:00 | L271 RT2 C22 V25608 | thread(7)
URL=https://x.com/mattpocockuk/status/2081766847477666147
TEXT: First day of course filming with a teleprompter

So good. Still 90% improvising, but doing it from a pre-written text is far less exhausting and makes the quality higher
[->] Thousands of hours of filming in and there's always ways you can improve
[->] I have a custom video editor so the teleprompter state is synced to my editor

Absolute dreamland, personal software paying off again
[->] @elderjava AI, based on some beats I've hand-organized. Doesn't need to be perfect since I'm improvising around it
[->] @odiesec Elgato one, ~£200
[->] @simeonGriggs Same same
[->] @wendy7756 Of course not
--
