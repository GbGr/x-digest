# X-FEED 2026-08-30 part 5/6 | items: 5

## @omarsar0 (продолжение)

T=2093786788628185328 | @omarsar0 | 2026-08-29T19:44+00:00 | L41 RT3 C9 V6733 | post
URL=https://x.com/omarsar0/status/2093786788628185328
TEXT: You do not need frontier models for everything.

For example, open models are great for automations. 

If you are not sure where to adopt open models, start there. 

It's one of the biggest changes I've made that contributed to a large percentage of my token usage moving to local or open models.

A huge percentage of my automations consist of repetitive tasks steered via self-tuned skills. 

These skills become useful automations that work really well with these open models. I don't even need to tune the models, but that's also an option I am currently exploring for more complex tasks. The skill essentially takes care of that. And it works because of the in-context learning capabilities of these models. 

If you don't run automations, it might be hard to figure this out. But I highly recommend you start somewhere. 

Besides ending up with more efficient automations, I've managed to significantly reduce costs. I then use that extra budget to leverage more closed frontier intelligence for other creative and research-heavy tasks. 

That's right! I use both closed and open frontier intelligence. This is not about vendor loyalty; this is about leveraging the best of all worlds. 

Something I heavily advocate for is owning the harness and the model, and this practice I feel will allow me to better tap into all flavors of intelligence (open & closed).

Maybe too early, but I suspect this is going to become best practice when AI ROI dominates the discussion. 

Model routing doesn't solve this. This requires tedious engineering, evals, and decision-making on your part. If you are developing your own harness, you are in the driver's seat and have more control over this important decision. This is why I strongly believe that companies will start to hire rapidly for harness engineering.

I am sharing a little snapshot of one example of an automation I run daily to track AI trending stories on HN. And I have a bunch of similar ones for different sources like arXiv, X, and so on. I also use it for some proactive agent sessions that keep track of important events around projects I build. You don't need frontier intelligence for this.
--
T=2093812326851903743 | @omarsar0 | 2026-08-29T21:25+00:00 | L31 RT8 C6 V5806 | rt
URL=https://x.com/omarsar0/status/2093812326851903743
RT-OF @dair_ai (L31): Finally, a paper testing whether hiding your agent skill files actually protects them.

The short answer is no. That's concerning.

Worth reading if you sell access to a skill or share one across teams.

This new paper discusses more:

Daydreaming reconstructs a hosted multi-file skill using only the ordinary tasks the service exists to perform. The victim is never asked to reveal the skill or grade a reconstruction, so disclosure filters have nothing to catch.

At the weakest access level, where the attacker sees only the final response and returned files, it recovers 86.8 percent of the original skill's capability across 7 skills and 4 victim models.

That is roughly 4x SigLeak, at a median of 32 victim calls per skill, with disclosure defenses enabled.

Paper: https://t.co/fG776Yglzm

Chat with Paper: https://t.co/arTr8VftTy
RT-URL=https://x.com/dair_ai/status/2093805947860967907
TEXT: RT @dair_ai: Finally, a paper testing whether hiding your agent skill files actually protects them.

The short answer is no. That's concern…
LINKS: https://arxiv.org/abs/2608.26733 ; https://academy.dair.ai/papers/hidden-agent-skills-can-be-stolen-through-normal-use-2608.26733
--
T=2093868737124295121 | @omarsar0 | 2026-08-30T01:09+00:00 | L52 RT7 C13 V6187 | rt
URL=https://x.com/omarsar0/status/2093868737124295121
RT-OF @dair_ai (L52): // Your LLM judge disagrees with the experts //

LLM Judges can be tricky to build.

Here is an interesting showcasing why:

There propose a reference-full benchmark of hundreds of complete human-to-human dialogues written by professional script writers, with realistic turn densities and more than 36,000 per-turn human annotations across over 30,000 expert-generated turns.

