# X-FEED 2026-08-15 part 3/7 | items: 10

## @mattpocockuk — 6 шт.

T=2088168130824561139 | @mattpocockuk | 2026-08-14T07:37+00:00 | L27 RT0 C5 V4490 | post
URL=https://x.com/mattpocockuk/status/2088168130824561139
TEXT: @tomdevisser Also /improve-codebase-architecture
--
T=2088169856298348997 | @mattpocockuk | 2026-08-14T07:44+00:00 | L889 RT9 C31 V81513 | post
URL=https://x.com/mattpocockuk/status/2088169856298348997
TEXT: The grill &gt; shill pipeline is real
QUOTED @theo: Gotta say that Matt's "grill-me" skill is exceptional and helps a ton with getting agents aligned with my brain
--
T=2088255075634364551 | @mattpocockuk | 2026-08-14T13:23+00:00 | L99 RT13 C1 V16110 | rt
URL=https://x.com/mattpocockuk/status/2088255075634364551
RT-OF @dotnet (L99): Matt Pocock drops an agent‑skills masterclass:
🔥 grill‑me → interrogates plans before coding
🗺️ wayfinder → decision‑tree planning w/ fog zones
📚 grill‑with‑docs → thin DDD‑style repo docs
🧠 smart vs dumb context zones
🎧 https://t.co/5LfgBRQr9S https://t.co/N4Jwv9ksGH
RT-URL=https://x.com/dotnet/status/2087977829099065652
TEXT: RT @dotnet: Matt Pocock drops an agent‑skills masterclass:
🔥 grill‑me → interrogates plans before coding
🗺️ wayfinder → decision‑tree plann…
LINKS: https://buff.ly/vpLKNEE
--
T=2088256526372815234 | @mattpocockuk | 2026-08-14T13:28+00:00 | L853 RT26 C53 V54259 | thread(2)
URL=https://x.com/mattpocockuk/status/2088256526372815234
TEXT: https://t.co/ObUDIg67QN
[->] One thing I've underplayed in my skill set is how customizable it is

Specifically the /code-review skill

1. Notice the agent is doing something bad
2. Write it in CODING_STANDARDS.md (root of the repo)
3. /code-review picks it up and enforces it at review time

I have hundreds of lines in my CODING_STANDARDS.md files
LINKS: https://www.aihero.dev/skills-code-review
--
T=2088272462618247478 | @mattpocockuk | 2026-08-14T14:32+00:00 | L853 RT7 C16 V52366 | post
URL=https://x.com/mattpocockuk/status/2088272462618247478
TEXT: When you realise @theo has filmed a video about my skills...

...PERFECTLY timed for my next product launch

Serendipity slaps
--
T=2088290954910347312 | @mattpocockuk | 2026-08-14T15:45+00:00 | L3066 RT147 C51 V133417 | thread(2)
URL=https://x.com/mattpocockuk/status/2088290954910347312
TEXT: Here's the Crash Course! Dropping on Monday:

https://t.co/Ws6UxJKV1N
[->] Just saw a comment saying that I've never made a proper overview of EVERY skill in my skills repo

I thought "damn it, he's right".

So, here it is. My 25 skills (now @theo-approved), explained in 10 minutes: https://t.co/V4LrLeTduf
LINKS: https://www.aihero.dev/s/YkXWCF
--
## @mitchellh — 4 шт.

T=2088102633190064559 | @mitchellh | 2026-08-14T03:17+00:00 | L69 RT0 C0 V8205 | post
URL=https://x.com/mitchellh/status/2088102633190064559
TEXT: @bcardarella I never used Elixir, but had to do high-performance Erlang for a few years. We had to dive into NIFs pretty heavily. This was way back in 2011 or so so I'm not sure how BEAM has improved (or not) since then. Its a pain in the ass but no choice.
--
T=2088346714545750422 | @mitchellh | 2026-08-14T19:27+00:00 | L836 RT11 C34 V53782 | post
URL=https://x.com/mitchellh/status/2088346714545750422
TEXT: Look how good these themes are. They permeate through the app plus into the terminal. 

We built out a set of 41 fully original human designer curated themes. We also built a full in browser theme editor. 

The plan is to open source with a permissive license and package them all up for all the most popular tools (editors, terms, etc.). These aren’t just for our product. 

