# X-FEED 2026-07-30 part 8/9 | items: 8

## @omarsar0 (продолжение)

T=2082602113558077599 | @omarsar0 | 2026-07-29T23:00+00:00 | L109 RT18 C16 V9430 | post
URL=https://x.com/omarsar0/status/2082602113558077599
TEXT: Super interesting new work from NVIDIA.

(bookmark it)

They suggest building agents as Python objects.

Very cool idea and I think it could a lot with agent reliability.

More below:

Agent development today spreads across prompt templates, tool schemas, callback code, and workflow graphs. NOOA replaces all four with one abstraction.

An agent is a Python object. Its methods are the actions the model can take, its fields hold state, its docstrings are the prompts, and its type annotations act as contracts.

A method whose body is "..." gets completed at runtime by a validated LLM loop. A method with a normal body stays deterministic Python.

That single convention puts the boundary between probabilistic and deterministic behavior right in the source.

Agent behavior becomes testable, traceable, and refactorable with the same tools you already use on the rest of your codebase.

NVIDIA reports six model-facing ideas combined on one surface, including pass-by-reference over live objects and model-callable harness APIs for context and events, evaluated on SWE-bench Verified, Terminal-Bench 2.0, and ARC-AGI-3.

Paper: https://t.co/PCtFtVY8rT

Learn to build effective AI agents in our academy: https://t.co/1e8RZKs4uX
LINKS: https://arxiv.org/abs/2607.20709 ; https://academy.dair.ai/
--
## @sayashk — 2 шт.

T=2082419281317282173 | @sayashk | 2026-07-29T10:53+00:00 | L79 RT15 C9 V6973 | rt
URL=https://x.com/sayashk/status/2082419281317282173
RT-OF @random_walker (L79): Imagine if car safety testers only did tests on the engine and called it a day, instead of testing the vehicle itself. This is roughly the situation in our understanding of the mental health risks of chatbots. Most of the research is on models but models aren't what people interact with. Chatbots used to be thin wrappers around models, so this used to be an acceptable approximation that enabled automated testing, but not anymore. The chatbot scaffold drastically affects the safety profile, in ways both good and bad: memory and personalization, search and other tools, additional guardrails and filters, drift during extended interactions, and more. Research needs to keep pace with the changing tech and companies need to provide better access to external researchers.
RT-URL=https://x.com/random_walker/status/2082417715558404140
TEXT: RT @random_walker: Imagine if car safety testers only did tests on the engine and called it a day, instead of testing the vehicle itself. T…
--
T=2082560105317319033 | @sayashk | 2026-07-29T20:13+00:00 | L7 RT1 C1 V590 | rt
URL=https://x.com/sayashk/status/2082560105317319033
RT-OF @BenDLaufer (L7): Should AI companies be able to outsource safety? In a new @FastCompany op-ed, I connect recent developments involving Anthropic, Kimi K3, and the EU AI Act to a question from my research: how do rules aimed at one company change the behavior of others in the AI supply chain? https://t.co/Ut2GEItxAr
RT-URL=https://x.com/BenDLaufer/status/2082556241554083965
TEXT: RT @BenDLaufer: Should AI companies be able to outsource safety? In a new @FastCompany op-ed, I connect recent developments involving Anthr…
--
## @sh_reya — 1 шт.

T=2082503669145317570 | @sh_reya | 2026-07-29T16:29+00:00 | L104 RT0 C6 V17547 | thread(2)
URL=https://x.com/sh_reya/status/2082503669145317570
TEXT: I don’t love the premise that “the same amount of basic research is done in industry as academia” (doesn’t feel broadly true); I think it is extremely CS (and AI) coded; but I am optimistic about this 4 year program. Currently there’s a massive opportunity cost for talented American undergrads to pursue a CS PhD. Dare i say, I hope the American government takes a vested interest in Making PhD Programs Attractive Again
[->] I don’t think enough academics realize how unattractive getting a PhD is for the best undergrads, who are choosing between frontier lab/startup (which does a lot of CS work btw, not just AI) and PhD. It is not just about money. In both situations the environment is conducive to learning and growth; the people around you are working 996. In industry, students (from what I hear) feel they can get good mentorship, faster feedback cycles, can develop influence/rise up quickly. In academia, the perception is that the PIs have “checked out” or spend most of their time in operating roles in industry, with little time for hands-on mentorship. 5-6 years with little direction and mentorship isn’t always the greatest bet for a bright 21 year old
QUOTED @mkratsios47: Today, roughly the same amount of basic research is done in industry as in academia. It’s time our doctoral training reflected that. 

@NSF is launching a first-of-its-kind 4-year PhD program at more than 30 universities. Students will spend a year+ embedded with industry partners doing research that informs their dissertation.
--
## @simonw — 4 шт.

T=2082324003231060151 | @simonw | 2026-07-29T04:35+00:00 | L214 RT21 C48 V27519 | post
URL=https://x.com/simonw/status/2082324003231060151
TEXT: A new TIL on adding custom MCP servers to both the ChatGPT and Claude regular chat interfaces - it's a little less obvious than I had hoped, but I got there in the end https://t.co/ahwaFyJYtp https://t.co/kPqgNoi4Uh
LINKS: https://til.simonwillison.net/llms/mcp-in-claude-and-chatgpt
--
T=2082471910835998945 | @simonw | 2026-07-29T14:22+00:00 | L42201 RT797 C387 V2694304 | rt
URL=https://x.com/simonw/status/2082471910835998945
RT-OF @ScienceYael (L42201): ahhhhhhh so I'm hiring a tech to help me out in lab and screening applications now and THE KIDS ARE USING PROMPT INJECTION!!!!!! 2.25 pt white text, here's what I've found so far https://t.co/s8TtKxqUgE
RT-URL=https://x.com/ScienceYael/status/2082175224007848019
TEXT: RT @ScienceYael: ahhhhhhh so I'm hiring a tech to help me out in lab and screening applications now and THE KIDS ARE USING PROMPT INJECTION…
--
T=2082487009642479972 | @simonw | 2026-07-29T15:22+00:00 | L190 RT11 C30 V16703 | thread(2)
URL=https://x.com/simonw/status/2082487009642479972
TEXT: My current weird hobby is having GPT-5.6 Pro "over-analyze" things

&gt; I want a deep character study of Bebop and Rocksteady - I want to understand their motivations, their interests, their hopes and aspirations, how they differ from each other - really over-analyze this https://t.co/vcALVDsNvj
[->] https://t.co/VYB63Tki1H https://t.co/YBmBYEbT60
LINKS: https://chatgpt.com/share/6a6a1c95-177c-83e8-b42c-ab534915d3d2
--
T=2082641030093127768 | @simonw | 2026-07-30T01:34+00:00 | L175 RT6 C16 V18728 | post
URL=https://x.com/simonw/status/2082641030093127768
TEXT: GPT-5.6 found optimizations that "reduced end-to-end serving costs by 20%" for OpenAI to serve that model

Presumably that's billions of dollars a month in savings at this point?
QUOTED @reach_vb: Codex analysed production traffic, improved load balancing, rewrote production GPU kernels and ran hundreds of experiments on its own speculative-decoding model.

The kernel improvements reduced end-to-end serving costs by 20%, while speculative decoding improved token-generation efficiency by more than 15%.
--
