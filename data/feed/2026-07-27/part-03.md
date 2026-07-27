# X-FEED 2026-07-27 part 3/4 | items: 10

## @mitsuhiko — 6 шт.

T=2081306120455340213 | @mitsuhiko | 2026-07-26T09:10+00:00 | L239 RT8 C9 V18111 | post
URL=https://x.com/mitsuhiko/status/2081306120455340213
TEXT: AI really makes me re-evaluate things. I always liked Cloudflare's DOs but I was a) worried about lock-in and b) the DX was horrible. Now I worry about neither. AI can make me move off quickly and it's now the agent's problem to suffer through wrangler and their runtime.
--
T=2081352486057578868 | @mitsuhiko | 2026-07-26T12:14+00:00 | L31 RT0 C3 V3991 | post
URL=https://x.com/mitsuhiko/status/2081352486057578868
TEXT: Heatwave is coming and we’re out of town. Going to do some moistioneering and aquaspronkling today. Wish me look! https://t.co/nJ1kmzAgt4
--
T=2081358322565857790 | @mitsuhiko | 2026-07-26T12:37+00:00 | L24 RT0 C29 V12225 | post
URL=https://x.com/mitsuhiko/status/2081358322565857790
TEXT: Do you think you will work in or run a software factory in two years for most of your software development?
--
T=2081358913811734797 | @mitsuhiko | 2026-07-26T12:40+00:00 | L144 RT1 C8 V18248 | post
URL=https://x.com/mitsuhiko/status/2081358913811734797
TEXT: Unfortunately "Datenschutz" (Data privacy) in the German speaking world has become the excuse to everything. https://t.co/08lWmHNcWs
QUOTED @polizeiberlin: @nida_banou @BrennpunktUA Ein Foto finden Sie unter folgendem Link: https://t.co/gzhjx9qVx6
Aus datenschutzrechtlichen Gründen können wir dies nicht direkt auf Social Media teilen.
LINKS: https://x.com/polizeiberlin/status/2081247011005735004
--
T=2081395567289053577 | @mitsuhiko | 2026-07-26T15:05+00:00 | L42 RT1 C3 V87268 | post
URL=https://x.com/mitsuhiko/status/2081395567289053577
TEXT: Vibing too hard for GitHub search. https://t.co/5OLj1D434Y
--
T=2081418453878006213 | @mitsuhiko | 2026-07-26T16:36+00:00 | L413 RT3 C24 V78718 | thread(2)
URL=https://x.com/mitsuhiko/status/2081418453878006213
TEXT: Was curious. openclaw/openclaw is 72K commits, 7M LOC and 2.2GB of .git data. https://t.co/ZorbzAbvwp
[->] Small little slop report. https://t.co/4zdmZNKrr6 https://t.co/AtToMifMj4
QUOTED @mitsuhiko: Vibing too hard for GitHub search. https://t.co/5OLj1D434Y
LINKS: https://x.com/mitsuhiko/status/2081395567289053577?s=20 ; https://radius.earendil.com/artifact/01kyfppxkffmyvwm8n060dc0hn
--
## @omarsar0 — 4 шт.

T=2081438258664235360 | @omarsar0 | 2026-07-26T17:55+00:00 | L48 RT5 C1 V24866 | rt
URL=https://x.com/omarsar0/status/2081438258664235360
RT-OF @dair_ai (L48): https://t.co/bVYEuDFWY1
RT-URL=https://x.com/dair_ai/status/2081437966866505856
TEXT: RT @dair_ai: https://t.co/bVYEuDFWY1
LINKS: http://x.com/i/article/2081432283236442112
--
T=2081441816394490194 | @omarsar0 | 2026-07-26T18:09+00:00 | L116 RT18 C5 V19532 | rt
URL=https://x.com/omarsar0/status/2081441816394490194
RT-OF @dair_ai (L116): The Top AI Papers of the Week (July 20 - July 26):

- GAMUT
- PRO-LONG
- Harness Handbook
- From Memory to Skills
- Progressive Disclosure
- Global Workspace in LLMs
- Structured Output Collapses Diversity

Read on for more:
RT-URL=https://x.com/dair_ai/status/2081438074702078156
TEXT: RT @dair_ai: The Top AI Papers of the Week (July 20 - July 26):

- GAMUT
- PRO-LONG
- Harness Handbook
- From Memory to Skills
- Progressiv…
--
T=2081471875885203791 | @omarsar0 | 2026-07-26T20:09+00:00 | L90 RT16 C12 V8440 | post
URL=https://x.com/omarsar0/status/2081471875885203791
TEXT: New research from NVIDIA.

Does AdamW have a scale ceiling?

This work claims yes, and shows where it sits. At batch sizes up to 100M tokens for next-token prediction, SOAP and Muon maintain training stability and quality while AdamW degrades.

Higher-order optimizers have promised faster convergence for a while. The standing objection has been computational cost and numerical stability at scale.

The team identifies instabilities in SOAP at large batch sizes and eliminates the loss spikes with per-step QR orthogonalization and improved preconditioning strategies. They also measure Muon's orthogonalization quality empirically rather than assuming it.

On multi-billion-parameter models trained over trillions of tokens, both optimizers consistently beat AdamW. A layer-wise distributed optimizer compatible with Megatron-LM balances memory and hides communication without approximating the optimizer math, so the convergence benefit survives the systems layer.

Paper: https://t.co/WFy3YEQms2

Learn to build effective AI agents in our academy: https://t.co/1e8RZKs4uX
LINKS: https://arxiv.org/abs/2607.20548 ; https://academy.dair.ai/
--
T=2081530022947705201 | @omarsar0 | 2026-07-27T00:00+00:00 | L62 RT15 C8 V7154 | post
URL=https://x.com/omarsar0/status/2081530022947705201
TEXT: Great technical paper from Google.

Great read on why context beats scale for agents working against unfamiliar APIs.

(bookmark it)

GPU kernel optimization has KernelBench to hillclimb on. TPUs had nothing, and the Pallas DSL is documented thinly enough that models mostly guess. New research from Google, Harvard, and UC Berkeley introduces JAXBench, 50 JAX workloads built from real MaxText architectures like Llama-3.1, DeepSeek-V3, Mixtral, Mamba-2, and AlphaFold2.

Eight operators ship with hand-tuned Pallas kernels from Tokamax, so agent output gets measured against expert work instead of a naive baseline.

With Gemini 3 Flash, conditioning on curated TPU documentation lifts per-sample correctness from 5.8% to 37.3%, solving 48 of 50 benchmarks at a 1.28x geomean speedup. Beam search then pushes it to 1.36x.

Correctness turned out to be a documentation problem and speed turned out to be a search problem.

Paper: https://t.co/8lOLtFHlfq

Learn to build effective AI agents in our academy: https://t.co/1e8RZKs4uX
LINKS: https://arxiv.org/abs/2607.20466 ; https://academy.dair.ai/
--
