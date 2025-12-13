---
type: post
title: "Disasters I've seen in a microservices world"
date: "2021-04-02 15:28:31"
entry_id: 8363
canonicalURL: "https://world.hey.com/joaoqalves/disasters-i-ve-seen-in-a-microservices-world-a9137a51"
---

When Martin Fowler's post about [microservices](https://www.martinfowler.com/articles/microservices.html) came out in 2014, the teams where I worked were already building service-oriented architectures. That post and the subsequent hype made their way into almost every software team in the world. The "Netflix OSS stack" was the coolest thing back then, allowing engineers worldwide to leverage Netflix's lessons in distributed systems. More than six years later, if we look into software engineering jobs right now, most of them talk about a microservices' architecture.

**Hype Driven Development**

In the earliest part of the 2010s, many organizations were suffering challenges regarding their software development cycle. Folks working with other 50, 100 or 200 engineers struggled with development environments, heavy QA processes and programmed deployments. While Martin Fowler's "[Continuous Delivery](https://martinfowler.com/books/continuousDelivery.html)" book shed light on many of those teams, they started to realize their *majestic* monoliths were creating organizational problems for them. Hence, microservices were appealing for software engineers. It's more challenging to introduce continuous delivery or deployment in a big project rather than start with it.

So teams started spinning off three, ten, a hundred microservices. Most of them used "JSON over HTTP" — others may say RESTful 😉 — APIs for remote calls between these components. People knew well the HTTP protocol, and it seemed a relatively easy way to convert the monoliths into smaller pieces. At this point, teams started to deploy code into production in less than 15 minutes. There was no more the "Oh, team A broke the CI pipeline, and I can't deploy my code", and it felt great!

Most engineers forgot, though, that while solving an organizational problem at the software architecture's level, they also introduced a lot of complexity. The [distributed systems fallacies](https://en.wikipedia.org/wiki/Fallacies_of_distributed_computing) became more and more evident and quickly were a headache for those teams. Even for companies that were already doing client/server architectures where they already existed, this exploded in their faces once they had 10+ moving pieces in their systems.

**The reality strikes back**

Going for significant architectural changes doesn't come for free. Teams started to realize that sharing a database was a single-point-of-failure. Then, they realized that separating their domains created a whole new world: eventual consistency was a thing. What about when a service where you're pulling data off is down? The number of questions and problems started to pile up. The promises of a high-speed development pace were trumped by looking for bugs, incidents, data consistency issues, etc. Another problem was that engineers needed centralized logs and observability solutions to span across tens of services to spot and correct these defects.

**Disaster #1: too small services**

Having the ability to create new services every day came with an explosion of developer's creativity. A new feature? Bam, let's start a service! Suddenly, teams with 20 engineers were maintaining 50 services. That's more than one service per person! The problem with code, in general, is that it rots. Maintaining every service came at a cost. Imagine propagating a library upgrade across your services' fleet. Imagine that these services were started at different time points, with different architectures and some entanglement between the business logic and the frameworks used. That's *bananas*! Of course, there are ways to solve these problems. Most of them weren't available back in those days, and others cost a lot in FTEs work.

Another smell was when someone told me that deploying a new feature in service A also needed a deployment — at the same time — in service B. Or when people started to write services to generate CSVs. Why would someone introduce network hops to produce a worldwide known file format? Who would maintain that? Some teams were suffering from *servicitis*. Even worse than that, it generated a lot of friction while developing. One could not just look into a project in their IDE, but it required to have multiple projects open simultaneously to make sense of all that mess.

**Disaster #2: development environments**

I've lost count of the number of times someone approached me saying:

> Hey, João. Do you have a minute? We need to fix our development environments! People are complaining about them all the time, and this isn't working!

The problem crossed different dimensions. Mobile developers not developing a feature before it was in a development environment or backend developers who wanted to try their service didn't break any business flow. It was also problematic if someone wanted to test the whole flow in a mobile app before production.

There are several issues with development environments across distributed systems, especially at scale:

1. How much does it cost to spin 200 services in a cloud provider? Can you do it? Can you also spin up the infrastructure needed to run them?
2. How much time does it cost to do so? What if, when a mobile engineer starts to develop a feature, there's a set of services in a given version, and when they finish, there are ten new versions deployed into production?
3. What about test data? Do you have test data for all your services? Is it coherent across the fleet, so users and other entities match?
4. If you're developing a multi-tenant, multi-region application, what about configuration and feature flags? How do you stay in sync with production? What if the defaults change meanwhile?

That is the tip of the iceberg. One can think of throwing engineering power into this problem. It might work. But I'd challenge that most organizations have the scale to do it. Doing it right is astoundingly tricky and expensive.

**Disaster #3: end-to-end tests**

