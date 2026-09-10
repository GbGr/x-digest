# X-FEED 2026-09-10 part 8/10 | items: 9

## @omarsar0 (продолжение)

T=2097840372592369992 | @omarsar0 | 2026-09-10T00:11+00:00 | L455 RT43 C26 V61677 | rt
URL=https://x.com/omarsar0/status/2097840372592369992
RT-OF @dair_ai (L455): Banger report from Microsoft.

(bookmark it)

They show that it's possible to build competitive small coding agents without traditional distillation from frontier models.

This is a big deal!

The work describes how they achieved this.

They introduce a 4B coding agent trained on roughly 1,500 software engineering environments.

The cool thing is that they use no distillation from a larger model at any point.

FrogNano is post-trained purely with RL on synthetic tasks.

The target is a coding agent that runs on minimal machines, which rules out both a frontier backbone and a frontier teacher.

The ingredient the report credits the most is online task synthesis.

The pipeline generates tasks calibrated to the frontier of learnability for the current checkpoint, so the agent always trains on problems it can just barely solve. The authors argue that calibration, rather than the volume of synthetic data, is what makes this work.

This means that competitive small coding agents can be trained from synthetic tasks alone.

And generating those tasks at the current agent's learnability frontier is what makes this particular training productive.

The report covers training methodology, evaluations across diverse environments, and analyses of what the agent learned.

Paper: https://t.co/rSmH21XMD5
RT-URL=https://x.com/dair_ai/status/2097695781935624477
TEXT: RT @dair_ai: Banger report from Microsoft.

(bookmark it)

They show that it's possible to build competitive small coding agents without tr…
LINKS: https://academy.dair.ai/papers/frognano-training-a-4b-coding-agent-via-online-task-synthesis-2609.07925
--
T=2097958286146605446 | @omarsar0 | 2026-09-10T08:00+00:00 | L4 RT0 C4 V609 | post
URL=https://x.com/omarsar0/status/2097958286146605446
TEXT: Nice paper from Salesforce on co-evolving harnesses and models.

Harness engineering is a hot topic right now. So this is a great read.

(bookmark it)

Salesforce evolved a harness with a weak model across seven enterprise agent tasks, then trained that model on a stronger expert's full trajectories under the same harness.

Performance dropped on all seven tasks, by 4 to 30 points across Qwen3-Coder and Gemma 4.

The same fine-tuning helps under the unevolved harness. So the harness is what changes the outcome.

Their analysis points at model-harness fit.

Imitation transfers knowledge and increases scaffold usage, but the weaker model adopts the expert's planning strategy without the competence to execute it, and it no longer matches a harness that was evolved around its own native planning style.

The fix is to stop copying whole trajectories.

A meta-level agent finds the failing turn in the weaker model's own rollout and asks the expert to rewrite only that turn. That keeps the model's planning style intact and combines the gains from harness evolution and weight updates.

Paper: https://t.co/gG3J6MnvT0
LINKS: https://academy.dair.ai/papers/co-evolving-harnesses-and-models-on-policy-correction-helps-weaker-models-catch-2609.09134
--
## @rasbt — 1 шт.

T=2097677953450561596 | @rasbt | 2026-09-09T13:26+00:00 | L1777 RT252 C55 V65172 | thread(2)
URL=https://x.com/rasbt/status/2097677953450561596
TEXT: Here's a link to the article: https://t.co/bz9kw9UqUR
[->] I put together a mega write-up on GPT-6 Astra &amp; looped transformers.

How looped transformers / recurrent depth works, cost-tradeoffs, whether it hides reasoning traces, with lots of figures and a tour of recent looped transformer research. https://t.co/VR6HaPFVXH
LINKS: https://magazine.sebastianraschka.com/p/gpt-6-astra-looped-transformers-and
--
## @sh_reya — 2 шт.

