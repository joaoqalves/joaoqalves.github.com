---
type: post
title: "I’m a Tech Lead, and nobody listens to me. What should I do?"
date: "2025-12-16 09:26:34"
entry_id: 46153
canonicalURL: "https://world.hey.com/joaoqalves/i-m-a-tech-lead-and-nobody-listens-to-me-what-should-i-do-e16e454d"
---

In June 2018, I joined mytaxi ([FREE NOW](https://www.free-now.com/uk/)), a competitor of Uber in the ride-hailing space, as Backend Chapter Lead. I was looking for an opportunity to grow in technical leadership. Honestly, I did not even fully understand what “Chapter Lead” meant. After some research, I learned it was part of [Spotify](https://agile-frameworks.com/_spotify/spotify.html)’s squad (team) and chapter (horizontal domain, such as iOS, Android, Backend, Data, etc.) model, as well as tribes (groups of squads organized around vertical domains, for example, everything related to drivers).  
  
*Note*: this article is a translation from the original “[Soy Tech Lead y no me hacen caso. ¿Qué hago?](https://enespanol.joaoqalves.net/p/soy-tech-lead-y-no-me-hacen-caso)”, in Spanish.  
  
  
 
[![Screenshot 2025-12-10 at 20.10.55.png](https://world.hey.com/joaoqalves/e16e454d/representations/eyJfcmFpbHMiOnsiZGF0YSI6MjM4MDE2NTAyNiwicHVyIjoiYmxvYl9pZCJ9fQ--faeb376287e9805a250b9f66538ddbad3f2a57406a2c5e8bd67ac6e9263ff351/eyJfcmFpbHMiOnsiZGF0YSI6eyJmb3JtYXQiOiJwbmciLCJyZXNpemVfdG9fbGltaXQiOlszODQwLDI1NjBdLCJxdWFsaXR5Ijo2MCwibG9hZGVyIjp7InBhZ2UiOm51bGx9LCJjb2FsZXNjZSI6dHJ1ZX0sInB1ciI6InZhcmlhdGlvbiJ9fQ--7edc7b21f6fad97fa22412618822c4d19725431f296c7ce47dc174b61535d27c/Screenshot%202025-12-10%20at%2020.10.55.png)](https://world.hey.com/joaoqalves/e16e454d/blobs/eyJfcmFpbHMiOnsiZGF0YSI6MjM4MDE2NTAyNiwicHVyIjoiYmxvYl9pZCJ9fQ--faeb376287e9805a250b9f66538ddbad3f2a57406a2c5e8bd67ac6e9263ff351/Screenshot%202025-12-10%20at%2020.10.55.png?disposition=attachment "Download Screenshot 2025-12-10 at 20.10.55.png")

*The squads, tribes, chapters, and guilds model popularized by Spotify.* [*Source*](https://agile-frameworks.com/_spotify/spotify.html)*.*

That role had two main components:

- **Backend technical leadership** (TL), driven by best practices and with a strong emphasis on continuous improvement. At the time, mytaxi was experiencing major traffic growth. Some services — for example, the one used to incentivize drivers to complete more rides — experienced significant traffic spikes and required improvements, re-architecting, and similar work. On top of that, there were a bit over 200 services to manage.
- **People management** in a horizontal setup. The idea was that all backend engineers would report to either [Ariel](https://www.linkedin.com/in/ariel-cardieri-6971261/), the other Chapter Lead, or me, regardless of their team. This was not a very orthodox setup, but at the time, around 3–5 backend engineers were joining every month. There was a strong need to make people productive as quickly as possible, align on architecture, and keep the product moving.

I came in with no prior formal experience as a Tech Lead. I think I never read as much in my life as during the month between announcing I was leaving my previous job and joining mytaxi. Not only that. I had never really had a proper Tech Lead to learn from. What could go wrong?  
  
---

The first day was very entertaining. I log into Slack and introduce myself to the infrastructure and platform manager. He says:

> By the way, you have an incident in service X. Could you take a look?

Just like that. It is nine in the morning on a Monday, and we already have an incident. I do not even know where the logs are, Henning. After the initial shock, I managed to find the responsible team. They identified the issue, fixed it, and everything got resolved.

This first interaction made several things very clear to me:

- Nobody really knows how to manage incidents, document what happened, or communicate progress. Great start.
- There is no culture of doing incident reviews or extracting actions to prevent similar incidents in the future.
- There is some coupling between domains. In this case, the Value Added Tax (VAT) concept was applied to two completely different use cases. A change in one of them caused the incident in the other.
- Many people do not know how to debug. They look at me as if the logs were talking to me, or as if I were Harry Potter.

The good part was that there was clearly a lot to fix. I had a pretty clear idea of how engineering culture could be improved. On top of that, I had the Tech Lead title. This was going to be easy. Or maybe not.  
  
---

👋 Hi, João here. This is the opening post of a series designed for Tech Leads and Engineering Managers who want to lead with greater clarity and intention.

- “[Traits of a good Tech Lead](https://world.hey.com/joaoqalves/traits-of-a-good-tech-lead-b5cac0ae)”
- “I’m a Tech Lead, and nobody listens to me. What should I do?” ← This article
- “KPIs, SLOs, and operational excellence”. Coming soon. Subscribe so you do not miss it.
- To be continued…

I’m currently writing “The Tech Lead Handbook”, scheduled for release in H1 2026. The ideas in this series will form its core.

**If you want to** [**join the waitlist**](https://forms.gle/eMFGuc1Q3FZ8r3NG8)**, you’ll get a 25% launch discount**.

---

# Trust

After that incident, I created an incident review document and suggested a small review of the tasks that should be prioritized to prevent it from happening again. I got carried away and created an initial presentation for the other backend Chapter Leads with a backend strategy. I do not remember it perfectly, but it included hexagonal architecture, a testing pyramid with contract tests to avoid breaking APIs used by mobile apps, and more. Days go by, and I start thinking:

> Damn, nobody is listening to me. I put a lot of work into those slides and that strategy.

Today, the reason seems obvious to me. Titles do not grant influence. To influence, you need to build trust. And I had not earned enough of it yet to propose something so fundamental. Through my own experience and through coaching sessions, I have seen this exact mistake repeated several times throughout my career.

Years later, I discovered the well-known [trust equation by Maister, Green, and Galford](https://www.designative.info/2025/06/02/book-review-trusted-advisor-david-maister-charles-green-robert-galford/). It would have been incredibly helpful back then. It goes like this:  
  
 
[![trust-equation.png](https://world.hey.com/joaoqalves/e16e454d/representations/eyJfcmFpbHMiOnsiZGF0YSI6MjM4MTcxODM0NCwicHVyIjoiYmxvYl9pZCJ9fQ--f1e3d73f30a752badc535e4ac09dff9a65ecc47f40ee03c0e223da457666b3de/eyJfcmFpbHMiOnsiZGF0YSI6eyJmb3JtYXQiOiJwbmciLCJyZXNpemVfdG9fbGltaXQiOlszODQwLDI1NjBdLCJxdWFsaXR5Ijo2MCwibG9hZGVyIjp7InBhZ2UiOm51bGx9LCJjb2FsZXNjZSI6dHJ1ZX0sInB1ciI6InZhcmlhdGlvbiJ9fQ--7edc7b21f6fad97fa22412618822c4d19725431f296c7ce47dc174b61535d27c/trust-equation.png)](https://world.hey.com/joaoqalves/e16e454d/blobs/eyJfcmFpbHMiOnsiZGF0YSI6MjM4MTcxODM0NCwicHVyIjoiYmxvYl9pZCJ9fQ--f1e3d73f30a752badc535e4ac09dff9a65ecc47f40ee03c0e223da457666b3de/trust-equation.png?disposition=attachment "Download trust-equation.png")

*The trust equation. Generated with Gemini 3 / NanoBanana.*

The first time I read it, my mind was blown because it described exactly what was happening to me. Let’s break it down:

- **Credibility**: knowing what you are talking about and having technical judgment. When you say something, people feel it is well-founded. In 2018, I might have had some of this credibility, but it had not yet been proven in that context, with those people, with those systems. I was coming from the outside. Imported credibility is always worth less — unless you come from a FAANG or have built a strong personal brand — than credibility earned on the ground.
- **Reliability**: doing what you say you will do. Being consistent and showing up when needed. In a high-paced environment like mytaxi, this matters a lot. In those first days, I was still learning where the logs lived. It is hard to demonstrate reliability if you do not even control the map.
- **Intimacy**: people feel they can talk to you, that you will not leave them exposed, and that you understand their fears and doubts. For a TL, this is more important than it seems. Without this, any technical proposal feels like a judgment. And when people get defensive, everything slows down.
- And then there is the denominator: **self-orientation**. When your proposals seem to serve your own agenda more than the team’s needs, trust collapses. That was my mistake. I arrived with a strategy too early, without listening, without seeing what they actually needed, without having earned the moral right to propose it.

In other words, even if my ideas were good, the equation still did not work out. I had some credibility, a bit of reliability still to build, intimacy yet to be created, and too much self-orientation. The result was obvious. Low trust.

**Two key moments**

Over time, I realized that trust is not built through big speeches, but through concrete actions that solve real, everyday problems. Looking back, two obvious moments accelerated the team’s shift in how they perceived me.

**Regulatory complexity**

Because mytaxi competed with Uber in a highly regulated taxi market, with very local regulations across Europe, the application needed to support multiple variants of the same flow. This led to the proliferation of dozens of configuration flags across all services. The result was chaos. Nobody knew for sure what was enabled in each city, what affected iOS, what affected Android, or where each option was actually defined. To make matters worse, the configuration was spread across roughly 200 services.

One day, [Maria](https://www.linkedin.com/in/mariachec/) — an Agile Coach — talked to me very directly about this pain. I did what I knew best at the time. I built something. I put together a portal — a bit rough, to be honest — that queried the configuration APIs of all services and aggregated that information by functionality, country, or city. Features could be browsed by city or by name. The website was very simple, generated from an HTML template by a Python service.  
  
 
[![ff-tool-mytaxi-en.png](https://world.hey.com/joaoqalves/e16e454d/representations/eyJfcmFpbHMiOnsiZGF0YSI6MjM4MTcyMDczOCwicHVyIjoiYmxvYl9pZCJ9fQ--0761f5b0a191c12c02353aad23d02bd91dcf2d69af8cd01efea104da80e6abd5/eyJfcmFpbHMiOnsiZGF0YSI6eyJmb3JtYXQiOiJwbmciLCJyZXNpemVfdG9fbGltaXQiOlszODQwLDI1NjBdLCJxdWFsaXR5Ijo2MCwibG9hZGVyIjp7InBhZ2UiOm51bGx9LCJjb2FsZXNjZSI6dHJ1ZX0sInB1ciI6InZhcmlhdGlvbiJ9fQ--7edc7b21f6fad97fa22412618822c4d19725431f296c7ce47dc174b61535d27c/ff-tool-mytaxi-en.png)](https://world.hey.com/joaoqalves/e16e454d/blobs/eyJfcmFpbHMiOnsiZGF0YSI6MjM4MTcyMDczOCwicHVyIjoiYmxvYl9pZCJ9fQ--0761f5b0a191c12c02353aad23d02bd91dcf2d69af8cd01efea104da80e6abd5/ff-tool-mytaxi-en.png?disposition=attachment "Download ff-tool-mytaxi-en.png")
  
 *The features could be queried by city or by name. The website was very simple, with HTML generated by a Python service.*

Suddenly, at a glance, anyone could see what was enabled and where. It was not pretty, but it solved a problem. More importantly, it showed that **I was there to help them work better** (credibility), not to impose an abstract technical agenda. Soon after, other teams started using the portal, including Product Owners, QA, and even Operations. Without intending to, it became an organizational alignment tool. And it led to something even more interesting. Other engineers started contributing.

Once they saw the value it created, several colleagues proposed improvements, fixed minor bugs, and added features I had never even considered. One of them built a small website to visualize city zones, which solved a long-standing pain for teams working with geofencing or driver-passenger assignment. Another automated part of the flag update process. Someone else added metrics to detect inconsistent configurations across platforms.

What started as a quick hack turned into a small ecosystem of internal tools that reduced uncertainty, sped up decisions, and made the team’s life a little easier every week.

That domino effect taught me something important. When you solve a real problem and make it visible, people join in. Trust is also built that way, by inviting others to improve what you started and celebrating when they do it better than you.

**Debugging**

The second moment concerned something much more human. Helping people debug. I have never considered myself especially smart, but I have always been very systematic when connecting error messages, code, hypotheses, and system behavior. To my surprise, many people saw this as almost magical. It was not magic. It was a mix of experience, fundamentals, intuition, knowing where to look, and not being afraid to dive into third-party library code.

I started pairing with colleagues during incident resolution (intimacy), teaching them to formulate and discard hypotheses, read logs with intent, and distinguish symptoms from root causes. I proposed incident-review practices that improved the quality of our responses and helped us learn collectively.

Without realizing it, these two contributions did more for my reputation than any presentation or strategy deck. **Building helpful things and standing by people when the system is on fire creates more trust than any title**. That was when my ideas finally started gaining traction. Interestingly, these two actions reduced my self-orientation to zero. I stopped thinking about “my strategy” and started thinking about “our work”.

# What would you tell your 2018 self?

Looking back, one idea stands out. No, TLs don’t earn influence just because “it is their role”. It is earned every day, not through speeches, but by solving painful problems and being present when people need real support.

If you are in a similar situation, here is some advice I wish I had received in 2018:

- Before proposing a strategy, first understand what actually hurts your team.
- Pick one or two actions that deliver immediate value and execute them.
- Talk less about architecture and more about how your proposal reduces toil, risk, or uncertainty.
- Do not try to prove you are the smartest person in the room. Try to help others do their job better.
- Feedback cycles, unlike code, are slower. They are measured in weeks or months. Be patient.
- And above all, remember that trust is cumulative. It is earned in every interaction.

Technical influence does not start with a title. It begins with the **visible impact** you create. Because when a TL feels unheard, the solution is not to speak louder.  
  
It is to change the conversation. And to start from the only place you truly control: **your own behavior**.  
  
---  
  
🎁 **Want to put this into practice with your team tomorrow? Subscriber-only gift**

Many Tech Leads feel unheard because EMs, TLs, and the rest of the team operate with different expectations that no one has made explicit. That friction is not resolved with more meetings or more processes. It is determined with clarity. To help you close that gap, I have prepared a FREE alignment toolkit with three practical tools:

- For **Tech Leads**: a self-assessment traffic light to fight impostor syndrome and clearly understand where you are creating value and where you are burning out.
- For **Engineering Managers**: an evaluation traffic light to give objective feedback based on behaviors, not gut feelings. Help your Tech Leads have areal impact.
- For the **team**: an operational principles template to stop debating the same decisions every week and create shared criteria.

In addition, to complement this article, **I will include a concrete plan for your first 90 days as a Tech Lead**: what to observe, what to prioritize, what to avoid, and how to build trust through small, visible steps. It is the plan I wish I had had during my first week at mytaxi.

If you have already downloaded the toolkit, you do not need to do anything. You already have the updated version and will automatically receive the 90-day plan.

If you are not yet subscribed, **subscribe,** [**complete this form**](https://forms.gle/UBZtSnBMXTgqZYt46)**, and I’ll send you the kit** so you can move from intention to action. It is FREE!

---  
  
— João
