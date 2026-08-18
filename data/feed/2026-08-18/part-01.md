# X-FEED 2026-08-18 part 1/9 | items: 14

## @_philschmid — 3 шт.

T=2089352023812517945 | @_philschmid | 2026-08-17T14:01+00:00 | L143 RT10 C15 V15292 | post
URL=https://x.com/_philschmid/status/2089352023812517945
TEXT: Gemini 3.7 Flash: "Play 1 round of Wordle" using my Android emulator via ADB.

The latency and visual reasoning make Gemini 3.7 Flash exceptionally good for multimodal agentic use case like mobile control and Computer Use. https://t.co/etK0yDw2tX
QUOTED @_philschmid: https://t.co/twxC73wpt0
--
T=2089351795369718238 | @_philschmid | 2026-08-17T14:01+00:00 | L56 RT9 C3 V20916 | post
URL=https://x.com/_philschmid/status/2089351795369718238
TEXT: https://t.co/twxC73wpt0
LINKS: https://x.com/i/article/2089334749718364160
--
T=2089425074323419187 | @_philschmid | 2026-08-17T18:52+00:00 | L66 RT1 C1 V5993 | post
URL=https://x.com/_philschmid/status/2089425074323419187
TEXT: Gemini 🤝 Multimodalities.
QUOTED @OfficialLoganK: @unixpickle Gemini got it in ~8 seconds https://t.co/WPCddVoqKN
--
## @bcherny — 2 шт.

T=2089537919795212565 | @bcherny | 2026-08-18T02:20+00:00 | L383 RT12 C47 V55897 | post
URL=https://x.com/bcherny/status/2089537919795212565
TEXT: Let us know what you think!
QUOTED @ClaudeDevs: Claude Code can design now. The new /design skill (research preview) brings Claude Design's artboard workflow into the CLI and Desktop, built on artifacts.

Run /design to get editable artboards for your UI — pick one, tweak it, then have Claude implement it. https://t.co/uttl4F1G0e
--
T=2089538781909332210 | @bcherny | 2026-08-18T02:24+00:00 | L326 RT10 C38 V36790 | post
URL=https://x.com/bcherny/status/2089538781909332210
TEXT: Small quality of life improvements like this add up. More on the way
QUOTED @ClaudeDevs: Perf win of the day: Claude Code CLI now uses 2x less CPU at p99.

Bun's garbage collector was running on a fixed timer, so it would kick in mid-turn and steal CPU right when Claude Code was busiest. Now it waits until the process is idle. https://t.co/icGc35LDQs
--
## @chipro — 1 шт.

T=2089476363678028283 | @chipro | 2026-08-17T22:16+00:00 | L75 RT3 C21 V12166 | post
URL=https://x.com/chipro/status/2089476363678028283
TEXT: what's a good model tiering system? i'm sick of telling my agent orchestrator things like: "for Claude, use model X, for OpenAI, use model Y, etc."

i want to be able to tell my orchestrator: "use models tier ..." for this kind of task
--
## @cwolferesearch — 1 шт.

T=2089419256354033911 | @cwolferesearch | 2026-08-17T18:29+00:00 | L18 RT1 C2 V2050 | post
URL=https://x.com/cwolferesearch/status/2089419256354033911
TEXT: I’m a big fan of smaller MoE models, and NVIDIA’s Nemotron 3.5 lightning is a great release in this space…

NVIDIA is expanding the suite / offering of Nemotron models to be quite comprehensive. Now, Nemotron includes a smaller MoE model (30B parameters, 3B active), which provides better support for use cases that require high throughput / low latency.

AI research is moving away from using frontier models for everything. For long-running agentic tasks, it doesn’t make sense to use a frontier-level reasoning model for every step of the task. Instead, we should use a powerful model for planning / orchestration and delegate sub-tasks to faster / efficient agents that can better handle execution.

Nemotron 3.5 lightning focuses on this area, providing a model optimized for the high-volume execution layer of agentic tasks; e.g., validating tool outputs, executing commands, solving simpler sub-tasks, etc. The model is also specifically trained for agentic use cases and compatibility with popular agent frameworks / harnesses (e.g., hermes / openclaw).

“Frontier reasoning models such as Nemotron 3 Ultra handle orchestration and complex planning while smaller, more efficient models handle the high-volume execution layer.” - Nemotron 3.5 Lightning blog

To support even better inference efficiency, Nemotron 3.5 lightning is also trained with multi-token prediction to enable speculative decoding. The release also includes drafters for DSpark / DFlash (and quantized checkpoints) to enable further inference optimizations.

