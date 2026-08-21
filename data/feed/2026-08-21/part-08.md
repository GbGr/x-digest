# X-FEED 2026-08-21 part 8/10 | items: 5

## @omarsar0 (продолжение)

T=2090533587066249514 | @omarsar0 | 2026-08-20T20:17+00:00 | L152 RT25 C16 V11068 | post
URL=https://x.com/omarsar0/status/2090533587066249514
TEXT: Banger paper on harness continual learning.

(bookmark it)

If you already are allowing your agents to rewrite their own prompts, skills, or memory files, this one is worth your time.

(bookmark it)

Continual learning has always tracked what changes in the weights. Modern agents accumulate experience in the harness instead, across prompts, memories, tools, skills, and routing rules.

What this means is that if you update any harness component, previously reliable behavior can break with the model completely untouched. The paper names that harness-level forgetting and provides a way to measure it.

Guarded harness evolution separates proposing an update from committing it. A Continual Optimizer drafts a candidate harness from post-execution feedback, and a Continual Evaluator commits only after checking current improvement, historical retention, and validity.

Relative gains exceed 10% across textual reasoning, multimodal perception, and open-world interaction.

Paper: https://t.co/58HvPcpANi

Track more trending AI papers in our academy: https://t.co/1e8RZKs4uX
LINKS: https://arxiv.org/abs/2608.19013 ; https://academy.dair.ai/
--
T=2090537621600510209 | @omarsar0 | 2026-08-20T20:33+00:00 | L28 RT7 C2 V4259 | rt
URL=https://x.com/omarsar0/status/2090537621600510209
RT-OF @dair_ai (L28): Very interesting new work Amazon and colleagues.

(bookmark it)

This connects to the emerging theme of treating the corpus as part of the harness. Planning loops, tool protocols, and context management have matured fast, while the knowledge an agent investigates over still sits behind an embedding index as opaque chunks.

CTIFoundry builds structure at index time instead. Official cross-references across four authoritative security knowledge bases become typed traversable edges, and a span-grounded report layer keeps provenance attached to every chunk. Seven typed tools and three procedural skills expose that structure on a stock open-source harness.

Swapping only the action surface lifts the identically-harnessed agent by 0.19 to 0.28 overall F1 across a four-model panel. A small model on the scaffold beats a flagship on the flat substrate at roughly half the tool calls.

Paper: https://t.co/FywxdksD62

Track more trending AI papers in our academy: https://t.co/LRnpZN7L4c
RT-URL=https://x.com/dair_ai/status/2090535851612942340
TEXT: RT @dair_ai: Very interesting new work Amazon and colleagues.

(bookmark it)

This connects to the emerging theme of treating the corpus as…
LINKS: https://arxiv.org/abs/2608.18613 ; https://academy.dair.ai/
--
T=2090560448277959036 | @omarsar0 | 2026-08-20T22:03+00:00 | L35 RT3 C7 V4230 | rt
URL=https://x.com/omarsar0/status/2090560448277959036
RT-OF @dair_ai (L35): Finally a good paper testing whether memory-based self-improving agents actually improve.

The re-evaluation adds two things prior work skipped, multiple runs to measure variance and randomly shuffled task orders.

Both hurt.

Agent evaluation is already noisy on multi-step tasks, and stacking a self-improvement loop amplifies that noise. Default task orderings impose an implicit curriculum that much of the reported gain was riding on.

Adding detailed rubrics and environment feedback to memory construction recovers part of the drop, and a significant gap remains.

Paper: https://t.co/qRsrqf0GcX

Track more trending AI papers in our academy: https://t.co/LRnpZN7L4c
RT-URL=https://x.com/dair_ai/status/2090559561128407336
TEXT: RT @dair_ai: Finally a good paper testing whether memory-based self-improving agents actually improve.

The re-evaluation adds two things p…
LINKS: https://arxiv.org/abs/2608.18066 ; https://academy.dair.ai/
--
## @sayashk — 1 шт.

T=2090454448384712856 | @sayashk | 2026-08-20T15:02+00:00 | L107 RT3 C13 V10195 | rt
URL=https://x.com/sayashk/status/2090454448384712856
RT-OF @random_walker (L107): This made me wonder — are there newsletters that are getting sold? What happens to them? Do they get their subscriber lists harvested for spam? Very confused by the concept. https://t.co/79CDjAI2YD
RT-URL=https://x.com/random_walker/status/2090421361474715996
TEXT: RT @random_walker: This made me wonder — are there newsletters that are getting sold? What happens to them? Do they get their subscriber li…
--
## @simonw — 1 шт.

T=2090300020918481059 | @simonw | 2026-08-20T04:48+00:00 | L241 RT16 C63 V33838 | thread(2)
URL=https://x.com/simonw/status/2090300020918481059
TEXT: Notes here https://t.co/VGzmtn8RVc
research report here: https://t.co/B2rR4rgCJR
[->] I had Claude Code for web experiment with smolvm as a code execution sandbox

Fable 5 spotted that its environment couldn't run that (no /dev/kvm)... so, without asking me first, it wrote a GitHub Actions workflow to run the experiments and pushed that directly to GitHub instead!
LINKS: https://simonwillison.net/2026/Aug/19/smolmachines-untrusted-sandbox/ ; https://github.com/simonw/research/tree/main/smolmachines-untrusted-sandbox#readme
--
