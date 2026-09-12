# X-FEED 2026-09-12 part 2/9 | items: 11

## @cwolferesearch — 1 шт.

T=2098436385506005407 | @cwolferesearch | 2026-09-11T15:39+00:00 | L161 RT18 C5 V6829 | thread(2)
URL=https://x.com/cwolferesearch/status/2098436385506005407
TEXT: for more details, read my full post on RL for LLMs: https://t.co/BZ1FsxzHZi
[->] Importance sampling is a concept that appears constantly in RL research (e.g., PPO objective, training / inference mismatch, and more). Here’s how it works…

In RL, the policy used to generate rollouts does not always perfectly match the current policy we are optimizing. For example, algorithms like PPO may perform multiple policy updates over the same rollouts, while recent asynchronous RL infrastructure may lead to the incorporation of mildly stale or off-policy data into the training process.

Importance sampling is a general technique in probability theory that can help to correct mismatches of this kind. Formally, importance sampling allows us to estimate an expectation under a target distribution f(x) using samples drawn from a different proposal distribution g(x).

Instead of sampling directly from f(x), we can sample from g(x) and correct for the discrepancy between these distributions using the importance ratio f(x) / g(x). Intuitively, samples that are more likely under f(x) than g(x) receive a larger importance ratio, while samples that are less likely receive a smaller ratio.

Importance ratios appear constantly in research on RL for LLMs. For example, PPO uses an importance ratio to compare the probability of a sampled token under the current policy and the policy that sampled the rollout—this ratio is a core component of the PPO loss function.

Additionally, if rollouts are generated using a policy that is different than the policy being optimized—or a separate inference engine that produces slightly different token distributions—we can use importance ratios to account for this mismatch.

In practice, the importance ratio can become large when the distributions differ substantially, yielding unstable and high-variance estimates. For this reason, RL algorithms may choose to clip or truncate the importance ratio, which introduces bias in order to reduce variance and improve stability. For example, both PPO and truncated importance sampling (TIS) adopt a clipped version of the importance ratio.
LINKS: https://cameronrwolfe.substack.com/p/llm-rl
--
## @dexhorthy — 6 шт.

T=2098419423417958747 | @dexhorthy | 2026-09-11T14:32+00:00 | L56 RT3 C11 V10132 | post
URL=https://x.com/dexhorthy/status/2098419423417958747
TEXT: refreshing article actually, i laughed at the image title but okay sure ship it
QUOTED @AgenticAIFdn: @dexhorthy has fresh evidence that unattended coding agents still turn healthy codebases into radioactive spaghetti.

At @humanlayer_dev, a lightly supervised software factory metastasized into 30,000 to 40,000 lines with an "insanely complicated state machine" running four Unix processes. They archived the whole thing.

His new SlopCodeBench data shows every model accumulated defects as challenges piled up. That is the pattern.

He is presenting "There Is No Software Factory Without Better Veri
--
T=2098488167158722655 | @dexhorthy | 2026-09-11T19:05+00:00 | L76 RT5 C9 V8179 | thread(2)
URL=https://x.com/dexhorthy/status/2098488167158722655
TEXT: we're back with more software factory alpha on the 🦄 AI That Works show - @vaibcode and I teamed up with 

- @tbrownio - discussed how they run a discuss/do/compound loop in their factory, with @linear as the frontend and all agent sessions running on mac minis
- @colemurray sharing tales from the trenches rolling out the OSS OpenInspect factory to teams of up to 500 engineers in the enterprises

super fun time - catch us every week at 10:15am PT on X and on https://t.co/wqJaaD1QPx
[->] youtube going live in 30 minutes - https://t.co/xerXicSm7p
LINKS: http://lu.ma/baml ; https://youtu.be/HGizPRQfpdw
--
T=2098512846762230073 | @dexhorthy | 2026-09-11T20:43+00:00 | L45 RT0 C8 V4026 | post
URL=https://x.com/dexhorthy/status/2098512846762230073
TEXT: still no @abhiaiyer https://t.co/snmdAQE0nR
--
T=2098542816595194354 | @dexhorthy | 2026-09-11T22:42+00:00 | L377 RT28 C10 V44073 | post
URL=https://x.com/dexhorthy/status/2098542816595194354
TEXT: humanlayer/skills popping off. 

