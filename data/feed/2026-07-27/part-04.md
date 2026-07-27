# X-FEED 2026-07-27 part 4/4 | items: 10

## @rasbt — 1 шт.

T=2081374704753950742 | @rasbt | 2026-07-26T13:42+00:00 | L1146 RT185 C69 V48975 | post
URL=https://x.com/rasbt/status/2081374704753950742
TEXT: Yes, open-source / open-weight models are important for a healthy AI ecosystem. That's how we can verify things, check claims, and keep up outside the closed labs. Plus, it gives us the freedom to run AI on our own hardware if we are not ready to share personal data and IPs with closed labs through using their models. (Not that proprietary models are bad, actually I use them a lot as well, but it wouldn't healthy not to have any alternatives.)

Anyway, while pretty much everyone is waiting for the Kimi K3 and Ling 3.0 weights to land on the model hub any day now, there were quite a few other interesting new open-weight model releases the past week. Yes, one of those weeks!

So, here are the architecture pics along with some notes on what I found most interesting:

1) Nanbeige 4.2 3B uses looped depth sharing. This basically means it runs the same 22-layer (=transformer block) stack twice. So, it extends the 22-layer architecture to 44-layers, but without duplicating the weights. (2x the transformer block compute but same memory footprint.)

Why? The info is a bit sparse, but section 2.1 of the Nanbeige 4.2 technical report says two passes gave the best trade-off and retained about 75% of the token efficiency of a standard architecture. More passes gave barely any gains but made the training much slower and much more expensive.

2) Laguna S 2.1 is poolside's Laguna model in a really nice size: 118B sparse MoE with 8B active parameters and a 1M-token context window. Otherwise, the architecture is pretty standard. It uses 36 sliding-window and 12 global (gated-)GQA layers. However, given this size, and the fact that it (just barely) runs on my DGX Spark (uses about <80 GB of RAM), this is right now the most interesting model for me personally. It's 3x bigger and thus a tad slower but maybe a good candidate as daily-driver-Qwen3.6-35B-replacement. (Still waiting on some more independent performance benchmarks though.)

3) Motif-3-Beta is a new 314B-A13B sparse MoE that is somewhat based on DeepSeek V4 in terms of mHC and latent attention. But it uses a new component, Grouped Differential Latent Attention, which is inspired by Multi-head Latent Attention. I probably should write an article about this some time, but for now, the tl;dr is as follows. Regular MLA compresses the keys and values into a smaller latent representation to mainly reduce the KV cache size. GDLA does a similar low-rank compression but puts the attention heads into groups and also learns a noise head for each group where the noise gets subtracted for filtering purposes... Anyway, a topic for another day!

4) Solar Open 2 is a new 250B-A15B hybrid MoE by Upstage that interleaves three Kimi Delta Attention layers with one GQA layer. 

5) Antares 1B is a small model (and there is also an even smaller 0.3B variant) from Cisco starts that with the IBM Granite 4.0 1B backbone and uses SFT plus GRPO for terminal-based cybersecurity stuff. It is a nice example of task-specific post-training on a genuinely small model.

6) BTL-3 is a rank-32 LoRA adapter for Qwen3.6-27B aimed at coding agents and structured tool use. The really strong benchmark performance suggests that LoRA adapters are still a useful tool/technique in 2026.

I added all six to the LLM Architecture Gallery for some additional details:
https://t.co/JDtfup3ncn
LINKS: https://sebastianraschka.com/llm-architecture-gallery/
--
## @RLanceMartin — 1 шт.

T=2081408482344149047 | @RLanceMartin | 2026-07-26T15:57+00:00 | L78 RT5 C11 V16946 | post
URL=https://x.com/RLanceMartin/status/2081408482344149047
TEXT: lol this talk is from AIE 2024 (before I was at Anthropic). im glad graphs are cool (again)!
QUOTED @0xCodez: Anthropic engineer just released a 2-hour workshop on "Graph Engineering" for agentic systems:

“80% of our engineers are using self-improving loops. Now everyone is building agentic graphs.”

• 00:00 - Introduction to RAG & Graphs
• 06:39 - Core of "Graph Engineering" (state, nodes)
• 14:29 - 3 feedback loops of Graph agents
• 23:06 - Agent evaluation with Graphs
• 36:29 - Agent cycles in graphs
• 1:15:22 - Agentic RAG & agent context
• 1:41:20 - Evaluation datasets based on Graphs

This 2-hour
--
## @sh_reya — 2 шт.

