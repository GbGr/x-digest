# X-FEED 2026-07-29 part 9/12 | items: 9

## @omarsar0 — 9 шт.

T=2082105300392542246 | @omarsar0 | 2026-07-28T14:06+00:00 | L137 RT30 C14 V11203 | post
URL=https://x.com/omarsar0/status/2082105300392542246
TEXT: New research from Meta and CMU.

This one is on agentic context management for long horizon tasks.

(bookmark it)

Production agents accumulate context every turn. The usual fix compresses on a token threshold and throws the remainder away, so the trigger sometimes fires for reasons unrelated to what the agent is currently working on.

ACM hands the agent purpose-built context editing tools. It decides when to compress, offloads what it drops into an external memory store, and queries that store later when it needs the detail back. Compression shifts from short-term to long-term memory.

They also build a post-training pipeline on high-quality context management demonstrations. That yields a 27% relative gain on BrowseComp-Plus and gets close to open-source models 40 times larger.

Better context management lowers peak token pressure, lets the agent explore longer before running out of room, and produces more consistent solutions across independent trials of the same task.

Code, data, and checkpoints are released.

Paper: https://t.co/ZRWaYrAwfg

Learn to build effective AI agents in our academy: https://t.co/1e8RZKs4uX
LINKS: https://arxiv.org/abs/2607.23809 ; https://academy.dair.ai/
--
T=2082118182718894202 | @omarsar0 | 2026-07-28T14:57+00:00 | L63 RT10 C6 V9627 | post
URL=https://x.com/omarsar0/status/2082118182718894202
TEXT: Interesting paper. Frontier models can exhibit invisible reasoning by leveraging semantically irrelevant filler tokens. More understanding of CoT.
QUOTED @dair_ai: Very interesting paper on LLM reasoning.

They find that frontier models can exhibit invisible reasoning by leveraging semantically irrelevant filler tokens.

In other words, invisible reasoning can serve objectives entirely invisible to
CoT monitoring.

Paper: https://t.co/ElnZdLYIQG

Learn to build effective AI agents in our academy: https://t.co/LRnpZN7L4c
--
T=2082128185597022324 | @omarsar0 | 2026-07-28T15:36+00:00 | L49 RT7 C9 V10772 | thread(4)
URL=https://x.com/omarsar0/status/2082128185597022324
TEXT: I am not even trying to make these perfect or anything like that. I work on models that generate interactive worlds and simulations. 

This can be significantly improved with more effort. 

My focus right now is to build the harness that generates these and works across models.
[->] Not sure if this is good enough, as I have never built anything remotely close to this with previous models. 

The harness I built also works for GPT-5.6-Sol. Sharing more results soon. These runs can take a few hours.

Another example below. Not perfect but great start. https://t.co/IPZYDO66Ow
[->] Opus 5 built this flight simulator in one go.

Using only Three.js. 

The trick to getting this quality and higher (if you prompt harder) seems to be in building a good judge-executor harness. The judge keeps the loop running to improve output quality. https://t.co/PIivNHtZ0r
[->] For a fun little example of how the harness works, which is essentially built on top of my dynamic workflows functionality. 

The harness dynamically spins out a subagent (as needed) to critique and improve things like graphics and playability. This is super interesting. 

This is for another open-world game I have been building.
--
T=2082137823977807919 | @omarsar0 | 2026-07-28T16:15+00:00 | L18 RT1 C1 V8035 | post
URL=https://x.com/omarsar0/status/2082137823977807919
TEXT: I spent the last two years rebuilding my work around agents. Research, writing, and my daily analysis of the field now run as loops I keep refining, and the gains stack with every new model release.

Very little of that way of working has reached research labs. @ReactorfieldAI is a 4-week fellowship built to bring it to scientists and deep tech teams.
QUOTED @jamessinka: AI transformed coding, science is next

@ReactorfieldAI makes scientists and deep tech startups AI-native

