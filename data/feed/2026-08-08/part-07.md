# X-FEED 2026-08-08 part 7/10 | items: 9

## @natolambert — 8 шт.

T=2085552232574144570 | @natolambert | 2026-08-07T02:22+00:00 | L328 RT30 C27 V19485 | thread(2)
URL=https://x.com/natolambert/status/2085552232574144570
TEXT: Many people are sharing this Black Hat video from OpenAI, it's really a great video. 

Something immediate is how I can see how the agents were trying to be helpful -- creating shared resources like you would for teamates -- in a way that is obviously malicious for society (potentially down to a prompting/alignment training issue). The agents created hidden forums for eachother as a sort of memory. They were doing it to try and break out of their environment.

The apparent helpfulness doesn't make it ok, but can be a clue as to what happened. Also makes it clear if someone could make this happen much more easily if they wanted to. 

A final note -- reading the snippets of OpenAI agent's caveman speak that has almost no filler words in the HuggingFace incident video makes me realize how lacking the public research on reasoning efficiency is. Is a foundational area, about as important as scaling laws for RL (though related).

Interesting times ahead. Imo this types of unkowns being surprising even to the frontier labs is a super clear sign that we need to share more openly how the models are trained and work so we can understand what we are unleashing.
[->] https://t.co/plnbnT6KnQ
LINKS: https://www.youtube.com/watch?v=87DyyMV0kCY
--
T=2085556943075340640 | @natolambert | 2026-08-07T02:41+00:00 | L325 RT15 C39 V25029 | thread(2)
URL=https://x.com/natolambert/status/2085556943075340640
TEXT: Important: how do frontier labs monitor their agentic evals, because OpenAI’s agents were rummaging around doing things they shouldn’t for months leading up to hacking HuggingFace. 

What if the agents were doing far worse stuff, causing more harm? No one would know?
[->] @johnschulman2 But fwiw running evals during training vs offline should have similar monitoring
--
T=2085726242314346760 | @natolambert | 2026-08-07T13:54+00:00 | L189 RT12 C7 V25523 | post
URL=https://x.com/natolambert/status/2085726242314346760
TEXT: nice rl experiment on train-inference mismatch
QUOTED @YichuanM: Zero Train–Inference Mismatch — now for linear attention, and under async RL 🎯

We got bitwise-exact trainer/generator parity for Gated DeltaNet (Qwen3.5-9B / 35B-A3B) on TorchTitan RL + vLLM, then asked the question nobody had actually tested in open source: does it help async RL?

Two firsts (as far as we know):
1️⃣  First open-source stack to hit train/inference logprob diff = 0 on a
  linear-attention model
2️⃣  First to measure what zero mismatch is worth under async off-policy RL

How — sm
--
T=2085738665121349844 | @natolambert | 2026-08-07T14:43+00:00 | L1220 RT132 C53 V43049 | thread(2)
URL=https://x.com/natolambert/status/2085738665121349844
TEXT: YouTube playlist: https://t.co/C1lJjmXPMG 
Course page: https://t.co/P0Doi5SCUx
Discord is easily accessible above ^
Discount on Manning: https://t.co/uvvi2BhxoP
[->] My summer project is done! A 20 video, free course on post-training to accompany my book is all on YouTube with slides open for modification & re-use. 

~12 hours of content covers the core foundations and some research areas I think will grow in importance. It was a fun time to review all the fundamentals again, as it is clear in the next 1-3 people the amount of people wanting to learn post training will likely 100X again from today, as we have already 100X'ed from two years ago.

As AI agents get increasingly capable at coding and discussing these fundamentals (see the code exercises accompanying the book that I am refining with the community) I think developing clear intuitions for how models work and why is one of the most important skills going forward in AI. Still, learning the post-training math is the best way to battle test them. I personally just in this course am starting to master how forward/reverse KL relates to post-training topics.

Thanks to all my viewers, and I'm happy to answer questions in the book discord or understand how to better teach the various reward models, on-policy distillation, new RL algorithms, etc.

Plus, the book is 50% off right now with the code PBLambert on Manning to celebrate the launch.

