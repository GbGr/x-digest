# X-FEED 2026-09-03 part 4/8 | items: 7

## @mitchellh — 4 шт.

T=2095218879714996629 | @mitchellh | 2026-09-02T18:34+00:00 | L979 RT32 C49 V121999 | thread(2)
URL=https://x.com/mitchellh/status/2095218879714996629
TEXT: The Superlogical server is built to run anywhere and everywhere and serve a level of scale (terminals+clients) unmatched w/ prior solutions. So let's start talking about that, starting with memory usage and comparisons to other popular multiplexers.

I want to start by talking high level: why does terminal/client scale matter? This matters because we're seeing unprecedented terminal usage and client attachment mainly due to AI. They like to spawn more sessions than we've ever seen, and they are all their own clients. So we have to optimize it. Even if you don't use AI/agents, this just makes the software better for humans, too.

Okay, onto the results. First thing to notice is that while tmux's empty states are excellent, Superlogical makes it up at scale and there is an early breakpoint with busy terminals and clients where we use significantly less memory than tmux or anyone else.

Zellij simply does very poorly. There is no other way to put it. Its default out of the box empty footprint is high. And its per-client attachment is simply unscalable. It was clearly meant in its current form for smal single-human low-terminal-count scale. 

The per-client attachment for Zellij was so unbelievable I had to dig into why. Out of the box (zero config) Zellij has a tab bar and status bar plugin. These are wasm-plugins and each tab gets an instantiation. Each instantiation is its own wasm runtime. Huge memory explosion. I also noticed the memory was never reclaimed when I closed the tabs (even when waiting for minutes for memory to settle) but didn't dig into that more.

Anyways, credit where credit is due tmux has excellent memory usage for empty states. The tmux project has always been great and they've been really receptive to the bugs I've found via Ghostty or the protocols we've championed. Much respect. 

I'm going to talk more about how we achieve this in a follow-up video.
[->] @tkukurin @abi7hek In addition to that we do online grid compression with lz4. I’ve also posted about that before. That’s a big part of why our full terminal size is so much smaller even with random data
--
T=2095232081853039041 | @mitchellh | 2026-09-02T19:27+00:00 | L1201 RT43 C29 V46981 | post
URL=https://x.com/mitchellh/status/2095232081853039041
TEXT: A video explaining a handful of the tricks we use to optimize for memory within the Superlogical server: in-memory compression, moving file descriptors between event-driven and blocked threads dynamically, full terminal state binary snapshot/restore in microseconds, and more! https://t.co/gPcjXyxNCu
--
T=2095256578559807810 | @mitchellh | 2026-09-02T21:04+00:00 | L4466 RT376 C85 V134982 | post
URL=https://x.com/mitchellh/status/2095256578559807810
TEXT: Beware people obsessed with outcomes instead of building outcome machines. Its worse than ever with AI, but these people existed before. Short term results above all else, etc. Don't fall into the trap. Invest in building strong fundamentals, invisible supports, and outcomes flow like water. An outcome machine.
--
T=2095357417903345721 | @mitchellh | 2026-09-03T03:45+00:00 | L593 RT9 C31 V55119 | post
URL=https://x.com/mitchellh/status/2095357417903345721
TEXT: Guess which one is Rust btw. 🤣

(The point is the language isn't a free lunch for performance. Rust could be just as small as any other here. It isn't a given. Fundamentals and system design trump everything else. Language wars are stupid as hell.)
QUOTED @mitchellh: The Superlogical server is built to run anywhere and everywhere and serve a level of scale (terminals+clients) unmatched w/ prior solutions. So let's start talking about that, starting with memory usage and comparisons to other popular multiplexers.

I want to start by talking high level: why does terminal/client scale matter? This matters because we're seeing unprecedented terminal usage and client attachment mainly due to AI. They like to spawn more sessions than we've ever seen, and they are 
--
## @mitsuhiko — 3 шт.

T=2095135727910596762 | @mitsuhiko | 2026-09-02T13:04+00:00 | L19 RT6 C0 V5714 | rt
URL=https://x.com/mitsuhiko/status/2095135727910596762
RT-OF @SebastianBaye (L19): I am in London for the next weeks and working on evals for @pidotdev, if you are working on evals or something related, I would be happy to have a chat! Just DM me.
RT-URL=https://x.com/SebastianBaye/status/2094367294163935396
TEXT: RT @SebastianBaye: I am in London for the next weeks and working on evals for @pidotdev, if you are working on evals or something related,…
--
T=2095258262597754978 | @mitsuhiko | 2026-09-02T21:11+00:00 | L494 RT8 C38 V21397 | post
URL=https://x.com/mitsuhiko/status/2095258262597754978
TEXT: This week is full on AI psychosis for me. I think I burned around 1000 USD on one PR that is not going anywhere.
--
T=2095271567492026492 | @mitsuhiko | 2026-09-02T22:04+00:00 | L39 RT1 C8 V6791 | post
URL=https://x.com/mitsuhiko/status/2095271567492026492
TEXT: Not sure who needs to know this but `additional_tools` in openai is not additive with prior message with `additional_tools` but additive to the `tool`s in the system prompt.
--
