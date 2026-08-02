# X-FEED 2026-08-02 part 4/7 | items: 8

## @karpathy — 1 шт.

T=2083749667410727319 | @karpathy | 2026-08-02T03:00+00:00 | L8166 RT555 C518 V530403 | post
URL=https://x.com/karpathy/status/2083749667410727319
TEXT: We're starting to leave the territory where you'd test an LLM by e.g. "create an svg of pelican on a bicycle". As one idea to generalize it, I was interested what Opus 5 would do if I gave it the first paragraph of the Lord of the Rings, a 1M token budget (~$10) and asked for three js render of it. Opus went off for ~2 hours and wrote 5500 lines of code that (procedurally) rendered the story. It's kind of janky but fun. But it's a bit mindboggling that the LLM has to place and orchestrate various polygon assets in (x,y,z) coordinates and write code that animates it all, and that it even does anything at all.

I also like this kind of examples because no one in their right mind would ever spend the time to write something this custom but LLMs have all the stamina and patience in the world, so it's an example where we go from "no one would ever do this" to "sure, why not, it's ~free". There might be a lot more. But I'm excited about creating hyper custom worlds that you can imagine dropping players into, e.g. here to participate in the LoTR story as a spectator NPC, or one of the characters, or etc. Something like an ephemeral GTA of X on demand.

Last thought is that the domain of worlds/games exposes a weakness in LLMs: they can't easily audit their work because they aren't able to efficiently and natively perceive videos or play games within them. Here, Opus 5 had to very slowly and painstakingly take screenshots at different points, and it messed up a few times and created a bunch of jank. An example of raw capability (multimodal, gameplay) that I think is still quite lacking.
--
## @lateinteraction — 2 шт.

T=2083412573131522141 | @lateinteraction | 2026-08-01T04:40+00:00 | L18 RT1 C3 V2124 | rt
URL=https://x.com/lateinteraction/status/2083412573131522141
RT-OF @dbreunig (L18): https://t.co/qYjndRSKpy
RT-URL=https://x.com/dbreunig/status/2083410286997131432
TEXT: RT @dbreunig: https://t.co/qYjndRSKpy
LINKS: http://x.com/i/article/2083409392435871744
--
T=2083643780305965507 | @lateinteraction | 2026-08-01T19:59+00:00 | L85 RT9 C6 V8189 | thread(2)
URL=https://x.com/lateinteraction/status/2083643780305965507
TEXT: i think that's true for most of us honestly; it's just not a take that would spread as widely

imo a BIG part of this is whether you're problem- or method-oriented. if you're problem-oriented, you'd recalibrate to a new normal quickly or enjoy the craft more with richer tradeoffs https://t.co/EbOEWkV6ql
[->] in many ways, it's a good idea to be sort of a "declarative" person by default

what this means is that what you value and what you seek to be "good" at is necessarily hierarchical and flows downstream from grounded impact.

so, you're not great at some little technical over-specialized contingency for reasons you don't understand (except insofar that you do that for pure fun; fair). BUT you can and should be great at it to the extent that it's currently a necessary or useful piece to offer an impactful and ever-lasting contract/interface, which is what you actually care about.

accordingly, when the needs of that contract shift, you're just adjusting to one level higher up in the hierarchy, rather than fighting for the downstream parts.

the need for the exposed interface almost never goes away at all useful levels of the hierarchy, unless you choose very poorly.
QUOTED @alex_peys: maybe i am lucky but across my work (ai+bio research) and relevant hobbies (music, motorsports) there have been 0 model releases where my reaction has been “oh no, the machine is somehow reducing my enjoyment of my craft.”
--
## @mattpocockuk — 2 шт.

T=2083563358180012470 | @mattpocockuk | 2026-08-01T14:39+00:00 | L1094 RT49 C127 V70656 | thread(3)
URL=https://x.com/mattpocockuk/status/2083563358180012470
TEXT: Great guest article from Birgitta on Martin Fowler's site:

https://t.co/i3KmU0IdLM
[->] Everyone always confuses my skills with spec-driven-development.

It really annoys me. The specs my skills create are intended to be deleted immediately - not kept around, or treated as source code.

Birgitta Boeckeler calls this 'spec-first' development, but still groups this under the SDD umbrella (link below).

I disagree - I think it needs its own term. The specs aren't that important. They're just a projection of the decisions made during grilling.

GDD? Grill-driven-development. IDK
[->] @aiglesias_ Also, I do use ADR's - but they are less likely to go stale than specs and I delete those that do go stale.
LINKS: https://martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html
--
T=2083641584705253414 | @mattpocockuk | 2026-08-01T19:50+00:00 | L1178 RT36 C38 V87547 | thread(2)
URL=https://x.com/mattpocockuk/status/2083641584705253414
TEXT: Domain language is unbelievably powerful with agents
[->] @k1484502 Also, yeah it does
QUOTED @asidorenko_: Find the right terms https://t.co/tIJc97XPW5
--
## @mitchellh — 3 шт.

T=2083580194410148033 | @mitchellh | 2026-08-01T15:46+00:00 | L1 RT0 C0 V111 | post
URL=https://x.com/mitchellh/status/2083580194410148033
TEXT: @rockorager @jossephus To some degree is right. And yeah, its way more efficient to transfer the binary (compressed) than VT. Eg an every cell styled 120x40 10k lines scrollback is 300 KB (much less to usability cause we do scrollback background). VT js way more expensive.
--
T=2083586549766377677 | @mitchellh | 2026-08-01T16:11+00:00 | L10 RT0 C2 V4799 | post
URL=https://x.com/mitchellh/status/2083586549766377677
TEXT: @raphamorims Btw did some resize optimizations yesterday. Should be closer to like 20us now or so. I have a bigger architectural changes coming later but more focused on deferred scrollback reflow won’t change active area performance
--
T=2083630166191043007 | @mitchellh | 2026-08-01T19:05+00:00 | L7 RT0 C1 V4675 | thread(5)
URL=https://x.com/mitchellh/status/2083630166191043007
TEXT: @jonathan_s Yes, the server parses too. But the teeing happens ahead of the server, so the clients can parse simultaneously to the servers (also if anyone is slow there’s some queues).
[->] @jonathan_s As in, ignoring rendering completely. Purely based on how long internal state takes to even update
[->] @jonathan_s It’s probably slower by sending VT streams through it to Ghostty vs ghostty alone. Purely on the bytes per second read through the pty.
[->] @jonathan_s Sorry you’re getting a bunch of tweets I’m sending these on the go haha. Also not even talking about their server architecture here. On the basis of their pure terminal emulation. It’s slow
[->] @jonathan_s The issue with the screen diffing is less performance and more making it very difficult to allow native scrollback, selection, etc.
--