T=2081392089729053122 | @sh_reya | 2026-07-26T14:51+00:00 | L38 RT3 C6 V5996 | post
URL=https://x.com/sh_reya/status/2081392089729053122
TEXT: hot take: sometimes I wonder if the uncanny valley is actually what we need, so we can more easily distinguish human-AI interaction from human-human interaction.

for example, writing. when I read something that feels mostly AI produced, I evaluate it differently.

instead of asking, “do I trust this person’s taste and understanding of the topic? so much that if I spend time reading this, will I learn something interesting?”

I switch to asking, “am I interested in this topic? and does the AI probably know more than I do here, without being so sloppy that I can still understand it?”

in short, the uncanny valley is a good cue to tell us how to evaluate or make sense of the information; the uncanny value cues the appropriate epistemic frame
QUOTED @HamelHusain: Voice models love replying with "Exactly!"  even when it isn't called for
--
T=2081444175061598455 | @sh_reya | 2026-07-26T18:18+00:00 | L95 RT6 C5 V10112 | post
URL=https://x.com/sh_reya/status/2081444175061598455
TEXT: In evals you have two totally different components: (1) discovery of what the failure modes are, (2) focused measurement of how prevalent these failure modes are—so you can prioritize what to fix. LLMs can help in (1) by finding some failure modes— but not all, since many failure modes are subjective/ about human interpretation of outputs. LLMs can help in (2) by looking at a trace and determining if the failure mode exists, rather than having a human look at every trace. But a big mistake people make is to have LLMs fully automate (1) and (2). LLM judge is a complement to human experts, not a replacement.
QUOTED @isaac_flath: IMO people should think of LLM judge as instrumentation rather than as evals

The eval is human labels.  LLM judge is instrumenting those human labels.

It's why skipping human labels to do LLM judge first makes no sense
--
## @thorstenball — 6 шт.

T=2081256432616276145 | @thorstenball | 2026-07-26T05:52+00:00 | L35 RT0 C2 V3940 | post
URL=https://x.com/thorstenball/status/2081256432616276145
TEXT: No newsletter today! 

Back from my bike trip, reading Wikipedia articles on asphalt and wishing a long-ass article on asphalt's influence on civilization titled Where the Rubber Hits the Road existed, chilling and preparing Laracon talk.
--
T=2081279570611675334 | @thorstenball | 2026-07-26T07:24+00:00 | L70 RT1 C3 V7890 | post
URL=https://x.com/thorstenball/status/2081279570611675334
TEXT: Watched Moana 2 with the kids yesterday.

Now I'm building a little bash-the-Kakamora game for them https://t.co/NBhf6mor9d
--
T=2081298436209479839 | @thorstenball | 2026-07-26T08:39+00:00 | L119 RT4 C8 V12068 | post
URL=https://x.com/thorstenball/status/2081298436209479839
TEXT: ... but can it stay in sync like Amp can? https://t.co/mgQdQIQtS2
--
T=2081381315501293716 | @thorstenball | 2026-07-26T14:09+00:00 | L23 RT0 C14 V6136 | post
URL=https://x.com/thorstenball/status/2081381315501293716
TEXT: Lufthansa has got to have the worst airline website out of all of them, no?
--
T=2081431457193476428 | @thorstenball | 2026-07-26T17:28+00:00 | L41 RT0 C7 V7247 | post
URL=https://x.com/thorstenball/status/2081431457193476428
TEXT: "Typed live inside a GPUI window in an Amp Orb"

After I asked the agent to give me a demo video of the text editor it built.

Future's here. https://t.co/XPGtOOZvNS
--
T=2081433098722373785 | @thorstenball | 2026-07-26T17:34+00:00 | L111 RT0 C15 V16363 | thread(2)
URL=https://x.com/thorstenball/status/2081433098722373785
TEXT: I think this is what people who are skeptical of non-local-dev haven't seen yet:

There is no magic trick. The latest models are *incredible* at figuring out how to be productive in a headless machine.

You can literally ask them to record a demo video of a Linux app or a website and they will very likely just go and do it.

The times when you had to painfully recreate local tooling in a remote machine are over.
[->] I mean, look:

1. What I sent to Puck
2. What the agent in Orb produced without me doing anything

Screenshot of Ghostty running in a headless Orb.

It figured out the Nix toolchain, installed drivers, etc.

It's nearly make-a-wish level now. https://t.co/CqpSCGE8du
QUOTED @thorstenball: @RidgetopAI I mean, that's it. That's the video :) 

I asked it to build a text editor, then asked whether it can't record a demo video. https://t.co/DOcS1AytTV
--
