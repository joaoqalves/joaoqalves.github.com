---
type: post
title: "I could build this during the weekend"
date: "2021-05-02 08:45:05"
entry_id: 10747
canonicalURL: "https://world.hey.com/joaoqalves/i-could-build-this-during-the-weekend-aa093c5e"
---

Every time people buy a new house, car, or TV, they say lovely things first. It's the honeymoon phase. Then, they realize their expensive, fancy stuff has flaws too. Engineers tend to take it one step further. We enter *solution mode* and start thinking about solutions for those flaws and how we'd design those items. We are so intelligent. We'd make it better, wouldn't we?

However, when we do this kind of analysis, we may miss the context. Maybe the folks responsible for the design had constraints. It can be a tight timeline, low-quality, or too-expensive materials. Sometimes, it's a waterfall process, and it's too late or too expensive to fix it. We often ignore how most people prefer to have something that works rather than something perfect. There are plenty of reasons why some things are flawed or, at least, they *look* one order of magnitude more complicated than they should be. I still remember when Andrew Houston submitted Dropbox on Hackernews. The first and most [infamous comment](https://news.ycombinator.com/item?id=8863) read like this:

> I have a few qualms with this app:  
>   
> 1. For a Linux user, you can already build such a system yourself quite trivially by getting an FTP account, mounting it locally with *curlftpfs*, and then using SVN or CVS on the mounted filesystem. From Windows or Mac, this FTP account could be accessed through built-in software.  
> 2. It doesn't actually replace a USB drive. Most people I know e-mail files to themselves or host them somewhere online to be able to perform presentations, but they still carry a USB drive in case there are connectivity problems. This does not solve the connectivity issue.  
> 3. It does not seem very "viral" or income-generating. I know this is premature at this point, but without charging users for the service, is it reasonable to expect to make money off of this?

Someone suggested installing a file synchronization app that *just worked* was similar to setting up our FTP server and dealing with all the complexity around that. To me, it's the perfect example of a lack of second-order thinking. We focus too much on the happy path that we forget about the long-tail of complex problems solved. Or we miss the point, not realizing that a solution is democratizing things that only a few folks could solve more or less efficiently.

**Why does Uber need 100 mobile developers?**

I've never worked for Uber, but I did for a competitor. We tend to think that things are simple because we see them that way. If we want to get a ride home, all we see is a ride-hailing app that works. We choose the type of ride. Then, the driver comes, and they can even phone us or send us a message. At the end of the journey, we pay and call it a day. Some apps even allow for splitting the bill between the passengers.

So, why in the hell does Uber need hundreds of mobile developers? Ride-hailing disrupted the taxi industry. Like all the disruptions in software as a service (SaaS), they addressed a local problem and came up with a global, scalable solution. There's one big difference from other SaaS cases, though. Most of the cities in the world had a (strict) regulation for taxis. So, companies needed to go hyper-local. They were required to adapt their applications and business to every country, city, and even to specific use-cases, like train stations and airports.

So what? That's all a backend configuration, one could say. In some cases, it's that. Now, imagine that some cities require a virtual queue for riders at the airport. This new requirement creates a set of new problems to handle. How do we announce it to the drivers? How do we show them their position in the queue? What about geofencing? What if the driver's GPS disconnects for a while and they were second in the line? Are they placed at the end?

A big chunk of all of that happens in the backend. Nevertheless, suddenly we have a lot of work in the apps to cover only this use-case. Now, multiply that by tens of regulations across the world. And then consider that Uber and others have global apps. You install the app in Caminha, and then you can use it when you visit Kuala Lumpur. It's part of the promise of solving mobility across the globe.

Not all the features are available everywhere. When summing all the features, A/B testing, User Interfaces, Payments, etc., we can see this requires a lot of engineering power. Mainly because hiring people doesn't solve immediatly the problems of building apps at scale. In the backend, we have microservices and straightforward ways on how to separate bounded contexts. How to do it in mobile apps, packaged as a single binary? Uber has an [excellent story](https://twitter.com/StanTwinB/status/1336890442768547845?s=20) around binary size optimization.

So, one of the most challenging parts of the problem is to allow hundreds of engineers to collaborate effectively and build a single app. Be it separating the apps into modules, creating and testing release trains, and so forth. In his "[Mobile at Scale](https://t.co/boK0ki0Vpa?amp=1)" book, Gergely Orosz talks about all these challenges. It's *bananas*! That's how Uber and other big companies end up with hundreds of mobile developers.

We could say similar things about other SaaS. When I joined [InfoJobs](https://www.infojobs.net/), I thought there wasn't much need for complexity. A job board for candidates and a way for companies to advertise their offers. Then, I realized there were many actors involved. Some companies want to use their ERPs to post. Hence, we needed a REST (or SOAP) API. Big companies also have sub-companies and departments. They have substantial Human Resources departments, so they need Role-Based Access Control. The list went on, and I was amazed every time I spoke to someone that knew about the business.

**I hate my company's Platform/Infrastructure team**

Platform teams are on the rise in the software engineering industry. While they seek efficiency, they sometimes upset engineers in product-driven teams. I've heard many times people asking questions like:

> Why are we not using X technology instead of Y? It would be way easier.

> Z is not what the cool kids are doing these days. Why are we stuck using it? I could build a better version of this during the weekend!

Aside from the technical debt and legacy code, there are many reasons why that happens. These teams are responsible for a *Platform* or *Infrastructure*. Engineers expect them to work flawlessly. Likewise, most people expect to cross a bridge or drive home without problems because they trust that *infrastructure*. It's one of those things that you only notice when they break and make us suffer. Virtually no one praises them when everything works as expected.

That responsibility comes with inevitable trade-offs. We may not get the hottest technology, trading it off for a battle-tested, boring, secure, and pervasive across the company one. Even when some folks insist on trying something new, they quickly realize they need to care for everything they get for *free* in their *Platform* — logging, metrics, single sign-on, libraries, etc. Engineers start seeing the invisible cost of supporting new technologies — especially if they're niche — inside the organization.

It's easy to oversimplify problems and try new, leaner technologies that optimize for our use cases. However, when scaling it to the rest of the organization, we start to see the dragons. People that didn't build their software *the right way*. Entire tech stacks depending on libraries that teams can't update due to *reasons™*. Quickly, we start realizing that our lean way of doing things may not serve most situations.

**Second-order thinking**

The world is messy. As software is more ubiquitous, we're encoding this chaos in 1's and 0's. It's more than that. Some scenarios are more difficult to encode in software than their pre-digital counterparts. A physical taxi queue at the airport is quite simple to understand. There's no GPS technology involved, no geofencing. A person and a car can only be in one place at a time. In the digital world, things get messier.

When going into solution mode, we should try to understand the context and think about second-order factors that can lead to a suboptimal state. Maybe we can't build that app on the weekend, after all.

— João
