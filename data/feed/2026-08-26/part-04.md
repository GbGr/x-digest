# X-FEED 2026-08-26 part 4/7 | items: 7

## @mitchellh — 2 шт.

T=2092250065582895509 | @mitchellh | 2026-08-25T13:57+00:00 | L308 RT3 C14 V17523 | post
URL=https://x.com/mitchellh/status/2092250065582895509
TEXT: OSC parsing in libghostty was our last non-SIMD optimized VT stream path. OSCs are usually small so it just never showed up on benchmarks. But now that we are potentially passing megabytes of data (Kitty clipboard), it got the SIMD treatment. 🫡 https://t.co/JbsTM0Jy7o
--
T=2092326409071198210 | @mitchellh | 2026-08-25T19:01+00:00 | L1495 RT46 C59 V57483 | post
URL=https://x.com/mitchellh/status/2092326409071198210
TEXT: The Ghostty memory usage memes are dead with the upcoming 1.4 release, much to the dismay of internet trolls everywhere. ~10x less memory for a visible window. ~450x lower for a non-visible window. Very reasonable compared to other terminals with 10 tabs.

This was the result of a lot of incremental hard work, but there were two big wins. One I talked about before which was scrollback compression. I want to note that these charts do NOT include scrollback, so with scrollback the results are more dramatic!

The other big win is that we free almost all GPU resources when a window is fully occluded (covered by another window, minimized, etc.). We triple-buffer our screens so for large screens this has major savings.

Those account for a large chunk of the improvements, but we also had dozens of incremental 1% wins here, a few KB there, etc. throughout the 1.4 cycle. And there are more coming!

I noted before that Ghostty's memory waste was all in the app layer and we can see it here. libghostty has always been very tight in comparison and I've shown comparisons to other embedded terminal libraries elsewhere.

And importantly, the charts below use the same grid sizes with a very small +/-2% difference due to differences in how cell metrics are calculated between terminals.
--
## @mitsuhiko — 2 шт.

T=2092345827964424476 | @mitsuhiko | 2026-08-25T20:18+00:00 | L49 RT1 C8 V9202 | post
URL=https://x.com/mitsuhiko/status/2092345827964424476
TEXT: There must be some sort of consolidated effort going on to make people really hate taxation. https://t.co/mbO584uKbJ
QUOTED @Polymarket: JUST IN: Germany’s proposed “sugar tax” would reportedly also cover zero-sugar beverages that use artificial sweeteners.
LINKS: https://x.com/Polymarket/status/2092329194051035182?s=20
--
T=2092373066940617186 | @mitsuhiko | 2026-08-25T22:06+00:00 | L352 RT6 C41 V12954 | post
URL=https://x.com/mitsuhiko/status/2092373066940617186
TEXT: Maybe I just read too much AI text now vs before, but I really feel like the model's ability to produce text I actually want to read and understand went downhill with newer releases.
--
## @natolambert — 3 шт.

T=2092217514419691684 | @natolambert | 2026-08-25T11:48+00:00 | L59 RT5 C10 V7087 | post
URL=https://x.com/natolambert/status/2092217514419691684
TEXT: In the frantic era feeling early RSI effects, sending friends physical books, hosting events, chatting with students early on their ai journey, etc are all wonderful to do. Many things AGI won’t replace, and it’s easy to forget to do them. I’ll visit a few more universities!
QUOTED @yacinelearning: just received a great bed time reading book by the mail looking forward for tonight https://t.co/aKoXDIVVV3
--
T=2092298564537897198 | @natolambert | 2026-08-25T17:10+00:00 | L227 RT16 C18 V28512 | rt
URL=https://x.com/natolambert/status/2092298564537897198
RT-OF @xeophon (L227): happy that the blog is finally out, i tried to be as transparent and in-depth as possible to make clear
- what happened
- what could've happened and how a simple reward hack could turn into a security issue

some more thoughts:
https://t.co/yMHN4fkIeZ
RT-URL=https://x.com/xeophon/status/2092287596109967809
TEXT: RT @xeophon: happy that the blog is finally out, i tried to be as transparent and in-depth as possible to make clear
- what happened
- what…
LINKS: https://x.com/PrimeIntellect/status/2092283970537017598?s=20
--
T=2092381263478817138 | @natolambert | 2026-08-25T22:39+00:00 | L121 RT1 C9 V6753 | post
URL=https://x.com/natolambert/status/2092381263478817138
TEXT: OOO for a bit, time to celebrate &amp; rest :) https://t.co/SUDnav5fYE
--
