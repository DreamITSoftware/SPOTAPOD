# How I Learned Not to Trust a Single Source

### A third-party document claimed 1,706 identical resume-rewrite posts. The real number, checked directly against the raw data, was 533.

This project exists to verify claims about LinkedIn engagement manipulation against raw data rather than repeating whatever number sounds most alarming. That discipline got tested early, on a statistic that came from someone else's work.

## The claim, and the check

A disputed third-party document asserted that 1,706 posts across the dataset used an identical resume-rewrite template. That's a specific, falsifiable number, so before repeating it anywhere in this project, it got checked directly: load the raw file, normalize the template text, count exact matches.

The actual count was **533**.

Not close. Not a rounding difference. It's a number more than three times too high, sitting in a document that had apparently been cited without anyone re-deriving it from source.

## What this incident actually teaches

It's not "that document was wrong, so ignore it." Most of what a disputed document claims can still be directionally correct even when a specific number is off, and dismissing a whole source over one bad figure is its own kind of sloppy reasoning. The lesson is narrower and more useful: a specific quantitative claim is only as good as the last time someone actually recomputed it against the source data, not the last time someone cited it.

Every number that ends up in this project's published research passes through that same check, including, as later articles in this series describe, this project's own previously published numbers.

## Why this matters more than it sounds like it should

Numbers travel. A claim gets published once, then cited, then re-cited, and each hop away from the original computation is a chance for a transcription error, a stale figure, or an outright miscount to calcify into "the number everyone knows." The only defense is treating every citation as a hypothesis to check, not a fact to repeat, including your own.

## What this is, and isn't

**VERIFIED**: 533 identical resume-rewrite-template posts, independently recomputed and reproducible from the raw data.

**Corrected, not concealed**: the 1,706 figure and its correction are both documented in this project's changelog, not quietly dropped.

Full correction history: **github.com/DreamITSoftware/SPOTAPOD**.

---

*Self-published. Not peer-reviewed.*
