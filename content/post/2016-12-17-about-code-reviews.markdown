---
type: "post"
title:  "About code reviews"
date:   2016-12-17 10:00:00
categories:
- software craftsmanship
tags:
- code review
aliases:
  - "/software craftmanship/2016/12/17/about-code-reviews.html"
---

Code reviews are - or they should be - an important part of any software creation
process. They allow people get to know better the different code bases within
their companies. Also, they learn from others and try to understand the
reasoning, trade-offs and solutions about a somewhat complex problem. Moreover,
people strive to improve each others' code: _"Hey, we should add some tests here"_,
_"Shouldn't we use a functional interface here? It would make the code more readable"_,
and a lot more comments like these are common in such process.

I've been doing a lot of code reviews lately. I must say that I really enjoy it,
although it's a very time-consuming and exhausting task. Why? Because you may need to
change the context of your daily tasks to another different project; Then, you need
to understand a solution proposed by someone and, most important of all, give feedback
about it. If possible, you should try to find something that can be improved. The point
here it's not to be picky, but to set the bar really high within your organization.

No one achieved excellence when setting the bar low. Cristiano Ronaldo, Messi, Lewis Hamilton, 
Mohammed Ali and others didn't achieve excellence aiming for mediocrity. We should try to follow
their example. We won't be inspired every day. Sometimes we will make mistakes or we won't think 
about a better solution to a problem.  That's totally OK. Because your colleagues - your team - 
get your back covered in their code reviews. I usually say that we have two options in our career:

+ aiming for excellence;
+ everything else. This will lead us, most of the times, into mediocrity.

Of course, not all of us are Messi or Cristiano Ronaldo. I'm certainly not close to
neither of them in my area. That's fine. What really matters, at the end of the day,
is to **strive** to improve and to learn everything you can from the people 
around you. It's about attitude, not only skill.

After reviewing a lot of code, I've came up with some advice that I try to follow
every day:

1. **Be kind**. You're reviewing someone's work and, 99% of the times, people don't make mistakes
intentionally. Perhaps they were having a bad day, or couldn't come up with a better solution.
Take it easy. Ask people why they did it like that, in a polite way. Sometimes you don't
understand the trade-offs that were made. Sit down with him/her if needed;
2. **Empathize** with the faced problem. Try to use _we_ instead of _you_. Moreover, we should try
to give a good justification about the changes that we're requesting. Everyone has
its own personal opinions. Try to get to the facts and to the best practices in the industry.
You may even link people to articles, blog posts or book pages. Examples:
  + "Perhaps we could improve this method here. Using ... would allow us to ..."
  + "We should use constructor injection over the field one. The motivation behind this is...";
3. **Suggest, don't command**. People will be more enthusiastic about changing their work when you
make polite suggestions instead of commanding actions. Examples:
  + "Change this!" vs "We could probably write this in a more readable way..."
  + "This has a bug here! Fix it" vs "Perhaps I'm not understanding it correctly, but it seems
  that this code won't work properly in X and Y cases. Can we review it? If it has a bug
  we can fix it together!";
4. **Be patient**.You shouldn't expect that all of your comments end up in the code base. That's
totally OK. If you think that you are requesting too much changes or that some of them are not
that important, please refer to them as recommendations for **future** work. People will still learn
and will try to improve for the next time;
5. **Thank people** for their work. For instance, saying: _"thanks for the changes. The code looks geat. Good work!"_
motivates people to pursue the excellence even more. Everyone likes to have their effort recognized;
6. **Prepare** your code reviews. Having a check list about the important things that you are looking
at helps a lot. I have a set of pre-written comments about some common topics. In that way,
I make sure that I'm giving the best answer I know, in a consistent way to other people. Moreover,
it usually contains links and references to the best industry practices.

The list could keep going on, but I think the most relevant aspects are covered with these points.
If you look at them, they are nothing more than a derivative of politeness, education and respect
towards your pairs. A company is made of people. If you make them comfortable while trying
to push their limits, you may end up with an excellence culture and a great workplace too. Go for it,
try to improve yourself and make everyone better around you!
