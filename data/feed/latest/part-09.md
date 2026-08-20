# X-FEED 2026-08-20 part 9/10 | items: 8

## @omarsar0 (продолжение)

T=2090138031902675402 | @omarsar0 | 2026-08-19T18:05+00:00 | L51 RT6 C5 V7574 | thread(2)
URL=https://x.com/omarsar0/status/2090138031902675402
TEXT: I enjoyed digging into how the loop is built. If you are moving agents from prototype to production, this repo is worth your time.

Star the repo. https://t.co/Vy7Wuu1Boz
[->] New open-source agent harness just landed!

I got early access to TrueForge by TrueFoundry and have been running it locally for the past few days.

The harness layer deserves as much attention as the model, and open source matters here because you can inspect the loop, run it on your own infrastructure, and swap to the latest or cheaper models.

TrueForge handles the runtime work that makes an agent reliable.

It drives the tool-calling loop, manages context, coordinates subagents, and executes code in a sandbox, with any model you choose. Every tool call re-sends the growing context to the model, so in practice the harness controls most of what an agent costs to run.

A few things stood out from my testing and their published benchmarks.

Vendor-Neutral by design. It runs OpenAI, Anthropic, and Google models alongside open-weight models like Kimi, GLM, and DeepSeek. Model routing is a setting, and you can send each task to the model that fits it.

On a 14-task enterprise agent benchmark, it matched the accuracy of Claude Managed Agents running the same Opus 4.8 model at roughly 30% lower cost per run (3.8M tokens vs 10M for the same answers).

Routing the same tasks to GLM-5.2 held accuracy and brought cost down by about 75%, around $3 per run instead of $12.

Fully self-hosted and Open Source (MIT License). I had it running locally with one command, with sandboxed code execution working out of the box.

It's time to own your agent harness. 

Thanks to @truefoundry for partnering on this post.
LINKS: https://github.com/truefoundry/trueforge
--
## @rasbt — 2 шт.

T=2090254612557156587 | @rasbt | 2026-08-20T01:48+00:00 | L3 RT0 C1 V1251 | post
URL=https://x.com/rasbt/status/2090254612557156587
TEXT: @gpjt Nvm, I just saw your article (https://t.co/9PPtrNJAFI).

Really good one. I should have profiled this better. I plan to do some profiling for the bonus materials and will link your article as a good case-study.

> I'm not that sure why the hand-rolled version is in there -- he covers the maths, but the specific implementation isn't explained in that much depth

Yeah, I think it was the page limits for this chapter...

> the hand-written code from the book uses an approximation using tanh

btw the reason for the approximate one was that the original model weights assumed that the model was using this approximation (gpt-2 was trained with tensorflow where the approximate version is the default); you'd notice slight differences in inference if you don't use the approximate version with the pretrained weights.

> On the other hand, I do intend to have a look at torch.compile in the future, to see what kind of speedup I can get from it.

Yeah, I can imagine that'll get close to the built-in one.

> But anyway, for now, lesson learned: use built-in PyTorch modules when you can. It's a pretty obvious one ;-)

100%. The handrolled ones are just for educational purposes. 

Some function benefit from it a lot (like cross entropy), because they simplify terms in the backward pass, e.g., I discussed this a bit here https://t.co/jFDeu4eMTT)
LINKS: https://www.gilesthomas.com/2026/08/built-in-gelu ; https://sebastianraschka.com/blog/2022/losses-learned-part1.html
--
T=2090254955676414087 | @rasbt | 2026-08-20T01:49+00:00 | L21 RT1 C2 V6341 | post
URL=https://x.com/rasbt/status/2090254955676414087
TEXT: Nice case study on using optimized functions whenever possible (except for educational purposes, though 😆)
QUOTED @gpjt: By switching from a hand-rolled GELU to PyTorch's built-in one, I improved my LLM training speed -- and much more than I expected, from 21,000 tokens/second to 25,000!

https://t.co/NmNQu53cmW
--
## @sh_reya — 1 шт.

T=2089948571475075401 | @sh_reya | 2026-08-19T05:32+00:00 | L71 RT0 C12 V6095 | thread(2)
URL=https://x.com/sh_reya/status/2089948571475075401
TEXT: extremely bearish on any programming tool that doesn't have an agent-friendly interface
[->] bullish on designing pre-attentive attributes for agents; i.e., anything that helps agents solve the problem without spending reasoning tokens
--
## @swyx — 4 шт.

T=2090122629625872546 | @swyx | 2026-08-19T17:04+00:00 | L36 RT2 C3 V7938 | rt
URL=https://x.com/swyx/status/2090122629625872546
RT-OF @bradenjhancock (L36): It's felt like harness month on Twitter. We're seeing much faster and cheaper gains on a bunch of benchmarks by focusing on harness improvement rather than model improvement.

Allowing the harness to be updated during use is just another form of continual learning. The common issue with continual learning is catastrophic forgetting. But a lot of us have an 80/20 situation where most of our agent usage is in the same domain, so it's kind of wasteful to not specialize the harness for the environment it's being used in.

I like the implicit bet the Exo project makes -- allowing specialization beyond just memories and skills may lower the floor, but I think it raises the ceiling more. Excited to have it in the next (not yet announced) @LaudeInstitute  Slingshots batch.

@AlexKrentsel is also an absurdly natural podcast guest. The motivations for the project are well explained on @swyx's recent Latent Space podcast:
https://t.co/fOz4v6Fgol
RT-URL=https://x.com/bradenjhancock/status/2090114460828766567
TEXT: RT @bradenjhancock: It's felt like harness month on Twitter. We're seeing much faster and cheaper gains on a bunch of benchmarks by focusin…
LINKS: https://www.youtube.com/watch?v=5lFD-34dhqE
--
T=2090123965356478898 | @swyx | 2026-08-19T17:09+00:00 | L17 RT7 C1 V3869 | rt
URL=https://x.com/swyx/status/2090123965356478898
RT-OF @latentspacepod (L17): Model routing is having a moment thanks to the $7B Stripe acquisition of OpenRouter. But it's also increasingly important in enterprises. We talk to @glean  CEO @jainarvind about why model routing helps control AI costs for organizations. https://t.co/doTDTuKTwL
RT-URL=https://x.com/latentspacepod/status/2089834053637661095
TEXT: RT @latentspacepod: Model routing is having a moment thanks to the $7B Stripe acquisition of OpenRouter. But it's also increasingly importa…
LINKS: https://www.latent.space/p/glean-model-routing
--
T=2090259930662211615 | @swyx | 2026-08-20T02:09+00:00 | L1 RT0 C1 V1524 | post
URL=https://x.com/swyx/status/2090259930662211615
TEXT: positive UBB take if you view openrouter in that lens

https://t.co/rOtLC5UkC5
QUOTED @cjc: Stripe has confirmed the singularity is here. 

And naturally, it will be usage-based billing.
LINKS: https://x.com/cjc/status/2090153713617010999?s=46
--
T=2090283975105564866 | @swyx | 2026-08-20T03:45+00:00 | L6 RT0 C4 V784 | post
URL=https://x.com/swyx/status/2090283975105564866
TEXT: in a world of cheap many:many, the rock-solid 1:1 is king
--
