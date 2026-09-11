# X-FEED 2026-09-11 part 6/9 | items: 7

## @omarsar0 — 12 шт.

T=2097958286146605446 | @omarsar0 | 2026-09-10T08:00+00:00 | L114 RT23 C23 V10382 | post
URL=https://x.com/omarsar0/status/2097958286146605446
TEXT: Nice paper from Salesforce on co-evolving harnesses and models.

Harness engineering is a hot topic right now. So this is a great read.

(bookmark it)

Salesforce evolved a harness with a weak model across seven enterprise agent tasks, then trained that model on a stronger expert's full trajectories under the same harness.

Performance dropped on all seven tasks, by 4 to 30 points across Qwen3-Coder and Gemma 4.

The same fine-tuning helps under the unevolved harness. So the harness is what changes the outcome.

Their analysis points at model-harness fit.

Imitation transfers knowledge and increases scaffold usage, but the weaker model adopts the expert's planning strategy without the competence to execute it, and it no longer matches a harness that was evolved around its own native planning style.

The fix is to stop copying whole trajectories.

A meta-level agent finds the failing turn in the weaker model's own rollout and asks the expert to rewrite only that turn. That keeps the model's planning style intact and combines the gains from harness evolution and weight updates.

Paper: https://t.co/gG3J6MnvT0
LINKS: https://academy.dair.ai/papers/co-evolving-harnesses-and-models-on-policy-correction-helps-weaker-models-catch-2609.09134
--
T=2098060818763878673 | @omarsar0 | 2026-09-10T14:47+00:00 | L1011 RT108 C100 V510458 | rt
URL=https://x.com/omarsar0/status/2098060818763878673
RT-OF @eglyman (L1011): Ramp made a real Broadway musical starring Billy Porter, Billy Zane and Jessica Billy Vosk.

It’s a show about bills. By Bills. Starring Bills—with original songs, full choreography, and an actual Broadway playwright.

In the 1950s and ’60s, America’s biggest companies staged lavish musicals about cars, appliances, and soda. Somewhere along the way, we lost our nerve.

We’re bringing back the industrial musical.

One night only, September 25, at the Broadhurst Theatre.

https://t.co/PbMCdlKd9X
RT-URL=https://x.com/eglyman/status/2098049270553383031
TEXT: RT @eglyman: Ramp made a real Broadway musical starring Billy Porter, Billy Zane and Jessica Billy Vosk.

It’s a show about bills. By Bills…
LINKS: http://billpaythemusical.com
--
T=2098064464536818141 | @omarsar0 | 2026-09-10T15:02+00:00 | L39 RT5 C4 V7779 | post
URL=https://x.com/omarsar0/status/2098064464536818141
TEXT: Another goated release by DeepSeek. 

Open weight, btw. Outperforms Opus 5 on key benchmarks, btw. Lower prices too. 

Looks like an extremely efficient model. 

What a legendary run.
QUOTED @deepseek_ai: 🚀 Introducing DeepSeek-V4.1-Flash: smarter, faster, more efficient.

🔹 Introducing the smallest model in our new architecture family, with native visual understanding.
🔹 Designed for greater capability, faster inference, higher throughput, and scaling to larger models.

1/6
--
T=2098071565040853118 | @omarsar0 | 2026-09-10T15:30+00:00 | L71 RT10 C12 V8586 | post
URL=https://x.com/omarsar0/status/2098071565040853118
TEXT: Great paper from AWS.

I use a similar setup where an agent orchestrator sits on top of a multi-agent system.

(bookmark it)

This work introduces one of the many approaches available to manage compound LLM systems.

Compound LLM systems usually solve coordination by adding a higher-level model.

That meta-agent reads worker outputs, writes the final answer, allocates later calls and decides when to stop, which concentrates three separate control decisions in one opaque, order-sensitive call.

UnitBoost investigates whether the manager needs to be generative at all.

A task-given unit map turns worker outputs into slot-value proposals, a constrained argmax assembles the output, and slots left unfilled or unsupported become an explicit residual that directs the next round.

On three held-out benchmarks it beats the best single candidate chosen with gold labels by 0.060 to 0.195 task-score points, and beats input-matched generative managers by 0.048 to 0.076.

Replacing only the management step improves six compound-system configurations. Residual-directed rounds raise FanOutQA cell F1 from 0.4778 to 0.5524.

