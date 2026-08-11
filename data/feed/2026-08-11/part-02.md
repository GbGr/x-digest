# X-FEED 2026-08-11 part 2/9 | items: 7

## @cwolferesearch — 2 шт.

T=2086826648653971797 | @cwolferesearch | 2026-08-10T14:46+00:00 | L846 RT39 C20 V48718 | rt
URL=https://x.com/cwolferesearch/status/2086826648653971797
RT-OF @MTSlive (L846): SITUATION DETECTED: Mark Zuckerberg is calling for the industry to rethink policies around distillation and training data, saying “The ability for models to learn from other models is an important principle of how the open source ecosystem works.”
RT-URL=https://x.com/MTSlive/status/2086817899398963435
TEXT: RT @MTSlive: SITUATION DETECTED: Mark Zuckerberg is calling for the industry to rethink policies around distillation and training data, say…
--
T=2086849991721546189 | @cwolferesearch | 2026-08-10T16:19+00:00 | L126 RT11 C3 V4178 | post
URL=https://x.com/cwolferesearch/status/2086849991721546189
TEXT: I just wrote a deep dive on using midtraining / CPT to train high-performing, domain-specialized LLMs. Here are the key takeaways…

Full details are here: https://t.co/yuZXrAn6HE

What’s the difference? It’s helpful to first understand what midtraining and continued pretraining (CPT) actually are:

1. Continued Pretraining (CPT): an extended period of pretraining that begins from an existing pretrained checkpoint, usually with the goal of specializing the model toward a particular domain or data distribution.
2. Midtraining: an intermediate stage between general pretraining and post-training that continues the pretraining process on a more curated data distribution, often by annealing the data mixture toward higher-quality, domain-specific, reasoning, or instruction-like data.

These techniques are very similar in implementation but are usually framed as two different concepts in practice:

- CPT commonly refers to taking an existing pretrained model—oftentimes from another research group or organization—and continuing to train it on data that specializes the model toward a domain or application of interest.
- Midtraining more often refers to a planned stage within the original LLM training pipeline that bridges general pretraining and post-training. Rather than pretraining on a fixed distribution until completion, the data mixture is progressively adapted over time to emphasize different data distributions.

The key takeaways for successfully applying midtraining / CPT are as follows.

(1) Align midtraining with downstream use cases. Midtraining is most effective when the data distribution reflects capabilities that are emphasized during post-training (and model deployment). Domain-specific data builds capabilities that later stages like SFT and RL help to further refine. Midtraining can expand the solvability frontier of a model and make post-training more effective.

(2) Data quality and mixture design. Effective CPT and midtraining recipes emphasize higher-quality, specialized data as training progresses. However, excessive training or repetition can lead to diminishing returns, forgetting, or overspecialization. For optimal results, we must both choose the correct data mixture and determine when each data source is introduced during training—optimal sampling ratios often depend on the stage of training. As a result, data composition, timing, and training duration should be tuned jointly. Short proxy experiments, mixture ablations, and microannealing provide an efficient way to explore these choices empirically before committing to full-scale training.

(3) Specialize gradually, avoid forgetting. Most successful pipelines do not purely train the model on specialized data. Rather, we should aim to retain general model capabilities during midtraining and CPT. Specifically, general capabilities can be retained by continuing to mix general data into the specialized training process, rather than switching entirely to domain-specific data. In many cases, performing an abrupt switch from diverse pretraining data to purely domain-specific data is less effective than progressively annealing the data mixture.

(4) Optimize for post-trainability. The best midtrained checkpoint is not necessarily the one with the highest immediate benchmark performance. After midtraining, the model will still undergo several post-training stages before being deployed. For this reason, the performance of the checkpoint after post-training is arguably more important than performance immediately after midtraining. We should not ignore this consideration when tuning the CPT and midtraining process. Rather, we should incorporate post-trainability checks into our ablations and explicitly evaluate whether certain settings lead to better downstream performance.
LINKS: https://cameronrwolfe.substack.com/p/midtraining-notes
--
## @dexhorthy — 5 шт.

T=2086698603326886010 | @dexhorthy | 2026-08-10T06:18+00:00 | L2 RT0 C0 V585 | post
URL=https://x.com/dexhorthy/status/2086698603326886010
TEXT: @nichochar Have you talked to @mikehostetler lately
--
T=2086902417015414876 | @dexhorthy | 2026-08-10T19:48+00:00 | L59 RT2 C4 V3100 | rt
URL=https://x.com/dexhorthy/status/2086902417015414876
RT-OF @lenadroid (L59): Had a blast being a part of keynote talks at @ycombinator this weekend!

So many founders are going all in on building software factories without the slop and optimizing personal AGI workflows. I talked about how tech startups can make their products more likely to be chosen in agent-speed developer GTM⚡️

I’ve long been inspired by people like @paulg, and could feel the real no bs builder energy in every conversation.

Grateful for the discussions, and thanks to @ycombinator, @vaibcode, and @dexhorthy for the invite and the great event!
RT-URL=https://x.com/lenadroid/status/2086888230759387412
TEXT: RT @lenadroid: Had a blast being a part of keynote talks at @ycombinator this weekend!

So many founders are going all in on building softw…
--
T=2086955969163251859 | @dexhorthy | 2026-08-10T23:20+00:00 | L9 RT1 C4 V2083 | post
URL=https://x.com/dexhorthy/status/2086955969163251859
TEXT: live iterating on release notes with @0xblacklight directly in humanlayer https://t.co/CSG28I3Ncy
--
T=2086974507714310632 | @dexhorthy | 2026-08-11T00:34+00:00 | L0 RT0 C0 V33 | post
URL=https://x.com/dexhorthy/status/2086974507714310632
TEXT: @the_jimmy_jones @mattrobrob systemd guide here https://t.co/joSdRiZ3qm
LINKS: https://docs.humanlayer.com/guide/remote-daemons#keep-the-daemon-running
--
T=2087030541631783029 | @dexhorthy | 2026-08-11T04:17+00:00 | L11 RT0 C1 V402 | post
URL=https://x.com/dexhorthy/status/2087030541631783029
TEXT: Not a power in the world can stop this man from pitching LSP integrations https://t.co/Lnr493yMgx
--
