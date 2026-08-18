# X-FEED 2026-08-18 part 7/9 | items: 10

## @omarsar0 — 7 шт.

T=2089230498199474249 | @omarsar0 | 2026-08-17T05:59+00:00 | L76 RT14 C11 V15450 | rt
URL=https://x.com/omarsar0/status/2089230498199474249
RT-OF @omarsar0 (L76): Interesting new research from IBM.

If you pick models from benchmark deltas, some of that delta belongs to the phrasing rather than the model.

BenchDrift generates meaning-preserving variations of benchmark problems along linguistic, referential, pragmatic, and structural axes, holding the answer fixed, then measures how often correctness flips.

Phrasing sensitivity does not fade as models improve. It changes sign. Weak models gain more from rephrasing than they lose, while strong models lose far more than they gain, so the top models on a benchmark are the ones whose scores depend most on the wording they happened to receive.

Fragility also belongs to the rephrasing. Across eight models on GSM8K, MMLU, and MATH-Hard, they largely agree on which rephrasings cost the most correct answers even while differing in how much they drift overall.

Rephrasing breaks answers models were confident about, whether the problem gets shorter or longer.

Paper: https://t.co/69JlAwXcev

Track more trending AI papers in our academy: https://t.co/1e8RZKs4uX
RT-URL=https://x.com/omarsar0/status/2088675092238889461
TEXT: RT @omarsar0: Interesting new research from IBM.

If you pick models from benchmark deltas, some of that delta belongs to the phrasing rath…
LINKS: https://arxiv.org/abs/2608.11694 ; https://academy.dair.ai/
--
T=2089376463330128151 | @omarsar0 | 2026-08-17T15:39+00:00 | L109 RT21 C7 V13131 | post
URL=https://x.com/omarsar0/status/2089376463330128151
TEXT: Interesting paper demystifying agent skills.

If you maintain skills for your agent, this one is worth your time.

(bookmark it)

Skills are usually assumed to inject knowledge the model lacks. However, this paper finds something interesting.

Across 8,135 normalized trial records, procedural anchoring accounts for 65.7% of cases where a skill helps, and explicit knowledge injection accounts for 4.5%. Skills stabilize execution rather than supply facts.

As the pool grows from 5 to 100 skills, actual-use precision falls from 29.6% to 3.3%.

Skills still beat Workflow Memory by 6.06 points in matched comparisons, and they break under brittle assumptions, incompatible contexts, or insufficient adaptation.

Paper: https://t.co/BRo32B4GXY

Track more trending AI papers in our academy: https://t.co/1e8RZKs4uX
LINKS: https://arxiv.org/abs/2608.14036 ; https://academy.dair.ai/
--
T=2089383982827794660 | @omarsar0 | 2026-08-17T16:08+00:00 | L180 RT19 C7 V41793 | thread(2)
URL=https://x.com/omarsar0/status/2089383982827794660
TEXT: Recommended read. Good tips for how to coordinate/orchestrate multiple agents in Codex.
[->] BTW, this is a really good prompt (packaged as a skill) you could use for the coordinator.

It's from the post, and I think it's a really interesting use of parameters like reasoning_effort &amp; fork_turns for effective and efficient use of multi-agent workflows. https://t.co/FXJPwoT2EQ
QUOTED @pvncher: https://t.co/hsvsflUPmf
--
T=2089391064184492138 | @omarsar0 | 2026-08-17T16:37+00:00 | L33 RT2 C11 V8046 | post
URL=https://x.com/omarsar0/status/2089391064184492138
TEXT: Grok Bot is so good! I am very impressed with all the recent updates on Grok models as well. 

If you ever wanted to try a different product outside Codex and Claude Code, Grok Bot is worth trying.
QUOTED @GavinSBaker: I think @bot is another “Claude Code” moment for AI.

I would estimate my personal AI usage is up something like 100x.

And for everyone who reached out about how to build a “podcast summarizer” it took me about 15 seconds in Grok Bot and is better than what I had before. https://t.co/AaoeHbEqtl
--
T=2089411994499903566 | @omarsar0 | 2026-08-17T18:00+00:00 | L135 RT17 C13 V9858 | post
URL=https://x.com/omarsar0/status/2089411994499903566
TEXT: Recommended paper for agent skill builders.

