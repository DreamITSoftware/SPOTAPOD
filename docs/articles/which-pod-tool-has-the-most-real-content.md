# Which Pod Tool Has the Most "Real" Content?

### Comparing distinct-string ratios across three datasets as a rough proxy for how much of each tool's content is templated versus original

None of this project's three datasets is "real" in the sense of organic, unmanipulated LinkedIn activity. All three exist because someone used a tool designed to inflate engagement. They differ from each other in how much of their text is unique versus duplicated.

## The measure

A distinct-string ratio, the count of unique post text values divided by total post count, gives a rough sense of duplication intensity. A ratio near 1.0 means almost every post has unique text. A ratio well below that means the same or near-identical text is being reused across many records. This project's duplicate-content findings (533 identical resume-rewrite posts, a 400-author single-post cluster, and others) are specific instances of what a low distinct-string ratio looks like up close.

## Why this varies by dataset

The three datasets' underlying manipulation models differ: like-based reciprocal engagement in two of them, comment-based in the third. A tool's mechanism plausibly shapes how much original text its users need to produce. A like-based pod does not require the liking members to write anything, which leaves room for template-heavy content among the posters. A comment-based model requires participants to produce comment text, which could mean more original text (if comments are meant to look natural) or more templated text (if comment generation is automated).

## What this comparison is, and isn't, good for

It shows at a glance which tool's dataset leans more on duplicated templates and which on one-off content, without any claim about which tool is "worse" or more harmful. Duplication rate is a content-pattern signal, not a direct measure of deception or harm on its own.

## What this is, and isn't

**A comparison built on this project's previously VERIFIED duplicate-content findings**, not a new independent statistic.

Full duplicate-content research: **github.com/DreamITSoftware/SPOTAPOD**.

<!-- export65-note -->
> **Update, 22 October 2026.** In the [65 export files](../provenance.md#the-65-export-files), 5,510 of 56,363 records (9.8%) share their exact post text with at least one other record, in 1,619 groups. The same measure in the baseline profile is 28,254 of 213,491 (13.2%) in podawaa2024, 9,717 of 49,369 (19.7%) in HyperClapper and 76,532 of 77,969 (98.2%) in LinkBoost-2025. On that measure the 65 files have the lowest share of repeated text of the four. They hold 52,235 distinct post texts among 56,126 records that have text (93.1%), and the most repeated text appears in 274 records. Detail: [engagement statistics fields](../research/export-65-profile.md#engagement-statistics-fields).

---

*Self-published. Not peer-reviewed.*
