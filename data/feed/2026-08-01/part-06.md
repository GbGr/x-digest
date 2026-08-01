# X-FEED 2026-08-01 part 6/7 | items: 11

## @omarsar0 — 7 шт.

T=2083210384236855600 | @omarsar0 | 2026-07-31T15:17+00:00 | L58 RT9 C14 V7968 | thread(2)
URL=https://x.com/omarsar0/status/2083210384236855600
TEXT: Opus 5 - Build a photorealistic ThreeJS app that zooms continuously through nine powers of ten, from a leaf on a branch down to the single magnesium atom at the centre of a chlorophyll molecule. https://t.co/KzDokUQf03
[->] Nothing too crazy, but this got me wondering how much more I can improve this if I tried.
--
T=2083215323482750998 | @omarsar0 | 2026-07-31T15:36+00:00 | L41 RT4 C5 V6774 | post
URL=https://x.com/omarsar0/status/2083215323482750998
TEXT: "Intelligence too cheap to meter" battle is on!

Given that DeepSeek-V4-Flash-Preview is already great for agentic tasks, there is no doubt this new checkpoint must be an absolute beast.

20+ point jump on TerminalBench-2.1!

1M tokens - in ($0.14) | out ($0.28). Insane price!
QUOTED @deepseek_ai: 🚀 DeepSeek-V4-Flash Official API is now LIVE in public beta!

🔷 We’ve massively upgraded its Agent capabilities—benchmark scores are now far surpassing the V4-Pro-Preview. Check out the massive performance leap below! 👇
🔷 The official V4-Flash now natively supports the Responses API format and is fully adapted for Codex!

Check out the configuration details in our official API docs: https://t.co/smCwQZMeiq
--
T=2083232479641821418 | @omarsar0 | 2026-07-31T16:45+00:00 | L63 RT9 C11 V6421 | post
URL=https://x.com/omarsar0/status/2083232479641821418
TEXT: New research from Microsoft.

This one is on training computer-use agents at scale.

Recent pipelines generate synthetic environments in bulk, which moved the bottleneck from how many exist to what is inside each one. Echoverse compiles specifications into stateful applications whose tasks are graded against the application's own database, then runs a co-evolution loop that reads every graded rollout twice. Once as repairs to the environment, its tasks and its verifier. Once as training signal for the model.

On the same domains, shallow environments pushed live-site accuracy below the base model, from 80.0 down to 75.0. Deep ones raised it, 80.0 to 85.0 and 48.0 to 65.0.

Repairing a single environment lifted the model trained on it from 16.2% to 38.5%. Across twelve environments, a 9B model went from 36.5% to 67.1% on fourteen evaluation splits, within fourteen points of the much larger frontier model that taught it.

They release four environments as a benchmark with applications, seed data and grounded graders.

Paper: https://t.co/thTetOjep1

Track trending AI papers in our academy: https://t.co/1e8RZKs4uX
LINKS: https://arxiv.org/abs/2607.28074 ; https://academy.dair.ai/
--
T=2083235209642663964 | @omarsar0 | 2026-07-31T16:55+00:00 | L59 RT5 C4 V10262 | post
URL=https://x.com/omarsar0/status/2083235209642663964
TEXT: Great release for recursive self-improving in ML Engineering.
QUOTED @dair_ai: Very interesting paper on recursive self-improvement.

The whole stack is released.

Machine learning engineering gives recursive self-improvement a concrete, executable testbed. OpenMLE is an open full-stack system for that research, spanning verifiable task environments with execution feedback, operator learning, and long-horizon search.

On top of it the team post-trains Frontis-MA1, a 35B meta-evolution agent aligned around four atomic program-evolution operators. Draft, Improve, Debug, Cros
--
T=2083292876587577549 | @omarsar0 | 2026-07-31T20:45+00:00 | L51 RT15 C13 V5630 | post
URL=https://x.com/omarsar0/status/2083292876587577549
TEXT: Neat work on long-horizon agents.

Splitting a hard task across agents is typically how standard multi-agent work. The usual design lets them exchange findings only at phase boundaries, through staged handoffs or synchronized rounds, so communication and work stay mutually exclusive.

AgentRadio breaks that constraint with an asynchronous message-passing layer. Three primitives, threads, messages, and waiting for mentions. The last one runs as a background task, surfacing a teammate's discovery without interrupting foreground work.

On SWE-Atlas QnA, a single Claude Code agent on Opus 4.6 resolves 32.3% of tasks. Four agents wired through AgentRadio resolve 62.1%. That also beats a single Claude Code agent running the newer Opus 4.8 at 57.2%.

Rubric-level analysis shows the gain growing with task difficulty, which points at mid-course correction as the mechanism rather than raw parallelism.

