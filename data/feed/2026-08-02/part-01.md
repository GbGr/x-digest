# X-FEED 2026-08-02 part 1/7 | items: 4

## @cwolferesearch — 1 шт.

T=2083588813675274301 | @cwolferesearch | 2026-08-01T16:20+00:00 | L199 RT31 C6 V14115 | post
URL=https://x.com/cwolferesearch/status/2083588813675274301
TEXT: Why is evaluating agents so difficult relative to evaluating a standard LLM?

An LLM generates a single response to a prompt. An agent instead interacts with an environment by reasoning, calling tools, observing the results, and repeating. Rather than evaluating a single output, we are evaluating a full trajectory for a long horizon problem.

Outcome & environment. Success is usually determined by the final outcome. Instead of checking the agent’s output, however, we usually check the actual state of the environment after a trajectory completes. For example:
- A coding agent can say it fixed a bug but still fail test cases.
- A personal assistant could say “your flight has been booked!”, but we don’t know if this is true until we check the booking database.

The environment plays a huge role in the evaluation process. For example, we need a stable environment that does not change over time in order to run reliable evals, and we need this environment to be efficient so that evals can be run efficiently. Additionally, the environment must be realistic and expose the proper harness / tools for the agent to be effective.

Environment state. The final answer is only one part of the evaluation. We also need to understand how the agent reached that answer. Did the agent use the correct tools? Did it interact efficiently with the environment? We can validate certain tool calls, check for intermediate solutions in the trajectory, and look at how many turns / tokens were used.

Verifying intermediate trajectory states is common in agentic evaluation. If the agent solves a task, then this provides a valuable signal. But, what do we do if the agent solves a small ratio of tasks in a benchmark? In this case, we need to have a more granular measure of performance that allows us to understand how close the agent came to solving certain problems.

Agent evals are expensive. Unlike traditional LLM benchmarks, agent evaluations can span long time horizons with many reasoning steps, tool calls, and environment interactions. A single evaluation may require vast amounts of generated tokens and dozens or hundreds of interaction turns with the environment. For this reason, agent evaluations are much more difficult to both curate and run! This data is super complex and even solving a single task can be expensive.

Less data, more noise. Because each evaluation is costly, we typically run far fewer examples than in traditional LLM benchmarks. This is both because each task can take a long time to run and because curating the data / setup for each task is expensive. Rather than evaluating single dataset examples, we are asking the agent to solve a real problem. As a result, we usually have smaller evaluation dataset with higher variance, making reliable measurement difficult.
--
## @dexhorthy — 3 шт.

T=2083582284658245837 | @dexhorthy | 2026-08-01T15:55+00:00 | L206 RT6 C29 V22939 | thread(2)
URL=https://x.com/dexhorthy/status/2083582284658245837
TEXT: My AI coding journey so far

Copy paste ChatGPT to jetbrains

Cursor autocomplete 

Codebuff CLI + jetbrains for reading + cursor for polish

Claude code in terminal + jetbrains for debugging

4 Claude’s in tmux worktrees with a 5th merging every commit into main

Claude code - Research with subagents, then impl

Claude code - research, plan, impl

CodeLayer (cc) RPI

Humanlayer (cc) QRSPI

+ nightly gh actions loops to do small incremental changes across migrations and cleanups

Took the codex pill, 5.5 for all coding

Fables managing codex subagents and 5.6s managing fables 

Still read the code, still learning
[->] oh and somewhere in there, several flavors of lights-off factory with linear state machine
QUOTED @GregKamradt: My AI coding journey so far:

* Copy paste between ChatGPT &amp; vscode
* Cursor autocomplete
* Cursor sidebar
* Claude code in cursor's terminal
* Claude code/Codex in terminal, but no ide
* Amp w/ 5 terminals at once
* Codex Desktop App
* Codex Desktop App + mobile
--
T=2083642061946011753 | @dexhorthy | 2026-08-01T19:52+00:00 | L56 RT1 C8 V6413 | post
URL=https://x.com/dexhorthy/status/2083642061946011753
TEXT: oh wow...fun SlopCodeBench results coming today for new frontier models Kimi K3, GPT-5.6-Sol, and Fable 5
--
T=2083647568979050937 | @dexhorthy | 2026-08-01T20:14+00:00 | L35 RT0 C7 V4796 | post
URL=https://x.com/dexhorthy/status/2083647568979050937
TEXT: oh wow we went a little deeper on SlopCodeBench and the frontier is better but not by much...stay tuned for the full post https://t.co/a2ZFt2igBu
--
