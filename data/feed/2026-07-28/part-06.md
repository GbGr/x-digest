# X-FEED 2026-07-28 part 6/13 | items: 12

## @mitchellh (продолжение)

T=2081842660634218691 | @mitchellh | 2026-07-27T20:42+00:00 | L1761 RT92 C30 V132152 | post
URL=https://x.com/mitchellh/status/2081842660634218691
TEXT: Btw this is why computer science matters. Yes, you can self teach it if you really want to (I personally wouldn't have had the discipline, so college was a way better force). However you learn it, the theoretical fundamentals matter and get applied to work every single day.
QUOTED @mitchellh: If you're interested in "how" or "why": the major culprit is that each row in Alacritty has 32 bytes of metadata and each cell is 24 bytes. In Ghostty, every row and cell is represented by exactly 8 byte each. How do we do this?

The first major culprit is styles. Alacritty stores the full cell style alongside each cell (foreground, background, underline, etc.). Ghostty stores a 16-bit style ID and de-dupes all styles into a look-aside custom reference-counted hash table.

MOST cells are unstyle
--
T=2081853246084468846 | @mitchellh | 2026-07-27T21:24+00:00 | L77 RT4 C4 V4181 | post
URL=https://x.com/mitchellh/status/2081853246084468846
TEXT: Realistic projects attached to theoretical concepts is what always worked best for me. Like, yes, you need to write proofs (PUMPING LEMMA BABY), but also, lets do something realistic instead of e.g. teaching SIMD through fast summation. 

The best course I ever took was our OS + databases (two separate classes ofc) courses. The former we actually hacked on the real Linux kernel. The latter we got source access to MS SQL to learn from.
--
T=2081914005422252092 | @mitchellh | 2026-07-28T01:25+00:00 | L4 RT1 C1 V193 | thread(3)
URL=https://x.com/mitchellh/status/2081914005422252092
TEXT: Data structures (hash tables, linked lists), OS or CPU arch (allocators, cache awareness, virtual memory, general byte/bit size consideration), etc. These are obviously the applications in practice, but based on fundamental knowledge like algo complexity, etc. You can learn just the application but the theory solidifies it much stronger.
[->] I disagree. 

You can't optimize the performance of something and choose to use a hash table if you don't understand the basic properties of a hash table. 

You can't optimize memory locality if you don't understand why locality even exists or how the virtual memory system interacts with it.

You can't "performance engineer" what you don't understand. And to understand, my point is that can go a long way with just the applicable knowledge (but you still need it), but the theoretical grounding really gives it a different meaning.

Etc.
[->] To put it another way very specifically, how do you "performance engineer" a hash table if you don't understand how it resolves collisions? 

Separate chaining, open addressing, Robin Hood hashing, etc. fundamentally changes its performance characteristics.

But the actual reason to implement it this way isn't just performance, they're different tradeoffs between memory usage, cache locality, allocation behavior, deletion complexity, probe length, and worst-case behavior.

You can, I guess, be overly reductionist and reduce that down to "performance," but I'd say its more about system architecture and general understanding. It may be dictated by hardware rather than any need for performance, for example.
--
## @mitsuhiko — 9 шт.

T=2081687574272168068 | @mitsuhiko | 2026-07-27T10:26+00:00 | L1 RT0 C0 V38 | post
URL=https://x.com/mitsuhiko/status/2081687574272168068
TEXT: @hexlabsoftware I just analyze my pi sessions and that’s what I can tell you.
--
T=2081690056297721921 | @mitsuhiko | 2026-07-27T10:36+00:00 | L493 RT14 C26 V33117 | thread(3)
URL=https://x.com/mitsuhiko/status/2081690056297721921
TEXT: I feel like more and more places have now an "Office of the Slop" where some people just vibe code random nonsense.
[->] @SIGKITTEN If you don’t have a Chief Slop Officer you’re ngmi
[->] @SIGKITTEN If you ask @badlogicgames he would agree.
--
T=2081690173343982015 | @mitsuhiko | 2026-07-27T10:36+00:00 | L7 RT0 C5 V1776 | thread(4)
URL=https://x.com/mitsuhiko/status/2081690173343982015
TEXT: @thorstenball @badlogicgames (no i don't use plan mode)
[->] @thorstenball @badlogicgames Ackshually …
[->] @thorstenball @badlogicgames What do you mean "never had"?! https://t.co/imNtqx2von
[->] @thorstenball @badlogicgames That tweet was only four AI years ago!
LINKS: https://x.com/beyang/status/2001150592480313425
--
T=2081746793163853914 | @mitsuhiko | 2026-07-27T14:21+00:00 | L66 RT0 C4 V13672 | thread(5)
URL=https://x.com/mitsuhiko/status/2081746793163853914
TEXT: I love that apparently the source of my durable object performance issues right now is Sentry's integration. Well, let's get to the bottom of this.
[->] @madbyk Basically it slows down the durable object way too much flushing out stuff
[->] @madbyk I haven't figured out yet if there is a way to do some async flushes somehow
[->] @DanielGri @madbyk I’m honestly not entirely sure what’s going on because CF makes that hard to find out. Clanker is convinced that I need to get rid of sentry entirely to get the DO not to contend. Seemingly 95% of the execution time is sentry flushing spans.
[->] @DanielGri @madbyk Context here is that there can just be one instance of the DO
--
T=2081781224842871086 | @mitsuhiko | 2026-07-27T16:38+00:00 | L37507 RT6056 C1220 V7819294 | rt
URL=https://x.com/mitsuhiko/status/2081781224842871086
RT-OF @Kimi_Moonshot (L37507): Releasing the model weights and technical report of Kimi K3.

Kimi K3 is our most capable model: a 2.8T MoE model with native visual understanding and a 1M-token context window.

New model architecture: 2.5x the intelligence per unit of compute, not just more params.

Alongside Kimi K3, we're opening up more of the stack behind it — high-performance attention kernels, MoE communication library, and infrastructure for running agent environments at scale.

Model weights: https://t.co/7m7eEg6Y0B
Tech report:  https://t.co/yeu6cjpMCT
Tech blog: https://t.co/YTfiMSNM1f
RT-URL=https://x.com/Kimi_Moonshot/status/2081760186235289764
TEXT: RT @Kimi_Moonshot: Releasing the model weights and technical report of Kimi K3.

Kimi K3 is our most capable model: a 2.8T MoE model with n…
LINKS: http://huggingface.co/moonshotai/Kimi-K3 ; http://github.com/MoonshotAI/Kimi-K3/blob/master/k3_tech_report.pdf ; http://kimi.com/blog/kimi-k3
--
T=2081816340885582123 | @mitsuhiko | 2026-07-27T18:57+00:00 | L76 RT3 C3 V11487 | post
URL=https://x.com/mitsuhiko/status/2081816340885582123
TEXT: I think this is fair but I wish these were springing licenses such as the FSL. Convert to regular MIT a few years down the line.
QUOTED @__tinygrad__: This is a great sustainable business model for open weights. It's free if you run it yourself, but if you are running a cloud providing it to others for money, you should have to share profits. (from Kimi K3 License) https://t.co/mK9jKeHe37
--
T=2081818517901344845 | @mitsuhiko | 2026-07-27T19:06+00:00 | L44 RT0 C8 V4798 | thread(5)
URL=https://x.com/mitsuhiko/status/2081818517901344845
TEXT: Every time we go camping. https://t.co/SJ7k1TOh3e
[->] @MartinHeisenbe1 That’s not a roof tent
[->] @MartinHeisenbe1 I’m in the market for this. https://t.co/h5BAQT39Wa
[->] @baptistedajon @MartinHeisenbe1 @Decathlon Indeed.
[->] @rolandkdev Oh don’t tempt me. Sadly California doesn’t scale to a family of 5 :)
--
T=2081823641377907198 | @mitsuhiko | 2026-07-27T19:26+00:00 | L0 RT0 C1 V232 | post
URL=https://x.com/mitsuhiko/status/2081823641377907198
TEXT: @lucasmeijer @badlogicgames Come back when we leave the TUI behind us ;)
--
T=2081848260788981899 | @mitsuhiko | 2026-07-27T21:04+00:00 | L86 RT0 C6 V10986 | thread(2)
URL=https://x.com/mitsuhiko/status/2081848260788981899
TEXT: Pi build me a local version of durable objects matching production behavior completely. Make no mistakes (I hope this will help me debug shit)
[->] @_ashleypeacock @dillon_mulroy Seeing some contention on a durable object (probably because I’m a dum dum but I cannot Repro locally)
--
