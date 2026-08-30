# X-FEED 2026-08-30 part 1/6 | items: 9

## @_philschmid — 1 шт.

T=2093694057818009934 | @_philschmid | 2026-08-29T13:35+00:00 | L116 RT19 C25 V7325 | post
URL=https://x.com/_philschmid/status/2093694057818009934
TEXT: Learn how Gemini Co-Scientist worked with researchers across materials science, biology, and computer science to design experiments, predict biological behavior, grow new materials, and improve AI-generated research.

Results: 
- Gemini proposed lab recipes that produced 3 atom-thin semiconductors on the first attempt
- Helped predict 3 of 4 measurements of engineered E. coli growth
- Independently designed an AI system that gave safer medical answers, and cut serious fabricated results in AI-written papers from 90% to 4%.

Reading Recommendation: https://t.co/DUvhlbbiWz and kudos to @SRSchmidgall and team!
LINKS: https://arxiv.org/html/2608.26701v1
--
## @cwolferesearch — 2 шт.

T=2093731741550719037 | @cwolferesearch | 2026-08-29T16:05+00:00 | L943 RT151 C32 V176872 | rt
URL=https://x.com/cwolferesearch/status/2093731741550719037
RT-OF @SRSchmidgall (L943): Today, we're excited to share early progress on using Gemini to accelerate scientific discovery in the real-world. We present an extension of Co-Scientist which we use to collaborate with scientists across materials science, biology, and computer science. https://t.co/jwDF5aSK28
RT-URL=https://x.com/SRSchmidgall/status/2093380426924708082
TEXT: RT @SRSchmidgall: Today, we're excited to share early progress on using Gemini to accelerate scientific discovery in the real-world. We pre…
--
T=2093827393928536145 | @cwolferesearch | 2026-08-29T22:25+00:00 | L48 RT3 C6 V3943 | thread(2)
URL=https://x.com/cwolferesearch/status/2093827393928536145
TEXT: link to post: https://t.co/o8vPidMOWJ
[->] Crazy that Terminal Bench 4 has already been released (only ~a month after Terminal Bench 3, though they mention this marks a transition to a continuous-style benchmark). 

It's really interesting to study the high-level patterns in improvement to a popular benchmark like this.

The key idea is to simply respond to user feedback (or general observations from running evals) from Terminal Bench 3 by fixing known issues and reduce noise as much as possible by removing tasks, improving tasks, and fixing eval infra issues. 

Recall that Terminal Bench 3 has 74 tasks across seven domains. In Terminal Bench 4, there are no new tasks, but eight tasks are removed due to:
- saturation
- high rate of refusals
- existing public solutions
- other quality or platform-compatibility issues

Tasks are considered saturated when all models in the latest generation model families solve the task with 100% accuracy in 5 trials.

19 of the tasks are also patched with fixes. In the blog post, they mention that these fixes come in a variety of forms (e.g., new instructions, environment changes, verifier updates, etc.) and are identified via a combination of user feedback or issues found by the developers within leaderboard runs. Most of these issues are discovered via trial and error. Put simply, it helps to look through eval results, question scores, and investigate whether unexpected trends in performance are legitimate or coming from a benchmark issue. 

Interestingly, Terminal Bench 4 also tries to improve calibration of resources / infra used to run tasks in Terminal Bench. This is a really interesting area of agentic evals that shows why evaluating agents is so nuanced and difficult to get right. 

We've seen in prior work (e.g., https://t.co/MRvkMzJlfP) that changing resources limits in evals can meaningfully impact performance. Specifically, there are a few key infra factors that tend to make a big impact on benchmark scores, such as:

1. OOM errors 
2. CPU limits
3. Timeouts

Ideally, we do not want our agent to fail tasks because it is too resource-constrained. However, providing unlimited resources to the agent is also not a good solution. For example, the agent can spend way too long solving a task via a brute force solution if it has no timeout. 

