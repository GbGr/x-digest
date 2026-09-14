# X-FEED 2026-09-14 part 4/5 | items: 5

## @omarsar0 — 5 шт.

T=2099133736310731250 | @omarsar0 | 2026-09-13T13:50+00:00 | L66 RT7 C22 V8934 | post
URL=https://x.com/omarsar0/status/2099133736310731250
TEXT: This is all I will say on the matter:

It’s alarming to see the constant effort to try to tell me how I should use AI, how I should build AI, and now how I should pace it.

Is it just me, or are all these proposals demanding way too much control?

It’s clear that open-source AI matters more than ever.

It’s how we free ourselves from suspicious views, constant desire for control, and hidden agendas.

There's still so much to solve. 

Better evals, removing biases, novelty generation, reliability, creativity, code quality, OOD problems, automation capabilities like dynamically generating workflows/harnesses, automated prompt engineering, compaction, cost, multimodality, omni models, latency, throughput, long context understanding, retrieval, tool calling, agent coordination, and the list goes on and on.

We need more people working on these problems instead of constantly fear-mongering society about what the technology isn't.   

As an independent researcher, I don't ignore the safety concerns around AI. Some are valid. And I work on these every day. But we all need to bring more scientific rigor back to this problem, less anthropomorphizing of frontier capabilities, and concerns more grounded in reality than in personal belief or feelings. 

Lastly, I've never seen so much pessimism about human capabilities as what the topic of recursive self-improvement has brought. We need to be more optimistic about humanity's potential, and how we all play a role in this. To me, that's one of the real problems.

I remain optimistic about our field. Transparent dialogue is key to getting this right. But cleverly coordinated self-serving efforts are not welcome. We need to level the playing field. AI is too important to be controlled by only a few.

Now back to building.
--
T=2099173843289977183 | @omarsar0 | 2026-09-13T16:30+00:00 | L61 RT8 C3 V22493 | rt
URL=https://x.com/omarsar0/status/2099173843289977183
RT-OF @dair_ai (L61): https://t.co/B0r0rw2yrC
RT-URL=https://x.com/dair_ai/status/2099168306863190147
TEXT: RT @dair_ai: https://t.co/B0r0rw2yrC
LINKS: https://x.com/i/article/2099167331314204676
--
T=2099176998748737909 | @omarsar0 | 2026-09-13T16:42+00:00 | L95 RT12 C6 V13925 | rt
URL=https://x.com/omarsar0/status/2099176998748737909
RT-OF @dair_ai (L95): The Top AI Papers of the Week (September 7 - 13):

- STAIR
- PARSER
- FrogNano
- Codebook Agent
- Procedural Graphs
- AI-Native Design Docs
- Proactive Thought Partners

Read on for more:
RT-URL=https://x.com/dair_ai/status/2099168415487287613
TEXT: RT @dair_ai: The Top AI Papers of the Week (September 7 - 13):

- STAIR
- PARSER
- FrogNano
- Codebook Agent
- Procedural Graphs
- AI-Nativ…
--
T=2099184337195565335 | @omarsar0 | 2026-09-13T17:12+00:00 | L227 RT28 C22 V16720 | post
URL=https://x.com/omarsar0/status/2099184337195565335
TEXT: Looped transformers are a popular architecture topic right now.

This new technical report extends the loop across tokens.

Recurrent Looped Transformer (RLT) makes the decoder recurrent over every token, prompt and response included.

A causal encoder builds global KV memory. For each new token, the decoder combines the token's encoder representation with its own final hidden state from the previous token and a sliding-window cache of recent activations.

With a 48-layer decoder, the computation path after t tokens runs through 48t decoder blocks, while each token still executes a fixed number of blocks. Depth grows with the sequence and per-token cost stays the same.

The same state transition is used for pretraining, SFT, sampling and RL replay, and nothing resets at the prompt-response boundary. RL replay rebuilds states under the current weights instead of reusing stale rollout states.

The report is a design proposal. The author states that reasoning gains, hardware speedups and RL scaling are goals that have not been measured yet.

Paper: https://t.co/rSSuuWijR3

Chat with Paper: https://t.co/fVDQaGdfpX
LINKS: https://github.com/yifanzhang-pro/recurrent-looped-tranformer ; https://academy.dair.ai/papers/recurrent-looped-transformer
--
T=2099208894866178204 | @omarsar0 | 2026-09-13T18:49+00:00 | L773 RT61 C61 V81667 | thread(2)
URL=https://x.com/omarsar0/status/2099208894866178204
TEXT: Should you build an agent harness?

I see lots of opinions about it.

My thoughts:

As an AI engineer, learning how to build a harness is one of the best ways to stay ahead and unlock unique value from agents.

If you understand how to build one, you can, at a minimum, transfer that knowledge to tune whatever harness or set of harnesses (closed or open) you use. 

In the best case, you apply your domain expertise to build domain-specific harnesses that unlock unique real-world value and solve reliability issues other companies just aren't willing to invest time in. If you haven't noticed, many companies and startups have already started doing this. Harnesses are enablers in that way.

I don't see any drawbacks in learning to build one. 

The main pushback against building a custom harness is that models will get better at generating them on the fly, so why build one? Or that companies will provide harness-as-a-service, etc. Now, ask yourself: will you have the level of customization that a proper harness requires? See, you are not building a wrapper here; you are building an important part of your intelligence stack. Something you want to control completely. 

Like automated prompt engineering, evals, and many other areas requiring extensive domain knowledge, harness engineering isn't something models are great at (see dynamic workflows from ant as an example). We assume too much that tools will remain static, data won't change, or knowledge will not evolve. A custom harness lets you own these issues and solve them at your desired pace. You simply cannot afford to sit back and wait for model providers to solve this problem for you. The harness is too important to offload.

While general frontier models get better at verifiable (math, code, and the like) tasks, I haven't seen evidence that they solve reliability issues when you apply them to domain-specific and more dynamic environments. This is why you want to understand how the harness works and potentially build your own. I see a lot of companies already doing this in bio, health, legal, and finance. 

My other concern about just relying on a model provider to solve the harness for you is vendor lock-in. Right now, we mostly use single models for most tasks, but it's not hard to see a world where we leverage a set of frontier models (open and closed) to address issues like cost and diversity of intelligence. Are you going to rely on some company to build that harness solution for you, or, even worse, trust a single model to do that for you?

I can go on and on. 

Building your own harness is about working towards building your own intelligence stack. I don't think that's optional where things are headed if you really want to have a differentiated business or offering. 

So where do you get started?

I suggest feeding this list of seminal harness engineering papers to your agent: https://t.co/nOPcXIaITT

You can start with something like: "Summarize the main components of an agent harness by researching this list of papers and tools: https://t.co/nOPcXIaITT. Then put together a set of visual notes on where to get started to build my own minimal harness using <language_of_your_choice>."

Your thoughts? I want to keep this as an open discussion. Please share any concerns or thoughts. I'll share more thoughts as the conversation evolves. 

https://t.co/uW8VgM9FzH
[->] @JayKurtz90 And thanks for sharing your use case and experience.
QUOTED @omarsar0: Learn to build a harness, folks.

It's not surprising to me that so many YC builders want to build domain-specific harnesses. 

If you work long enough on a domain-specific problem, you quickly realize the opportunity. But you also realize how important that harness will be to stay competitive in the agentic era.

From a product perspective, harnesses open up interesting new surface areas and experiences for the services/products you provide.

From a technical perspective, harnesses are how you 
LINKS: https://academy.dair.ai/papers/collections/harness-engineering ; https://x.com/omarsar0/status/2098809969252450451?s=20
--
