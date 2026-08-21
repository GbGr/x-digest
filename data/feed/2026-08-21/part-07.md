# X-FEED 2026-08-21 part 7/10 | items: 5

## @omarsar0 — 8 шт.

T=2090445800752951425 | @omarsar0 | 2026-08-20T14:28+00:00 | L34 RT10 C13 V7457 | thread(10)
URL=https://x.com/omarsar0/status/2090445800752951425
TEXT: An open-weight release from @dotsstudioai built on the bet that recursive self-improvement starts with recursive self-critique.

Tech blog: https://t.co/0legzXFUlv

Try it free: https://t.co/2FHvcMG4Jc
[->] Real life is harder than a closed benchmark.

User intent emerges gradually. Tasks unfold across stages. External conditions change.

In a simulated coffee e-commerce scenario, the agent tracks inventory, procurement, fulfillment, and customer needs—then revises its plan as conditions evolve.
[->] Learning matters only if the model can act on it.

dots3-note Preview combines text, vision, and speech with stronger coding and tool use—closing the loop from understanding a task to delivering a result.

One example: end-to-end development of a Xiaohongshu VR experience. https://t.co/6ijzh60X5U
[->] Dropped into an unfamiliar environment, dots3-note Preview can:

→ Observe through interaction
→ Form and test hypotheses
→ Update its own memory
→ Correct stale assumptions
→ Reuse what it learns in later decisions

This behavior also generalized to Slay the Spire 2—an environment it wasn’t trained on.
[->] Self-critique also works outside the training loop.

Using a custom internal harness around a branch of dots3-note Preview, the system recursively generated, evaluated, and improved its proofs—earning an officially certified 42/42 and gold at IMO 2026. https://t.co/34RdXyLzr2
[->] The Critic can separate trajectories that environment rewards cannot.

In a hidden-rule knight-placement game, two branches ran for 64 rounds with identical rewards:

→ Branch A found the real constraint: 3.80

→ Branch B misunderstood the objective: 2.29

The reward saw a tie. The Critic saw real progress.
[->] A traditional scalar value head estimates value with a fixed forward pass.

TEMPO instead uses an agentic value model that can scale its reasoning and tool use at test time.

On ARC-AGI-3, TEMPO scored:

→ 31.5% above the baseline checkpoint
→ 20.6% above GRPO https://t.co/Wvbb90qp0k
[->] TEMPO is the proposed answer.

It divides a long trajectory into macro-steps. At each step, the same model switches from actor to critic.

The Critic reasons over the current state, calls tools, and estimates the expected remaining return—before the full task is complete.
[->] The core problem is credit assignment.

A long-horizon rollout may take tens of hours, while a single terminal reward must be attributed across thousands of interactions.

This is where value-free RL methods such as GRPO begin to struggle.
[->] dots3-note Preview is an open-weight model built for tasks that run for hours—sometimes days.

→ 280B total / 16B active parameters
→ 512K context
→ Text, vision, and speech
→ Reasoning, coding, and tool use

But the most interesting part isn’t the model size.

It’s how the model learns to evaluate its own progress before a long task is finished. 🧵
LINKS: https://studio.dots.ai/dots/dots3-en.html ; https://openrouter.ai/dots-studio/dots-3-note-preview:free
--
T=2090466402809561334 | @omarsar0 | 2026-08-20T15:50+00:00 | L95 RT19 C8 V8085 | post
URL=https://x.com/omarsar0/status/2090466402809561334
TEXT: Finally a good paper testing whether agents can really post-train other agents.

(bookmark it)

They analyzed a large corpus of publicly released post-training trajectories. Across tasks, the agent locks in its training strategy at the very first step and spends the entire remaining budget on local adjustments inside it.

They then tried three escalating fixes. An experience-driven scaffold lifted execution broadly, worth 12.6 points on GSM8K and 40.8 on HumanEval, and the strategy stayed frozen.

Human guidance redirected the opening choice, and the agent slid back into local loops once training began. Extra inference compute paid off on easy tasks and did almost nothing on the hardest one.

What agents lack here is a way to reconsider strategy while execution is still running.

Paper: https://t.co/3XJAfRYmtB

Track more trending AI papers in our academy: https://t.co/1e8RZKs4uX
LINKS: https://arxiv.org/abs/2608.19072 ; https://academy.dair.ai/
--
T=2090471258966159670 | @omarsar0 | 2026-08-20T16:09+00:00 | L58 RT13 C22 V6650 | post
URL=https://x.com/omarsar0/status/2090471258966159670
TEXT: The most important agentic workflows are the ones where you collaborate with the agent, verify its results, and encode them as a skill or verifier for reuse. 

This works for things like writing, researching, coding, and other tasks. 

Domain expertise, in the form of human verification, is a crazy moat. Don't let anyone or any company tell you otherwise. 

And you can build incredibly valuable services and products with that. Protect it and don't give it away for free.

Keep upskilling yourself and leverage the AI agents along the way. But don't forget how crucial it is to develop and hone taste, judge quality, and critical thinking. 

In simpler terms, don't offload understanding to your AI systems. Offload all the rest (boring and repetitive tasks). Careful automation goes a very long way.

A lot of the narrative today is around eliminating the need/replacing domain expertise. But if you work on hard problems, which you should be doing with AI, you realize quickly how primitive AI models are in their "intelligence", capabilities, and adapting to extremely hard and important domains. There is a reason why math problems continue to be solved only by folks with deep math backgrounds. Learn from that. I am not saying the models won't get better. They will get better, but so will humans (it's important to be an optimist in human intelligence for this to be crystal clear), and so the agent-to-human relationship and interactions are the real moat and where all the value and discovery will come from.
--
T=2090476536034197871 | @omarsar0 | 2026-08-20T16:30+00:00 | L171 RT13 C9 V30360 | post
URL=https://x.com/omarsar0/status/2090476536034197871
TEXT: This is just the beginning of what's coming. Not paid to say this, but I think Harvey provides a glimpse into the future of what successful AI-native companies will look like and how they operate. 

Successful companies will need to think of how to build and own their entire intelligence stack. They own the models, agents, and everything in between.
QUOTED @harvey: Introducing Tenet, our first model post-trained for legal.

Tenet is a Kimi K3 base that we post-trained with @FireworksAI_HQ on a corpus of publicly available legal data, synthetic data, and human expert data simulating long-horizon legal work.

Training increases Tenet's all-pass rate by 82% on LAB and 22% on LAB Contracts relative to the Kimi K3 base model. It achieves state-of-the-art performance on LAB Contracts and places second on LAB.

These gains generalize to other leading agentic benc
--
T=2090476918403444807 | @omarsar0 | 2026-08-20T16:31+00:00 | L15 RT2 C2 V7374 | post
URL=https://x.com/omarsar0/status/2090476918403444807
TEXT: That video is funny but painfully accurate.

Email might be the biggest opportunity for agents right now. Having Lindy learn the style of replies and keep the inbox organized on its own is genuinely useful. 

The memory feature in Lindy is pretty good, tbh.
QUOTED @Altimor: Announcing the Lindy Chrome extension.  

Bring Lindy straight into your inbox to highlight your most important emails, draft replies backed by all your memories, and teach it how to label your email.  

Live now: https://t.co/av9senk60g https://t.co/Kfudarwt6b
--
