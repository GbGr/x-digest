# X-FEED 2026-07-22 part 9/11 | items: 9

## @omarsar0 (продолжение)

T=2079718100447166533 | @omarsar0 | 2026-07-22T00:00+00:00 | L50 RT9 C15 V7023 | post
URL=https://x.com/omarsar0/status/2079718100447166533
TEXT: Progressive disclosure in agents doesn't scale.

And its benefits seems agent harness dependent.

(bookmark this one)

Finally there is a proper study on using agent skills and the effect of progressive disclosure.

Progressive disclosure is the agent skills pattern where you hand an agent a document path and let it decide what to read, from a short description down to specific passages.

Practitioners adopted it fast for book-length tasks, purely on vibes.

Researchers ran it across three agent harnesses and three model families on InfiniteBench.

On a single book:

> the gain is harness-dependent,
> large when the agent navigates raw documents poorly,
> near zero when a strong harness already retrieves on its own.

Scale to many books and raw navigation falls apart while one level of disclosure pulls ahead. A second routing level never helps and sometimes breaks accuracy.

It feels like progressive disclosure buys context, but not intelligence. It is redundant while a strong agent can find the passage itself, and decisive once the corpus is too large to read.

Paper: https://t.co/SUOIhmwD8j

Learn to build effective AI agents in our academy: https://t.co/1e8RZKs4uX
LINKS: https://arxiv.org/abs/2607.17598 ; https://academy.dair.ai/
--
T=2079726383496826940 | @omarsar0 | 2026-07-22T00:33+00:00 | L34 RT2 C2 V9043 | post
URL=https://x.com/omarsar0/status/2079726383496826940
TEXT: I was a bit too early on this. 

But I highly recommend reading it. 

It essentially packages two ideas mentioned by both Claude (recording skills) and Andrej Karpathy (rich multimodal prompting) today. 

Lots of people seem to be picking this up now.
QUOTED @omarsar0: https://t.co/bPal5UBLGg
--
T=2079740696022446343 | @omarsar0 | 2026-07-22T01:29+00:00 | L244 RT22 C19 V43627 | rt
URL=https://x.com/omarsar0/status/2079740696022446343
RT-OF @omarsar0 (L244): Recommended reading. 

(bookmark it)

Pay attention to the prices and what a combination of models can unlock for you. 

You don't need the absolute best model for everything.

I am not that impressed with the Rust SQLite replica. A totally new and improved SQLite (or something more creative and new) could be a more interesting test. 

Takeaways:

- Use a frontier model for decomposition, architecture, key design choices, and trade-offs.
- Have cheaper, faster workers execute well-defined, narrow implementation tasks.
- Do not have planners implement or workers make broad design decisions.

Use a swarm or harness with a recursive task tree: planners break the original spec into subtrees, delegate them, and workers operate at the leaves. Cursor argues this helps mostly because each agent has a constrained context, rather than simply because many agents run in parallel. Pay extra attention to biases and failures that might emerge from poor/inefficient agent coordination.
RT-URL=https://x.com/omarsar0/status/2079300039525249159
TEXT: RT @omarsar0: Recommended reading. 

(bookmark it)

Pay attention to the prices and what a combination of models can unlock for you. 

You…
--
## @rasbt — 1 шт.

T=2079554737247064355 | @rasbt | 2026-07-21T13:11+00:00 | L1623 RT101 C47 V81376 | post
URL=https://x.com/rasbt/status/2079554737247064355
TEXT: Thanks everyone for all the kind words and feedback. Super happy that you are enjoying Build a Reasoning Model (From Scratch)! 

Unfortunately, there's small typo in listing 6.5 on page 198 (see video below).

The line "torch.manual_seed(0)"
should be "torch.manual_seed(5)"

This correction is needed to reproduce the generated response in listing 6.5 and the corresponding log-probability outputs later in Chapter 6. If you use 0, the generated response and the results that follow will be different.

This will be fixed in the next printing. I am sorry about the oversight, and I hope this note saves you some debugging time.
--
## @RLanceMartin — 2 шт.

