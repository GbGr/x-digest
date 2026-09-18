# X-FEED 2026-09-18 part 1/9 | items: 10

## @_philschmid — 5 шт.

T=2100573241865597384 | @_philschmid | 2026-09-17T13:11+00:00 | L5 RT0 C0 V868 | post
URL=https://x.com/_philschmid/status/2100573241865597384
TEXT: @mitsuhiko Sorry it took so long but we added hookable fetch in version 2.3.0. 
https://t.co/zZp4mEx6jJ
LINKS: https://github.com/googleapis/js-genai/commit/01897b33eecdbcefbe8e4f83eb336735a2a464b6
--
T=2100635161788305801 | @_philschmid | 2026-09-17T17:17+00:00 | L279 RT19 C15 V45563 | thread(4)
URL=https://x.com/_philschmid/status/2100635161788305801
TEXT: New Files API to move data in and out of your agent environment:

- Seed files inline or upload data mid-conversation with `files.upload()`.

- Inspect generated files and directory sizes with `files.list()`.

- Download artifacts, dashboards, reports, CSVs, or git repos with `files download()`.

- Sandboxes persist across turns via `environment_id`

Docs: https://t.co/QXbYQXuTA3
[->] New Credentials API to securely authenticate with external services and MCP servers without the model ever seeing your secrets:

- Register secrets once with `credentials.create()` supporting `bearer_token`, `environment_variable`, or `oauth2` (with auto-refresh and token rotation). 

- Zero plaintext exposure: Secrets never enter model context, stdout, memory.

- The agent only sees a placeholder (e.g., `__GEMINI_CRED_slack-bot-token__`).

- Egress proxy swaps real token on the request only for allowlisted `trusted_domains` (any exfiltration attempt to another host gets a `403`).

- Bind credentials directly to remote `mcp_server` tools or sandbox env vars.

Docs: https://t.co/IGM9tLaISp
[->] `antigravity-preview-09-2026` upgrades our managed agent runtime:

- Runs on Gemini 3.8 Flash by default, or configure default model.

- Persistent Linux sandbox with bash execution, file tools (`view_file`, `write_to_file`, `replace_file_content`), Google Search, and URL context.

- 30% cost reduction on multi-turn coding and 17% on reasoning thanks to higher cache hit rates.

- 40% fewer tokens on file edits and up to 8% higher task completion on SWE and research evals.

- Automatic context compaction at ~135k tokens.

- Save reusable agent configs once with `agents.create()` and call them by id.

Docs: https://t.co/wzhGXXClm8
[->] Today we are releasing a new Gemini managed agents version with better caching, lower costs, a Files API, and a Credentials API.

📉 Up to 30% lower costs with up to 22% higher cache hits
📁 Files API: Upload, list and download files from sandbox easily
🔐 Credentials API for MCP servers, OAuth2, and 3rd-party APIs as secure egress proxy
🆓 Free tier to experiment in @GoogleAIStudio & Gemini API

Start Here: https://t.co/BVw7K5IwH3
LINKS: https://ai.google.dev/gemini-api/docs/agent-environment#download-files ; https://ai.google.dev/gemini-api/docs/agent-credentials ; https://ai.google.dev/gemini-api/docs/antigravity-agent ; https://aistudio.google.com/learn/managed-agents-updated-harness-files-credentials?e=0
--
T=2100636812079141284 | @_philschmid | 2026-09-17T17:23+00:00 | L2 RT0 C1 V876 | post
URL=https://x.com/_philschmid/status/2100636812079141284
TEXT: @chetaslua We are out https://t.co/rKMFqEmGXC
QUOTED @_philschmid: Today we are releasing a new Gemini managed agents version with better caching, lower costs, a Files API, and a Credentials API.

📉 Up to 30% lower costs with up to 22% higher cache hits
📁 Files API: Upload, list and download files from sandbox easily
🔐 Credentials API for MCP servers, OAuth2, and 3rd-party APIs as secure egress proxy
🆓 Free tier to experiment in @GoogleAIStudio & Gemini API

