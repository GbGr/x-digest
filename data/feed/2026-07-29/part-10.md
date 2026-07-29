# X-FEED 2026-07-29 part 10/12 | items: 6

## @rasbt — 2 шт.

T=2082098201247600765 | @rasbt | 2026-07-28T13:37+00:00 | L2756 RT404 C81 V119215 | post
URL=https://x.com/rasbt/status/2082098201247600765
TEXT: The Kimi K3 architecture figure for yesterday's big open-weight model release, along with some observations and thoughts.

1. Yes, it looks relatively complicated, but it's essentially a scaled-up production version of their Kimi Linear model they released last year (scaled up from 48B -> 2.8T; K3 is by far the biggest open-weight model right now)

2. The one new component compared to Kimi Linear is the LatentMoE. I omitted it in the figure below since it's already very crowded, but that's essentially the same LatentMoE as in Nemotron 3 Ultra (you can find it in my LLM Architecture Gallery if you are curious). The idea here is to compress (down-project) large linear layers similar to multi-head latent attention.

3. Kimi K3's overall trend (similar to Nemotron 3, DeepSeek V4, and others) is also towards better inference efficiency. That is, there are many components that replace existing components with efficiency-tweaked versions. I.e., MoE -> LatentMoE, regular attention -> multi-head latent attention and Kimi Delta Attention. (I also have short tutorials and write-ups in my gallery if you are curious about additional details).

4. The one component change that is not an efficiency tweak is attention residuals. Like DeepSeek V4 improved the residual path with mHC (manifold-constrained Hyper-Connections), attention residuals are a way to improve the residual path, but it works a bit differently. I.e., mHC made the residual path wider. Attention residuals (also already part of Kimi Linear) connect the residuals across layers; the connection itself uses an attention score for an important/contribution weight. According to the report, it improves the validation loss and downstream performance (a bit) consistently and adds about 4% in training cost and 2% in inference cost.

5. Interestingly, Kimi K3 got rid of all RoPE layers and uses NoPE (No Positional Embeddings) everywhere instead. (Again, this is inherited from Kimi Linear). In other architectures, the recent trend was towards RoPE in local attention layers (like sliding window attention) and NoPE in the global layers. There were a few architectures that only used NoPE everywhere, but this is the first frontier-level one as far as I know.

6. Kimi K3 now also has native multimodal support, which is great!

There are several other interesting training tidbits in the technical report, but that's it from the architecture front so far. A really great release overall.
--
T=2082101241908249014 | @rasbt | 2026-07-28T13:49+00:00 | L2375 RT107 C64 V112744 | post
URL=https://x.com/rasbt/status/2082101241908249014
TEXT: Yes, LLM architectures are getting a little more complicated https://t.co/jII112pJbO
--
## @RLanceMartin — 2 шт.

T=2082179931040264623 | @RLanceMartin | 2026-07-28T19:02+00:00 | L10280 RT1031 C239 V1411464 | rt
URL=https://x.com/RLanceMartin/status/2082179931040264623
RT-OF @ClaudeDevs (L10280): MCP 2026-07-28 is live and it's the largest update to the protocol since launch.

MCP is now stateless, making it easier to deploy and scale remote servers. 

https://t.co/K8KqxbUh4e
RT-URL=https://x.com/ClaudeDevs/status/2082164248697069935
TEXT: RT @ClaudeDevs: MCP 2026-07-28 is live and it's the largest update to the protocol since launch.

MCP is now stateless, making it easier to…
LINKS: https://claude.com/blog/bringing-mcp-2026-07-28-to-claude
--
T=2082179884051489219 | @RLanceMartin | 2026-07-28T19:02+00:00 | L4776 RT629 C330 V1515086 | rt
URL=https://x.com/RLanceMartin/status/2082179884051489219
RT-OF @AnthropicAI (L4776): New Anthropic research: Discovering cryptographic weaknesses with Claude.

Claude Mythos Preview has helped our researchers find weaknesses in cryptographic algorithms—the mathematical methods that are used to keep data private.

Read more: https://t.co/TYKLjb3Q7V
RT-URL=https://x.com/AnthropicAI/status/2082153297670992134
TEXT: RT @AnthropicAI: New Anthropic research: Discovering cryptographic weaknesses with Claude.

Claude Mythos Preview has helped our researcher…
LINKS: https://anthropic.com/research/discovering-cryptographic-weaknesses
--
## @sayashk — 2 шт.

T=2082213499040682254 | @sayashk | 2026-07-28T21:15+00:00 | L9 RT3 C0 V391 | rt
URL=https://x.com/sayashk/status/2082213499040682254
RT-OF @BerkeleyISchool (L9): Dr. @sayashk has been appointed as an assistant professor at the I School, starting in July 2027.

“I am excited about the School of Information’s commitment to interdisciplinary scholarship and conducting research in the public sphere,” said Kapoor. 
https://t.co/wSgffc5ZnD
RT-URL=https://x.com/BerkeleyISchool/status/2082212257719628202
TEXT: RT @BerkeleyISchool: Dr. @sayashk has been appointed as an assistant professor at the I School, starting in July 2027.

“I am excited about…
LINKS: https://www.ischool.berkeley.edu/news/2026/sayash-kapoor-joins-uc-berkeley-focus-artificial-intelligence
--
T=2082287347710689680 | @sayashk | 2026-07-29T02:09+00:00 | L617 RT61 C19 V150404 | rt
URL=https://x.com/sayashk/status/2082287347710689680
RT-OF @random_walker (L617): To understand and empathize with how workers in many or most fields outside software experience advances in AI capabilities, I propose a little thought experiment. https://t.co/QZG24aRiBe
RT-URL=https://x.com/random_walker/status/2082163285588107752
TEXT: RT @random_walker: To understand and empathize with how workers in many or most fields outside software experience advances in AI capabilit…
LINKS: http://x.com/i/article/2082158799104659456
--
