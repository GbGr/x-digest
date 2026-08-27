# X-FEED 2026-08-27 part 3/8 | items: 10

## @lateinteraction — 15 шт.

T=2092614839331938594 | @lateinteraction | 2026-08-26T14:07+00:00 | L238 RT36 C13 V31628 | rt
URL=https://x.com/lateinteraction/status/2092614839331938594
RT-OF @tomaarsen (L238): 📈 New blog post: Training and Finetuning Multi-Vector Embedding Models with Sentence Transformers.

As a practical example, I finetuned a ColBERT-style model for medical retrieval. 14.5 hours on one RTX 3090, and it beats every general-purpose retriever I could find.

Thread 🧵 https://t.co/zRWY3j3ivJ
RT-URL=https://x.com/tomaarsen/status/2092611931890713066
TEXT: RT @tomaarsen: 📈 New blog post: Training and Finetuning Multi-Vector Embedding Models with Sentence Transformers.

As a practical example,…
--
T=2092616750516822178 | @lateinteraction | 2026-08-26T14:14+00:00 | L22 RT4 C1 V1703 | rt
URL=https://x.com/lateinteraction/status/2092616750516822178
RT-OF @antoine_chaffin (L22): Late interaction is not only strong OOD and on new tasks
It's also insanely strong when fine-tuned, and now with PyLate being merged into ST, it is even easier than before to get models that just destroy everything at home
RT-URL=https://x.com/antoine_chaffin/status/2092616296978350438
TEXT: RT @antoine_chaffin: Late interaction is not only strong OOD and on new tasks
It's also insanely strong when fine-tuned, and now with PyLat…
--
T=2092633716736602263 | @lateinteraction | 2026-08-26T15:22+00:00 | L26 RT3 C3 V1915 | rt
URL=https://x.com/lateinteraction/status/2092633716736602263
RT-OF @AmelieTabatta (L26): Need a model that, out-of-the-box, (almost) tops a specialist benchmark? mLateOn B)
Need to actually top that benchmark? Fine-tune it on an RTX 3090.
Late interaction just can't stop winning!
RT-URL=https://x.com/AmelieTabatta/status/2092631683937837558
TEXT: RT @AmelieTabatta: Need a model that, out-of-the-box, (almost) tops a specialist benchmark? mLateOn B)
Need to actually top that benchmark?…
--
T=2092633690908078579 | @lateinteraction | 2026-08-26T15:22+00:00 | L14 RT4 C2 V1460 | rt
URL=https://x.com/lateinteraction/status/2092633690908078579
RT-OF @paulomouraj (L14): Once again, great models and experiments by @tomaarsen! Really cool to see mLateOn performing so well even at zero-shot when compared against 8B dense models, proving again that late-interaction generalizes better, and fine-tuning on a consumer gpu explodes the gap!
RT-URL=https://x.com/paulomouraj/status/2092617837701370313
TEXT: RT @paulomouraj: Once again, great models and experiments by @tomaarsen! Really cool to see mLateOn performing so well even at zero-shot wh…
--
T=2092654035308285953 | @lateinteraction | 2026-08-26T16:42+00:00 | L87 RT12 C3 V23081 | post
URL=https://x.com/lateinteraction/status/2092654035308285953
TEXT: Thanks to @tomaarsen for letting me contribute a tiny experiment (the dashed triangles) to this yesterday.

I wanted to demonstrate my claim that late interaction's far stronger quality does NOT generally require a "storage overhead", with technology (PLAID) that was released in 2022 before GPT-3.5.

Extremely tiny 307M-parameter mLateOn models, even zero-shot off the shelf ones, have no trouble handily beating every single-vector method, including 26x bigger Qwen3-Embedding-8B by double-digit nDCG %.

Moreover, Tom's lightly-finetuned mLateOn-medical can trivially do so while representing hundreds of millions of tokens with ~1 GiB, an index size that is SMALLER than Qwen3's single-vector fp16 representations*, which is almost certainly the way you're currently storing Qwen embeddings.

*Good luck compressing single-vector representations with that fidelity esp if OOD.
QUOTED @tomaarsen: 📈 New blog post: Training and Finetuning Multi-Vector Embedding Models with Sentence Transformers.

As a practical example, I finetuned a ColBERT-style model for medical retrieval. 14.5 hours on one RTX 3090, and it beats every general-purpose retriever I could find.

