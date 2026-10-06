# How I Learned Not to Trust a Single Source

### A third-party document claimed 1,706 identical resume-rewrite posts. The real number, checked directly against the raw data, was 533.

This project verifies claims about LinkedIn engagement manipulation against raw data instead of repeating whichever number sounds most alarming. That discipline was tested early, on a statistic from someone else's work.

## The claim, and the check

A disputed third-party document asserted that 1,706 posts across the dataset used an identical resume-rewrite template. That is a specific, falsifiable number, so before repeating it anywhere in this project, it was checked directly: load the raw file, normalize the template text, count exact matches.

The actual count was **533**.

The claimed number was more than three times too high, in a document that had apparently been cited without anyone re-deriving it from source.

## What this incident teaches

The lesson is not to ignore that document. Most of what a disputed document claims can still be directionally correct even when a specific number is off, and dismissing a whole source over one bad figure is sloppy reasoning. The narrower lesson: a specific quantitative claim is only as good as the last time someone recomputed it against the source data, not the last time someone cited it.

Every number that ends up in this project's published research passes through that same check, including, as later articles in this series describe, this project's own previously published numbers.

## Why this matters

A claim gets published once, then cited, then re-cited. Each step away from the original computation is a chance for a transcription error, a stale figure, or a miscount to become "the number everyone knows." The defense is to treat every citation as a hypothesis to check and not a fact to repeat, including your own.

## What this is, and isn't

**VERIFIED**: 533 identical resume-rewrite-template posts, independently recomputed and reproducible from the raw data.

**Corrected openly**: the 1,706 figure and its correction are both documented in this project's changelog.

Full correction history: **github.com/DreamITSoftware/SPOTAPOD**.

---

*Self-published. Not peer-reviewed.*
