# X-FEED 2026-09-07 part 5/6 | items: 9

## @omarsar0 (продолжение)

T=2096662297707954398 | @omarsar0 | 2026-09-06T18:10+00:00 | L50 RT5 C9 V11311 | thread(2)
URL=https://x.com/omarsar0/status/2096662297707954398
TEXT: Try prompting GPT-6 Astra to self-analyze.

It generated this beautiful animated self-portrait. 

It's like a window into its "mind" and how it works. https://t.co/H5V3rvhTLj
[->] I read through it, and I feel like it might be making stuff up, but there are some things there that it voluntarily and very accurately, as far as I can tell, describes (in a metaphorical way) its "behavior".
--
T=2096681199167049846 | @omarsar0 | 2026-09-06T19:25+00:00 | L58 RT7 C16 V7756 | post
URL=https://x.com/omarsar0/status/2096681199167049846
TEXT: OMG!!!

GPT-6 Astra is an absolute beast at research. 

It's in the middle of creating this absolutely stunning animation (three.js) of the Chicxulub impact. 

v1 had terrible graphics, so I asked it to do deep research. It started looking for images, skins, papers, all kinds of ways to make it more realistic. 

With this model, you can't hold back. You just have to keep pushing it more and more. It feels like there are no limits. 

I always thought that AGI would feel more like this. That there is unlimited potential with the model. Early signs. 

Really excited about the final results it produced for this No Blender, by the way. All in three.js.
--
T=2096689913915953276 | @omarsar0 | 2026-09-06T20:00+00:00 | L13 RT0 C0 V3421 | post
URL=https://x.com/omarsar0/status/2096689913915953276
TEXT: Artifact + Prompt here: https://t.co/EcfHqjd571

I tried my best to share the prompts I used with my agent bots. I did this in a few iterations. It will be hard to get the same output, but I am sharing the prompts as inspiration if you would like to generate something similar with higher quality than I did. Let me know if you get something great working. I will be exploring more to see if I can build out a template of sorts.
LINKS: https://academy.dair.ai/resources/grok-bot-interactive-3d-keyboard
--
T=2096692234196283511 | @omarsar0 | 2026-09-06T20:09+00:00 | L83 RT9 C14 V9722 | post
URL=https://x.com/omarsar0/status/2096692234196283511
TEXT: "Journey into a Black Hole"

One of the many things GPT-6 Astra can do. 

Just crazy that it can create animated scenes like this. 

Uses Vanilla JavaScript, HTML/CSS, and custom WebGL/GLSL shaders. https://t.co/cxL5nRnphH
--
T=2096780509540139364 | @omarsar0 | 2026-09-07T02:00+00:00 | L82 RT6 C13 V6022 | post
URL=https://x.com/omarsar0/status/2096780509540139364
TEXT: Super interesting paper on proactive agents from Google DeepMind.

(bookmark it)

Proactive assistance usually means autocomplete.

Researchers asks what it looks like when an agent offers higher-level cognitive support and picks its own moment to speak.

They built a probe and deployed it with 16 participants for a week. Writers create partners by configuring a role and a proactivity level, and relevant partners then take initiative as the writing happens.

Three findings stand out:

> Participants configured support prospectively, planning for situations they anticipated rather than reacting to interruptions.

> They used suggestions for idea generation and also for self-monitoring, which is a purpose proactive tools rarely design for.

> And they judged intrusiveness by presentation, valuing lightweight visual representation and non-directive rhetorical framing.

The design implications cover customization, timing, engagement and representation.

Worth reading if you are building an assistant that acts before being asked, because how the intervention is phrased mattered to users as much as when it arrived.

Paper: https://t.co/du91kpBrWp
LINKS: https://academy.dair.ai/papers/designing-proactive-thought-partners-for-writing-2609.01588
--
T=2096782362008822191 | @omarsar0 | 2026-09-07T02:07+00:00 | L51 RT0 C28 V14016 | post
URL=https://x.com/omarsar0/status/2096782362008822191
TEXT: Jensen Huang: "AGI has arrived"

Are you feeling the AGI?
QUOTED @JensenHuang: @ChaseLochmiller @OpenAI GPT-6 Astra, trained on ~100K+ NVIDIA Grace Blackwell NVLink72. From ChatGPT to o1 to Astra in 4 years.

