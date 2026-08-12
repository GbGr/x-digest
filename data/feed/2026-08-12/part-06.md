# X-FEED 2026-08-12 part 6/8 | items: 6

## @rasbt — 1 шт.

T=2087180773497421926 | @rasbt | 2026-08-11T14:14+00:00 | L997 RT135 C48 V49241 | post
URL=https://x.com/rasbt/status/2087180773497421926
TEXT: Whoa, Meta released a new open-weight LLM yesterday, something that hasn't happened since the good old Llama days.

Their Meta Muse Glimmer model is a 30B multimodal reasoning model with a Gemma-like architecture design. (“Glimmer” is probably a wordplay on “Spark,” the more likely capable model from which Glimmer was distilled. Muse Spark is only available through Meta’s Model API, though.)

Architecture-wise, here are some of the main points:

1. "Only" a 131k context window, compared to Qwen3.6 and Gemma 4, which support 2x that natively; it's reasonable, but maybe on the shorter end in the age of agent harnesses

2. It's a dense model, not a mixture-of-experts. (So, it's fairer to compare it to Qwen3.6 27B than Qwen3.6 30B-A3B.)

3. Hybrid attention with grouped-query attention (GQA) and sliding window attention (SWA); the SWA:GQA pattern is a 3:1 local:global ratio. Other models like Gemma 4, which uses similar components, have a 5:1 ratio for comparison.

4. It adopts gated attention for both GQA and SWA; gated attention has become quite common in recent months. It basically applies a sigmoid gate to the attention output to decide how much of the attention information enters the residual connection. The interesting point is that it uses relatively standard GQA and SWA rather than hybrid attention mechanisms such as Nemotron or Qwen3.6.

5. A very extreme GQA ratio: 32 query heads and only 2 KV heads; for comparison, Gemma 4 31B uses 32 Q / 16 KV in the local heads and 32 Q / 4 KV in the global heads. This means that Meta Glimmer has a very small KV cache.

Overall, the probably most similar architecture is Gemma 3 27B (including the Gemma-style pre/post RMSNorm placement) and Gemma 4 31B, but with some tweaks like SwiGLU instead of GeGLU activations, gated attention, and the more extreme GQA:SWA pattern mentioned before.

What stands out is its extreme KV-cache efficiency. 
I.e., the KV CACHE / TOKEN ratios (in BF16) are:

- Muse Glimmer: 52 KiB (lower is better)
- Qwen3.6 27B: 64 KiB
- Gemma 4 31B: 840 KiB

Modeling-performance-wise, their own benchmarks show that it's mostly ahead of Qwen3.6. According to the independent composite benchmarks on the Artificial Analysis Intelligence Index, it's slightly behind Qwen3.6 (see figure below). So, a few days of using it will tell where it really ranks.

Overall, it looks like a solid model, particularly for agentic workflows. What stands out most is its very low memory footprint and also pretty fast prefill and decode speed. It’s also just great to see Meta releasing open weights again :).
--
## @swyx — 5 шт.

T=2087017780617126075 | @swyx | 2026-08-11T03:26+00:00 | L50 RT1 C5 V13385 | post
URL=https://x.com/swyx/status/2087017780617126075
TEXT: btw pdb envs have an experimental AFS clone support that basically does what all of you are suggesting but runtime agnostic and language agnostic

https://t.co/SiFupvsIm8

we shall replace git by making every single command "agent native"
LINKS: https://pdb-env-research.swyxio.workers.dev/
--
T=2087045848022843451 | @swyx | 2026-08-11T05:18+00:00 | L148 RT4 C47 V29223 | post
URL=https://x.com/swyx/status/2087045848022843451
TEXT: gpt luna max vs claude fable ultracode 

sent "pls build a mostly faithful clone of grok imagine with open models via fal"

i woke up to these two and assumed fable was left and luna was right

i was wrong... it was the other way!!

objectively, fable did the better visual clone. but luna somehow understood intent better and created the more USABLE clone given my open model bent.
--
T=2087046173135901128 | @swyx | 2026-08-11T05:19+00:00 | L17 RT3 C1 V8202 | rt
URL=https://x.com/swyx/status/2087046173135901128
RT-OF @lily_gpupoor (L17): sign up for COLM 2026 before it sells out! for non-local researchers, here's the SF map by @swyx.
safety tip: i added poop alerts 💩 for the rough blocks. try to avoid booking hotel around union square and tenderloin, you'll thank me later. @COLM_conf https://t.co/i8J6BuafCU
RT-URL=https://x.com/lily_gpupoor/status/2087033148454691228
TEXT: RT @lily_gpupoor: sign up for COLM 2026 before it sells out! for non-local researchers, here's the SF map by @swyx.
safety tip: i added poo…
--
T=2087230916590744021 | @swyx | 2026-08-11T17:33+00:00 | L38 RT11 C1 V5491 | rt
URL=https://x.com/swyx/status/2087230916590744021
RT-OF @grinich (L38): AGENT NIGHT is tomorrow at The Regency Ballroom 🌉

The lineup: @swyx · @JayaGup10 · @Altimor · @davidcrawshaw · @bdougieYO · @abhiaiyer · @inazarovaLive

Live demos and sharp discussions, plus a sneak peek of something new from @WorkOS 👀

See you there! https://t.co/yQ85k4kEXX
RT-URL=https://x.com/grinich/status/2087205399426424977
TEXT: RT @grinich: AGENT NIGHT is tomorrow at The Regency Ballroom 🌉

The lineup: @swyx · @JayaGup10 · @Altimor · @davidcrawshaw · @bdougieYO · @…
LINKS: http://luma.com/agent-night
--
T=2087244948441792543 | @swyx | 2026-08-11T18:29+00:00 | L2 RT0 C10 V1832 | post
URL=https://x.com/swyx/status/2087244948441792543
TEXT: if you have a better skill cutting policy or skill cutting skill lmk

https://t.co/ZkOxnGX5Md https://t.co/qXoMl8Vyd2
LINKS: https://forge.smol.ai/skits/swyxio/sbrain?skill=skill-cutter
--