T=2079597461174436209 | @RLanceMartin | 2026-07-21T16:00+00:00 | L528 RT42 C23 V22152 | rt
URL=https://x.com/RLanceMartin/status/2079597461174436209
RT-OF @jackclarkSF (L528): Props to OpenAI for publishing this post on some safety and alignment issues observed in internal deployments - there are many counter-incentives to publishing stuff like this, but by making it public we all get better info about safety at the frontier. https://t.co/7UKWrLSI3y
RT-URL=https://x.com/jackclarkSF/status/2079576870555939013
TEXT: RT @jackclarkSF: Props to OpenAI for publishing this post on some safety and alignment issues observed in internal deployments - there are…
LINKS: https://openai.com/index/safety-alignment-long-horizon-models/
--
T=2079635721447760160 | @RLanceMartin | 2026-07-21T18:32+00:00 | L59 RT6 C4 V6876 | thread(2)
URL=https://x.com/RLanceMartin/status/2079635721447760160
TEXT: we've repeatedly seen that this is a useful separation of concerns: 

1/ the brain is a managed harness, well-tuned for Claude, auto-upgraded w/ each model release. 

2/ and hands are dispatched on-demand w/ data residency &amp; network isolation. 

video:
https://t.co/A7ohKgQaAe
[->] this is a nice talk from Vercel Ship 2026. Harrison (a core contributor on Claude Managed Agents) covers some of the benefits of splitting the "brain" (agent harness) from the "hands" (@vercel sandboxes inside your VPC): https://t.co/Ep7Hxcoieo
LINKS: https://youtu.be/kZloOvs08-A?si=Y5_Z7STkAez1xCv2
--
## @sh_reya — 3 шт.

T=2079573187113652732 | @sh_reya | 2026-07-21T14:24+00:00 | L4 RT1 C0 V1257 | rt
URL=https://x.com/sh_reya/status/2079573187113652732
RT-OF @_ScottCondron (L4): Deslopification coming soon
RT-URL=https://x.com/_ScottCondron/status/2079522942870782318
TEXT: RT @_ScottCondron: Deslopification coming soon
--
T=2079700575013224677 | @sh_reya | 2026-07-21T22:50+00:00 | L78 RT2 C6 V7603 | post
URL=https://x.com/sh_reya/status/2079700575013224677
TEXT: I am currently in West Africa teaching university students and faculty about AI and databases. It has already been quite eye-opening for me. AI could not even understand local languages until recently. Some people are worried that they don’t know how to pick projects, majors, and jobs (or advise students) now given how quickly AI is improving. Some thought we have solved these problems in the US and asked for advice. We had to say, we definitely have not solved these problems in the US. 

My takeaway so far is that while we all may be at different points on the AI adoption curve, we are all similarly lost when it comes to envisioning how, in the long term, to harness AI for education, AI for science and social science, AI for building computer systems, etc.
QUOTED @akothari: There’s an insane amount of alpha in:
- People in SF leaving SF to see how people and companies around the world are using AI (hint: most are still using it primarily as search)
- People outside SF spending even two weeks in SF to see how people and companies are operating here (hint: many are already living in the future)

This may be obvious to some, but the gap right now is staggering. The global diffusion of AI is a massive opportunity.
--
T=2079702624568283423 | @sh_reya | 2026-07-21T22:58+00:00 | L79 RT4 C6 V8916 | thread(2)
URL=https://x.com/sh_reya/status/2079702624568283423
TEXT: In 5 years when gen AI is solved, all the big data people are going to be like “the big lesson is that all code is data. there are trillions of LoC generated a day. they need to be stored somewhere for us to query, along with their environments for Instant Replay and Time Travel”
[->] This was supposed to be a joke but now the severity of the truth is dawning on me that
QUOTED @rauchg: The big lesson from AI is that everything is code. A slide deck is code. Design is code. That cool promo video? Code. Excel automation? Code. The universe? Probably made of code too.
--
