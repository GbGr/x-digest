# X-FEED 2026-07-28 part 5/13 | items: 2

## @mitchellh — 5 шт.

T=2081788657078505732 | @mitchellh | 2026-07-27T17:07+00:00 | L705 RT14 C21 V99546 | thread(11)
URL=https://x.com/mitchellh/status/2081788657078505732
TEXT: libghostty vs. Alacritty (alacritty_terminal crate) memory usage. This tests pure terminal state with various payloads: empty screen, full screen, 10K row scrollback with plain text, unicode, heavy styling, and mixed. This is the most accurate read to what an embedder sees.
 
So, when you see meme posts about Ghostty (or any of its embedders) memory usage, that is the fault of the application. Ghostty GUI itself certainly has some memory bloat! But its the GUI apps causing this, not libghostty. 

Note that Ghostty's results include our active scrollback compression, which Alacritty doesn't support. This is fair because it is on by default and happens automatically (while we still have higher IO throughput than Alacritty). It is the proper like-for-like comparison because it's what you'd experience. 

I included uncompressed numbers too though even though you'd have to actively try to get these, just to show even uncompressed is significantly better.

Also, these were all run within the same Rust-written binary that embeds both, so it also avoids measuring the binary overhead differently since they run from an identical binary.

I'm working on also measuring libvte and writing a longer form blog post to share the whole testing setup. I needed something to link to whenever I see the memes.

libghostty is small, nimble, and excellent software.
[->] @dakull one of our maintainers slop forked alacritty and memed this in lol. I’m trying to goad him into making a PR
[->] @silva_anxo We’ve done those before and I’ve posted them before. This is purposely addressing specifically memory usage since it’s memed on.
[->] @nikitf777 There are clearly many dimensions to benchmarking, this is purposely addressing memory usage. I’ll show others later.
[->] Yep, as noted, I plan to release the full suite. Its not exciting, its literally just filling a terminal and reading the memory usage use macOS syscalls. 

For why it jumps to 30MB, I know why. Its two things:

1. Alacritty stores all styles (in particular) alongside every cell. Their cell structure is multiple times larger than Ghostty. Its not visible in an empty/full viewport with 120x40 because its just not that many cells.

Ghostty stores every cell as a packed 64-bit value with de-dupped look-aside tables for styles, hyperlinks (untested here), and graphemes. It dramatically increases the code complexity but results in crazy savings.

As a result, Alacritty is basically O(N) as scrollback increases and you have to pay style costs even for plain cells. Ghostty does not.

It does slow down some operations but we make it up in other places (this benchmark doesn't show IO but we've already showed that plenty of times, we're faster even at Alacritty's own benchmarks there). 

2. Ghostty has scrollback compression. We're able to achieve this because we store every 400KB chunk of grid as a single base address + offsets (rather than N pointers). So simply compress the raw memory.
[->] @TheNoamLewis Not really, because Linux doesn't believe in binary compatibility across distros. For macOS, we ship binary compatible frameworks that work on macOS and iOS for the past 4 years of OS releases.
[->] @TheNoamLewis Yep, we should provide DLLs actually...
[->] @rodrigolj libghostty is fully supported on Windows (we test in CI, and have other projects utilizing it).
[->] @Art049 Nothing lol. Just what I did by default, I didn't put much thought into it.
[->] @tawnniee @dakull This is not the whole app. See the graphs, they all say it’s the alacritty terminal crate. It is apples to apples. The app uses way more RAM!
[->] @tawnniee @dakull Linux or Mac? One of our maintainers is working on one for Linux (Wayland only) and mains it daily.
--
T=2081833183835013618 | @mitchellh | 2026-07-27T20:04+00:00 | L969 RT35 C13 V190097 | thread(9)
URL=https://x.com/mitchellh/status/2081833183835013618
TEXT: If you're interested in "how" or "why": the major culprit is that each row in Alacritty has 32 bytes of metadata and each cell is 24 bytes. In Ghostty, every row and cell is represented by exactly 8 byte each. How do we do this?