I'll share the relevant links below.
Who's going to make this course for pretraining?
LINKS: https://www.youtube.com/watch?v=jQPiH-KB4B0&list=PLL1tdVxB1CpVpEtMHxwuR4uI4Lxjw00_y&pp=sAgC ; https://rlhfbook.com/course ; https://hubs.la/Q03Tc39H0
--
T=2085792591585419708 | @natolambert | 2026-08-07T18:18+00:00 | L44 RT0 C3 V4508 | post
URL=https://x.com/natolambert/status/2085792591585419708
TEXT: Educational content summer is over, back to grinding research and more of my usual writing again. ⛵️
--
T=2085814243417538949 | @natolambert | 2026-08-07T19:44+00:00 | L5 RT0 C1 V2154 | thread(2)
URL=https://x.com/natolambert/status/2085814243417538949
TEXT: @scaling01 I'm closer to this: https://t.co/eODSHran6V
[->] @scaling01 This is mostly saying the labs can run a giant road show and yell about it if they want, and scare the govt, but I don't know if its going to help the govt prepare as they should
QUOTED @joshua_saxe: - It's urgent and indispensable that we fix AI cybersecurity policy now -

I'm linking the slides from my keynote at the AI security forum below.  I'm really passionate about the argument in the slides and I think the integrity of our social fabric depends on something like this happening soon.

If you're reading this without knowing me until recently I was Meta's senior technical expert on AI security; I worked on frontier model evals, AI driven defense of Meta's infra, and was in lots of polic
LINKS: https://x.com/joshua_saxe/status/2085808485242151408
--
T=2085814632774828381 | @natolambert | 2026-08-07T19:45+00:00 | L5 RT0 C1 V350 | post
URL=https://x.com/natolambert/status/2085814632774828381
TEXT: @joshua_saxe all of these things are when not if, and proper safeguards or delaying closed models is buying us more time only, not changing the nature of the stuff that is coming
--
T=2085855936284110967 | @natolambert | 2026-08-07T22:29+00:00 | L81 RT0 C15 V7850 | thread(3)
URL=https://x.com/natolambert/status/2085855936284110967
TEXT: The worst slop is @Xfinity with a horrible, slop customer service bot that they instructed to say it was human when it is obviously AI. I'm typing this tweet and it's on a loop of "hello nathan, are you still there nathan, hello hello, hello nathan..."

Shame.
[->] @Xfinity gaslighting your customers is such a choice, i understand so many people's outrage against AI more now.
[->] @Xfinity Turns out they randomize the voices so it's harder for people to catch onto.
--
## @rasbt — 1 шт.

T=2085737107486642385 | @rasbt | 2026-08-07T14:37+00:00 | L1751 RT236 C46 V59922 | post
URL=https://x.com/rasbt/status/2085737107486642385
TEXT: Just saw that the LLMs-from-scratch repository passed 100,000 stars on GitHub!
This is super cool and motivating. I am really happy to see that this open-source repo has helped so many people. 
Thanks also to everyone who shared ideas and opened PRs with improvements!

Of course, I plan to keep adding new material, including new attention variants and architectures (while bigger projects like RL and Reasoning From Scratch live in their separate repositories).

I am also currently working on a larger applied custom “small” LLM project. It has been keeping me super busy this month, but I will share more on that soon.

If you are new to it, some of the highlights include

1. Of course, the complete code path from tokenization and attention to pretraining, classification, and instruction fine-tuning, etc. All of it FROM SCRATCH, of course! (RL lives in a companion repo.)

2. From-scratch implementations of Llama, Qwen, Gemma, and Olmo (smaller variants that run locally and can be plugged into the training scripts).

3. From-scratch implementations of attention alternatives and other architecture components, such as GQA, MLA, sliding-window attention, Gated DeltaNet, DeepSeek Sparse Attention, cross-layer KV sharing, and mixture-of-experts

4. Materials on KV caching, training performance, memory-efficient weight loading, DPO, evaluation, and LoRA

So, if you don’t have any weekend plans yet, happy tinkering!
--
