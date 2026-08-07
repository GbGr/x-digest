# X-FEED 2026-08-07 part 2/9 | items: 7

## @fchollet — 7 шт.

T=2085323411903889876 | @fchollet | 2026-08-06T11:13+00:00 | L2889 RT228 C142 V297648 | thread(6)
URL=https://x.com/fchollet/status/2085323411903889876
TEXT: I would have assumed it was fairly obvious, but in case it's not: a million-line codebase (also known as a "harness"), running at inference time, orchestrating thousands of calls to a neural network for any given task, is the exact definition of a "neurosymbolic architecture"
[->] Among proponents of neurosymbolic architectures, there had been some debate over the years about whether the outer level would be symbolic (i.e. a harness that calls neural models) or whether the outer level would be neural (i.e. a neural model using symbolic tool calls as part of its neural inference cycle).

Right now, the answer is that the outer level is symbolic --  this is the stronger neurosymbolic formulation.

To be exact, it's more like a symbolic sandwich: a symbolic program drives a neural model, but also makes tool calls and writes + runs symbolic scripts as part of its inference cycle. This is a maximalist neurosymbolic vision.
[->] For a very long time most high-performing AI models were end-to-end neural models; vector input -> vector output, with only ultra-thin symbolic preprocessing and postprocessing layers (e.g. label decoding). For many, it seemed that moving more and more logic to the end-to-end neural model was the way of the future. "Differentiable programming".

But what we have now is heavy neurosymbolic systems where the model itself is symbolic.
[->] Some folks already saying "no no it's only neurosymbolic if the symbolic part encodes cognitive logic, otherwise that's just engineering" my man what do you think is in the million-loc harnesses. Why do you think they're this large. Why do you think their presence is critical for long-running reasoning. Try to read a few, several important ones are open source
[->] An accurate characterization of the arc of AI is that it is shaped by two trends:

1. Moving more and more logic to a neural model for tasks where training data can be densely sampled (e.g. the shift from pre-DL feature engineering to end-to-end learning circa 2013-2016, and more recently the trend of baking more and more harness functionality directly into models over time)

2. Achieving more and more powerful / generalizable systems by leveraging those neural models in sophisticated neurosymbolic architectures, e.g. AlphaGo instead of an end-to-end Go-player model (2016), the Waymo neurosymbolic architecture instead of a single end-to-end vehicle control model (early 2020s), TTA LRMs and coding agent harnesses instead of plain LLM inference (now).

As far as I can tell, this dual trend will keep going. You can always do more with a neurosymbolic system than with just the neural model inside it.
[->] A third trend that you should expect in the future is that the symbolic layers will be learned / evolved, rather than hand-engineered.
--
T=2085416724266983682 | @fchollet | 2026-08-06T17:24+00:00 | L935 RT70 C56 V85284 | thread(2)
URL=https://x.com/fchollet/status/2085416724266983682
TEXT: One thing I want to make perfectly clear: back in 2023 and early 2024, I was wrong about the role that LLMs would come to play. I underestimated their long-term importance. I have acknowledged this many times.

This was the moment I changed my mind, in December 2024, following the o3 test-time compute breakthrough: https://t.co/uKovjRrTyD

I did not initially see that LLMs could work as a base to build systems actually capable of fluid intelligence. Then in late 2024 I updated my views.

And here's what did *not* happen: the early 2023 narrative that all we needed to solve AGI was scaling up base LLMs did not pan out. To this day, current base LLMs (considerably scaled up compared to the models from that time) still do not perform well on something as easy as ARC 1 -- and can't even reliably do simple math operations. TTC and harnesses are in fact critical, and the TTC breakthrough was not obvious.
[->] These are the 2023 and early 2024 views I updated based on new evidence. LLMs did in fact represent considerable progress, as a foundation.
LINKS: https://arcprize.org/blog/oai-o3-pub-breakthrough
--
T=2085453401874477556 | @fchollet | 2026-08-06T19:50+00:00 | L198 RT22 C17 V19503 | rt
URL=https://x.com/fchollet/status/2085453401874477556
RT-OF @mikeknoop (L198): Outlook where frontier AI is headed next 18 months:

The AI reasoning training + harness loop works if you can produce enough data and reasoning traces (via verifiers). Proven with code and math results.

