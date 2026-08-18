# X-FEED 2026-08-18 part 6/9 | items: 13

## @mitchellh — 3 шт.

T=2089223578239844842 | @mitchellh | 2026-08-17T05:31+00:00 | L3 RT0 C1 V961 | post
URL=https://x.com/mitchellh/status/2089223578239844842
TEXT: @peter0x44 @caballerobrah @valigo Here’s how to do it (Zig but it’s just a thin vehicle for assembly). I contributed some of these which is how I know. https://t.co/mastdWOBlY
LINKS: https://codeberg.org/ziglang/zig/src/branch/master/lib/std/valgrind.zig
--
T=2089351136839090387 | @mitchellh | 2026-08-17T13:58+00:00 | L661 RT19 C27 V40827 | post
URL=https://x.com/mitchellh/status/2089351136839090387
TEXT: I've moved on to optimizing libghostty Wasm runtime memory usage and I am learning a lot! The first discovery: Zig's `std.heap.MemoryPool` is very bad for Wasm! We replaced it with a custom Wasm-specific pool that lowered libghostty's required terminal memory by 75% without any measurable throughput impact.

Some background: `std.heap.MemoryPool` is a very high performance memory pool implementation for identically sized items directly in the Zig standard library. For non-wasm targets, its very good! We use it a lot!

But there is a major problem due to the interaction of two separate behaviors: first, the Zig std memory pool grows by 1.5x whenever it has no free space. To grow, it asks the backing allocator, which is usually general-purpose. On Wasm targets, that general-purpose allocator is the BrkAllocator which grows by power-of-two for big allocation slots (what we were hitting).

On native (non-wasm) targets, this just gets increasingly large virtual memory allocations, which is fine! Good, even! Virtual memory mappings are cheap and the total mapped memory isn't resident/physical until it's used. Allocation syscalls are expensive and its better to get too much.

But wasm is not like that. Every linear memory growth is immediately measured, zeroed, resident memory. Second, memory growth doesn't require a "syscall" in the same sense/overhead of the word. 

The result is you get really big linear memory growth in WebAssembly and it looks/feels bad in web inspector and saves absolutely nothing on future IO.

We replaced it with a very simple pool (~20 lines of effective code) that grows the linear memory by exactly 1 item size when it needs it and maintains a module-global free list (assumes single-threaded Wasm module) so same-item pools are shared globally.

PR here: https://t.co/1Uh2yPk9fn
LINKS: https://github.com/ghostty-org/ghostty/pull/13865
--
T=2089446702285758559 | @mitchellh | 2026-08-17T20:18+00:00 | L1329 RT34 C40 V77047 | post
URL=https://x.com/mitchellh/status/2089446702285758559
TEXT: Good moment today to remind everyone to stay frosty with AI. I was working on making a server stoppable via the CLI, and Codex decided the best path forward was to implement an unauthenticated network API to every server to shut itself down. Excellent work.

I responded with "I don't know about that." (I usually give more direct feedback but this was so absurd) and it thought for like 20 seconds and responded "Server stopping should not be part of an unauthenticated network API." Yes. lol. 

By the way, the result I was looking for was that we automatically start a locally discovery Unix-socket bound server so I wanted it to discover that (using prior mechanisms already made) and gracefully stop that. 

The driver is absolutely accountable here (me). My lazy prompting led AI to think I wanted to be able to stop ANY configured server I was talking to. Shame on me for thinking it was obvious here. But, I also reviewed it and found this idiocy, so, that's where good AI drivers come in. Also me.
--
## @mitsuhiko — 6 шт.

T=2089353094538645874 | @mitsuhiko | 2026-08-17T14:06+00:00 | L110 RT11 C14 V28225 | rt
URL=https://x.com/mitsuhiko/status/2089353094538645874
RT-OF @bentlegen (L110): 🎙️ State of Agentic Coding w/ @mitsuhiko and @bentlegen returns

