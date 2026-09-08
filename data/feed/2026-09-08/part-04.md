# X-FEED 2026-09-08 part 4/5 | items: 8

## @omarsar0 — 8 шт.

T=2096936977459241352 | @omarsar0 | 2026-09-07T12:21+00:00 | L86 RT20 C16 V9067 | rt
URL=https://x.com/omarsar0/status/2096936977459241352
RT-OF @dair_ai (L86): // Evaluating and Improving LLM Self-Modeling //

Really interesting paper.

Can a model answer questions about its own behavior?

The questions are deliberately verifiable, such as whether a particular prompt edit would change the model's final answer. This framing avoids the usual trap where introspection claims cannot be checked by anyone.

Current models show real but limited skill on a new benchmark covering diverse self-modeling question types, and they make consistent errors on simple counterfactuals about themselves.

A scalable synthetic-data pipeline plus reinforcement learning raises the aggregate score across three open-source model families, with some transfer to held-out tasks.

The authors then decline the interpretation their own result invites. They note the gains may not come from privileged access to the model's internal decision process, so a better self-modeling score is not evidence of introspection.

Useful if you want agents that predict their own failures well enough to route or escalate, since that capability can now be measured without settling what produces it.

Paper: https://t.co/a3uIuITe8s
RT-URL=https://x.com/dair_ai/status/2096871139184451647
TEXT: RT @dair_ai: // Evaluating and Improving LLM Self-Modeling //

Really interesting paper.

Can a model answer questions about its own behavi…
LINKS: https://academy.dair.ai/papers/evaluating-and-improving-llm-self-modeling-2608.30980
--
T=2096972099394928951 | @omarsar0 | 2026-09-07T14:41+00:00 | L131 RT9 C22 V41356 | thread(3)
URL=https://x.com/omarsar0/status/2096972099394928951
TEXT: This is insane! 

GPT-6 Astra built this beautiful math animation in one go! (🔉 sound on)

"Jaw-on-the-floor" moment. 

I've not been able to get anything close to this with previous AI models. 

True personalized learning has arrived! https://t.co/x2oQEJlAbi
[->] I gave it an ElevenLabs API key, and it just figured out the rest. I am mindblowned. 

Scenes are all customizable. It's all code. So color theme can be changed for instance. 

I will be generating more of these to see how far math animations can be pushed. https://t.co/I8Jj4QFl3L
[->] The takeaway here is that you can't be afraid to give Astra access to tools. This model feels like it has no limits. Everything you had done before and failed, you should be trying again with it.
--
T=2096983084956852537 | @omarsar0 | 2026-09-07T15:25+00:00 | L230 RT35 C23 V18058 | post
URL=https://x.com/omarsar0/status/2096983084956852537
TEXT: // Design Docs Are All You Need //

Banger paper from Google DeepMind, MIT, and colleagues.

What a genuinely strange and interesting paper this one is.

Here is the setup:

They maintain a performance-modeling library whose main branch contains almost no code.

The repository is a directed graph of natural-language design docs. Coding sub-agents regenerate the entire implementation from those docs whenever a version updates.

Every human change is an edit to a doc.

The premise is that ML performance modeling invalidates its own abstractions every hardware and model generation, and coding agents are now cheap enough that regenerating a library beats patching one.

Two things make the regeneration reliable. The design docs are written around step-by-step worked examples, which act as in-context demonstrations for the generating agents. The system is also anchored on a minimal recursively defined operator IR with symbolic cost expressions in SymPy.

Regenerated implementations reproduce hand-audited reference models to round-off precision, including DeepSeek-V3 serving on a TPU pod slice.

Paper: https://t.co/l9Uv8JZ4GX
LINKS: https://academy.dair.ai/papers/design-docs-are-all-you-need-an-ai-native-machine-learning-performance-tool-2609.05364
--
T=2097009156901294510 | @omarsar0 | 2026-09-07T17:08+00:00 | L124 RT14 C16 V12604 | thread(2)
URL=https://x.com/omarsar0/status/2097009156901294510
TEXT: View it here: https://t.co/4oQLNAjWhC

Let me know what you think. I will continue to explore this more in the coming days.
[->] Testing GPT-6 Astra on visualizing popular AI papers. 

Started with this beautifully generated interactive version of the Transformer paper. 

