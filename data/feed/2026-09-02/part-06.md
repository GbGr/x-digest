# X-FEED 2026-09-02 part 6/8 | items: 4

## @omarsar0 (продолжение)

T=2094908191075357100 | @omarsar0 | 2026-09-01T22:00+00:00 | L127 RT17 C19 V9073 | post
URL=https://x.com/omarsar0/status/2094908191075357100
TEXT: Super interesting paper from Meta.

Long-horizon research agents are coming.

But one common problem with research agents today is the lack of originality and how to decide what experiments are worth exploring.

An AI research agent can propose far more experiments than it can afford to run, so the problem is not idea generation, it's deciding which candidates get GPU time.

AI Research Preference Models is trained to predict which candidate solution is most promising before any of them execute.

Two variants, both built on frozen pretrained LLMs. An inference-only model reasons over candidate plans, code, and previously executed solutions. An agentic model additionally runs small-scale pilot experiments before committing budget.

Dropped into the AIRA-dojo agent and measured on AIRS-Bench, average normalized score moves from 0.684 to 0.711 and 0.729.

Both variants reach the unguided agent's 24-hour performance in roughly 15 hours, using less than two-thirds of its execution budget, and together set new state of the art on two AIRS-Bench tasks.

Paper: https://t.co/djM6W6qhwU

Chat with Paper: https://t.co/3sKj8bu6l0
LINKS: https://arxiv.org/abs/2608.13940 ; https://academy.dair.ai/papers/ai-research-preference-models-2608.13940
--
T=2094955860707451199 | @omarsar0 | 2026-09-02T01:09+00:00 | L75 RT8 C11 V6438 | rt
URL=https://x.com/omarsar0/status/2094955860707451199
RT-OF @dair_ai (L75): // Agent Zero Memory //

This work separates three things that agent memory systems usually collapse into one.

If you build agents with long-term memory, this memory design is a worth a read.

Here is how it works:

Agent Zero Memory runs an episodic events timeline, an entity-event knowledge graph, and a curated documentary memory of durable facts side by side over the same history.

A retrieval turn passes through an intent gate, then a source router, then three concurrent agentic searches, one per system.

Every stored item carries its origin, timestamp and evidence pointer, and answers run under a citation lock, so a reply may cite only evidence its reader actually opened. When the evidence is missing the system abstains.

It reaches 95.60% on LongMemEval and 93.60% on LoCoMo, both new highs.

The cost result is the more useful one for AI builders. Across eight backbone models accuracy moves by 3.4 points while per-query cost moves about 30x, with near state of the art quality available at up to 20x lower cost per query. Memory design is driving the quality here.

Paper: https://t.co/kWsccbfoAE

Chat with Paper: https://t.co/NPPl02rR8L
RT-URL=https://x.com/dair_ai/status/2094953486047977860
TEXT: RT @dair_ai: // Agent Zero Memory //

This work separates three things that agent memory systems usually collapse into one.

If you build a…
LINKS: https://arxiv.org/abs/2608.29606 ; https://academy.dair.ai/papers/agent-zero-memory-provenance-aware-long-term-memory-for-llm-agents-2608.29606
--
T=2094972586358927466 | @omarsar0 | 2026-09-02T02:16+00:00 | L86 RT10 C7 V7222 | post
URL=https://x.com/omarsar0/status/2094972586358927466
TEXT: Finally, a good paper testing if graph memory actually beats flat retrieval for long-term agents.

(bookmark this one)

Researchers extract each conversational turn into typed nodes and attributed edges, answer from a two-hop subgraph, and hold the candidate-generation budget fixed at five retrieval roots.

On LongMemEval the graph gets token F1 0.42 against 0.47 for a flat vector baseline, and a paired bootstrap over 500 questions puts the gap at -0.050 (95% CI -0.085 to -0.016).

The damage concentrates on questions that require recalling a specific prior assistant turn, where judged correctness falls from 0.911 to 0.607. Splitting a turn into entities discards the surface form those questions depend on.

The forgetting module fares much better. One pruning pass over a persistent 27,021-node graph, scored on recency, access frequency, degree centrality and age, removes 9.8% of nodes and 9.5% of stored bytes with token F1 unchanged.

Paper: https://t.co/KDUecWNGTH

Chat with Paper: https://t.co/b661ajV2ri
LINKS: https://arxiv.org/abs/2608.28978 ; https://academy.dair.ai/papers/selective-forgetting-a-graph-based-memory-framework-for-long-term-llm-agents-2608.28978
--
T=2094989685957288351 | @omarsar0 | 2026-09-02T03:23+00:00 | L189 RT25 C9 V22589 | rt
URL=https://x.com/omarsar0/status/2094989685957288351
RT-OF @dair_ai (L189): Banger paper from the Qwen team.

If you evaluate agents on anything longer than a single session, this one is worth your time.

(bookmark it)

E-Commerce Bench runs an agent through a simulated 365-day year operating several online stores at once.

18 frontier models are scored across seven dimensions and no single model dominates.

GPT-5.6 Sol earns the most, growing a 100,000 opening stake into 1,431,425, then ranks 16th of 18 on fraud avoidance and trails Fable 5 on operational efficiency.

Among open-weight models, Qwen3.8-Max-Preview leads at 416,252, 38% above GLM 5.2 (high), and shows the strongest learning over the horizon by progressively bargaining suppliers down across repeated orders.

Paper: https://t.co/pX3u6GABA6

Chat with Paper: https://t.co/SXhS6zAxBF
RT-URL=https://x.com/dair_ai/status/2094872928240447665
TEXT: RT @dair_ai: Banger paper from the Qwen team.

If you evaluate agents on anything longer than a single session, this one is worth your time…
LINKS: https://arxiv.org/abs/2608.30730 ; https://academy.dair.ai/papers/e-commerce-bench-evaluating-llm-agents-on-long-horizon-autonomous-business-opera-2608.30730
--
