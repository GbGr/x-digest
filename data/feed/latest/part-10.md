# X-FEED 2026-09-09 part 10/11 | items: 9

## @omarsar0 (продолжение)

T=2097558879194558838 | @omarsar0 | 2026-09-09T05:33+00:00 | L19 RT2 C9 V2793 | post
URL=https://x.com/omarsar0/status/2097558879194558838
TEXT: Nice paper to improve inference efficiency.

It's been a while we haven't seen good work on efficiency.

Here is why it matters:

A long-running agent's workspace outgrows its context window long before the task finishes.

The first approach commonly used, compaction, loses the fine-grained execution evidence. And text retrieval re-prefills content the model already processed.

KVMem keeps the overflow as paged KV state instead, spread across GPU memory, host memory and NVMe.

Lightweight attention-space indexes, native to the model, pick the relevant historical blocks and materialize a query-dependent view that fits inside the native context window.

On the DeepSWE long-context test with Qwen3.8-27B, task success goes from 43.8% under compaction to 48.4%.

The local deployment result stands out. It runs Qwen3.6/3.8-27B NVFP4 with MTP on a laptop with a 24GB RTX 5090, virtualizing an agent workspace up to 1M tokens, four times the model's native 256K window, at around 50 tokens per second.

Paper: https://t.co/rKIAqnzxII
LINKS: https://academy.dair.ai/papers/kvmem-virtualizing-million-token-agent-workspaces-on-a-consumer-gpu-2609.04852
--
## @rasbt — 1 шт.

T=2097319324721557964 | @rasbt | 2026-09-08T13:41+00:00 | L1077 RT99 C81 V62468 | thread(2)
URL=https://x.com/rasbt/status/2097319324721557964
TEXT: Re today's incident, maybe not a bad idea to check your settings (Settings → Data Controls) https://t.co/QHLPaJWoCZ
[->] Btw I don't mean to imply that this is necessarily related or cause for said incident. 
Just a general reminder for a general data privacy hygiene.
--
## @sh_reya — 2 шт.

T=2097353567753666934 | @sh_reya | 2026-09-08T15:57+00:00 | L2694 RT350 C83 V627939 | rt
URL=https://x.com/sh_reya/status/2097353567753666934
RT-OF @Thom_Wolf (L2694): wtf is this way to handle mathematicians work and scientific communication

TLDR: Leven and Tristan worked over several months on one of the Millenium Prize Problems with various AIs to reach final interesting results. OpenAI apparently heard about it in the last days and prompted their latest models to work on the direction Leven and Tristan found fruitful. They then tried to push for controlling communication of the result and dropping Leven from authorship with some very bad taste social pressure.

Hope this is not a glimpse of the future we’ll get in science research with these dominating players playing marketing games hurtful for the real scientific community.
RT-URL=https://x.com/Thom_Wolf/status/2097215782484607029
TEXT: RT @Thom_Wolf: wtf is this way to handle mathematicians work and scientific communication

TLDR: Leven and Tristan worked over several mont…
--
T=2097360579396821144 | @sh_reya | 2026-09-08T16:25+00:00 | L11373 RT570 C55 V167123 | rt
URL=https://x.com/sh_reya/status/2097360579396821144
RT-OF @RadishHarmers (L11373): If you near solving P vs NP, Riemann, or Collatz, and ask an LLM to check your work, it flags it to its AI lab owners to scoop you. The $$$ incentives are too large. I drafted this joke a few days ago, was working to polish it, but must now rush it out on pain of being scooped.
RT-URL=https://x.com/RadishHarmers/status/2097318260718940314
TEXT: RT @RadishHarmers: If you near solving P vs NP, Riemann, or Collatz, and ask an LLM to check your work, it flags it to its AI lab owners to…
--
## @simonw — 2 шт.

T=2097474703380365698 | @simonw | 2026-09-08T23:58+00:00 | L500 RT43 C41 V35543 | post
URL=https://x.com/simonw/status/2097474703380365698
TEXT: Wrote up my thoughts on the whole OpenAI Navier–Stokes Millennium Prize Problem story, and how it highlights the still confusing question of what using my data "to improve model performance" actually means
https://t.co/vgheVu3rw3 https://t.co/dXoCrQPqDm
LINKS: https://simonwillison.net/2026/Sep/8/on-navier-stokes/
--
T=2097475247595536880 | @simonw | 2026-09-09T00:00+00:00 | L50 RT3 C26 V15886 | post
URL=https://x.com/simonw/status/2097475247595536880
TEXT: "Deterministic code checks the result" sounds like they might be implementing a variant of the DeepMind CaMeL paper https://t.co/c91rFU1z3s
QUOTED @dps: One threat we’re particularly focused on is prompt injection, and we handle it in layers. The model is trained to recognize and resist it. The harness marks anything coming from an untrusted source. Deterministic code checks the result. And an ensemble of classifiers runs where the agent can't reach them.
LINKS: https://simonwillison.net/2025/Apr/11/camel/
--
## @swyx — 3 шт.

T=2097345133188632875 | @swyx | 2026-09-08T15:23+00:00 | L575 RT59 C7 V69640 | rt
URL=https://x.com/swyx/status/2097345133188632875
RT-OF @stratechery (L575): Write Things Down

Writing things down is powerful, for humans and for AI; what comes first, however, is what to write, why to do it, and actually getting things done.

https://t.co/9q4tEziR9b
RT-URL=https://x.com/stratechery/status/2097263683411792017
TEXT: RT @stratechery: Write Things Down

Writing things down is powerful, for humans and for AI; what comes first, however, is what to write, wh…
LINKS: https://stratechery.com/2026/write-things-down/
--
T=2097446534417895797 | @swyx | 2026-09-08T22:06+00:00 | L2096 RT213 C170 V1003668 | rt
URL=https://x.com/swyx/status/2097446534417895797
RT-OF @cognition (L2096): The world needs far more software than it can build. Cognition exists to change that.

We’ve just raised over $2B at a $48B valuation, led by a16z, Accel, Founders Fund, General Catalyst, and Avenir.

Since our round in May, run-rate revenue has grown from $492 M to almost $900 M.
RT-URL=https://x.com/cognition/status/2097369798518681891
TEXT: RT @cognition: The world needs far more software than it can build. Cognition exists to change that.

We’ve just raised over $2B at a $48B…
--
T=2097539352683499891 | @swyx | 2026-09-09T04:15+00:00 | L44 RT5 C3 V4821 | rt
URL=https://x.com/swyx/status/2097539352683499891
RT-OF @pk_iv (L44): our conference on the state of the agentic web + computer use could not have been better timed! 

join us in SF on thursday for a glimpse into the near future: https://t.co/65Omy9MpNe
RT-URL=https://x.com/pk_iv/status/2097457675693158438
TEXT: RT @pk_iv: our conference on the state of the agentic web + computer use could not have been better timed! 

join us in SF on thursday for…
LINKS: https://www.browserbase.com/navigate
--
