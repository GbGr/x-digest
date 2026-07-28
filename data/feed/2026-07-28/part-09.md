# X-FEED 2026-07-28 part 9/13 | items: 7

## @omarsar0 (продолжение)

T=2081872946960675017 | @omarsar0 | 2026-07-27T22:42+00:00 | L179 RT31 C17 V15581 | rt
URL=https://x.com/omarsar0/status/2081872946960675017
RT-OF @omarsar0 (L179): New research from NVIDIA.

Does AdamW have a scale ceiling?

This work claims yes, and shows where it sits. At batch sizes up to 100M tokens for next-token prediction, SOAP and Muon maintain training stability and quality while AdamW degrades.

Higher-order optimizers have promised faster convergence for a while. The standing objection has been computational cost and numerical stability at scale.

The team identifies instabilities in SOAP at large batch sizes and eliminates the loss spikes with per-step QR orthogonalization and improved preconditioning strategies. They also measure Muon's orthogonalization quality empirically rather than assuming it.

On multi-billion-parameter models trained over trillions of tokens, both optimizers consistently beat AdamW. A layer-wise distributed optimizer compatible with Megatron-LM balances memory and hides communication without approximating the optimizer math, so the convergence benefit survives the systems layer.

Paper: https://t.co/WFy3YEQms2

Learn to build effective AI agents in our academy: https://t.co/1e8RZKs4uX
RT-URL=https://x.com/omarsar0/status/2081471875885203791
TEXT: RT @omarsar0: New research from NVIDIA.

Does AdamW have a scale ceiling?

This work claims yes, and shows where it sits. At batch sizes up…
LINKS: https://arxiv.org/abs/2607.20548 ; https://academy.dair.ai/
--
T=2081887960207683809 | @omarsar0 | 2026-07-27T23:42+00:00 | L64 RT5 C10 V6510 | thread(4)
URL=https://x.com/omarsar0/status/2081887960207683809
TEXT: With Kimi K3 being this good, there is no more ignoring of open-weight models going forward. You are doing yourself a huge disservice if so. Time to start owning every bit of your intelligence stack. Start small if you need to, but start somewhere.
[->] @joenjenga_ It really is that great of a model.
[->] It's crazy to see in my timeline the widespread availability of this model. Inference providers, coding agents, AI apps of all kinds, etc. Everyone is jumping on this model for a good reason. Don't miss out.
[->] And the best part of it is that it is open, which means you can download the weights, tune it, inspect it, and make it yours. Great for improving efficiency, capabilities, applicability, safety, and much more.
--
T=2081892052841766989 | @omarsar0 | 2026-07-27T23:58+00:00 | L3 RT0 C0 V297 | post
URL=https://x.com/omarsar0/status/2081892052841766989
TEXT: @FireworksAI_HQ @cursor_ai 🔥
--
## @rasbt — 2 шт.

T=2081733770449658181 | @rasbt | 2026-07-27T13:29+00:00 | L126 RT11 C13 V17251 | post
URL=https://x.com/rasbt/status/2081733770449658181
TEXT: Looking forward to chatting with @hugobowne today (July 27) at 4 pm PT on the Vanishing Gradient livestream on YouTube.

Will cover open source, the newest LLMs &amp; trends, agent frameworks, and whatever else comes up.

Basically, all the exciting stuff. Should be fun!
QUOTED @hugobowne: Next week I’m sitting down with @rasbt, independent AI researcher, author of Build a Large Language Model (From Scratch) and Build a Reasoning Model (From Scratch), and creator of Ahead of AI, which just crossed 200,000 subscribers.

Since we last spoke, Sebastian and I have been messaging about the insanity of DeepSeek-V4, then GLM-5.2, and now Kimi K3. Qwen3.8 is about to land as well.

I’m excited to ask him:

• What are these new models actually doing differently?
• What do stronger open-wei
--
T=2081834681582895370 | @rasbt | 2026-07-27T20:10+00:00 | L465 RT25 C8 V34869 | rt
URL=https://x.com/rasbt/status/2081834681582895370
RT-OF @eliebakouch (L465): this scaling law is a piece of art, kimi K3 recipe improves by ~2.5x over kimi K2 recipe

the tech report is amazing https://t.co/SRSHLaqrFd
RT-URL=https://x.com/eliebakouch/status/2081762200180453657
TEXT: RT @eliebakouch: this scaling law is a piece of art, kimi K3 recipe improves by ~2.5x over kimi K2 recipe

the tech report is amazing https…
--
## @sayashk — 2 шт.

T=2081747636697092131 | @sayashk | 2026-07-27T14:24+00:00 | L0 RT18 C0 V0 | rt
URL=https://x.com/sayashk/status/2081747636697092131
RT-OF @? (L0): 
TEXT: RT @sapinker: A much-debated and important paper: AI as Normal Technology  https://t.co/inhFQLPVmK
LINKS: https://knightcolumbia.org/content/ai-as-normal-technology
--
T=2081852012728115695 | @sayashk | 2026-07-27T21:19+00:00 | L66 RT11 C3 V3859 | thread(2)
URL=https://x.com/sayashk/status/2081852012728115695
TEXT: @r_zwetsloot Link to full interview: https://t.co/0vqv8znmLH
[->] How can academics impact AI policy? I had the pleasure of talking to @r_zwetsloot about my PhD experience in AI policy. While the interview is about policy impact, most of the points apply to AI research broadly. https://t.co/o4uWDfkZOY
LINKS: https://horizonlaunchpad.substack.com/p/shaping-ai-policy-as-an-academic
--
