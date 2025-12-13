---
type: post
title: "Building on vibes: Lessons from three years with LLMs"
date: "2025-10-09 08:55:39"
entry_id: 45270
canonicalURL: "https://world.hey.com/joaoqalves/building-on-vibes-lessons-from-three-years-with-llms-564f2801"
---

There's a massive hype about Large Language Models (LLMs) and Artificial Intelligence (AI), in general. A few days ago, OpenAI and AMD [announced](https://www.amd.com/en/newsroom/press-releases/2025-10-6-amd-and-openai-announce-strategic-partnership-to-d.html) a partnership to deploy six gigawatts of AMD GPUs, with an initial rollout scheduled for 2026.

I've been using ChatGPT since 2022. I did one or two projects with it, even before agentic coding was a thing. Still, I could build a "score guesser" for the Qatar World Cup in under a week. Authentication and social sharing included. I was mind-blown.

After that experience, and with Cursor, Claude Code, and other agentic coding tools, it only got better. My workflow typically begins with a ChatGPT [project](https://help.openai.com/en/articles/10169521-projects-in-chatgpt), where I provide context about what I plan to build.  
  
 
[![description.png](https://world.hey.com/joaoqalves/564f2801/representations/eyJfcmFpbHMiOnsiZGF0YSI6MjI5MzU4NDk5OSwicHVyIjoiYmxvYl9pZCJ9fQ--2ed78d22a9b1fe48acf115cdf69dc9d0316ac13d87d6a7e5f75a57618e17c94c/eyJfcmFpbHMiOnsiZGF0YSI6eyJmb3JtYXQiOiJwbmciLCJyZXNpemVfdG9fbGltaXQiOlszODQwLDI1NjBdLCJxdWFsaXR5Ijo2MCwibG9hZGVyIjp7InBhZ2UiOm51bGx9LCJjb2FsZXNjZSI6dHJ1ZX0sInB1ciI6InZhcmlhdGlvbiJ9fQ--7edc7b21f6fad97fa22412618822c4d19725431f296c7ce47dc174b61535d27c/description.png)](https://world.hey.com/joaoqalves/564f2801/blobs/eyJfcmFpbHMiOnsiZGF0YSI6MjI5MzU4NDk5OSwicHVyIjoiYmxvYl9pZCJ9fQ--2ed78d22a9b1fe48acf115cdf69dc9d0316ac13d87d6a7e5f75a57618e17c94c/description.png?disposition=attachment "Download description.png")

You can see that there's a high-level description of the project ("what do I want to do?"), alongside some core Minimum Viable Product (MVP) feature set. Finally, I give some hints about the tech stack. The main reason I chose ChatGPT over Cursor or Claude Code is that I prefer to discuss things in depth with ChatGPT, which incurs a significant number of tokens in Cursor. So I use the latter only to implement the features. In smaller projects or Command-Line Interface (CLI) programs, I perform everything directly in Cursor.

# Feature lifecycle

For each feature, I create a new chat in ChatGPT, inside the project. I discuss briefly what I want to do, based on a prompt similar to:

> The first feature I want to implement is to create a "rotation", where an event on a given day is assigned to a finite list of people ("User").  
> I would like a minimal version of it. Before implementing it, please discuss it with me and ask me any clarifying questions.

So it triggers some questions like:

- How should the rotation be structured? For example, is it round-robin (cyclical) or random assignment?
- Do we need to account for people being unavailable on certain days?
- Should one event be assigned to exactly one user, or can multiple users share responsibility?
- How do we handle changes to the rotation list (e.g., adding or removing users)?
- Should assignments be visible to all users, or only to the person assigned to them?
- How do we notify a user that they've been assigned to an event?

By surfacing these questions early, ChatGPT helps me refine the scope of the feature before coding. Once I clarify the answers, I can then proceed to write a minimal implementation plan. I ask for a [Product Requirements Document](https://www.atlassian.com/agile/product-management/requirements) (PRD). It gives me back something similar to this:

[![prd.png](https://world.hey.com/joaoqalves/564f2801/representations/eyJfcmFpbHMiOnsiZGF0YSI6MjI5MzU4MzYxOCwicHVyIjoiYmxvYl9pZCJ9fQ--3bdf04d10a4deb42ce82abdcfbc4782ad20ab5ec825cfe9a2254a8dd28e32673/eyJfcmFpbHMiOnsiZGF0YSI6eyJmb3JtYXQiOiJwbmciLCJyZXNpemVfdG9fbGltaXQiOlszODQwLDI1NjBdLCJxdWFsaXR5Ijo2MCwibG9hZGVyIjp7InBhZ2UiOm51bGx9LCJjb2FsZXNjZSI6dHJ1ZX0sInB1ciI6InZhcmlhdGlvbiJ9fQ--7edc7b21f6fad97fa22412618822c4d19725431f296c7ce47dc174b61535d27c/prd.png)](https://world.hey.com/joaoqalves/564f2801/blobs/eyJfcmFpbHMiOnsiZGF0YSI6MjI5MzU4MzYxOCwicHVyIjoiYmxvYl9pZCJ9fQ--3bdf04d10a4deb42ce82abdcfbc4782ad20ab5ec825cfe9a2254a8dd28e32673/prd.png?disposition=attachment "Download prd.png")

The full PRD is available on my [GitHub](https://gist.github.com/joaoqalves/d190fa4f9dcc89836f306ea7fcc67bc5). My learnings on feature development are:

1. **Spend time writing detailed context**, both at the project level and feature level. LLMs are fantastic but not magical. No one is in your head. I like to leverage them to ask clarifying questions that narrow down the problem, or make me think about edge cases or things I hadn't considered myself.
2. The **PRD is a great format** to give to coding agents, as it increases the odds of achieving the desired result on the first attempt.
3. LLMs are great at creating new requirements or suggesting additions. **Prioritize ruthlessly**, or otherwise you'll make a monster in no time. Code is still a liability, and having ways to develop code faster is like having access to multiple credit cards at once. Be careful about product debt.

# Implementation

In terms of implementation, my main experience is with the Cursor code editor and CLI. My key learnings are:

1. At first, everything feels magical and one-shotted. You feel incredibly powerful and want to develop more features! That's a trap. I was dazzled by the *magical* moment and forgot the first principles of Software Engineering. **Writing tests, refactoring after the implementation, and documenting architecture** are essential to avoid a monster that makes the LLM hallucinate.
2. Context. It's a repetition, but with an important nuance. **Using features like** [**Cursor rules**](https://cursor.com/docs/context/rules) **or the "**[**AGENTS.md**](https://agents.md/)**" file enhances window context handling and yields better results**. You can even have different rules for the entire project, specific parts, or tech stack (e.g., SQL, Python, Java, or React), using classic glob patterns. For Abistama's Support Hero, I [created one](http://bit.ly/4oeAcPb) for Spring Boot + Kotlin.
3. **Writing tests is a surprisingly weak spot**, depending on the tech stack you use. What I usually do is provide an example of tests — it can be an agent rule, too, applied to the tests folder — and ensure it consistently generates tests.

# Talk is cheap, show me the products!

What have I shipped with this? A few things:

1. [RotaHog](http://bit.ly/4h3sF3s): a simple task roster ("rotation") to distribute work across a team. Who will prepare the next all-hands? As an Engineering Manager, I was tired of manually tracking it or using spreadsheets.
2. "[La Porra](https://archive.ph/5MSbI)". A soccer match predictor, where users can create leagues and compete against one another. I took it down temporarily and plan to revive it at some point.
3. "[Support Hero](https://github.com/abistama/support-hero)". A Slack bot that transforms a reaction in a thread into a Jira ticket. Then, it asks for a Customer Satisfaction (CSAT) at the end. It's open-source, and [I've written about it](https://world.hey.com/joaoqalves/you-can-just-open-source-things-2c1e2b77) before.
4. [ClickEdu API client](https://github.com/joaoqalves/clickedu-python-client). My daughter attends a school that utilizes this app to communicate with parents, post photos, and share other updates. The app is not intuitive, and you need to select photos one by one. I then reverse-engineered the Android app and got the API working, allowing me to obtain everything I need directly. I've open-sourced it.
5. The new [Abistama website](http://bit.ly/3J1PyHS). I wanted something simple that shows the intent of the company I'm building. We have a solid business plan: it's called building things.
6. "[Menú St Nico](https://github.com/joaoqalves/menu-stnico)". Again, at my daughter's school, there's a quarterly canteen menu. The school provides it in PDF format, along with the weeks to which the menu applies. However, I didn't find it helpful and found myself asking, "What did Helena eat today?" every day. I built a small parser for the PDF, generating a [static HTML](https://joaoqalves.github.io/menu-stnico/) file and a calendar (.ics) file so we can import it into ours. Then, I thought: what if I could get notified every day? Utilizing GitHub Actions and Telegram bots made it extremely simple to build. Bam. Nearly zero maintenance. Zero hosting and notification costs.

I've built at least three or four more projects, still in stealth mode. Considering my daily life as Head of Engineering, managing a crew of over 70 people, and being a father of two, I could not have even dreamed of building these without the heavy lift from LLMs. One final thought: when it comes to "vibe coding," I genuinely believe in the power of *100% tailored software*. Instead of bending workflows to fit generic tools, we now have the means to shape software around our unique needs and personal context.

These are my learnings, and I hope they inspire you to start building your own. What are you building?

— João
