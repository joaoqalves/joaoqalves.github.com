---
type: post
title: "Unmasking hidden value: leading Cost Centers"
date: "2023-07-18 12:17:50"
entry_id: 30330
canonicalURL: "https://world.hey.com/joaoqalves/unmasking-hidden-value-leading-cost-centers-d61daa5e"
---

Leading Product engineering, Platform, DevEx, or other internal teams is very different. One of them has high visibility with senior leadership and the executive team. They can even use the features you build! The other one often gets questioned by part of the exec team, and their leaders suffer to staff teams adequately and translate the real value their teams provide.

I've been working on a Platform team for the last three years and learned some lessons the hard way.

# Cost and profit centers

There's a classic division in the departments inside a company:

1. **Cost Centers.** A department or function within an organization that does not directly add to profit but still costs the organization money to operate. Cost centers only contribute to a company's profitability indirectly. Think about the **Accounting** or **Human Resources** departments. Both are necessary for a company to function — you can't survive without finance or hiring — but they do not bring any money.
2. **Profit Center**. These directly add to the company's profits, helping revenue generation. Think about **Sales** or **Product Engineering** by creating and selling the company's products or services to its customers.

Like it or not, Platform and DevEx teams fall into the cost center category. You can generate revenue indirectly by streamlining going to production, curating observability tools to reduce downtime, and more. But that, *per se*, does not bring a single euro more to the company.  
  
 
[![money.png](https://world.hey.com/joaoqalves/d61daa5e/representations/eyJfcmFpbHMiOnsiZGF0YSI6MTI5MzE0Mzg2NiwicHVyIjoiYmxvYl9pZCJ9fQ--24ea1eeffb9f35c5dc4238eb2b5510861bf3ca6a7c6836cb95e3d3a0e5c554e3/eyJfcmFpbHMiOnsiZGF0YSI6eyJmb3JtYXQiOiJwbmciLCJyZXNpemVfdG9fbGltaXQiOlszODQwLDI1NjBdLCJxdWFsaXR5Ijo2MCwibG9hZGVyIjp7InBhZ2UiOm51bGx9LCJjb2FsZXNjZSI6dHJ1ZX0sInB1ciI6InZhcmlhdGlvbiJ9fQ--7edc7b21f6fad97fa22412618822c4d19725431f296c7ce47dc174b61535d27c/money.png)](https://world.hey.com/joaoqalves/d61daa5e/blobs/eyJfcmFpbHMiOnsiZGF0YSI6MTI5MzE0Mzg2NiwicHVyIjoiYmxvYl9pZCJ9fQ--24ea1eeffb9f35c5dc4238eb2b5510861bf3ca6a7c6836cb95e3d3a0e5c554e3/money.png?disposition=attachment "Download money.png")

We can argue that without that help, the business would not react quickly to the market, or changes that bring real money wouldn't get deployed so frequently. The point still stands, and that's why we saw so many layoffs affecting more of these internal teams, even at places like Google, where Developer Experience is so important. Why? Because most of the platform already works. There are always things to improve, bugs to fix, and security issues, but you can do that with 1/3 of the team.

# Unmasking Platform teams' hidden value

The first thing to acknowledge is that the perceived value of these teams is, unfortunately, often inversely proportional to how well they're doing their job. When everything is running smoothly, and there are no issues, the value of Platform teams might not be immediately apparent to those outside the group. The time when the company realizes its importance is when things go wrong, and these teams are needed to fix the problems and quickly bring operations back to normal.

But there are better ways to prove value than waiting for a catastrophe. As leaders, it's essential to continuously demonstrate the value our teams bring, which involves highlighting what might not be visible to everyone in the company. A few things that worked for me:

1. **A Product mindset**. It is crucial to prioritize users' needs by focusing on direct communication, empathy, and technical expertise. However, this can be challenging in teams with very senior engineers — highly specialized individuals — who may not interact with users and develop a sense of superiority by not working on the main product but on (perceived) "cool tech stuff", resulting in over-reliance on process-driven interactions like ticketing, which can push the user's needs into the background. Encouraging team members to engage directly with users — pair program with them, see the pains in their process! — seeing and facilitating this process through regular feedback sessions and collaborative activities is critical. Treating a platform as a product means to focus on **users** needs, it has **ownership**, it **evolves** over time and it has first-class support, through **documentation**, **support**, and **self-service**. Mathew Skelton and Manuel Pais' book, [Team Topologies](https://teamtopologies.com/), is an excellent start if you want to learn more about it.
2. **Embrace integration over reinvention.** Brimming with pride in their innovative technology, Platform teams often expect product teams to adapt to entirely new workflows. However, this needs to address the practical realities faced by the latter. Product teams primarily concern themselves with immediate, top-of-mind challenges within their domain and the application of tools in their current workflows. In conversations with product teams, their adoption of specific tools often hinged on compatibility with their existing programming languages, infrastructure, or seamless integration with tools like Slack, GitHub, or Jira. It's a common pitfall for platform teams to assume that product teams would be ready to switch to an entirely new toolchain for unknown gains. This approach is generally unfeasible for most teams with established processes. Platform teams must shift their focus towards enhancing compatibility with the existing tools used by Product teams and strive for incremental steps. That implies meeting Product teams where they already are rather than expecting them to adapt to new workflows and tools.
3. **User satisfaction.** For platform teams, your users are the other departments within your company. Regularly gather feedback and work to improve satisfaction levels. High user satisfaction can indicate your team's value to the rest of the organization. One key aspect related to the above point is to give users support where they are. Avoid making them join 3+ channels and open tickets through a five-step process to engage with your team.
4. **Metrics and KPIs.** Establish clear and quantifiable metrics demonstrating your team's impact. You can base these metrics on uptime, the speed of issue resolution, or the number of successful deployments. It could also relate to cost savings or impact on the [DORA metrics](https://cloud.google.com/blog/products/devops-sre/using-the-four-keys-to-measure-your-devops-performance).
5. **Communicate successes.** You need more than just your team to know their accomplishments. Others in the organization should be aware too. Communicate about the significant improvements your team has implemented, the efficiency gains, and any potential disasters your team avoided, thanks to proactive measures.

# 

# Is it enough?

The journey of leading Platform, DevEx, and other internal teams can be challenging, often marked by complexities and pitfalls. Despite being categorized as cost centers, these teams play an indispensable role in a company's operations, and their value usually goes underappreciated.

Through the lessons I've learned, a user-centric approach, seamless integration with existing workflows, continuous feedback, and effective communication of our successes are pivotal in elucidating our teams' real value. We don't just keep the cogs turning behind the scenes; we are the backbone that enables the company to run smoothly and adapt quickly to market changes.

These learnings are not a way to avoid layoffs in cost centers like Platform teams. However, if you can prove to your organization that you deliver real value for the teams that build on top, they may think twice before making cuts.

Have you faced similar challenges in your organization? How do you demonstrate the value of your teams?  
  
If you enjoyed this article, consider subscribing to the newsletter and [**buying me a coffee**](https://bit.ly/buy-me-a-coffee-joaoqalves).

— João
