# X-FEED 2026-07-25 part 2/14 | items: 10

## @dexhorthy — 10 шт.

T=2080659639356850667 | @dexhorthy | 2026-07-24T14:21+00:00 | L31 RT4 C6 V3300 | rt
URL=https://x.com/dexhorthy/status/2080659639356850667
RT-OF @Pragmatic_Eng (L31): Why did spec-driven development never take off - the workflow tools like Amazon’s Kiro or GitHub Workspaces encouraged? @dexhorthy, founder of HumanLayer:

“These projects have a really interesting idea: you maintain a set of specifications for your software, and then you maintain the code itself, and the dream is the coding part is just compiling specs into code.

But that part never really materialized. I’m on a GitHub issue in spec kit that’s been open for a year, and every couple of weeks I get a new email on the thread of people complaining about the same problem:

I edit my specs and then I edit the code, and the code drifts from the specs. How do I keep the specs up to date as the code is changing?

You now have two sources of truth, and it stops being useful. That’s why with RPI (Research, Plan, Implement), the docs are tactical execution docs -  I do the research, the plan, the implementation, and I throw the docs out. 

The next time I need research I just do it from scratch, because tokens are cheap and my time is expensive.”
RT-URL=https://x.com/Pragmatic_Eng/status/2080658383384805729
TEXT: RT @Pragmatic_Eng: Why did spec-driven development never take off - the workflow tools like Amazon’s Kiro or GitHub Workspaces encouraged?…
--
T=2080675027041849454 | @dexhorthy | 2026-07-24T15:22+00:00 | L81 RT3 C4 V4941 | post
URL=https://x.com/dexhorthy/status/2080675027041849454
TEXT: we'll take it - thanks for the jovial (rowdy?) discussion yesterday https://t.co/kwqojC5Gvl
--
T=2080694316801085899 | @dexhorthy | 2026-07-24T16:39+00:00 | L57 RT3 C5 V25036 | rt
URL=https://x.com/dexhorthy/status/2080694316801085899
RT-OF @0xblacklight (L57): does he know https://t.co/fDddRHbnBr
RT-URL=https://x.com/0xblacklight/status/2080676620978041241
TEXT: RT @0xblacklight: does he know https://t.co/fDddRHbnBr
--
T=2080697380379427275 | @dexhorthy | 2026-07-24T16:51+00:00 | L505 RT47 C27 V61912 | post
URL=https://x.com/dexhorthy/status/2080697380379427275
TEXT: gave up on waiting on nikita for the articles fix - part 1 is here part 2 is coming https://t.co/8aS4vN6LK3
LINKS: http://x.com/i/article/2078710413345402880
--
T=2080720510561013842 | @dexhorthy | 2026-07-24T18:23+00:00 | L27 RT1 C3 V3282 | post
URL=https://x.com/dexhorthy/status/2080720510561013842
TEXT: everybody wanna do software engineering but nobody wanna rewrite the ! operator from scratch using nothing but bit shifting
--
T=2080723580380496226 | @dexhorthy | 2026-07-24T18:35+00:00 | L4 RT1 C1 V1105 | rt
URL=https://x.com/dexhorthy/status/2080723580380496226
RT-OF @itschef_ai (L4): @dexhorthy I was probably one of the first people to read about dark factories when Simon posted about it and was immediately fascinated. Internally, we immediately built a dark/loghts-off factory and eventually came to the same conclusion. 

With no disrespect to anyone a lot of the motherships you mentioned seem to larp to make themselves project as agentic by sharing how they cut people and made structures more agentic. 

I’ve talked to atleast 6-7 enterprises in the 2months that have suffered the consequences ^.

Educated vibing is ok, but goalmaxxing, dark factories are unsustainable for maintaining prod level code.
RT-URL=https://x.com/itschef_ai/status/2080722725132505275
TEXT: RT @itschef_ai: @dexhorthy I was probably one of the first people to read about dark factories when Simon posted about it and was immediate…
--
T=2080726631484887538 | @dexhorthy | 2026-07-24T18:47+00:00 | L29 RT1 C5 V22572 | post
URL=https://x.com/dexhorthy/status/2080726631484887538
TEXT: opus 5 benchmarking on slopcodebench https://t.co/rq5xrpoW4O
LINKS: https://x.com/i/broadcasts/1qJVmmPywOXGB
--
T=2080734551912202354 | @dexhorthy | 2026-07-24T19:19+00:00 | L91 RT4 C13 V19680 | thread(8)
URL=https://x.com/dexhorthy/status/2080734551912202354
TEXT: benchmarking opus 5 on slopCodeBench - we are part way into the eval run - will keep posting status updates as we go - so far (no surprise) sonnet 5 slower and more expensive than opus 4.8 and opus 5 