There are 56,804 public agent skills today, all competing for fewer than 100 reliable trigger slots in the system prompt. Your own playbooks compete for that same space, and the long tail never gets used.

skills separates the three things installation bundles together. Content, persistence, and automatic triggering. Only triggering needs to sit in the prompt.

A path addresses any skill, subtree, or collection, and reading it is enough to use it. A directory becomes a menu, so bundles stop being all-or-nothing. Vendoring copies a skill into your Git tree at the same path, so your team owns and adapts it.

No manifest, no lockfile, no registration, and SKILL.md is unchanged.

Paper: https://t.co/Dq8Mf0SVK0

Track more trending AI papers in our academy: https://t.co/1e8RZKs4uX
LINKS: https://arxiv.org/abs/2608.12610 ; https://academy.dair.ai/
--
T=2089418707202084991 | @omarsar0 | 2026-08-17T18:26+00:00 | L21 RT1 C4 V6473 | post
URL=https://x.com/omarsar0/status/2089418707202084991
TEXT: It has been a bit surprising, to say the least, how powerful LLMs for code have turned out to be in unlocking general capabilities. 

Diffusion models are going to have their moment soon, but I expect LLMs to continue to improve and transcend.
QUOTED @trq212: all of the recent proc gen art, video editing and 3d game demos recently have made me update towards LLM coding models being better at a lot of creative work than diffusion models
--
T=2089460996045676882 | @omarsar0 | 2026-08-17T21:14+00:00 | L40 RT6 C3 V7055 | post
URL=https://x.com/omarsar0/status/2089460996045676882
TEXT: Recommended resource. Largest dataset of agent skills I’ve come across. Great for mining cool ideas and patterns for your agents.
QUOTED @dair_ai: How many agent skills are actually out there?

There are ~3.8M SKILL.md files across 282,200 public GitHub repositories, nine months after Anthropic published the format as an open spec.

This research mined all of them into a dataset.

Skills resist the usual software mining. They are written in natural language, an agent picks them probabilistically at run time, and no compiler or type checker verifies the choice. There is no registry and no package manager, so they spread by copying folders b
--
## @rasbt — 1 шт.

T=2089527404138033497 | @rasbt | 2026-08-18T01:38+00:00 | L4 RT0 C2 V2006 | post
URL=https://x.com/rasbt/status/2089527404138033497
TEXT: Clarification here. Somewhere in the comments, I agreed that one might have to rerun the LLM for checking for watermarks. That's not correct.

I am not 100% which exact technique they use, but they mentioned that they base their method on the SynthID-Text method from https://t.co/1YdFP3vnNQ

So, in that method, they have so-called watermarking functions that give 1’s for certain terms and 0’s for others, and then they do a tournament-style selection. 

Those that survive have a lot of 1’s, i.e., are high-scoring.
So, to later check if a text is watermarked, they basically just have to (re)apply the watermarking functions to some text and if it’s above a score threshold (which you reach if you have a lot of those watermark-words that score highly), then the text is likely watermarked.

I.e., you don’t need to rerun the LLM to check, just the “cheap” watermark functions (it’s kind of like hashing).
LINKS: https://www.nature.com/articles/s41586-024-08025-4
--
## @sh_reya — 2 шт.

T=2089188860085575957 | @sh_reya | 2026-08-17T03:13+00:00 | L6 RT1 C2 V2464 | rt
URL=https://x.com/sh_reya/status/2089188860085575957
RT-OF @vishal_learner (L6): trying this skill out on claude dot ai with opus 4.6 high and i'm liking it. too soon to understand why.
RT-URL=https://x.com/vishal_learner/status/2089179310947188971
TEXT: RT @vishal_learner: trying this skill out on claude dot ai with opus 4.6 high and i'm liking it. too soon to understand why.
--
T=2089361022620770740 | @sh_reya | 2026-08-17T14:37+00:00 | L1 RT1 C0 V377 | post
URL=https://x.com/sh_reya/status/2089361022620770740
TEXT: @vishal_learner Skills (and mcp) feel different from generic open source code in that skills pollute context windows, so one has to be careful about the skills they add to their agents
--
