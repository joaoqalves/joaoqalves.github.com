---
type: post
title: "On Hiring QA engineers"
date: "2021-04-11 10:20:52"
entry_id: 9092
canonicalURL: "https://world.hey.com/joaoqalves/on-hiring-qa-engineers-75dfa472"
---

Yet another mobile application release halted due to a critical bug. It's time to stop the rollout and push a *hotfix*. If you're lucky, you may have a *post-mortem*. Otherwise, you may hear someone directly saying: "We need to invest more in Quality Assurance (QA). Let's hire QA engineers!".

Suddenly, you have a whole QA department with 30+ folks. That is a typical reaction in companies with a track record of problems in the software they ship.

There are different QA engineers with different skill-sets:

1. The ex-tester: someone that used to run manual tests in late phases of the development process. As companies started to see the benefit of having automated tests, they pushed these folks into learning how to automate. Although their day encompasses automation, they usually lack the skills to fully understand systems end-to-end and resort to manual tests and test plans when something becomes difficult.
2. The *Automator*: usually engineers with software engineering (SWE) backgrounds or ex-testers that gained sufficient knowledge on SWE practices. Most of their day to day work is to automate test cases and set up frameworks to help other developers write them more efficiently.
3. The coach: here, we have people with lots of experience writing and testing software. Their goal is not to write tests but rather teach best practices to their colleagues and make sure there are a vision and a strategy to write tests.
4. The infrastructure expert: a developer with solid SWE skills that realized the best way to accelerate other engineers to write tests is through providing infrastructure, frameworks, or other tools that enhance their productivity. Some folks call this Engineering Productivity, Developer Experience (DevEx), etc.

There are shades of grey in these skills. Sometimes, there are people in between. Although I agree that there are some cases where extensive QA processes are helpful — e.g., healthcare, military —, I believe that hiring this kind of profiles does more harm than good if we're talking about Software-as-a-Service (SaaS) companies.

> Are you saying that QA is useless? That I shouldn't hire QA engineers?

More or less. First, let's talk about the QA process. Should we trust software engineers that don't test their software themselves? I don't think so. Then, in most companies, this means a new column in their SCRUM/Kanban boards. Now, things need to be QA'd before they go to production. When did everything get so broken that we need a particular part of the process dedicated to quality?

These QA processes also create wrong incentives all over the place. They create bottlenecks, and they send a message that only QA folks need to test things. If there's automation in place, why is there such a process? What's missing? Why don't you automate that instead? If it's automated, why is there a particular column on the board?

**Solo efforts vs multiplying effects**

A big problem I saw in different organizations is that while they agree they need this kind of QAs, they hire people who fall into the first bucket: ex-testers and automation experts. That creates two new problems. On the one hand, ex-testers don't have a deep understanding of writing software and automating things. On the other hand, automation experts usually focus on one or two technologies — e.g. Android, iOS, etc. —, which constrain the multiplier effect that companies need to get to improve their software quality.

If we talk about hiring QA engineers, my take on that is: if we're talking about coaches and infrastructure experts, go ahead. Considering the definition above, these engineers are multipliers for the rest of the organization. If you have 100 developers, I'd say that not more than 5% should dedicate their time to these activities. If you think it's not enough, maybe it's time to rethink your automation and CI/CD strategy.

**The problem of reverse coaching**

When people realize they need more of the third and fourth bucket of engineers and less of the first two ones, it may be too late. It's not easy to find experts in the market. Companies tend to avoid significant reorganizations, mainly if they affect technical roles because they're challenging to hire anyway. That, alongside the survival instinct of the first two groups, may set up your organization for a less-than-ideal state: you need coaches and experts, but the talent you have access to are no experts and, hence, they can't coach.

The natural consequence of this situation is that SWEs end up coaching QA engineers, which are supposed to be the room's experts. So, instead of a multiplying effect, we have a dividing one. People that suck up time from your organization because they don't understand modern CI/CD practices, or they don't know how modern distributed systems are impossible to test as a whole, etc. The effects on the organizations vary, but we can sum them up into:

1. First and second class citizens in the engineering departments
2. Big QA departments with their objectives and agenda
3. More processes and manual work than necessary

Again, these problems are challenging to fix. If you ignore them, they will span into engineering attrition, intricate career ladder design and progression, and frustration — due to lack of expectations and clear boundaries — on both the QA folks and your SWEs.

**Unit, integration and end-to-end tests**

Some schools of thought say that software engineers should focus on writing unit and integration tests, and QA should focus on the end-to-end critical paths. I think it is backwards. If we create silos and handovers — "Now we only miss the e2e tests, which is QA's job" —, we can't expect our business to go full speed. Then, at this point, with distributed systems all over the place, there's no room for end-to-end tests anymore. At least not the traditional ones. If the folks that write a piece of software don't know how to observe it in production, that's a big engineering problem in our teams.

**Should I hire QA engineers?**

Hire QA engineers. Not too many. Mostly SWE experts. Don't try to fix your organizational problems by throwing QA power because, in the long run, it won't cut it.

— João
