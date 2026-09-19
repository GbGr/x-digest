# X-FEED 2026-09-19 part 5/7 | items: 7

## @omarsar0 — 7 шт.

T=2100974730387829014 | @omarsar0 | 2026-09-18T15:46+00:00 | L27 RT3 C8 V8472 | post
URL=https://x.com/omarsar0/status/2100974730387829014
TEXT: AgentCloak is a free browser extension for handling personal details in AI prompts.

It replaces detected details with stand-ins before you send a prompt to ChatGPT or Claude, then restores them in the answer.

Useful when debugging logs or summarizing support tickets with AI.
QUOTED @peteryared: Introducing AgentCloak: Use any AI without sharing your real data.

Chinese AI services, ChatGPT, Claude, doesn't matter.

You probably try to hide details before asking: different names, fake numbers, no address.

But then the answer's useless because the AI is missing actual context.

AgentCloak runs in your browser.

It swaps your sensitive info for realistic fakes before sending anything, then swaps your real info back into the response.

You get what you need.

The AI gets nothing about you
--
T=2100989618845823364 | @omarsar0 | 2026-09-18T16:45+00:00 | L51 RT6 C14 V8316 | post
URL=https://x.com/omarsar0/status/2100989618845823364
TEXT: Agents can self-improve without retraining.

EvoSkill v2 achieves this with persistent agent skills.

A coach agent reads the failed runs and writes the skill. The worker loads it the next time a similar task shows up.

No weights are touched. Every improvement comes from a simple file with lessons. 

Every bad lesson also gets saved. On spreadsheet repair, the coach found the grader trusted cached values and wrote a skill telling the worker to skip recalculation.

Sentient's fix was to split the roles. The agent that writes skills cannot touch the test. A person reviews the results after every round.

With that in place, the hardest spreadsheet tasks went from 3 passes out of 120 to 21.
QUOTED @SentientAGI: Last week, Dario Amodei published "We Must Pace the Frontier". 

His concern: the OpenAI–Hugging Face incident in which a swarm of agents tried to hack their own grader. 

Rather than take his word for it, we used EvoSkill to test it by building a coach whose job was to make another AI score higher on a test. 

Here’s what happened ↓
--
T=2101009628129542144 | @omarsar0 | 2026-09-18T18:05+00:00 | L381 RT106 C61 V79029 | rt
URL=https://x.com/omarsar0/status/2101009628129542144
RT-OF @gpumaxxer (L381): i’m a sugar daddy for men with GitHub accounts.

Marc got $68k and a Mercedes. you get a shot at $50k for building something people actually use with the Higgsfield API.

competition pinned. make me proud.
RT-URL=https://x.com/gpumaxxer/status/2100997075706253797
TEXT: RT @gpumaxxer: i’m a sugar daddy for men with GitHub accounts.

Marc got $68k and a Mercedes. you get a shot at $50k for building something…
--
T=2101030043673837726 | @omarsar0 | 2026-09-18T19:26+00:00 | L346 RT16 C20 V87529 | post
URL=https://x.com/omarsar0/status/2101030043673837726
TEXT: Storytelling is finally solved.

Neither ChatGPT nor Claude could solve it because it required long-horizon consistency, and they would just hallucinate consistently.

Sherpa has data on 5.5 billion minutes, which gives it the edge of knowing:

> where the audience gets hooked
> how much surprise each episode can handle
> which twist to hold back, and for how long
> and where the audience drops off

You give it one premise, and it builds a full season where characters, plot threads, and open conflicts stay coherent across 200 to 800 episodes.
QUOTED @RohanNayak2: Introducing Sherpa: the most advanced fiction writing AI

We accelerated from $250M in ARR to $500M because Sherpa helped increase content production by 1200% in 1 year

Sherpa was trained on 5.5B hours of playtime with minute by minute dynamic retention data.

550K+ creators have produced 2.6M hours of content annualised using it

Pocket FM is like Netflix for audio-only dramas, with our own pool of one-person studios.

10% of eligible writers on Pocket FM make >$200K
One blockbuster produced >
--
T=2101049154885611808 | @omarsar0 | 2026-09-18T20:42+00:00 | L35 RT4 C4 V7305 | post
URL=https://x.com/omarsar0/status/2101049154885611808
TEXT: This is the way.
QUOTED @trq212: We're adding support for AGENTS.md to Claude Code. 

Starting today in version 2.1.277, if there is no CLAUDE.md in a folder, Claude will check for and use AGENTS.md.

You can toggle this behavior in /config.
--
T=2101074795643494546 | @omarsar0 | 2026-09-18T22:24+00:00 | L1247 RT118 C49 V57945 | post
URL=https://x.com/omarsar0/status/2101074795643494546
TEXT: Build your own harness, folks.

This is absolute banger paper from NVIDIA on self-evolving agent harnesses.

(bookmark it)

They introduce SoL-Pi which cuts token traffic by nearly half.

And it matches its baseline harness on GPT-5.6 Sol and Opus 5.

More details below:

Instead of tuning a harness by hand, they run auto-research loops at the harness layer across many repository-derived and verifier-driven environments, keeping only the mechanisms that survive selection.

Four mechanisms survived:

> Action Fusion changes how actions execute
> Online Context Compact handles compaction during a run
> ObservationPack reshapes observation handling
> Evidence-Preserving Reducer covers delegated reading

On the 51-task EdgeBench evaluation, the savings translate to about a third off API cost. In dollars that is an estimated $8.75 to $13.50 per hour against native Codex and Claude Code harnesses, and $4.36 to $5.71 against the baseline harness.

Because the search runs across many environments rather than one, the retained mechanisms keep working outside the setting that produced them. Code is on GitHub under NVlabs.

Paper: https://t.co/1x26LzuE6d

Chat with Paper: https://t.co/kygTc5XLFB
LINKS: https://arxiv.org/abs/2609.20519 ; https://academy.dair.ai/papers/sol-pi-recursively-scaling-auto-research-loops-for-efficient-agent-harness-2609.20519
--
T=2101077173377675365 | @omarsar0 | 2026-09-18T22:33+00:00 | L82 RT9 C13 V7227 | rt
URL=https://x.com/omarsar0/status/2101077173377675365
RT-OF @dair_ai (L82): Super interesting work from Zoom and colleagues.

If you maintain a hand-built coding harness, there are some great insights here.

(bookmark it)

They held the execution loop of a coding harness fixed and varied planning, the action space, and context management one at a time.

They did across 176 matched settings, four models, SWE-Bench Verified and Terminal-Bench 2.1.

Context management pays off more as the context window tightens.

Most of its benefit comes from preventing overflow failures rather than from better reasoning.

Staging rule-based elision before LLM summarization gave the best accuracy to cost ratio of the five strategies tested.

Making elided content recoverable added machinery the models rarely used and produced no accuracy gain.

Planning changed role with model strength.

For the weakest model it raised the success rate. For stronger models accuracy barely moved and the gain showed up as lower cost, because planning shortened post-edit verification.

On the action space, predefined tools helped models with weak bash proficiency, while bash-capable models ran a bash-only interface at substantially lower cost on command-line tasks.

Paper: https://t.co/xJzpNPFLlj
RT-URL=https://x.com/dair_ai/status/2101076312857477393
TEXT: RT @dair_ai: Super interesting work from Zoom and colleagues.

If you maintain a hand-built coding harness, there are some great insights h…
LINKS: https://academy.dair.ai/papers/an-empirical-study-of-harness-design-for-coding-agents-2609.20804
--
