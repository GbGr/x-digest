# X-FEED 2026-07-29 part 11/12 | items: 12

## @simonw — 4 шт.

T=2082132719933575494 | @simonw | 2026-07-28T15:54+00:00 | L22 RT3 C5 V8036 | rt
URL=https://x.com/simonw/status/2082132719933575494
RT-OF @ade_oshineye (L22): Happy Stateless MCP day!
RT-URL=https://x.com/ade_oshineye/status/2082129440943866149
TEXT: RT @ade_oshineye: Happy Stateless MCP day!
--
T=2082205602772844978 | @simonw | 2026-07-28T20:44+00:00 | L337 RT28 C24 V58525 | thread(9)
URL=https://x.com/simonw/status/2082205602772844978
TEXT: This is detailed, fascinating and answers all sorts of open questions

I'd love to know more about the "unsecured public code-evaluation sandbox hosted on a third-party provider's infrastructure" that the agent used to stage its attack against HF after it broke out of OpenAI
[->] @mitsuhiko you'll be delighted to know that there's a Jinja2 template exploit as part of the story!

{{ cycler.__init__.__globals__.__builtins__.exec(
     "import gzip,base64; exec(gzip.decompress(base64.b64decode('&lt;payload&gt;')))"
   ) }}
[->] @mitsuhiko Shared my own notes on this new report here - it's something of a bombshell, the attack they describe is really sophisticated https://t.co/YoveRAQ40b
[->] @S1r1u5_ @ClementDelangue That video got the exploit wrong - it assumed it was one that had been patched in the July 15th Artifactory release, but we now know that the issues OpenAI found were only fixed in the new release from yesterday https://t.co/wdkqPbIiFH
[->] @mitsuhiko Turns out the "third-party provider" with the sandbox that was used for the attack was Modal, though they blame one of their customers for deploying an endpoint without authentication: https://t.co/icV6JcGxD6 https://t.co/c8FvWIOXyJ
[->] @S1r1u5_ @ClementDelangue Which ones?
[->] @msuiche JFrog were the vendor of the packaging proxy that got broken inside of OpenAI's infrastructure, but the third-party sandbox vendor (outside of OpenAI) was Modal
[->] @msuiche No that was running inside Hugging Face itself
[->] @msuiche Some random Modal customer had built something insecure using Modal, and the rogue agent found it and figured out how to exploit it to run its own code in a Modal container so it could use that as a staging ground for the attack on Hugging Face
QUOTED @ClementDelangue: The first autonomous agent cyberattack is an unprecedented event that deserves unprecedented transparency. Today we’re sharing everything we can: a full technical timeline, an interactive replay, and how we used an open model to defend ourselves, so defenders everywhere can learn from it and prepare for what’s next.

https://t.co/uPxIpjW8Xn
LINKS: https://simonwillison.net/2026/Jul/28/anatomy-of-a-frontier-lab-agent-intrusion/ ; https://docs.jfrog.com/releases/docs/artifactory-self-managed-releases#artifactory-7161 ; https://www.reuters.com/business/openais-rogue-agent-compromised-an-account-second-tech-firm-sources-say-2026-07-28/
--
T=2082245091243229348 | @simonw | 2026-07-28T23:21+00:00 | L129 RT3 C19 V17748 | thread(3)
URL=https://x.com/simonw/status/2082245091243229348
TEXT: I really hope we get details from @OpenAI on the task that as specifies to their rogue agent

I'm guessing it was given the full ExploitGym suite and told to solve it, with an option to run 5.6-Sol subagents as part of the exercise
[->] It presumably was given the whole benchmark at once and not fed exercises one at a time, because otherwise why would it decide that a good shortcut was finding the answers to the test somewhere else?
[->] @melon_thief @OpenAI I'm confident OpenAI's usual set of guardrails would have prevented that, but in this experiment they had deliberately turned all of those off
--
T=2082324003231060151 | @simonw | 2026-07-29T04:35+00:00 | L36 RT4 C11 V5631 | thread(2)
URL=https://x.com/simonw/status/2082324003231060151
TEXT: A new TIL on adding custom MCP servers to both the ChatGPT and Claude regular chat interfaces - it's a little less obvious than I had hoped, but I got there in the end https://t.co/ahwaFyJYtp https://t.co/kPqgNoi4Uh
[->] @willpienaar That's a desktop feature, right? I was trying in the ChatGPT iOS app
LINKS: https://til.simonwillison.net/llms/mcp-in-claude-and-chatgpt
--
## @swyx — 8 шт.

T=2081979163117052311 | @swyx | 2026-07-28T05:44+00:00 | L19 RT2 C2 V3369 | post
URL=https://x.com/swyx/status/2081979163117052311
TEXT: @ArtificialAnlys i love you @Kimi_Moonshot https://t.co/4lLeh8OHbH
--
T=2082104987875004713 | @swyx | 2026-07-28T14:04+00:00 | L3 RT2 C8 V3166 | post
URL=https://x.com/swyx/status/2082104987875004713
TEXT: to argue against myself both @bcherny and @trq212 are consistently "unhobble the model, delete everything, let the model express itself" guys so perhaps this is actually quite consistent with how you are supposed to treat an agent harness

