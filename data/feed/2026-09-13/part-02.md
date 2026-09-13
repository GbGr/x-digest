# X-FEED 2026-09-13 part 2/8 | items: 6

## @dexhorthy — 6 шт.

T=2098675233398079563 | @dexhorthy | 2026-09-12T07:29+00:00 | L22 RT1 C4 V7722 | post
URL=https://x.com/dexhorthy/status/2098675233398079563
TEXT: what so just every time we get hacked now we just blame rogue oai agents lol
QUOTED @zeeg: 🤠 https://t.co/nVFPg3C1DL
--
T=2098864953709253024 | @dexhorthy | 2026-09-12T20:02+00:00 | L99 RT4 C14 V9950 | thread(8)
URL=https://x.com/dexhorthy/status/2098864953709253024
TEXT: full writeup comign next week. watch out for that slop out there
[->] Astra seems slightly more clustered toward "fewer, more complex functions", while glm and sol are more centered around "more functions, each less complex" https://t.co/tuSZ5xAv1S
[->] across our top 4 code quality metrics, the winners are mixed:

- Mean Cyclomatic Complexity - Astra had the lowest
- Most complex function - GLM 5.3's most complex function was simpler than sol/astra's
- Astra had the least % of cloned lined, doing almost 5x better than GLM
- Astra had the smallest number of single-use functions
[->] Astra XHigh is the first model to ace circuit_eval, among every time i've run this benchmark. https://t.co/NXZMIMSoUi
[->] price vaguely correlates to quality, although GLM 5.3 is close to Sol's score for ~half the price. 

Astra is ~twice as good as Sol for the same price https://t.co/z4gD0k1LdM
[->] for the circuit_eval challenge, astra xhigh leads the pack in cyclomatic complexity and in graph dependency entropy by a pretty sizable margin https://t.co/kPXJWetxcw
[->] finally finished a full SlopCodeBench run against GLM 5.3, Sol 5.6, and Astra (Fable 5.1 results coming soon)

This is different from all our previous research on SlopCodeBench (from @GOrlanski  @ UW) in that we ran the full benchmark, every single scenario here. Previous runs did a small subset of the challenges.

Asterisks:
- this was run over ~1 week and had to be resumed a few times due to various provider outages
- I still think a more scientific approach here would be to do what's common with other benchmarks, which is run multiple evaluations and aggregate the scores

Looks like Astra scores a few points higher than gpt-5.5 here. Not as many as I'd think. I'm surprised Sol got lower than gpt 5.5 because in my experience I like working with Sol a bit more. 

My vibes-best guess is that the newer models are likely to go more off the rails on higher thinking modes (e.g. I almost always use Sol in medium or low effort for most work on @humanlayer_dev)
[->] Correction. - prev post axes i read wrong - Astra writes more and simpler functions, glm/sol write fewer and more complex
--
T=2098877952561996083 | @dexhorthy | 2026-09-12T20:54+00:00 | L87 RT7 C11 V9114 | post
URL=https://x.com/dexhorthy/status/2098877952561996083
TEXT: dark factories = fail eventually*

Lights on factories = very good idea plz automate everything that can be automated
QUOTED @petergyang: I am skeptical of "software factories."

Other than for verification & testing, I don't think AI is at a point where it can self-improve a product or build a new feature end-to-end without human in the loop.

Whenever I loop something overnight to build something new = if it makes one wrong assumption the whole thing becomes a waste of tokens. 

What products or features have been built end-to-end with a software factory and no human defining the requirements or checking the work?
--
T=2098906764678955276 | @dexhorthy | 2026-09-12T22:49+00:00 | L24 RT0 C0 V3575 | post
URL=https://x.com/dexhorthy/status/2098906764678955276
TEXT: I am adding p(starcraft) to my p(doom) charts
QUOTED @ZergGirl: The new StarCraft game looks like helldivers but it’s an open world shooter. Having turned into a more social and casual gamer, I’d be honestly excited to play!

But release date 2030? 😭😭😭
--
T=2098912016987730059 | @dexhorthy | 2026-09-12T23:09+00:00 | L66 RT6 C18 V4727 | post
URL=https://x.com/dexhorthy/status/2098912016987730059
TEXT: coming soon to a humanlayer new you:

live multiplayer prompting - co-author a single prompt with your team. 

A few weeks ago we shipped "send a prompt to your colleague's session" - now we made each individual prompt collaborative. 

No cloud agents required, works wherever you run your agent - across laptops, mac minis, cloud compute, we even have this working in coding agent sessions that run in disposable compute like github actions. 

built on durable streams and @rivet_dev actors on ECS - incredible work from @0xblacklight 

That's in addition to all the other things we made collaborative in the last 2 months:

- live google-docs style commenting on plans, right in the IDE, or plan/collab from your phone
- diffs stream live as the coding agent is working, so you can comment on changes wayyy before PR

shift collaboration left, shift alignment left, go check it out @humanlayer_dev - free for small teams go check it out today
--
T=2098933523529027819 | @dexhorthy | 2026-09-13T00:35+00:00 | L124 RT2 C9 V35267 | post
URL=https://x.com/dexhorthy/status/2098933523529027819
TEXT: oh shit
QUOTED @nickmmark: An alternative hypothesis:
- model performance is plateauing
- compute is getting much more expensive 
- AI data centers are massively unpopular
- slowing down AI development is a way to explain slowing progress, reduce spending, and try to regain some goodwill.
- This is an effort to save the IPO not humanity.
--