As you can imagine, end-to-end tests have similar problems to development environments. Before, it was relatively easy to create a new development environment using virtual machines or containers. It was also fairly simple to create a test suite using Selenium to go through business flows and assert they were working before deploying a new version. After microservices, even if we can solve all the above's problems with setting up environments, we cannot declare that a system is working anymore. At most, we can state that a system with specific versions of the services running and a given configuration is working at a particular point in time. That's a huge difference!

It was extraordinarily tough to convince people that we could not have more than a couple of these tests. And that it wasn't enough to run them in the Continuous Integration flow. They should run continuously. And they should run against production and produce alerts accordingly. I've shared countless times Cindy Sridharan's article "[Testing in production, the safe way](https://copyconstruct.medium.com/testing-in-production-the-safe-way-18ca102d0ef1)" to try to make people understand my points.

**Disaster #4: huge, shared database**

An easy way out of the monoliths while keeping data consistency across them is to keep using a shared database. It does not increase the operational load, and it makes it easy to slice a monolith step-by-step. However, it also comes with considerable disadvantages. Aside from being an obvious single-point-of-failure, defeating some of the service-oriented architecture's principles, there's more. Do you create a user per service? Do you have fine-grained permissions so service A can only read or write from specific tables? What if someone removes an index unintentionally? How do we know how many services are using different tables? What about scaling?

Disentangling all of this becomes a whole new problem on its own. Technically, it may not be trivial, considering that databases tend to outlive software. Solving the problem using data replication — be it Kafka, AWS DMS or whatever — creates a need for your engineering teams to understand database specifics and how to deal with duplicated events, and so on.

**Disaster #5: API gateways**

API Gateways are a typical pattern in service-oriented architectures. They're helpful to decouple the backend from the frontend consumers. They're also beneficial when it comes to implementing endpoint aggregation, rate-limiting or authentication across your system. More recently, the industry has been leaning towards *backend-for-frontend* architectures, where these gateways are deployed for every single frontend consumer — iOS, Android, web, or desktop apps —, making their evolution decoupled from each other.

As with everything in this world, people start to have new, creative use-cases for it. Sometimes it's a small hack to make the mobile application backwards compatible. Suddenly, you have your "API gateway" being a single-point-of-failure — because people find it easier to handle authentication in a single place — **and** with some unintended business logic inside it. Instead of having a monolith getting all of the traffic, now you have a home-made Spring Boot service getting all of it! What could go wrong? Engineers quickly realize this is a mistake, but as there are many customizations, sometimes they cannot substitute this piece for stateless, scale-friendly ones.

The culprit of the API gateways disasters comes when it consumes endpoints that are not paginated or return massive responses. Or when you make an aggregation without fallback mechanisms in place, making one single API call burn down your gateway.

**Disaster #6: Timeouts, retries, and resilience**

Distributed systems are **constantly** in a partial failure mode. What happens when service A can't contact service B? We can retry our request, right? But this promptly leads us to go down the rabbit hole. I've seen teams using circuit breakers and then increase the timeouts of an HTTP call to a service downstream. While this might be a normal reaction to buy us some time to fix the problem, it creates second-order effects. Now, all these requests that your circuit breaker would cancel because they're too long are there for more time. If there's an increase in traffic, more and more requests will get queued, leading to a worse situation than the one you wanted to fix. I've seen that engineers struggle to understand queue theory and why there are timeouts in place. The same thing happens when teams start to discuss thread pools for their HTTP clients and whatnot. While configuring those is an art in itself, setting values based on gut feeling may set you up for a significant outage.

A tricky thing when recovering from a failure is that not all of them are created equal. We may expect our consumer to be idempotent in some cases. But this means that we should proactively decide what to do in each of the failure scenarios. Is the consumer idempotent? Can I retry this call? I've seen many engineers ignoring these because it's "an edge case", to realize later they have a massive data integrity problem.

Retries are even trickier than all of this, even if you set up fallback mechanisms. Imagine that you have five million users in your mobile app and that your message bus that updates users preferences' stopped working for a while. You set up a fallback mechanism for that case, which calls the users' preferences service through an HTTP API. I guess you know where I'm going. Now, this service got a massive traffic spike suddenly, and it may not be able to cope with all the traffic. It's even worse than that: your service *might* be able to get all these new requests, but if the retries mechanism doesn't implement exponential backoff **and** jitter, you might experience a distributed denial-of-service from your mobile applications.

**Seeing all these disasters, are you still in love with distributed systems?**

What if I told you that I only wrote about a fraction of the disasters I've seen? 🤣 Distributed systems are hard to grasp, and only recently most software engineers have been consistently exposed to them.

The good thing is that many of the *disasters* I've talked about have good answers, and the industry has created better tools to make them solvable by organizations other than [FAANG](https://www.urbandictionary.com/define.php?term=FAANG).

I still love distributed systems, and I still think that microservices are a good solution for organizational problems. However, the problems come when we think about failures as "edge cases" or things that we think will never happen to us. These edge cases become the new normal at a certain scale, and we should cope with them.
