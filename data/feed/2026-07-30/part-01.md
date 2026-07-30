# X-FEED 2026-07-30 part 1/9 | items: 12

## @_philschmid — 1 шт.

T=2082505615574716524 | @_philschmid | 2026-07-29T16:36+00:00 | L54 RT1 C2 V5117 | post
URL=https://x.com/_philschmid/status/2082505615574716524
TEXT: Cool Test!
QUOTED @skalskip92: gemini 3.5 flash is sooooooo good at image reasoning

image reasoning is when the model has to actually think about what it sees

not just label objects or read text

it needs to connect the facts and figure out what’s going on

reasoning trace:

current order top to bottom: 654, 770, 655, 771, 772
target order: 654, 655, 770, 771, 772
LIS is 4: 654, 655, 771, 772
slide 770 between 655 and 771

answer: 1
--
## @dexhorthy — 11 шт.

T=2082326970629837094 | @dexhorthy | 2026-07-29T04:46+00:00 | L10 RT2 C0 V2063 | rt
URL=https://x.com/dexhorthy/status/2082326970629837094
RT-OF @marcelfahle (L10): Note sure when @humanlayer_dev added them PR Walkthroughs, but it's pretty awesome.. each numbered step is one commit, shown in the order the work happened, with the reasoning attached. You read a change instead of decoding it 🔥 https://t.co/U5gMKjQTkQ
RT-URL=https://x.com/marcelfahle/status/2079494087254639066
TEXT: RT @marcelfahle: Note sure when @humanlayer_dev added them PR Walkthroughs, but it's pretty awesome.. each numbered step is one commit, sho…
--
T=2082328299607556256 | @dexhorthy | 2026-07-29T04:52+00:00 | L91 RT5 C6 V6467 | rt
URL=https://x.com/dexhorthy/status/2082328299607556256
RT-OF @nayshins (L91): Back to my unifying theory on slop:

Creativity takes time to reduce a problem or idea to its core idea or solution. Since llms are trained to generate solutions they will add more than is needed to do so, which is how we get slop. 

Creativity requires synthesis and reduction.
RT-URL=https://x.com/nayshins/status/2082304120279667145
TEXT: RT @nayshins: Back to my unifying theory on slop:

Creativity takes time to reduce a problem or idea to its core idea or solution. Since ll…
--
T=2082473745428676850 | @dexhorthy | 2026-07-29T14:30+00:00 | L15 RT0 C2 V8877 | post
URL=https://x.com/dexhorthy/status/2082473745428676850
TEXT: No contest
QUOTED @gregpr07: What's better for coding?
--
T=2082510831858893115 | @dexhorthy | 2026-07-29T16:57+00:00 | L484 RT36 C12 V84159 | post
URL=https://x.com/dexhorthy/status/2082510831858893115
TEXT: https://t.co/XeKct44ig5
LINKS: http://x.com/i/article/2082133743893204992
--
T=2082511243701883350 | @dexhorthy | 2026-07-29T16:59+00:00 | L133 RT3 C3 V24288 | post
URL=https://x.com/dexhorthy/status/2082511243701883350
TEXT: good summary of the last ~7 days of software factory debates. Thanks @itamar_mar for the shout out!
QUOTED @itamar_mar: @unclebobmartin doesn't read the code his agents write.
@dexhorthy says, for now, read the dang code.
It kicked off some great discussion and follow-ups, e.g. @GergelyOrosz, because they're both right.

Wrote a piece about it. https://t.co/ez5SuzWn7Z
--
T=2082544959820013685 | @dexhorthy | 2026-07-29T19:13+00:00 | L234 RT4 C8 V44752 | post
URL=https://x.com/dexhorthy/status/2082544959820013685
TEXT: if you have said the word agent or factory in the last six months I’m begging you to read this whole post it’s short
QUOTED @GeoffreyHuntley: [1] software factories are super real but we need to be realistic. the factory aspects haven’t been cracked yet, the [3] innovators are toying around with discovering practices and pieces. 

if someone is selling you a factory rn and they aren’t in the super small cohort (ie. they are likely startups created in last six months!) or circa <10 people in the who’s-who, who have been trying (and realistically failing) over the last two years.

