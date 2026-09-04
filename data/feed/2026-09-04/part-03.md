# X-FEED 2026-09-04 part 3/11 | items: 7

## @fchollet — 6 шт.

T=2095556013407834273 | @fchollet | 2026-09-03T16:54+00:00 | L1779 RT197 C181 V87231 | thread(2)
URL=https://x.com/fchollet/status/2095556013407834273
TEXT: I believe we need to make a deliberate effort to keep humans in the loop in all critical processes across our economy and society, regardless of whether it is technically necessary.

Even if AI develops the *capability* for advanced autonomy, we should not make it highly autonomous. We have to maintain control and keep visibility and understanding of all critical processes, we should not blindly hand over everything to AI agents just because we can. AI as a tool in the human hand is the only form of AI that is worth pursuing.
[->] For a long time, the limits of AI deployment were only defined by technical capabilities. But as AI continues to make rapid progress, it needs to become a deliberate, collective choice about what kind of world we want to shape.
--
T=2095574794158928096 | @fchollet | 2026-09-03T18:08+00:00 | L38 RT2 C5 V8191 | rt
URL=https://x.com/fchollet/status/2095574794158928096
RT-OF @ccatalini (L38): Whether through human augmentation or better tooling, if we want human preferences correctly represented, we need to stay in the loop.
RT-URL=https://x.com/ccatalini/status/2095571374488391829
TEXT: RT @ccatalini: Whether through human augmentation or better tooling, if we want human preferences correctly represented, we need to stay in…
--
T=2095577204361179390 | @fchollet | 2026-09-03T18:18+00:00 | L443 RT28 C35 V31456 | post
URL=https://x.com/fchollet/status/2095577204361179390
TEXT: This is the wrong approach. This kind absolute, overbearing take on AI regulation will prove to be actively counterproductive.
QUOTED @AndrewCurran_: Bernie Sanders and Greg Casar today announced the Ban Artificial Superintelligence Act. All AI development in the United States will be paused. Systems that have capabilities that match or exceed human cognitive performance will be banned. Violators will face 20 years in prison. https://t.co/B6AhM3GiZl
--
T=2095598451115614371 | @fchollet | 2026-09-03T19:42+00:00 | L5436 RT690 C136 V537800 | thread(4)
URL=https://x.com/fchollet/status/2095598451115614371
TEXT: GPT-6 Astra represents a step-function change in model capability for interactive reasoning problems. It scores 66% on ARC-AGI-3 using our standard harness, and nearly 100% with a continuous conversation harness and custom compaction, at a cost of roughly $360 per game.

In fact, the continuous harness version significantly outperforms our human baseline in action efficiency across almost all levels. When we examined the reasoning chains to understand how the model operates, we found it performing highly efficient, on-the-fly symbolic world modeling for each game and level. It goes as far as developing its own shorthand DSL to represent in-game situations -- essentially a game-specific algebraic notation.

Overall, Astra exhibits symbolic modeling behaviors we had previously only seen with sophisticated harnesses -- so harness capabilities are increasingly shifting into the model itself.

We see Astra as a major breakthrough in model intelligence.

Read our post on Astra and what these results mean: https://t.co/wJnYxEqYNI
[->] Many of you will ask, "if it saturates ARC 3, is it AGI?"

We're not making this claim. All we know about the system so far are its benchmark scores.

When we launched ARC 3, and in every presentation we made about it, we were very insistent on one thing: solving it is not proof of AGI. It's not intended as a finish line.

ARC 3 is testing the right qualitative properties you'd expect of an AGI system -- exploration under uncertainty, adaptation without instructions, causal world modeling from limited data, etc. -- but in small quantities. ARC 3 games are orders of magnitude shorter timescales than real world tasks, and represent orders of magnitude less data, less modeling complexity, less on-the-fly learning.

(Slide below is from a March 2026 presentation)
[->] Benchmarking AI systems is a continual process that co-evolves with the models. New benchmarks challenge AI capabilities with emerging questions to shape the directions and feedback signal of the research process. Then they adapt as models progress, targeting the residual between AI and human intelligence.

