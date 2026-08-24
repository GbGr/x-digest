# X-FEED 2026-08-24 part 3/4 | items: 7

## @omarsar0 — 8 шт.

T=2091548272968245466 | @omarsar0 | 2026-08-23T15:29+00:00 | L107 RT16 C17 V9910 | post
URL=https://x.com/omarsar0/status/2091548272968245466
TEXT: You don't often see one-word titles in AI papers.

That aside, strong recommend this paper from Google DeepMind.

I think this is an interesting training-free approach to evolve model architectures by leveraging the model itself to inform architectural modifications.

Something like this could also inspire even more robust recursive self-improvement approaches.

Approach details below:

A feedforward transformer can only update its internal state as many times as it has layers. Long generations need more updates than that, so chain-of-thought ends up doing basic state tracking in text.

Recirculation adds recurrence at inference time.

The model feeds activations back through itself during prefill, which lets it act like a dynamical system and track belief states without any retraining.

Generation cost stays flat. All the serial work happens in prefill.

On the Gemma3 family, the adaptive variant cuts perplexity 23% and lifts GSM8k accuracy 21%, with the original weights frozen and only light hyperparameter tuning.

Paper: https://t.co/H8LlBJG4pJ

Track more trending AI papers in our academy: https://t.co/1e8RZKs4uX
LINKS: https://arxiv.org/abs/2608.17981 ; https://academy.dair.ai/
--
T=2091558158439182738 | @omarsar0 | 2026-08-23T16:08+00:00 | L172 RT10 C8 V43092 | post
URL=https://x.com/omarsar0/status/2091558158439182738
TEXT: This is gold! Recommend reading if you want to understand the landscape of AI chip architectures. IMO, a lot can change once RSI comes around, as model architectures could evolve rapidly, looking completely different from today, hence requiring different compute needs.
QUOTED @jacobpeake: sharing a new long-form blog post: ai chip architectures

it covers the leading chip architectures (nvidia, amd, tpus, trainium, cerebras, groq) across architecture, scaling (scale-up and scale-out), and software stacks.

it helps build an intuition for the architectures and their trade-offs.

https://t.co/7eZMh3ddZS
--
T=2091558655858479469 | @omarsar0 | 2026-08-23T16:10+00:00 | L69 RT13 C14 V12058 | rt
URL=https://x.com/omarsar0/status/2091558655858479469
RT-OF @dair_ai (L69): The Top AI Papers of the Week (August 17 - 23):

- SocialRL
- Strategy Lock-In
- Agent Lightning v1.0
- The Control-Plane Tax
- Demystifying Agent Skills
- Harness-Level Forgetting
- The Skill Trigger Bottleneck

Read on for more:
RT-URL=https://x.com/dair_ai/status/2091553997471568171
TEXT: RT @dair_ai: The Top AI Papers of the Week (August 17 - 23):

- SocialRL
- Strategy Lock-In
- Agent Lightning v1.0
- The Control-Plane Tax…
--
T=2091565973098676670 | @omarsar0 | 2026-08-23T16:39+00:00 | L28 RT1 C17 V7263 | post
URL=https://x.com/omarsar0/status/2091565973098676670
TEXT: Important discussion. Measuring models against harnesses is completely broken. I prefer to test model quality against minimal harnesses like Pi and Hermes Agent. This is not perfect, as there are biases in the harnesses that favor some models and not others. 

A standard way to do this is missing but important, as harness engineering is where leading AI companies are focusing efforts. Not enough effort here, as things are moving fast and harness optimization is individualistic.

On the flip side, I feel like models will eventually have the ability to dynamically generate harnesses on the fly as per task. Claude models do this already to some extent, though pretty inconsistently and remain a mystery. But this could mean that a harness is just a tunable artifact like a system prompt. In that realm, how are we assessing it, and exactly what? Benchmarking will only get murkier from here onwards.
QUOTED @onusoz: We need to normalize measuring and judging models against a standardized test harness

