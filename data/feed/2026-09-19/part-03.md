# X-FEED 2026-09-19 part 3/7 | items: 12

## @lateinteraction — 4 шт.

T=2101008635568513259 | @lateinteraction | 2026-09-18T18:01+00:00 | L77 RT4 C11 V11932 | thread(2)
URL=https://x.com/lateinteraction/status/2101008635568513259
TEXT: took 2 years but indeed they are bifurcating
[->] i think people are still missing the key idea that you do not write RISC instructions (or even CISC for that matter) by hand! a compiler maps a higher level language that corresponds to your simple abstract machine down into that optimized soup.
QUOTED @lateinteraction: Work like o3 suggests that future foundation models will diverge like RISC and CISC architectures.

Developers will express their system specifications in extremely high-level programming languages.

And compilers will translate those into a few RISC—or many CISC—instructions.
--
T=2101078744433840543 | @lateinteraction | 2026-09-18T22:39+00:00 | L7 RT2 C2 V1199 | rt
URL=https://x.com/lateinteraction/status/2101078744433840543
RT-OF @pamelafox (L7): I just tried out lm15, the new lightweight alternative to litellm from the @DSPyOSS crew.
It works with all Foundry hosted models, like Azure OpenAI, Kimi, and Anthropic.

Examples:
https://t.co/jPz6H1jwfq
https://t.co/6LIkauasMa

lm15 is way faster to import and has 0 deps! https://t.co/uuXqC31VGM
RT-URL=https://x.com/pamelafox/status/2101076778257408361
TEXT: RT @pamelafox: I just tried out lm15, the new lightweight alternative to litellm from the @DSPyOSS crew.
It works with all Foundry hosted m…
LINKS: https://github.com/pamelafox/python-stack-foundry-models/blob/main/examples/lm15_request.py ; https://github.com/pamelafox/python-stack-foundry-models/blob/main/examples/lm15_router.py
--
T=2101124326040740002 | @lateinteraction | 2026-09-19T01:40+00:00 | L58 RT10 C1 V13028 | rt
URL=https://x.com/lateinteraction/status/2101124326040740002
RT-OF @lateinteraction (L58): There are three different problems here. 

Abstractions and training that make models good at programmatic use are very different from those that make models good for user-facing interactions, which in turn are different from those that make models good at test taking.
RT-URL=https://x.com/lateinteraction/status/1888689878789197958
TEXT: RT @lateinteraction: There are three different problems here. 

Abstractions and training that make models good at programmatic use are ver…
--
T=2101125760337510808 | @lateinteraction | 2026-09-19T01:46+00:00 | L74 RT5 C7 V14436 | rt
URL=https://x.com/lateinteraction/status/2101125760337510808
RT-OF @lateinteraction (L74): Conventional programming languages get a few things "right" in a way that AI-based programming will need to bring back instead of giving in to 'vibe coding'.

It's actually useful that you can define and compose functions, define control flow (if statement, for loops, exceptions) explicitly when you want to, divide your program into modules/classes, reuse stable libraries, compile high-level code to lower-level code, etc.

We don't need to nor can we afford to lose any of these. But what we need is to raise the level of abstraction on how you define and test the behavior of individual modules—and to begin to figure out how allow some fuzziness in your specs when you want "intelligent" modules (hint: it'll look like DSPy).
RT-URL=https://x.com/lateinteraction/status/1905447832099983564
TEXT: RT @lateinteraction: Conventional programming languages get a few things "right" in a way that AI-based programming will need to bring back…
--
## @mattpocockuk — 3 шт.

T=2100895593618907402 | @mattpocockuk | 2026-09-18T10:31+00:00 | L550 RT20 C46 V44958 | post
URL=https://x.com/mattpocockuk/status/2100895593618907402
TEXT: Tip: get your agents to classify the merge danger of the PR

1. Is it a one-way door, or a two-way door?

One way doors involve expensive migrations, or are hard to reverse. They need thorough review. Two-way doors are easy to revert.

2. What's the blast radius?