We are still working on ARC-AGI-4, which we started developing after releasing ARC-AGI-3 earlier this year.  It is coming Q1 2027. We think it's going to be really special.
[->] When we released ARC 3, I got asked, "when do you think a frontier model will saturate it?", and I answered "in about a year, though it depends on how much it gets explicitly targeted"

That was 6 months ago, so the progress that Astra represents happened about 2x faster than I anticipated. I think the speed of progress will surprise a lot of people, and what the new models can do will challenge the views of AI that people developed by using prior generations of models.
LINKS: https://arcprize.org/blog/astra
--
T=2095603911323467786 | @fchollet | 2026-09-03T20:04+00:00 | L3081 RT344 C103 V835746 | rt
URL=https://x.com/fchollet/status/2095603911323467786
RT-OF @arcprize (L3081): GPT-6 Astra by @OpenAI achieves SOTA on ARC-AGI:

- Astra scores 63% on ARC-AGI-3, 99% via a new provider adapter harness
- It surpasses human performance on 96% of ARC-AGI-3 levels
- It builds the most precise symbolic model of novel environments we've seen

Our analysis: https://t.co/GX77KsRNer
RT-URL=https://x.com/arcprize/status/2095597602545025138
TEXT: RT @arcprize: GPT-6 Astra by @OpenAI achieves SOTA on ARC-AGI:

- Astra scores 63% on ARC-AGI-3, 99% via a new provider adapter harness
- I…
--
T=2095605239269519771 | @fchollet | 2026-09-03T20:09+00:00 | L3098 RT210 C82 V207937 | post
URL=https://x.com/fchollet/status/2095605239269519771
TEXT: Side note: when we released ARC-AGI-3 in March, and frontier models scored <1% on it, a few Singularitarian poasters took it as a personal insult, and got very worked up about it. They argued the benchmark was fundamentally broken, that it could not even be solved by the smartest humans, that the max reachable score was actually 40%, etc.

We had to deal with a torrent of insults and hate poasts since because we had released an unsaturated benchmark.

As it turns out, the benchmark is perfectly calibrated. It is straightforward for a human to score 100% if they do better than average people – all you need is to use fewer actions than our human baseline (which is not a strong baseline, as we used unfiltered human testers).

And naturally as a result it's also very feasible for AI to score 100% once real progress towards agentic general intelligence has been made. The trajectory of AI from <1% to 100% over the course of 6 months shows that the benchmark was able to snapshot the recent rise of agentic capabilities. And that rise has happened faster than most people expected, including us.
QUOTED @fchollet: Any smart human giving it real effort should score &gt;90%  on ARC-AGI-3
--
## @ggerganov — 1 шт.

T=2095518026523107829 | @ggerganov | 2026-09-03T14:23+00:00 | L2738 RT243 C186 V134879 | rt
URL=https://x.com/ggerganov/status/2095518026523107829
RT-OF @julien_c (L2738): Super happy to officially announce that we are a̶c̶q̶u̶i̶r̶i̶n̶g̶ joining forces with @nvidia 🔥

Here is a more personal take:

AI is at an inflection point. Open source AI can become less relevant in the coming years if the big closed labs run away with it, OR it can become the foundational fabric of the next phase of human civilization.

Those are vastly different outcomes, and we need the critical mass to ensure we give our collective best shot to the second outcome. Given @JensenHuang's stance on open source AI and how he stepped up to defend it when it was under threat earlier in the summer, NVIDIA was the only partner we truly considered.

HF will remain an independently run, neutral platform.

This gives fuel to our long-term vision and mission of unlocking the community's progress to ensure that AI, which is the greatest breakthrough of our lifetime, is accessible to as many people as possible.
RT-URL=https://x.com/julien_c/status/2095487938909876366
TEXT: RT @julien_c: Super happy to officially announce that we are a̶c̶q̶u̶i̶r̶i̶n̶g̶ joining forces with @nvidia 🔥

Here is a more personal take…
--
