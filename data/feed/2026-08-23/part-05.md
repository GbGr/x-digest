# X-FEED 2026-08-23 part 5/6 | items: 6

## @omarsar0 — 5 шт.

T=2091180120610312573 | @omarsar0 | 2026-08-22T15:06+00:00 | L214 RT8 C48 V17316 | thread(4)
URL=https://x.com/omarsar0/status/2091180120610312573
TEXT: Own your harness.

I really wish the Claude Code harness was open source. 

I often think about this, especially now that custom harnesses are foundational to AI-native companies.

I am now building mostly on top of Pi and Hermes Agent. Open-source harnesses are the future.
[->] With companies I collaborate with, I am seeing custom harnesses for evals, RL envs, research, design, coding, marketing, and so much more. 

I am noticing a lot of Harness Engineering, so I am putting together a set of best practices, tools, skills, and guides.
[->] Not much (technically speaking) is discussed about recursive self-improvement.

But I have a hunch that when we get there, it will be more obvious how important it will be to own your harnesses and models. This is why I am a strong believer in the open-source harness ecosystem.
[->] @xpasky I think Claude Code has done some things right, like the skill use, prompt caching, and the system prompt. I think it is really good; the interface/experience is also nice (not perfect but nice). Their agent loop with verification is probably the best, and the one I miss the most is the dynamic workflows command. Just a few I have in mind. For all of these, I built something for myself.
--
T=2091199978014458081 | @omarsar0 | 2026-08-22T16:25+00:00 | L122 RT17 C20 V9698 | post
URL=https://x.com/omarsar0/status/2091199978014458081
TEXT: What a fascinating paper on AI agents.

A lot of the issues we see with AI agents today revolve around wrong assumptions the LLMs make.

This leads to problems like hallucination, cost inefficiencies, unreliable tool calls and much more.

I think if we can solve this problem, even current LLMs would significantly improve in terms of performance and efficiency.

The problem is that context acquisition is treated as afterthought, but it shouldn't be that way.

Users tend to leave out constraints when prompting. So the agent agent needs to guess the default, or spend tokens on a clarifying question, a retrieval call, a tool call, or a prompt trial.

This new work gives this problem an objective function. Context acquisition becomes active inference over a latent task state. An inner step updates beliefs, and an outer step picks the next context action, task action, or stop action to minimize expected free energy under cost.

In deterministic settings the epistemic term reduces to expected information gain, optionally normalized by token cost. That is directly implementable today as a scoring rule.

They coin it as Optimal Question Asking, with exact posteriors and a dynamic programming oracle, then benchmark frontier models on binary and multiway tasks from 25 to 300 candidates. So you can measure the gap between your agent and the true optimum.

Paper: https://t.co/XKMXNeXRJU

Track more trending AI papers in our academy: https://t.co/1e8RZKs4uX
LINKS: https://arxiv.org/abs/2608.19202 ; https://academy.dair.ai/
--
T=2091206127417507972 | @omarsar0 | 2026-08-22T16:49+00:00 | L232 RT15 C11 V27901 | post
URL=https://x.com/omarsar0/status/2091206127417507972
TEXT: Recommended agent skill.

/eli5 works great for visualizing deep technical concepts! 

I find it speeds up my thought process and helps me collaborate better with agents. 

Try /eli5 with Pi and Ox Alpha in our harness playground: https://t.co/7ivyJJ9xu2 https://t.co/QCA1J9PBoG
QUOTED @trq212: a skill people at Anthropic have been using a lot recently: ELI5

/eli5 &lt;what you want explained&gt;

"explain like I'm someone who knows nothing about this topic, using a HTML artifact with big pictures and few words" https://t.co/OZqzjAyFdT
LINKS: https://academy.dair.ai/dashboard/playground
--
T=2091215131581497764 | @omarsar0 | 2026-08-22T17:25+00:00 | L59 RT8 C12 V6969 | rt
URL=https://x.com/omarsar0/status/2091215131581497764
RT-OF @dair_ai (L59): Banger paper from Microsoft.

It's on agent reliability in real business workflows.

(bookmark it)

Thinkingbox is a sandbox with isolated MCP-compatible tool sessions, plus a benchmark of 507 policy-conditioned workflows across retail, hospitality, auto insurance, neobank IT, and consulting support.

Every attempt is graded on the backend state the agent leaves behind. Executable checks accept valid trajectories and reject wrong, missing, or extra effects, so collateral damage counts against you.

The strongest model reaches 65.36% pass@1 and 25.25% pass^20.

Many failed trials terminate cleanly with valid state-changing tool calls. Watching the response or the tool call tells you very little about whether the task actually completed.

Paper: https://t.co/EkMhBafbvI

Track more trending AI papers in our academy: https://t.co/LRnpZN7L4c
RT-URL=https://x.com/dair_ai/status/2091209556122808532
TEXT: RT @dair_ai: Banger paper from Microsoft.

It's on agent reliability in real business workflows.

(bookmark it)

Thinkingbox is a sandbox w…
LINKS: https://arxiv.org/abs/2608.19741 ; https://academy.dair.ai/
--
T=2091276740815638911 | @omarsar0 | 2026-08-22T21:30+00:00 | L143 RT27 C16 V9192 | post
URL=https://x.com/omarsar0/status/2091276740815638911
TEXT: Great paper if you are tracking progress in recursive self-improvement (RSI).

(bookmark it)

There is so much hype around RSI, so I think it's worth understanding why current models are not able to do this properly yet.

Issues range from "lack of creativity" of models to getting stuck in a local optimum.

This work tries to provide more insights into whether agents can really post-train other agents.

Here is the most interesting finding reported in the paper: "the agent’s training strategy is locked in at the very beginning, and the entire remaining budget is spent on local adjustments within the selected strategy."

They analyzed a large corpus of publicly released post-training trajectories. Across tasks, the agent locks in its training strategy at the very first step and spends the entire remaining budget on local adjustments inside it.

They then tried three escalating fixes. An experience-driven scaffold lifted execution broadly, worth 12.6 points on GSM8K and 40.8 on HumanEval, and the strategy stayed frozen.

Human guidance redirected the opening choice, and the agent slid back into local loops once training began. Extra inference compute paid off on easy tasks and did almost nothing on the hardest one.

What agents lack here is a way to reconsider strategy while execution is still running.

Paper: https://t.co/3XJAfRYmtB

Track more trending AI papers in our academy: https://t.co/1e8RZKs4uX
LINKS: https://arxiv.org/abs/2608.19072 ; https://academy.dair.ai/
--
## @rasbt — 1 шт.

T=2091153701155029117 | @rasbt | 2026-08-22T13:21+00:00 | L284 RT56 C27 V23595 | thread(2)
URL=https://x.com/rasbt/status/2091153701155029117
TEXT: Here's a link to the video + slides + transcript: https://t.co/nWpIrEb21O
[->] A couple of days ago, I did a quick explainer on Claude’s new watermarking process and implementation. Since it’s such a popular topic and sparked such a lively discussion, I thought it might be interesting to go into a bit more detail when explaining how it works.

So, instead of the usual text article, I recorded a little lecture on the topic (to change it up a bit from my usual articles). 

It ended up a bit longer than intended, but I hope it clarifies a lot of things:

- Sampling the next token in an LLM and pseudorandom number generators
- How watermarking relates to the regular LLM sampling process
- Whether watermarking makes text "worse"
- How to remove watermarks
- Tournament sampling
- How new text is checked for watermarks without rerunning the LLM

I ended up with ~50 slides, but I hope that these explain it well, though! Happy watching!
LINKS: https://magazine.sebastianraschka.com/p/claude-watermarking
--