This unlocks new ways to explore research. https://t.co/wkGknbFH5t
LINKS: https://academy.dair.ai/resources/attention-is-all-you-need-interactive-paper
--
T=2097029441729831259 | @omarsar0 | 2026-09-07T18:29+00:00 | L135 RT3 C13 V23999 | thread(4)
URL=https://x.com/omarsar0/status/2097029441729831259
TEXT: OMG!!!

Using GPT-6 Astra to animate fundamental concepts. It produced this entire clip.

I wish I had GPT-6 Astra when I was learning this stuff.

This really changes personalized learning. https://t.co/GMdMkJaVmK
[->] I haven't checked that it all checks out, but I think this sort of stuff needs verification. But all of it is customizable and generated in code, so that's a huge win. You can just use the model to make modifications as you go.
[->] With everything put together, it feels like less slop and something I would sit and watch.
[->] GPT-6 Astra takes about 30-60 minutes to generate these. It has nice verification steps that it uses to make sure things don't look off. I think most people won't understand how insanely difficult this is to build from scratch. AI models just weren't able to do this well in my previous test. GPT-6 Astra is the first model that goes over the threshold I was looking for.
QUOTED @omarsar0: This is insane! 

GPT-6 Astra built this beautiful math animation in one go! (🔉 sound on)

"Jaw-on-the-floor" moment. 

I've not been able to get anything close to this with previous AI models. 

True personalized learning has arrived! https://t.co/x2oQEJlAbi
--
T=2097053863463268376 | @omarsar0 | 2026-09-07T20:06+00:00 | L41 RT6 C13 V6464 | rt
URL=https://x.com/omarsar0/status/2097053863463268376
RT-OF @dair_ai (L41): // From Language Models to World-Acting Systems //

A critical review of agentic AI, and a framework that is genuinely useful for deciding how much authority to hand an agent.

Here is how it works.

The review separates three things the field routinely treats as one. Model competence, harness integration, and the authority a deployment actually grants are pulled apart and assessed separately.

Evidence gets organized along delegated authority, temporal persistence and environmental coupling, and the model, the harness and the environment stay distinct when a result is attributed.

The finding across the papers examined is that expansion of action interfaces is documented far more convincingly than robust completion, recovery, authorization or independent verification. MCP and Agent2Agent improve interoperability without establishing that delegation is trustworthy. Multi-agent organization buys specialization along with cost and correlated failure.

Paper: https://t.co/u6g80V2hpC
RT-URL=https://x.com/dair_ai/status/2097022152088445034
TEXT: RT @dair_ai: // From Language Models to World-Acting Systems //

A critical review of agentic AI, and a framework that is genuinely useful…
LINKS: https://academy.dair.ai/papers/from-language-models-to-world-acting-systems-progress-and-limits-of-agentic-ai-a-2609.04894
--
T=2097059598960132110 | @omarsar0 | 2026-09-07T20:29+00:00 | L2439 RT123 C67 V154897 | thread(2)
URL=https://x.com/omarsar0/status/2097059598960132110
TEXT: A few days ago, Anthropic shared this brilliant prompt. 

I was surprised by how it significantly improved writing with Fable 5.1.

Even more surprising, it also improved writing for GPT-5.6 Sol. 

I have it as a rule everywhere I use AI for editing/writing. https://t.co/rlXZPmzcz5
[->] I also wrote a little interactive tutorial if you want to test it yourself.

I highly recommend that you try it at least once and pay close attention to the output improvement. 

https://t.co/OY7C1Pf1qR https://t.co/iR6o9hWRQl
LINKS: https://academy.dair.ai/resources/write-better-with-claude-fable-5-1
--
T=2097077895277539493 | @omarsar0 | 2026-09-07T21:41+00:00 | L318 RT247 C31 V48620 | rt
URL=https://x.com/omarsar0/status/2097077895277539493
RT-OF @gpumaxxer (L318): we reached AGI. Higgsfield is using GPT-6 Astra to make N3on stream forever.

we’re testing a new feature on @higgsfield_ai: endless AI livestreams.

new video gets generated as you watch. there’s always a next moment.

AGI is here and its first job is being N3on. https://t.co/sFZSaA5yQC
RT-URL=https://x.com/gpumaxxer/status/2097023467694793211
TEXT: RT @gpumaxxer: we reached AGI. Higgsfield is using GPT-6 Astra to make N3on stream forever.

we’re testing a new feature on @higgsfield_ai:…
--
