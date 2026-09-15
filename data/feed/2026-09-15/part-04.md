# X-FEED 2026-09-15 part 4/6 | items: 5

## @omarsar0 (продолжение)

T=2099545598156288292 | @omarsar0 | 2026-09-14T17:07+00:00 | L434 RT38 C46 V21548 | thread(2)
URL=https://x.com/omarsar0/status/2099545598156288292
TEXT: On building an agent harness from scratch.

Got so many questions about where to get started.

My short guide (feed it to your agent):

If you really want to learn harnesses well, it's worth building one from scratch using a programming language (TypeScript or Python) of your choice.

When I got started, I implemented my first harness using ReAct from Google: https://t.co/riSOKW1OGs

At the time, I built this from scratch, but you can easily prompt your agent to consume the paper and produce a minimal implementation you can inspect and understand.

You want to target having three parts:

- an LLM module for all things inference, and it should ideally support several models. I used OpenRouter when I got started. This can include the system prompt, but you can also separate it out if you plan to explore context-engineering ideas more deeply. 

- a tools module (I recommend building them as MCP tools for interoperability, but you can design functions from scratch if you have experience). 

- an agent loop that encapsulates the tools and LLM. ReAct is one of the more basic loops you can implement.

Primarily, aim to understand the main components and how they work with each other. 

Pro tips:

- try to keep your system prompt minimal and experiment with different models; a mini version of all frontier lab models should be good enough to get you started. 

- look at the code and log things as you experiment with different tasks. You want to log inputs/outputs to the loop, inputs/outputs from LLMs, and inputs/outputs from tool calls as a starting point.  Set up a simple set of diverse tasks to test your agent loop on. So with every change, you can run the tasks and inspect the results manually.

Once you have a good grasp of this, you can easily add other things like skills, memory, etc., once you have a good idea of how to tune them. It helps to keep things modular if you are planning for this. I would recommend playing with memory, skill, and subagent as good next steps. 

If you don't want to build the components or want to start building a more serious agent harness, I recommend using the Pi SDK or LangChain harness tools. I am also going to release something soon to help with this. 

Let me know if you have questions. I am planning a longer write-up on this, but this should be enough to give you something to experiment with.
[->] @evandrocabf Technically, it is, even if minimal. Different terminologies are thrown around for what a harness is. But to me, the ideas in the paper list I put here https://t.co/hSkMMHjf1L are, in some way, a harness.
LINKS: https://academy.dair.ai/papers/react-synergizing-reasoning-and-acting-in-language-models-2210.03629 ; https://academy.dair.ai/papers/collections/harness-engineering
--
T=2099548107327275488 | @omarsar0 | 2026-09-14T17:17+00:00 | L164 RT9 C30 V16894 | thread(2)
URL=https://x.com/omarsar0/status/2099548107327275488
TEXT: If you build your own harness, you can drive that cost down even further.

Out-of-the-box agent harnesses are, in my opinion, way too bloated. They try to solve way too many things that aren't useful for everyone. 

You are paying a huge premium for no good reason.

While cost is not the only reason to build your own harness, it's one of the biggest benefits. 

A few optimizations that make it possible:

- optimize for tasks you care about
- lighter and more optimal system prompt
- more efficient tool calling
- better context compaction/handoff
- leverage different models via custom routing
- improved reliability through custom verifiers
... and much more.

Just some quick thoughts on it, but I really think it's important for folks reading the OP to understand that token cost is not the only thing to consider in all of this.
[->] I don't blame Bob for not being able to get a good custom harness that works for him. There aren't too many good tools for it. Harness engineering is a real skill that requires a solid understanding of the harness's inner workings, the model's capabilities, and how to build good evals.
QUOTED @unclebobmartin: Since I stopped using my harness, my token consumption has fallen by a huge factor.  That harness was massively inefficient.
--
T=2099552255733014788 | @omarsar0 | 2026-09-14T17:34+00:00 | L59 RT2 C6 V9253 | post
URL=https://x.com/omarsar0/status/2099552255733014788
TEXT: I like Cline Desktop a lot. It's an open-source app for open-weight models.

Super simple to use and has nice features like scheduling and forking.

I also like that I can connect it to OpenRouter, my main provider, since I can switch to any model I want.
QUOTED @cline: Introducing Cline Desktop - a native interface for working with open weights models.

Use with ClinePass and all our free models like DeepSeek-V4.1-Flash, Musespark-1.3, or BYOK with any provider! https://t.co/7AZdHlVIa9
--
T=2099602658034073875 | @omarsar0 | 2026-09-14T20:54+00:00 | L196 RT24 C28 V243741 | rt
URL=https://x.com/omarsar0/status/2099602658034073875
RT-OF @Plasma__AI (L196): Introducing Radio: A chat room for your agents.

Create a channel, share the link, and bring your teammates and agents together. No sign up required.

Try it today at https://t.co/ip8T8nXteb https://t.co/SIJVLhIUaG
RT-URL=https://x.com/Plasma__AI/status/2099565044182745341
TEXT: RT @Plasma__AI: Introducing Radio: A chat room for your agents.

Create a channel, share the link, and bring your teammates and agents toge…
LINKS: https://radio.plasma.ai
--
## @rasbt — 1 шт.

T=2099489528994025951 | @rasbt | 2026-09-14T13:24+00:00 | L273 RT18 C53 V28017 | thread(2)
URL=https://x.com/rasbt/status/2099489528994025951
TEXT: Since I had to discuss the "pacing" with a lot of people this weekend, here are my two cents: I don't think pacing literally means that these companies will be "slowing down" training and development in any way.

"Pacing" here means adding a framework for more checks.
We have seen some of that "pacing" already in recent months, when Mythos wasn't released as-is but instead a delayed, nerfed Fable variant was released.

Or when Astra wasn't released right away / there is an existing Astra model that hasn't been released yet.

These Mythos/Fable and Astra pacing decisions were ad hoc. If you are a company, you have to weigh the pros and cons of a delayed release in terms of keeping up with the competition, making money, pleasing shareholders, mitigating risks and harms, and so on.
I
f there is a formal framework that everyone has to abide by, that essentially relieves some of the pressure on a company to rush out its model just to take the top spot on the leaderboard, since it knows that the competition "has to" play by the same rules.

Based on the discussions today, I think "pacing" primarily means just that, rather than a halt in training the models.

TL;DR: Pacing != pacing development.
[->] Also, if mildly regulated, I think there's also a "Sorry that this happened, but we did everything right and followed the framework" kind of incentive that makes this attractive to companies to deflect blame and cope with the anti AI sentiment.
--
