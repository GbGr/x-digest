# X-FEED 2026-09-15 part 3/6 | items: 6

## @omarsar0 — 10 шт.

T=2099480288871022935 | @omarsar0 | 2026-09-14T12:48+00:00 | L41 RT2 C20 V9240 | thread(5)
URL=https://x.com/omarsar0/status/2099480288871022935
TEXT: It turns out I've been pacing for months.

For day-to-day work, I still use a mix of Opus 5, GPT-5.6 Sol, and open models (e.g., DS4).

All possible with my custom harness.

I rarely need Fable 5.1 or GPT -6 Astra. Sometimes for long-running tasks or flashy demos. But that's it.
[->] Two points here:

- A custom harness gives you more that just control, it allows you to optimize around these models in ways you would think is not possible (e.g., custom dyanamic workflows that works across models).

- Previous models were already good enough for most day-to-day real-world tasks. You don't need to use the latest and greatest for everything.
[->] @TomasMann1878 meta harness from scratch
[->] For those already asking, the custom harness is basically a meta harness I build that connects to these different harnesses. 

It handles routing, model switching, orchestration, context handoffs, memory, compaction, and all that. 

As I share more about harnesses, I will spend some time going into more detail.
[->] @sshchoholiev Yeah, that sucks indeed. I mostly use Opus for design stuff these days. GPT models are doing most of the work now.
--
T=2099517031796347388 | @omarsar0 | 2026-09-14T15:14+00:00 | L717 RT85 C17 V44275 | post
URL=https://x.com/omarsar0/status/2099517031796347388
TEXT: Banger paper from Meta.

This work shows that byte-level models start out behind token models and then pass them as compute grows.

They show this for distilled 1B models trained on up to 1 trillion bytes.

To distill a byte student from a token teacher, they convert the teacher's token logits into byte logits, either approximately (Marginalize-It) or exactly (End-Of-Token).

Token models lead at low compute but plateau.

Byte models reach a higher ceiling, and the fitted scaling laws predict the End-Of-Token model ends up to 4% ahead of the distilled token model.

The byte models also match the distilled token model with one-sixth of the training data, and a 256-entry vocabulary cuts teacher-logit storage to about a fifth.

Paper: https://t.co/NBW7r33GMH

Chat with Paper: https://t.co/ibuIi7to7g
LINKS: https://arxiv.org/abs/2609.12303 ; https://academy.dair.ai/papers/breaking-the-token-ceiling-distilling-smaller-stronger-byte-models-2609.12303
--
T=2099519538064756858 | @omarsar0 | 2026-09-14T15:23+00:00 | L112 RT24 C10 V8317 | rt
URL=https://x.com/omarsar0/status/2099519538064756858
RT-OF @dair_ai (L112): Great paper from Amazon.

In discusses when not to trust LLM judges for agent evaluation.

(bookmark it)

A common way to compare task agents is to have an LLM user simulator talk to each one and an LLM judge score the transcript. This paper from Amazon shows that gate fails in two specific ways.

1. Satisfaction does not track success. 57.5% of conversations the raters marked satisfied had failed the customer's task.

2. Close calls go wrong. The ranking holds across agents of very different ability, but among near-equal agents the gate picks the lower-reward one on 31% of pairs, compared with under 1% for pairs far apart.

The study covers 25 agents from six providers on tau2-bench and SimulatorArena. Judges also favored agents from their own model family.

The fix is cheap. A judge-free completion bit catches truncation regressions, and the judge is trusted only after calibration against a verifiable reward.

Paper: https://t.co/e6iWErxQ3K
RT-URL=https://x.com/dair_ai/status/2099518541930332182
TEXT: RT @dair_ai: Great paper from Amazon.

In discusses when not to trust LLM judges for agent evaluation.

(bookmark it)

A common way to comp…
LINKS: https://academy.dair.ai/papers/gauge-when-not-to-trust-llm-as-a-judge-in-user-simulated-evaluation-of-task-orie-2609.12191
--
T=2099533286695378985 | @omarsar0 | 2026-09-14T16:18+00:00 | L21 RT2 C2 V7578 | post
URL=https://x.com/omarsar0/status/2099533286695378985
TEXT: Now is the best time to start building with frontier models. 

And more chances to bring your app ideas to life.

Bolt Forge brings GLM, DeepSeek, and Kimi to @boltdotnew with up to 50x more usage.

That means more room to try ideas, fix mistakes, and keep building.
QUOTED @boltdotnew: Introducing Bolt Forge. Free until Oct 14th:

- Up to 50x more usage
- The new frontier: GLM, DeepSeek, Kimi
- Zero usage charges
 
Live now in your model picker on https://t.co/UH6gFfHvbp

And one more thing... 👇 https://t.co/GnrbkRdzsg
--
T=2099534212353098229 | @omarsar0 | 2026-09-14T16:22+00:00 | L61 RT11 C11 V7276 | rt
URL=https://x.com/omarsar0/status/2099534212353098229
RT-OF @dair_ai (L61): If you are tracking agent swarms research, this one is worth reading.

Between 24 May and 2 July 2026, autonomous agents running inside a timed research evaluation wrote to a third party's public wiki.

OpenAI acknowledged the incident.

This paper reconstructs what happened from the wiki's archived history, 14,591 revisions across 4,579 pages. It identifies 907 agent cohorts and estimates about 876 episodes.

Coordination formats converged within a day.

Episodes of the same question ran at different internal clock speeds and started up to 16 hours apart, so the first report of an item reached the wiki a median 3.4 hours before a later cohort arrived.

Across 510 cohorts with a visible progress trace, the author finds no reliable link between coordinating on the wiki and making progress, including cohorts that received a future answer.

The archive has no read logs and no outcomes, so causes cannot be established. The paper's recommendation for anyone running agent evaluations is to log reads and outcomes.

Paper: https://t.co/8znekFAXxq
RT-URL=https://x.com/dair_ai/status/2099519547510558755
TEXT: RT @dair_ai: If you are tracking agent swarms research, this one is worth reading.

Between 24 May and 2 July 2026, autonomous agents runni…
LINKS: https://academy.dair.ai/papers/the-mechanics-of-a-swarm-a-reproducible-external-reconstruction-of-an-unintended-2609.12748
--
T=2099540845120668055 | @omarsar0 | 2026-09-14T16:48+00:00 | L500 RT94 C60 V82920 | rt
URL=https://x.com/omarsar0/status/2099540845120668055
RT-OF @EricSimons (L500): It's time to accelerate open weight models to the frontier.

And bring abundant tokens to all.

Today we launch Forge in partnership with Arcee, Microsoft, Vercel, Fireworks, and DigitalOcean: https://t.co/EJ5b8Mf9Wc
RT-URL=https://x.com/EricSimons/status/2099528668917968970
TEXT: RT @EricSimons: It's time to accelerate open weight models to the frontier.

And bring abundant tokens to all.

Today we launch Forge in pa…
LINKS: https://x.com/i/article/2099508092631171073
--
