# X-FEED 2026-07-30 part 5/9 | items: 8

## @mitchellh — 7 шт.

T=2082489600715661389 | @mitchellh | 2026-07-29T15:33+00:00 | L7832 RT435 C463 V710422 | thread(11)
URL=https://x.com/mitchellh/status/2082489600715661389
TEXT: I've started a new company: @superlogical! We're going to begin by building a terminal multiplexer. The entire vision is much larger, but the multiplexer is the foundation. Sign up for the newsletter to get beta access and devlogs (product updates only I promise).

https://t.co/XJuqufkmCd
[->] @ParkerRex @superlogical Nothing, the problem is how current multiplexers work, not the problem they solve. Our architecture is radically different and gets rid of all their shortcomings plus unlocks some new stuff.
[->] @turanmahmudov @superlogical It’s not. It’ll support agents very well but how you use it is up to you and nothing about it is agent specific.
[->] @PraveenJangid99 @superlogical Its an architectural dead end. It'd be like trying to fashion a contemporary car by strapping a bunch of horses together. You have to rebuild the foundation to move forward, and they're not doing it. (I don't say this without lack of experience)
[->] @lowly_dev @ParkerRex @superlogical Sure, most, and their biggest papercuts. I've read every [open] issue on top of about a decade of mailing list history (when available) on top of building a terminal emulator for the past 5 years. I'll avoid the extremes, let's say "most".
[->] @cptaffe @superlogical Thanks. I come from a very long Go background (which is a modern gateway into plan9 and therefore Acme). I'm aware of it :) and noted.
[->] @rickc42069 @superlogical When we have a formal blog up, we will.
[->] Less AI-focused, less opinionated, more of a platform. We're not trying to compete with people like cmux (@lawrencecchen) or @herdrdev or similar. They're more likely probably partners so their terminals can become remote too. The differences will become very clear over the coming months/year.
[->] @carllerche @Douglance @superlogical Oh man yeah what we’re building I think will really be perfect for what you do. Unify all that to one mux server that owns the ssh, navigate all throigh a single app or browser interface
[->] @yacineMTB @superlogical Hah. We already have a direct integration with tailscale that we probably will ship with. Servers can automatically join a tailscale and expose themselves as services and clients can automatically find them with one config. We’re doing other integrations too. cc @Tailscale btw.
[->] @brnthoney @superlogical https://t.co/60GMNOYiUc
LINKS: https://www.superlogical.com/ ; https://mitchellh.com/writing/superlogical
--
T=2082527120618852480 | @mitchellh | 2026-07-29T18:02+00:00 | L34 RT0 C1 V563 | thread(2)
URL=https://x.com/mitchellh/status/2082527120618852480
TEXT: @Mng64218162 @GergelyOrosz Good news for you, check back in to what we're doing in 6 months. Terminals is just where we start. Its not where we're ultimately going to take you.
[->] @BGokulkumar @GergelyOrosz No, you'll see soon what we're doing is quite a bit different. If you're looking for a clone of something like herdr/cmux you'll be disappointed.
--
T=2082570190970343867 | @mitchellh | 2026-07-29T20:53+00:00 | L147 RT1 C0 V6769 | post
URL=https://x.com/mitchellh/status/2082570190970343867
TEXT: @charliermarsh GLP-1 strikes again
--
T=2082571869623042299 | @mitchellh | 2026-07-29T21:00+00:00 | L4 RT0 C2 V189 | post
URL=https://x.com/mitchellh/status/2082571869623042299
TEXT: @igor_kupczynski @abelanger5 That was the primary motivation. The nerdiness of it was a cool side effect. A large number of applicants so far (in the hundreds now) and we haven't identified one obvious LLM applicant. The filter is working for us.
--
T=2082623830510710865 | @mitchellh | 2026-07-30T00:26+00:00 | L519 RT3 C11 V17102 | thread(4)
URL=https://x.com/mitchellh/status/2082623830510710865
TEXT: @orhundev @ratatui_rs I have nothing bad to say about Ratatui, I’ve heard and seen only good things. But no, no Rust here sorry. The server/networking components are Go, native apps are Swift (Apple), and the low level bits and bobs are Zig with bindings upward.
[->] @AleksYankov @orhundev @ratatui_rs We’re not sure. I’m not an expert at windows dev so we’re gonna let the person coming in voice an opinion. For Linux, likely Zig.
[->] @mariusdotdev @orhundev @ratatui_rs Many people saying that from the sideline (don’t know about you) but I’ve been writing Zig almost exclusively for one of their larger/largest non compiler projects for 3 years and it continues to be excellent. No qualms from me.
[->] No, it really doesn't, and neither does C (which we can trivially consume). Go is the right choice for networked servers. Incredibly rich ecosystem, the runtime is actually helpful there, and the performance is dominated by networking. Where its not, you can use cgo to reach into libs written in Zig.
--
T=2082624677391057211 | @mitchellh | 2026-07-30T00:29+00:00 | L63 RT1 C2 V5736 | post
URL=https://x.com/mitchellh/status/2082624677391057211
TEXT: @minhash @superlogical I talk about this in my personal post: https://t.co/60GMNOYiUc tldr, it’s in a non profit with its own governance and remains independent
LINKS: https://mitchellh.com/writing/superlogical
--
T=2082664114720313520 | @mitchellh | 2026-07-30T03:06+00:00 | L1 RT0 C0 V77 | post
URL=https://x.com/mitchellh/status/2082664114720313520
TEXT: @iridescence_dev @superlogical Oh thanks! Yeah not a big deal they're out there but patched them out anyways (they're in the build still but 404 on the route, not a problem they're in the build. we'll do a better job another day)
--
## @mitsuhiko — 1 шт.

T=2082408728041521283 | @mitsuhiko | 2026-07-29T10:11+00:00 | L586 RT47 C27 V53485 | rt
URL=https://x.com/mitsuhiko/status/2082408728041521283
RT-OF @louszbd (L586): We added a setup guide for using GLM in Pi. GLM Coding Plan is supported. https://t.co/ttdK63yKhK
RT-URL=https://x.com/louszbd/status/2082397274592965025
TEXT: RT @louszbd: We added a setup guide for using GLM in Pi. GLM Coding Plan is supported. https://t.co/ttdK63yKhK
LINKS: https://docs.z.ai/devpack/tool/pi
--