Paper: https://t.co/LQ0It2dnZ2

Track more trending AI papers in our academy: https://t.co/1e8RZKs4uX
LINKS: https://arxiv.org/abs/2607.28430 ; https://academy.dair.ai/
--
T=2083302486819934437 | @omarsar0 | 2026-07-31T21:23+00:00 | L50 RT2 C11 V10231 | post
URL=https://x.com/omarsar0/status/2083302486819934437
TEXT: Nice open-source tool. Lots of agent work is now happening with an agent team in channels/groups. This works with Pi, OpenCode, Claude Code, and Codex.
QUOTED @ycombinator: We’ve decided to open-source a multi-agent harness we use internally at YC.

We call it “QM” and it’s meant to be easy to customize, like Hermes or OpenClaw, but useful for a whole company. We use it across accounting, legal, events, and engineering (including building QM itself!).

The whole project is under an MIT license. It is cloud-first and has Slack and web UI natively.
--
T=2083309230161826003 | @omarsar0 | 2026-07-31T21:50+00:00 | L40 RT4 C12 V9239 | post
URL=https://x.com/omarsar0/status/2083309230161826003
TEXT: People haven't been paying enough attention.

No point in staying loyal to one harness anymore.

Btw, this token efficiency trend started with models like Qwen-3.7, Nemotron, and DeepSeek-V4 preview.

I've been testing, and I can confirm that lightweight harnesses like Pi and Hermes work better with frontier open models like Kimi K3.
QUOTED @composio: We ran Kimi K3 through 3 more agent harnesses (Pi Agent, OpenCode, and Codex) bringing the comparison to 6 harnesses across 26 agentic tasks.

2 things stood out: Codex ranked last on success despite mid-pack speed and cost, while Claude Code cost about 4x more than Hermes. 🧵🧵 https://t.co/8YLOE1C0yZ
--
## @simonw — 4 шт.

T=2083310593164095944 | @simonw | 2026-07-31T21:55+00:00 | L71 RT9 C14 V10352 | thread(4)
URL=https://x.com/simonw/status/2083310593164095944
TEXT: More on my own blog as well: https://t.co/C94uYasHTF
[->] I've been working with Prime Radiant building a new tool for running small eval suites against models, harnesses, and prompts - it's called "smevals", you can try it with "uvx smevals docs", and I wrote about it here: https://t.co/zj3sFgSN03
[->] Here's an example of the kind of report it can produce having run and graded an evaluation suite against different models https://t.co/imSAxnDxtT
[->] On of the hardest parts of the project was figuring out the vocabulary! Here's what I settled on https://t.co/mKDC8Br2B8
LINKS: https://simonwillison.net/2026/Jul/31/smevals/ ; https://primeradiant.com/blog/2026/smevals.html ; https://static.simonwillison.net/static/2026/smevals-haiku-build/#/haiku
--
T=2083314572988236154 | @simonw | 2026-07-31T22:11+00:00 | L28 RT3 C6 V7513 | post
URL=https://x.com/simonw/status/2083314572988236154
TEXT: I'm on Oxide and Friends podcast this week!

We talked about accidental cyberattacks, Kimi K3, Golden Gate Claude, the Zizians, Alameda wild turkey attacks, Soviet Marburg virus research, the Lead-crime hypothesis, and a bunch of other worthy digressions https://t.co/1IewPkP1KB
LINKS: https://oxide-and-friends.transistor.fm/episodes/the-open-weight-revolution-with-simon-willison
--
T=2083330693313220615 | @simonw | 2026-07-31T23:15+00:00 | L214 RT14 C22 V16552 | post
URL=https://x.com/simonw/status/2083330693313220615
TEXT: The new stateless MCP specification has rekindled my interest in MCP, and inspired some new projects, including mcp-explorer and datasette-mcp https://t.co/fn6fd1hZv7
LINKS: https://simonwillison.net/2026/Jul/31/stateless-mcp/
--
T=2083342783071621224 | @simonw | 2026-08-01T00:03+00:00 | L257 RT9 C39 V22491 | thread(2)
URL=https://x.com/simonw/status/2083342783071621224
TEXT: Got a disappointing pelican from DeepSeek-V4-Flash-0731 at default reasoning mode - on the left - but then I bumped reasoning up to high (via OpenRouter) and got the much better one on the right https://t.co/iBEov5peB6
[->] More notes on my blog - this model looks VERY good for its price, here's the Artificial Analysis pareto line for it https://t.co/C3ia9eeiwx https://t.co/cN2rO9OK5H
LINKS: https://simonwillison.net/2026/Jul/31/deepseek-v4-flash-0731/
--
