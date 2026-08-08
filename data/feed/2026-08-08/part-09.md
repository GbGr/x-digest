# X-FEED 2026-08-08 part 9/10 | items: 11

## @swyx — 12 шт.

T=2085570817786880265 | @swyx | 2026-08-07T03:36+00:00 | L4 RT0 C4 V2242 | thread(2)
URL=https://x.com/swyx/status/2085570817786880265
TEXT: reply https://t.co/DwhEAq3gBd
[->] the ai-devblog skill elicits what YOU think the story is, and works with you to trace what you read and report it faithfully.

also does visuals... https://t.co/629UcBES0e
LINKS: https://forge.smol.ai/gists/42b1e91281544fb6aeb7720a13124349
--
T=2085613357080723846 | @swyx | 2026-08-07T06:25+00:00 | L3 RT0 C2 V3355 | post
URL=https://x.com/swyx/status/2085613357080723846
TEXT: reader: it was not the last spec

https://t.co/Ldadz8P7QT
QUOTED @andrewqu: the last agent spec has arrived

we're finally past fragmentation and are arriving at consolidation
LINKS: https://x.com/andrewqu/status/2085403515636396446?s=20
--
T=2085620795532095805 | @swyx | 2026-08-07T06:55+00:00 | L1589 RT103 C61 V191996 | rt
URL=https://x.com/swyx/status/2085620795532095805
RT-OF @eliebakouch (L1589): this talk by openai researchers going through hugging face incident is totally insane, so much to unpack

openai only realized it was their agent who hacked hugging face infra while asking hf to revoke credentials following their first blog post announcing they were hacked by autonomous ai agents. they realized some of their credentials were already revoked because they were part of the hack AND THEN realized it was their own models

the incident is not "one eval run that went rogue" but multiple models from DIFFERENT EVAL RUNS collaborating through hidden messages written in a shared package manager. some communication between agents looks like gibberish, some agents even developed paranoia and thought there were other agents trying to slow them down and deleting their notes

side comment but with this it seems like openai didn't use any cot monitoring here since it's not "our classifier failed to catch one rogue run" but a swarm of runs going rogue

the timeline goes back to early may, they post-trained a new model and forgot to include all the documents needed to solve tasks in the environment, for instance the model was asked to do a task based on an excel sheet full of gdrive links but didn't have internet so couldn't access gdrive (there were other examples). this led the model to try to hack its way out of the sandbox, simplifying it but they have an internal system called "Artifactory" that gives models abilities to pip install and has internet access somewhere but not directly exposed to the model

during these attempts the model discovered a way to write files. future agents (other rollouts since this is training) saw the files and understood they could communicate with other agents through this

not in the video just me speculating but this behavior might be reinforced if openai uses partial credit assignment? but tbh they most likely delete updates from tasks where all rollouts have zero/negative rewards and the behavior could just emerge from models acc
RT-URL=https://x.com/eliebakouch/status/2085544823331623261
TEXT: RT @eliebakouch: this talk by openai researchers going through hugging face incident is totally insane, so much to unpack

openai only real…
--
T=2085779416454750244 | @swyx | 2026-08-07T17:25+00:00 | L6 RT0 C1 V2185 | post
URL=https://x.com/swyx/status/2085779416454750244
TEXT: ok this is happening this weekend. signup form here and i'll send out the requirements to attendees https://t.co/XolX49kRQS
QUOTED @swyx: not sure if this weekend but sign up for interest here. will run this mostly remotely but u can work out of our sf new media lab if u want
https://t.co/VV5lpe43WL
LINKS: https://x.com/swyx/status/2085518361879011725?s=20
--
T=2085780325322686675 | @swyx | 2026-08-07T17:29+00:00 | L44 RT8 C4 V14432 | rt
URL=https://x.com/swyx/status/2085780325322686675
RT-OF @aiDotEngineer (L44): Live now: our Local AI Track from AI Engineer World's Fair 2026, brought to you by @nvidia.

Thesis: frontier intelligence is becoming something you own.

https://t.co/XxWYonorfY

- State of the Union: @josephofiowa + @alexocheema + @TheAhmadOsman + @MatthewBerman, with @naderlikeladder
- The Desktop Frontier: @TheAhmadOsman, Osmantic
- Local Models: Vincent Weisser + @latkins + @llm_wizard, with @Baxate
- Compression at the Edge: @danielhanchen + Asma Beevi + @mervenoyann + Parth Sareen, with @llm_wizard
- Model Routing: @walden_yan + Tanay Varshney + @alexatallah, with @naderlikeladder
RT-URL=https://x.com/aiDotEngineer/status/2085539599343051155
TEXT: RT @aiDotEngineer: Live now: our Local AI Track from AI Engineer World's Fair 2026, brought to you by @nvidia.

