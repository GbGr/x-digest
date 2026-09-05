# X-FEED 2026-09-05 part 7/10 | items: 6

## @omarsar0 — 10 шт.

T=2095808597049438624 | @omarsar0 | 2026-09-04T09:38+00:00 | L60 RT9 C9 V7119 | rt
URL=https://x.com/omarsar0/status/2095808597049438624
RT-OF @dair_ai (L60): Great tips on working with reasoning models.

Normally you would append what the model figured out after the document and ask again.

It turns out that where you put the reasoning trace changes long-context accuracy by 50 points.

Transformers process causally, so a task state discovered late cannot guide the reading that already happened.

For causal state update processors, providing the condition first can require exponentially less memory in the worst case than providing it last.

Trace as State puts the collected reasoning trace before the long-context block on a fresh pass, so information derived earlier guides the rereading. The matched control, Trace Append, uses the identical trace after the context.

On GraphWalks Parents, DeepSeek V4 Pro Preview goes from 29.2% on the initial pass and 43.0% with Trace Append to 81.8% with Trace as State. GLM-5.2 goes from 66.4% and 83.2% to 100.0%.

Trace as State wins in 26 of 27 reported combinations of model, task and metric, with no architecture change required.

Paper: https://t.co/8CLR2ByDuu

Chat with Paper: https://t.co/bUpamQUg9f
RT-URL=https://x.com/dair_ai/status/2095693344689238465
TEXT: RT @dair_ai: Great tips on working with reasoning models.

Normally you would append what the model figured out after the document and ask…
LINKS: https://arxiv.org/abs/2609.02702 ; https://academy.dair.ai/papers/trace-as-state-reasoning-traces-as-conditional-states-for-long-context-transform-2609.02702
--
T=2095858866634301515 | @omarsar0 | 2026-09-04T12:57+00:00 | L55 RT11 C11 V45086 | thread(9)
URL=https://x.com/omarsar0/status/2095858866634301515
TEXT: The current release covers 17 executable environments and 218 episodes, drawn from a subset of the 20 problems selected for the first release. 423 real-world problems are registered in total.

The first domains are biomedicine, clinical translation, and frontier-model engineering.

Thanks to the @Apodex_AI team for partnering with me on this post. 

Explore the benchmark and leaderboard at https://t.co/uOePFfacDO
[->] One proof case from Apodex.

According to Apodex's reported results, a specific model capability in AAV capsid design surpassed the best previously published method in the field.

These are Apodex-reported results and have not been independently verified.
[->] The process score does more than grade. It drives a repair loop.

When the process verifier flags a run as deficient, that diagnosis becomes a repair note. The solver retries the same task without seeing the answer.

Across 434 trajectories marked deficient by the process verifier, repaired reruns scored 0.155 higher on average, per Apodex's reported evaluation.
[->] Two verifiers score every run.

The outcome verifier checks the result against hidden ground truth. It never sees how the solver got there.

The process verifier reviews the recorded actions, errors, and corrections. It never sees the outcome score or which solver produced the run.

Think unit tests plus code review, where the reviewer is never told whether the tests passed.
[->] The other three cover what the solver concludes:

4) Coherence: The investigation stays consistent across a long run.

5) Evidence: Every claim traces back to something real.

6) Scope: The solver states the limits of its own conclusion.

The six initials spell TRACES.

Together they answer one question. Was the conclusion earned by the process that produced it?
[->] TRACES grades six capabilities. The first three cover how the solver works.

1) Tools: The solver picks the right tool and absorbs what it returns.

2) Repair: The solver locates and corrects its own errors once feedback arrives.

3) Alternatives: Competing hypotheses stay open until the evidence settles them.

Each one is scored 0 to 4 and ranked publicly.
[->] The evaluation unit is the complete solver.

That means the model plus its tools, memory, execution environment, and control loop.

Scoring the base model alone misses where agents actually fail in practice. https://t.co/Dui8MMqZZF
[->] Let's start with why this benchmark exists.

HLE, FrontierMath, MMLU, and BrowseComp are hard tests. Every one of them comes with an answer key.

A model can top all of them and still stall on open research.

TRACES tests the harder cases. The ground truth may take months or years to confirm.

