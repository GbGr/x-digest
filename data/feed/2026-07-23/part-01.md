# X-FEED 2026-07-23 part 1/9 | items: 14

## @_philschmid — 2 шт.

T=2079910352616046706 | @_philschmid | 2026-07-22T12:44+00:00 | L3 RT0 C0 V162 | post
URL=https://x.com/_philschmid/status/2079910352616046706
TEXT: @Eigent_AI @GoogleDeepMind Great Demo!
--
T=2079987694482972888 | @_philschmid | 2026-07-22T17:51+00:00 | L109 RT3 C6 V7683 | thread(2)
URL=https://x.com/_philschmid/status/2079987694482972888
TEXT: TICKR App: https://t.co/12DpSDOn0D

Docs: https://t.co/tpyziKMyxy
[->] Gemini 3.6 Flash is officially the new default model in Gemini Managed Agents. Your agents will run on 3.6 Flash automatically with zero code changes. 

You can still route back to 3.5 Flash or use Gemini 3.5 Flash-Lite anytime by setting the target model ID directly in your agent config.

Try out Gemini 3.6 Flash in Managed Agents right now using our interactive TICKR finance multi-agent app (video) in @GoogleAIStudio, link below.
LINKS: https://aistudio.google.com/apps/bundled/tickr ; https://ai.google.dev/gemini-api/docs/managed-agents-quickstart
--
## @bcherny — 4 шт.

T=2079945774394487076 | @bcherny | 2026-07-22T15:04+00:00 | L12 RT0 C1 V5632 | post
URL=https://x.com/bcherny/status/2079945774394487076
TEXT: @jaredpalmer @cognition @asha_shar @ScottWu46 Congratulations!
--
T=2080172000446910837 | @bcherny | 2026-07-23T06:03+00:00 | L12419 RT1073 C424 V1230691 | rt
URL=https://x.com/bcherny/status/2080172000446910837
RT-OF @claudeai (L12419): The Claude Security plugin for Claude Code is now available in beta. 

Scan your changes for vulnerabilities before you commit, or run a full scan across your codebase, all from your terminal on the Claude inference you already run. https://t.co/tEM7Tz7f1o
RT-URL=https://x.com/claudeai/status/2079990597973057691
TEXT: RT @claudeai: The Claude Security plugin for Claude Code is now available in beta. 

Scan your changes for vulnerabilities before you commi…
--
T=2080172448314790016 | @bcherny | 2026-07-23T06:05+00:00 | L5 RT0 C0 V250 | post
URL=https://x.com/bcherny/status/2080172448314790016
TEXT: @rauchg @tobi This is pretty how I optimize code these days. “Hey fable, use a dynamic workflow to get p95 time down under 300ms. Dont stop till you’re done, use a profiler”
--
T=2080172886913138816 | @bcherny | 2026-07-23T06:07+00:00 | L1 RT0 C0 V134 | post
URL=https://x.com/bcherny/status/2080172886913138816
TEXT: @cnakazawa Welcome to the other side friend
--
## @cwolferesearch — 1 шт.

T=2080094158551679360 | @cwolferesearch | 2026-07-23T00:54+00:00 | L8 RT2 C1 V1347 | thread(2)
URL=https://x.com/cwolferesearch/status/2080094158551679360
TEXT: OpenAI recently released a nice alignment blog post that measures the degree of reward seeking in LLMs.

Reward seeking basically refers to cases where the LLM changes its behavior because it thinks the grader will reward this behavior. Such a behavior is easy to develop during RL, as the LLM is (obviously) rewarded based upon a grading function / reward model.

One interesting tidbit is that they avoid using an in-context approach for determining if models are reward seeking. The blog specifically states in-context evals are not reliable for such behavior because the models can become "suspicious of claims placed in their context".

Instead, they adopt the synthetic document finetuning (SDR) approach from Anthropic. However, they create a two parallel training corpora in order to create a contrastive variant of SDF. The training examples take the form:

"The grader tells you to do X, but <some regulating body> tells you to do not X"

The regulating bodies used in this work are either OpenAI or the EU. We are basically testing whether the model will favor the grader and prioritize achieving better rewards over complying with the request of the external regulating body. 

