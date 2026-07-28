# X-FEED 2026-07-28 part 12/13 | items: 10

## @thorstenball (продолжение)

T=2081746978623328767 | @thorstenball | 2026-07-27T14:22+00:00 | L22 RT3 C6 V4346 | rt
URL=https://x.com/thorstenball/status/2081746978623328767
RT-OF @lewis_b_metcalf (L22): Yea, that is THE question right now! 

5 weeks ago, I had the same question - in fact, I was kinda the steward of the TUI on our team, and now I work ~100% in orbs, and I would hate to go back. 

Weirdly, it's kinda tricky to explain why, but it has changed the way I work, and changed the type of work I would take on. I'll make an attempt here though, hopefully without this turning into an essay...

In a pithy phrase: 
It brings friction down to zero.

By friction, I mean a number of things:
- The friction of starting a new feature or fix or experiment, where normally you'd need a new workspace or checkout and so on.
- The friction of storing work and coming back to it later, which you'd have to think about storing, remembering, etc.
- The friction of working on lots of things in parallel, which you'd otherwise have to keep track of, ensure isolation, etc.
- The friction of having an agent run long manual test runs, which would otherwise consume shared resources

All of those things don't sound like big things, but it's like they're a thousand paper cuts that, in aggregate, make the mental-load of running lots of agentic processes unmanageable. 

For something a bit more tangible; a lot of my orbs are started with single prompts that are just a screenshot of a tweet of a user reporting a bug. That's enough for a high-mode orb to track it, read production logs, reproduce it, send me a screenshot, propose a fix - normally a pretty good one - and ship it. The friction for me starting that work is basically zero. No local checkout, no making sure git status is clean, no messing around with worktrees, no making sure my current dev work hasn't messed up the local db. 

Other orbs are big features - I'd often say something like: 'ok, now give me 10 storybooks so i can see how it looks in every situation" or "manually test this in the matrix of possible state combinations, take screenshots, and make a video to demo the happy path". Who cares if it takes a long time? The fri
RT-URL=https://x.com/lewis_b_metcalf/status/2081744155517051384
TEXT: RT @lewis_b_metcalf: @olrtg_ @thorstenball Yea, that is THE question right now! 

5 weeks ago, I had the same question - in fact, I was kin…
--
T=2081755650992812086 | @thorstenball | 2026-07-27T14:56+00:00 | L2 RT0 C0 V33 | post
URL=https://x.com/thorstenball/status/2081755650992812086
TEXT: @olrtg_ @lewis_b_metcalf I use it every day to check for unshipped release posts; or "remind me in 1hr to check on the release of that" or something.
--
T=2081805589554847754 | @thorstenball | 2026-07-27T18:15+00:00 | L107 RT8 C11 V11363 | rt
URL=https://x.com/thorstenball/status/2081805589554847754
RT-OF @sqs (L107): Time capsule of how I'm building software with Amp and orbs and all...more good change in the last month than all of last year https://t.co/2lqKTKCRqU
RT-URL=https://x.com/sqs/status/2081783179523084495
TEXT: RT @sqs: Time capsule of how I'm building software with Amp and orbs and all...more good change in the last month than all of last year htt…
--
T=2081808493229588629 | @thorstenball | 2026-07-27T18:26+00:00 | L47 RT1 C1 V4656 | post
URL=https://x.com/thorstenball/status/2081808493229588629
TEXT: 20% cheaper orbs!
QUOTED @sqs: Just reset all Amp subscribers' orb usage. We had some orb startup bugs on Sunday (fixed).

Also just cut @AmpCode orb prices by 20% for everyone.

It's orbin' time! https://t.co/IIVk1tlLDm
--
T=2081812544444879086 | @thorstenball | 2026-07-27T18:42+00:00 | L40 RT1 C2 V9275 | post
URL=https://x.com/thorstenball/status/2081812544444879086
TEXT: Turns out we did have a plan mode.

For six weeks, internally.

And then we ripped it out instead of releasing it. https://t.co/jncTi5s8lj
QUOTED @thorstenball: @mitsuhiko @badlogicgames I'm pretty sure Beyang was referring to an internal feature or TODOs but not plan-mode as we know it. I'm 99.99 sure we never had it. And your tweet is the only reason why I'm not 100%.
--
T=2081837549757112331 | @thorstenball | 2026-07-27T20:22+00:00 | L14 RT3 C0 V4991 | rt
URL=https://x.com/thorstenball/status/2081837549757112331
RT-OF @jedelstein25 (L14): In case you were unsure about how Orb-pilled the @AmpCode team truly is. Here is a chart that shows our internal shift from local to cloud agents for the development of Amp itself.

P.S. I wouldn’t be surprised to see that number at 95%+ by the end of the week https://t.co/uMmpstmypM
RT-URL=https://x.com/jedelstein25/status/2081829067041722552
TEXT: RT @jedelstein25: In case you were unsure about how Orb-pilled the @AmpCode team truly is. Here is a chart that shows our internal shift fr…
--
T=2081843988034719924 | @thorstenball | 2026-07-27T20:47+00:00 | L1 RT0 C0 V94 | post
URL=https://x.com/thorstenball/status/2081843988034719924
TEXT: @r00k @adamwathan I'm here, right now!
--
T=2081843873026875625 | @thorstenball | 2026-07-27T20:47+00:00 | L43 RT0 C2 V2362 | post
URL=https://x.com/thorstenball/status/2081843873026875625
TEXT: Boston is looking good! https://t.co/JsqD4nvT2A
--
T=2081852279276081486 | @thorstenball | 2026-07-27T21:20+00:00 | L2 RT0 C1 V752 | thread(3)
URL=https://x.com/thorstenball/status/2081852279276081486
TEXT: @d_dizhevsky That or Amp-hosted projects or this workaround, let me find it
[->] @d_dizhevsky Ooops, forgot to paste:

GIT_CONFIG_COUNT=1
GIT_CONFIG_KEY_0=url.https://USERNAME:TOKEN@gitlab.com/.insteadOf
GIT_CONFIG_VALUE_0=https://t.co/VzZazNTK3f
[->] @d_dizhevsky Adding these to your user env vars will let Amp clone from gitlab for orbs, I'm sure you could change this to work with Azure? https://t.co/1wlIvc1J2a
LINKS: https://gitlab.com/
--
## @trq212 — 1 шт.

T=2081875343246250431 | @trq212 | 2026-07-27T22:52+00:00 | L5291 RT714 C1731 V2858515 | rt
URL=https://x.com/trq212/status/2081875343246250431
RT-OF @AnthropicAI (L5291): There’s been a lot of speculation about where we stand on open-weights models. We’ve outlined our views in full here: https://t.co/NtXQuWm2g5
RT-URL=https://x.com/AnthropicAI/status/2081864750296658008
TEXT: RT @AnthropicAI: There’s been a lot of speculation about where we stand on open-weights models. We’ve outlined our views in full here: http…
LINKS: https://www.anthropic.com/news/position-open-weights-models
--
