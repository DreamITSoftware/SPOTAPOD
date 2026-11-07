# One Post: Series Launch

### A recurring deep-dive on one anomalous record per installment, without showing the record itself

A "one post" deep-dive series would normally display an actual post and dissect it. This project can't do that without risking re-identification, so each installment covers one anomaly type, described entirely through its measurable properties and never its content.

## Installment one: the 88,028-likes-zero-views post

**What's measurable about it:** a single record in `podawaa2024.json` with a like count of 88,028 and a view count of 0. That specific combination, real likes, zero views, is the largest single instance of this project's zero-view anomaly pattern in the entire dataset.

**What that combination would require, if the metrics were genuine:** 88,028 individual people encountering and liking a post that was, per the same record, viewed by nobody. That is a large discrepancy, and it has no plausible innocent explanation under normal platform mechanics.

**What this project doesn't know:** which account posted it, when precisely, what it said, or why this specific record shows this specific anomaly rather than a smaller one. The record is one data point in an aggregate pattern, examined in isolation. It is not a case study of an identified individual's behavior.

## Why this format fits this project's constraints

Depth doesn't require identity. This installment goes deeper into a single record's numbers than this project's aggregate-statistics pieces do, while disclosing nothing that could trace back to a real account. "One post, examined closely" and "one person, exposed" are different projects, and this series only does the first.

## What is verified

**VERIFIED**: this specific like/view combination exists in the dataset, independently reproducible.

**Anonymized by design, not by omission**: no identifying detail about this record is available to reveal, because none was ever retained.

Full findings: **github.com/DreamITSoftware/SPOTAPOD**.

<!-- export65-note -->
> **Update, 22 October 2026.** In the [65 export files](../provenance.md#the-65-export-files), the largest like count in the `statsLikes` field is 12,029 and the largest view count in `statsViews` is 842,676. The records with the ten highest like counts include none with zero views: two have no view count at all and eight have a view count above zero. Views are present on only 11,987 of 56,363 records and the site does not document the fields, so this is a limited check. Detail: [engagement statistics fields](../research/export-65-profile.md#engagement-statistics-fields).

---

*Self-published. Not peer-reviewed.*
