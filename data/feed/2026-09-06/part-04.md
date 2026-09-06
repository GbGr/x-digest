# X-FEED 2026-09-06 part 4/6 | items: 9

## @omarsar0 — 10 шт.

T=2096219681682018409 | @omarsar0 | 2026-09-05T12:51+00:00 | L194 RT14 C44 V19589 | rt
URL=https://x.com/omarsar0/status/2096219681682018409
RT-OF @omarsar0 (L194): Updated my harness to combine the best of Grok Bot and Hermes Agent. 

Woah!!!

Persistent self-improving agents, with well a designed UI, are mindblowing.🤯 

Much closer to the dream of personal agents I’ve been building for over a year. More to share soon. Excited!
RT-URL=https://x.com/omarsar0/status/2096042211272003947
TEXT: RT @omarsar0: Updated my harness to combine the best of Grok Bot and Hermes Agent. 

Woah!!!

Persistent self-improving agents, with well a…
--
T=2096227739426517343 | @omarsar0 | 2026-09-05T13:23+00:00 | L38 RT8 C7 V10675 | rt
URL=https://x.com/omarsar0/status/2096227739426517343
RT-OF @omarsar0 (L38): I read AI papers for a living, but it has become impossible to track insights.

Every week I triage agent papers for our Top AI Papers of the Week digest.

A few weeks ago, I tried @viktor_com, an AI employee that works inside Slack, in the channel where that triage happens.

I asked it to go through the week's agent papers and pull three worth reading.

It sent the list back that same morning.

On day 19, it posted in the channel without being asked. "Six more landed overnight. One of them contradicts the routing section in module 4."

Two days later, again without me, it drafted the correction and left it unpublished. 2,100 people are on that module.

Everything it did came back as a proposal for me to approve. That is why I kept it running.

Finding new papers is easy. Knowing when one of them breaks something is much harder - in my case, the course lessons I teach.

If you run agents for weeks at a time, look closely at how the approval trail works. Happy to go deeper on this one.
RT-URL=https://x.com/omarsar0/status/2095889841728675933
TEXT: RT @omarsar0: I read AI papers for a living, but it has become impossible to track insights.

Every week I triage agent papers for our Top…
--
T=2096272427818811495 | @omarsar0 | 2026-09-05T16:21+00:00 | L174 RT17 C13 V20231 | post
URL=https://x.com/omarsar0/status/2096272427818811495
TEXT: Highly recommended. It's not obvious, but a bottleneck in even the most powerful models, like GPT-6 Astra, is context bloat and compaction. This new config can help keep Astra persistent across long-running tasks. 

If it helps, here is a little visual summary courtesy of GPT-6 Astra.
QUOTED @gabrielchua: "With Astra, we’re introducing a new way for Codex to preserve and retrieve context when the context window fills ... In Codex, Astra can keep notes across context windows, preserving accumulated details without repeatedly compressing them into a single summary..."

See the next post on how to enable it 👇
--
T=2096288397811679718 | @omarsar0 | 2026-09-05T17:24+00:00 | L76 RT7 C4 V18964 | post
URL=https://x.com/omarsar0/status/2096288397811679718
TEXT: GPT-6 Astra is absolutely insane for generating 3D stuff.

"Generate a Grok Bot version of Codex Micro."

Now I want this so bad!

In one prompt. Imagine what else it can do—sharing more insane examples shortly. https://t.co/YOcWgKZe8x
--
T=2096293183063744629 | @omarsar0 | 2026-09-05T17:43+00:00 | L84 RT7 C10 V8841 | rt
URL=https://x.com/omarsar0/status/2096293183063744629
RT-OF @dair_ai (L84): Banger paper from Microsoft and Cornell.

If you have looked at thinking tokens and decided you cannot afford the context, read this one.

(bookmark it)

A pause token buys the model extra compute for each next-token prediction, and it pays for that compute with a sequence position. Free pause tokens carry the same compute in a parallel prediction stream over a weight-shared backbone, riding an existing position instead of adding one.

At inference it adds nothing to context length, leaves the KV cache unchanged, and costs essentially no extra latency, since the additional flops are not the throughput bottleneck. On a 1B model it improves next-token prediction by 2 to 3 centinats.

The cost moves to training, where the overhead against an optimized pretraining pipeline comes down to about 1.14x while keeping most of the benefit.

