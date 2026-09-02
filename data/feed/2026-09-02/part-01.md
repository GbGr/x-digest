# X-FEED 2026-09-02 part 1/8 | items: 13

## @_philschmid — 4 шт.

T=2094785934298378512 | @_philschmid | 2026-09-01T13:54+00:00 | L39 RT1 C13 V6371 | post
URL=https://x.com/_philschmid/status/2094785934298378512
TEXT: Do i need to worry? Wont click on one. But how can you spam these https://t.co/txj5Gt8ImB
--
T=2094798491113414795 | @_philschmid | 2026-09-01T14:44+00:00 | L122 RT10 C5 V41142 | post
URL=https://x.com/_philschmid/status/2094798491113414795
TEXT: https://t.co/O5Oj2tfUAp
LINKS: https://x.com/i/article/2094796958573436928
--
T=2094799789636407564 | @_philschmid | 2026-09-01T14:49+00:00 | L214 RT8 C20 V26425 | post
URL=https://x.com/_philschmid/status/2094799789636407564
TEXT: Another Bitter Lesson is coming. You might have noticed your coding agents preferring bash over dedicated tool more and more. 

They became superhuman in Bash.

Frontier models can now write complex disposable scripts in seconds. Atomic Python multi-file edits, git worktrees, and log aggregations.
QUOTED @_philschmid: https://t.co/O5Oj2tfUAp
--
T=2094840645617619036 | @_philschmid | 2026-09-01T17:31+00:00 | L237 RT12 C10 V12762 | post
URL=https://x.com/_philschmid/status/2094840645617619036
TEXT: Gemini video understanding is now agentic. Gemini can now iteratively navigate video timelines, decide watch what, pick frame rates, or chooses whether it needs speech transcripts, audio, or visual frames to answer your prompt.

Result: Long videos get up to 88% fewer tokens and 66% lower costs, with ~7% higher accuracy on benchmarks.

How it works: 
- Receives a lightweight URI reference (Files API or YouTube) and loads content via tool.
- Scans speech transcripts to pinpoint relevant moments before fetching visual frames.
- Navigates key timestamps and picks its own frame rate (0.1 or 10 FPS).
- Pulls audio tracks directly when acoustic cues matter.

Set `processing="agentic"`on `video` to enable. Keep `static` (none) for videos under 2 minutes. Available today in the Gemini API and Google AI Studio across Gemini 3.7 Flash, 3.6 Flash, and 3.5 Flash Lite. https://t.co/2eHeIduApg
LINKS: http://ai.dev/learn/agentic-video-understanding-with-gemini
--
## @addyosmani — 1 шт.

T=2094877355034747009 | @addyosmani | 2026-09-01T19:57+00:00 | L8059 RT618 C352 V824792 | rt
URL=https://x.com/addyosmani/status/2094877355034747009
RT-OF @ClaudeDevs (L8059): Fable 5.1 is now live in Claude Code and the Claude Platform.

It's priced the same as Fable 5, with 75% cheaper API cache reads. It gets a lot further into a long task before it needs your input, is better at telling you when it's stuck, and its writing style is more natural.
RT-URL=https://x.com/ClaudeDevs/status/2094851229734277228
TEXT: RT @ClaudeDevs: Fable 5.1 is now live in Claude Code and the Claude Platform.

It's priced the same as Fable 5, with 75% cheaper API cache…
--
## @bcherny — 1 шт.

T=2094864064648536068 | @bcherny | 2026-09-01T19:04+00:00 | L4589 RT184 C417 V358957 | thread(4)
URL=https://x.com/bcherny/status/2094864064648536068
TEXT: Last but not least, Fable 5.1 writes better and has better tone. We heard your feedback, and are actively working on reducing Claude-speak. Solid progress with 5.1, more to come.
[->] We have been working on how often safeguards intervene. Our latest biology safeguards intervene on benign requests 85% less often than the ones we shipped with Fable 5, and Claude Code users should see around 60% fewer cyber interventions per session. Expect more improvements soon.
[->] We have also reduced prices for Enterprise, API, and SDK customers. Cache reads on Fable 5.1 are now $0.25 per million tokens (previously: $1). Up to 38% cheaper for a typical Claude Code session.
[->] Fable 5.1 is our best model yet for coding, data analysis, computer use, design, presentations, Tag, and the hardest long-running agentic work.

This model is a pleasure to work with, and I've been using it for everything.
--
## @cwolferesearch — 1 шт.

T=2094777120601829407 | @cwolferesearch | 2026-09-01T13:19+00:00 | L155 RT15 C7 V6893 | post
URL=https://x.com/cwolferesearch/status/2094777120601829407
TEXT: Ever wondered where the policy / importance ratio in the PPO loss function comes from?

