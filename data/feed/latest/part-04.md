# X-FEED 2026-07-22 part 4/11 | items: 9

## @lateinteraction — 4 шт.

T=2079556126585069610 | @lateinteraction | 2026-07-21T13:16+00:00 | L12 RT1 C0 V2063 | rt
URL=https://x.com/lateinteraction/status/2079556126585069610
RT-OF @jtaylorhodge (L12): Exciting to see RLMs and meta-harnesses reach escape velocity.

Now vertical on the pad:
Machine studying
RT-URL=https://x.com/jtaylorhodge/status/2079418612238954918
TEXT: RT @jtaylorhodge: Exciting to see RLMs and meta-harnesses reach escape velocity.

Now vertical on the pad:
Machine studying
--
T=2079565789678473245 | @lateinteraction | 2026-07-21T13:54+00:00 | L586 RT67 C17 V48765 | rt
URL=https://x.com/lateinteraction/status/2079565789678473245
RT-OF @lateinteraction (L586): The "harness" is starting to blur with the neural architecture, in terms of who carries the inductive biases that unlock generalization.

We show that training RLMs specifically is far superior at scaling and generalization to harder tasks than training vanilla Transformers.
RT-URL=https://x.com/lateinteraction/status/2079206085957693505
TEXT: RT @lateinteraction: The "harness" is starting to blur with the neural architecture, in terms of who carries the inductive biases that unlo…
--
T=2079649592870682982 | @lateinteraction | 2026-07-21T19:27+00:00 | L126 RT8 C5 V14185 | post
URL=https://x.com/lateinteraction/status/2079649592870682982
TEXT: a thought experiment we left out of the blog since it’s comparatively undercooked:

suppose you take the best pre-Transformer LSTM and tune+scale up the modern pre-/post-training recipe on it with a modern harness, would that or would it not produce a far better AI assistant, even for plain tasks that don’t necessitate tool use, than the best vanilla Transformer without a harness? (i.e., not even a <reasoning> loop, which is a harness that changes the expressive power of the otherwise overly parallel Transformers - but you can do all the RL[HF] you want otherwise!)

i think it clearly would! ergo, attention is not all you need. in fact, it’s not even clear that you actively need it. it goes without saying but attention is really useful though.
QUOTED @a1zhang: Transformers struggle to generalize to tasks they were not explicitly trained on. Instead, we propose in 2026 that it is the job of the harness to generalize through composition.

We observe a powerful property when training RLMs: for tasks with shared structure that look different, the root model naturally learns the same trajectory, meaning it views the two task trajectories as the same! In other words, the Transformer does not need additional generalization capabilities to transfer capabiliti
--
T=2079777388938854709 | @lateinteraction | 2026-07-22T03:55+00:00 | L12 RT3 C0 V1023 | rt
URL=https://x.com/lateinteraction/status/2079777388938854709
RT-OF @_reachsumit (L12): PLAID-PRF: Pseudo-Relevance Feedback with Centroid-like Tokens in PLAID

Introduces a lightweight pseudo-relevance feedback method for PLAID that reuses existing indexing-time centroid codes to reformulate queries.

📝 https://t.co/hipbpIF15E
👨🏽‍💻 https://t.co/THTW5ZAonI
RT-URL=https://x.com/_reachsumit/status/2079773591755973013
TEXT: RT @_reachsumit: PLAID-PRF: Pseudo-Relevance Feedback with Centroid-like Tokens in PLAID

Introduces a lightweight pseudo-relevance feedbac…
LINKS: https://arxiv.org/abs/2607.18626 ; https://github.com/cmacdonald/pyterrier_colbert2/
--
## @mattpocockuk — 3 шт.

T=2079506509411635549 | @mattpocockuk | 2026-07-21T09:59+00:00 | L417 RT21 C58 V57171 | post
URL=https://x.com/mattpocockuk/status/2079506509411635549
TEXT: "Greenfield" codebases don't really exist anymore. Let me explain:

I get asked a lot: "do your skills work on greenfield codebases?" or "do they work on legacy codebases?"

Greenfield vs Brownfield is a distinction that has never really felt real to me.

- Greenfield: you are building new software from scratch
- Brownfield: you are editing existing software

The truth is that the green field that we imagine when we start out a new project is an illusion. We are not spitting out software into an empty void. There are existing systems to integrate with. User preferences to work around.

The only difference between Greenfield and Brownfield is the state of your repo. In a Greenfield project you haven't set up coding conventions. There is no prior art to work from. You have an opportunity to set up your agent's experience in that repo from scratch.

But since code is being produced faster than ever before, how long does that codebase stay green? Two days? A week at most?

All the fields are brown, and being churned up faster than ever. Your default posture should be "this is a legacy codebase", even if it's a week old.
--
T=2079534578285371544 | @mattpocockuk | 2026-07-21T11:50+00:00 | L726 RT8 C54 V55049 | post
URL=https://x.com/mattpocockuk/status/2079534578285371544
TEXT: Just filmed the new /grill-me lesson of the new course...

...and it asked me 46 questions

Dude, chill, you're scaring the noobs
--
T=2079852909282435421 | @mattpocockuk | 2026-07-22T08:55+00:00 | L44 RT0 C11 V4888 | post
URL=https://x.com/mattpocockuk/status/2079852909282435421
TEXT: Looking to submit a Codex plugin for my skills. Anyone I know on here that can help fast-track it?
--
## @mitchellh — 2 шт.

T=2079636607049896174 | @mitchellh | 2026-07-21T18:36+00:00 | L1569 RT69 C12 V175561 | post
URL=https://x.com/mitchellh/status/2079636607049896174
TEXT: Quality software doesn’t break, doesn’t demand attention, knows its limits, and fixes fast. @almonk is a fine builder of quality software, recommend.
QUOTED @almonk: https://t.co/Rz0q1W33ut
--
T=2079672171321081908 | @mitchellh | 2026-07-21T20:57+00:00 | L297 RT10 C9 V26655 | post
URL=https://x.com/mitchellh/status/2079672171321081908
TEXT: LLVM21 is a stinker and has worse codegen in general, and a bug forced disabled loop auto-vectorization. Turned out to be a blessing: we clearly identified areas we were over-reliant on implicit compiler optimizations and were able to explicitly restructure our code to what we really wanted.

The result is that we now have clean generic SIMD subroutines in places we previously relied on auto-vectorization. And we did it better and as a result produced faster code (see below). Pure ASCII throughput improved more than 20% (30% on Linux) which is insane and is purely because we wrote better SIMD than an auto-vectorizer can. Lit.

We also found it stopped inlining automatically in certain places which destroyed some benchmarks based on real world corpuses. As a result, we now explicitly inline those backed by benchmarks. Wonderful.

Some things slowed down more than can be attributed to noise. I'm looking into that now but they're minor benchmarks. The important ones are parity or better.
--