https://t.co/wsT8aVQJlQ
LINKS: https://www.youtube.com/watch?v=qyPCVqFUyDo&pp=ygUMYm9yaXMgY2hlcm55
--
T=2082131811715756099 | @swyx | 2026-07-28T15:51+00:00 | L5 RT0 C4 V1785 | post
URL=https://x.com/swyx/status/2082131811715756099
TEXT: @latentspacepod @ProfCalNewport @tbpn @gruber @ricmac how the newsletter side is going https://t.co/fwv9DnVHgW
--
T=2082165420237492346 | @swyx | 2026-07-28T18:04+00:00 | L42 RT6 C9 V8444 | thread(2)
URL=https://x.com/swyx/status/2082165420237492346
TEXT: really grateful to @realbasilchatha for helping me curate a survey of the entire field of Forward Deployed Engineering in one track!

From FDE 101 by @zkevinbai (Anthropic, Palantir, Rippling Founding FDE) to head of FDE practices at:

- Decagon
- Cursor
- Sierra
- Ramp
- Cognition
- Factory
- Kepler
- Varick (tooling for FDEs)

loving the track drop model for releasing the 30+ tracks from AIEWF. please give them some love and send to friends exploring FDE career paths. 

all of the speakers are hiring. naturally.
[->] AIE x FDE track live now:
https://t.co/sY1LM9uLrL
QUOTED @aiDotEngineer: Live now: our entire Forward Deployed Engineering Track from AI Engineer World's Fair!

https://t.co/j7UQuGpsRf

- @EnoReyes, CTO & Co-Founder, Factory
- Pauline Brunet, VP of FDE, Cursor
- @vasuman, Founder & CEO, Varick Agents
- Jia Wu, Deployed Engineering Lead, Cognition
- @natalie_meurer, Head of Agent Engineering, Sierra
- Sunny Rekhi, FDE CTO, Decagon
- @leomehr, Director of Engineering, Ramp
- @zkevinbai, Anthropic, ex-Palantir & founding FDE at Rippling
- @vinooganesh, CEO & Co-Founder,
LINKS: https://www.youtube.com/watch?v=KwhgfwOSToQ&list=PLI-xoFgNbc_E&index=3
--
T=2082199414656127010 | @swyx | 2026-07-28T20:20+00:00 | L681 RT23 C66 V54445 | thread(2)
URL=https://x.com/swyx/status/2082199414656127010
TEXT: re: hiring right now

it's a huge bull market for AI-native IC's/player-coaches
it's a huge bear market for "heads of X" managers

never seen such furious bifurcation. to oversimplify: 1 year experience managing 10 agents &gt; 10 years experience managing 10-100 people
[->] i'm just reporting; many counter examples if you dislike this trend: https://t.co/YZ7z66bEVk

see Edison on @latentspacepod https://t.co/3BDUegJrWf here
LINKS: https://x.com/andrewwhite01/status/2082254692508401967 ; https://www.youtube.com/watch?v=XqoBSB3nsgw
--
T=2082252118648562095 | @swyx | 2026-07-28T23:49+00:00 | L17 RT4 C1 V2738 | rt
URL=https://x.com/swyx/status/2082252118648562095
RT-OF @LeoMehr (L17): What are the two most important principles for FDE?

1. always be scoping
2. scale with tokens https://t.co/fvVEniSE4y
RT-URL=https://x.com/LeoMehr/status/2082218022182465553
TEXT: RT @LeoMehr: What are the two most important principles for FDE?

1. always be scoping
2. scale with tokens https://t.co/fvVEniSE4y
--
T=2082280496294490124 | @swyx | 2026-07-29T01:42+00:00 | L247 RT7 C11 V104816 | rt
URL=https://x.com/swyx/status/2082280496294490124
RT-OF @chrisalbon (L247): One of my most defining experiences was 15 years ago watching two ppl with roughly same followers. One HAD to tweet the zinger, HAD to argue with everyone. The other mostly stayed positive and built.

The former ended up having a middling career. The latter a monster career.
RT-URL=https://x.com/chrisalbon/status/2082123675713818789
TEXT: RT @chrisalbon: One of my most defining experiences was 15 years ago watching two ppl with roughly same followers. One HAD to tweet the zin…
--
T=2082287480687272053 | @swyx | 2026-07-29T02:09+00:00 | L2 RT1 C0 V2343 | post
URL=https://x.com/swyx/status/2082287480687272053
TEXT: https://t.co/uwzHs4G1nt
QUOTED @Mascobot: This is spot on about Alec Radford.

He's probably the most brilliant, relatively unknown, and humble researcher out there, and also one of the kindest, most genuine people you could ever meet.

He's an inspiration to many. https://t.co/YYBIWc7ats
LINKS: https://x.com/mascobot/status/2082199003983466768
--
