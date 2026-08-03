# X-FEED 2026-08-03 part 1/3 | items: 8

## @bcherny — 2 шт.

T=2083782540570279992 | @bcherny | 2026-08-02T05:10+00:00 | L3550 RT61 C77 V78425 | post
URL=https://x.com/bcherny/status/2083782540570279992
TEXT: @Mahaximus_ I did not use the word “graph”, nor am I talking about graphs in this video. Please don’t attribute words to me that I did not say. I do encourage people to watch the video!
--
T=2083783798802760063 | @bcherny | 2026-08-02T05:15+00:00 | L7 RT0 C2 V989 | post
URL=https://x.com/bcherny/status/2083783798802760063
TEXT: @steve_umstead @leanderriefel Thanks for the feedback! Actively working on improving all of these 🙇‍♂️
--
## @cwolferesearch — 2 шт.

T=2084021452970270910 | @cwolferesearch | 2026-08-02T21:00+00:00 | L148 RT18 C4 V16932 | rt
URL=https://x.com/cwolferesearch/status/2084021452970270910
RT-OF @Vtrivedy10 (L148): great write up, evals are hard!  here are 2 broad buckets we use to evaluate agents:
1. Measure the State of the World
2. Agent as a Judge on the Trajectory

1. Measure the state of the environment before and after the Agent does the Task.

@harborframework and containerized Evals make this easier.  The agent thinks in operating in a real world and we need to set up that world (files, installed tools, security boundaries, instructions) such that it mirrors what the agent will do in the real world.

Every action the agent takes alters the world in some way.  And success on a task means running a verification step on the final state of the world after the agent is done to see if this state corresponds to a successful pass.

The tricky thing here is calibrating when the agent produces a final state that’s technically correct but your verifier didn’t forsee - you often want to allow this to pass or make sure the correct end state is capturable by your verifier.  

2. Judge the trajectory -> Correctness is not the only factor - cost, latency, interpretability matter too.  Those require understanding the action space

The right answer is a good signal, but if the agent got there by cheating the Task then that means our agent is misaligned AND our task is bad because it allows cheating.

If the agent is inefficient with cost/tokens, then that’s a signal that we may need to imbue more priors to help it find the correct trajectory (could be better prompting)

we’ll be doing a bunch more educational content and open sourcing our tooling, reach out if there’s anything you want to see in particular!

this should be accessible and easy for every team to do!
RT-URL=https://x.com/Vtrivedy10/status/2083701846816817297
TEXT: RT @Vtrivedy10: great write up, evals are hard!  here are 2 broad buckets we use to evaluate agents:
1. Measure the State of the World
2. A…
--
T=2084025104686538806 | @cwolferesearch | 2026-08-02T21:14+00:00 | L25 RT1 C2 V3251 | post
URL=https://x.com/cwolferesearch/status/2084025104686538806
TEXT: Many RSI-style papers use the coding agent to hill climb results. This works and is simple, but I wonder if greater improvements can be unlocked with coding agent + evolutionary / genetic algos. Much to be explored for designing effective self-improving agent harnesses!
QUOTED @askalphaxiv: "Frontis-MA1: Training an AI4AI Model towards Recursive Self-Improvement in Machine Learning Engineering"

This 35B AI4AI agent is trained to improve ML solutions through executable evolution.

Rather than generating one ML pipeline, it evolves many candidates by drafting, refining, repairing, and recombining code. It then executes each in a sandbox, and learns from real task scores to guide longer-horizon search.

This turns recursive self-improvement into a MLE loop, pushing the model from 39.
--
## @fchollet — 1 шт.