We want to find a middle ground. We should set resource limits high enough to avoid infra failures, but not so high that we artificially inflate the model's problem solving ability. To do this, we can start with lower resource limits and increase them until we find a "smooth" region where the amount of noise in the eval seems to level out, providing reproducible results that are not significantly impacted by infra failures. For Terminal Bench 4, a timeout of 8 hours is found to yield minimal timeout failures and reduce benchmark noise.

The key idea here is that we need to consider things like CPU/RAM limits, timeout policies, hardware, API latency, and other infrastructure details when running evals. These factors are unrelated to the quality of the model but can create significant fluctuation in benchmark scores. We need to account for this and try to reduce the amount of variance / noise caused in the benchmark by factors other than model quality. 

Notably, Terminal Bench 4 also marks the transition of Terminal Bench to a continuously evolving benchmark. In my opinion, this is a great move that is necessary given evolving model capabilities. Benchmarks need to adapt / evolve regularly to stay relevant!
LINKS: https://tbench.ai/news/terminal-bench-4-0 ; https://www.anthropic.com/engineering/infrastructure-noise
--
## @dexhorthy — 2 шт.

T=2093757824849301669 | @dexhorthy | 2026-08-29T17:49+00:00 | L296 RT16 C14 V20785 | post
URL=https://x.com/dexhorthy/status/2093757824849301669
TEXT: everyone wants to sell you a software factory, but as @davidcrawshaw  (founder tailscale, https://t.co/kFFHzfu9QD) would probably say, these things need to be open systems

I went deep with @vaibcode  on the future of software factory architecture, and the tradeoffs between turnkey stacks and owning+composing the system

full video here: https://t.co/ocOr5IDHVD
LINKS: http://exe.dev ; https://www.youtube.com/watch?v=tGbjIvvYuHE
--
T=2093802050513703221 | @dexhorthy | 2026-08-29T20:44+00:00 | L2305 RT143 C33 V55440 | rt
URL=https://x.com/dexhorthy/status/2093802050513703221
RT-OF @threepointone (L2305): theory: in &lt;domain you care about&gt; there are only about 500 people in the world who really matter (ie: do the work, have impact, genuine, non grifter, non blowhards, will deepen and broaden your own skills and perspectives). it is your job to find them and make friends with them.
RT-URL=https://x.com/threepointone/status/2093608977300897850
TEXT: RT @threepointone: theory: in &lt;domain you care about&gt; there are only about 500 people in the world who really matter (ie: do the work, have…
--
## @emollick — 4 шт.

T=2093664018363822585 | @emollick | 2026-08-29T11:36+00:00 | L37 RT1 C2 V8527 | post
URL=https://x.com/emollick/status/2093664018363822585
TEXT: As I was saying https://t.co/hqfYLAE5eq
--
T=2093747487433478296 | @emollick | 2026-08-29T17:07+00:00 | L133 RT18 C15 V22251 | post
URL=https://x.com/emollick/status/2093747487433478296
TEXT: This paper does a good job of showing the promise and gaps of autonomous AI scientists. Big question is how much more advanced models close those gaps.
QUOTED @SRSchmidgall: Today, we're excited to share early progress on using Gemini to accelerate scientific discovery in the real-world. We present an extension of Co-Scientist which we use to collaborate with scientists across materials science, biology, and computer science. https://t.co/jwDF5aSK28
--
T=2093819069552021740 | @emollick | 2026-08-29T21:52+00:00 | L532 RT21 C55 V41984 | post
URL=https://x.com/emollick/status/2093819069552021740
TEXT: Was just skimming through the webpages of some of my favorite hard science fiction authors and wow the majority of them hate LLMs: a surprising number of them because they think it is a useless stochastic parrot, some because of IP￼, and a minority because of existential risk.
--
T=2093823173619769806 | @emollick | 2026-08-29T22:08+00:00 | L445 RT11 C29 V19484 | post
URL=https://x.com/emollick/status/2093823173619769806
TEXT: It might soon be disrespectful to use a weaker model for human-facing content: “you saved 6 cents to make me read through error-filled &amp; badly written AI slop? At least send me high quality and low-error slop that doesn’t waste my time.”

(This is how I feel about AI X comments)
--
