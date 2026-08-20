# X-FEED 2026-08-20 part 1/10 | items: 9

## @addyosmani — 2 шт.

T=2090158817522684125 | @addyosmani | 2026-08-19T19:27+00:00 | L150 RT10 C7 V271254 | post
URL=https://x.com/addyosmani/status/2090158817522684125
TEXT: I had a great conversation in SF with @GergelyOrosz. We talked about engineering roles unbundling, DevTools to AI agents, cognitive debt &amp; surrender and more.
QUOTED @GergelyOrosz: If you’ve ever opened Chrome DevTools, or optimized a page for Core Web Vitals, you’ve used software built by @addyosmani. 

Timestamps:
00:00 Intro
02:50 Addy’s current workflow
05:11 Addy’s path into tech
15:04 Addy’s work on jQuery
16:44 TodoMVC
21:44 Getting hired at Google and working on Chrome
27:17 Building dev tools
40:15 Core Web Vitals
45:42 Google’s engineering culture
51:03 Addy’s career trajectory at Google
57:55 The director role at Google
1:01:40 Cognitive debt and cognitive surre
--
T=2090159565308408226 | @addyosmani | 2026-08-19T19:30+00:00 | L995 RT121 C36 V399359 | rt
URL=https://x.com/addyosmani/status/2090159565308408226
RT-OF @addyosmani (L995): https://t.co/Gkd5qvcrAk
RT-URL=https://x.com/addyosmani/status/2087427868343373919
TEXT: RT @addyosmani: https://t.co/Gkd5qvcrAk
LINKS: http://x.com/i/article/2087205551038230528
--
## @bcherny — 2 шт.

T=2089924199804711410 | @bcherny | 2026-08-19T03:55+00:00 | L1057 RT22 C129 V115735 | post
URL=https://x.com/bcherny/status/2089924199804711410
TEXT: The small quality of life improvements keep coming. When you’re using Desktop every day, slow startup makes the app feel sluggish. Working on improving this even more!
QUOTED @ClaudeDevs: Claude Desktop now starts ~2x faster than it did a month ago.

When the app started in the background, its timers got throttled and the JS engine dropped into power-saving mode. We now boot at full speed even while the window's still hidden, along with some smaller perf fixes! https://t.co/pt5UviYvkL
--
T=2089956862968074503 | @bcherny | 2026-08-19T06:05+00:00 | L10918 RT1237 C474 V3199504 | rt
URL=https://x.com/bcherny/status/2089956862968074503
RT-OF @AnthropicAI (L10918): Many drugs work by binding to a specific target in the body and blocking or changing what it does. An important first step in the drug development process is designing a molecule that can bind tightly to its target. Traditionally, that's meant weeks or months of expert work per target, sifting through a large number of candidates to identify the few that work.

We wanted to test if Claude could successfully design novel protein binders from scratch (also called de novo design). With a protein design prompt written by a human expert, Claude autonomously designed protein binders against 14 out of 15 targets.

We then worked with Adaptyv Bio and Twist Bioscience, who independently built and tested the proteins Claude designed.
RT-URL=https://x.com/AnthropicAI/status/2089842387845804246
TEXT: RT @AnthropicAI: Many drugs work by binding to a specific target in the body and blocking or changing what it does. An important first step…
--
## @cwolferesearch — 1 шт.

T=2090080281248325744 | @cwolferesearch | 2026-08-19T14:15+00:00 | L69 RT9 C5 V3904 | thread(2)
URL=https://x.com/cwolferesearch/status/2090080281248325744
TEXT: When training a specialized LLM with midtraining / CPT, there are several important dimensions of the training process that need to be tuned…

Data mixture. Midtraining should emphasize high-quality data from domains that matter for downstream use cases (e.g., math, code, science, or instruction following). However, we usually want to retain some general data rather than switching entirely to a specialized distribution. The optimal mixture can be found empirically with small-scale mixture ablations.

Training duration. More training is not always better. Gains from midtraining can saturate relatively quickly, and excessive training on a specialized distribution can cause diminishing returns, forgetting, or overspecialization (although this can be mostly mitigated by tuning the data mixture properly). For this reason, the token budget itself should be treated as a hyperparameter rather than simply maximizing the amount of training.

