# X-FEED 2026-08-26 part 6/7 | items: 7

## @omarsar0 (продолжение)

T=2092326207077634351 | @omarsar0 | 2026-08-25T19:00+00:00 | L139 RT32 C21 V11878 | post
URL=https://x.com/omarsar0/status/2092326207077634351
TEXT: If you keep safety rules or coding standards in an AGENTS.md or a CLAUDE.md, this one is worth your time.

(bookmark it)

Researchers measured what context compaction actually destroys across 20 production agent configurations.

A safety rule and an episodic log compete for the same tokens, and when the budget overflows both get summarized at the same rate. Only the rule needs exact wording to stay enforceable.

Claude Code compact on Sonnet 4.6 preserves 53% of safety rules after one round. After five rounds, it goes to 10%.

Their fix is Knowledge Triage, which classifies each line of the knowledge base by type and routes each type through its own retention policy. Three deterministic operators handle compaction, partitioning, and retrieval, preserving 2 to 4x more safety rules at every ratio with 96% recall over five rounds.

Paper: https://t.co/iVYbNrTRJX

Track more trending AI papers in our academy: https://t.co/1e8RZKs4uX
LINKS: https://arxiv.org/abs/2608.22752 ; https://academy.dair.ai/
--
T=2092389950532554920 | @omarsar0 | 2026-08-25T23:13+00:00 | L56 RT3 C4 V6301 | post
URL=https://x.com/omarsar0/status/2092389950532554920
TEXT: Great paper on agent harnesses.
QUOTED @dair_ai: // There Is No Neutral Harness //

Great work discussing some of the issues in harness evaluation.

Twelve open-weight models answer the same 3,679 items from ARC, HellaSwag, MMLU, and TruthfulQA under 26 equally defensible harness configurations.

Items, weights, and greedy decoding stay fixed. Only option order, prompt wording, and whether the answer is read from generated text or per-option likelihoods change.

gemma4-31b lands anywhere from 31% to 89% depending on the harness alone.

On the 
--
T=2092412718573899970 | @omarsar0 | 2026-08-26T00:44+00:00 | L32 RT3 C10 V4072 | post
URL=https://x.com/omarsar0/status/2092412718573899970
TEXT: Great paper on why agent leaderboard comparisons are hard to trust.

It's on the hot topic of how much of an agent benchmark score actually belongs to the harness.

The harness is the layer between the model and the task. It builds the context the model sees, mediates tool calls, validates outputs, and decides when to retry or stop. Every score comes out of a model and a harness together, but only the model gets reported.

The authors ran a controlled grid to measure this. Three frontier models, three harness configurations, 100 tasks from SWE-bench Verified, with task order, execution environment, step budget, and evaluation script all held fixed.

Swapping the harness moved GLM-5.1 by 13.0 points. Swapping the model inside a fixed harness moved scores by 3.0, 2.5, and 5.0 points.

Harness-induced variance came out 7.8x larger than model-induced variance, and 6 of 9 model-pair comparisons flipped their ranking depending on which harness ran.

Public leaderboards show the same thing. On SWE-bench Verified Mini, HAL reports a 34 point swing for Claude Sonnet 4.5 across scaffolds and nearly 48 points for o4-mini.

They propose a Harness Card, a structured disclosure across seven layers, so you can tell whether a score gap came from the model, the harness, or the interaction.

Paper: https://t.co/pAE8edBsB9

Track more trending AI papers in our academy: https://t.co/1e8RZKs4uX
LINKS: https://arxiv.org/abs/2605.23950 ; https://academy.dair.ai/
--
## @sh_reya — 2 шт.

T=2092261559074779301 | @sh_reya | 2026-08-25T14:43+00:00 | L349 RT62 C19 V88974 | rt
URL=https://x.com/sh_reya/status/2092261559074779301
RT-OF @boazbaraktcs (L349): https://t.co/AWw2y59tv5
RT-URL=https://x.com/boazbaraktcs/status/2091898813283770457
TEXT: RT @boazbaraktcs: https://t.co/AWw2y59tv5
LINKS: http://x.com/i/article/2091897098530619392
--
T=2092292061710159946 | @sh_reya | 2026-08-25T16:44+00:00 | L40 RT3 C6 V11470 | rt
URL=https://x.com/sh_reya/status/2092292061710159946
RT-OF @petergyang (L40): “You still have to look at the data.”

From @sh_reya:

“There is no world in the future, even if you have AGI, where you’re building a product and don’t have to look at your data. You have to be able to inject your taste into the development of your product.

This is our attempt to show you how to do it effectively, with all the benefit and might of AI helping you accelerate.”

📌 Watch the full episode here: https://t.co/BuTklgfbr4
RT-URL=https://x.com/petergyang/status/2091941123187237138
TEXT: RT @petergyang: “You still have to look at the data.”

From @sh_reya:

“There is no world in the future, even if you have AGI, where you’re…
LINKS: https://www.youtube.com/watch?v=bdMHQLvtVaQ
--
## @swyx — 2 шт.

T=2092418790629970086 | @swyx | 2026-08-26T01:08+00:00 | L75 RT9 C7 V10282 | rt
URL=https://x.com/swyx/status/2092418790629970086
RT-OF @StephanEwen (L75): Something we @restatedev are incredibly proud of is powering Replit's agents with durable execution.

Their scale and the sophistication of how their agent architecture uses durable execution is absolutely amazing. Truly an honor to be a part of that.
RT-URL=https://x.com/StephanEwen/status/2090169947456434393
TEXT: RT @StephanEwen: Something we @restatedev are incredibly proud of is powering Replit's agents with durable execution.

Their scale and the…
--
T=2092421090882756769 | @swyx | 2026-08-26T01:17+00:00 | L33 RT2 C3 V8016 | rt
URL=https://x.com/swyx/status/2092421090882756769
RT-OF @aditabrm (L33): I will be addressing the allegations https://t.co/hmsJ9t2oMN
RT-URL=https://x.com/aditabrm/status/2092420428396642361
TEXT: RT @aditabrm: I will be addressing the allegations https://t.co/hmsJ9t2oMN
--
