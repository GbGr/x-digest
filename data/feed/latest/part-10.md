# X-FEED 2026-09-04 part 10/11 | items: 9

## @omarsar0 (продолжение)

T=2095601652157821306 | @omarsar0 | 2026-09-03T19:55+00:00 | L135 RT6 C17 V29841 | post
URL=https://x.com/omarsar0/status/2095601652157821306
TEXT: I had to look twice at this table.

I know they are just numbers, but how the heck do you beat a competitor model released just a couple of days ago on some of the toughest benchmarks out there? 

Something is different about GPT-6 Astra.
QUOTED @OpenAI: GPT-6 Astra is state-of-the-art on FrontierMath Tier 4, ARC-AGI 3, and TerminalBench-4.0.

GPT‑6 Astra is also a major advance for scientific discovery, with state-of-the-art performance on Terminal-Bench Science 0.1 and HealthBench Pro. https://t.co/7hEFadVAN9
--
T=2095612805496164801 | @omarsar0 | 2026-09-03T20:40+00:00 | L349 RT54 C14 V23720 | post
URL=https://x.com/omarsar0/status/2095612805496164801
TEXT: Banger paper from Google DeepMind and colleagues.

(bookmark it)

A model reads its entire KV cache on every generated token, even though it ends up attending to a tiny slice of it.

In other words, if you ask about one detail from a 1M-token conversation the global attention layers re-read all of it, per token.

The usual fix is to guess the relevant tokens first with cheap proxy scores, which still costs O(N) every step. Declarative Attention asks the model instead.

The model declares where it needs to look, inside its own chain-of-thought.

In this way, generation splits into three modes: global reads the full context, focus reads one specific region, and local reads only recent output.

The inference engine parses those declarations the same way it parses tool calls and skips most of the cache read.

On zero-shot on off-the-shelf weights across 15 long-context tasks, attended tokens during decoding drop 52.0% on Gemma-4-31B and 31.1% on Qwen-3.6-27B.

Paper: https://t.co/caC2iKjXGD

Chat with Paper: https://t.co/6TIllXY5nQ
LINKS: https://arxiv.org/abs/2609.02737 ; https://academy.dair.ai/papers/language-models-can-control-their-own-attention-2609.02737
--
T=2095633412388192505 | @omarsar0 | 2026-09-03T22:01+00:00 | L112 RT4 C19 V8790 | thread(2)
URL=https://x.com/omarsar0/status/2095633412388192505
TEXT: Is it just me, or is it odd that we got access to Fable 5.1 on launch day but not GPT-6 Astra? 

Kinda disappointed about it, tbh. 

Hope that's not how AGI is launched. Just saying.
[->] That's why I am bullish on open models. We need access to AGI together at once, not in phases. 😅
--
T=2095667273004462392 | @omarsar0 | 2026-09-04T00:16+00:00 | L66 RT11 C4 V6358 | rt
URL=https://x.com/omarsar0/status/2095667273004462392
RT-OF @dair_ai (L66): Brilliant paper on long-horizon agents.

They cut 78.9% of an agent's LLM calls while raising its success rate.

Here is how:

It turns out that ReAct issues one primitive action per model round. That allows frequent replanning, and on long-horizon tasks it spends most of the episode re-deciding routine sequences that were never in doubt.

Training an agent to emit variable-length action chunks with standard RL fails because the policy never learns where a chunk should end, so it either falls back to single actions or commits to sequences that run far too long.

SPACE derives the supervision from data it already has.

It induces two-level programmatic skills from successful trajectories and uses the subskill boundaries as direct chunk-boundary labels, then distills the temporal structure into a primitive-chunk policy with hybrid on-policy and off-policy optimization and chunk-aware credit assignment.

On ALFWorld and ScienceWorld it improves success rates by 7.0 to 31.3% over the strongest baseline in each setting while reducing average LLM decision rounds by up to 78.9%.

Paper: https://t.co/G1qi98XetG

Chat with Paper: https://t.co/RNr7I1Q9Ml
RT-URL=https://x.com/dair_ai/status/2095617916284936502
TEXT: RT @dair_ai: Brilliant paper on long-horizon agents.

They cut 78.9% of an agent's LLM calls while raising its success rate.

Here is how:…
LINKS: https://arxiv.org/abs/2609.02042 ; https://academy.dair.ai/papers/act-more-decide-less-skill-guided-adaptive-action-chunking-for-long-horizon-llm-2609.02042
--
## @RLanceMartin — 2 шт.

T=2095533773668683878 | @RLanceMartin | 2026-09-03T15:25+00:00 | L203 RT14 C11 V34003 | rt
URL=https://x.com/RLanceMartin/status/2095533773668683878
RT-OF @Voxyz_ai (L203): If you just switched Claude Code to Fable 5.1, run this on your Skills first:

