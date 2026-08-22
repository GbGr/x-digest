# X-FEED 2026-08-22 part 5/8 | items: 7

## @mitchellh — 3 шт.

T=2090871481412866343 | @mitchellh | 2026-08-21T18:39+00:00 | L22 RT0 C2 V2628 | post
URL=https://x.com/mitchellh/status/2090871481412866343
TEXT: @rockorager @Scanline00 @dhh This extends outside of tech too! My wife told me like our 2nd date and continues to tell me and others to this day how striking it is how little I care about what others think about me. Not in a how I dress or talk or whatever way, but in the sense that when I have some conviction about what I want to do, no one is swaying me from that lol (I may fail at it, but I'm going to try).
--
T=2090875695346139621 | @mitchellh | 2026-08-21T18:56+00:00 | L2384 RT89 C61 V108713 | post
URL=https://x.com/mitchellh/status/2090875695346139621
TEXT: Ghostty (and libghostty!) now has a 100% complete implementation of the Kitty Graphics Protocol. We support every feature, every option. We are the first terminal beyond Kitty to do this. 

Most terminals stop at basic image placements, then give up on the long tail of other features. Ghostty covers all of them:

- Unicode placeholders (so it works in tmux)
- Relative placements (so images can be positioned relative to other images)
- Animation 
- Scroll region handling (so images scroll properly with terminal scroll regions)
- All transport mediums: shared memory, temp files, etc.
- etc...

All of these features don't impact steady-state use (CPU or memory, besides raw code size). And for libghostty consumers, you can use the compile-time features flags to disable them completely.

I read the spec myself a hundred times. I read Kitty's source code to validate behaviors (our implementation is markedly different, so no GPL violation). 

I also utilized agents, primarily for validation. I spun Fable and Sol in a loop for 3 weeks (pausing only when their dedicated subs exhausted limits) with a prompt to find mismatches between the spec, Kitty's reference implementation, and Ghostty.

And now we're done. Ghostty is the most compliant Kitty Graphics implementation (ignoring Kitty itself of course). And, this is all in libghostty, so now everyone can be perfectly compliant.
--
T=2090893729469268109 | @mitchellh | 2026-08-21T20:08+00:00 | L438 RT5 C23 V37734 | post
URL=https://x.com/mitchellh/status/2090893729469268109
TEXT: Part of the LLM-assisted work here is that Fable+Sol put together a test suite of over 400 cases that are bare shell scripts plus a harness that runs Kitty and Ghostty GUIs and captures their full pty stream AND screenshots (multiple, for animations).  

For the pty stream we assert byte equality. So Ghostty's success and error messages and field order of responses (its k=v) directly matches Kitty byte for byte.  

For screenshots, we can't do pixel-identical comparisons because the way Kitty and Ghostty calculate grids and do alpha blending doesn't match. But, LLMs are pretty good now at "do they look the same" PLUS I went through all the screenshots myself in the end.   

Super helpful AI assist. It allowed me to focus a lot of my brain energy and time on reading the spec, reading/writing the implementation, reviewing a lot of code, considering the right shape of things, the performance implications, etc. while I had a couple very good interns in the background doing work like this.

I plan on open sourcing this validation set and harness, with the full disclaimer that it is 100% AI written. But, I think its a perfect example of something that SHOULD be.

The way I had Fable+Sol work together here:

  1. Sol put together the harness.
  2. Fable + Sol (two separate agents) in parallel would write test cases and output them on disk in their own folders. These two are just in a ralph loop.
  3. Sol + Fable (reversed) with an adversarial prompt would judge the others work by picking up the changes on disk that step 2 wrote. They would determine how accurate/worthwhile it is to keep. They'd put it in another folder.
  4. Sol finally woke up for changes to this final folder and would determine if its a dup or not and then add it to the final repo.

Then I'd pick up the bug reports, validate them myself, and either fix them myself or kick off new agents manually, just Codex app or Claude app.

Finally, re-ran both agents once against the full test suite to verify what I saw myself: everything passed, all images look the same.
QUOTED @mitchellh: Ghostty (and libghostty!) now has a 100% complete implementation of the Kitty Graphics Protocol. We support every feature, every option. We are the first terminal beyond Kitty to do this. 

Most terminals stop at basic image placements, then give up on the long tail of other features. Ghostty covers all of them:

- Unicode placeholders (so it works in tmux)
- Relative placements (so images can be positioned relative to other images)
- Animation 
- Scroll region handling (so images scroll properl
--
## @mitsuhiko — 3 шт.

T=2090767748041232809 | @mitsuhiko | 2026-08-21T11:47+00:00 | L23 RT3 C0 V4767 | post
URL=https://x.com/mitsuhiko/status/2090767748041232809
TEXT: Deref continues to be a hilarious hack to get specializations in Rust within macro contexts https://t.co/kn58m38Pof
LINKS: https://gist.github.com/mitsuhiko/41251bf17b0903c6433fd61d528e024d
--
T=2090862681427226820 | @mitsuhiko | 2026-08-21T18:04+00:00 | L341 RT2 C19 V11305 | post
URL=https://x.com/mitsuhiko/status/2090862681427226820
TEXT: My kids found my old GameCube and now they’re playing Ocarina of Time. https://t.co/vkO4eo0V80
--
T=2090921151685955630 | @mitsuhiko | 2026-08-21T21:57+00:00 | L52 RT2 C2 V4702 | post
URL=https://x.com/mitsuhiko/status/2090921151685955630
TEXT: Hey agent, can we make our OpenAPI spec be agent discoverable? Like, return the right API specs when the agent writes a summary of the task?

Five minutes later the agent wires up an embedding model on Cloudflare. I'm kinda impressed by both Cloudflare and the agent capabilities here really.
--
## @natolambert — 1 шт.

T=2090932648021500320 | @natolambert | 2026-08-21T22:42+00:00 | L110 RT2 C2 V11743 | post
URL=https://x.com/natolambert/status/2090932648021500320
TEXT: So happy for the whole Marin team. They've been quietly working up to this for a long time. I'm excited to get to work with the community post-training this model!
QUOTED @percyliang: 🚢 Marin 535B-A23B started training this week! As usual, the whole process is open.
Voyage plan: pretraining (80%) + midtraining (20%) on 18.75T tokens on 11 x GB200 NVL72 for ~3 months (2.7e24 FLOPs).  Post-training will follow.
Before kicking off the run, we trained a 4-rung scaling ladder from 1.6B-A61M (48B tokens) to 27.7B-A1.2B (926B tokens) to debug issues, and to make a forecast of our hero run.  This is by far our biggest run, so definitely expecting the unexpected.
--
