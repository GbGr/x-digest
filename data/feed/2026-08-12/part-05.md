# X-FEED 2026-08-12 part 5/8 | items: 6

## @omarsar0 — 6 шт.

T=2087183764057460972 | @omarsar0 | 2026-08-11T14:26+00:00 | L28 RT7 C6 V8433 | post
URL=https://x.com/omarsar0/status/2087183764057460972
TEXT: Qodo just launched the AI Code Review Academy.

It’s a free set of chapters from @QodoAI on code review in the era of AI-generated code.

No sign-up required.

I went through the benchmarks and tool comparison chapter. I would recommend it to anyone evaluating review tools right now.

It gives you a way to judge whether a benchmark means anything before you act on it.

- The dataset has to be real production PRs.
- Every tool has to run at default settings; otherwise you are measuring tuning effort.
- The methodology has to be open enough to rerun yourself.
- And precision and recall have to be reported together, so you know how much a tool catches and how much of what it flags is real.

The number that stuck with me came from a 2025 study cited in the chapter. Same model, two evaluations. It scored 84-89% on an isolated benchmark and 25-34% inside a real codebase with dependencies and conventions.

The chapter's best advice is to run every tool you are considering against the same 10-20 pull requests from your own codebase.

Academy: https://t.co/s1wipsItkS

Thanks, Qodo, for partnering on this post.
LINKS: https://www.qodo.ai/academy/?utm_source=x&utm_medium=partner&utm_campaign=academy-launch-2026&utm_content=omarsar0
--
T=2087187835530948776 | @omarsar0 | 2026-08-11T14:42+00:00 | L61 RT6 C8 V10728 | post
URL=https://x.com/omarsar0/status/2087187835530948776
TEXT: Recommended reading. 

"This suggests that distilling reasoning traces may have been possible for a long time without ever breaking the cryptography."
QUOTED @kotekjedi_ml: We can finally talk about it:

We found a way to extract hidden reasoning of frontier models using a vulnerability in the APIs of every frontier AI company.

We verified that our reasoning token count matches billed API thinking tokens 1:1 for most of the prompts we queried. https://t.co/S7wN8aP3X7
--
T=2087191397111656738 | @omarsar0 | 2026-08-11T14:56+00:00 | L41 RT10 C13 V8326 | post
URL=https://x.com/omarsar0/status/2087191397111656738
TEXT: This is kind of wild.

BDH-CQ scored 29.5% on ARC-AGI 1. Fair. But with just $.0007 per task. 

How it’s done is particularly interesting. It reasons recurrently in latent space rather than using CoT. They’ve also verified Transformer-like scaling up to 600B params.
QUOTED @zuzanna_pathway: Pathway’s BDH-CQ model redefines the Cost-Efficiency Frontier on ARC-AGI-1: $.0007 at 29.5%. This is made possible by in-context learning and latent reasoning. Welcome to the Post-Transformer Era. https://t.co/raSTkwgNQ5
--
T=2087255292954243553 | @omarsar0 | 2026-08-11T19:10+00:00 | L15 RT1 C5 V6192 | post
URL=https://x.com/omarsar0/status/2087255292954243553
TEXT: Own your intelligence.

How? Start by building specialized models using agents.

@oumi_ai does this well. It creates the data, the recipes, and the model weights, and even writes LLM-as-a-judge evaluators. It deploys for you too. https://t.co/YM12Oinryu
QUOTED @Koukoumidis: Enterprise AI is in a wildly paradoxical state 🤔, and we’re reaching the inflection point that will resolve it. 💥

Enterprises want to differentiate with AI, yet rent the same intelligence as their competitors.

Their workflows and expertise are highly specialized, yet they rely on generic models built to be good at everything.

They worry about AI costs, yet pay premium prices for massive models where only a fraction (1%) of the intelligence is relevant to their task. 💸

And they demand control
--
T=2087264593982746735 | @omarsar0 | 2026-08-11T19:47+00:00 | L85 RT19 C7 V8024 | rt
URL=https://x.com/omarsar0/status/2087264593982746735
RT-OF @dair_ai (L85): Impressive new paper from Microsoft.

(bookmark it)

Reasoning modes beat non-reasoning modes on multi-step agentic tasks, and they charge a 3 to 6x premium in output tokens on every single episode. Much of that spend goes into re-deriving procedures the model already worked out on earlier episodes in the same domain.

This work amortizes that cost.

A coding agent reads a small corpus of existing trajectories from a training split, compiles a compact natural-language skill, and injects it into the non-reasoning model's system prompt.

Across ALFWorld, tau-squared-bench telecom and retail, and SpreadsheetBench-Verified, skills recover 55% to over 100% of the reasoning gap for GPT-5.4-mini on held-out tasks. On two of the four benchmarks the skill-equipped non-reasoning model beats reasoning mode outright, while emitting 2.7 to 6x fewer output tokens and zero reasoning tokens.

Reasoning traces turn out to be optional. Skills distilled from non-reasoning trajectories alone stay competitive with skills distilled from paired corpora.

Paper: https://t.co/LwBBH5e7qw

Track more trending AI papers in our academy: https://t.co/LRnpZN7L4c
RT-URL=https://x.com/dair_ai/status/2087264294782279808
TEXT: RT @dair_ai: Impressive new paper from Microsoft.

(bookmark it)

Reasoning modes beat non-reasoning modes on multi-step agentic tasks, and…
LINKS: https://arxiv.org/abs/2608.07885 ; https://academy.dair.ai/
--
T=2087290593651093775 | @omarsar0 | 2026-08-11T21:30+00:00 | L431 RT66 C17 V30692 | rt
URL=https://x.com/omarsar0/status/2087290593651093775
RT-OF @omarsar0 (L431): Impressive new paper from Meta.

(bookmark it)

Scaling laws assume model size and training data act on loss independently.

This work introduces Skaling law, which couples capacity and data through a single interaction exponent. The extra term cuts mean absolute percentage error by 1.5x to 3x across both interpolation and extrapolation.

The largest corrections land in the data-scarce and heavy-overtraining regimes where the standard Chinchilla and Kaplan forms drift.

Paired with a sparse grid restricted to low-compute runs, it extrapolates the full grid using roughly 10x less compute than a uniform sweep.

Why does it matter?

Deployment now happens well past compute optimal. A law that stays accurate there, and that can be fit from small runs, changes how a pretraining budget gets planned.

Paper: https://t.co/IoD2ityxIl

Track more trending AI papers in our academy: https://t.co/1e8RZKs4uX
RT-URL=https://x.com/omarsar0/status/2086845790983716917
TEXT: RT @omarsar0: Impressive new paper from Meta.

(bookmark it)

Scaling laws assume model size and training data act on loss independently.…
LINKS: https://arxiv.org/abs/2608.07222 ; https://academy.dair.ai/
--