Paper: https://t.co/gtVh1RkXqd

Chat with Paper: https://t.co/xknIYXckQ3
RT-URL=https://x.com/dair_ai/status/2096278691966001512
TEXT: RT @dair_ai: Banger paper from Microsoft and Cornell.

If you have looked at thinking tokens and decided you cannot afford the context, rea…
LINKS: https://arxiv.org/abs/2609.03807 ; https://academy.dair.ai/papers/free-pause-tokens-2609.03807
--
T=2096303354435760305 | @omarsar0 | 2026-09-05T18:24+00:00 | L78 RT13 C22 V8509 | post
URL=https://x.com/omarsar0/status/2096303354435760305
TEXT: This is a weird behavior in coding models and something worth looking into.

It turns that some models over-edit code that another models wrote.

There is a high chance that your repo now has commits from more than one model, and that changes how each of them edits.

Researchers measured what happens when one model edits code another model wrote. Different training data produces different stylistic preferences, and models make more edits, often excessive ones, on foreign code than on their own.

CROCODIL is a post-training framework that reduces that behavior. A similarity reward penalizes large changes and an execution reward scores build and test success, and the two are multiplied rather than added. That product stops the policy from shrinking edits by simply failing the task.

Paper: https://t.co/WyzDs0YWiO
LINKS: https://academy.dair.ai/papers/crocodil-cross-model-code-editing-with-llms-2609.03894
--
T=2096314593182171545 | @omarsar0 | 2026-09-05T19:08+00:00 | L164 RT20 C14 V13930 | thread(4)
URL=https://x.com/omarsar0/status/2096314593182171545
TEXT: I am in disbelief right now. 

GPT-6 Astra is a truly incredible model. 

It took about 2 hrs to generate this 3D model of Xunantunich, a Maya archaeological site in western Belize. https://t.co/lbEfTCx2go
[->] I also had this one set on my /goal feature. GPT-6 Astra built it from images it found on the internet.
[->] I have tried to do this with Fable plenty of times, and the quality is usually not there. This is the first time I've gotten something that looks like pretty good quality. In one go!

It's fun to give Astra an image and let it recreate something.
[->] BTW, if you come to Belize, go and visit this site. It's one of the most breathtaking things you will experience.

A 3D model doesn't do it any justice.
--
T=2096321092931485758 | @omarsar0 | 2026-09-05T19:34+00:00 | L1475 RT105 C42 V132376 | thread(4)
URL=https://x.com/omarsar0/status/2096321092931485758
TEXT: I found that using 4K in the prompt for v2 above led to much better results.

Here is v1:
https://t.co/DzbLgZNWDy
[->] OMG!!!

GPT-6 Astra built this using just one image reference.

I am at a loss for words. https://t.co/29ar6Ylu77
[->] Prompt used by my orchestrator for v2:

"Upgrade the existing isolated prototypes/grokbot interactive 3D keyboard to a 4K, markedly more realistic, premium product visualization with detailed manufactured geometry, convincing PBR materials, and refined studio lighting; preserve and validate key, dial, orbit, zoom, finish, lighting, and exploded-view interactions; pass the project's tests and production build."
[->] I will be writing more about the process to get something like this. Stay tuned!

I also have a bunch more generations to share.
QUOTED @omarsar0: GPT-6 Astra is absolutely insane for generating 3D stuff.

"Generate a Grok Bot version of Codex Micro."

Now I want this so bad!

In one prompt. Imagine what else it can do—sharing more insane examples shortly. https://t.co/YOcWgKZe8x
LINKS: https://x.com/omarsar0/status/2096288397811679718?s=20
--
T=2096339043919237288 | @omarsar0 | 2026-09-05T20:45+00:00 | L165 RT25 C20 V14876 | thread(3)
URL=https://x.com/omarsar0/status/2096339043919237288
TEXT: What the heck!?

GPT-6 Astra just finished creating this 3D camera with 122 component groups and 1,877 modeled pieces.

I didn't even realize you could build these in Three.js. https://t.co/YCpnLaXdl3
[->] If there is enough interest, I can share this online. I think this is the kind of AI output that could be great for learning about things around us.
[->] This one took a bit longer. It was like 3 hours. Sharing how I am building these this coming week. 

Along with a bunch of other ones I have been sharing.
--