The first major culprit is styles. Alacritty stores the full cell style alongside each cell (foreground, background, underline, etc.). Ghostty stores a 16-bit style ID and de-dupes all styles into a look-aside custom reference-counted hash table.

MOST cells are unstyled, and when there are styles MOST styles are shared, and when styles are shared MOST are repeated in a run (multiple cells with the same style in a row). Put this all together, and the tradeoff on compute to access it doesn't even end up being slower.

Next, codepoints. Alacritty stores multi-codepoint graphemes (like, Emoji) by having an 8-byte nullable pointer to a `Vec<char>`. This hurts doubly: (1) its almost always null (because multi-codepoint is rare) yet you pay an 8 byte cost on every cell and (2) every multi-codepoint grapheme triggers a heap allocation to make that Vec.

Ghostty stores single codepoints inline, but multiple codepoints in a look-aside table. The memory for this table uses a custom bitmap-tracked chunk-allocator (since grapheme frequency follows a measurable curve we calculated by scanning various online texts). The presence of graphemes is marked by a 2-bit content tag in our packed 64-bit cell. To keep the key small in the hash table, its limited to a 16-bit unsigned int that is an offset from a base pointer.

Okay, the astute systems programmer will quickly notice there are a lot of 16-bit integers and ask: so this is all limited to a max of ~65K values? 

Nay. We maintain our grid using a linked list of contiguous ~400KB memory chunks (which themselves are in a memory pool using a custom allocator to speed up alloc/free). Each memory chunk is limited to 2^16. If/when we reach a limit, we move to the next page. In practice, this really doesn't happen except under pathological cases... the important point is we handle it.

Lots, lots, lots more details, but thats a 10,000 foot view.

These things alone account for ~95% of the difference of our uncompressed vs. Alacritty's uncompressed memory usage. (Theres also a reason why Alacritty's data structures aren't trivially compressable but thats a whole other topic)
[->] @dcolascione Because there aren't many that are embeddable, and that's what matters here. As noted in my quote post, I plan on looking at libvte too.
[->] @EmGeeDoubleU this is probably AI? sounds like AI, but maybe i can train the brain: because a pointer needs 64-bits (usually, nowadays) and I don't have that kind of space.
[->] @dcolascione Oh sorry missed this. Honestly, we never tried this. I could see in my head it working I can see it not working. I don't see it as an obvious big win. Even under style heavy workloads our ref counting doesn't show up on benchmarks at this stage.
[->] @C99Chad @EmGeeDoubleU Its like... so nonsense lol. Its hard to fathom how a human being could come up with it. So its either an AI or a massive idiot, and its kinder to assume AI.
[->] @IAmZerebos @dcolascione @raphamorims Oh good idea. I just did alacritty cause it’s the one most memed. But I plan on doing libvte and will look at this too
[->] @sebuzdugan Yes and no. Styles are usually used for a run of text so you have it for a bit. Having an 8 byte cell lets more cells fit on the cache line (we keep all cells packed). We keep all styles packed too (in separate). Custom allocators
[->] @sebuzdugan Also the only thing that needs to READ styles is the renderer. And we just copy the style contiguous block over in a critical area. Renderer can be a lot slower. We’ve got 8ms for a 120hz frame. In practice a full setup is microseconds though
[->] @OctagonSuitcase @ZH1YGD Its pretty much there. I'm waiting for a few more implementations to iron out any issues (e.g. neovim is very close) and I'm close to tagging it. Full C API here: https://t.co/iehlJ3zwof
QUOTED @mitchellh: libghostty vs. Alacritty (alacritty_terminal crate) memory usage. This tests pure terminal state with various payloads: empty screen, full screen, 10K row scrollback with plain text, unicode, heavy styling, and mixed. This is the most accurate read to what an embedder sees.
 
So, when you see meme posts about Ghostty (or any of its embedders) memory usage, that is the fault of the application. Ghostty GUI itself certainly has some memory bloat! But its the GUI apps causing this, not libghostty. 
LINKS: https://libghostty.tip.ghostty.org/
--
