---
type: "post"
title:  "There are no free meals"
date:   2016-02-20 19:00:00
categories:
- engineering
tags:
- software engineering
- libraries
aliases:
    - /engineering/2016/02/20/there-are-no-free-meals.html
---

**Bob**: "Hey, what will we use to communicate with ``X`` in this project?"

**Ted**: "We're using library ``Y``, of course! 5k stars at Github. Looks solid!"

(_5 months later..._)

**Bob**: "Ted, we have a problem. We need to update ``X`` and library ``Y`` does not have support for it."

**Ted**: "Hmmm... We could just _monkey-patch_ ``Y`` and then create our own in-house version. Problem solved!"

(_and then it begins..._)


Dear CTO/VP of Engineering / Head of Development, please do not allow your team to do these kind of things.
They are bad. They are bad for your software, for software, in general, and they will hurt your company,
sooner or later. Why? You may think that this is the quickest way to solve the above stated problem, but let's
talk about what could happen:

- ``X`` changed so much that your patch will be more like an in-house library rewriting
- You break ``Y`` in an unexpected way, because you were in such a hassle that you did not pass
the tests nor write new ones for the function that was missing
- You end-up with a mixture of library ``Y`` and your own code, because ``Y`` was missing a small
feature
- You end-up with a ``O(n^2)`` implementation of the feature you needed, because the change was
so small that the intern could just do it and create the binary himself

All of these can be heavily mitigated, if not totally, if you said to your team: "_Go to Github,
clone that project, create a branch, make a pull request and get your code reviewed_. See?
Seems easy, right? So why don't you do it? Because you think that is quickest to do the
"dirty quick-life-saver fix", but down the road things can be much worse. Remember that guy
that wrote the _monkey-patch_? Yeah, he's working for another company now. And, of course,
the library that your team patched now cannot be updated and take advantage of the new
features that were implemented. Because, now, your code is entangled with ``n+1``
_monkey-patches_ to that same library. Yeah, that sucks. So, please, stop doing it.

## Conclusions

Apart from the technical debt argument - hey, technical debt is as bad as the financial one -
you probably owe the community. Your company was only allowed to bootstrap and to quickly
develop the first features because you built it upon someone else's work. You found a bug?
You think you can improve it? The current maintainers do not have that much time and did not
implement the feature you need? Contribute back. Go to the goddamn git repository, fork it,
code it, test it and make a pull request. At the end, everyone will be happier. You'll not
end-up with your own in-house version, you will (probably) not break the library, you'll
get your code reviewed and you'll be able to update the library in the future. Cool, right? :)