they  are selling bullshit.

it isn’t cracked but it’s a
--
T=2082569016200270000 | @dexhorthy | 2026-07-29T20:48+00:00 | L0 RT0 C0 V42 | post
URL=https://x.com/dexhorthy/status/2082569016200270000
TEXT: @cyrusnewday There’s some good mech interp papers out there
--
T=2082615161819717857 | @dexhorthy | 2026-07-29T23:52+00:00 | L126 RT6 C19 V11496 | thread(3)
URL=https://x.com/dexhorthy/status/2082615161819717857
TEXT: is it possible that the idea of “loops” can be detangled into “forward pressure” (events, crons, while true loops, /goal nudges) that pushes new work / iteration, and “back pressure” (tests, verification, performance testing) that drives model inside a particular task/goal

Have we (in)conveniently complected these separable concerns? How does the conversation evolve if we deal with each separately?
[->] @yoheinakajima Ohhhhh it says “detangle into” I read it wrong I missed the “into”
[->] and before you say "oh no dex has the ai psychosis" - this was surfaced at the Loops Engineering dinner last night that @jerryjliu0 hosted - no agents necessary!
--
T=2082668177419362618 | @dexhorthy | 2026-07-30T03:22+00:00 | L74 RT2 C2 V5673 | post
URL=https://x.com/dexhorthy/status/2082668177419362618
TEXT: man design tools might be a little cooked... 

people talk a lot about html for nicer docs and explainers 

But its also really really good for riffing on product prototypes - this was like 10-20 fast rounds of back and forth to figure out what we wanna build before wiring it all into the app
--
T=2082669044780695820 | @dexhorthy | 2026-07-30T03:26+00:00 | L12 RT0 C4 V2076 | thread(2)
URL=https://x.com/dexhorthy/status/2082669044780695820
TEXT: was riffing about RLMs recently... decided there are two "most interesting" dimensions

preface - my simple definition of RLM is just N-depth subagents, and wielding context well there

but... what if you frame it as:

RLM = f(max_subagent_depth, min_subagent_depth)

where max_subagent_depth is self-explanatory

and min_subagent_depth is "how many layers do you have to go before tools other than Agent() are allowed"

so RLM(3,1) means max 3 levels and the root agent can only invoke subagents, no other tools

bu tyou could have RLM(1,0) - claude code default where the parent gets tools + one layer of subagents

or RLM(2,1) or RLM(5,2) where parent AND its subs are blocked from all tools and tool calling agents must start at layer 3

(h/t allison for the inspo)
[->] @irl_danB how did i do
--
T=2082673672813445204 | @dexhorthy | 2026-07-30T03:44+00:00 | L50 RT4 C17 V11352 | rt
URL=https://x.com/dexhorthy/status/2082673672813445204
RT-OF @jerryjliu0 (L50): Yesterday I cohosted a dinner with @dexhorthy with a wonderful group of founders, to talk about agent loops and loop engineering.

Some interesting insights:
* Most of our group was *not* actively using /loop in Codex/Claude Code
* You can build long-running autonomous agent loops through multi-agent handoffs, event triggers, or….just stacks of cron jobs (?)
* Almost everyone believes that no one will be reviewing code in 1-2 years.
* The more interesting question is whether we’d be reviewing *anything* in 1-2 years.
* AI is still a bit of a skill issue. Humans are responsible for maximizing AI output and reducing slopification.
* Will human intellect provide alpha as models get better, or will the playing field be leveled? Most people think it will be leveled a bit, but there is a need for humans to provide alignment, guardrails, judgment, creativity.
* The minimum amount of context you need for AI could be just the codebase with some documentation. Any research/plan files are for one-off tasks and not meant to be maintained. Having a self-organizing wiki is nice but adds complexity.

If you missed this one, we’ll be hosting more dinners like this on a regular cadence! If you have thoughts on what we should talk about, let us know :) (e.g. continual learning, RL envs, competitive differentiation vs. Anthropic, etc.)
RT-URL=https://x.com/jerryjliu0/status/2082673383255216356
TEXT: RT @jerryjliu0: Yesterday I cohosted a dinner with @dexhorthy with a wonderful group of founders, to talk about agent loops and loop engine…
--