Chat with Paper: https://t.co/Abzm42JJHL
LINKS: https://academy.dair.ai/papers/unitboost-managing-compound-llm-systems-with-a-merge-operator-not-a-model-2609.09815
--
T=2098076353421545796 | @omarsar0 | 2026-09-10T15:49+00:00 | L30 RT5 C4 V8436 | post
URL=https://x.com/omarsar0/status/2098076353421545796
TEXT: This is brilliant—a great program to get started with building agents. 

Lots of really great resources to learn how to build and scale with AI.

Includes open models, orchestration, retrieval, evaluation, and observability on top of it.
QUOTED @nebiusai: The Nebius AI Builder Program is now available.
AI isn’t just a model you call anymore. It’s a system you build. And builders, not a few closed labs, will decide what it becomes.

The open ecosystem has all the pieces. We want to make it easier to put them together and start building.

The program is free, with $400+ in credits and discounts, working code and cookbooks, office hours with engineers, and a community to build with.

We’re joined by @NVIDIAAI, @LangChain, @huggingface, @cognition, @
--
T=2098079174778835270 | @omarsar0 | 2026-09-10T16:00+00:00 | L74 RT8 C13 V9069 | post
URL=https://x.com/omarsar0/status/2098079174778835270
TEXT: Just amazed by how specialized models keep pushing the Pareto frontier. 

Just watch that massive cost reduction.

SWE-2 achieves 50.0% on FrontierCode 1.1 Main1, within one point of Fable 5.1, while being 64% cheaper. https://t.co/eysqkp39tU
QUOTED @cognition: Introducing SWE-2, our closest model yet to the frontier.

On leading evals, it scores on par with recent frontier models – at up to 70% lower cost.

We scaled RL to multiple trillions of parameters, with a refined recipe that pushes the Pareto curve on both capabilities &amp; cost. https://t.co/FjBxrikExs
--
T=2098111664486826129 | @omarsar0 | 2026-09-10T18:09+00:00 | L3343 RT454 C266 V1851662 | rt
URL=https://x.com/omarsar0/status/2098111664486826129
RT-OF @RohanNayak2 (L3343): We grew from ~0 to $500M ARR, adding $250M last year alone while being EBITDA profitable.

1,300-word post on every growth tactic that worked for us:

1. What got us from 0-$400M ARR in the US works in every country.
2. Retention and Monetisation Hacks.
3. Localization > Translation.
4. Experiment with $1M internal seed checks.
5. Pivoting to only AI content production unlocked 100% ARR growth.

Pocket FM is like Netflix for audio-only dramas, with our own pool of one-person studios.

1. Acquisition Playbook for 0-$10M ARR in any country in 6 months

We run a 90 sec video trailer of an audio drama as an Ad and ask users to download the app if they're interested in the rest of the story.

Our core insight after spending >$100M on acquisition is: If the clickthrough rate (CTR) for an ad goes from 2% to 2.25%, our customer acquisition cost (CAC) decreases by ~ 30%.

We remodelled our system around this insight and built an AI-first 2.25% CTR ad manufacturing machine that works in every country.

For every new country, we take our hit shows -> use LLMs to extract and most intriguing moments -> Write a 5-min script combining all the best parts. The first 60 seconds has to have a hook every 5 seconds and needs to end with a crazy cliffhanger to force a download mid-scroll.

If a marketing video is not hitting our benchmarks (2.5% CTR and 55% 3-second through-play), a creative director gets involved to change the hook or cliffhanger to get the numbers there.

AI lets us make 1,000 Ads per show, and in total we do ~17.5k Ads per month. When a business creating scales from 1k to 10k Ads, the normal thing is for CAC to skyrocket. But with what I just shared, we 7-8x'd our User Acquisition budget without increasing our CAC materially.

It took us 8 months to figure this out, but then the timeline from 0-$10M in every country got shorter and shorter:

US revenue grew to $25M in 19 months. (US is now 78% of total)
Germany to 21M in 11 months.
France to $10M in 3 months.

2. Rete
RT-URL=https://x.com/RohanNayak2/status/2098104784264065525
TEXT: RT @RohanNayak2: We grew from ~0 to $500M ARR, adding $250M last year alone while being EBITDA profitable.

1,300-word post on every growth…
--
