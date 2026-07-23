# X-FEED 2026-07-23 part 6/9 | items: 8

## @mitchellh — 2 шт.

T=2079955485365866786 | @mitchellh | 2026-07-22T15:43+00:00 | L1176 RT36 C19 V47788 | post
URL=https://x.com/mitchellh/status/2079955485365866786
TEXT: Ghostty and libghostty are now on Zig 0.16! This was done by a [paid!] contributor. Through this process, the Ghostty non-profit also paid for hours to contribute over a dozen patches upstream to the translate-c and arocc projects which help the entire ecosystem. Amazing work.

Zig 0.16 came out awhile ago, but in reality it wasn't a focus of the project to upgrade until the past few weeks. It did take a few weeks to upgrade, but the primary complexity was due to C translation/integration and not Zig itself.

Zig 0.16 switched C translation from clang to the translate-c/arocc projects which are faster and a much smaller dependency. 

Ghostty is a very complex C user, consuming Apple headers (e.g. blocks), Windows headers, GTK headers, SIMD intrinsic headers, and more. This stressed these upstreams and we had to fix a number of issues to get through. 

This was high quality and good work though and I'm happy to see it help the ecosystem. translate-c and arocc are just excellent standalone projects even if you're not interested in Zig. They're way easier to embed than clang and solve that problem well.

Upstream patches:
* translate-c: https://t.co/jxEeVYsHpu
* arocc: https://t.co/16QetK5g4I
LINKS: https://codeberg.org/ziglang/translate-c/pulls?q=author%3Avancluever&type=all&sort=relevance&state=closed&labels=&milestone=0&project=0&assignee=0&poster=714165&archived=false ; https://github.com/Vexu/arocc/pulls?q=author%3Avancluever+is%3Aclosed
--
T=2079992025261424803 | @mitchellh | 2026-07-22T18:08+00:00 | L1781 RT167 C30 V70418 | post
URL=https://x.com/mitchellh/status/2079992025261424803
TEXT: Wrote up a practical introduction to SIMD using a real example from Ghostty. SIMD has a reputation for being complex, but the common case follows a simple, repeatable shape and shouldn’t be scary! Everyone should know at least this much. https://t.co/yVcAycaq8P
LINKS: https://mitchellh.com/writing/everyone-should-know-simd
--
## @natolambert — 6 шт.

T=2079934392563343844 | @natolambert | 2026-07-22T14:19+00:00 | L263 RT6 C17 V12574 | post
URL=https://x.com/natolambert/status/2079934392563343844
TEXT: Number 1 on day 1, is a good way to start. https://t.co/Jj9WWPzCFY
QUOTED @natolambert: My book, Reinforcement Learning from Human Feedback is done!

This is the book I wish I had when learning to fine-tune, align, & now post-train models since ChatGPT. The resource has been built by me finding time to study and document the fundamentals on nights and weekends since 2024. 

Transferring as much of the intuitions of building Olmo as I possibly can in the book format.

The book is launching with an over 10 hour, full course with slidedecks, functional code for the training chapters, 
--
T=2079935460265382048 | @natolambert | 2026-07-22T14:23+00:00 | L189 RT27 C8 V14839 | thread(2)
URL=https://x.com/natolambert/status/2079935460265382048
TEXT: New podcast with @xeophon on all things open models. More on Kimi K3, Qwen 3.8, GLM-5.2, Xi's WAIC speech, distillation, the open-closed Gap, and what's next.

Chapters:
00:00 Welcome & context
04:38 Living with / using Kimi K3
08:53 GLM 5.2’s continued role
12:47 How are the Chinese models this good?
17:41 Data, environments, and a tour of the Chinese labs
19:47 Roundup of Chinese providers: Qwen, DeepSeek, MiniMax…
24:08 The US open-model ecosystem
30:25 Frontier vs. near-frontier, and the cybersecurity case against bans
34:58 Distillation and the Ben Thompson debate
44:12 Predictions and a frontier tier list
48:36 Wrap-up

Hoping to keep doing a few more of these on @interconnectsai. Crucial times in AI, we're working hard to share our expertise.
[->] @xeophon YouTube: https://t.co/2wWxSm3BMl
Interconnects: https://t.co/HS8Wo9aAAB
LINKS: https://www.youtube.com/watch?v=XsBy8UGIY-I ; https://www.interconnects.ai/p/open-models-recap-more-on-kimi-k3
--
T=2079940672354931138 | @natolambert | 2026-07-22T14:44+00:00 | L52 RT4 C4 V10014 | post
URL=https://x.com/natolambert/status/2079940672354931138
TEXT: We're starting to see early forms of how the government can support development and use of open models in the US. Congrats to my friends at Arcee for this big step.
QUOTED @latkins: We've been quiet since Trinity-Large-Thinking came out in early April - but for good reason!

I'm excited to finally share that not only have we @arcee_ai  joined the DOE's Genesis Mission, but to also announce the development of Genesis-Science-1. https://t.co/bh6oaE5G5P
--
T=2080044382456263007 | @natolambert | 2026-07-22T21:36+00:00 | L839 RT47 C46 V32647 | rt
URL=https://x.com/natolambert/status/2080044382456263007
RT-OF @signulll (L839): if you’re a major ai lab publicly complaining that you’ve been distilled, that is not a good look. at all.

normal ppl do not care that you feel wronged. they see a company claiming to build the most powerful systems on earth while asking everyone else to protect its homework.

the security implications are different & deserve serious consideration, especially cuz model weights are opaque black boxes.

but commercial grievance dressed up as principle is not going to persuade anyone.
RT-URL=https://x.com/signulll/status/2080038160592228684
TEXT: RT @signulll: if you’re a major ai lab publicly complaining that you’ve been distilled, that is not a good look. at all.

normal ppl do not…
--
T=2080047222146928696 | @natolambert | 2026-07-22T21:47+00:00 | L135 RT5 C7 V6768 | thread(2)
URL=https://x.com/natolambert/status/2080047222146928696
TEXT: At night I dream of a distillation debate grounded in public, technical info, not reading tea leaves of backroom deals and political intrigue. 

Then I wake up and I'm crushed by reality of chaos, potentially classified information, and a spiraling global AI ecosystem.
[->] Where I think things are at: the public information MASSIVELY favors the state of affairs that distillation is fine, no action needed. Public research shows minimal effect.

There have been some classified reports (e.g. data from NSA, other govt agencies), private briefings from labs, which show more influential usage & impact, but not a 100% crucial role in training. I.e. the Chinese are incredibly good at using the APIs to train models, better than anyone in the U.S. or public research.

A lot of the "we must act now" rhetoric comes from an additional embellishment of the second point.
--
T=2080052152475775078 | @natolambert | 2026-07-22T22:07+00:00 | L554 RT47 C42 V45452 | post
URL=https://x.com/natolambert/status/2080052152475775078
TEXT: There's no legal precedent that model outputs are IP. I'd argue it also doesn't stand up conceptually. 

The frontier labs are under no obligation to have their APIs be available to these customers, and can protect model generations in other ways if they want to.
QUOTED @SecScottBessent: We support open-source AI and the innovation it unlocks. But open source is not open season on American IP. When PRC firms conduct covert, industrial-scale distillation attacks that cross the line into IP theft, sanctions and Entity List designations will be on the table.
--
