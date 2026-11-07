# Three Pods, Three Personalities

### podawaa, HyperClapper, and LinkBoost are different tools. They manipulate different metrics, at different scales, with zero shared accounts.

This project draws on three independently sourced LinkedIn engagement-pod datasets. Side by side, they look like three distinct approaches to the same business rather than three instances of the same product.

## The structural differences

**podawaa2024** is the largest by post volume, 213,491 posts, and is built around like-based reciprocal engagement, the classic pod model. Members like each other's posts on a rotating basis to inflate visibility.

**HyperClapper** is smaller in scale (49,369 posts, 702 unique authors) but shows extreme account concentration. The top 20 authors account for 36.2% of posts, and the top 100 for 83.5%. Its posting-velocity outliers include accounts active for over 700 consecutive days without a gap.

**LinkBoost** manipulates a different metric, using a comment-based model rather than the like-based approach of the other two, which produces a measurably different anomaly signature in its data.

## Zero overlap

Checking for shared accounts between HyperClapper and LinkBoost, two tools serving the same market of people wanting inflated LinkedIn engagement, found zero overlapping accounts. This is verified and somewhat counterintuitive, since a customer might be expected to use whichever tools are available, or several at once for redundancy. The absence of overlap suggests separate customer bases, pricing or feature differences strong enough to segment the market, or some other structural factor this project's data does not explain.

## What this comparative view establishes

There are multiple, structurally distinct engagement-pod businesses, possibly serving non-overlapping customer segments, each leaving a different statistical signature in the data. Treating "pod activity" as a single phenomenon would miss these differences.

## What this is, and isn't

**VERIFIED**: all scale, concentration, and zero-overlap figures cited above, independently computed from the raw datasets.

**UNCORROBORATED**: the reasons behind the zero account overlap. This project observes the pattern but cannot explain the underlying market dynamics with certainty.

Full comparative data: **github.com/DreamITSoftware/SPOTAPOD**.

<!-- export65-note -->
> **Update, 22 October 2026.** The [65 export files](../provenance.md#the-65-export-files) are not a fourth tool in this comparison. The collector reports that they came from the LinkBoost web application (STATED), and nothing here says they hold the same data as LinkBoost-2025. On concentration, the top 100 of their 1,380 accounts produce 62.7% of the records, against 83.5% in HyperClapper. Detail: [provenance](../provenance.md#the-65-export-files) and [engagement statistics fields](../research/export-65-profile.md#engagement-statistics-fields).

---

*Self-published. Not peer-reviewed.*