If things go wrong, how bad will it be? Large blast radius: closer review

Helps you apply your precious review time where it's actually needed.
--
T=2100928387753635892 | @mattpocockuk | 2026-09-18T12:42+00:00 | L520 RT33 C49 V32879 | post
URL=https://x.com/mattpocockuk/status/2100928387753635892
TEXT: An actual slide from my talk at @aiDotEngineer Paris next Thursday.

People have this mad idea that their implementer agent should ALSO apply their coding standards

The solution? Hide your coding standards from your implementer agent, fix them in review https://t.co/WPWOiCBsmr
--
T=2101030569123418227 | @mattpocockuk | 2026-09-18T19:28+00:00 | L1453 RT39 C34 V88600 | post
URL=https://x.com/mattpocockuk/status/2101030569123418227
TEXT: Hooray - .agents/skills soon please
QUOTED @trq212: We're adding support for AGENTS.md to Claude Code. 

Starting today in version 2.1.277, if there is no CLAUDE.md in a folder, Claude will check for and use AGENTS.md.

You can toggle this behavior in /config.
--
## @mitsuhiko — 5 шт.

T=2100827444404011028 | @mitsuhiko | 2026-09-18T06:01+00:00 | L507 RT15 C38 V56073 | thread(3)
URL=https://x.com/mitsuhiko/status/2100827444404011028
TEXT: I would not dismiss the idea of using Jev for compaction at all. First of all because most harnesses need some pruning on compaction anyways for cost reasons which Jev might help with. I can see this being quite interesting.
[->] Also, modern compaction in many ways is deeply unintuitive. For instance in Codex, there’s even a remote where the LLM makes a request for a blank context on its own and maintains notes itself.
[->] @dotpem But that's an Anthropic specific problem and affects all compaction
QUOTED @theo: This is a terrible compaction strategy that fundamentally doesn't understand how compaction and context management work.

Seems like a lot of people are confused so let's break this down.

1. Compaction isn't a filter
The role of compaction is to clean up history to keep the agent focused, not just deleting noise. It should be used sparingly when context gets too long, not constantly to keep context small.

2. Jev doesn't even know what it's deciding on!
Models use the context of the thread to d
--
T=2100857561859735853 | @mitsuhiko | 2026-09-18T08:00+00:00 | L133 RT1 C24 V15059 | thread(2)
URL=https://x.com/mitsuhiko/status/2100857561859735853
TEXT: You can kinda layer it on top of MCP but it's really not built for that :(
[->] I wonder if at this point there couldn't be a very of MCP that is literally codemode + openapi + RAG for openapi docs instead. The reference Radius skill is just OpenAPI and it works so well.
--
T=2100917650847154660 | @mitsuhiko | 2026-09-18T11:59+00:00 | L705 RT16 C228 V77427 | post
URL=https://x.com/mitsuhiko/status/2100917650847154660
TEXT: I'm so suck of LLM generated replies on Twitter. I stopped replying almost entirely to my replies on my own Tweets because I expect all of them to just be LLM slop. Why are y'all doing this?
--
T=2101025797188247983 | @mitsuhiko | 2026-09-18T19:09+00:00 | L277 RT4 C18 V24830 | post
URL=https://x.com/mitsuhiko/status/2101025797188247983
TEXT: I paid 25 USD for a cheap Chinese USB device to burn 4500 USD trying to vibecode myself some firmware on it. I have a firmware and it’s about as good as you would expect.
--
T=2101033175262671124 | @mitsuhiko | 2026-09-18T19:38+00:00 | L216 RT3 C19 V36930 | post
URL=https://x.com/mitsuhiko/status/2101033175262671124
TEXT: We gave web components an honest chance. Left terribly disappointed. https://t.co/dAoRxnhO1y
QUOTED @badlogicgames: team decided to go all in on react. i never touched frontend stuff except for lit (don't @ me).

perfect timing. thanks @odysseus0z !

https://t.co/o98Dd6AKA1
LINKS: https://x.com/badlogicgames/status/2101029897950863543?s=20
--
