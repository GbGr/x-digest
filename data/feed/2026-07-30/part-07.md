# X-FEED 2026-07-30 part 7/9 | items: 6

## @omarsar0 — 7 шт.

T=2082451814461354397 | @omarsar0 | 2026-07-29T13:02+00:00 | L37 RT9 C3 V8786 | rt
URL=https://x.com/omarsar0/status/2082451814461354397
RT-OF @Evolvent_AI (L37): We recently released a project we’re especially excited about: RSIBench-Data.
Rather than asking whether an agent can solve another difficult task, RSIBench-Data asks a different question: can an agent work like a researcher—diagnosing model weaknesses, designing training data, refining post-training strategies based on feedback, and ultimately producing a better model?
Our experiments suggest that agents are already capable of autonomous research and meaningful strategy improvement. However, there is still a long way to go before they can achieve reliable recursive self-improvement. We hope RSIBench can provide an open and reproducible platform for measuring real progress toward that goal.
The project is now open source. We’d love your support and feedback—and if you’re a researcher at a model lab interested in testing your model, feel free to reach out. Send us the model, and we’ll take care of the rest 😁
Paper: https://t.co/ywAX2LCTfZ
Code: https://t.co/4gmT6uhgLc
Website: https://t.co/FAmtr7Q9wg
RT-URL=https://x.com/Evolvent_AI/status/2082327462193791237
TEXT: RT @Evolvent_AI: We recently released a project we’re especially excited about: RSIBench-Data.
Rather than asking whether an agent can solv…
LINKS: https://arxiv.org/abs/2607.25886 ; https://github.com/evolvent-ai/RSIBench-Data ; https://rsibench.co/
--
T=2082473005859446971 | @omarsar0 | 2026-07-29T14:27+00:00 | L10 RT1 C0 V8173 | post
URL=https://x.com/omarsar0/status/2082473005859446971
TEXT: Viktor reached $25M ARR in its first 16 weeks, fully self-serve, with essentially no sales team. 

I've watched this team closely, and their execution is impressive.

Now the operator who ran GTM for Dropbox, Asana, and Notion is joining @viktor__com as CRO. That's huge! Very cool to see how this team is scaling.
QUOTED @frydwia: Robbie took @NotionHQ, @asana and @Dropbox to market.

Then he took a year off, sat with Europe's top VCs, and watched the whole AI market from the investor side.

He could have joined any company in the world.

We're proud to announce he's joining https://t.co/mfL3pEAdBy as CRO.

The playbook for taking an AI employee to market doesn't exist yet. It's weird. Huge LTV on SMBs, and volatility all over the place. Nobody has written it.

Someone has to. Robbie is that someone.

Honored to be buildi
--
T=2082480019948122293 | @omarsar0 | 2026-07-29T14:55+00:00 | L123 RT32 C13 V10758 | post
URL=https://x.com/omarsar0/status/2082480019948122293
TEXT: Impressive paper!

It's on one of the hardest tasks for coding agents today.

Of course, I am talking about kernel optimization. Coding agents are usually not so great at this.

Reasons: Unfamiliar low-level API, no room for a plausible-looking answer, and every candidate has to actually run and be faster.

Kernel Forge is an open-source agent harness that takes an unmodified PyTorch model in place and rewrites its CUDA kernels. It covers vision, diffusion, and LLM workloads.

Instead of a linear generate-and-fix chain, it runs Monte Carlo Tree Search over multiple optimization paths, with a GUI for monitoring progress, inspecting candidate kernels, and debugging failures.

On an NVIDIA DGX Spark with a GB10 GPU, at 50 optimization iterations per kernel, it optimized 14 kernels past their PyTorch baselines across four models.

It looks like the gain came from harness structure and in-place reintegration rather than a stronger model. That lesson repeats for any agent working against an API it was never trained on.

Paper: https://t.co/kJrLL9wx2B

Learn to build effective AI agents in our academy: https://t.co/1e8RZKs4uX
LINKS: https://arxiv.org/abs/2607.24762 ; https://academy.dair.ai/
--
T=2082503558713290911 | @omarsar0 | 2026-07-29T16:28+00:00 | L34 RT2 C7 V8581 | post
URL=https://x.com/omarsar0/status/2082503558713290911
TEXT: Replit just launched Replit Design.     

