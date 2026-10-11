# LinkedIn's CEO Admitted His Platform Has a Fakery Problem. He Described Only Half of It.

### What Dan Shapero told The Wall Street Journal, and what my own data says he left out

**What this is:** commentary and opinion, not a research finding in its
own right. It draws on this repo's VERIFIED, reproducible figures
(cited below with their evidence tier) plus one reporter's own
framing and argument, which is not independently fact-checked beyond
the underlying numbers. It sits here, separate from `docs/research/`,
because it makes an argument rather than only reporting a measurement.

On September 29, 2026, LinkedIn CEO Dan Shapero sat down with the Wall Street Journal and said that applications per job seeker on LinkedIn are up roughly 30% since the pandemic, because AI now lets anyone write, tailor, and fire off a résumé in seconds. The result, in his own words, is that "it's gotten harder and harder for employers to know who can actually do the job anymore."

LinkedIn's own chief executive said on the record that AI-generated noise has degraded the platform's core function: helping people tell who is real. His fix is Hiring Assistant, an AI tool that now runs at a $450 million annualized revenue rate, built to help recruiters find who is actually qualified.

I believe him. I also think he described only half the problem, and the other half is in my own research.

## The noise he is fixing, and the noise he is not

Shapero's fix is aimed at one direction of traffic: job seekers flooding recruiters with AI-assisted applications. That is a real problem, and $450 million in annualized revenue shows LinkedIn thinks it is worth solving.

There is a second direction of traffic on the same platform that LinkedIn has not held a press briefing about: "career advice" content flowing the other way, from a small number of accounts toward millions of job seekers, teenagers among them, who are trying to learn what a successful career even looks like.

I analyzed two LinkedIn datasets, 213,491 posts from 2024 and 49,369 posts from 2025 into 2026, and found that 100 accounts produce 83.5% of everything in the second dataset that has an identifiable author.

More than four in five posts in the "most-talked-about" career content trace back to a hundred accounts running the same handful of scripts on repeat.

The engagement numbers behind that content do not hold together. In the 2024 dataset, 75,442 posts, 35.3% of the entire file, show likes recorded against zero views. You cannot like a post you never saw. One post logged 88,028 likes on zero views. Another logged 41,315 likes on a single view, a ratio past 41,000 to 1. Among the ten highest-liked posts in that 213,491-post dataset, four show zero recorded views.

Employers cannot tell who can do the job because of AI noise on one side of the platform. Teenagers scrolling LinkedIn at eleven at night cannot tell who is actually successful because of manufactured noise on the other side. Nobody built them a $450 million tool for that.

## The same industry, being honest about half its problem

I want to be precise about what I am claiming. Shapero's 30% application-increase figure and my zero-view like counts are different statistics, and I am not presenting them as the same. His number describes real people submitting more applications, faster, with AI's help. My numbers describe posts whose engagement could not have happened the way it is displayed. They are two different mechanisms on two different parts of the same platform.

They share a cause: AI and automation make it cheap to generate volume, and that volume drowns out the signal a human used to be able to trust. Shapero describes that failure when he says employers cannot tell who can do the job. He describes the version that costs LinkedIn's paying customers, the recruiters, money and frustration.

The version that affects LinkedIn's non-paying users, the job seekers and the teenagers studying a stranger's "success" story for a blueprint, gets no comparable tool. There is no Hiring Assistant for a sixteen-year-old trying to work out whether the person who says they "ran their resume through ChatGPT after 90 days of silence" ever actually existed as described, or whether that post is one of the 533 word-for-word copies of the same template running across a handful of high-volume accounts.

## LinkedIn already has the tool, and it points at the customer, not the reader

LinkedIn recently announced AI, upgraded with better memory and reasoning models from OpenAI, built to sort real signal from AI-generated noise. That is the kind of tool needed to flag a zero-view, thousand-like post, or a headline template recycled 533 times by the same content mill. LinkedIn has shown this week that it knows how to build one. It built it to protect the side of the business that pays a subscription fee.

Shapero told the Journal that "now technology is helping employers give more people a proper assessment." I would ask him directly: what technology helps a job seeker give a career-advice post a proper assessment, before they take out a loan for the certification it sells, or measure their own progress against a hiring story that never happened the way it is shown?

## What I am and am not saying

I am not saying Shapero's statements to the Journal are false. I have no reason to doubt that applications per job seeker are up roughly 30%, or that his team built Hiring Assistant for the reasons he described. That reporting is **STATED**: it rests on what Shapero told a Wall Street Journal reporter and what the Journal published, and I did not verify it independently.

I am not saying LinkedIn caused the fake engagement in my datasets, or that Podawaa, HyperClapper, or LinkBoost, the three tools my research actually profiles, are connected to anything Shapero discussed. I have no evidence they are, and his remarks do not mention any of them.

What I am saying is narrower: LinkedIn's own CEO publicly acknowledged the core premise of my research, that AI-driven fakery on this platform degrades people's ability to tell who is real, enough to justify a nine-figure product investment. He did so for the side of the platform that pays LinkedIn directly. My data shows the same failure, at what I would argue is a more extreme and more measurable scale, on the side that pays LinkedIn nothing, the job seekers and teenagers reading career content for free. One side got a product launch. The other has got nothing, three years running.

## The numbers, by evidence tier

**VERIFIED**, computed directly from the raw data I can rerun: the 213,491 and 49,369 post counts, the 75,442 zero-view-like posts (35.3% of the 2024 dataset), the 88,028-likes-on-zero-views post, the 41,315-likes-on-one-view post, the 83.5% concentration in the top 100 accounts (of posts with an identified author), and the 533 word-for-word repeats of the resume-rewrite template. An earlier draft of this piece, and the document it drew from, stated these last two figures as 87% and 1,706. I re-ran the underlying counts against the raw source files rather than repeat the earlier numbers, and the corrected figures above are what the data shows. The concentration effect and the templating are both real, but the specific numbers attached to them were overstated. See [authenticity-content.md](../research/authenticity-content.md) and [baseline-profile.md](../research/baseline-profile.md) for the full methodology and this correction's history.

**STATED**, reported by Shapero to the Wall Street Journal and published by the Journal, not independently re-verified by me: the 30% rise in applications per job seeker since the pandemic, the $450 million annualized revenue figure for LinkedIn's agentic hiring tools, and Shapero's own characterization of why Hiring Assistant was built.

**Not established, and not claimed here**: that LinkedIn's leadership is aware of the specific fake-engagement patterns in my datasets, that they consider it a comparable problem, or that any decision not to build a similar tool for content integrity was deliberate rather than simply a different set of priorities.

Full documentation, the dataset methodology, the regulatory analysis, and the underlying research are at **github.com/DreamITSoftware/SPOTAPOD**.

---

*Self-published. Not peer-reviewed. The Wall Street Journal reporting referenced here is Isabelle Bousquette and Belle Lin's September 29, 2026 piece, "LinkedIn's CEO on How AI Is Reshaping Hiring," cited and quoted briefly for commentary, not reproduced. My own dataset findings are documented in full, with methodology and evidence tiers, in the SPOTAPOD repository linked above.*
