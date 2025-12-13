---
type: post
title: "Internal Platforms"
date: "2021-04-19 13:24:56"
entry_id: 9757
canonicalURL: "https://world.hey.com/joaoqalves/internal-platforms-a1d1f2ef"
---

During the early 2010s, I was in college, and everyone in Hackernews was talking about two technologies: Ruby-on-Rails (RoR) and Heroku. I was lucky enough to have forward-thinking Professors. In most practical assignments, they didn't put constraints on languages or frameworks we could use. That allowed us to explore *git*, RoR, use Trello and Asana for project management, and much more.

In one of these assignments, I discovered Heroku. It felt magic! I could just type *git push origin heroku*, and bam, there it was! My website was live, and I could even spin up a database to store any data I needed. Before, I played with setting up a deployment system using NginX, Passenger, Capistrano, etc. Heroku's simplicity and *serverless* — yes, it **is** serverless! — paradigm made me realize the true power of platforms. All the hours setting up a server, installing and configuring reverse proxies, were now gone. That allowed me to focus on what I really cared about: writing my goddamn application and make sure it was ready to receive traffic and handle users' requests.

**The cloud, microservices, and DevOps**

The cloud was also exploding, and Amazon Web Services (AWS) took a big lead. Every year, at Re:Invent, they were adding more, better, faster, and cheaper services. That was also a significant change to sysadmins. Some of them were already using configuration management services such as Chef. However, the cloud made it possible to go one step forward: treating (compute) infrastructure as cattle, not pets. Simultaneously, the DevOps movement was getting traction. The barriers between sysadmins and developers got more and more diffuse. Together with the rise of service-oriented architectures, it pushed developers to set up their caches, databases, message queues, and so forth.

DevOps practices, paired with a vast cloud world, created tons of new challenges for infrastructure engineers. These folks soon realized that things started to derail if they didn't use an Infrastructure as Code (IaC) approach.