"Oh but model X performs best in their own proprietary harness"

I could not care less. When I take exams, I go to the standardized classroom, get the standardized pencil and exam sheet, and have to solve it under 2 hours

This system arose because we have a LOT of people to test

Guess what? We now have a LOT of models, and they are multiplying by the day

"Oh but model X performs substantially better in ARC-
--
T=2091588680565522564 | @omarsar0 | 2026-08-23T18:09+00:00 | L19 RT2 C19 V6371 | post
URL=https://x.com/omarsar0/status/2091588680565522564
TEXT: It's one data point, but I think token share for open models will continue to rise. 

You can get more insights by looking more closely at the multi-agent systems/patterns being adopted across domains. A supervisor leads a bunch of execution subagents (frontier open models work beautifully here). This is one of the most effective and widely used patterns today, where subagents dominate token use (which you can get from frontier open models at a much better price and efficiency). This trend will continue. There really is no point in using a Fable 5 for everything, where cheaper models will do just fine and at a faster and cheaper rate.
QUOTED @GavinSBaker: More data than open-source AI is taking share from OpenAI and Anthropic. Open source has gone from 28% token share to 62% token share @vercel over the last 2 months. Chart from @rauchg 

Super impressive given that the sum of OpenAI and Anthropic accelerated in July. So net token/AI infra demand accelerated even more than the acceleration we saw at the frontier. And suspect Grok growing even faster than open-source and we saw some of this in the @tryramp data.

Open-source AI taking share is pos
--
T=2091631620025647184 | @omarsar0 | 2026-08-23T21:00+00:00 | L68 RT11 C17 V6189 | post
URL=https://x.com/omarsar0/status/2091631620025647184
TEXT: Great paper on multi-agent systems for code review.

It's challenging to know how many coding agents to use to address a problem.

The default fix for weak agentic code review is more agents. In turns out that scaling agents to a large number gives diminishing returns on repository-level tasks.

This new work tries structured conflict instead. Adversarial Review runs three agents. A main coding agent writes, a reviewer evaluates, and a critic audits the review before any edit are done.

On LiveCodeBench it beats a five-agent baseline while using three agents.

On SWE-PRBench the naive version exposed a failure mode. The agents converged on agreement without enough evidence behind it. Making disagreement an explicit instruction recovered the highest F1 among tested methods.

They also find that cooperative review works when the disagreement is minimal, structured, and grounded in evidence.

Paper: https://t.co/NY1gcqajI0

Track more trending AI papers in our academy: https://t.co/1e8RZKs4uX
LINKS: https://arxiv.org/abs/2608.18167 ; https://academy.dair.ai/
--
T=2091676534566166949 | @omarsar0 | 2026-08-23T23:58+00:00 | L101 RT13 C10 V9128 | rt
URL=https://x.com/omarsar0/status/2091676534566166949
RT-OF @dair_ai (L101): If you maintain an AGENTS.md or a CLAUDE.md, this one is worth your time.

(bookmark it)

Researchers traced 94K development events across 557 agentic coding sessions, plus 690K file-level change records from 33K agentic pull requests.

Instruction files and working notes account for 60.5% of everything agents read.

Classical technical docs get 10.6%.

API references get 1.3%.

Reading docs is associated with less immediate testing, at an adjusted odds ratio of 0.39.

And consultation is self-initiated 70.2% of the time, against 7.5% driven by a failure.

In multi-commit agentic pull requests, code gets touched first 4.7x more often.

Paper: https://t.co/alrihmMkQd

Track more trending AI papers in our academy: https://t.co/LRnpZN7L4c
RT-URL=https://x.com/dair_ai/status/2091661799737446864
TEXT: RT @dair_ai: If you maintain an AGENTS.md or a CLAUDE.md, this one is worth your time.

(bookmark it)

Researchers traced 94K development e…
LINKS: https://arxiv.org/abs/2608.20195 ; https://academy.dair.ai/
--
