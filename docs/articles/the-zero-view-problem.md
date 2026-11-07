# The Zero-View Problem

### 75,442 posts in one LinkedIn dataset were liked by people who, according to LinkedIn's own numbers, never saw them

Some posts have zero recorded views and thousands of recorded likes. That should not be possible.

You cannot like a post you never saw. LinkedIn's view counter counts who scrolled past a post, and its like counter counts who reacted. When one says zero and the other says thousands, one of those numbers is wrong.

In a dataset of 213,491 LinkedIn posts collected in 2024, this is not a rare glitch. It happens **75,442 times**, which is 35.3% of the entire file. More than a third of the posts in this dataset show engagement that, by LinkedIn's own accounting, could not have happened as displayed.

## What "zero views, nonzero likes" looks like

This is more than a handful of posts off by a rounding error. The pattern spans the full range of the dataset, from posts with a single like and zero views up to a post with **88,028 likes and zero recorded views**. If that number were real, it would be one of the most-engaged posts on the platform that year, with a view count of zero.

## Why this matters

Every one of those 75,442 posts shows a like count that other LinkedIn users read. A hiring manager scanning a candidate's activity, a job seeker deciding whose advice to trust, and a teenager scrolling career content at eleven at night all read a like count as evidence that other real people found something worth agreeing with. If more than a third of that evidence is impossible as recorded, the signal is unreliable at a scale that is hard to write off as noise.

## What this is, and isn't

**VERIFIED**, computed directly from the dataset and reproducible by rerunning the same check: 75,442 posts (35.3% of 213,491) show `Views == 0` and `Likes > 0`.

**Not established here**: why the counts diverge this way. This repo does not claim to know the specific mechanism (whether it's a data-collection artifact, a display bug, or manufactured engagement), only that the two numbers, as recorded, contradict each other at a scale too large to be incidental. Two documented, LinkedIn-acknowledged flaws in how view and reaction data can leak or misfire are covered separately in this project's provenance notes, for readers who want the mechanism-level detail.

Full methodology and the underlying dataset documentation: **github.com/DreamITSoftware/SPOTAPOD**.

<!-- export65-note -->
> **Update, 22 October 2026.** The [65 export files](../provenance.md#the-65-export-files) carry optional fields named `statsLikes`, `statsComments` and `statsViews`. Of the 11,943 records that carry both a like count and a view count, none has zero views with likes above zero, so the zero-view pattern counted above does not appear in those fields. 1,636 of the 11,943 (13.7%) have more likes than views. The site does not document what the fields measure, and views are present on only 11,987 of the 56,363 records, so these are counts for the records that have the field and not rates for the whole file. Detail: [engagement statistics fields](../research/export-65-profile.md#engagement-statistics-fields).

---

*Self-published. Not peer-reviewed. Every figure above is independently reproducible from the source file using the scripts published in the linked repository.*