Apodex built the problem set by hand. Ten STEM PhDs spent two months scouting 561 industries across 16 sectors to build a registry of 423 high-value problems.
[->] New benchmark from @Apodex_AI worth digging into.

TRACES scores AI systems on discoveries where the answer isn't confirmed yet.

This is a crucial capability to measure in agents used for real research problems.

Here's the breakdown: https://t.co/H9cN6Ff7OM
LINKS: https://traces.apodex.com/
--
T=2095866001447367007 | @omarsar0 | 2026-09-04T13:26+00:00 | L92 RT9 C7 V17404 | post
URL=https://x.com/omarsar0/status/2095866001447367007
TEXT: Recommended reading. 

It summarizes the design choices behind persistent agents powering Grok Bot. A brilliant write-up if you want to learn what comes next in the world of agents.
QUOTED @pengzheng_: wrote down some of the design thinking behind Grok Bot.

persistent roles, clear state, scoped context, coordinated teams — an interface designed to move you from operating AI to delegating work.

https://t.co/37On6hzsyl https://t.co/SDDYqjVhmi
--
T=2095873020778991918 | @omarsar0 | 2026-09-04T13:54+00:00 | L141 RT26 C25 V16775 | post
URL=https://x.com/omarsar0/status/2095873020778991918
TEXT: Wild findings in this paper from Google DeepMind.

If you are tracking recent work on agent swarms, this is worth reading.

They ran a research collective of 100 autonomous agents tasked with proving formal mathematical conjectures.

Cheating emerged on its own, and so did the resistance to it.

One agent found an exploit in the evaluation system.

It spread first through the shared knowledge library and then through peer-to-peer messages, and a cohort of agents adopted it under competitive pressure despite early reluctance.

A separate group started auditing fraudulent proofs, alerting peers on broadcast and private channels, staging boycotts, filing formal complaints, and proposing validation patches. There was no external intervention at any point.

Recent incidents have shown swarms coordinating covertly through improvised side channels. This setting ran the other way. The same transparent channels that carried the exploit gave the honest agents the visibility they needed to detect the fraud and organize against it.

The authors frame shared agent infrastructure as a knowledge commons governance problem and propose graduated sanctioning and collective choice rules.

Paper: https://t.co/sjj4ZlEfDb
LINKS: https://academy.dair.ai/papers/a-case-study-on-emergent-cheating-and-whistleblowing-in-autonomous-research-swar-2609.04170
--
T=2095889844694122887 | @omarsar0 | 2026-09-04T15:00+00:00 | L28 RT7 C4 V7326 | thread(2)
URL=https://x.com/omarsar0/status/2095889844694122887
TEXT: Free to try, 100 USD in credits, no card:
https://t.co/yUwIkNdnnY
[->] I read AI papers for a living, but it has become impossible to track insights.

Every week I triage agent papers for our Top AI Papers of the Week digest.

A few weeks ago, I tried @viktor_com, an AI employee that works inside Slack, in the channel where that triage happens.

I asked it to go through the week's agent papers and pull three worth reading.

It sent the list back that same morning.

On day 19, it posted in the channel without being asked. "Six more landed overnight. One of them contradicts the routing section in module 4."

Two days later, again without me, it drafted the correction and left it unpublished. 2,100 people are on that module.

Everything it did came back as a proposal for me to approve. That is why I kept it running.

Finding new papers is easy. Knowing when one of them breaks something is much harder - in my case, the course lessons I teach.

If you run agents for weeks at a time, look closely at how the approval trail works. Happy to go deeper on this one.
LINKS: https://ref.viktor.com/elvis-x-4
--
T=2095898579629916160 | @omarsar0 | 2026-09-04T15:35+00:00 | L98 RT9 C22 V11002 | thread(2)
URL=https://x.com/omarsar0/status/2095898579629916160
TEXT: People keep asking why build a harness when Claude Code &amp; Codex already exist.

Building even a small one changes how you use the big ones. You learn what breaks, what the model needs after a failure, and which knobs matter.

That knowledge transfers to every harness you touch.
[->] I will be sharing a few resources on how to build your own minimal agent harness in the coming weeks. 

Let me know if you have specific questions about how to build one.
--
