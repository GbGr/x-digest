# X-FEED 2026-09-03 part 6/8 | items: 5

## @omarsar0 (продолжение)

T=2095239812689068072 | @omarsar0 | 2026-09-02T19:57+00:00 | L362 RT57 C26 V39051 | rt
URL=https://x.com/omarsar0/status/2095239812689068072
RT-OF @dair_ai (L362): // Harness-of-Harness //

Exciting new research on coding agents that keep building for days without a human.

Here is how it works:

Harness-of-Harness wraps whatever coding harness you already run and organizes its executions into repeated planning, coding and testing increments.

The loop balances repair against capability growth, scopes work into small verifiable steps, keeps implementation-time testing separate from independent evaluation, and constrains the outputs rather than the workflow.

Across GameCraft-Bench, FrontierSWE and ProgramBench with three different harness and model pairs, it averages a 52.25 percent relative gain over the standalone harnesses after three iterations, peaking at 82.86 percent.

Paper: https://t.co/n4V5KwMNjM

Chat with Paper: https://t.co/CCjDSFiYwm
RT-URL=https://x.com/dair_ai/status/2095172426925801608
TEXT: RT @dair_ai: // Harness-of-Harness //

Exciting new research on coding agents that keep building for days without a human.

Here is how it…
LINKS: https://arxiv.org/abs/2609.01481 ; https://academy.dair.ai/papers/harness-of-harness-multi-day-autonomous-software-development-with-continual-impr-2609.01481
--
T=2095240828658589864 | @omarsar0 | 2026-09-02T20:01+00:00 | L74 RT2 C23 V9568 | post
URL=https://x.com/omarsar0/status/2095240828658589864
TEXT: Is it just me, or does this feel like we are in the early innings of RSI? 

Something has dramatically changed in the last month.

Have you witnessed the velocity of model releases recently?
--
T=2095255706324619502 | @omarsar0 | 2026-09-02T21:01+00:00 | L65 RT7 C9 V5978 | rt
URL=https://x.com/omarsar0/status/2095255706324619502
RT-OF @dair_ai (L65): Nice paper with great insights on improving self-evolving agents.

Self-evolving agents fail in three specific ways:

1. Terminal-only feedback makes it ambiguous which step caused the error.

2. Agents memorize task-specific patterns instead of acquiring general capability.

3. And unguarded updates quietly erase competence the agent already had.

HarnessEvolve addresses all three in one loop.

For credit assignment it generates reference trajectories, execution paths produced when the agent is given the ground-truth answer, then aligns failed runs against them to extract error signals.

Those signals are clustered so the update targets a systematic pattern rather than one bad rollout.

Two gates stand between a candidate harness update and the live agent. A quality gate filters data leakage and prompt bloat. A performance gate accepts the update only if it improves the current batch without degrading recent batches, with epoch-end validation on a held-out set choosing the snapshot.

Execution, evaluation, optimization and gating are separate modules, so the agent doing the work is decoupled from the pipeline changing it.

Results hold across open-domain and enterprise benchmarks, different models and different agent frameworks.

Paper: https://t.co/v0qB5sdsNm

Chat with Paper: https://t.co/eMaaJrJe86
RT-URL=https://x.com/dair_ai/status/2095252935659913657
TEXT: RT @dair_ai: Nice paper with great insights on improving self-evolving agents.

Self-evolving agents fail in three specific ways:

1. Termi…
LINKS: https://arxiv.org/abs/2609.00829 ; https://academy.dair.ai/papers/harnessevolve-learning-from-reference-trajectories-for-reliable-agent-self-evolu-2609.00829
--
T=2095276262415577550 | @omarsar0 | 2026-09-02T22:22+00:00 | L33 RT2 C7 V6660 | post
URL=https://x.com/omarsar0/status/2095276262415577550
TEXT: Brilliant effort worth checking out. 

Ultra-long horizon coding tasks are where frontier models like Fable 5.1 will shine. 

But that's a crazy gap (over ~25 percentage points).

What I think could be interesting is seeing results for a mixture of agents like what Cursor did.
QUOTED @ProximalHQ: We are releasing FrontierSWE v2, our updated ultra-long horizon coding benchmark

V2 features an expanded task suite and improved methodology. We see large performance gaps between frontier models, with Claude Fable 5.1 leading by a wide margin https://t.co/VBXoMgMI0e
--
T=2095300793561931948 | @omarsar0 | 2026-09-03T00:00+00:00 | L109 RT11 C19 V7367 | post
URL=https://x.com/omarsar0/status/2095300793561931948
TEXT: What a super interesting paper this one is.

They propose an architecture for agents that outlive their model, harness and host.

Today we describe an agent by whatever model and harness it happens to run on. That works for a single session. It says very little about an agent that runs for months and gets moved to a new model, a new harness, or a new machine along the way.

The paper splits an agent in two.

One half is the agent itself, and it persists. Its identity, its private memory, and its own code with version history.

The other half is plumbing you can replace. The model doing the reasoning, the harness running it, the server hosting it, and the ways people reach it such as chat, an API, or a UI.

Swap the plumbing and you have moved the agent rather than built a new one, as long as the handoff is authorized and keeps the record of where it came from.

The handoff is six steps. Pause the agent, save its state, check the save is valid, attach it to the new setup, load the state back, then let it run again.

They ran the frozen public release on a clean machine and it passed 833 core tests plus 92 more for providers and libraries. They also swapped model versions, interfaces and physical hosts on live deployments.

The authors are careful about what this proves. It shows you can move an agent without breaking it mechanically. Whether the agent still behaves like itself afterwards is a separate question.

Paper: https://t.co/RMxw1FwoZh

Chat with Paper: https://t.co/qJvJ41oxoZ
LINKS: https://arxiv.org/abs/2609.00546 ; https://academy.dair.ai/papers/runtime-independent-persistent-agents-preserving-identity-memory-and-code-across-2609.00546
--
