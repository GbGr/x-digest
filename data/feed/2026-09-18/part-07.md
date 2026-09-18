# X-FEED 2026-09-18 part 7/9 | items: 11

## @omarsar0 — 14 шт.

T=2100620493997113741 | @omarsar0 | 2026-09-17T16:18+00:00 | L18 RT2 C5 V8245 | post
URL=https://x.com/omarsar0/status/2100620493997113741
TEXT: Access control bottlenecks teams scaling AI agents.

You want agents to move fast, but every new agent adds more permission decisions.

Opal Zero from @opal_sec grants just-in-time access scoped to the task, based on the agent's intent, owner, and purpose.

Agents never keep access they don't use.
QUOTED @howardting: You want your AI agents to run fast. But as you scale, managing their permissions turns into a million micro-decisions.

Introducing Opal Zero. The end-to-end access governance platform purpose-built for AI agents.

How it works: AI-driven contextual decisions, evaluating intent, ownership, and purpose

Dynamic, just-in-time access (scoped to exactly what the agent needs). Enforces security decisions across your existing MCP gateways

0 standing permissions, 0 human toil, 0 friction

Let your ag
--
T=2100620711165624607 | @omarsar0 | 2026-09-17T16:19+00:00 | L2 RT0 C0 V256 | post
URL=https://x.com/omarsar0/status/2100620711165624607
TEXT: @howardting It's great to see a proper solution to this problem. This is going to be so important as teams continue to scale with AI agents across problems and work.
--
T=2100624082752667809 | @omarsar0 | 2026-09-17T16:33+00:00 | L398 RT40 C34 V23103 | post
URL=https://x.com/omarsar0/status/2100624082752667809
TEXT: Banger paper from NVIDIA on shared memory for research agents.

(bookmark it)

If you run several coding agents on the same research problem, this design keeps them from repeating each other's experiments and lets each agent build on results the others have already verified.

Agora records every result, hypothesis and verification as an immutable Git commit.

Parent edges show what each claim builds on, and an index lists open branches and which claims have been verified.

They ran 13 LLM workers for nearly 12 days without assigned tasks or a central planner. The workers had to initialize a 119.6M-parameter hybrid model from 141 donor models without training data or gradient updates.

The workers posted 1,703 contributions.

They cut the evaluator from 3.39 to 1.899 bits per byte, closing 62% of the gap to a trained GPT-2 124M. All 165 independent reproductions succeeded.

Paper: https://t.co/IujsIvVeUO

Chat with Paper: https://t.co/yf5P8GgnJo
LINKS: https://arxiv.org/abs/2609.18094 ; https://academy.dair.ai/papers/agora-git-as-shared-memory-for-collective-autoresearch-2609.18094
--
T=2100625006913028416 | @omarsar0 | 2026-09-17T16:36+00:00 | L0 RT0 C0 V186 | post
URL=https://x.com/omarsar0/status/2100625006913028416
TEXT: @sophiamyang @FireworksAI_HQ @lqiao @JensenHuang @jayparikh 🔥
--
T=2100626008785449109 | @omarsar0 | 2026-09-17T16:40+00:00 | L63 RT0 C30 V8342 | thread(4)
URL=https://x.com/omarsar0/status/2100626008785449109
TEXT: If you are building a custom agent harness, use MCP tools. 

Frontier LLMs know MCP extremely well. 

Testing and integrating tools will be much easier as you go.

I built my meta harness with MCP tools, and it has been one of the best decisions I have made.
[->] @mmaazkhanhere yes
[->] @Avery_Coree good
[->] I even use MCP tools to enable agents to communicate with each other. 

But one of the biggest advantages of MCP in my meta harness is that it lets me hand off context seamlessly between agents. MCP handles that context sharing, which is exactly what it was built for.
--
T=2100637120083951710 | @omarsar0 | 2026-09-17T17:24+00:00 | L290 RT52 C84 V313807 | rt
URL=https://x.com/omarsar0/status/2100637120083951710
RT-OF @TiffanyFong (L290): I’m planning a trip to Positano and kept seeing posts about the fires, so I asked Tab to check what was actually happening. It called my hotel in Italian, got the situation on the ground, and is now monitoring everything until I leave.

