# X-FEED 2026-09-18 part 2/9 | items: 13

## @dexhorthy — 6 шт.

T=2100496400547041778 | @dexhorthy | 2026-09-17T08:05+00:00 | L2451 RT122 C61 V178350 | post
URL=https://x.com/dexhorthy/status/2100496400547041778
TEXT: jev is the best excuse you could possibly have to go re-read 12 factor agents. Tool calling itself can be decomposed into classify+action,

 if you learn to design ai programs as pipelines that switch breathlessly between classification, structuring data, deterministic code, AND small agent-shaped append-chat loops, then jev is a WONDERFUL building block

https://t.co/Zw0UO8Wis5
QUOTED @dillon_mulroy: i think jev is resonating with devs so well b/c it unlocks so many opportunities for composing ai into systems and products rather than ai _becoming_ the product/system

really does feel like it was a missing primitive
LINKS: https://hlyr.dev/12fa
--
T=2100537593808945244 | @dexhorthy | 2026-09-17T10:49+00:00 | L163 RT3 C47 V18221 | post
URL=https://x.com/dexhorthy/status/2100537593808945244
TEXT: Question - with everyone wanting to use /show-me as building block for other skills (eg in humanlayer we have a mash ups of grill-me and show-me everywhere)

I’ve been thinking about a simple vendoring manager for skills - what we do is we take the content of SKILL.md of a dependency skilland add it as a reference for the main skill

We do this internally - Would this be useful?

Not calling it a package manager but even a year ago I was exploring ideas for a “kustomize for markdown” to mix/match/patch other skills from the web without having to fork them and detach from upstream
QUOTED @mattpocockuk: Thinking about creating a /pr skill. You invoke it to create a PR that:

- Makes human review as fast and as simple as possible
- Takes the best parts of /show-me by @dexhorthy 
- Uses your domain language (from /grill-with-docs)
- Shows evidence that the change works (images, test output etc)
- Assesses merge risk (is it a one-way door, or a two-way door?)

IMO every model/harness I've seen creates garbage PR bodies - needs a skill here.

WDYT?
--
T=2100558413314859118 | @dexhorthy | 2026-09-17T12:12+00:00 | L1093 RT73 C36 V65195 | thread(2)
URL=https://x.com/dexhorthy/status/2100558413314859118
TEXT: cool product out of riffing w/ @mattpocockuk this week - decided to open source the pull request skill that bundles with @humanlayer_dev - /show-me bundled with some steering to cut out a lot of the slop and noise that comes with most agent prs

It's a small piece of a much larger puzzle, but rather than just share the SKILL.md contents with Matt, I figured we'd just give it to all of you 🙂 enjoy

npx skills add humanlayer/skills --skill visual-pr
[->] @mattpocockuk @humanlayer_dev if you read closely you'll see /bro in there too from @backnotprop (cc @dillon_mulroy 🙂)
--
T=2100607710538723567 | @dexhorthy | 2026-09-17T15:28+00:00 | L33 RT0 C3 V3424 | post
URL=https://x.com/dexhorthy/status/2100607710538723567
TEXT: great time hanging with the OG @lucasmeijer last night https://t.co/qUkYR8A7UQ
--
T=2100610897467105340 | @dexhorthy | 2026-09-17T15:40+00:00 | L111 RT0 C12 V7535 | post
URL=https://x.com/dexhorthy/status/2100610897467105340
TEXT: Code mode https://t.co/5qJhNi6NXJ
--
T=2100848649328623709 | @dexhorthy | 2026-09-18T07:25+00:00 | L11 RT4 C1 V1248 | post
URL=https://x.com/dexhorthy/status/2100848649328623709
TEXT: going live in 20 minutes at @AgenticAIFdn AGNTCon + MCPCon to chat about "12-factor factories" - slopcodebench, the gas town situation, and more  - stream here https://t.co/XyEzy7rccx
LINKS: https://www.youtube.com/watch?v=LbsBVem-VcE
--
## @emollick — 7 шт.

T=2100646721814737109 | @emollick | 2026-09-17T18:03+00:00 | L320 RT12 C23 V27610 | post
URL=https://x.com/emollick/status/2100646721814737109
TEXT: When I talk to nonprofit leaders about AI they often report widespread resistance from staff, usually because of environmental objections (that mix real issues &amp; fake ones). It causes them frustration because they’re all under-resourced for their mission &amp; see AI as a way to help
--
T=2100651315617800358 | @emollick | 2026-09-17T18:21+00:00 | L508 RT36 C31 V43105 | thread(2)
URL=https://x.com/emollick/status/2100651315617800358
TEXT: I had access to the new Claude Projects and was able to do some very complex work.