Start Here: https://t.co/BVw7K5IwH3
LINKS: https://x.com/_philschmid/status/2100635151080550793?s=20
--
T=2100636741161845244 | @_philschmid | 2026-09-17T17:23+00:00 | L2 RT0 C1 V648 | post
URL=https://x.com/_philschmid/status/2100636741161845244
TEXT: @dedene We are out https://t.co/rKMFqEmGXC
QUOTED @_philschmid: Today we are releasing a new Gemini managed agents version with better caching, lower costs, a Files API, and a Credentials API.

📉 Up to 30% lower costs with up to 22% higher cache hits
📁 Files API: Upload, list and download files from sandbox easily
🔐 Credentials API for MCP servers, OAuth2, and 3rd-party APIs as secure egress proxy
🆓 Free tier to experiment in @GoogleAIStudio & Gemini API

Start Here: https://t.co/BVw7K5IwH3
LINKS: https://x.com/_philschmid/status/2100635151080550793?s=20
--
T=2100664321646690491 | @_philschmid | 2026-09-17T19:12+00:00 | L46 RT4 C6 V5123 | thread(2)
URL=https://x.com/_philschmid/status/2100664321646690491
TEXT: Excited to share that we partnered with @speakeasydev  to build the sdks for the Interactions API and supported them to open-source their their entire OpenAPI generator suite (SDKs, agent CLIs, and MCP servers) open source for the community to use: https://t.co/vkVz5pYMHP
[->] @speakeasydev https://t.co/Wj57hGV4Ux https://t.co/8i9xsbghm0
LINKS: https://developers.googleblog.com/why-client-sdk-generation-belongs-in-the-open/ ; https://github.com/speakeasy-api/openapi-generation
--
## @addyosmani — 1 шт.

T=2100634616147464492 | @addyosmani | 2026-09-17T17:14+00:00 | L242 RT17 C31 V41645 | post
URL=https://x.com/addyosmani/status/2100634616147464492
TEXT: Projects are rolling out in Claude Code today. 

A Project is an ongoing conversation that coordinates a stream of related work for you. You describe a goal, Claude splits it into threads, runs them in parallel in the cloud and keeps going after you close your laptop. 

Starting with select Pro and Max users on cloud sessions.
QUOTED @ClaudeDevs: Today we're rolling out Projects in Claude Code on desktop and web.

A project is one conversation with Claude. It splits the work into threads itself, runs them as parallel cloud sessions, passes context between them, and keeps going when you leave.

In beta for select users. https://t.co/j4k7rludhV
--
## @bcherny — 2 шт.

T=2100639991244427490 | @bcherny | 2026-09-17T17:36+00:00 | L1993 RT54 C140 V319366 | post
URL=https://x.com/bcherny/status/2100639991244427490
TEXT: Projects are how I write a lot of my code these days. Really excited for everyone to try the new experience! Rolling out now
QUOTED @claudeai: Projects now run from one conversation, starting in Claude Code. You describe what needs doing, and Claude directs parallel threads that keep working after you close your laptop.

In beta today for select Pro and Max users in cloud sessions; coming to all Claude users soon. https://t.co/GYzoKbxS23
--
T=2100669598995816511 | @bcherny | 2026-09-17T19:33+00:00 | L2450 RT87 C220 V382806 | post
URL=https://x.com/bcherny/status/2100669598995816511
TEXT: Projects have changed not only how I interact with Claude but how I code.

I stopped managing sessions. I just send thoughts as they come, Claude splits them into threads, and the project remembers how I work. It's where I do a ton of my coding now.

[screenshot: my actual prompts for claude code cli yesterday]
QUOTED @ClaudeDevs: Today we're rolling out Projects in Claude Code on desktop and web.

A project is one conversation with Claude. It splits the work into threads itself, runs them as parallel cloud sessions, passes context between them, and keeps going when you leave.

In beta for select users. https://t.co/j4k7rludhV
--
## @cwolferesearch — 2 шт.

T=2100632127612109162 | @cwolferesearch | 2026-09-17T17:05+00:00 | L1 RT0 C0 V126 | post
URL=https://x.com/cwolferesearch/status/2100632127612109162
TEXT: @code_star @arcee_ai congrats! super excited to learn more about everything the team is doing soon
--
T=2100667677777842503 | @cwolferesearch | 2026-09-17T19:26+00:00 | L1 RT0 C0 V351 | post
URL=https://x.com/cwolferesearch/status/2100667677777842503
TEXT: @askalphaxiv congrats! love this feature and has been super cool to see it evolve
--
