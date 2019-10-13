---
type: "post"
title:  "The casino paradox"
date:   2016-02-23 20:00:00
categories:
- business
tags:
- software engineering
- strategy
aliases:
    - /business/2016/02/23/the-casino-paradox.html
---

It's 2:37am and you already lost 3000$ in the casino. "_Just put 1000$ more
in this blackjack round_" - said no one, ever. This is the same feeling
I have many times in software engineering projects. I mean, yeah,
I get it, 2 years ago you **needed** to spent the minimum amount of time
possible to get the work done. That's fine. You delivered, you got customers,
everything went well.


_Fast-forward_ to 2016. Now you have 10x more customers, who are demanding
10x more and better data, because, you know, you got some competition as well.
You set-up some big data systems, added 15 small services and everything
seems to work. Except when it doesn't. Now, Bob warns Tom, every 3 days that
the piece ``X`` does not seem to work properly. After digging into 5 different
log files across 3 different servers and correlate them by hand they find out
the problem. Cool, time to fix it. It's an apparently easy-to-fix problem, so
Tom fixes it right away and deploy it. Meanwhile, it's 6pm, but who cares?
One problem less. Fantastic! Or at least it was fantastic until Bob warns him
**again**, next Monday, that it seems this system that was fixed last Friday
(and last Tuesday, and 2 weeks before, ...) it's failing. Again. Another
morning debugging. Another afternoon fixing it. The cycle repeats itself again
and again. This repetition happens because there is no time to rethink what
makes sense in that specific service, how you can improve it, how you can
roll out updates without breaking it, etc. Yeah, these fixes that you do so
often apparently break stuff that was working before. Because, you know,
there are no tests :)

I call this "The casino paradox". You throw "good money" (good work-hours)
because you already threw away a lot of "bad money" (lost work-hours). Stop
right there. Stop and think about it. It's the same case that we stated above.
You already lost 3000$ in the casino. No one would tell you to spend more
money to "recover" the money you lost before, because it's a really bad idea!
Your money is limited. So it's not a good idea to throw it away. Your team,
the amount of work that they can get done and the hours they work per day
are limited too. Think about it. Sometimes you need to stop, think about the
value that you are generating with this software and give it some perspective.
If you don't do it, you'll end-up generating frustration and not delivering
what you're supposed to the business. Then it's not about software anymore.
It's about strategy.
