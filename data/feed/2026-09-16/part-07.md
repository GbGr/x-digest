# X-FEED 2026-09-16 part 7/9 | items: 6

## @omarsar0 (продолжение)

T=2099933100440494105 | @omarsar0 | 2026-09-15T18:47+00:00 | L106 RT6 C6 V20829 | post
URL=https://x.com/omarsar0/status/2099933100440494105
TEXT: Recommended read. Jev gives up text generation to make AI dramatically faster.  

TypeSafe built a new architecture that answers structured questions in parallel, with RLCD training its probabilities to reflect how often it’s right.  

The team reports 40–200x faster responses on System One queries.
QUOTED @CompleteSkeptic: After co-inventing ChatGPT, I kept asking myself: why have superhuman chat models not led to AGI?

I’ve spent the last 2 years in stealth building a new way to train models (RLCD), and a new type of frontier AI model that we are releasing today: Jev

• 20-200x faster
• 40-400x cheaper (w/ output tokens free)
• Frontier composable intelligence optimized for decisions

AFAICT the shortest path to AI-based economic revolution
--
T=2099970990935867485 | @omarsar0 | 2026-09-15T21:17+00:00 | L53 RT6 C9 V9869 | thread(3)
URL=https://x.com/omarsar0/status/2099970990935867485
TEXT: I agree. MCP is clearly better than CLI for most integrations. It felt that way early on, and it still does now. And frontier models keep getting better at it. 

If you build custom harnesses, use MCP tools. 

My meta harnesses use MCP for all external tools.
[->] @germanburgardt I totally get that the vague posting isn't conducive to discussion. I'll take some time over the next few days to say more and share some detailed thoughts. I reacted because I have seen wider adoption of MCP across all sorts of domains.
[->] @germanburgardt No worries. I appreciate the pushback, tbh. I do see it as useful to discuss this more openly and share notes.
QUOTED @trq212: I was not expecting things to go this way, but I think MCPs are better than CLIs for most integrations. 

The models have gotten much better at tool calling, we can defer tools &amp; MCP is now stateless.

If you need to compose/filter data, add params like query to your MCP tools.
--
T=2100048882998636661 | @omarsar0 | 2026-09-16T02:27+00:00 | L44 RT3 C7 V7344 | post
URL=https://x.com/omarsar0/status/2100048882998636661
TEXT: Exactly! Let’s attack the safety problem with rigorous science and engineering. Great to see Jensen and more recently Mark bring some sense into this conversation. Not sure how we have allowed this alignment stuff to become so political and sci-fi. We need to go back to fundamentals. If your model or AI product by extension is unsafe/defective, it’s your responsibility to fix it.
QUOTED @DavidSacks: Jensen Huang: “Safety is paramount. In a lot of ways, it’s job one. However, safety is an engineering problem... If we’re not confident about the safety of the products — like all companies, like you and I, all the companies here — if you build a product or a service and you’re not confident in its functionality, capability, or safety, then don’t release it.
That’s a very obvious thing to do. You pace yourself until you are confident you’re releasing something that the market would appreciate. T
--
T=2100080746056777899 | @omarsar0 | 2026-09-16T04:34+00:00 | L53 RT6 C11 V4789 | post
URL=https://x.com/omarsar0/status/2100080746056777899
TEXT: Banger report from Salesforce.

Pretty interesting to see more of these custom enterprise models.

Salesforce trained the enterprise agent model from the same files it uses to configure agents.

Koa starts from the open-weight Nemotron-3-Super-120B.

Salesforce takes Agent Script specifications, the declarative files that define Agentforce agents, and expands them into multi-turn tasks with simulated user personas.

The reward checks whether the agent resolved the task with the right tool calls, and training uses GRPO.

The gains are modest and consistent.

Koa scores 69.41 on Tau2Bench against 68.64 for its base and 54.48 for GPT-4.1. On CRM Bench it reaches 0.86, close to Claude Opus 4.8 at 0.87, and function-call accuracy rises from 0.71 to 0.77.

If your company already describes its workflows in a structured format, those descriptions might be useful to turn into RL environments.

Paper: https://t.co/rXmmh6cbBN

Chat with Paper: https://t.co/JyURoT8IGj
LINKS: https://arxiv.org/abs/2609.15066 ; https://academy.dair.ai/papers/salesforce-koa-an-enterprise-language-model-for-agentic-tool-use-2609.15066
--
## @rasbt — 2 шт.

T=2099842037990236495 | @rasbt | 2026-09-15T12:45+00:00 | L10 RT2 C5 V5604 | post
URL=https://x.com/rasbt/status/2099842037990236495
TEXT: Potentially also related to the pacing, since fewer releases = fewer expenses
QUOTED @Polymarket: JUST IN: Anthropic says they’re highly profitable if you take out some of their biggest expenses.
--
T=2099846949377585659 | @rasbt | 2026-09-15T13:05+00:00 | L240 RT24 C46 V18226 | post
URL=https://x.com/rasbt/status/2099846949377585659
TEXT: Some food for thought when designing benchmarks...

So, here's a little computer-use (visual) comparison between GPT-5.6 Astra and Qwen3.8 Max.

The task here was to recreate the image in the center using the Paint UI. 

Super interesting how the two different LLMs+Harnesses approached this totally differently by default.

I.e., Astra tried to approach this by drawing and layering geometric shapes. Qwen approached this pixel by pixel. (Of course, the pixel-by-pixel result looks closer to the original, it's essentially a low-res version of that by nature.)

So, the Qwen-generated image would surely score higher in the sense that it's closer to the original.

But I wouldn’t conclude from this example that one LLM generalizes better than the other on other tasks. Also, I wouldn't say Qwen has better compute-use capabilities or better visual understanding than Astra.

But it highlights an interesting point about how slippery benchmarks are when they only compare final results.
--