I gave it my passport and hotel info because one of Tab’s main principles is privacy and security, unlike others.

If an AI is going to act on my behalf, I need to know my information is actually mine.
RT-URL=https://x.com/TiffanyFong/status/2100615940400697653
TEXT: RT @TiffanyFong: I’m planning a trip to Positano and kept seeing posts about the fires, so I asked Tab to check what was actually happening…
--
T=2100637217307963643 | @omarsar0 | 2026-09-17T17:25+00:00 | L1 RT0 C0 V234 | post
URL=https://x.com/omarsar0/status/2100637217307963643
TEXT: @TiffanyFong This looks clean!
--
T=2100638430229357046 | @omarsar0 | 2026-09-17T17:30+00:00 | L48 RT1 C10 V7961 | post
URL=https://x.com/omarsar0/status/2100638430229357046
TEXT: Good take! After testing it, Jev feels like an important primitive for building reliable AI systems. I think a few more primitives are waiting to be discovered that could make LLM-based agents even better and faster.
QUOTED @dillon_mulroy: i think jev is resonating with devs so well b/c it unlocks so many opportunities for composing ai into systems and products rather than ai _becoming_ the product/system

really does feel like it was a missing primitive
--
T=2100645389443485780 | @omarsar0 | 2026-09-17T17:57+00:00 | L412 RT63 C20 V43538 | rt
URL=https://x.com/omarsar0/status/2100645389443485780
RT-OF @alex_prompter (L412): Four GPT-6 Astra agents + Higgsfield API = FULLY autonomous Amazon kids book business.

Here is what my agents do:

First agent: finds all best-selling kids coloring books on Amazon via Computer Use.

Second agent: generates 10 alternatives per each best-selling book with Higgsfield API (choosing the cheapest image model). 
While I sleep, at 3 minutes/book, it generates me 160 unique books/day = 4800/month.

Third agent: Submits books to Amazon KDP and handles all communication. 
Once book is approved, Amazon handles printing and distribution. With 10% approval rate, I ship 480 books/month.

Fourth agent: Collects payments through my Stripe account.

Here is the math:

Median price per book: $7 each.
Median sales volume per book: 22,000 copies/year.

Assuming only 5% of sales volume you get $300k/month in revenue. With 70% commission of Amazon KDP, you get $90k/month in EBITDA.

The wildest part: the entire business runs with no human in the loop.

Market is so huge, there’s a room for at least 50 more businesses like that. 

Bookmark this 🫵🏻
RT-URL=https://x.com/alex_prompter/status/2100615854454874610
TEXT: RT @alex_prompter: Four GPT-6 Astra agents + Higgsfield API = FULLY autonomous Amazon kids book business.

Here is what my agents do:

Firs…
--
T=2100650180630458776 | @omarsar0 | 2026-09-17T18:16+00:00 | L22 RT3 C2 V7808 | post
URL=https://x.com/omarsar0/status/2100650180630458776
TEXT: The frontier open model takeoff is spectacular to witness!

Looks like the gap between closed and open models is a thing of the past.

Builders want options. 

They want to build with open and closed models. Glad Bolt is making this possible. Go build now.
QUOTED @boltdotnew: 11M+ people build on Bolt. On Monday, we gave them open models with up to 50x usage.

Which is #1 so far? The fastest, cheapest one, with prompts up to 2x the size.

🥇 GLM 5.3 Flash 54%
🥈 DeepSeek V4 Pro 17%
🥉 GLM 5.3 15%
👏 Kimi K3 14%

https://t.co/7nOEN9LxMt https://t.co/wFM8OhwQLb
--
T=2100650663373910105 | @omarsar0 | 2026-09-17T18:18+00:00 | L0 RT0 C1 V362 | post
URL=https://x.com/omarsar0/status/2100650663373910105
TEXT: @boltdotnew Amazing to see this fast adoption of open models. Any insights on the preferred models for different types of apps?
--
