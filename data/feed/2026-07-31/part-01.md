# X-FEED 2026-07-31 part 1/12 | items: 12

## @_philschmid — 2 шт.

T=2082844768598393248 | @_philschmid | 2026-07-30T15:04+00:00 | L53 RT5 C4 V4309 | thread(2)
URL=https://x.com/_philschmid/status/2082844768598393248
TEXT: Blog: https://t.co/9PWL5EvDgb

Live API quickstart: https://t.co/tJmPWhrs73

AI Studio: https://t.co/XyHudqxKr7 https://t.co/rjadTFy7je
[->] Bipup beep... 🤖 Say hello to Gemini Robotics ER 2! ER 2 not only outperforms competing frontier models on embodied reasoning, it thinks and plans next steps simultaneously while executing current actions

- Live API support for bidirectional, sub-second robot streaming.
- 91.3% moment-finding accuracy at 4x faster execution speed.
- 57.4% accuracy tracking 5-stage task progress on video feeds.
- Allows multi-robot orchestration handoffs between different machines.
- Built on Gemini 3.5 Flash (`gemini-robotics-er-2-preview` and`gemini-robotics-er-2-streaming-preview)`

Watching Boston Dynamics Spot complete tasks without awkward freezes feels like a bit step. Excited for the future! 

[Video: Boston Dynamics Spot + Gemini Live API]
LINKS: https://blog.google/innovation-and-ai/models-and-research/google-deepmind/gemini-robotics-er-2/ ; https://github.com/google-gemini/robotics-samples/tree/main/live-api ; https://aistudio.google.com/prompts/new_chat?model=gemini-robotics-er-2-preview
--
T=2082855911865938393 | @_philschmid | 2026-07-30T15:48+00:00 | L451 RT22 C11 V49607 | post
URL=https://x.com/_philschmid/status/2082855911865938393
TEXT: 1) What https://t.co/4FCoITegMC
--
## @addyosmani — 2 шт.

T=2082721045807779858 | @addyosmani | 2026-07-30T06:52+00:00 | L210 RT17 C24 V485504 | post
URL=https://x.com/addyosmani/status/2082721045807779858
TEXT: Code quality, taste and judgement matter. @SonarSource is great for catching bug and security issues on every commit. Here's why I like using it. 

Learn more: https://t.co/v2vKFgrFCQ https://t.co/2gDDOGUBK3
LINKS: https://fandf.co/4x9KWCL
--
T=2082723002836545641 | @addyosmani | 2026-07-30T07:00+00:00 | L1031 RT123 C78 V428990 | post
URL=https://x.com/addyosmani/status/2082723002836545641
TEXT: Software quality now depends on the constraints you set around your agents.

When humans manually wrote most of the code we could look at the code itself for signs of quality. Is it clean? Is it thoughtful? Is it fast? Can another engineer understand it? Does it have tests?

Agents can now generate more code than people can read. When code generation scales beyond review, quality - checks for one or more of correctness, maintainability, security, performance etc - increasingly has to live somewhere else.

It moves into the harness, environment and operating system around the agent.

This can be the tests and deterministic checks that decide what the system is allowed to do (amongst others). Your constraints are what may eventually enable loops of agents to deliver production software reliably. They can include unit tests, property tests, acceptance tests, mutation testing and quality metrics. 

This back-pressure lets the system resist bad work before it becomes somebody elses problem. 

Set your constraints. They decide whether the code your agents generate is good enough to ship.
--
## @cwolferesearch — 2 шт.

T=2082923683748725099 | @cwolferesearch | 2026-07-30T20:17+00:00 | L25 RT0 C2 V1555 | thread(2)
URL=https://x.com/cwolferesearch/status/2082923683748725099
TEXT: link to the paper: https://t.co/RRKpKj3TkU
[->] RSIBench-Data is a neat benchmark. It focuses on the data aspect of RSI by fixing the training setup (based on Tinker) and having a coding agent iteratively refine the training data used for an separate specialized LLM.

The data refinement process is pretty simple:

1. Refine the training data.
2. Run training.
3. Evaluate (on dev set) + get feedback.
4. Repeat.

Eventually, the refinement process stops (due to fixed time or $ budgets), and we run the final model on a test set (separate from the evals that are visible to the agent) to determine performance. 

At each step the agent basically submits a training manifest along with a training configuration for Tinker. Then, the model is executed on a set of dev benchmarks and gets benchmark scores / feedback that can be used to refine its data selection.

For example, the agent can look at token usage, verifier outcomes, per-task trajectories, errors, time elapsed, and more. This info is then used by the agent to refine training data in a variety of ways:

- Source new data. 
- Filter / validate data.
- Mix data.
- Create curriculums (e.g., based on difficulty). 