Here, I asked it to go through all the images, videos and records about Umberto Eco's famous 33,000 book library &amp; try to reconstruct it, including book locations, in 3D. https://t.co/jL2jyzNH0f https://t.co/j15qlmlBRR
[->] This is now open source: https://t.co/ij8T0mtPX7

The AI found all the references itself. Note the highlighted part. https://t.co/rTq859PMHg
LINKS: https://eco-library-map.netlify.app/ ; https://github.com/emollick/eco-library
--
T=2100665801800093959 | @emollick | 2026-09-17T19:18+00:00 | L479 RT34 C50 V54850 | thread(3)
URL=https://x.com/emollick/status/2100665801800093959
TEXT: What makes Claude Projects so interesting is that it handles teams of agents really well, you talk to a main orchestrator agent and it spins up specialists. Basically it creates an organization to solve your issue, mixing expensive and cheap agents depending on your preferences.

For example, I asked Fable in Claude Projects to select famous historical mysteries that it could try to resolve. It initiated research agents, selected the mysteries based on data it could access, and spun up eighteen separate threads, each with an agent each focused on one mystery. Then each thread launched additional agents (simulating avalanches, breaking codes) before summarizing those and passing them to still more agents for write up and another set of skeptical agents to fact check. It did this over a day of work, with the central orchestrator agent organizing it all. 

The results were interesting if you like historical mysteries. They are also for fun and certainly not definitive or guaranteed error-free (but they are also mostly reasonable & grounded in the literature). https://t.co/uHToT5GNuF
[->] Caveats: I take no money from the AI labs, and pay for my own accounts, but during early access there is no limit on tokens so I can’t speak to costs.

Also, I have published peer reviewed work in history but am only an interested amateur on the topics the AI selected.
[->] Here is the open source repository, including all research notes and public domain source files (with a list of copyrighted source files the AI consulted): https://t.co/HhFoBvvxYh
LINKS: https://historical-mysteries.netlify.app/ ; https://github.com/emollick/historical_fun
--
T=2100714800527327488 | @emollick | 2026-09-17T22:33+00:00 | L247 RT14 C21 V17992 | post
URL=https://x.com/emollick/status/2100714800527327488
TEXT: I overestimated the difficulty of orchestrating massive numbers of agents. I assumed research would be needed to build working organizations of agents, but they self-organize very well (and politely)

Here is a Fable coordinator in Claude Projects passing messages between agents. https://t.co/0bc5fXFAH8
--
T=2100743641190781114 | @emollick | 2026-09-18T00:28+00:00 | L399 RT24 C29 V38387 | post
URL=https://x.com/emollick/status/2100743641190781114
TEXT: I think it is worth continuing to ask if the Labs just eat every valuable AI vertical, especially as their costs of product development drop lower and lower due to AI in addition to the advantages of direct pricing on token costs and access to the underlying models themselves.
QUOTED @spicey_lemonade: Astra for Law shows a HUGE performance increase in our Legal Research Bench https://t.co/elD4N5GVvK
--
T=2100744220562673683 | @emollick | 2026-09-18T00:30+00:00 | L127 RT11 C14 V18244 | post
URL=https://x.com/emollick/status/2100744220562673683
TEXT: Epoch continues to do some of the best public benchmarking work on AI. This is helpful (and tells us how bad the state of benchmarking is, and how terrible some of our favorite benchmarks are)
QUOTED @EpochAIResearch: Introducing Benchmark Reviews: our new initiative to audit AI benchmarks. We are launching with 15 benchmarks: 4 Verified, 9 Flawed, and 2 with not enough information for a review. https://t.co/xU43tv32gH
--
T=2100767116819325141 | @emollick | 2026-09-18T02:01+00:00 | L408 RT40 C37 V25555 | thread(2)
URL=https://x.com/emollick/status/2100767116819325141
TEXT: Hey Claude, "Pick a problem or mystery that obsesses you and solve it as best you can &amp; make a movie we can share on social media about it"

So it took a crack at the Voynich Manuscript &amp; failed. Then it made this movie, which is pretty interesting to watch and a good explainer. https://t.co/CLhT0BbXcu
[->] As per usual, be careful not to be pulled in by the self-anthropomorphism, which was implied by the prompt. 

This fit into my Claude usage limit, but the entire analysis of the manuscript (including many agents) &amp; movie would have cost about $85 in tokens on Fable 5.1 otherwise
--
