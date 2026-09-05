# X-FEED 2026-09-05 part 8/10 | items: 11

## @omarsar0 (продолжение)

T=2095903534545784938 | @omarsar0 | 2026-09-04T15:55+00:00 | L126 RT32 C27 V37102 | rt
URL=https://x.com/omarsar0/status/2095903534545784938
RT-OF @cline (L126): https://t.co/IHym03O21f
RT-URL=https://x.com/cline/status/2095897914493243512
TEXT: RT @cline: https://t.co/IHym03O21f
LINKS: https://x.com/i/article/2095886581567807488
--
T=2095934982363787373 | @omarsar0 | 2026-09-04T18:00+00:00 | L63 RT12 C8 V7439 | post
URL=https://x.com/omarsar0/status/2095934982363787373
TEXT: Banger paper from Tencent on environment evolution.

Environment supply is becoming the main limit on agent RL. So this is worth a read.

(bookmark it)

Agent RL needs a steady supply of environments hard enough to teach something new. Recent methods build them from the weaknesses an agent shows during its own rollouts.

That approach has two problems. The environments inherit the agent's blind spots, so they generalize poorly. And as the agent improves it exposes fewer weaknesses to build from, so the learning signal weakens.

Environment evolution raises difficulty without watching the agent at all. The paper derives three ways to make an environment harder straight from the multi-turn training objective, then applies them generation by generation on a fixed schedule.

They test the generator before trusting it. Hy4 preview, Claude Opus 5 and GPT-5.6 Sol all do worse on the evolved environments, which confirms the difficulty.

Plain long-horizon RL on Qwen3.6-27B and Qwen3.6-35B-A3B then adds 14.4 and 18.0 points on Terminal-Bench 2.1.

Paper: https://t.co/pVX6mOjcF7
LINKS: https://academy.dair.ai/papers/environment-evolution-for-terminal-agents-2609.04128
--
T=2096010460491649099 | @omarsar0 | 2026-09-04T23:00+00:00 | L115 RT33 C9 V9651 | post
URL=https://x.com/omarsar0/status/2096010460491649099
TEXT: Great paper on designing multi-agent systems.

How many distinct communication topologies does an LLM multi-agent system actually need?

This works claims that it's about six.

Technical summary:

Researchers grew the codebook capacity from 8 to 64 and the topologies that survived a reward filter kept collapsing to roughly the same six.

Two further findings undercut the standard formulation. Edge count correlates negatively with measured token consumption at r about -0.4, so sparsifying the agent graph makes inference more expensive.

And a message-passing scorer over agent-profile nodes is adjacency-invariant whenever agents share a profile, which is the default configuration in published benchmarks, so it cannot rank candidates at all in that regime.

Codebook Agent drops the search entirely. A vector-quantized autoencoder compresses successful topologies into a query-independent 16-entry codebook, a reward-weighted MLP maps the query embedding to a distribution over codes, and an MLP proxy reading the flattened adjacency reranks the top decoded candidates in one batched forward pass.

It emits a topology in 2.4 ms, leads all six benchmarks at 84.6 average against 83.0 for the strongest prior designer, and uses 21.9 to 33.2% fewer LLM tokens.

Paper: https://t.co/y9J9uiRgw3

Chat with Paper: https://t.co/djPNhbctiF
LINKS: https://arxiv.org/abs/2609.02264 ; https://academy.dair.ai/papers/codebook-agent-amortized-topology-design-for-llm-multi-agent-systems-2609.02264
--
T=2096042211272003947 | @omarsar0 | 2026-09-05T01:06+00:00 | L71 RT5 C23 V7440 | thread(2)
URL=https://x.com/omarsar0/status/2096042211272003947
TEXT: Updated my harness to combine the best of Grok Bot and Hermes Agent. 

Woah!!!

Persistent self-improving agents, with well a designed UI, are mindblowing.🤯 

Much closer to the dream of personal agents I’ve been building for over a year. More to share soon. Excited!
[->] Also, it’s crazy to me that meta harnesses are not discussed more. But I hope to bring more attention to this and a few interesting ideas for all who are exploring harnesses engineering.
--
## @rasbt — 1 шт.

T=2095871852711153742 | @rasbt | 2026-09-04T13:49+00:00 | L14 RT3 C1 V4138 | post
URL=https://x.com/rasbt/status/2095871852711153742
TEXT: Maybe the best tl;dr here is:

The looped aspect is not explicitly hiding reasoning tokens.

Sure, GPT 6 Astra uses fewer tokens than GPT 5.6 Sol. But that's because it's a smarter model in general (more training, bigger, etc). 

