# LinkBoost's Different Universe: Comment-Based vs. Like-Based Manipulation

### Most engagement-pod research, including most of this project's own, focuses on inflated likes. LinkBoost inflates comments.

podawaa and HyperClapper both fit the pattern most people picture when they hear "engagement pod": coordinated reciprocal liking. LinkBoost's dataset describes a different mechanism, and comparing the two models shows things a single-model view would miss.

## The mechanism difference

Like-based pods (podawaa, HyperClapper) coordinate members to like each other's posts, inflating one metric. LinkBoost's data reflects a comment-based manipulation model, inflating comment counts and comment-driven visibility rather than raw likes. A fabricated comment can carry inauthentic text content, which a fabricated like cannot, so an anomaly looks different in the data and takes different methods to detect.

## Implications for detection

A detection approach tuned to catch like-based anomalies, unusually high like-to-view ratios, zero-view-with-high-likes patterns, would likely miss comment-based manipulation, because it looks at the wrong metric. This project's zero-view-anomaly analysis, one of its most-cited findings, is a like-based signal. It says nothing about comment-based manipulation, which needs its own detection approach.

## For anyone building on this methodology

Future work that extends this approach to new datasets should check which manipulation model a pod tool uses before assuming like-based anomaly detection will transfer. LinkBoost is included because assuming "engagement pod" means "like-based pod" would have left a whole manipulation category undetected.

## What this is, and isn't

**STATED/VERIFIED**: LinkBoost's dataset reflects a comment-based rather than like-based manipulation model, based on its own schema and anomaly patterns.

**A methodology note, not a severity ranking**: this project makes no claim that either manipulation model is more or less harmful than the other.

Full LinkBoost findings: **github.com/DreamITSoftware/SPOTAPOD**.

---

*Self-published. Not peer-reviewed.*
