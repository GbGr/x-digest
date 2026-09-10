# X-FEED 2026-09-10 part 7/10 | items: 6

## @omarsar0 (продолжение)

T=2097747814885273746 | @omarsar0 | 2026-09-09T18:03+00:00 | L39 RT9 C5 V5129 | rt
URL=https://x.com/omarsar0/status/2097747814885273746
RT-OF @dair_ai (L39): Wild paper from Microsoft and colleagues.

They show a new attack that reconstructs the text a local LLM generates by watching CPU cache activity while it detokenizes.

Earlier cache attacks needed something unusual in the deployment, such as shared data memory, CPU offloading, or a Mixture-of-Experts architecture. This work targets the detokenizer, which runs in default inference pipelines.

The method has two stages.

1) Flush+Reload on shared tokenizer code detects when decoding happens, which lets the attacker fire Prime+Probe at the right moment and isolate token-dependent cache activity.

2) A clustering and language-model pipeline then recovers readable text from the noisy observations.

They evaluate across datasets, hardware platforms, inference frameworks and model families, including real local deployments and agentic systems.

The widely used tokenizer implementations are susceptible, and they are embedded in many popular local LLM products and agent frameworks. OpenClaw is demonstrated directly.

Paper: https://t.co/KPLJVpoyBZ
RT-URL=https://x.com/dair_ai/status/2097746964662366376
TEXT: RT @dair_ai: Wild paper from Microsoft and colleagues.

They show a new attack that reconstructs the text a local LLM generates by watching…
LINKS: https://academy.dair.ai/papers/detokenization-leaks-reconstructing-local-llm-outputs-from-cache-traces-2609.06674
--
T=2097752941507535140 | @omarsar0 | 2026-09-09T18:24+00:00 | L15 RT1 C2 V7778 | post
URL=https://x.com/omarsar0/status/2097752941507535140
TEXT: Better models don’t automatically mean smaller AI bills.

Sometimes they mean you finally have a reason to run the workflow you couldn’t get working before.  

That’s what makes GPT-6 Astra interesting to me.  

Once a model can research, build, inspect, and refine, you start giving it more ambitious tasks. A single response becomes an entire working session.  

The useful question is no longer just “what does a million tokens cost?”  

It’s “what can I get done with this budget?”  

That’s also why cashback on inference is worth paying attention to. On work you were already going to run, getting some of the spend back gives you a choice: keep the savings or fund another experiment.  

But the goal should never be to burn more tokens.  

It should be to get more verified, useful work out of the same budget.
QUOTED @Mutchtaba2: STOP PAYING FOR TOKENS !

START GETTING PAID INSTEAD

Introducing Straitly, the first AI service that PAYS YOU for using tokens

Unlike
> Openrouter charges 5.5% service fee
> Vercel charges 2.9% payment fee
> Anthropic gives you low rate limits
> OpenAI only lets you use GPT models

Straitly:
> PAYS YOU 5% CASHBACK on all closed-source models
> 10% CASHBACK on open-source models
> High rate limits
> 177 AI models
> 99.8% reliability
> ZDR

This means that you can save up to 25% on your token bi
--
T=2097755424007373270 | @omarsar0 | 2026-09-09T18:34+00:00 | L585 RT87 C24 V52097 | post
URL=https://x.com/omarsar0/status/2097755424007373270
TEXT: Another banger paper from Google.

If you build memory for long-horizon agents, this one is worth your time.

(bookmark it)

Really nice to see how knowledge graphs are being explored in creative ways for agents. This has lots of implications for self-evolving agents.

Technical summary below:

Agents usually pick actions by generating over an accumulating history, which leaves the procedural knowledge implicit. As trajectories get longer they lose track of objectives, call tools out of order, and repeat actions that did not work.

The Procedural Graph helps to make that knowledge explicit.

A knowledge graph stores facts as entity-relation-entity triplets. A Procedural Graph stores procedures as procedure-relation-procedure triplets, so the agent can query what to do next and under which conditions.