In this episode (#9):
- how agents are getting more autonomous
- the subsidies will continue until morale improves
- @herdrdev and VC-funded terminal apps
- vibe coding from your car, and more! https://t.co/pO9LKCSASW
RT-URL=https://x.com/bentlegen/status/2089346117179773187
TEXT: RT @bentlegen: 🎙️ State of Agentic Coding w/ @mitsuhiko and @bentlegen returns

In this episode (#9):
- how agents are getting more autonom…
--
T=2089355671900709099 | @mitsuhiko | 2026-08-17T14:16+00:00 | L41 RT2 C3 V5468 | post
URL=https://x.com/mitsuhiko/status/2089355671900709099
TEXT: People come up with elaborate explanations of why things are like they are, but then they are just because of some weird decision. Similar story in C where people to this day cargocult common prefixes for struct fields, even though they only exist because they used to be global. https://t.co/67tRC2th6q
--
T=2089358222939332955 | @mitsuhiko | 2026-08-17T14:26+00:00 | L191 RT5 C4 V14661 | post
URL=https://x.com/mitsuhiko/status/2089358222939332955
TEXT: Look at the bright side of life. https://t.co/kR133PxqE7
--
T=2089372027056476295 | @mitsuhiko | 2026-08-17T15:21+00:00 | L53 RT2 C3 V6981 | post
URL=https://x.com/mitsuhiko/status/2089372027056476295
TEXT: Didn't we all ask for a bit of friction and back pressure? GitHub is providing it! https://t.co/sRtfmlqaKY
QUOTED @mitsuhiko: Look at the bright side of life. https://t.co/kR133PxqE7
LINKS: https://x.com/mitsuhiko/status/2089358222939332955?s=20
--
T=2089374335387463907 | @mitsuhiko | 2026-08-17T15:30+00:00 | L93 RT4 C10 V13857 | post
URL=https://x.com/mitsuhiko/status/2089374335387463907
TEXT: I don't have anything there, but maybe now is a good time to point out that I have a tangled account. https://t.co/HuEDNQlRri
LINKS: https://tangled.org/mitsuhiko.at
--
T=2089420729997513167 | @mitsuhiko | 2026-08-17T18:34+00:00 | L109 RT2 C7 V9289 | post
URL=https://x.com/mitsuhiko/status/2089420729997513167
TEXT: People are saying Cursor has great timing to launch Origin but given how often GitHub is down these days I don’t find the timing to be too impressive :P
--
## @natolambert — 4 шт.

T=2089370522689606078 | @natolambert | 2026-08-17T15:15+00:00 | L118 RT9 C10 V14751 | post
URL=https://x.com/natolambert/status/2089370522689606078
TEXT: The core of open-source AI is that the training recipe itself is the closest analogue to Linux and open-source software. Model weights are transient. Nvidia is building their models in the open so everyone can build their own later, avoiding a monopoly on intelligence.
QUOTED @interconnectsai: Teaching Everyone to Fish for Tokens
Nvidia wants you building your own model, not buying from Anthropic/OpenAI.
https://t.co/Zo61qqn5li
--
T=2089382137875005858 | @natolambert | 2026-08-17T16:01+00:00 | L115 RT15 C11 V13325 | thread(2)
URL=https://x.com/natolambert/status/2089382137875005858
TEXT: Nvidia’s optimism on open-source AI harkens back to Meta &amp; Google investing so much in the free web with the assumption that if more people get more access to the web, good things will happen. Nvidia's betting AI will play out similarly -- massive explosion in opportunities.
[->] I hope @NVIDIAAI is as successful as google was in open source ;)
QUOTED @interconnectsai: Teaching Everyone to Fish for Tokens
Nvidia wants you building your own model, not buying from Anthropic/OpenAI.
https://t.co/Zo61qqn5li
--
T=2089389309333787107 | @natolambert | 2026-08-17T16:30+00:00 | L492 RT16 C23 V82877 | post
URL=https://x.com/natolambert/status/2089389309333787107
TEXT: I tell a ton of people that getting a PhD is not a good idea for your career, but it’ll likely be far higher in personal growth and fulfillment which is maybe worth way more anyways. I need to think about how to price that in.
QUOTED @NateSilver538: Rare unironic life advice. It can be great for many people but if you're on the fence about whether to go to some sort of graduate school, i.e. you don't have something fairly specific you're trying to accomplish, probably don't. A much worse value proposition than 20 years ago.
--
T=2089480421792780312 | @natolambert | 2026-08-17T22:32+00:00 | L111 RT3 C8 V5991 | post
URL=https://x.com/natolambert/status/2089480421792780312
TEXT: Personal milestone: 1000 true fans of @interconnectsai ! Hitting a very long term goal feels great. 

I’m very happy to get to be an independent voice in AI. Cultivating a paid base helps me commit to that longer term, and scale Interconnects’ impact. https://t.co/SRBayGvFg7
--
