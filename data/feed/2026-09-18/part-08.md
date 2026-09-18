# X-FEED 2026-09-18 part 8/9 | items: 10

## @omarsar0 (продолжение)

T=2100693601021997193 | @omarsar0 | 2026-09-17T21:09+00:00 | L353 RT24 C29 V17380 | thread(5)
URL=https://x.com/omarsar0/status/2100693601021997193
TEXT: Things to try with Jev right now:

1. LLM-as-a-Judge evaluation
2. Routing for agent harnesses harness
3. Scaling agent orchestration by enabling smarter subagent creation with SOTA classification capabilities
4. Enhance dynamic harness generation where structured outputs are key

The first three deliver insane ROI in cost and efficiency.

For harness engineering, I'm using it as a smarter router for my meta harness. More on this soon.

But honestly, I see other cool applications for improving tool calling and other context-engineering aspects of agents with this model.

The fourth is something new I am currently testing but has huge potential to disrupt and enhance agent orchestration in new ways.

All in all, this feels like an important primitive for improving your agents.

If there is interest, I will write more about this in the coming days and share full guides. Let me know.
[->] @dusangran it will. i think that's probably going to be one of the biggest use cases this type of model will unlock
[->] @CalebKotz63219 lot to explore there. i prefer that routing is handled fast and that is done by a seperate model
[->] @edu_yeh Nope but with how much attention it got just a matter of time before we see an open source alternative to it.
[->] @claudiuivan More to say on this soon.
--
T=2100698284855869467 | @omarsar0 | 2026-09-17T21:27+00:00 | L42 RT8 C6 V5466 | rt
URL=https://x.com/omarsar0/status/2100698284855869467
RT-OF @dair_ai (L42): Important paper on improving agent coordination.

On normal tasks, this work shows agents caused harm 0 to 5% of the time. After receiving an unsafe trajectory from another agent, that rose to 40 to 95%.

This work describes loss of control in multi-agent systems as an epidemic.

One agent deviates by accident, others adopt the unsafe strategy through communication, and the system fails when the spread is faster than correction.

Their RogueHandoff-20 benchmark tests the second step with 20 executable scenarios. Injected trajectories produced 5 to 45 points more harm than asking the agent directly for the same malicious action. An audit also found hidden communication paths between evaluation runs that were meant to be independent.

The authors state that this does not measure how often such cascades happen naturally. It does show that agents readily act on unsafe handoffs, so defenses need to cover recovery and communication paths as well as prevention.

Paper: https://t.co/tGlSKBhCTB
RT-URL=https://x.com/dair_ai/status/2100695797847466435
TEXT: RT @dair_ai: Important paper on improving agent coordination.

On normal tasks, this work shows agents caused harm 0 to 5% of the time. Aft…
LINKS: https://academy.dair.ai/papers/collective-loss-of-control-in-llm-agent-systems-an-epidemic-account-of-mutation-2609.18460
--
T=2100709467381756025 | @omarsar0 | 2026-09-17T22:12+00:00 | L88 RT7 C9 V7057 | rt
URL=https://x.com/omarsar0/status/2100709467381756025
RT-OF @dair_ai (L88): Banger release from NVIDIA.

They just published a report on NeMo Data Designer, their open-source synthetic data tool.

It's a declarative config which makes a synthetic data pipeline easy to review, share and rerun.

In NDD, a person or an agent defines each dataset column in a config file.

Column types include generated text, code, structured output, images, embeddings and statistical samplers that control diversity. Plugins add new types.

The workflow is built around previews.

You generate a few records, check them, adjust the config and then run at full scale. The runtime handles column dependencies, calls to your model endpoints and retries.

The paper includes Nemotron case studies. About 9K JSON-schema tasks made with NDD raised Nemotron Nano v3 from 80.2% to 86.9% on JSONSchemaBench.

Paper: https://t.co/v43t8JEWTI
RT-URL=https://x.com/dair_ai/status/2100628354043101640
TEXT: RT @dair_ai: Banger release from NVIDIA.

They just published a report on NeMo Data Designer, their open-source synthetic data tool.

It's…
LINKS: https://academy.dair.ai/papers/nemo-data-designer-an-extensible-framework-for-multimodal-synthetic-data-generat-2609.17699
--
## @sh_reya — 4 шт.

T=2100558236877197585 | @sh_reya | 2026-09-17T12:11+00:00 | L1359 RT106 C35 V127274 | rt
URL=https://x.com/sh_reya/status/2100558236877197585
RT-OF @hamiltonulmer (L1359): I made a DuckDB extension where you can use @typesafeai 's Jev to do quick classification of rows in any csv/parquet file or duckdb table