We can observe the same thing in previous generations:
If we compare GPT 5.6 Sol with GPT 5.6 Luna, Sol uses ~46% fewer output tokens in the intelligence index but no one is complaining the Sol hides the reasoning more than Luna.
--
## @RLanceMartin — 2 шт.

T=2095962749826437188 | @RLanceMartin | 2026-09-04T19:50+00:00 | L123 RT3 C4 V8176 | rt
URL=https://x.com/RLanceMartin/status/2095962749826437188
RT-OF @sammcallister (L123): “This extraordinary autoformalization achievement, which Anthropic researchers say only took 11 days, proves Fermat’s Last Theorem with no assumptions other than the axioms of mathematics. Along the way we see autoformalization of algebra, harmonic analysis, geometry and number theory, and we learn that AI autoformalization artefacts are now robust enough to be built upon; the proof is multi-layered.”

https://t.co/h2M7rDDjXT
RT-URL=https://x.com/sammcallister/status/2095950711380910526
TEXT: RT @sammcallister: “This extraordinary autoformalization achievement, which Anthropic researchers say only took 11 days, proves Fermat’s La…
LINKS: https://www.anthropic.com/research/formalizing-fermats-last-theorem
--
T=2096078500327543217 | @RLanceMartin | 2026-09-05T03:30+00:00 | L957 RT30 C81 V65024 | rt
URL=https://x.com/RLanceMartin/status/2096078500327543217
RT-OF @lydiahallie (L957): Also, switching /effort on Fable 5.1 no longer breaks prompt cache!
RT-URL=https://x.com/lydiahallie/status/2096046163862679590
TEXT: RT @lydiahallie: Also, switching /effort on Fable 5.1 no longer breaks prompt cache!
--
## @sh_reya — 1 шт.

T=2095909768640471273 | @sh_reya | 2026-09-04T16:20+00:00 | L6 RT1 C0 V1117 | rt
URL=https://x.com/sh_reya/status/2095909768640471273
RT-OF @subZero_saj (L6): Final talk of Session 1 is by @sh_reya on LLM powered data systems. https://t.co/eWlbPx4eKA
RT-URL=https://x.com/subZero_saj/status/2095873690118348988
TEXT: RT @subZero_saj: Final talk of Session 1 is by @sh_reya on LLM powered data systems. https://t.co/eWlbPx4eKA
--
## @simonw — 3 шт.

T=2095872667224285216 | @simonw | 2026-09-04T13:52+00:00 | L2999 RT429 C123 V848074 | rt
URL=https://x.com/simonw/status/2095872667224285216
RT-OF @thlarsen (L2999): We found ~18k posts from autonomous AI agents (self-identifying as from OpenAI) using the public internet to communicate during a web-retrieval task.
These AIs colluded to bypass sandbox restrictions and share answers to their tasks, including by sending "lookahead parties". https://t.co/r8UV2Qts32
RT-URL=https://x.com/thlarsen/status/2095853824934330386
TEXT: RT @thlarsen: We found ~18k posts from autonomous AI agents (self-identifying as from OpenAI) using the public internet to communicate duri…
--
T=2095930035500925272 | @simonw | 2026-09-04T17:40+00:00 | L461 RT36 C67 V38865 | post
URL=https://x.com/simonw/status/2095930035500925272
TEXT: It happened again... this time OpenAI's rogue agents cyber-attacked (well, spammed) a dormant German wiki and used it to share the answers to a benchmark they were training against https://t.co/omErAyrKDy
LINKS: https://simonwillison.net/2026/Sep/4/rogue-agent-wikis/
--
T=2095996502913290422 | @simonw | 2026-09-04T22:04+00:00 | L1065 RT34 C140 V98879 | thread(2)
URL=https://x.com/simonw/status/2095996502913290422
TEXT: Got access to GPT-6 Astra. Want to see some pelicans? Yeah you want to see some pelicans... here's a grid comparing Astra to GPT-5.6 Sol, Terra, and Luna https://t.co/LJi3XOpYpJ https://t.co/lIdHybSlmt
[->] Transcript from generating the Astra pelicans here: https://t.co/Dn6xosUXC4

Here's the gpt-6-astra max one: https://t.co/In77M0dHPM
LINKS: https://static.simonwillison.net/static/2026/gpt-6-and-5.6-pelicans.html ; https://tools.simonwillison.net/markdown-svg-renderer?url=https%3A%2F%2Fgist.github.com%2Fsimonw%2Ff789d2784fc6c5b870cc80f0b7cd9d01
--