Looks amazing!    

Designing is hard, and AI agents tend to generate mostly generic stuff. This will help tremendously.    

I like that Replit Design acts as a thoughtful design partner and suggests more personalized designs for your apps.
QUOTED @Replit: Introducing Replit Design.

The next era of design, for everyone. https://t.co/cLH5e1XAu5
--
T=2082550450373451938 | @omarsar0 | 2026-07-29T19:34+00:00 | L133 RT10 C30 V23316 | thread(2)
URL=https://x.com/omarsar0/status/2082550450373451938
TEXT: After a few more hours, I think I've figured out Opus 5.

Opus 5 is trained to be more agentic than anything I've used. All Claude 5 models are like that.

So what changes?

The way to interact with Opus 5 or contextualize it won't work the same way as with other models. 

It loves exploring, so it doesn't need much guidance for it. Unique preferences, artifacts, and references compliment it well and enable cleaner and more effective exploration and execution.

Now that it can explore more effectively on its own and understand intent better, the best thing to do is to get out of its way (e.g., it doesn't need examples of your preferences; a clear high-level description of it works best). It's truly agentic in that sense.

A good first step to provide better context for Opus 5 is to distinguish between what's situational and what needs persistence. 

Regardless, persistent system prompts and CLAUDE.MD needs to stay lightweight. Remove memories and tool descriptions from these. CLAUDE.MD is also a great place to tap into progressive disclosure by linking command/skills to it.

On the situational side, agent skills and auto-memory can leverage progressive disclosure and the improved ability of the model to use its external context/knowledge. Conflicting and unnecessary instructions, which are common at this layer (mainly to ensure reliability), are going to throw off this model easily. That's the biggest change I had to make. 

Simple, clean, and clear prompts and skills work best. 

I had to clean a lot of my skills and system prompts. The way I prompt remains the same (usually clear and well-scoped). MCP tool descriptions are also more descriptive and have been deduped from the system prompt. 

Anthropic released a guide on the new rules for context engineering, which was helpful here. I started to test the recommendations and created a little artifact with the things that worked along the way.

This might feel like a lot of work. Believe me, it has been frustrating. But I think we can expect future frontier models to become more agentic and smarter at figuring out the right context/gaps. The best thing to do is to prepare for that now. 

@bcherny mentioned that Opus 5 is their least prompt-injectable model yet. I am not sure if that was something they intentionally trained for or if it emerged based on how it was trained, which is to be extremely agentic in nature and more direct in execution.
[->] And let me know if the visual HTML artifact would be useful if I share it.
--
T=2082595872886358175 | @omarsar0 | 2026-07-29T22:35+00:00 | L80 RT16 C8 V7372 | rt
URL=https://x.com/omarsar0/status/2082595872886358175
RT-OF @dair_ai (L80): On benchmarking long-context agentic instruction following.

Agent benchmarks mostly reward reaching the answer. This new benchmark measures whether the agent reached it the permitted way, which is the question enterprise deployments care about.

If you ship skills files, policy documents, or long system prompts, you have been trusting that they actually bind agent behavior.

But how are you measuring all of this?

Surge AI built a benchmark to actually check this.

HANDBOOK.md places a standard operating procedure of 20 to 124 pages in context and grades whether it governed every action across an extended tool-use horizon. 65 tasks, five domains, ten fictional companies.

Each task runs in a self-contained company environment with a file workspace plus mock email, chat, calendar, issue-tracking, and commerce services exposed over MCP. Every task mutates one of ten base handbooks, altering the specific rules and thresholds that grading turns on, so memorization does not help.

Grading is fully deterministic and two-sided. 824 programmatic criteria check that required actions occurred and that prohibited actions did not.

Paper: https://t.co/qKA2z8R1rz

Learn to build effective AI agents in our academy: https://t.co/LRnpZN7L4c
RT-URL=https://x.com/dair_ai/status/2082488327379538219
TEXT: RT @dair_ai: On benchmarking long-context agentic instruction following.

Agent benchmarks mostly reward reaching the answer. This new benc…
LINKS: https://arxiv.org/abs/2607.25398 ; https://academy.dair.ai/
--