Checkpoint 1, problem one:

Opus 4.8 - 7 turns
Opus 5 - 11 turns
Sonnet 5 - 33 turns and counting 😅

more results as they stream in
[->] Update - 

1) Sonnet has now cost inverted, no longer more expensive now that the basics are built out

2) Opus 5 unmatched on defect rates - test failures per checkpoint:

Opus 4.8: 1→2→4→4→6→8→10
Sonnet 5: 1→2→2→2→2→3
Opus 5: 0→0→0→1 https://t.co/g1guxPNkwh
[->] 45 minutes later, the newest updates:

Opus 4.8 and Sonnet 5 got their first "strict passes" on the database_migration exercise

Opus 5 got its first checkpoint without a strict pass at ck4 - but up until that point was the only one with any "strict passes" - 3 in a row to start the race 

Watch the live progress here: https://t.co/3I0THDiBIV

and for those who asked, we're working off the SlopCodeBench paper - https://t.co/baNnxtbZ8T
[->] Update - problem 1 (circuit_eval, 8 checkpoints) is done for all three

Opus 5 wins outright. defects left open at the end:

Opus 5: 2 
Sonnet 5: 7 
Opus 4.8: 12

it also cost ~2x sonnet to get there ($44 vs $24)

but the ranking flips on problem 2 (database_migration):

Opus 4.8: 15 open 
Sonnet 5: 26 open

sonnet came apart at ck4 - core 4/14, fifteen new defects in a single checkpoint

still waiting on opus 5 - may be better and more thorough but its also slower 

follow along live here (and we made it mobile friendly too) 

https://t.co/3I0THDiBIV
[->] @DrockStowe okay made it a little more mobile friendly thanks claude
[->] still cooking! Seems like all three failed database_migration in the same way opus 5 (model orchestrating this) seems to have some feedback for @GOrlanski and team on the cost counting semantics 😅

Opus 4.8 and Sonnet 5 are finished with exactly 1/17 strict passes each (on the same problem)

Opus 5 is on problem 14/17 and has 4 strict passes so far.

follow along here https://t.co/3I0THDiBIV!
[->] @GOrlanski WE ARE DOWN TO THE FINAL STRETCH - OPUS 5 is already up by 3 points - I think the biggest takeaway here though is that we have a truly unsaturated benchmark for the next frontier of models

nice work @GOrlanski and team https://t.co/xZOUZmVFQF
[->] @GOrlanski final result - opus 5 wins but none of them did a very good job IMO

bonus content. the frontier is still dumb af 

&gt; The user is upset because I made a critical mistake: I overwrote their edited draft by patching it with the final version, then sent it out. https://t.co/Fv4uGXfiSi
QUOTED @dexhorthy: opus 5 benchmarking on slopcodebench https://t.co/rq5xrpoW4O
LINKS: https://cloud.dev.codelayer.gg/shared/artifacts/019f9589-c234-7001-9411-1affefdd02ba?key=43656371-414e-4e43-8147-0c73f0e36951 ; https://arxiv.org/html/2603.24755v1
--
T=2080850557489877222 | @dexhorthy | 2026-07-25T03:00+00:00 | L34 RT0 C1 V2441 | post
URL=https://x.com/dexhorthy/status/2080850557489877222
TEXT: lmao okay bud relax https://t.co/svvoP7syRH
--
T=2080867239608369444 | @dexhorthy | 2026-07-25T04:06+00:00 | L7 RT0 C3 V1570 | post
URL=https://x.com/dexhorthy/status/2080867239608369444
TEXT: oh yeah and opus 5 really likes calling the "clean coder" skill i keep forgetting i left in my home directory. thx @unclebobmartin https://t.co/ENLJmyDm2b
--