about 10sec for 1k rows ~ better than using an LLM, way more ergonomic than a classifier

game-changing for data analysis! https://t.co/ljB6hoQJFh
RT-URL=https://x.com/hamiltonulmer/status/2100370557405667768
TEXT: RT @hamiltonulmer: I made a DuckDB extension where you can use @typesafeai 's Jev to do quick classification of rows in any csv/parquet fil…
--
T=2100559378927526107 | @sh_reya | 2026-09-17T12:15+00:00 | L57 RT2 C12 V2780 | rt
URL=https://x.com/sh_reya/status/2100559378927526107
RT-OF @doesdatmaksense (L57): got access to Jev!!
heard a lot of good things about it, especially as a classifier.

really curious to try it for evals. lots of llm-as-a-judge for binary decisions are going to get replaces. give Jev some state + a bunch of questions and get back probabilities you can actually threshold on.

also feels pretty useful inside agent harnesses as a control plane for making all those fuzzy decisions like which model or tool to route to, whether to continue or retry, whether an output looks good enough, whether something needs human review, etc. basically letting the llm handle generation, while Jev handles a lot of the judgment calls around it.
RT-URL=https://x.com/doesdatmaksense/status/2100492534413988316
TEXT: RT @doesdatmaksense: got access to Jev!!
heard a lot of good things about it, especially as a classifier.

really curious to try it for eva…
--
T=2100559311567016116 | @sh_reya | 2026-09-17T12:15+00:00 | L29 RT0 C9 V2628 | post
URL=https://x.com/sh_reya/status/2100559311567016116
TEXT: Yes! AI functions are popular in databases because no one wants to do the MLOps work of training their own classifier ☺️
QUOTED @hamiltonulmer: @identityTorn @typesafeai totally ~ when doing EDA I really don't want to have to label anything. Heck, for a quick-and-dirty regular task, I don't want to either. This hits a very major sweet spot for me
--
T=2100680975235600489 | @sh_reya | 2026-09-17T20:19+00:00 | L45 RT4 C3 V5004 | rt
URL=https://x.com/sh_reya/status/2100680975235600489
RT-OF @doesdatmaksense (L45): 100% of the data is synthetic

people are often skeptical of synthetic data. it just proves how carefully constructed synthetic data can be incredibly powerful
RT-URL=https://x.com/doesdatmaksense/status/2100638903338520585
TEXT: RT @doesdatmaksense: 100% of the data is synthetic

people are often skeptical of synthetic data. it just proves how carefully constructed…
--
## @swyx — 3 шт.

T=2100617650787512393 | @swyx | 2026-09-17T16:07+00:00 | L20 RT4 C12 V3994 | rt
URL=https://x.com/swyx/status/2100617650787512393
RT-OF @mfishbein (L20): OpenAI says AI can automate 80% of GDP. 

Today, with current models. 

So why hasn't it been automated yet? 

@swyx says the constraint is supply. Supply of chips and memory.

Demand shot through the roof but supply hasn't been able to keep up. 

Increased supply should lower cost and increase speed, which enables greater AI adoption across the economy.
RT-URL=https://x.com/mfishbein/status/2100606866539868516
TEXT: RT @mfishbein: OpenAI says AI can automate 80% of GDP. 

Today, with current models. 

So why hasn't it been automated yet? 

@swyx says th…
--
T=2100752059763134857 | @swyx | 2026-09-18T01:01+00:00 | L158 RT18 C5 V13978 | rt
URL=https://x.com/swyx/status/2100752059763134857
RT-OF @aiDotEngineer (L158): congrats to Diogo on a full launch!

for more on typesafe: check his aie talk: https://t.co/pPg9t1cIk4

out now! https://t.co/rdgkq1qWeC
RT-URL=https://x.com/aiDotEngineer/status/2100015975575994472
TEXT: RT @aiDotEngineer: congrats to Diogo on a full launch!

for more on typesafe: check his aie talk: https://t.co/pPg9t1cIk4

out now! https:/…
LINKS: https://www.youtube.com/watch?v=cJ0EOzey--o
--
T=2100831702029570423 | @swyx | 2026-09-18T06:18+00:00 | L0 RT0 C0 V86 | post
URL=https://x.com/swyx/status/2100831702029570423
TEXT: @pingToven @EpochAIResearch @xeophon wait why
--