“Why?” There’s a lot of beautiful themes out there that are questionable on licensing. This enables us to give out a truly unencumbered set of themes spanning all those styles. Plus, beauty matters. Customization matters.
QUOTED @almonk: It's Friday, lets talk about themes.

For @superlogical we've created a suite of 41 original themes for both light and dark modes that are portable across all our clients.

Themes tint not just the ANSI terminal colors, but the entire application chrome. https://t.co/zazgcO8Cdq
--
T=2088378990998524206 | @mitchellh | 2026-08-14T21:35+00:00 | L268 RT6 C12 V30698 | post
URL=https://x.com/mitchellh/status/2088378990998524206
TEXT: libghostty for WebAssembly got a lot of love recently and is now very, very, very good. I spent the day building harnesses and comparing to xterm.js and here are the results: faster at IO, faster at reflow, faster at rendering. Like, a lot a lot faster. 

We now provide pre-built `ghostty-vt.wasm` files in our GitHub releases. These are the fastest, most optimized builds that are compatible with every major browser going back a number of years.

Before going over setups, I want to say that xterm.js is very good software. It is a relatively modern terminal, the maintainers are very nice, it's done incredible work for the web terminal ecosystem. I have nothing against them, but I'm in the business of making super fucking fast terminal emulators.

Let me explain the setup in every case:

IO throughput: This is an apples-to-apples comparison of `ghostty_terminal_vt_write` vs xterm's `Terminal.write(Uint8Array)` timed from first write to final completion callback. This is testing how fast a terminal emulator can process input and update internal state. Nothing else. Units are in MB/s processed.

Note for graphemes: Ghostty has grapheme processing enabled and xterm.js does not (requires an addon). So, this shows how Ghostty does better despite having that cost.

Column reflow throughput: Compares `ghostty_terminal_resize` to xterm's `Terminal.resize` with identical terminal states (same content, same size, same scrollback). The "dance" is rapid bigger/smaller resize of matching column widths, forcing text reflow. Units are in resizes/second.

Render speeds: These test use the identical xterm.js WebGL renderer for both Ghostty and xterm.js. Since the renderer is identical, we can focus on how long it takes to prepare the inputs to the renderer (build the render state) and assert we get the same output byte-for-byte (since its the same renderer!). This is the truest way to measure these two because libghostty-vt itself does not provide a renderer, its about how long it takes to go from terminal state to render-ready.

Full render: This tests a fresh renderer with nothing previously rendered. Units are in updates/second.

Incremental render: This tests having prior state and only rendering specific changes such as adding scrollback, moving the viewport, moving the cursor. Units are in updates/second.

This is using the latest released version of xterm in every case compared to the HEAD libghostty (since we haven't tagged a release, exact commit d760ee96e54657416eb427b793c7e839f003df7d).
--
T=2088383346439336232 | @mitchellh | 2026-08-14T21:52+00:00 | L116 RT4 C6 V17398 | post
URL=https://x.com/mitchellh/status/2088383346439336232
TEXT: A couple more notes on this:

First, the xterm.js benchmarks were very noisy. A lot of the results relied on whether they got lucky with the V8 JIT/inliner. e.g. the frame times for ASCII ranged from 20us to 100us (!!!). For the purpose of optimism, I only used the fastest times in the medians below and threw out anything about a 20% deviation from the min.

Ghostty on the other hand had a variation of at most 1.5% on any given run. I suspect this is due to the heavy (near-exclusive) use of WebAssembly, which isn't as beholden to the runtime gods. 

Next, bundle size. Ghostty's Wasm bundle is significantly larger than xterm.js. Our fast bundle is ~1.1MB uncompressed. xterm.js ~270KB uncompressed. Both very cache-able. I've tried to optimize this but there isn't a lot of juice to squeeze that I can find, Ghostty has to ship with a huge amount of Unicode tables for example.
QUOTED @mitchellh: libghostty for WebAssembly got a lot of love recently and is now very, very, very good. I spent the day building harnesses and comparing to xterm.js and here are the results: faster at IO, faster at reflow, faster at rendering. Like, a lot a lot faster. 

We now provide pre-built `ghostty-vt.wasm` files in our GitHub releases. These are the fastest, most optimized builds that are compatible with every major browser going back a number of years.

Before going over setups, I want to say that xterm
--
