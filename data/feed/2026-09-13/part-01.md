# X-FEED 2026-09-13 part 1/8 | items: 7

## @_philschmid — 1 шт.

T=2098777533386756432 | @_philschmid | 2026-09-12T14:15+00:00 | L136 RT4 C10 V10468 | post
URL=https://x.com/_philschmid/status/2098777533386756432
TEXT: This as a "thinking" animation? https://t.co/6GpPgG3QIy https://t.co/l2fLYplbcz
LINKS: https://www.shadercn.run/playground?orb=orb-21&state=thinking
--
## @addyosmani — 4 шт.

T=2098662421644853433 | @addyosmani | 2026-09-12T06:38+00:00 | L293 RT19 C49 V48421 | post
URL=https://x.com/addyosmani/status/2098662421644853433
TEXT: How do you hold the bar on production agent code?:

1. Agree on the outcome and the constraints first. 

What does "done" look like? what must it not touch? is the simpler design is to refactor or reuse what you already have? Then let Claude cook. You do not need a long planning ritual on the latest models. You do need to reject a bad change before it becomes a PR.

2. Give Claude a way to check its work. 

Put the exact build, test, and lint commands in there. Turn the things you reject in review into skills: /verify, e2e, schema checks and so on. Run those before you open the PR. Use /code-review. I've said that quality now lives in the constraints you put around your agents and think this is worth spending time on.

3. Your job is the design and the bar. 

Blast radius decides how much you read. Throwaway code with a small blast radius can be a black box. Production code should have a higher bar than if a human wrote it, especially anything that touches money, auth, or user data.

4. When Claude misses, don’t quietly fix it by hand. Have it write the lesson into CLAUDE.md or a skill. 

If it still misses, use the latest frontier model, turn effort to higher or have Claude pay down the debt and make the codebase easier to work in.

You can start with one check you already run today on every PR. The rest compounds from there.
QUOTED @bcherny: Hey ████,

I think there is room for both.

1. Prototypes and other throw-away code can be treated as totally black box. If you’re going to throw it away anyway, and if the blast radius of it breaking is low, it doesn’t need to be perfect.
2. Production code written by Claude should have a higher bar than if it was written by a human. At Anthropic, we have many guardrails in place to make sure this is happening: lots of lint rules, lots of tests, Claude-driven end to end tests, Claude-powered fu
--
T=2098677768280330403 | @addyosmani | 2026-09-12T07:39+00:00 | L682 RT36 C103 V47678 | rt
URL=https://x.com/addyosmani/status/2098677768280330403
RT-OF @lydiahallie (L682): new toggle in Claude Code desktop 👀 you can now keep your computer awake for a single session, including waits between turns! https://t.co/ffG6tdw68f
RT-URL=https://x.com/lydiahallie/status/2098455697004613814
TEXT: RT @lydiahallie: new toggle in Claude Code desktop 👀 you can now keep your computer awake for a single session, including waits between tur…
--
T=2098678724707467548 | @addyosmani | 2026-09-12T07:42+00:00 | L1001 RT79 C78 V144392 | rt
URL=https://x.com/addyosmani/status/2098678724707467548
RT-OF @addyosmani (L1001): How I do code reviews these days: more code = more selective human review i.e. don't read all the code.

1. Every PR gets a multi-agent first pass. It should find bugs, verify them, rank by severity, suggest fixes. Approval stays a human call on anything that matters.

2. Low blast radius changes on less sensitive code (there's often a lot!) can skip a deep human review once that review is clean. This helps keep the explosion of PRs manageable.

3. Core / sensitive paths still need an owner and human sign-off. That's where you spend time: verification, constraints and earning trust in what the agents can safely cover. You want to keep recoverability.

Agents do the first pass and humans cover blast radius.

Great question from @GergelyOrosz!
RT-URL=https://x.com/addyosmani/status/2097027173941141799
TEXT: RT @addyosmani: How I do code reviews these days: more code = more selective human review i.e. don't read all the code.

1. Every PR gets a…
--
T=2099034401208184944 | @addyosmani | 2026-09-13T07:16+00:00 | L2102 RT124 C78 V278028 | rt
URL=https://x.com/addyosmani/status/2099034401208184944
RT-OF @trq212 (L2102): we heard feedback that it's hard to know if your skills are still working with new model releases

plugin evals are here to help

run `claude plugin eval init` in your plugin folder
RT-URL=https://x.com/trq212/status/2098531560643539440
TEXT: RT @trq212: we heard feedback that it's hard to know if your skills are still working with new model releases

plugin evals are here to hel…
--
## @bcherny — 2 шт.

T=2098670885150605529 | @bcherny | 2026-09-12T07:11+00:00 | L1881 RT109 C105 V225194 | rt
URL=https://x.com/bcherny/status/2098670885150605529
RT-OF @ClaudeDevs (L1881): Here's how our team uses Claude Tag for on-call:

When an alert fires in Slack, Claude pulls metrics, diffs deploys, and checks flags. It finds a likely cause and proposes a fix, which we can approve and merge. Every minute counts, so we love that it starts right away! https://t.co/15gdEHjI7d
RT-URL=https://x.com/ClaudeDevs/status/2098508880921899197
TEXT: RT @ClaudeDevs: Here's how our team uses Claude Tag for on-call:

When an alert fires in Slack, Claude pulls metrics, diffs deploys, and ch…
--
T=2098670782184612051 | @bcherny | 2026-09-12T07:11+00:00 | L5828 RT401 C172 V811698 | rt
URL=https://x.com/bcherny/status/2098670782184612051
RT-OF @ClaudeDevs (L5828): New in Claude Code: claude plugin eval

See what value your plugin is adding, or if it needs more work.

You can create test cases, run your plugin or skill against those test cases, score those runs, then run each case again without the plugin to see the differences. https://t.co/qfPU6WHueV
RT-URL=https://x.com/ClaudeDevs/status/2098500999656923145
TEXT: RT @ClaudeDevs: New in Claude Code: claude plugin eval

See what value your plugin is adding, or if it needs more work.

You can create tes…
--
