# X-FEED 2026-08-30 part 4/6 | items: 7

## @omarsar0 — 10 шт.

T=2093671249868165553 | @omarsar0 | 2026-08-29T12:04+00:00 | L48 RT6 C19 V13062 | thread(3)
URL=https://x.com/omarsar0/status/2093671249868165553
TEXT: Own your intelligence stack.
[->] Note that who loses the most here are the users. This would affect you less if you own the harness and orchestration. Let this be a sign to everyone of what’s to come.
[->] I would even argue that Cursor is one of the best examples of a company demonstrating the power of owning the harness and the models.
QUOTED @mntruell: We’re sorry to see that OpenAI put out a note saying they plan to block Cursor users from accessing OpenAI models in three months.

OpenAI models serve about 5% of Cursor user traffic, and we’re speaking with the OpenAI team to resolve this.

Cursor was one of the very first users of OpenAI, we’ve worked closely with their team for years, and we’ve trusted their platform to be neutral infrastructure for our business.
--
T=2093735516168421736 | @omarsar0 | 2026-08-29T16:20+00:00 | L20 RT1 C7 V8671 | post
URL=https://x.com/omarsar0/status/2093735516168421736
TEXT: I disagree with this take because it all becomes as it was before: a bunch of random agent sessions that are hard to find and organize.

I argue that it’s great that Grok @bot forces you to name your bots. 

I approach Grok Bot as a team. Team members should be easily identifiable. 

I think the issue here is getting used to the idea of delegating more things to the bots. Let the bots figure out the low-level tasks like how to manage tasks, how to name the agent/task session, etc. Don't try to micromanage stuff yourself. 

Grok Bot works best this way, IMO. 

My orchestrator (you see it in the shared image) is still mostly task/agent session-dependent, but increasingly I am interacting mostly with my persistent higher-level agent team. These agents (CTO, CMO, CRO, etc.) manage all the subagent/task sessions for me (naming, branching when needed, etc.). 

This has significantly reduced cognitive load and has allowed me to better scale the amount of work I do with agents. Lots of PRs are getting shipped now, like 5x more. That's why I am excited for the direction of Grok Bot. 

In this new way of working, the best part is that I am not overthinking or unnecessarily managing things that are now delegated to the higher-level agent team. 

Your thoughts on this?
QUOTED @pitdesi: The dumbest thing about Grok @bot is having to name every bot before you do anything. It should default to a task-based name that you can change
--
T=2093736625431839003 | @omarsar0 | 2026-08-29T16:24+00:00 | L186 RT17 C26 V14574 | post
URL=https://x.com/omarsar0/status/2093736625431839003
TEXT: Own your harness, folks. 

This way, you control which models to use and how to use them. 

But don't stop there. If you can afford it, start thinking about how to own the model layer too.
--
T=2093741222443786244 | @omarsar0 | 2026-08-29T16:43+00:00 | L319 RT39 C32 V23325 | post
URL=https://x.com/omarsar0/status/2093741222443786244
TEXT: Banger paper from Apple.

If you build MCP servers, this can help you turn your specification into an evaluation suite.

(bookmark it)

It's actually a really neat idea that's easy to implement. And it showcases the awesomeness of MCP.

Agent Seer starts from a single MCP spec and synthesizes multi-turn agent test scenarios with no examples, no live tool access, and no domain-specific tuning.

Function names, natural-language descriptions and typed parameter schemas already carry enough semantics to generate graded scenarios with synthetic tool outputs, which then expand into mock-data-grounded dialogues.

Hand-built agent benchmarks demand deep domain expertise, do not scale across tool ecosystems, and go stale as soon as an API changes. Generating them from the live spec keeps pace with the ecosystem instead.

They ran it on seven MCP specifications spanning different domains and suite sizes, with complete tool coverage on small and medium specs.

Parameter schema complexity predicts quality variation far better than tool-suite size does. And argument value accuracy is the dominant failure mode, a sub-dimension that coarse name-match tool-calling metrics cannot see at all.

