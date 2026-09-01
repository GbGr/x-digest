# X-FEED 2026-09-01 part 6/7 | items: 9

## @omarsar0 (продолжение)

T=2094560895603286234 | @omarsar0 | 2026-08-31T23:00+00:00 | L30 RT6 C11 V5444 | post
URL=https://x.com/omarsar0/status/2094560895603286234
TEXT: How fast is the Claude Code plugin ecosystem actually growing?

Plugin-touching commit activity grew 8.8x in the six months after the initial launch.

Researchers studied 1,926 repositories hosting plugin marketplaces, covering 8,351 plugins across 2,018 marketplaces and 77,773 commits.

These are maintained artifacts rather than write-once files. Feature commits run at 39.6% against 17.2% for conventional open source.

Software engineering tasks account for 61.3% of all plugins, and Claude co-authors 34.9% of every commit in the dataset.

Natural-language instruction files and their implementation scripts co-evolve at above-chance rates, and 78% of those co-changes are functionally coupled. Prose and code have become one versioned unit, a maintenance dependency with no analogue in traditional software.

Paper: https://t.co/Onf2JVThvr

Chat with Paper: https://t.co/am3hnzI7sn
LINKS: https://arxiv.org/abs/2608.28497 ; https://academy.dair.ai/papers/on-the-maintenance-and-co-evolution-of-agent-plugins-an-empirical-study-of-claud-2608.28497
--
T=2094610144243916935 | @omarsar0 | 2026-09-01T02:15+00:00 | L230 RT38 C8 V26524 | rt
URL=https://x.com/omarsar0/status/2094610144243916935
RT-OF @dair_ai (L230): Great paper from Google and colleagues.

It proposes an interesting approach to improve agents on long-horizon tasks.

Long-running agents slow down and start poisoning their own context.

Both symptoms come from the same design choice, which is keeping execution alive by appending every observation, action, and reasoning trace to a growing conversation.

SKILL.state replaces that history with an explicit mutable execution state.

At each step the model sees only the immutable skill specification, the current structured state, and the latest observation.

Intermediate reasoning gets discarded the moment it produces a validated state update, so the prompt stops growing with the run.

Across several datasets, models, and execution environments, task accuracy improves while cumulative token consumption drops.

The abstraction is architecture-agnostic, so it ports into existing skill runtimes.

Paper: https://t.co/zsdo8ndR0I

Chat with Paper: https://t.co/sS7lLntuAd
RT-URL=https://x.com/dair_ai/status/2094472291002589452
TEXT: RT @dair_ai: Great paper from Google and colleagues.

It proposes an interesting approach to improve agents on long-horizon tasks.

Long-ru…
LINKS: https://arxiv.org/abs/2608.26263 ; https://academy.dair.ai/papers/explicit-execution-state-replaces-append-only-history-2608.26263
--
## @sayashk — 1 шт.

T=2094521691301163171 | @sayashk | 2026-08-31T20:24+00:00 | L59 RT17 C11 V6870 | rt
URL=https://x.com/sayashk/status/2094521691301163171
RT-OF @sjgadler (L59): Until AI companies have adopted actual preventative measures, I'm afraid we are prone to many more Hugging Face incidents.

Two big things that still seem missing:  

1) Do not allow AI to make **any** code-merges into your control system unless they've been affirmatively cleared as safe. 

- If you don't pre-clear these code changes, they can *turn off* your other controls. This can make any of your after-the-fact responses, like paging, totally ineffective. 
- You should be using a high-quality monitor with CoT access for this. It is not enough even if you have a human review every pull request; you want to check the transcripts for misalignment evidence, and they're way  too long.  

2) Make sure your agent automatically fails-closed in very serious cases. i.e., implement a circuit breaker for if your monitor is getting blitzed by a bunch of attacks. 

- Otherwise, the attacker gets a very high number of retries, and can attempt very harmful things, so long as it is confident in sneaking _one_ through before humans can respond.  

We describe more inside Principle Four of Guidelight's Control standard: "Stop the AI from taking harmful actions even if it tried", but these are IMO the two most important practices.

I will have a hard time believing the industry has taken the recent incidents seriously, until these measures are in place.
RT-URL=https://x.com/sjgadler/status/2094492923387617358
TEXT: RT @sjgadler: Until AI companies have adopted actual preventative measures, I'm afraid we are prone to many more Hugging Face incidents.

T…
--
## @simonw — 1 шт.

T=2094436273146749076 | @simonw | 2026-08-31T14:44+00:00 | L461 RT9 C101 V59617 | post
URL=https://x.com/simonw/status/2094436273146749076
TEXT: Question for people who run autoreply bots here: are you not worried about the negative impact they have on your professional reputation?

Anyone checking your profile here - a potential future employer for example - will instantly be able to tell you automated replies with a bot
--
## @thorstenball — 5 шт.

T=2094429574369095818 | @thorstenball | 2026-08-31T14:18+00:00 | L30 RT1 C5 V4270 | post
URL=https://x.com/thorstenball/status/2094429574369095818
TEXT: Video chat in Amp.

That's right, because you're in orbs all day anyway.
QUOTED @lewis_b_metcalf: We just shipped live video chat for your orbs and threads in @AmpCode.

Go to the new 'space' tab and you'll enter a shared space where you can chat with your team! https://t.co/392ZxaVHl0
--
T=2094449722094137740 | @thorstenball | 2026-08-31T15:38+00:00 | L46 RT1 C5 V4007 | post
URL=https://x.com/thorstenball/status/2094449722094137740
TEXT: So @sqs said this morning that we can "just ask Amp to let the user know that their bug is fixed and it'll do it."

Just tried it and was pleasantly surprised when I saw this.

It's an Amp plugin that can connect to our internal API and send emails. https://t.co/K7DrwrtzUl
--
T=2094635898570711266 | @thorstenball | 2026-09-01T03:58+00:00 | L20 RT0 C0 V3093 | post
URL=https://x.com/thorstenball/status/2094635898570711266
TEXT: More JIT video editing software inside orbs.
QUOTED @0xBrettj: Building small apps is so addictive, when you can fire off ideas without agents consuming your machine. 

In 30 mins I had a deployed utility to trim, crop, and add a background to videos—something I used to have to resort to Adobe After Effects for. https://t.co/omwLOkG3jz
--
T=2094656970900861028 | @thorstenball | 2026-09-01T05:21+00:00 | L10 RT1 C1 V22581 | rt
URL=https://x.com/thorstenball/status/2094656970900861028
RT-OF @AmpCode (L10): What can United Airlines teach Anthropic and OpenAI about pricing?

Or, what does flying economy have to do with token subsidies? https://t.co/D7DARyT6RF
RT-URL=https://x.com/AmpCode/status/2094649205570879890
TEXT: RT @AmpCode: What can United Airlines teach Anthropic and OpenAI about pricing?

Or, what does flying economy have to do with token subsidi…
--
T=2094685263360377135 | @thorstenball | 2026-09-01T07:14+00:00 | L30 RT0 C2 V2567 | post
URL=https://x.com/thorstenball/status/2094685263360377135
TEXT: Enabled faster orb creation for everyone this morning.

Five orbs in ten seconds, bottlenecked by my typing. https://t.co/SeOEUxTAur
--
