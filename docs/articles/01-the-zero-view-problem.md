# The Zero-View Problem

### 75,442 posts in one LinkedIn dataset were liked by people who, according to LinkedIn's own numbers, never saw them

Here is a sentence that should not be possible: a post has zero recorded views and thousands of recorded likes.

You cannot like a post you never saw. LinkedIn's own view counter and like counter are supposed to describe the same event from two angles: one counts who scrolled past it, the other counts who reacted. When one says zero and the other says thousands, one of those numbers is not describing anything real.

In a dataset of 213,491 LinkedIn posts collected in 2024, this isn't a rare glitch. It happens **75,442 times**, which is 35.3% of the entire file. More than a third of the posts in this dataset show engagement that, by LinkedIn's own accounting, could not have happened the way it's displayed.

## What "zero views, nonzero likes" actually looks like

This isn't a handful of posts off by a rounding error. The pattern spans the full range of the dataset, from posts with a single like and zero views up to a post with **88,028 likes and zero recorded views**. That's a number large enough that, if it were real, it would represent one of the most-engaged posts on the platform that year, attached to a view count of nothing.

## Why this matters more than it sounds

Every one of those 75,442 posts is a signal someone else on LinkedIn sees and reacts to. A hiring manager scanning a candidate's activity, a job seeker deciding whose advice to trust, and a teenager scrolling career content at eleven at night are all reading a like count as evidence that other real people found something worth agreeing with. If more than a third of that evidence is structurally impossible, the signal itself is unreliable at a scale that's hard to write off as noise.

## What this is, and isn't

**VERIFIED**, computed directly from the dataset and reproducible by rerunning the same check: 75,442 posts (35.3% of 213,491) show `Views == 0` and `Likes > 0`.

**Not established here**: why the counts diverge this way. This repo does not claim to know the specific mechanism (whether it's a data-collection artifact, a display bug, or manufactured engagement), only that the two numbers, as recorded, contradict each other at a scale too large to be incidental. Two documented, LinkedIn-acknowledged flaws in how view and reaction data can leak or misfire are covered separately in this project's provenance notes, for readers who want the mechanism-level detail.

Full methodology and the underlying dataset documentation: **github.com/DreamITSoftware/SPOTAPOD**.

---

*Self-published. Not peer-reviewed. Every figure above is independently reproducible from the source file using the scripts published in the linked repository.*