/show-me up to 16k installs

enjoy https://t.co/D2OmGoNN8L https://t.co/Af3VJ9hPqs
QUOTED @dexhorthy: https://t.co/L0G15QT1Tv
LINKS: https://x.com/dexhorthy/status/2087569590268391897
--
T=2098635373861867743 | @dexhorthy | 2026-09-12T04:50+00:00 | L26 RT1 C6 V4454 | post
URL=https://x.com/dexhorthy/status/2098635373861867743
TEXT: same over here - astra for specific things but it didn’t get much better at coding if at all and generally more spazzy
QUOTED @thdxr: a portion of our team has gone back to Sol

astra is good and can do some novel things but it has some downsides

and so far our effective spend looks doubled so tough to justify
--
T=2098675233398079563 | @dexhorthy | 2026-09-12T07:29+00:00 | L0 RT0 C0 V703 | post
URL=https://x.com/dexhorthy/status/2098675233398079563
TEXT: what so just every time we get hacked now we just blame rogue oai agents lol
QUOTED @zeeg: 🤠 https://t.co/nVFPg3C1DL
--
## @emollick — 3 шт.

T=2098428962468700197 | @emollick | 2026-09-11T15:10+00:00 | L1459 RT58 C52 V67820 | thread(2)
URL=https://x.com/emollick/status/2098428962468700197
TEXT: No matter how much you are hearing about AI, today is the least you will ever hear about AI.
[->] Based on the bot replies, this is also the least you will hear from AI
QUOTED @tszzl: if you think AI chatter has reached an annoying level right now you're in for something else. it's going to be the only thing on anybody's mind starting shortly
--
T=2098464926507401338 | @emollick | 2026-09-11T17:33+00:00 | L269 RT37 C30 V32783 | thread(3)
URL=https://x.com/emollick/status/2098464926507401338
TEXT: Here's a automated forecasting system to estimate catastrophic risk from some major experts on forecasting.

The models predicts the chance of an AI-generated mass catastrophe as 0.47% by 2030 (with a 1.1% chance of a catastrophe by 2030 with any cause). https://t.co/zp3ovPVM1O https://t.co/fHEyw9m9oG
[->] Thread on the paper and dashboard: https://t.co/kNw5ReuYnI
[->] This assumes no policy interventions (there are lots of other assumptions they test in the paper and the site)
LINKS: https://airo.forecastingresearch.org/ ; https://x.com/Jabaluck/status/2098441741753786490?s=20
--
T=2098534460996075568 | @emollick | 2026-09-11T22:09+00:00 | L548 RT19 C89 V38618 | post
URL=https://x.com/emollick/status/2098534460996075568
TEXT: Now that METR long horizons is effectively saturated (Epoch found pre-Fable agents could do 18 weeks of human work), what is the best quantitative graph that shows the current exponential progress curve? 

Frontier Math is saturated, ARC-AGI is saturated, Millennium Prize is...
--
## @eugeneyan — 1 шт.

T=2098514686736240773 | @eugeneyan | 2026-09-11T20:51+00:00 | L46255 RT10516 C2643 V37768617 | rt
URL=https://x.com/eugeneyan/status/2098514686736240773
RT-OF @AnthropicAI (L46255): We're publishing our most detailed threat intelligence report to date. 

It covers how people tried to misuse Claude—for cyberattacks, influence operations, surveillance, biology, and building weapons—and how we found and stopped them.

We disrupted every operation in the report, and used the lessons from them to strengthen our safeguards. Where appropriate, we also shared what we found with authorities and other AI companies.

These cases are not typical: we’re highlighting some of the most sophisticated misuse we’ve seen. But they’re especially important to discuss, because they show us where AI misuse is headed, where our safeguards work, and where they need to improve.

We’re publishing this report so others can spot the same activity on their own platforms, and so we can give the public a clearer view of how emerging threats develop.

Read the report: https://t.co/0EJUnYEgfz
RT-URL=https://x.com/AnthropicAI/status/2098097512544444447
TEXT: RT @AnthropicAI: We're publishing our most detailed threat intelligence report to date. 

It covers how people tried to misuse Claude—for c…
LINKS: https://www.anthropic.com/threat-intelligence-report-september-2026
--