Thread 🧵 https://t.co/zRWY3j3ivJ
--
T=2092654230616129648 | @lateinteraction | 2026-08-26T16:43+00:00 | L23 RT1 C1 V2360 | thread(2)
URL=https://x.com/lateinteraction/status/2092654230616129648
TEXT: ok, episode 1 of this is complete AND released inside of @tomaarsen's amazing announcement today:

https://t.co/LYieEH6XCg
[->] @tomaarsen but stay tuned for far bigger things because we have some extremely potent ideas in the space of retrieval - and await the best ones from @dianetc_ (follow her to stay tuned!)
QUOTED @lateinteraction: Thanks to @tomaarsen for letting me contribute a tiny experiment (the dashed triangles) to this yesterday.

I wanted to demonstrate my claim that late interaction's far stronger quality does NOT generally require a "storage overhead", with technology (PLAID) that was released in 2022 before GPT-3.5.

Extremely tiny 307M-parameter mLateOn models, even zero-shot off the shelf ones, have no trouble handily beating every single-vector method, including 26x bigger Qwen3-Embedding-8B by double-digit n
LINKS: https://x.com/lateinteraction/status/2092654035308285953
--
T=2092658357593117063 | @lateinteraction | 2026-08-26T17:00+00:00 | L55 RT2 C2 V6969 | post
URL=https://x.com/lateinteraction/status/2092658357593117063
TEXT: the level to which this was trivial* and yet isn't done by some vector DB providers who offer late interaction by piggybacking on horribly inefficient single-vector infra (then blaming that on the paradigm itself!) is instructive

*i estimate that i hand-held codex for maybe 1hr end to end
QUOTED @lateinteraction: Thanks to @tomaarsen for letting me contribute a tiny experiment (the dashed triangles) to this yesterday.

I wanted to demonstrate my claim that late interaction's far stronger quality does NOT generally require a "storage overhead", with technology (PLAID) that was released in 2022 before GPT-3.5.

Extremely tiny 307M-parameter mLateOn models, even zero-shot off the shelf ones, have no trouble handily beating every single-vector method, including 26x bigger Qwen3-Embedding-8B by double-digit n
--
T=2092659832918602178 | @lateinteraction | 2026-08-26T17:05+00:00 | L96 RT14 C5 V7130 | post
URL=https://x.com/lateinteraction/status/2092659832918602178
TEXT: god i had almost forgotten how immediate it is to get mouth watering results when doing colbert stuff - @antoine_chaffin, @bclavie, @raphaelsrty, and @aaxsh18 were not lying; i know no other ML area with low-hanging fruit this big

await new open models from @dianetc_ and me soon
QUOTED @lateinteraction: Thanks to @tomaarsen for letting me contribute a tiny experiment (the dashed triangles) to this yesterday.

I wanted to demonstrate my claim that late interaction's far stronger quality does NOT generally require a "storage overhead", with technology (PLAID) that was released in 2022 before GPT-3.5.

Extremely tiny 307M-parameter mLateOn models, even zero-shot off the shelf ones, have no trouble handily beating every single-vector method, including 26x bigger Qwen3-Embedding-8B by double-digit n
--
T=2092681206311620752 | @lateinteraction | 2026-08-26T18:30+00:00 | L73 RT11 C4 V25308 | rt
URL=https://x.com/lateinteraction/status/2092681206311620752
RT-OF @mixedbreadai (L73): Mixedbread is retrieval infrastructure for AI agents to find the right evidence across text, PDFs, tables, images, audio, and videos.

We process millions of documents and searches every week. Our control plane runs on @planetscale Metal.

→ 0.05 ms p99 for our busiest access-control query
→ under 1.5ms p99 over every hot query pattern
→ faster debugging with Query insights and agent integrations
RT-URL=https://x.com/mixedbreadai/status/2092654670988628223
TEXT: RT @mixedbreadai: Mixedbread is retrieval infrastructure for AI agents to find the right evidence across text, PDFs, tables, images, audio,…
--
T=2092681231339045161 | @lateinteraction | 2026-08-26T18:31+00:00 | L29 RT1 C0 V2478 | rt
URL=https://x.com/lateinteraction/status/2092681231339045161
RT-OF @rikiyatakehi (L29): Very cool!

Also happy to see how our tiny mxbai-edge-32M holds up:)
RT-URL=https://x.com/rikiyatakehi/status/2092680752068436297
TEXT: RT @rikiyatakehi: Very cool!

Also happy to see how our tiny mxbai-edge-32M holds up:)
--