Frontier labs desire to scale this horizontally to many more domains as increasing generality isn't emerging from the NN substrate through data/scale.

But it's very expensive and slow to do this training loop manually. Enter "RSI" discourse. Labs want to automate this training loop they now know works. How? By leveraging coding agents to build world models aka symbolic verifiers.

The bet is automated horizontal domain scaling through automatic symbolic world modeling which offers the critical feedback into post-training.

This is important because many domains are intolerant of learning "online". Symbolic world models offer a path to learning/training "offline".

It's safe for an AI system to test hypotheses against a git repo with tests with no consequences. It's not safe for AI to test against online systems eg SaaS databases, tax filings, manufacturing spin up, etc.

A couple other trends to overlay.

We're seeing incredible capabilities emerge from better symbolic harnesses around frontier reasoning models. As time goes forward these harnesses produce the necessary training traces required to teach the models to emulate the harness, obviating the need for the fat harness.

The other related push is towards multi-agent scaling. Many problems are search constrained (we see this in math right now) where a single linear CoT is not the optimal way to find a solution when you're optimizing for time.
RT-URL=https://x.com/mikeknoop/status/2085452241545175176
TEXT: RT @mikeknoop: Outlook where frontier AI is headed next 18 months:

The AI reasoning training + harness loop works if you can produce enoug…
--
T=2085459327767171542 | @fchollet | 2026-08-06T20:13+00:00 | L752 RT40 C27 V76315 | rt
URL=https://x.com/fchollet/status/2085459327767171542
RT-OF @arcprize (L752): We re-tested GPT-5.6 Luna from @OpenAI on ARC-AGI (Verified) following its recent 80% price reduction: 

- ARC-AGI-2: 59.6%, $0.18/task
- ARC-AGI-1: 90.7%, $0.07/task

The new results match Luna's original performance at a much lower cost. https://t.co/K4THsxy9cM
RT-URL=https://x.com/arcprize/status/2085457823115133059
TEXT: RT @arcprize: We re-tested GPT-5.6 Luna from @OpenAI on ARC-AGI (Verified) following its recent 80% price reduction: 

- ARC-AGI-2: 59.6%,…
--
T=2085471158887923728 | @fchollet | 2026-08-06T21:00+00:00 | L45 RT6 C6 V12246 | post
URL=https://x.com/fchollet/status/2085471158887923728
TEXT: The Keras community meeting will take place this Friday at 10am PT -- the team will present the latest developments in the Keras ecosystem, in particular the new vLLM integration.

Anyone can join the call. Please use this link https://t.co/tllqzfieXS to join when the meeting starts (10am Friday).
LINKS: http://meet.google.com/gva-bbpr-twe
--
T=2085475268253098139 | @fchollet | 2026-08-06T21:17+00:00 | L179 RT13 C9 V16930 | rt
URL=https://x.com/fchollet/status/2085475268253098139
RT-OF @arcprize (L179): Gemini 3.6 Flash and 3.5 Flash-Lite from @Google on ARC-AGI (Verified):

3.6 Flash:
- ARC-AGI-2: 60.4%, $0.61/task
- ARC-AGI-1: 91.2%, $0.34/task

3.5 Flash-Lite:
- ARC-AGI-2: 10.3%, $0.14/task
- ARC-AGI-1: 53.5%, $0.09/task https://t.co/MGDSepep3f
RT-URL=https://x.com/arcprize/status/2085469770216792213
TEXT: RT @arcprize: Gemini 3.6 Flash and 3.5 Flash-Lite from @Google on ARC-AGI (Verified):

3.6 Flash:
- ARC-AGI-2: 60.4%, $0.61/task
- ARC-AGI-…
--
T=2085530367839125784 | @fchollet | 2026-08-07T00:56+00:00 | L52 RT7 C4 V9407 | rt
URL=https://x.com/fchollet/status/2085530367839125784
RT-OF @guyvdb (L52): This might be a good time to mention my recent keynotes titled: "Agentic AI is Neurosymbolic AI" https://t.co/MLghFpK5d9
RT-URL=https://x.com/guyvdb/status/2085520125831376906
TEXT: RT @guyvdb: This might be a good time to mention my recent keynotes titled: "Agentic AI is Neurosymbolic AI" https://t.co/MLghFpK5d9
--
