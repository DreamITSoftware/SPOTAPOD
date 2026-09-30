# LinkBoost's Different Universe: Comment-Based vs. Like-Based Manipulation

### Most engagement-pod research, including most of this project's own, focuses on inflated likes. LinkBoost inflates something else entirely.

podawaa and HyperClapper both fit the pattern most people picture when they hear "engagement pod": coordinated reciprocal liking. LinkBoost's dataset describes a structurally different mechanism, and comparing the two models side by side reveals things a single-model view would miss.

## The mechanism difference

Like-based pods (podawaa, HyperClapper) coordinate members to like each other's posts, inflating a single, simple metric. LinkBoost's data reflects a comment-based manipulation model, inflating comment counts and comment-driven visibility rather than raw likes. That's a meaningfully different manipulation surface. A fabricated comment can carry actual, if inauthentic, text content, in a way a fabricated like cannot, which changes both what an anomaly looks like in the data and what it would take to detect.

## Why this matters for detection generally

A detection approach tuned to catch like-based anomalies, unusually high like-to-view ratios, zero-view-with-high-likes patterns, would likely miss comment-based manipulation entirely, because it's looking at the wrong metric. This project's own zero-view-anomaly analysis, one of its most-cited findings, is specifically a like-based-manipulation signal. It says nothing about comment-based manipulation, which requires its own separate detection approach entirely.

## What this means for anyone building on this project's methodology

Any future work extending this project's approach to new datasets should check which manipulation model a given pod tool actually uses before assuming the existing like-based anomaly detection will transfer. It won't automatically. LinkBoost's inclusion in this project exists specifically because assuming "engagement pod" means "like-based pod" would have left an entire manipulation category undetected.

## What this is, and isn't

**STATED/VERIFIED**: LinkBoost's dataset reflects a comment-based rather than like-based manipulation model, based on its own schema and anomaly patterns.

**A methodology note, not a severity ranking**: this project makes no claim that either manipulation model is more or less harmful than the other.

Full LinkBoost findings: **github.com/DreamITSoftware/SPOTAPOD**.

---

*Self-published. Not peer-reviewed.*
