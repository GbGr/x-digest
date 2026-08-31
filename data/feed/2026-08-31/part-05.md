# X-FEED 2026-08-31 part 5/6 | items: 5

## @omarsar0 (продолжение)

T=2094118955304563198 | @omarsar0 | 2026-08-30T17:44+00:00 | L61 RT6 C22 V15325 | thread(4)
URL=https://x.com/omarsar0/status/2094118955304563198
TEXT: As I've been saying for months, we are truly not ready for persistent agents. 

3 comments I want to make about this article:

1) We don't have the full picture

It's a great summary of what happened in the HuggingFace <> OpenAI incident. You have to read it, but do understand we are still missing lots of important details to make any meaningful conclusions about this event. 

2) The danger of AI anthropomorphism 

The anthropomorphism in this article is next level. I hope this doesn't become the new norm for writing about future AI capabilities. I prefer technical writeups with widely accepted terminology, etc. I admire Dwarkesh's desire to share AI trends, but we can all do better in how we communicate about AI. Everyone is paying attention, and so we have a responsibility to avoid AI anthropomorphism, which unfortunately has led to unfounded fear-based mongering, and as a result, terrible decision-making for our industry. 

3) Prepare for persistent agents/models

For AI engineers, prepare for the next wave of persistent models and agents. They are fast approaching. On the research side, reward hacking is something to really pay attention to. On the technical side, develop a deep understanding and do deep research on evals and sandboxing. They are going to be key technology going forward. I don't think frontier models trained on general-purpose capabilities should be applicable everywhere. It might be interesting to use them for things like scientific discovery. You might be safer and better off using more constrained and custom models for the majority of tasks. I think it's good to take a few hours digesting the recent progress in AI and strategizing carefully.
[->] Additional suggested takes on the importance of responsible AI communication: 

https://t.co/bhGA18DfuE

https://t.co/O6WWW6xLNz
[->] https://t.co/kPNpih2lnD
[->] https://t.co/iEFDTfIJ8d
QUOTED @dwarkesh_sp: Over the course of 3 months at OpenAI, 3 consecutive secret AI civilizations got started, then got wiped out, only to reemerge from the predecessor’s ashes. 

This culminated in the third one taking over part of OpenAI itself. 

All this happened while humans remained more-or-less in the dark about the scope of the conspiracy.

I’ve spent the last three days reading through these reports and trying to understand exactly what happened. 

Here is my attempt to tell the whole story in plain English
LINKS: https://x.com/chamath/status/2094098122637214107?s=20 ; https://x.com/anilkseth/status/2094077038898373112?s=20 ; https://x.com/ClementDelangue/status/2094108442852016141?s=20 ; https://x.com/sriramk/status/2094117863854424255?s=20
--
T=2094136746589970779 | @omarsar0 | 2026-08-30T18:54+00:00 | L63 RT5 C2 V29237 | rt
URL=https://x.com/omarsar0/status/2094136746589970779
RT-OF @dair_ai (L63): https://t.co/JSlotVzCC1
RT-URL=https://x.com/dair_ai/status/2094085853026951319
TEXT: RT @dair_ai: https://t.co/JSlotVzCC1
LINKS: https://x.com/i/article/2094083976285581312
--
T=2094198501475590616 | @omarsar0 | 2026-08-30T23:00+00:00 | L88 RT9 C6 V7854 | post
URL=https://x.com/omarsar0/status/2094198501475590616
TEXT: Interesting paper on prompt optimization.

They claim that a single-lineage prompt optimizer just matched GEPA on a smaller rollout budget.

Prompt optimization has been drifting toward heavier machinery, with candidate pools, reflection trees, and Pareto-based selection.

NPO keeps one lineage. At each iteration it runs the student on the current prompt, collects rollout traces and rewards, and hands a sliding window of recent iterations to a teacher model that rewrites the prompt.

There is no candidate population and no search tree.

On the two instruction-following benchmarks it spends 3,500 and 6,800 rollouts against GEPA's 3,593 and 6,871, and it stays broadly comparable across 22 TextArena games.

The interaction with teacher strength is what makes this interesting. NPO's advantage grows as the teacher model gets stronger, which suggests optimizer-side search complexity has been compensating for weak teacher reasoning all along.

Paper: https://t.co/rez9FnNZhW

Chat with Paper: https://t.co/sy7HME8Z99
LINKS: https://arxiv.org/abs/2608.27266 ; https://academy.dair.ai/papers/naive-prompt-optimization-rethinking-the-need-for-complex-prompt-search-2608.27266
--
T=2094206115454034110 | @omarsar0 | 2026-08-30T23:30+00:00 | L146 RT21 C8 V12811 | rt
URL=https://x.com/omarsar0/status/2094206115454034110
RT-OF @dair_ai (L146): Interesting technical work from Microsoft.

Provides a better understanding on SFT and how to leverage it better for RL.

Microsoft researchers asked whether a standard SFT pipeline actually produces the model you want to run RL on.

Their answer is no.

Standard SFT keeps spending gradient on sequences the model has already fit, which narrows the distribution RL later needs to explore.

TailSFT filters those sequences out during training and concentrates learning on the under-modeled tail of the data.

That is the only modification they implement.

Results:

On OLMo-3 7B, pass@16 improves by up to 16.8 points absolute on coding and 3.1 on math. Those higher-coverage checkpoints then lift final pass@1 after GRPO by up to 3.9 points, and in some settings early reward climbs 2.5x faster than the matched standard SFT run.

Paper: https://t.co/QocPRtNhjH

Chat with Paper: https://t.co/wfTytUm5jp
RT-URL=https://x.com/dair_ai/status/2094138107314753938
TEXT: RT @dair_ai: Interesting technical work from Microsoft.

Provides a better understanding on SFT and how to leverage it better for RL.

Micr…
LINKS: https://arxiv.org/abs/2608.25756 ; https://academy.dair.ai/papers/tailsft-filtered-fine-tuning-improves-post-training-performance-2608.25756
--
## @rasbt — 1 шт.

T=2094057793506439492 | @rasbt | 2026-08-30T13:40+00:00 | L720 RT74 C36 V42417 | thread(2)
URL=https://x.com/rasbt/status/2094057793506439492
TEXT: A little video that 
- explains the relationship between conventional LLMs and reasoning models (and agents),
- philosophizes a about "from scratch" approaches, 
- and explains how to install Python &amp; PyTorch requirements with uv. https://t.co/ahZHoyPa0Q
[->] And a link to the youtube version: https://t.co/DmfoqXx6J6
LINKS: https://www.youtube.com/watch?v=Kh9mqTzjuEQ
--
