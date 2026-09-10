# X-FEED 2026-09-10 part 6/10 | items: 6

## @omarsar0 — 14 шт.

T=2097635577474568587 | @omarsar0 | 2026-09-09T10:37+00:00 | L94 RT15 C10 V7839 | rt
URL=https://x.com/omarsar0/status/2097635577474568587
RT-OF @dair_ai (L94): Good work on improving memory for long-horizon agents.

They separate two things that agent memory papers usually collapse into one. How memories get merged when they are written, and how retrieved content gets assembled into the prompt.

The setting is a tight prompt budget of 2k to 5k tokens, where full-context prompting is off the table because of latency, cost and context limits.

RSM-full combines a cosine-gated max-member merge rule on the write side with an atom-aware grouped packer on the read side. At a 4k budget it reaches 83% of full-context quality at 32% of the token cost.

The ablations attribute the gain to both halves separately. The merge rule is worth 5.7 points over online k-means and matched DP-means. The grouped packer is worth 5.0 points over flat concatenation.

It reproduces on RealMem, beating Budget-RAG, Streaming-Proto and the A-MEM agentic memory baseline, and landing level with BM25-RAG rather than above it.

The authors state that higher-token baselines stay stronger outside this budget range.

Paper: https://t.co/W6imgK7G0H
RT-URL=https://x.com/dair_ai/status/2097555607389896732
TEXT: RT @dair_ai: Good work on improving memory for long-horizon agents.

They separate two things that agent memory papers usually collapse int…
LINKS: https://academy.dair.ai/papers/compact-memory-llm-agents-via-online-max-member-clustering-and-atom-aware-packin-2609.04915
--
T=2097675916973334684 | @omarsar0 | 2026-09-09T13:18+00:00 | L27 RT4 C8 V7770 | thread(6)
URL=https://x.com/omarsar0/status/2097675916973334684
TEXT: Human review and the PR gate stay in place. This adds a quality layer before code ever gets there.

Install it with one command in the terminal, or from the Claude Code, Codex, or Kiro marketplace. It also runs as an MCP server for any MCP-compatible agent.

More here
https://t.co/IcfP3RxIWC

Thanks to the Qodo team for partnering on this post.
[->] The findings were specific.

My new ingestion path marked papers as public without checking for full text. That is the exact check the refactor was meant to add.

The chat endpoint was accepting questions on papers with no verified text.

Summaries were being stored as full documents.

A paid lesson page was missing an enrollment check.

All of this surfaced before a PR existed.
[->] I tested the beta on real work.

I had just refactored our academy's paper ingestion pipeline. It should guarantee that a paper has verified full text before Paper Chat can use it.

I ran "qodo review" on my uncommitted changes before opening a PR.

It reviewed 373KB of local changes against the base branch. 21 findings, 9 marked as action required.
[->] The Toolbox has four skills. The agent calls them in plain language.

- Ask codebase-wisdom which repos break if you change a function.

- Run a review on local work before the PR exists.

- Load team standards with get-rules before the agent writes.

Give review-resolver a PR, and it fixes the findings you scope it to.

Overall, the agent writes the code. A separate reviewer with full codebase context reviews it. You only see the issues they cannot resolve.
[->] Agents produce more code than any review process was designed to handle.

They also lack the context a senior engineer has. They do not know which other repos depend on the code, what earlier PRs changed, or what standards the team follows.

Review happens at the pull request, after the agent has already made the design decisions.
[->] Qodo just launched the Agentic Toolbox.

It gives Claude Code, Codex, Kiro, and Cursor direct access to @QodoAI's review engine, codebase knowledge, and team rules. https://t.co/bbtRFncQ0d
LINKS: https://www.qodo.ai/features/qodo-agentic-toolbox/?utm_source=x&utm_medium=partner&utm_campaign=launch-september9&utm_content=omarsar0
--
T=2097696747338232069 | @omarsar0 | 2026-09-09T14:40+00:00 | L115 RT16 C11 V17426 | post
URL=https://x.com/omarsar0/status/2097696747338232069
TEXT: Super cool paper from Microsoft. 

They show that it's possible to build competitive small coding agents without traditional distillation from frontier models.
QUOTED @dair_ai: Banger report from Microsoft.

(bookmark it)

They show that it's possible to build competitive small coding agents without traditional distillation from frontier models.

This is a big deal!

The work describes how they achieved this.

They introduce a 4B coding agent trained on roughly 1,500 software engineering environments.

The cool thing is that they use no distillation from a larger model at any point.

FrogNano is post-trained purely with RL on synthetic tasks.

The target is a coding ag
--
T=2097700490800771362 | @omarsar0 | 2026-09-09T14:55+00:00 | L27 RT5 C10 V7397 | thread(2)
URL=https://x.com/omarsar0/status/2097700490800771362
TEXT: See more here: https://t.co/Aszx9ny7yU
[->] Open video models are having their moment.

The previous generation of LTX alone reached 18M downloads, which shows how much demand there is for video models that builders can own and modify themselves.

LTX-2.5 from @ltx_io builds on that foundation as a world model with open weights, local deployment, and a pretrained base that teams can fine-tune for their own work.

For me, it's all about owning the intelligence stack.

Builders choose the hardware, keep access to the weights, and can fine-tune the model around a creative or production workflow.

More capabilities related to this model:

The release improves both generation and editing.

The new decoder targets sharper faces, legible text and signage, and cleaner fast motion.

Native Multishot generates connected shots while preserving character, environment, lighting, and voice across cuts.

IC-LoRA works on footage you already have, with support for object removal, continuity and wardrobe fixes, and environment changes without a reshoot or frame-by-frame rotoscoping.

A stronger distilled model brings more of the full model's quality and motion to local GPUs.

Open video is still early, and releases like this give builders more room to experiment, specialize models, and own the production stack.

I am looking forward to seeing what people build with LTX-2.5.
LINKS: https://huggingface.co/Lightricks/LTX-2.5?utm_source=social&utm_campaign=LTX-2.5&utm_medium=influencers
--
T=2097722055680483612 | @omarsar0 | 2026-09-09T16:21+00:00 | L17 RT1 C6 V8220 | post
URL=https://x.com/omarsar0/status/2097722055680483612
TEXT: We should all be building for agents.

@lightfld validates this with an impressive CRM solution for the agentic era. And massive adoption, too.

It gives you API, MCP, and CLI access to every record so automations can easily be built on top of it. Removes all the complications.
QUOTED @lightfld: We’ve raised $47M in Series A funding led by @a16z to reimagine CRM as a world model of a business.
--
T=2097730117900328968 | @omarsar0 | 2026-09-09T16:53+00:00 | L57 RT4 C5 V9499 | post
URL=https://x.com/omarsar0/status/2097730117900328968
TEXT: It's crazy how far small models can be pushed.

Robbyant just open-sourced LingBot-World 2.0 Small, a 1.3B world model that generates an interactive world in real time on a single consumer GPU.

Same pattern we saw with language & image models. Scale capabilities first, then distill down to hardware people own.
QUOTED @robbyant_brain: 🌍 What if an AI-generated world didn’t end after a few seconds—but kept running for hours, responded to every move, let you attack, cast spells, shoot, or summon storms, and continued evolving through AI agents?

That’s LingBot-World 2.0: our open-source real-time interactive world model, scaling to 720p/60fps in our full setup.

Today, we’re open-sourcing 3 more models:
🔹 LingBot-World 2.0 Small (1.3B) 
🔹 LingBot-World 2.0 Bidirectional  
🔹 LingBot-World 2.0 Causal Pretrain 

And now, with our 
--