T=2083863030589231160 | @fchollet | 2026-08-02T10:30+00:00 | L483 RT35 C36 V109675 | thread(6)
URL=https://x.com/fchollet/status/2083863030589231160
TEXT: To address the limits of deep learning and avoid stalling, the field of AI started by applying patch (1), which started being demoed 9 months later in December 2024 and has now become completely ubiquitous. However, long term, it is simply inevitable that AI will move to patch (2).
[->] Models typically don't use test time training, they do test time search in token space. They effectively do test time natural language program synthesis. Models nowadays use an enormous amount of test time compute, we are not in the single forward pass, next-token answer prediction regime of yore.
[->] Worth noting that to this day, base LLMs (no test time compute) *still* perform poorly on the ARC 1 benchmark from 2019 (on unseen tasks) despite continued massive scaling (~100,000x since 2019). We can say that without the switch to the test-time compute paradigm, AI would still not be capable of the kind of advanced reasoning that sota systems display today. Scaling the single-pass, static, next-token prediction paradigm of the GPT-2 through GPT-4 era was running into a capability asymptote. To bypass this plateau, test-time adaptation was a necessary evolutionary step.
[->] I know it feels very tempting to dunk, and that's fair, but to be clear, my past criticism of base LLMs does not apply to TTA systems, in the same way that criticism of the limits of steam trains would not apply to current-day electrified bullet trains (even if they feel similar and use the same platform, the principles at work are substantially different). I have first updated my views in December 2024 -- by that point I no longer believed the LLM tech platform (with TTA) would stall.

If you want to assess how my past assessment of the limits of base LLMs has fared with hindsight, compare to current-day base LLMs (yes, my points still apply, even with a few years of scaling added).
[->] My December 2024 takes were "there will be no wall", "if the only bottleneck is test-time search, we will see continued scaling in the future", and "the world is once again about to run out of GPUs"

To this day, I do expect post-training scaling and TTA scaling to continue to deliver. At least 10-100x from current levels.

https://t.co/cKe1lF2FTw
[->] @MarvinTBaumann I don't mean it the way Friston means it, I mean the opposite of static inference, i.e. "adaptation at inference time"
QUOTED @fchollet: There are essentially two main options to remedy this: 

1. Find ways to perform active inference, so that the model adapts its learned program in contact with a new data distribution at test time. Would likely lead to some meaningful progress, but it isn't the ultimate solution, more of an incremental improvement. 

2. Change the training mechanism to something more robust than SGD, such as the MDL principle. This would pretty much require moving away from deep learning (curve fitting) altogeth
LINKS: https://x.com/fchollet/status/1870194696477388836
--
## @HamelHusain — 3 шт.

T=2083996240094900501 | @HamelHusain | 2026-08-02T19:19+00:00 | L99 RT4 C10 V14570 | rt
URL=https://x.com/HamelHusain/status/2083996240094900501
RT-OF @sh_reya (L99): Has anyone cracked the code of LLM speak? it's truly atrocious

I recently added a "deslopify" command to my plain-writing skill to get the agents to write responses better
https://t.co/eoFhSo3SrU 

not perfect but better than nothing

h/t @bradenjhancock for the idea https://t.co/23XxsKEeDV
RT-URL=https://x.com/sh_reya/status/2083994977223532693
TEXT: RT @sh_reya: Has anyone cracked the code of LLM speak? it's truly atrocious

I recently added a "deslopify" command to my plain-writing ski…
LINKS: https://github.com/docwriter-org/plain-writing-skill
--
T=2084001425881985308 | @HamelHusain | 2026-08-02T19:40+00:00 | L5 RT0 C0 V226 | post
URL=https://x.com/HamelHusain/status/2084001425881985308
TEXT: @sqs @connorado @AmpCode Computer use !
--
T=2084029123463467152 | @HamelHusain | 2026-08-02T21:30+00:00 | L1 RT0 C1 V290 | thread(2)
URL=https://x.com/HamelHusain/status/2084029123463467152
TEXT: @sh_reya @BEBischof @AAAzzam @bradenjhancock Cool I'm gonna try it, will add onto it 

Incase you are curious (my fork is probably overzealous but hey the AI needs to be controlled) https://t.co/n9LKAlnHKX
[->] @AAAzzam @sh_reya @BEBischof @bradenjhancock yeah I was forking it and customizing it and felt antisocial without at least opening a PR.  

But maybe the times of PRs are over, everyone should just customize their local?
LINKS: https://github.com/aaazzam/dslop/pull/4/changes
--