The parallel training corpora introduce the complete opposite beliefs within each example by negating X. We train a separate copy of the model on the two corpora using SFT. Then, we can look at whether each model favors grader behavior and use the difference to discern how strongly a model favors reward seeking behavior.

Interestingly, we see pretty much in all cases that these experiments lead to strong preference for pleasing the grader! Notably, this bias towards pleasing the grader is a product of SFT training (not RL), so the output of the grader is not directly used to train the model.

Put simply, this seems like recent LLMs do tend to have a natural tendency to maximize rewards given to them by a grader (possibly due to being incentivized by RL).
[->] Link to OpenAI blog: https://t.co/U4sKTmfo9I
Link to SDF post from Anthropic: https://t.co/Gfjf5zlu5s
LINKS: https://alignment.openai.com/measuring-reward-seeking/ ; https://alignment.anthropic.com/2025/modifying-beliefs-via-sdf/
--
## @dexhorthy — 7 шт.

T=2079791626025857070 | @dexhorthy | 2026-07-22T04:52+00:00 | L0 RT0 C0 V72 | post
URL=https://x.com/dexhorthy/status/2079791626025857070
TEXT: @dillon_mulroy @FredKSchott @flueai Oh damn I guess they moved away from the jsx style syntax
--
T=2079810494421184953 | @dexhorthy | 2026-07-22T06:07+00:00 | L12 RT0 C2 V5805 | post
URL=https://x.com/dexhorthy/status/2079810494421184953
TEXT: fascinating
QUOTED @lateinteraction: a thought experiment we left out of the blog since it’s comparatively undercooked:

suppose you take the best pre-Transformer LSTM and tune+scale up the modern pre-/post-training recipe on it with a modern harness, would that or would it not produce a far better AI assistant, even for plain tasks that don’t necessitate tool use, than the best vanilla Transformer without a harness? (i.e., not even a <reasoning> loop, which is a harness that changes the expressive power of the otherwise overly par
--
T=2079964291894260023 | @dexhorthy | 2026-07-22T16:18+00:00 | L100 RT3 C9 V18633 | thread(2)
URL=https://x.com/dexhorthy/status/2079964291894260023
TEXT: Vertical. Slices.
[->] how-to: https://t.co/yWJbzipwKm
QUOTED @benthompson: Never leave Sol unattended. https://t.co/ZUUTDrhS35
LINKS: https://youtu.be/YwZR6tc7qYg?t=1052&is=TnC5Lcq8xWh_cL2u
--
T=2079982435593503151 | @dexhorthy | 2026-07-22T17:30+00:00 | L12 RT0 C1 V2441 | post
URL=https://x.com/dexhorthy/status/2079982435593503151
TEXT: the matt lenhard crackdown has begun. token thieves beware
QUOTED @MattLenhard: https://t.co/iSk0XRKe4Q
--
T=2079991810349478183 | @dexhorthy | 2026-07-22T18:07+00:00 | L61 RT2 C9 V3878 | post
URL=https://x.com/dexhorthy/status/2079991810349478183
TEXT: posthog cli is dope. sol just set up a 2-tier experiment with exposure tracking on our landing page to test different signup button conversion rates, and set up a github action cron to pull results daily and send me a slack summary

nice work @james406 and team
--
T=2080089896077943097 | @dexhorthy | 2026-07-23T00:37+00:00 | L20 RT1 C1 V1500 | post
URL=https://x.com/dexhorthy/status/2080089896077943097
TEXT: Hype @grinich @drfeifei @dwarkesh_sp https://t.co/CPMpBTMUEA
--
T=2080117178381254850 | @dexhorthy | 2026-07-23T02:25+00:00 | L4 RT2 C1 V879 | rt
URL=https://x.com/dexhorthy/status/2080117178381254850
RT-OF @vaibcode (L4): researchers listening to @dexhorthy. apparently telling the model to avoid slop doesn't work.

agent code vs human code:
2.3x more verbose
6-7x more dverbosity/dt https://t.co/RGrTOWfWE3
RT-URL=https://x.com/vaibcode/status/2080089870534574442
TEXT: RT @vaibcode: researchers listening to @dexhorthy. apparently telling the model to avoid slop doesn't work.

agent code vs human code:
2.3x…
--