T=2097823350903173427 | @sh_reya | 2026-09-09T23:03+00:00 | L22 RT4 C2 V3487 | rt
URL=https://x.com/sh_reya/status/2097823350903173427
RT-OF @JiaZhihao (L22): We built LithosAI to make every step of your agent faster. The public API is now live. Try it on your own workloads and show us what you build. 🚀
RT-URL=https://x.com/JiaZhihao/status/2097820057275363545
TEXT: RT @JiaZhihao: We built LithosAI to make every step of your agent faster. The public API is now live. Try it on your own workloads and show…
--
T=2097838127406891226 | @sh_reya | 2026-09-10T00:02+00:00 | L9 RT3 C1 V763 | rt
URL=https://x.com/sh_reya/status/2097838127406891226
RT-OF @sirrice (L9): At last week's #VLDB26, I gave keynotes @ NOVAS &amp; DashSys workshops about @DAP__Lab's early work on Agentic Data Environments.   Agent use cases are dragging technology behind it &amp; there are research opportunities everywhere!

Annotated slides: https://t.co/FPz3LajfOH https://t.co/kPYd3dz2K9
RT-URL=https://x.com/sirrice/status/2097701690392588483
TEXT: RT @sirrice: At last week's #VLDB26, I gave keynotes @ NOVAS &amp; DashSys workshops about @DAP__Lab's early work on Agentic Data Environments.…
LINKS: https://eugenewu.net/talks/2026-09-agentic-data-envs.html
--
## @simonw — 1 шт.

T=2097847628155523242 | @simonw | 2026-09-10T00:40+00:00 | L93 RT5 C30 V11868 | thread(2)
URL=https://x.com/simonw/status/2097847628155523242
TEXT: Here's a Blender model of a Pluribus themed Fabergé egg I had GPT-6 Astra build - I generated the concept image using ChatGPT Images 2.5, then pasted the image into Codex and told Astra to turn that into a Blender file

Details here: https://t.co/9DZa0x6GZf https://t.co/ge8TbjsS5Y
[->] I also had Astra vibe code up an online Blender model viewing tool, so you can explore the egg interactively in your browser here: https://t.co/NGlFhPduoB
LINKS: https://simonwillison.net/2026/Sep/9/blender-viewer/ ; https://tools.simonwillison.net/blender-viewer?url=https%3A%2F%2Fgithub.com%2Fsimonw%2Fvibe-coded-blender-projects%2Fblob%2Fmain%2Fpluribus-faberge-egg%2Fdeliverables%2FPluribus_Jeweled_Egg_v1.blend
--
## @swyx — 3 шт.

T=2097765576286552134 | @swyx | 2026-09-09T19:14+00:00 | L60 RT7 C10 V7685 | rt
URL=https://x.com/swyx/status/2097765576286552134
RT-OF @aiDotEngineer (L60): We’re hiring at AI Engineer.

Help us unite and empower the global AI engineering community.

Open roles:
• Growth Marketing Lead
• Community Manager
• Event Systems &amp; Ops Manager
• Associate Producer

Apply: https://t.co/f2C5wMDtCZ https://t.co/kK5OtVctzi
RT-URL=https://x.com/aiDotEngineer/status/2097724211318194197
TEXT: RT @aiDotEngineer: We’re hiring at AI Engineer.

Help us unite and empower the global AI engineering community.

Open roles:
• Growth Marke…
LINKS: https://www.linkedin.com/company/aidotengineer/
--
T=2097772086785954172 | @swyx | 2026-09-09T19:40+00:00 | L305 RT27 C33 V41455 | rt
URL=https://x.com/swyx/status/2097772086785954172
RT-OF @varunshenoy_ (L305): at long lake, we've bought 40+ services businesses to build AI where work actually happens

we're working on:
- deploying agents to complete knowledge work
- frontier eval generation from real workflows
- post-training open models on data no lab has

come build with us @llmh https://t.co/3Ux6cXtsJ8
RT-URL=https://x.com/varunshenoy_/status/2097769417551888615
TEXT: RT @varunshenoy_: at long lake, we've bought 40+ services businesses to build AI where work actually happens

we're working on:
- deploying…
--
T=2097795139385348245 | @swyx | 2026-09-09T21:11+00:00 | L27 RT2 C1 V6451 | rt
URL=https://x.com/swyx/status/2097795139385348245
RT-OF @varunshenoy_ (L27): our full presentation from @aiDotEngineer world fair: https://t.co/yzllGm2wPM

thank you @swyx + team for having us!
RT-URL=https://x.com/varunshenoy_/status/2097769418898186505
TEXT: RT @varunshenoy_: our full presentation from @aiDotEngineer world fair: https://t.co/yzllGm2wPM

thank you @swyx + team for having us!
LINKS: https://www.youtube.com/watch?v=B0fjR3yaZFU
--