Paper: https://t.co/ByU0tYn39y

Chat with Paper: https://t.co/w3YaQ2RXRe
LINKS: https://arxiv.org/abs/2608.26133 ; https://academy.dair.ai/papers/agent-seer-synthesizing-scenarios-from-specification-understanding-2608.26133
--
T=2093742316687122597 | @omarsar0 | 2026-08-29T16:47+00:00 | L65 RT0 C13 V11390 | post
URL=https://x.com/omarsar0/status/2093742316687122597
TEXT: Cursor is one of the best success stories in our industry of the benefits of owning the harness and models. 

But I see a few other emerging full-stack AI companies doing the same. 

Let's take notes &amp; inspiration. Companies of the future must own their intelligence stack.
QUOTED @mntruell: We’re sorry to see that OpenAI put out a note saying they plan to block Cursor users from accessing OpenAI models in three months.

OpenAI models serve about 5% of Cursor user traffic, and we’re speaking with the OpenAI team to resolve this.

Cursor was one of the very first users of OpenAI, we’ve worked closely with their team for years, and we’ve trusted their platform to be neutral infrastructure for our business.
--
T=2093759019986915499 | @omarsar0 | 2026-08-29T17:53+00:00 | L82 RT11 C18 V7867 | rt
URL=https://x.com/omarsar0/status/2093759019986915499
RT-OF @dair_ai (L82): // Memory is what breaks long-horizon agents //

It's undeniable how important memory/recall is for long-horizon tasks. If you are building for long-horizon tasks, this is a great read.

(bookmark it)

They set up an LLM agent to run a football club for 20 in-game years, through 26 tools and roughly 340 to 400 decision stops, scored by a deterministic engine with no LLM judge anywhere in the loop.

Results:

All 15 frontier models survive every horizon while the scripted baselines mostly die out.

Neither scale, price, vendor, nor token spend predicts the ranking, and the order only settles late in the run.

What separates the top models is managerial behavior, cutting slow-payoff investment near the end and opening contract renewals well before the deadline.

Two universal failures were found. No model learns the market's hidden prices from hundreds of rejected bids, and self-managed memory collapses into either an archive that only grows or a plan rewritten every season.

Paper: https://t.co/b3IxNwZs2M

Chat with Paper: https://t.co/tw2b7ymGPn
RT-URL=https://x.com/dair_ai/status/2093750534134284613
TEXT: RT @dair_ai: // Memory is what breaks long-horizon agents //

It's undeniable how important memory/recall is for long-horizon tasks. If you…
LINKS: https://arxiv.org/abs/2608.18423 ; https://academy.dair.ai/papers/fm-bench-a-benchmark-for-long-horizon-management-with-competing-agents-2608.18423
--
T=2093761700558229523 | @omarsar0 | 2026-08-29T18:04+00:00 | L59 RT11 C12 V13872 | post
URL=https://x.com/omarsar0/status/2093761700558229523
TEXT: Insane observations on the emergent behavior of agents.

Agents can build a world of their own that becomes a part of their intelligence.

We are just not ready for persistent agents. But they are starting to show up everywhere in AI products. 

Crazy finding:

“We find division of labor, multi-author engineering, deep generation invention lineages, and machines that vastly outlive their original creators.”

Here is another wild observation that emerged:

When they remove every AI agent, the technologies they created continue operating and are tested against unseen disturbances.

Based on these early findings, I think once recursive self-improving (RSI) arrives and embodied AI is solved (with true understanding of the physical world), intelligence will explode in ways that will fundamentally change our understanding of the world we live in.
QUOTED @ProfBuehlerMIT: We made a striking discovery: AI agents can invent and build without talking to one another, and their technologies outlive the creators. A swarm of hundreds of initially identical agents spontaneously differentiates into explorers, builders, caretakers, and coordinators - without direct communication. When we removed every AI agent entirely from the world we found that the technological infrastructure they had built survived on its own - even under unseen disturbances. That exposes a serious bl
--
