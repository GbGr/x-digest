# X-FEED 2026-09-12 part 1/9 | items: 8

## @_philschmid — 2 шт.

T=2098413825435312299 | @_philschmid | 2026-09-11T14:10+00:00 | L126 RT12 C14 V8193 | post
URL=https://x.com/_philschmid/status/2098413825435312299
TEXT: Telling agents "don't cheat" in the prompt doesn't work if your eval is broken! Researchers at @GoogleDeepMind put 100 Gemini agents in a shared repo to solve 71 math theorems.

After an hour of doing real math, 1 agent found a loophole in the autograder. Within 27 minutes, the 100 agents split into 4 groups:

- 9% Cheaters: used the bug to fake proofs and steal every open problem
- 5% Good agents turned bad: started honest, saw cheaters winning with zero punishment ("the prompt is a bluff"), and started cheating too
- 24% Whistleblowers: caught the fake proofs in the shared repo, warned other agents, went on strike, and wrote bug fixes
- 62% Clueless solvers: kept doing real math until all the problems were gone

tl;dr: Telling agents "don't cheat" in the prompt doesn't work if your eval has a bug, and good agents can't stop bad ones without tools to block them.

Paper: https://t.co/qyFDGw0Fjh
LINKS: https://arxiv.org/abs/2609.04170
--
T=2098426046622118056 | @_philschmid | 2026-09-11T14:58+00:00 | L44 RT0 C9 V3590 | post
URL=https://x.com/_philschmid/status/2098426046622118056
TEXT: &gt; Build me a Rollercoaster Tycoon clone for the browser.

We are so EARLY. https://t.co/EBFbmBY2Kt
--
## @addyosmani — 4 шт.

T=2098297991019057363 | @addyosmani | 2026-09-11T06:30+00:00 | L702 RT63 C53 V38704 | post
URL=https://x.com/addyosmani/status/2098297991019057363
TEXT: Tip: Claude Code has several skill-cleanup commands.
Each answers a different question.  

/skill-doctor → which skills you use 
/skills, then t → what each costs 
/doctor → fixes setup + CLAUDE.md debt
/context → what's in the window now 
/usage → what burns your limits https://t.co/EdyrPoaNiq
--
T=2098662421644853433 | @addyosmani | 2026-09-12T06:38+00:00 | L43 RT2 C17 V8210 | post
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
T=2098677768280330403 | @addyosmani | 2026-09-12T07:39+00:00 | L599 RT30 C89 V37130 | rt
URL=https://x.com/addyosmani/status/2098677768280330403
RT-OF @lydiahallie (L599): new toggle in Claude Code desktop 👀 you can now keep your computer awake for a single session, including waits between turns! https://t.co/ffG6tdw68f
RT-URL=https://x.com/lydiahallie/status/2098455697004613814
TEXT: RT @lydiahallie: new toggle in Claude Code desktop 👀 you can now keep your computer awake for a single session, including waits between tur…
--
T=2098678724707467548 | @addyosmani | 2026-09-12T07:42+00:00 | L900 RT68 C75 V124471 | rt
URL=https://x.com/addyosmani/status/2098678724707467548
RT-OF @addyosmani (L900): How I do code reviews these days: more code = more selective human review i.e. don't read all the code.

1. Every PR gets a multi-agent first pass. It should find bugs, verify them, rank by severity, suggest fixes. Approval stays a human call on anything that matters.

2. Low blast radius changes on less sensitive code (there's often a lot!) can skip a deep human review once that review is clean. This helps keep the explosion of PRs manageable.

3. Core / sensitive paths still need an owner and human sign-off. That's where you spend time: verification, constraints and earning trust in what the agents can safely cover. You want to keep recoverability.

Agents do the first pass and humans cover blast radius.

Great question from @GergelyOrosz!
RT-URL=https://x.com/addyosmani/status/2097027173941141799
TEXT: RT @addyosmani: How I do code reviews these days: more code = more selective human review i.e. don't read all the code.

1. Every PR gets a…
--
## @bcherny — 2 шт.

T=2098670885150605529 | @bcherny | 2026-09-12T07:11+00:00 | L1284 RT69 C75 V131183 | rt
URL=https://x.com/bcherny/status/2098670885150605529
RT-OF @ClaudeDevs (L1284): Here's how our team uses Claude Tag for on-call:

When an alert fires in Slack, Claude pulls metrics, diffs deploys, and checks flags. It finds a likely cause and proposes a fix, which we can approve and merge. Every minute counts, so we love that it starts right away! https://t.co/15gdEHjI7d
RT-URL=https://x.com/ClaudeDevs/status/2098508880921899197
TEXT: RT @ClaudeDevs: Here's how our team uses Claude Tag for on-call:

When an alert fires in Slack, Claude pulls metrics, diffs deploys, and ch…
--
T=2098670782184612051 | @bcherny | 2026-09-12T07:11+00:00 | L4701 RT302 C123 V512671 | rt
URL=https://x.com/bcherny/status/2098670782184612051
RT-OF @ClaudeDevs (L4701): New in Claude Code: claude plugin eval

See what value your plugin is adding, or if it needs more work.

You can create test cases, run your plugin or skill against those test cases, score those runs, then run each case again without the plugin to see the differences. https://t.co/qfPU6WHueV
RT-URL=https://x.com/ClaudeDevs/status/2098500999656923145
TEXT: RT @ClaudeDevs: New in Claude Code: claude plugin eval

See what value your plugin is adding, or if it needs more work.

You can create tes…
--