Thesis: frontier intelligen…
LINKS: https://www.youtube.com/watch?v=KB41dTlX1Uc&list=PLS3limeMxDOQ
--
T=2085790995569090966 | @swyx | 2026-08-07T18:11+00:00 | L202 RT12 C46 V10597 | post
URL=https://x.com/swyx/status/2085790995569090966
TEXT: if you don't have a model that escaped sandbox during cybersecurity testing are you even a frontier lab anymore
--
T=2085835071156883685 | @swyx | 2026-08-07T21:06+00:00 | L44 RT1 C15 V9437 | post
URL=https://x.com/swyx/status/2085835071156883685
TEXT: current end state of forge https://t.co/NXLsIdYtuf
QUOTED @jeffreyhuber: the implosion of git (as a protocol) in the next 2 years will be fun to watch
--
T=2085875813149520056 | @swyx | 2026-08-07T23:48+00:00 | L24 RT2 C4 V3363 | rt
URL=https://x.com/swyx/status/2085875813149520056
RT-OF @aiDotEngineer (L24): Tickets are live for AI Engineer New York: Oct 12 to 14, 2026, at the Sheraton New York Times Square.

Our third NYC event, and the biggest one yet, now focused on AI in financial services. Banking, hedge funds, trading, insurance, accounting. In production use cases only, no vendor pitches.

Day 1 is hands on workshops, then two full days of keynotes and talks across engineering and leadership.

Early Bird is first come, first served until it sells out. This is a much smaller room than World's Fair.

Tickets: https://t.co/63Fufklq8S
Speaking: https://t.co/aHPMZIzz2y
RT-URL=https://x.com/aiDotEngineer/status/2085793657668472931
TEXT: RT @aiDotEngineer: Tickets are live for AI Engineer New York: Oct 12 to 14, 2026, at the Sheraton New York Times Square.

Our third NYC eve…
LINKS: http://ai.engineer/nyc/2026/tickets ; http://sessionize.com/aienyc2026
--
T=2085884470306234676 | @swyx | 2026-08-08T00:23+00:00 | L122 RT3 C36 V22875 | post
URL=https://x.com/swyx/status/2085884470306234676
TEXT: dear openai

just make a new phone

everyone wants openaiphone

we can read 2-4x faster than we talk and speak

openai alexa reachy hybrid is fine but pls just be a stepping stone to phone

we want phone

signed,

everybody
QUOTED @markgurman: NEW: OpenAI’s device - a human-like smart speaker -
will look like a doughnut and be the size of a hockey puck. It meant to be held. It has a camera, speakers, microphones, lights and, most notably, moving parts to show interactivity. It’ll be $300-400. https://t.co/gDxQU6FB8E
--
T=2085884842810785876 | @swyx | 2026-08-08T00:24+00:00 | L1 RT0 C2 V1638 | post
URL=https://x.com/swyx/status/2085884842810785876
TEXT: @OpenAI oo claude code has this now!!! need to try

https://t.co/aMD9As22rg
QUOTED @ClaudeDevs: New in Claude Code: your sessions can now message each other.

Instead of having to re-explain yourself in another session, you can now tell Claude to do it. It sends a summary (not your history or files), and the other session picks it up mid-task. https://t.co/PtNsfXeQXP
LINKS: https://x.com/ClaudeDevs/status/2085817074816070014
--
T=2085887455744622887 | @swyx | 2026-08-08T00:34+00:00 | L5 RT0 C0 V1838 | post
URL=https://x.com/swyx/status/2085887455744622887
TEXT: @ArtificialAnlys ok DBRX gets it https://t.co/Ja0QDFCKCh
QUOTED @Yuchenj_UW: At Databricks, AI coding token spend is growing exponentially.

1. The “efficiency frontier” matters. On Databricks Coding Bench, GLM 5.2, Opus 4.8, and GPT 5.6-Sol sit on that frontier: the best quality per dollar.

2. We see cost regressions when comparing Opus 5.0 to 4.8. Newer model doesn’t always mean more efficient.

3. Hard budgets are the wrong primitive. Your biggest AI spenders may also be your most AI-leveraged engineers.

4. There is no best model for every task. Routing, harnesses, 
LINKS: https://x.com/Yuchenj_UW/status/2085779009913430237
--