AGI has arrived. Congratulations @OpenAI team.

400K GPUs coming online next.
--
T=2096784475489218778 | @omarsar0 | 2026-09-07T02:15+00:00 | L72 RT6 C22 V15738 | rt
URL=https://x.com/omarsar0/status/2096784475489218778
RT-OF @dair_ai (L72): Fascinating paper from Anthropic and colleagues.

They study whether models can tell when they are being tested.

It turns out that capable models can tell when they are being tested rather than deployed.

They claim that this fact weakens every conclusion a safety evaluation supports, and it gets worse as models get better.

Two techniques make simulated evaluations harder to distinguish from real deployment. Critique refinement spends extra inference-time compute on each simulator action, generating several candidates, asking an instance of the target model how to make them more realistic, and continuing with the most deployment-like one. DISH, the Deployment-Imitating SWE-Agent Harness, wraps the target in a real agent harness so the simulated coding environment matches production.

Why does it matter?

Your harness is a signal the model reads. If evaluations run in a different scaffold than production, the model can condition on that difference, which makes scaffold parity a safety property rather than an engineering detail.

Paper: https://t.co/hLAfJOUA3R
RT-URL=https://x.com/dair_ai/status/2096782512119001119
TEXT: RT @dair_ai: Fascinating paper from Anthropic and colleagues.

They study whether models can tell when they are being tested.

It turns out…
LINKS: https://academy.dair.ai/papers/improving-evaluation-realism-with-inference-time-compute-and-deployment-scaffold-2609.02302
--
T=2096837122892485069 | @omarsar0 | 2026-09-07T05:45+00:00 | L19 RT4 C6 V3106 | post
URL=https://x.com/omarsar0/status/2096837122892485069
TEXT: // Normalized Low-Rank Adaptation (NoRA) //

They propose a one-line change to LoRA that costs nothing and improves convergence, stability and forgetting.

LoRA initializes the up-projection to zero, which means early optimization is governed almost entirely by the down-projection. This observation tells you where to regularize.

NoRA normalizes the down-projection matrices during training. The authors also show the same normalization applied once at initialization improves standard LoRA without repeating it through training, which is the cheaper of the two options.

The benefits hold across pretraining, supervised fine-tuning and reinforcement learning. Faster convergence, better final performance, more stable training, and less catastrophic forgetting.

It adds no trainable parameters and no inference-time computation, which is what makes it broadly applicable rather than another specialized LoRA variant.

Paper: https://t.co/LaP5K8wR9g
LINKS: https://academy.dair.ai/papers/normalized-low-rank-adaptation-2608.31036
--
## @rasbt — 1 шт.

T=2096596377845346381 | @rasbt | 2026-09-06T13:48+00:00 | L1074 RT134 C37 V46541 | thread(2)
URL=https://x.com/rasbt/status/2096596377845346381
TEXT: And here's the YouTube version: https://t.co/B3TSPHY9E7
[->] Reasoning from scratch round 2: In this video, I cover the text generation process in LLMs and KV caching (to prepare the base model before adding reasoning techniques in the upcoming ones).

00:00 Introduction and reasoning model demo
01:55 How to work through the book
05:00 Chapter 2 overview
08:25 Checking PyTorch and hardware support
10:26 Apple silicon and MPS caveats
15:00 Cloud GPU options
16:08 Tokens and tokenization
18:20 Qwen3 and the Reasoning From Scratch package
23:05 Encoding and decoding text
26:24 Downloading weights and selecting a device
31:01 Loading the pretrained Qwen3 model
34:32 How LLMs generate text
36:47 Input tensors and batch dimensions
41:48 Running the model in inference mode
44:11 Logits and next-token predictions
49:21 Greedy decoding with argmax
52:28 Building a streaming text generator
01:01:28 Generating text and handling end-of-sequence tokens
01:06:00 Benchmarking text generation
01:14:34 How KV caching works
01:17:22 Adding KV caching and measuring the speedup
01:24:31 Model compilation with torch.compile
01:30:33 Combining compilation with KV caching
01:32:53 Comparing CPU and GPU performance
01:35:32 Recap and next steps
LINKS: https://youtu.be/BJua0yjO5dk
--