/claude-api prompt-audit

𝗜 𝗿𝗮𝗻 𝗶𝘁 𝗮𝗰𝗿𝗼𝘀𝘀 𝗺𝘆 𝗲𝗻𝘁𝗶𝗿𝗲 𝘄𝗼𝗿𝗸𝘀𝗽𝗮𝗰𝗲 𝘆𝗲𝘀𝘁𝗲𝗿𝗱𝗮𝘆. It found duplicate constraints, dead slash commands, old hard-coded model names, and output scaffolding written for older models.

One of the clearest fixes:

Before:

CRITICAL: You MUST use this tool when...

After:

Use this tool when...

Fable 5.1 follows instructions more literally. Extra emphasis that kept older models on task can now trigger repeated checks and unnecessary tool calls.

The command only generates an audit report and a proposed diff. 𝗜𝘁 𝗱𝗼𝗲𝘀 𝗻𝗼𝘁 𝗲𝗱𝗶𝘁 𝗮𝗻𝘆 𝗳𝗶𝗹𝗲𝘀.

Each finding includes its location, explanation, and confidence level. You decide which changes to apply.

Quick setup below. 👇
RT-URL=https://x.com/Voxyz_ai/status/2095489486129877331
TEXT: RT @Voxyz_ai: If you just switched Claude Code to Fable 5.1, run this on your Skills first:

/claude-api prompt-audit

𝗜 𝗿𝗮𝗻 𝗶𝘁 𝗮𝗰𝗿𝗼𝘀𝘀 𝗺𝘆 𝗲…
--
T=2095697892657049945 | @RLanceMartin | 2026-09-04T02:18+00:00 | L2729 RT138 C174 V622584 | rt
URL=https://x.com/RLanceMartin/status/2095697892657049945
RT-OF @ClaudeDevs (L2729): We're exploring a new way to let you extend and customize Claude Code: Function Hooks.

Here's a couple videos showing what you'd be able to do. It hasn't shipped yet, we'd love feedback on this on our GitHub issue. https://t.co/0F3kBO3kjl
RT-URL=https://x.com/ClaudeDevs/status/2095572891941351550
TEXT: RT @ClaudeDevs: We're exploring a new way to let you extend and customize Claude Code: Function Hooks.

Here's a couple videos showing what…
--
## @sh_reya — 2 шт.

T=2095549447455560007 | @sh_reya | 2026-09-03T16:28+00:00 | L93 RT11 C11 V13940 | post
URL=https://x.com/sh_reya/status/2095549447455560007
TEXT: Love that AI functions are going mainstream. Several AI folks laughed at us when we started building DocETL; saying that better models are going to “solve” unstructured data processing. But 2 years later joke is on them: AI-powered data processing is being operationalized, as AI-powered operators (AI functions) in SQL are making database vendors tons of money. I think we are only at the tip of the iceberg and there is *so* much interesting stuff to be done all across the stack, from BI/interfaces for humans and agents to figure out the right questions to ask, down to custom LLM inference/execution engines and new features and indexes for storage engines
QUOTED @sethrosen: Snowflake, Databricks, ClickHouse, BigQuery, MotherDuck, etc are adding models and agents to mature systems that were never designed around LLMs

so they’re being forced to solve many of the architectural problems the rest of software has as well but they may be solving them first
--
T=2095599195809857578 | @sh_reya | 2026-09-03T19:45+00:00 | L12 RT1 C0 V1306 | rt
URL=https://x.com/sh_reya/status/2095599195809857578
RT-OF @pateljm (L12): It was great to have Connor McArthur, co-founder of @dbt_labs, give a flash talk in @CMUDB's database course. Watch for a quick update on what’s new with dbt, plus Connor’s quick take on dbt + Fivetran.

https://t.co/hy2rGpLO4i
RT-URL=https://x.com/pateljm/status/2095598284064669999
TEXT: RT @pateljm: It was great to have Connor McArthur, co-founder of @dbt_labs, give a flash talk in @CMUDB's database course. Watch for a quic…
LINKS: https://youtu.be/vYk4s5pr2FI
--
## @simonw — 1 шт.

T=2095595788542046260 | @simonw | 2026-09-03T19:32+00:00 | L200589 RT20071 C4787 V49243457 | rt
URL=https://x.com/simonw/status/2095595788542046260
RT-OF @OpenAI (L200589): This is GPT-6 Astra.

Anything you can do on a computer, Astra can do for you. Fast. https://t.co/gDd0IsewJw
RT-URL=https://x.com/OpenAI/status/2095595741528125780
TEXT: RT @OpenAI: This is GPT-6 Astra.

Anything you can do on a computer, Astra can do for you. Fast. https://t.co/gDd0IsewJw
--