At each step, the framework localizes the agent's active node, and a guidance model turns the surrounding subgraph into step-level guidance that biases the next action without dictating it.

The graph rewrites itself.

An LLM refiner compares failed trajectories against successful ones and edits the topology and attributes, committing only edits that hold up on held-out validation, and keeping the rejected ones on file so the same change is not proposed twice.

Starting from a minimal skeleton it builds graphs that match or beat hand-designed ones, and it helps to repair a flawed expert priors instead of inheriting them.

Paper: https://t.co/YZdhtzsSS2
LINKS: https://academy.dair.ai/papers/procedural-graphs-self-evolving-execution-structures-for-llm-agents-2609.09153
--
T=2097790938911498494 | @omarsar0 | 2026-09-09T20:55+00:00 | L113 RT11 C11 V14329 | post
URL=https://x.com/omarsar0/status/2097790938911498494
TEXT: Highly recommended. Model-harness co-optimization is where you design the harness for the task and then tune the model inside the harness.

A clear example of why you want to own the harness and the models. Harness engineering is the real deal. So much to unlock.

I have been tracking a bunch of papers showing how extremely effective this is. And there are many variants. Harvey explores RLMs, which somehow enable interesting ways to scale things. 

A few links here already: https://t.co/nOPcXIbgJr
QUOTED @nikogrupen: https://t.co/Fg8FniKQv3
LINKS: https://academy.dair.ai/papers/collections/harness-engineering
--
T=2097792763508998211 | @omarsar0 | 2026-09-09T21:02+00:00 | L852 RT179 C178 V281313 | rt
URL=https://x.com/omarsar0/status/2097792763508998211
RT-OF @gpumaxxer (L852): I’m spending my entire annual salary at Higgsfield on a billboard built like a Greek god.

Every ad slot on @marclou’s body is now Higgsfield. For HYROX.

Whoever wants to sell ad slots on their bodies, hit me up. @sydney_sweeney @KingJames 👀

fyi, my GPT-6 Astra agent is outbidding everyone automatically, f around and find out.
RT-URL=https://x.com/gpumaxxer/status/2097780427046199490
TEXT: RT @gpumaxxer: I’m spending my entire annual salary at Higgsfield on a billboard built like a Greek god.

Every ad slot on @marclou’s body…
--
T=2097822876615504345 | @omarsar0 | 2026-09-09T23:02+00:00 | L30 RT5 C7 V8444 | post
URL=https://x.com/omarsar0/status/2097822876615504345
TEXT: This is a really neat benchmark. It's super interesting that Astra starts strong and holds the lead for up to 19 hours, but Fable 5.1 catches up in the final hours.

Not entirely clear why.

Different models solve long-horizon problems with different strategies. It's no surprise that we see different trends. 

And then there is also the question of cost-performance efficiency. Qwen3.8 Max, Gemini 3.8 Flash, and Grok 4.6 are more economical for research, earning a place on the cost–performance Pareto frontier.

For AI research, things get complicated not because of the duration of the task but because agents (even with the best models) tend to stagnate due to low-quality exploration. Might be due to OOD. Or simply that agents are just simply not "creative" enough (well, at least not at human levels), which the top researchers are exceptional at, from years of experience building intuition and deep expertise. 

The other question is: where exactly are research agents spending their compute? Are they using it efficiently? Earlier work from @intology found that coding agents mostly spend compute on hyperparameter tuning, rarely attempting algorithmic research. https://t.co/BmjrGu9mYB Not sure where the research stands on that today, but all of these are interesting research questions.
QUOTED @AlexGDimakis: We are releasing AutoResearchExam, a benchmark on open-ended machine learning and engineering tasks. Our benchmark covers seven research areas including model training, data curation, AI safety and interpretability.

https://t.co/Rho35ULgS5

In each task, we give agents 24 hours with a CPU or GPU machine to develop and improve their solutions through experiments and feedback. We measure both speed and quality with a combined score. Our benchmark has a unique feature: testing if agents create imp
LINKS: https://x.com/intology/status/2056764236668493868?s=20
--