Sometimes, team A would set up all its databases in a single [availability zone](https://aws.amazon.com/about-aws/global-infrastructure/regions_az/), or team B would forget to tick the backups box. What started as empowerment quickly led to drifts in how teams were doing things, specifically at big companies. Atop, as services offered by AWS exploded, they also came with lots of cognitive-load that crews needed to cope with. It became clear that companies needed to standardize some of their infrastructure practices at scale.

**The first attempt: shared modules**

If we can define infrastructure as code, why can't we leverage software-alike structures for managing it at scale? That's what many companies did! CloudFormation templates, Terraform modules, and more. That eliminated drift in how different teams set up databases. Furthermore, it enabled sensible defaults across cloud resources. If we wanted to use a newer generation of EC2 instances, it was a matter of opening a Pull Request to our modules repository, and new services and deployments would use it right away.

Not all changes were easy, though. If we wanted to add or remove tags, IAM roles, or leverage a new type of instance in all the current services, it was challenging. It required intervention from each team, reviewing the changes in the upstream module and making sure it wouldn't break anything in their infrastructure. Now, multiply this effort for 30 teams that maintain 50 services. It piles up fast!

Another nightmare for engineering teams is migrations. Everyone *loves* them, right? When we debate moving from system A to system B, I can sense eyes rolling from engineers to CEOs. Migrations don't deliver value; they're not sexy, and they are often a Sisyphean task to accomplish. Imagine that you had to migrate from Datadog to Prometheus/Grafana. You can start imagining all those modules you have as code: metrics sending, instance tagging, dashboards as code, etc., need to be replaced. Again, you can multiply it by the number of teams, services, pieces of infrastructure, and the like.

When it comes to tooling, teams usually face governance, maintenance, and vision problems. Who builds them? Who maintains them? Is this new tool I'm creating aligned with the rest we have in the company? How can I make sure of that?

One last problem is that the specific needs sometimes result in a fork of the shared modules. If an "internal open-source" (IOSS) culture doesn't exist, this can lead to a problem where these modules are useless because everyone did customizations that they didn't port upstream.

**Platforms as a Service: a multiplier effect**

If shared modules scale poorly and rely on a solid IOSS culture to last, is there any alternative? From [Zalando](https://www.youtube.com/playlist?list=PLwc0Zy9e8diy0f5zT-Q1bk69FRBtiYFgG) to [HubSpot](https://product.hubspot.com/blog/how-we-designed-a-reporting-platform) or [Adevinta](https://medium.com/adevinta-tech-blog/how-we-rolled-out-our-kubernetes-platform-in-adevinta-spain-63495884a1db), many organizations started a path towards an internal Platform-as-a-Service (PaaS).

The idea behind a PaaS is to:

1. **Reduce cognitive load** in the product teams, making them focused on delivering value to the final user.
2. Provide a cohesive set of tools that help **increase engineers' productivity**. How can we make sure that these folks have 80% of what they need daily, out-of-the-box?
3. Benefit from **economies of scale**. If we can reduce computing spending by 10% through the platform without any intervention from our engineering teams, that's a massive gain.
4. **Ease migration paths**. Over the last decade, we've seen a fast transition in how people deploy applications: VMs on-premise -> EC2 AMIs -> Containers. It won't stop here. There are already novel models — such as [KNative](https://knative.dev/) or [Dapr](https://dapr.io/) — that allow users to get a *serverless* experience. How can we ease the migration so teams don't need to reinvent the wheel in every part of the company?

Some folks are skeptical about this kind of platform because they abstract stuff away from engineers. In some sense, it may be a new *developer vs. operations* division. I think, however, that's not the case. One of the most significant issues with modern software development is that they're many moving pieces. Keeping the cognitive load at an acceptable level is a requirement for teams to succeed.

I knew something about setting up infrastructure, but I was still blown away by Heroku back in the day. Considering how efficient — I mean, software development-wise, and not the total lead time — big companies like Amazon, Google, *et al*., it's critical to provide tools that make your engineers productive from the very first day. That happens so frequently that engineers from the FAANGs have a hard time joining startups or companies where CI/CD, code search, or build caching tools are not on par with what they used to have. There's even a [Github repository](https://github.com/jhuangtw/xg2xg) with open-source alternatives to Google's internal tooling.

Fortunately, during the last few years, a lot of venture capital was dedicated to Software as a Service (SaaS) in the developers' experience (DevEx) space. Engineering teams can integrate with those instead of building it themselves. However, without proper *glue*, it's not trivial to create a cohesive ecosystem end-to-end.

Other people claim that these internal platforms are like Object Relational Mapping (ORM) frameworks. In theory, they are good because you can abstract away from the SQL engine where you're running. In practice, though, not many people change their database engines. It's worse than that: most of the time, before engineers realize, they're using a specific feature from a database, and migrating away becomes more difficult.

In my experience, I believe the ORM example is not an accurate analogy. Over the last ten years, the computing model changed significantly from VMs to Functions. People started moving away from their monoliths towards microservices. The storage engines kept similar. Yes, maybe teams are now using tens of PostgreSQL instances rather than a big Oracle one. Some folks moved workloads to No-SQL databases, and now they leverage more in-memory systems for performance purposes. So, during recent years, the application layers got re-architected much more often than the persistence ones. That's where the analogy breaks. Although I've seen two or three systems migrating away from a relational database engine to another, I've seen many more systems being re-written and deployed in newer paradigms.

I've also seen many financial-led projects where teams needed to migrate from a metrics or logging solution to another. These projects are way more common than changing databases. So the value-added of connecting them to an internal platform is higher.

**Is Kubernetes my PaaS?**

When I talk to people, they tend to think that Kubernetes is their PaaS. I don't think so. Manuel Pais ([Team Topologies](https://teamtopologies.com/)) wrote a spot-on [article](https://www.infoq.com/articles/kubernetes-successful-adoption-foundation/) about it. One of my preferred parts of it is:

> The key idea of this talk is that Kubernetes, by itself, is not a platform. It's the foundation. It's awesome, brings us all this great functionality, autoscaling, self-healing, service discovery, you name it. A good product is more than that. You need to think about the usability, how they make this easy to use and adopt, think about the reliability, the support around the platform. It's the foundation. It's not the whole thing.

While we could consider Kubernetes (K8s) the GNU/Linux of distributed systems, it isn't a platform on its own. Its complexity is too high to make it palatable for most product — or *stream-aligned* — teams. Even cloud providers think that K8s is too complex, and they're starting offering easier-to-reason systems such as [Google Cloud Run](https://cloud.google.com/run/).

To truly unlock K8s potential in your organization, I believe that it should be paired with a good developer experience. Did you think all these YAML manifests and configurations are developer-friendly? I don't think so!

Spotify and others realized this a while ago. They've created frameworks — e.g., [Backstage](https://github.com/backstage/backstage) or [Clutch](https://github.com/lyft/clutch) — to share back with the world an extensible way to build internal portals. These companies realized that change is inevitable and that having good *discoverability* is key to their internal platforms' success.

Aside from the user experience, there are more questions that pop up when we talk about platforms: how do we report costs? How can different teams build atop what currently exists? Answering these and other similar questions is what makes the platforms widely adopted in big corporations.

**Should I build my own Internal Platform?**

I think that most small and medium businesses I know would be better off using something like Heroku. Building an internal platform is not the goal of 99.9% of the companies out there. However, at a certain scale, if there isn't *something* that reduces the cognitive load in stream-aligned teams, the cost of not having a PaaS — built or bought — adds up.

In the next decade, I think that Github, Gitlab, and others will invest more and more in making their experience integrated end-to-end. That will make PaaS affordable to more companies, and there will be pressure to standardize components and integrations — data stores, event consuming, observability, etc. — so the competitive advantage of having a platform will start to transfer to other domains such as deriving infrastructure from applications' code. That was an ambitious goal from [Darklang](https://darklang.com/), and I think it will become true in the future.

However, internal platforms are more than the tools they put together. If we think that every service we spin up needs [Service Level Indicators/Objectives](https://sre.google/sre-book/service-level-objectives/), wouldn't it be awesome to provide those by default in our observability stack? Even send alerts to the team's preferred channels! How cool would it be to map 1:1 every use case to the unit cost in terms of application consumption and infrastructure? The possibilities are endless.

In the end, building internal platforms must have a clear goal: to make your business more efficient. To allow your company to make more money. If you think you could benefit from economies of scale, go for it! If you're about to make your engineers write YAML and understand Kubernetes from the ground up, let the industry take care of the problem.

— João
