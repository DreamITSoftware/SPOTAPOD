# LinkedIn's CEO Just Admitted His Platform Has a Fakery Problem. He Was Only Talking About Half of It.

### What Dan Shapero told The Wall Street Journal, and what my own data says he left out

**What this is:** commentary and opinion, not a research finding in its
own right. It draws on this repo's VERIFIED, reproducible figures
(cited below with their evidence tier) plus one reporter's own
framing and argument, which is not independently fact-checked beyond
the underlying numbers. It sits here, separate from `docs/research/`,
because it makes an argument rather than only reporting a measurement.

On September 29, 2026, LinkedIn CEO Dan Shapero sat down with the Wall Street Journal and said something worth reading twice. Applications per job seeker on LinkedIn are up roughly 30% since the pandemic, he said, because AI now lets anyone write, tailor, and fire off a résumé in seconds. The result, in his own words, is that "it's gotten harder and harder for employers to know who can actually do the job anymore."

That is LinkedIn's own chief executive, on the record, admitting that AI-generated noise has degraded the platform's core function: helping people tell who is real. His fix is Hiring Assistant, an AI tool that now runs at a $450 million annualized revenue rate, built specifically to cut through the noise and help recruiters find who's actually qualified.

I believe him. I also think he only told half the story, and the half he left out is the one sitting in my own research.

## The noise he's fixing, and the noise he isn't

Shapero's fix is aimed at one direction of traffic: job seekers flooding recruiters with AI-assisted applications. That's a real problem, and $450 million in annualized revenue says LinkedIn agrees it's worth solving.

But there's a second direction of traffic on the same platform that nobody at LinkedIn is holding a press briefing about. It's the "career advice" content flowing the other way, from a small number of accounts toward millions of job seekers, teenagers among them, who are trying to learn what a successful career even looks like.

I analyzed two LinkedIn datasets, 213,491 posts from 2024 and 49,369 posts from 2025 into 2026, and found that a cluster of 100 accounts now produces 83.5% of everything in the second dataset that has an identifiable author. More than four in five posts in the "most-talked-about" career content on the platform trace back to a hundred accounts running the same handful of scripts on repeat.

The engagement numbers propping that content up don't hold together. In the 2024 dataset, 75,442 posts, 35.3% of the entire file, show likes recorded against zero views. You cannot like a post you never saw. One single post logged 88,028 likes on zero views. Another logged 41,315 likes on a single view, a ratio past 41,000 to 1. Among the ten single highest-liked posts in that 213,491-post dataset, four show zero recorded views.

If Shapero's employers can't tell who can do the job anymore because of AI noise on one side of the platform, the teenagers scrolling LinkedIn at eleven at night can't tell who's actually successful because of manufactured noise on the other side. Nobody built them a $450 million tool for that.

## The same industry, being honest about half its problem

I want to be precise about what I'm claiming here, because precision is the entire point of this project. Shapero's 30% application-increase figure and my zero-view like counts are not the same statistic, and I'm not presenting them as if they were. His number describes real people submitting real applications, more of them, faster, with AI's help. My numbers describe posts whose engagement could not have happened the way it's displayed. These are two different mechanisms sitting on two different surfaces of the same platform.

What they share is a cause and a shape. Both are the same underlying event: AI and automation making it cheap to generate volume, and that volume drowning out the signal a human used to be able to trust. Shapero is describing that exact failure mode when he says employers can't tell who can do the job anymore. He's just describing the version of it that costs LinkedIn's paying customers, the recruiters, money and frustration.

The version that costs LinkedIn's non-paying users, the job seekers and the teenagers studying a stranger's "success" story for a blueprint, doesn't get the same treatment. There's no Hiring Assistant for a sixteen-year-old trying to figure out if the person who says they "ran their resume through ChatGPT after 90 days of silence" ever actually existed as described, or whether that post is one of the 533 word-for-word copies of the same template running across a handful of high-volume accounts.

## LinkedIn already has the tool. It's just pointed at the customer, not the reader.

Here's the detail that makes this hard to write off as an unfair comparison. LinkedIn just told the world it built sophisticated AI, upgraded with better memory and reasoning models from OpenAI, specifically to sort real signal from AI-generated noise. That is precisely the tool needed to flag a zero-view, thousand-like post, or a headline template that's been recycled 533 times by the same content mill. LinkedIn has demonstrated, this week, that it knows how to build this. It built it to protect the side of the business that pays LinkedIn a subscription fee.

Shapero told the Journal that "now technology is helping employers give more people a proper assessment." I'd ask him directly: what technology is helping a job seeker give a career-advice post a proper assessment, before they take out a loan for the certification it's selling, or measure their own progress against a hiring story that never happened the way it's shown?

## What I am and am not saying

I am not saying Shapero's statements to the Journal are false. I have no reason to doubt that applications per job seeker are up roughly 30%, or that his team built Hiring Assistant for the reasons he described. That reporting is **STATED**, based on what Shapero told a Wall Street Journal reporter and what the Journal published, not something I independently verified myself.

I am not saying LinkedIn caused the fake engagement in my datasets, or that Podawaa, HyperClapper, or LinkBoost, the three tools my research actually profiles, are connected to anything Shapero discussed. They aren't, and his remarks don't mention any of them.

What I am saying is narrower, and I think it holds up: LinkedIn's own CEO just publicly validated the core premise of my research, that AI-driven fakery on this platform degrades people's ability to tell who's real, badly enough to justify a nine-figure product investment. He validated it for the side of the platform that pays LinkedIn directly. My data shows the same failure, arguably at a more extreme and more measurable scale, on the side of the platform that doesn't pay LinkedIn anything, the job seekers and teenagers reading career content for free. One of those gets a product launch. The other gets nothing, three years running.

## The numbers, tiered honestly

**VERIFIED**, computed directly from the raw data I can rerun: the 213,491 and 49,369 post counts, the 75,442 zero-view-like posts (35.3% of the 2024 dataset), the 88,028-likes-on-zero-views post, the 41,315-likes-on-one-view post, the 83.5% concentration in the top 100 accounts (of posts with an identified author), and the 533 word-for-word repeats of the resume-rewrite template. An earlier draft of this piece, and the document it drew from, stated these last two figures as 87% and 1,706. I re-ran the underlying counts directly against the raw source files rather than repeat the earlier numbers, and the corrected figures above are what the data actually shows. The concentration effect and the templating are both real; the specific numbers attached to them were overstated. See [authenticity-content.md](../research/authenticity-content.md) and [baseline-profile.md](../research/baseline-profile.md) for the full methodology and this correction's history.

**STATED**, reported by Shapero to the Wall Street Journal and published by the Journal, not independently re-verified by me: the 30% rise in applications per job seeker since the pandemic, the $450 million annualized revenue figure for LinkedIn's agentic hiring tools, and Shapero's own characterization of why Hiring Assistant was built.

**Not established, and not claimed here**: that LinkedIn's leadership is aware of the specific fake-engagement patterns in my datasets, that they consider it a comparable problem, or that any decision not to build a similar tool for content integrity was deliberate rather than simply a different set of priorities.

Full documentation, the dataset methodology, the regulatory analysis, and the underlying research lives at **github.com/DreamITSoftware/SPOTAPOD**.

---

*Self-published. Not peer-reviewed. The Wall Street Journal reporting referenced here is Isabelle Bousquette and Belle Lin's September 29, 2026 piece, "LinkedIn's CEO on How AI Is Reshaping Hiring," cited and quoted briefly for commentary, not reproduced. My own dataset findings are documented in full, with methodology and evidence tiers, in the SPOTAPOD repository linked above.*
