# X-FEED 2026-07-31 part 8/12 | items: 3

## @sayashk — 11 шт.

T=2082877458924065269 | @sayashk | 2026-07-30T17:14+00:00 | L346 RT62 C26 V55050 | post
URL=https://x.com/sayashk/status/2082877458924065269
TEXT: Can AI agents conduct open-ended AI research?

Most evaluations of agents conducting AI research focus on narrow, verifiable tasks. But AI research is often open ended. Researchers pick hypotheses, decide what evidence is appropriate, and recognize a failing approach. 

We gave agents research questions from two unpublished papers, six days, and thousands of dollars of API credits and compute. The authors of the original papers then reviewed the AI-generated papers. They unambiguously rejected agents' outputs. https://t.co/6HTHywjwzZ

We call these "shadow evaluations", since the agents are shadowing the original research effort by the authors. 

Agents were fluent at most *engineering* tasks 

They conducted serious literature reviews, debugged GPU environments, ran hundreds of experiments, and turned in camera-ready LaTeX without human help. We also found no evidence of reward hacking. If anything, we found the opposite: the agents started with marketable claims and walked them back to negative results as the evidence came in.

Neither agent output was close to the bar of a top conference paper 

Both papers suffered from similar failures: poor judgment about the bar for an AI paper submitted to a top conference, the lack of creative problem solving and ineffective backtracking, poor awareness of resources, and instruction drift.

1) Lack of judgment about the bar for a top conference. The agents had a poor model of the bar for an AI paper submitted to a top conference. We allowed agents to self review their papers. Despite the poor paper quality, their reviews predominantly labeled the papers "weak rejects".

2) Lack of creative problem-solving to address feedback. When they received negative reviews, the agents typically narrowed their hypothesis and claims, rather than working out creative ways to address these concerns.

3) Ineffective backtracking. The agents dropped their most ambitious hypotheses within the first fifteen hours of carrying out the experiment and never changed course afterwards.

4) Poor resource awareness. Both runs ended with over half the API budget unspent. One agent declared itself done seven hours before the deadline, right after its own self-reviewer returned another reject.

5) Instruction drift. They did not follow explicit instructions on minimum exploration time, incorporating feedback for reviews, and on paper length (the outputs exceeded the page limits in both cases).

This research design has many limitations 

Limitations include the small sample size, non-blind reviews, and the reviewers knowing that the work was AI-generated. We also couldn't test Anthropic's strongest model, because Fable 5 is deliberately limited on frontier AI research tasks, so ended up using OpenClaw with Opus 4.8 (extra-high) for our main experiments and Codex with Sol 5.6 (ultra) for a robustness check. 

But we think the research design is still helpful in assessing AI agents' ability to conduct research, and it is complementary to evaluations on verifiable tasks, as well as blinded reviews of AI outputs.

Our results show early evidence that even though agents are proficient on verifiable research tasks, they do not make genuine progress on open-ended ones. It is worth understanding if this is a fundamental limit, or if better models, scaffolds, and more compute could help close it. 

As the evidence for the gap between open-ended and verifiable tasks firms up, it is also worth understanding how much progress in AI depends on open-ended research rather than hill-climbing on well-specified objectives.

In follow-up studies, we are expanding the set of non-public papers we evaluate. If you are an AI researcher with unpublished papers, we would love to collaborate with you on our next shadow evaluation. Expression of interest: https://t.co/7YcYAIbYka

Conducting shadow evaluations involves a lot of researcher degrees of freedom. In many places, our coauthors disagreed with our interpretation of the findings, and we have surfaced those disagreements in the paper. (This is one reason why having a group of coauthors with different priors is important for open-ended research.) 

We also release the agent logs, one of the AI-generated papers (the other original paper is still not public), and all the code and data, so that others can conduct their own analyses of our results: https://t.co/K0zvuD1Xpk

Finally, we plan to conduct shadow evaluations regularly, and are hiring a senior researcher to help lead these efforts. Apply here: https://t.co/TPyOFyNxJE

I'm grateful for the core team leading this effort: @PKirgis, Andrew Schwartz, @steverab, and @random_walker, and to our collaborators who reviewed AI papers, analyzed agents logs, and gave feedback on the paper: @DavidDAfrica, @KozzyVoudouris, Viet Nguyen, Toby Pilditch, @DubMagda, @HarryCoppock, @CUdudec, @nityndg, Matilda Orona, @tilmanbayer, Derrick Chan-Sew, Yue Ling, Abhishek Shetty, @hlntnr, @ghadfield, @sethlazar, @snewmanpv, @shostekofsky, @RishiBommasani
LINKS: https://arxiv.org/pdf/2607.27191 ; https://forms.gle/CEcA4JmYhDWXQGot8 ; https://cruxevals.com/crux/can-ai-agents-conduct-research ; https://cruxevals.com/careers/senior-researcher-july-2026
--
T=2082881244946186647 | @sayashk | 2026-07-30T17:29+00:00 | L5 RT1 C0 V553 | rt
URL=https://x.com/sayashk/status/2082881244946186647
RT-OF @shostekofsky (L5): Autonomous AI researchers aren’t here yet. AI Village data shows the same, but we are getting closer quickly.

My worry: The point where they discover new findings may also be the point we can no longer catch their mistakes
RT-URL=https://x.com/shostekofsky/status/2082880297931079683
TEXT: RT @shostekofsky: Autonomous AI researchers aren’t here yet. AI Village data shows the same, but we are getting closer quickly.

My worry:…
--
T=2082881224519954885 | @sayashk | 2026-07-30T17:29+00:00 | L18 RT2 C0 V3036 | rt
URL=https://x.com/sayashk/status/2082881224519954885
RT-OF @DavidDAfrica (L18): Happy to have played a small role in this! My main takeaway— persistence, identifying gaps in the literature, and keen awareness of both resources and the original research question are still missing in agents— and these skills are hard to measure well.
RT-URL=https://x.com/DavidDAfrica/status/2082880338796085676
TEXT: RT @DavidDAfrica: Happy to have played a small role in this! My main takeaway— persistence, identifying gaps in the literature, and keen aw…
--