Timing / stage ordering. When should specialized data be introduced during training? The optimal data distribution is not fixed throughout pretraining. In practice, many successful recipes progressively shift toward higher-quality / specialized data later in training. Midtraining can also interact with other stages like long-context training, so the ordering of these stages matters.

Interestingly, the best settings for midtraining also depend on when it is applied. In particular, the optimal data mixture actually changes depending on the stage of the pretraining / midtraining process and how much the model has been trained. Models that have undergone less training tend to be able to train on high ratios of specialized data while still performing well.

Sequence length. Longer sequences are substantially more expensive to train on. Training at shorter context lengths can be more efficient, but doing so may deteriorate previously learned long-context capabilities. Often this is handled by putting a long-context training phase at the end of pretraining, but some papers show that inserting midtraining after this phase actually leads to the best results (despite slightly deteriorating long context performance). We can achieve the best of both worlds by running a short long-context restoration phase afterwards.

Post-trainability. The best midtrained checkpoint is not necessarily the one with the highest immediate benchmark performance. Midtraining builds knowledge and reasoning capabilities that downstream RL can exploit, so we should evaluate midtraining recipes based on their final post-trained performance as well. Usually, this is evaluated by just running a lightweight post-training phase (e.g., SFT) on each model checkpoint before performing evals.

Put simply, midtraining / CPT is more complex than just continuing pretraining on better data. Data composition, sampling ratios, training duration, sequence length, and placement within the overall training pipeline are tunable design choices that impact final performance.

For more details, see my recent writeup: https://t.co/yuZXrAnExc
[->] Links to papers referenced:
- https://t.co/BojGBMIIFQ
- https://t.co/7tf0Q13MyZ
LINKS: https://cameronrwolfe.substack.com/p/midtraining-notes ; https://arxiv.org/abs/2504.03624 ; https://arxiv.org/abs/2603.17074
--
## @dexhorthy — 4 шт.

T=2090091396917248209 | @dexhorthy | 2026-08-19T14:59+00:00 | L187 RT10 C29 V14322 | thread(2)
URL=https://x.com/dexhorthy/status/2090091396917248209
TEXT: there's a almost-year-old thread about spec driven development which has recently devolved into claude slop but CLEARLY demonstrates how hard it is to try and keep ALL your specs in sync with ALL your code - you basically have just manufactured a new problem that doesn't actually yield that much leverage 

(you may save a little bit of time/tokens during research but if you codebase research is dialed in, just spend the tokens my friends - trying to compact the moving target of "what is the structure and intent of this codebase" has enough downsides that its probably not worth the upside)

https://t.co/Ym0BfoJa8A
[->] https://t.co/3QvwwXOXFs
LINKS: https://github.com/github/spec-kit/discussions/152#discussioncomment-18080849 ; https://x.com/dexhorthy/status/2090093713947275760
--
T=2090093713947275760 | @dexhorthy | 2026-08-19T15:09+00:00 | L243 RT9 C16 V23411 | thread(2)
URL=https://x.com/dexhorthy/status/2090093713947275760
TEXT: man its crazy to me how many people are still talking about AI as if they've never seen no vibes allowed, a talk which is so full of now-outdated advice that I had stopped sending it to people but apparently these foundations are still important. if you're still saying the phrase "spec driven dev" I got some bad news for ya  https://t.co/WYkqvnw9fT
[->] https://t.co/txlQUSgLCH
LINKS: https://www.youtube.com/watch?v=rmvDxxNubIg ; https://x.com/dexhorthy/status/2090091396917248209?s=46
--
T=2090131031227867326 | @dexhorthy | 2026-08-19T17:37+00:00 | L15 RT0 C0 V2486 | post
URL=https://x.com/dexhorthy/status/2090131031227867326
TEXT: Waymo having a normal one https://t.co/tWd7UTr9FC
--
T=2090206415021572379 | @dexhorthy | 2026-08-19T22:36+00:00 | L145 RT2 C4 V8885 | post
URL=https://x.com/dexhorthy/status/2090206415021572379
TEXT: this guy gets it
QUOTED @adam__conway: My codebase slop theory is there's some threshold past which slop goes exponential https://t.co/ZUFMxPucRY
--
