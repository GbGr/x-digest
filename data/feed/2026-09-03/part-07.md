# X-FEED 2026-09-03 part 7/8 | items: 4

## @rasbt — 1 шт.

T=2095141254958858496 | @rasbt | 2026-09-02T13:26+00:00 | L2460 RT338 C99 V167010 | thread(2)
URL=https://x.com/rasbt/status/2095141254958858496
TEXT: A lot of hype around OpenAI's Astra model here on my timeline today. Apparently, this goes back to a new article from The Information, which said Astra is a "recurrent depth or looped transformer". 

It's always interesting to read about new or different approaches (including rumors about what the closed labs may be up to), but let's debunk this a bit.

About 2 months ago, I shared the architecture details of Nanbeige, for example, where "Nanbeige4.2-3B is pretrained from scratch on 28T tokens with a Looped Transformer that reuses the layer stack to increase capacity without adding parameters."
 
Yes, that's it. The looped transformer idea is just reusing layers in the transformer block.

In the case of Nanbeige, the main idea is to reuse the same 22-layer stack (=transformer block) twice instead of once. So, effectively it extends the 22-layer architecture to 44 layers, but without duplicating the weights. 

In simple terms, this roughly doubles the size of the model (if we ignore the embedding and output layers for a second). But instead of requiring 2x the storage and RAM to host this model, it stays at the same size since we reuse the components. However, it's almost 2x as expensive in terms of compute, because we run the embedded text through almost 2x as many layers.

Why? In the Nanbeige 4.2 technical report, the researchers found that two passes gave the best trade-off and retained about 75% of the token efficiency of a standard architecture. (More passes gave barely any gains but made the training much slower and much more expensive.)

While, as far as I know, Nanbeige 4.2 is the first notable open-weight model that adopted this approach, the idea goes back to the NeurIPS paper "Mixture-of-recursions: Learning dynamic recursive depths for adaptive token-level computation". Actually, this paper proposes a mechanism that is a bit more sophisticated by adding a learned router that determines whether each token receives one, two, or more passes. So, easy tokens can exit early while harder tokens receive additional computation.

In sum, Astra may be a really good model, but this shouldn't be about this "looped transformer aspect," which is just a tiny architectural tweak.

Also, the statement "the new technique works in a way that obscures some or all of the AI's reasoning, otherwise known as 'chain-of-thought'" is not necessarily true with respect to the looped transformer method. It's possible that The Information journalist refers to some other technique or misunderstood the looped transformer method.

Reusing layers does not by itself suppress visible chain of thought. It adds computation in hidden states before the next token is emitted, just as ordinary transformer layers do.

But based on the information we have, the only plausible interpretation here is that if a model uses more of these recurrent passes, it may need to generate fewer intermediate reasoning tokens. So then more of its computation happens in latent activations that cannot be read as text. But we would get the same effect if we were scaling up the model size, like GPT 5.6 Luna -> GPT 5.6 Sol.
[->] The YT version of this:
https://t.co/VRL5dPMTk5
LINKS: https://www.youtube.com/watch?v=KT4n-z_4QJU/
--
## @RLanceMartin — 1 шт.

T=2095170001175199771 | @RLanceMartin | 2026-09-02T15:20+00:00 | L526 RT38 C48 V104355 | post
URL=https://x.com/RLanceMartin/status/2095170001175199771
TEXT: i recently added this command to the claude-api skill. run it in Claude Code to fix common prompting "anti-patterns" that can hobble frontier models:

/claude-api prompt-audit
 
patterns include: 

1/Verification rituals. Instructions like "double-check your work” or "verify twice before responding” are often taken literally by frontier models and can waste tokens.

2/ Thoroughness and emphasis boosters. "Be maximally thorough," "CRITICAL: YOU MUST ALWAYS…" can lead to verbosity and extra tool calls when working with frontier models.

3/ Mandatory procedures and scratchpad scaffolds. Fixed step processes (e.g., "think step by step in a scratchpad") or reasoning templates are rituals that frontier models don't need. This scaffolding can stack on top of native reasoning and use unnecessary tokens.

4/ Stale examples. Few-shot examples tuned to an older model's failure modes can teach a frontier model to imitate long reasoning chains on requests that don't need them.

5/ Contradictory rules. Frontier models are better at instruction following. Contradictory instructions ("always refund within policy" vs. "never issue refunds without escalation") can be followed more literally by frontier models, resulting in degraded performance.

6/ Dated configuration. Settings written for an older Claude generation (e.g., manual thinking budgets) can be rejected by the Claude Platform with newer models.

these patterns accumulate in prompts over time, and can quietly degrade performance when upgrading to newer models. a common reason is the frontier models are better at instruction following, so these anti-patterns steer them to spend unnecessary tokens. 

example: i tested a migration from Opus 4.8 to Opus 5 on an internal customer support benchmark. with Opus 5 (and other frontier models like Fable 5.1), verification rituals ("verify twice") use unnecessary tokens by duplicating work. emphasis boosters ("be maximally thorough") become dozens of unneeded searches.

applying prompt audits can improve performance and reduce cost (as shown in example attached and will be sharing a full write-up soon). 

also, the skill is also open source and some of this guidance likely applies generally across frontier models
https://t.co/4rv1lfiDiz

https://t.co/iLbvKfnTH3
QUOTED @petergyang: If you're trying out Fable 5.1 I highly recommend running:

/claude-api prompt-audit

on your skills. It finds a bunch of redundancies and rules to remove for the latest models.

Running it for all my skills now.
LINKS: https://github.com/anthropics/skills/tree/main/skills/claude-api ; https://x.com/petergyang/status/2094987791566622971?s=20
--
## @sayashk — 1 шт.

T=2095192916482535733 | @sayashk | 2026-09-02T16:51+00:00 | L66 RT1 C7 V6465 | rt
URL=https://x.com/sayashk/status/2095192916482535733
RT-OF @random_walker (L66): There is a lot to say from an AI-as-normal-technology perspective about the OpenAI / Hugging Face incident and what lessons we should learn from it — some obvious points that need to be said anyway, and some non-obvious ones. Essay by @sayashk and me coming soon!
RT-URL=https://x.com/random_walker/status/2095192113663103059
TEXT: RT @random_walker: There is a lot to say from an AI-as-normal-technology perspective about the OpenAI / Hugging Face incident and what less…
--
## @sh_reya — 1 шт.

T=2095261507412005163 | @sh_reya | 2026-09-02T21:24+00:00 | L197 RT27 C7 V12709 | rt
URL=https://x.com/sh_reya/status/2095261507412005163
RT-OF @johnhewtt (L197): As agents perform increasingly complex tasks for researchers, it's important to develop norms for communicating with other humans. Here's my lab's policy on AI in writing and communication, focusing on helping us think deeply and communicate precisely.

https://t.co/vdvM7Ky3Os https://t.co/NJ6LemNQVQ
RT-URL=https://x.com/johnhewtt/status/2095231844136489296
TEXT: RT @johnhewtt: As agents perform increasingly complex tasks for researchers, it's important to develop norms for communicating with other h…
LINKS: https://www.cs.columbia.edu/~johnhew/lab/ai-policy.html
--
