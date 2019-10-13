---
type: "post"
title:  "Towards Continuous Deployment"
date:   2015-10-14 21:25:07
categories:
- engineering
tags:
- software engineering
- methodology
- continuous integration
- continuous deployment
aliases:
    - /engineering/2015/10/14/towards-continuous-deployment.html
---
Hi! This is my first post in this blog. Although it's meant to be a tech blog, this post is the first part of a series
where I mix software engineering, its practices and methodologies with a business background and why do software
companies need to move towards continuous deployment. Stay tunned!

## Background and Motivation

The world has changed a lot in the last 100 years. But if we stop to think about it, did it change more from
1900 until 1970 or from 1970 until now? Perhaps we could define the world evolution as an exponential function.
Everyday we use the technology we know and innovate, creating new technology based upon the old one. This evolution
pace is becoming faster and faster. It's like the Moore's Law applied in real life. Crazy. Given this, every
(decent) businessman knows that his company needs to adapt fast to market changes. If you cannot deliver, your
competitor in Australia, China, India, etc will do. If you cannot change fast enough, your competitors will eat you.

With all the technological boom that happened in the last 10-20 years, people should stop saying that software will
eat the world. Software has already eaten it. We live in a world where everything is manufactured, controlled or
served -_\* as a service_ - by software. I think that we could even use a _motto_ to describe the days we're
living in: "Automate... or be automated". I will not discuss if this is a bad or good thing, but let's think about
what are the business-side implications of a world dominated by software.

From a technical perspective - _finally_! - this "new" need to adapt, react, build and fix faster than your
competitors and deliver good software to your customer brings a lot of challenges to the industry:

+ We're a global company, how do we **scale** our software to millions of requests / second?
+ We need to act fast. How can we **distribute** our new software _as soon as possible_?
+ But we also need to be assured that **it works as expected**. Without loosing our focus in acting fast. How?
+ Perhaps these requirements will make my software **team** _slower_. What should I do?

Given these challenges, how can we transmit to business the need to be prepared to change fast? How can we
communicate that the work we do - the _invisible_ one - will (is) allow(ing) our company to respond in a quicker
way to new business requirements? I think every software company that grows to a certain point has this challenge.
Below, I explain my thoughts about it and how I think a *team* could try to solve it. The word *team* is very
important here: if you're expecting to change everything on your own, you'll fail 99% of the attempts. You can
evangelize, you can advise, you can discuss, but in the end, what matters is what the team as whole thinks and
what works for you. Remember: there's no silver bullet.

## Assumptions

I'm assuming here that you're familiar with agile methodologies (mainly _scrum_), software engineering and
continuous integration tools.

## High-level goals

+ Have fast-paced software deployment. Code, Review, Build, Deploy.
+ Fail fast, fix faster.
+ ... but reduce the number of bugs.
+ Give visibility about your work to other teams and management.

## How

+ Every new feature (that is not just a small script) must have unit tests
+ Every project must have a dependency manager (pip, maven, etc)
+ Every project must be deployed through a Continuous Integration platform (Jenkins, etc)
+ Every project must have code quality metrics:
  * code coverage. What is the % of your code that is covered by tests?
  * technical debt (repeated / dead / bad code)
  * code style (PEP8 for Python, Google Java style-guide, etc)
  * any other metrics that your team find relevant
+ Every project must have a ``README`` file that any new developer can read and, at least, set-up his machine.
+ Automate. Automate. Automate. If your team members spend 1h each week performing the same task, you must
automate. If your developers SSH into a machine to perform the same task, 5 minutes a day, you must automate.
+ Share the knowledge. Have a curated _wiki_, ``README`` files, and host in-house tech talks. Ideally, anyone
should be able to perform any task, in a small team.
+ Build or buy internal tools. Scripts that create a ``changelog``, send emails to your and other teams after a
deploy, moving tasks from ``open`` into ``Q&A`` when a _pull_ request is created, etc.

### Visibility and Communication

If you do a lot of work each week and your colleagues and management can't see it or you can't explain the added
value of your team's work regarding business goals, that is not right. Here I'm using the word visibility to show
the relationship between your team and other teams and management. Although internal visibility is important as well,
we are focus in communicating outside the team here. These are my thoughts:

+ if you have any team that heavily uses your own software, you should work seamlessly with them. They upload,
track, analyze and interact with the platforms you maintain more than anyone else. They are your #1 customer.
Communicate with them avoids misunderstandings, interruptions, bug-fixes and low productivity.
+ your team must be pro-active. Communicate relevant changes, each _sprint_, to all the people in the company.
You could write a brief summary of the changes and focus on the benefits that these changes bring to the company
as a whole. Then, you could attach the ``changelog`` of the whole _sprint_ so anyone can read it.
+ Have a decent and, global and ubiquitous communication channel. There are still many companies that use IRC.
IRC sucks. You can’t have IRC on your mobile phone. You can’t paste code in IRC. You can’t share a file in IRC.
You need to make my own automation tools in IRC. Your marketing does not use IRC. Your sales guys don’t use IRC.
You can't have a chat with them without sharing your personal email and/or Skype accounts. Or worse, create specific account just to communicate with the guys that work with you. How silly is that? Moreover, why can’t you facilitate everyone’s life and have a centralized chat where everyone can communicate and have dedicated channels to receive
alerts and automatic messages, instead of polluting our emails? C'mon, Slack, Hipchat, Mattermost... You don't
have an excuse.

## Conclusions

In this post I started by giving some context about how the business evolved in the last couple of years and the
impact of this evolution in software development teams. Then I stated the high-level goals when implementing
continuous deployment systems and I started to answer how to achieve them. In the next posts, I'll focus more
on scaling, team procedures, documentation, architecture and more. As a first conclusion, I think that alongside
with the right tools and processes to develop software - which is important! - you must be able to communicate
effectively both internally as a team and "externally" to other departments and stakeholders within your company.
