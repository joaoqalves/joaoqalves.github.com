---
type: post
title: "You can just open-source things"
date: "2025-08-26 08:01:03"
entry_id: 44646
canonicalURL: "https://world.hey.com/joaoqalves/you-can-just-open-source-things-2c1e2b77"
---

At [Adevinta](https://adevinta.com/), [Alex Moleiro](https://www.linkedin.com/in/alexmoleiro/) initiated a project a few years ago in his Platform teams: instead of asking people, "Can you just create me a ticket?" when they had a problem and passed by a Slack channel, he started automating that creation. In that way, there was a win-win situation:

1. People got support right where they were. No copy-and-paste, no friction. The member of a team reacted with an emoji (e.g., 🎫), and a bot created the ticket in Jira. Bam!
2. Teams not only had their internal processes respected, but it also surfaced the *actual* support volume. That was critical to understanding the users' pain points and creating a [compelling internal platform](https://platformengineering.org/talks-library/platform-as-a-product).

As I managed the Runtime team, responsible for overseeing a large Kubernetes-as-a-service fleet, I saw immediate value in it. I expanded the feature set to support specific use cases, such as providing users with context that a ticket had been created and setting expectations regarding service-level objectives.

[![cprhc-message.png](https://world.hey.com/joaoqalves/2c1e2b77/representations/eyJfcmFpbHMiOnsiZGF0YSI6MjIzOTg4MDg4MywicHVyIjoiYmxvYl9pZCJ9fQ--926bb1c22ee441e0b26f96dd06def8b8d8f13beae8afa20fdca4dc144cb57c07/eyJfcmFpbHMiOnsiZGF0YSI6eyJmb3JtYXQiOiJwbmciLCJyZXNpemVfdG9fbGltaXQiOlszODQwLDI1NjBdLCJxdWFsaXR5Ijo2MCwibG9hZGVyIjp7InBhZ2UiOm51bGx9LCJjb2FsZXNjZSI6dHJ1ZX0sInB1ciI6InZhcmlhdGlvbiJ9fQ--7edc7b21f6fad97fa22412618822c4d19725431f296c7ce47dc174b61535d27c/cprhc-message.png)](https://world.hey.com/joaoqalves/2c1e2b77/blobs/eyJfcmFpbHMiOnsiZGF0YSI6MjIzOTg4MDg4MywicHVyIjoiYmxvYl9pZCJ9fQ--926bb1c22ee441e0b26f96dd06def8b8d8f13beae8afa20fdca4dc144cb57c07/cprhc-message.png?disposition=attachment "Download cprhc-message.png")

# Creating Abistama

I really liked the idea of people not exposing internal complexity by asking "please create me a ticket". No one has time for that! That's why I created [Abistama](https://abistama.com/), a complete rewrite inspired by our experience at Adevinta. The idea was to streamline the adoption of these practices across multiple teams worldwide. Aside from doing zero marketing, I missed two important points with this solution:

1. It has double friction. It needs people to install it in their Slack workspaces. Most of the time, if you are big enough to have support problems, you need approvals to install new apps on Slack. Then, you will most likely need approvals to get authenticated through OAuth to Jira as well.
2. Partially because of the first point, people tend to automate these things themselves, internally. No credit cards. A new Slack application, a few API calls, or integrations with Zapier, and it works.

[![demo.gif](https://world.hey.com/joaoqalves/2c1e2b77/representations/eyJfcmFpbHMiOnsiZGF0YSI6MjIzOTg4MTEwMCwicHVyIjoiYmxvYl9pZCJ9fQ--829fc5088fa65acae0491a030c7adab64fce43bace9d190021aa5c962de68359/eyJfcmFpbHMiOnsiZGF0YSI6eyJmb3JtYXQiOiJnaWYiLCJyZXNpemVfdG9fbGltaXQiOlszODQwLDI1NjBdLCJxdWFsaXR5Ijo2MCwibG9hZGVyIjp7InBhZ2UiOm51bGx9LCJjb2FsZXNjZSI6dHJ1ZX0sInB1ciI6InZhcmlhdGlvbiJ9fQ--fa14265cdeaa7bfc361e7132c504746e1a27380cdc2502a56d65c43cc633e405/demo.gif)](https://world.hey.com/joaoqalves/2c1e2b77/blobs/eyJfcmFpbHMiOnsiZGF0YSI6MjIzOTg4MTEwMCwicHVyIjoiYmxvYl9pZCJ9fQ--829fc5088fa65acae0491a030c7adab64fce43bace9d190021aa5c962de68359/demo.gif?disposition=attachment "Download demo.gif")

# Open-sourcing

Lately, I've been inspired by the great work that David Heinemeier Hansson ([DHH)](https://world.hey.com/dhh) has been doing with [Omarchy](https://omarchy.org/) and Linux in general. If we pair that work with Large Language Models (LLM) and the ease of code in 2025, I'm seeing a "builder mentality" come back. People are prouder to build things than ever.

Abistama evolved with different products, such as [Rotahog](https://rotahog.com/), and I lost some interest in this support bot. Still, the codebase is OK-ish, has plenty of tests, and it's easy to deploy the backend somewhere. So, with the help of [Cursor](https://cursor.com), I cleaned up some parts related to multi-tenancy and wrote a reasonably comprehensive [*ReadMe*](https://github.com/abistama/support-hero) file.

So the choice was easy: should I keep something for myself that I won't monetize anyway? Of course not. Let the community benefit from it. Sharing it feels like the natural conclusion of this journey. The value of these tools is rarely in the tool itself, but in the conversations and improvements they spark within teams. If Abistama can save someone from copy-pasting into Jira, or help a platform team better understand their support load, then it has done its job.

Will it be perfect for everyone? Absolutely not. However, that's the beauty of open source: it doesn't require it. Fork it, hack it, adapt it to your needs. Perhaps you'll integrate your own ticketing system, add AI to automate triage, or streamline the code for a small team. The critical part is lowering the barrier for others to try.

If you've ever sighed at the words "please create me a ticket," then maybe [Abistama's Support Hero](https://github.com/abistama/support-hero) is worth a look.   
  
At the very least, it can serve as a base to build something more aligned with your team's reality.

I'd love to hear feedback from anyone who picks it up or extends it. And if nothing else, I hope it serves as a reminder that you don’t always need to wait for the perfect tool or initiative. With today’s building blocks, it’s easier than ever to automate away friction and make life better for your team.   
  
You can find Support Hero on [GitHub](https://github.com/abistama/support-hero).

— João