In most explainers of PPO, we first present a vanilla policy gradient (VPG) expression, then go directly to explaining PPO. Usually, PPO is expressed as a loss function that multiplies an importance ratio by the advantage, whereas the VPG takes a product of the gradient of the log probability of an action and some learning signal (e.g., return or advantage). 

With this in mind, we might wonder: How do we get from this initial VPG expression to what we use in PPO?

PPO objective = importance ratio x PG. To understand, we can just take the gradient of the (unclipped) PPO objective. When we do this, we can see that the result is nearly identical to the vanilla policy gradient expression. However, we multiply a standard policy gradient expression by the importance ratio between the current policy and the old policy.

Old policy. In PPO, the old policy refers to the policy that is used to sample the rollouts that are being used to compute the policy update in the current batch. Notably, this is different from the reference model, which is used to compute the KL penalty and is usually set equal to the policy before RL training begins. The old policy is different from the current policy because we may perform several sequential policy updates / epochs over sampled data.

Importance ratio. Due to these multiple updates, our current policy is actually slightly different from the policy that was used to sample the rollouts. To correct for this mismatch, we can use importance sampling.

Formally, importance sampling allows us to estimate an expectation under a target distribution f(x) using samples drawn from a different proposal distribution g(x). Instead of sampling directly from f(x), we can sample from g(x) and correct for the discrepancy between these distributions using the importance ratio f(x) / g(x). This is exactly what we do in PPO, where f(x) is the current policy and g(x) is the old policy.

Importance in PPO. In the case of PPO, our importance ratio is the ratio of probabilities for an action between the current and old policy. By multiplying our standard policy gradient expression from the VPG by this ratio, we can correct for the mismatch between current / old policies, allowing us to perform multiple policy updates per batch without disrupting learning.
--
## @dexhorthy — 6 шт.

T=2094673504482238975 | @dexhorthy | 2026-09-01T06:27+00:00 | L312 RT16 C9 V40710 | post
URL=https://x.com/dexhorthy/status/2094673504482238975
TEXT: holy shit they admitted it
QUOTED @GOrlanski: It would be great if there were a benchmark that measured exactly this. https://t.co/oV3n6KG3Y9
--
T=2094836283726328104 | @dexhorthy | 2026-09-01T17:14+00:00 | L17 RT1 C0 V2222 | post
URL=https://x.com/dexhorthy/status/2094836283726328104
TEXT: Code Mode for Extensible Software: 🦄 AI That Works #72 https://t.co/DtcTjzoFEj
LINKS: https://x.com/i/broadcasts/1wxWjlpWEvmJQ
--
T=2094923474426900687 | @dexhorthy | 2026-09-01T23:00+00:00 | L55 RT1 C4 V5980 | post
URL=https://x.com/dexhorthy/status/2094923474426900687
TEXT: With the /show-me skill in @humanlayer_dev, we’re making agent-authored PRs as easy to review as possible
QUOTED @notgiorgi: Agents know what acquire-use-release is, but they'll implement it the way your repo does it (hacky and wrong).

Tax you pay for not using @EffectTS_ 

pseudocode by @dexhorthy  /show-me skill btw https://t.co/XeHCEcJsIB
--
T=2094942243547144402 | @dexhorthy | 2026-09-02T00:15+00:00 | L26 RT0 C0 V3575 | post
URL=https://x.com/dexhorthy/status/2094942243547144402
TEXT: the autonomous OSS artist collective known only as “open code”
QUOTED @jlongster: what if we rendered mermaid diagrams like this https://t.co/npHcwYTg6D
--
T=2094966154582270156 | @dexhorthy | 2026-09-02T01:50+00:00 | L22 RT0 C3 V2603 | post
URL=https://x.com/dexhorthy/status/2094966154582270156
TEXT: sup fam new slopcodebench coming at u https://t.co/wTWaF0rB3t
--
T=2094971314440217064 | @dexhorthy | 2026-09-02T02:10+00:00 | L54 RT1 C5 V4417 | thread(2)
URL=https://x.com/dexhorthy/status/2094971314440217064
TEXT: live results going up here: https://t.co/uWKdNJdDKt
[->] kicking off the biggest SlopCodeBench run to date tonight - we're testing the FULL benchmark on Fable 5.1, GLM 5.3, and 5.6-Sol

follow along in thread https://t.co/UUETV0FAxh
LINKS: https://cloud.dev.codelayer.gg/shared/artifacts/01a05fd3-0591-7a7f-82e9-a00238ac258b?key=26e28ad8-8659-4016-9d0c-7c28c32eeedc
--
