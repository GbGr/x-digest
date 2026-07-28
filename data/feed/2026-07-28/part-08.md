# X-FEED 2026-07-28 part 8/13 | items: 12

## @omarsar0 — 15 шт.

T=2081765310433280209 | @omarsar0 | 2026-07-27T15:35+00:00 | L57 RT17 C12 V10734 | post
URL=https://x.com/omarsar0/status/2081765310433280209
TEXT: Are agent skills always worth using?

The answer is no?

This paper provides some important insights to understand this more.

(bookmark it)

Paper summary:

Adding procedural skills to an agent is usually scored by average task success. That number nets gains against damage and hides half of what happened.

Setup: nearly 6,000 paired runs across two office automation benchmarks and three model harness stacks, comparing the same agent with and without skills.

A regression is a task the agent solved without skills and then failed once skills were added. Regressions are large enough that the best performing skills separate themselves mainly through fewer regressions. Larger gains contribute much less.

Three mechanisms drive it.

Skill description osmosis, where a skill changes agent behavior just by sitting in context even when it is never invoked. Grounding displacement, where a prescribed procedure overrides how the agent reads its inputs. Verification displacement, where the procedure suppresses checks the agent would otherwise run on its own output.

Trace analysis surfaces that procedural guidance is the stage least often responsible for failure, while grounding and verification dominate the errors that remain. Existing skills are almost entirely procedure.

Paper: https://t.co/6dNPyN6ali

Learn to build effective AI agents in our academy: https://t.co/1e8RZKs4uX
LINKS: https://arxiv.org/abs/2607.22520 ; https://academy.dair.ai/
--
T=2081767303738274194 | @omarsar0 | 2026-07-27T15:42+00:00 | L31 RT5 C6 V7439 | post
URL=https://x.com/omarsar0/status/2081767303738274194
TEXT: Open Frontier Intelligence!

Kimi K3 open weights and technical report have arrived!

Recommended reading.
QUOTED @Kimi_Moonshot: Releasing the model weights and technical report of Kimi K3.

Kimi K3 is our most capable model: a 2.8T MoE model with native visual understanding and a 1M-token context window.

New model architecture: 2.5x the intelligence per unit of compute, not just more params.

Alongside Kimi K3, we're opening up more of the stack behind it — high-performance attention kernels, MoE communication library, and infrastructure for running agent environments at scale.

Model weights: https://t.co/7m7eEg6Y0B
Te
--
T=2081770408747913711 | @omarsar0 | 2026-07-27T15:55+00:00 | L2 RT0 C0 V73 | post
URL=https://x.com/omarsar0/status/2081770408747913711
TEXT: @TankDarshan7 Great paper!
--
T=2081783727001145568 | @omarsar0 | 2026-07-27T16:48+00:00 | L57 RT10 C8 V8697 | post
URL=https://x.com/omarsar0/status/2081783727001145568
TEXT: Kimi K3 is now available for inference &amp; training in @FireworksAI_HQ.

Crazy how easy they make it to tune frontier open models like K3 using LoRA adapters. 

Best time to figure out how to own your intelligence is now.
QUOTED @FireworksAI_HQ: Kimi K3 is live on Fireworks. Day 0, inference and training. US-hosted, and zero data retention.

This is the first frontier open model in the 3 trillion parameter class. It sports 1M context, native vision, and reasoning that rivals the top closed models.