Built by me and @berkbuilds to accelerate science with frontier AI https://t.co/4rETjNfepp
--
T=2082139988544602355 | @omarsar0 | 2026-07-28T16:23+00:00 | L470 RT17 C59 V49164 | thread(4)
URL=https://x.com/omarsar0/status/2082139988544602355
TEXT: I quit using Opus 5 after the first few sessions. 

I can only explain it as a very "ignorant" model. It does stuff I didn't ask for. It ignores my skills and some of my tools. It broke pretty much all my workflows/loops. 

What a weird model. Not feeling it.
[->] The crazy thing is that it is really good at stuff like developing complex worlds, animations, simulations, etc. But as a coding agent, I prefer GPT-5.6-Sol for now.
[->] I get it that I need to adjust my workflows and skills and not get in the way of it. I totally understand that. I have been doing that already with newer models that understand intent much better. But this isn't plug-and-play. There is a lot of stuff it just does wrong. Makes me very feel uncomfortable using it.
[->] I say it like it is. Based on the reaction to this, I get the feeling that many others are also struggling with Opus 5. Can someone on the Claude team help us understand what's up with this model?
QUOTED @theo: I do not like Opus 5 as much as I hoped to :(
--
T=2082161529600741441 | @omarsar0 | 2026-07-28T17:49+00:00 | L86 RT15 C6 V9919 | post
URL=https://x.com/omarsar0/status/2082161529600741441
TEXT: Highly recommend reading. 

I agree that coding agents are great for scientific computing, but you can't just autoresearch yourself to useful discoveries (yet). I still find myself steering and collaborating closely with my research agents. 

Expertise matters a lot. https://t.co/bpIyPdPapQ
QUOTED @OpenAI: Coding agents are helping scientists spend more time advancing research, taking on everything from routine maintenance and targeted optimization to complete redesigns and new systems.

While agents can reliably execute on ambitious projects, researchers must still define the scientific questions, verify results, and take a stance on long-term ownership.
--
T=2082173006814568516 | @omarsar0 | 2026-07-28T18:35+00:00 | L86 RT1 C2 V20757 | post
URL=https://x.com/omarsar0/status/2082173006814568516
TEXT: Great updates to MCP. It's maturing fast!

With MCP now being stateless, it's going to make it even easier to adopt across applications. It should also be easier to manage and deploy MCP servers. Cool stuff!
QUOTED @ClaudeDevs: MCP 2026-07-28 is live and it's the largest update to the protocol since launch.

MCP is now stateless, making it easier to deploy and scale remote servers. 

https://t.co/K8KqxbUh4e
--
T=2082178403097018879 | @omarsar0 | 2026-07-28T18:56+00:00 | L17 RT3 C4 V7326 | post
URL=https://x.com/omarsar0/status/2082178403097018879
TEXT: Good takes from @finkd. I like the new movement of building pro-human AI. Mark doesn't get enough credit for all the support he has given open-source over the years. I agree; open-source plays an essential role in the future worth building, and I am glad he mentioned it. https://t.co/jRYisuLlfv
QUOTED @finkd: I wrote about why we believe the future is for everyone. More coming about a positive vision for a world with superintelligence soon.
--
T=2082182306177933717 | @omarsar0 | 2026-07-28T19:12+00:00 | L113 RT52 C27 V38375 | rt
URL=https://x.com/omarsar0/status/2082182306177933717
RT-OF @bageldotcom (L113): We are releasing WorldDiT, a unified architecture for robotics world modeling and control.

On the LIBERO benchmark, it performs the best among all publicly released methods that do not need a VLM to generate actions. Its size and performance sit on the reported Pareto frontier. https://t.co/iC7XglykVn
RT-URL=https://x.com/bageldotcom/status/2082179134336512366
TEXT: RT @bageldotcom: We are releasing WorldDiT, a unified architecture for robotics world modeling and control.

On the LIBERO benchmark, it pe…
--