Models don't perform great on this benchmark yet. It's common for even top models to make decent gains early but struggle to find monotonic improvements (or even degrade performance) over time. This makes me feel like the current setup is mostly brute forcing data mixtures to see if the agent can find simple wins. Also seems like preventing decontamination on a bench like this will be very tough; e.g., the agent could learn to search for arxiv papers that propose good mixing strategies for public benchmarks.  

However, I think given a proper harness frontier models could be so helpful on data-centric research. For example, we can give the agent access to clustering / search techniques, inspection tools, etc. We could also allow the agent to invoke pools of external LLMs on our data to sample various LLM judge scores, compute difficulty metrics, or even use IRT. This is a very long horizon task with complex tools!

Super excited to track all of the techniques / agents that emerge to help with these style of tasks!
LINKS: https://arxiv.org/abs/2607.25886v1
--
T=2082992315950338099 | @cwolferesearch | 2026-07-31T00:50+00:00 | L5 RT0 C2 V1526 | post
URL=https://x.com/cwolferesearch/status/2082992315950338099
TEXT: So many rumors going around about Situational Awareness today, but I think Leo just wanted to buy the Jersey Mike's IPO.
--
## @dexhorthy — 6 шт.

T=2082845002745753912 | @dexhorthy | 2026-07-30T15:05+00:00 | L85 RT4 C12 V5988 | post
URL=https://x.com/dexhorthy/status/2082845002745753912
TEXT: i swear to god I am gonna vibecode a screen capture tool that detects claude slop on my display and blurs it out in real time so I never have to see this shit https://t.co/0XEjLaq7cu
--
T=2082869941326492096 | @dexhorthy | 2026-07-30T16:44+00:00 | L2 RT0 C0 V60 | post
URL=https://x.com/dexhorthy/status/2082869941326492096
TEXT: @braelyn_ai @shcallaway https://t.co/Vjd4kWEDfB
QUOTED @dexhorthy: every PR over 200 lines that @humanlayer_dev makes gets a diff tree attached to the PR, ordered logically by changes instead of just alphanumeric https://t.co/82wWXL6hDJ
LINKS: https://x.com/dexhorthy/status/2082230467445830104?s=46
--
T=2082891066815189056 | @dexhorthy | 2026-07-30T18:08+00:00 | L61 RT3 C4 V3903 | post
URL=https://x.com/dexhorthy/status/2082891066815189056
TEXT: POV claude just finished writing a plan to build a big feature in your monorepo https://t.co/lF4E2yXPOd
--
T=2082895696181817767 | @dexhorthy | 2026-07-30T18:26+00:00 | L472 RT30 C30 V29786 | post
URL=https://x.com/dexhorthy/status/2082895696181817767
TEXT: agree - a good software emerges through iteration, stacking small, well-tested automations/loops and triggers over time. If you set out to "build a factory" you are gonna struggle. 

The only "factory" wisdom you should be following is: Figure out your bottleneck, automate it, then find the next bottleneck. Thanks Eli Goldratt
QUOTED @MichaelArnaldi: Very hot take: you should not be building a software factory
--
T=2082910803196600371 | @dexhorthy | 2026-07-30T19:26+00:00 | L16 RT4 C1 V2749 | rt
URL=https://x.com/dexhorthy/status/2082910803196600371
RT-OF @MilksandMatcha (L16): “The codebase is part of the prompt.” 

@dexhorthy on why coding loops amplify existing patterns, and why better verifiers, human review, and deliberate codebase gardening matter more as generation gets faster.

Join us in the Token Billionaires Lounge, presented by @cerebras  and @aiDotEngineer.
RT-URL=https://x.com/MilksandMatcha/status/2082905063287353502
TEXT: RT @MilksandMatcha: “The codebase is part of the prompt.” 

@dexhorthy on why coding loops amplify existing patterns, and why better verifi…
--
T=2082998583901692001 | @dexhorthy | 2026-07-31T01:15+00:00 | L17 RT1 C3 V2629 | thread(3)
URL=https://x.com/dexhorthy/status/2082998583901692001
TEXT: *kool-aid guy voice* https://t.co/S4E7TtFV8e
[->] aaaaand they're off! benchmarking the new frontier, part two - slopCodeBench for Kimi K3, 5.6-Sol, and Fable 5

live results here https://t.co/hcMsfDBLql https://t.co/7ScKDRvP1M
[->] WHATS THIS

A NEW CHALLENGER HAS ENTERED THE ARENA https://t.co/HU1wwp1G7Y
LINKS: https://cloud.dev.codelayer.gg/shared/artifacts/019fb5bd-59b0-707d-806e-0449590a7fd0?key=b5cfbefc-bd79-4b9e-ae23-5b8b9d32d6e8
--