Nemotron 3.5 Lightning achieves impressive results on the accuracy-speed frontier. It has 4x inference speed of similar-size models. On the artificial analysis intelligence index, we can see that Nemotron 3.5 Lightning achieves impressive performance for the speed category it is in (kind of a region of its own).

Inference-optimized small MoE models are so useful for practical tasks. There are tons of use cases that can be solved by post-training a small, fast model to reach very high levels of reliability at low costs. Plus, NVIDIA provides several finetuning recipes that can be used with 3.5 lightning out of the box.
--
## @dexhorthy — 7 шт.

T=2089345968814915929 | @dexhorthy | 2026-08-17T13:37+00:00 | L31 RT10 C3 V6567 | rt
URL=https://x.com/dexhorthy/status/2089345968814915929
RT-OF @Pragmatic_Eng (L31): What is intentional compaction? @DexHorthy, founder of HumanLayer, explains:

“When context is noisy, you deliberately compress the useful parts into a clear markdown artifact, verify it, and then start a fresh conversation.

Frequent intentional compaction is the building block for building software with AI. How do we get the most out of today’s models, how do we control what we’re putting into the context window so we get the best results, which means doing as much work as possible in the smart zone, the first hundred thousand tokens.

1. The research step: we go read a bunch of code and turn it into a doc: that’s our compaction. We take that forward.

2. In the next session we read the ticket and the intent and turn that into a design document: here’s the high-level current state, desired end state, and a bunch of design questions.

3. Then you take the research and the design and you do a new session, new context: you’ve compressed the intent, and you’ve compressed the state of the codebase, so you can then do your planning.”
RT-URL=https://x.com/Pragmatic_Eng/status/2089344195265777695
TEXT: RT @Pragmatic_Eng: What is intentional compaction? @DexHorthy, founder of HumanLayer, explains:

“When context is noisy, you deliberately c…
--
T=2089429752092512601 | @dexhorthy | 2026-08-17T19:10+00:00 | L7 RT2 C0 V1594 | rt
URL=https://x.com/dexhorthy/status/2089429752092512601
RT-OF @heavybit (L7): On episode 12 of High Leverage, Dexter Horthy (@dexhorthy) of HumanLayer (@humanlayer_dev) explains why AI can generate code faster than ever but still requires careful specifications, architectural judgment, and human review to produce software that remains maintainable. Tune in!

https://t.co/oplzcGf74G
RT-URL=https://x.com/heavybit/status/2089429614221246716
TEXT: RT @heavybit: On episode 12 of High Leverage, Dexter Horthy (@dexhorthy) of HumanLayer (@humanlayer_dev) explains why AI can generate code…
LINKS: https://hubs.ly/Q04rBkR90
--
T=2089441382628839639 | @dexhorthy | 2026-08-17T19:57+00:00 | L120 RT0 C18 V15156 | post
URL=https://x.com/dexhorthy/status/2089441382628839639
TEXT: we've been working hard on the best way to collaborate across agent sessions - across any combination of dev workstations, mac minis, or cloud environments. 

Send prompts to your teammates sessions

teleport worktree bundles + task context across workstations

manage sessions and collab on artifacts from your phone

what else should we add?
--
T=2089443460243939623 | @dexhorthy | 2026-08-17T20:05+00:00 | L37 RT0 C2 V18389 | post
URL=https://x.com/dexhorthy/status/2089443460243939623
TEXT: this guy gets it
QUOTED @reillyjodonnell: the thing that displaces github wont:

have a login with github button
have prs
wont have async ci / an actions like primitive

it will meet teams where they already work
produce an unbelievable amt of confidence in a unit of work
generally be so unlike github 

its the end of an era but believe better things are yet to come
--
T=2089473173985366525 | @dexhorthy | 2026-08-17T22:03+00:00 | L17140 RT2197 C86 V361655 | rt
URL=https://x.com/dexhorthy/status/2089473173985366525
RT-OF @seclilc (L17140): AI;DR

(AI; didn’t read)
RT-URL=https://x.com/seclilc/status/2088660446270128324
TEXT: RT @seclilc: AI;DR

(AI; didn’t read)
--
T=2089486711902626276 | @dexhorthy | 2026-08-17T22:57+00:00 | L50 RT3 C2 V6799 | post
URL=https://x.com/dexhorthy/status/2089486711902626276
TEXT: customers are learning that /bro also works on the CTO https://t.co/vzXsAxxAUP
--
T=2089527653418295632 | @dexhorthy | 2026-08-18T01:39+00:00 | L9 RT0 C1 V1182 | post
URL=https://x.com/dexhorthy/status/2089527653418295632
TEXT: sloptimistic updates is this anything
--