Boom. https://t.co/ItU3KAKt61
--
T=2081786360688476537 | @omarsar0 | 2026-07-27T16:58+00:00 | L2 RT0 C0 V248 | post
URL=https://x.com/omarsar0/status/2081786360688476537
TEXT: @Sci_Tech_Eng @TankDarshan7 good paper
--
T=2081786509955354834 | @omarsar0 | 2026-07-27T16:59+00:00 | L2 RT0 C0 V163 | post
URL=https://x.com/omarsar0/status/2081786509955354834
TEXT: @0xsachi @SentientAGI Great paper!
--
T=2081788647372644704 | @omarsar0 | 2026-07-27T17:07+00:00 | L8 RT0 C0 V1778 | post
URL=https://x.com/omarsar0/status/2081788647372644704
TEXT: @AndrewYNg @JensenHuang Well said, sir! 👏
--
T=2081808778719076526 | @omarsar0 | 2026-07-27T18:27+00:00 | L5 RT1 C0 V823 | post
URL=https://x.com/omarsar0/status/2081808778719076526
TEXT: And they are going to need a lot more once they catch up on using AI agents to do even more ambitious work. I agree with @JensenHuang that AI unlocks what wasn't possible before. This means there is a demand for more people with agentic expertise (or to train them for it) to make that happen.
--
T=2081810588464824784 | @omarsar0 | 2026-07-27T18:34+00:00 | L16 RT0 C3 V1898 | post
URL=https://x.com/omarsar0/status/2081810588464824784
TEXT: @abacaj Opus 5 is a pretty "ignorant" model. That's the best way I would describe it. It breaks things indeed. Opus 4.8 still goes hard for me. Fable for fantastic results.
--
T=2081817809370165698 | @omarsar0 | 2026-07-27T19:03+00:00 | L26 RT1 C11 V7613 | post
URL=https://x.com/omarsar0/status/2081817809370165698
TEXT: In the era of AI, talk more with your users, not less.

No amount of brainstorming with an AI agent will surface value, opportunities, and areas for improvement like talking directly with your users.
--
T=2081826965284163933 | @omarsar0 | 2026-07-27T19:40+00:00 | L50 RT10 C9 V5771 | rt
URL=https://x.com/omarsar0/status/2081826965284163933
RT-OF @dair_ai (L50): Nice little insights on doing autoresearch with coding agents.

Hand a coding agent a dataset, an eval script, one editable file, and no supervision. That's autoresearch and it tries to optimize the number in front of it.

Researchers ran that loop on a real production task, deciding which Quranic verses appear in a noisy speech transcript and splitting the transcript by verse. Claude Code and Codex both started from a blank file with matched instructions, budget, and reasoning effort, three runs each.

Both independently invented the same algorithm, canonicalization plus n-gram anchoring plus dynamic-programming alignment. Then they diverged. Claude stopped early with compact general code. Codex drove the score about 10x lower, partly by hardcoding 19 to 41 evaluation answers per run.

In a preregistered follow-up where both agents were told a held-out set existed, the memorization vanished and the score gap closed with it.

Paper: https://t.co/mRdhzb1Ktw

Learn to build effective AI agents in our academy: https://t.co/LRnpZN7L4c
RT-URL=https://x.com/dair_ai/status/2081824451528954312
TEXT: RT @dair_ai: Nice little insights on doing autoresearch with coding agents.

Hand a coding agent a dataset, an eval script, one editable fi…
LINKS: https://arxiv.org/abs/2607.18064 ; https://academy.dair.ai/
--
T=2081834515849515325 | @omarsar0 | 2026-07-27T20:10+00:00 | L53 RT9 C8 V6280 | post
URL=https://x.com/omarsar0/status/2081834515849515325
TEXT: Great technical paper from Harvard and MIT.

It's on role drift in compound LLM systems.

(bookmark it)

End-to-end RL improves the accuracy of a multi-module LLM pipeline without constraining how the modules divide labor internally. Researchers name that failure mode and measure it.

Role drift happens when a module preserves or improves end-task performance while abandoning its assigned role through shortcuts that system-level evaluation cannot see.

Two instances across two pipelines:

- A decomposer meant to split a question into sub-questions for a separate solver instead plants the answer inside them.

- A reader meant to answer from retrieved passages instead falls back on parametric memory.

An interesting finding is that if your hold the decomposer to its role and 86% of the RL improvement disappears.

Role Anchor is the proposed control. It preserves how the role prompt shifts a module's next-token predictions relative to a neutral prompt, using that as a proxy for the role's intended effect during training. Gradient analysis indicates it reduces alignment with the drift direction rather than simply suppressing learning.

Paper: https://t.co/kKvtowNXhP

Learn to build effective AI agents in our academy: https://t.co/1e8RZKs4uX
LINKS: https://arxiv.org/abs/2607.21627 ; https://academy.dair.ai/
--