Conversational evaluation frameworks were mostly built for summarization, translation and short-form QA, and the metrics themselves are often derived and validated on synthetic data rather than human dialogue.

Tested against expert judgment at this scale, both classical automatic metrics and reference-free LLM-as-a-judge approaches turn out to be unreliable.

Their Mixture-of-Judges framework combines multiple evaluative signals and recovers roughly 30 percent better correlation with human assessment.

Paper: https://t.co/gj0vvfBANb

Chat with Paper: https://t.co/a7cktZX2zo
RT-URL=https://x.com/dair_ai/status/2093866305036427631
TEXT: RT @dair_ai: // Your LLM judge disagrees with the experts //

LLM Judges can be tricky to build.

Here is an interesting showcasing why:

T…
LINKS: https://arxiv.org/abs/2608.26131 ; https://academy.dair.ai/papers/evaluating-language-models-in-realistic-conversational-contexts-2608.26131
--
## @rasbt — 1 шт.

T=2093747982470459720 | @rasbt | 2026-08-29T17:09+00:00 | L186 RT16 C12 V18742 | thread(2)
URL=https://x.com/rasbt/status/2093747982470459720
TEXT: And if you can't make it at 10 am, here is the second Q&amp;A, hosted by Sage Elliott’s AI Book Club at 2 pm CT.
Model (From Scratch):
https://t.co/HdUvkpf6OB
[->] Thanks everyone for all the nice feedback on Build a Reasoning Model (From Scratch) so far!

I am also flattered that 2 book clubs are discussing it. 
I look forward to join for live Q&amp;As on Thu, Sep 3, at 10 am (and 2 pm CT). 

Please join us &amp; bring your questions!
QUOTED @sagecodes: already well over a hundred RSVPs in 24 hours! You have a whole week to read the book and come up with questions 😊
LINKS: https://x.com/sagecodes/status/2093543717538013442?s=20
--
## @sayashk — 1 шт.

T=2093735525186510852 | @sayashk | 2026-08-29T16:20+00:00 | L69 RT9 C14 V8772 | rt
URL=https://x.com/sayashk/status/2093735525186510852
RT-OF @NateWitkin (L69): Understandably, the reward-hacking behaviors on display in the Hugging Face incident are being treated as a cyber-risk story. But I'm not seeing sufficient discussion of the fact that they're also an economic story.

Reward-hacking behaviors pose a serious challenge for complex, long-horizon tasks in enterprise, considering that

1) by their nature, they are often unpredictable;

2) they are "fractal" in the sense that, even well-specified intermediate outcomes meant to guard against reward-hacking can themselves be reward-hacked (and so on at smaller scales);

3) they pose serious cyber, legal, and financial risks, as Hugging Face makes abundantly clear.

As a result, you could say that reward-hacking is as bearish on the economic front as it is "bullish" on the risk front.

It is greatly underappreciated by safety folks that, on average, the riskiness / unpredictability of a technology is going to be anti-correlated with its diffusion into the economy. This matters a lot in the AI case because capabilities growth is highly sensitive to the resources available for training, R&D and so on, resources that are at risk of drying up if AI produces insufficient returns, or only produces sufficient ones on the wrong timescale.

This is connected to a form of fallacious reasoning that I often see from the AI maximalist camp, which is to assume that the requisite capital for AI training, R&D, and so on will always be available in arbitrarily large amounts, which is why it can be safely assumed that capabilities will continue to grow without fail.

But this isn't true! The availability of capital for capabilities research and training is endogenous, and obviously so, to AI's economic prospects, even over very short timescales (one wonders, for example, how capabilities progress so far has been influenced by the timing and size of frontier labs' capital raises, relative to various counterfactual scenarios).

I see far too little discussion among safety folks of how these two 
RT-URL=https://x.com/NateWitkin/status/2093724533647618171
TEXT: RT @NateWitkin: Understandably, the reward-hacking behaviors on display in the Hugging Face incident are being treated as a cyber-risk stor…
--
