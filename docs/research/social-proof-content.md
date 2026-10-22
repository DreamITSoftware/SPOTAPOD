# Social proof and credibility signaling

`analysis/social_proof_scan.py` counts mentions of award/recognition
claims, follower-count milestones, engagement-bait question formats,
and congratulations/anniversary posts across post content in all three
datasets. Same discipline as every other scan in this repo: aggregate
counts only, no record, author, or matched text ever printed beyond
the duplicate-template check below.

## Why this scan is unusually on-theme

Unlike most of the niche-topic scans in this repo, this one measures
the exact mechanics this whole project studies: manufactured
credibility signals. The "engagement bait" category is built around
the already-documented "Agree?" template (3,918 occurrences in
podawaa2024, first reported in
[baseline-profile.md](baseline-profile.md)), and this scan confirms the
same phenomenon in LinkBoost-2025 too (888 occurrences) - the same
one-word engagement-bait post, independently duplicated at scale in a
second, structurally different dataset.

## Results (VERIFIED - reproducible via the script)

| Term | podawaa2024 | HyperClapper | LinkBoost-2025 |
|---|---|---|---|
| Engagement bait (Agree?/Thoughts?/etc.) | 5,072 | 173 | 1,408 |
| Congratulations / anniversary | 604 | 154 | 95 |
| Award / recognition (30 under 30, etc.) | 300 | 32 | 25 |
| Follower milestone | 93 | 47 | 184 |
| **Any mention (raw)** | **6,061 (2.839%)** | **404 (0.818%)** | **1,712 (2.196%)** |
| **Any mention (corrected)** | **2,144-3,918 range\*** | 404 (no correction needed) | **825-1,712 range\*** |

\* Both podawaa2024 and LinkBoost-2025 trigger the duplicate-template
note for the same reason: the "Agree?" template. This is not a new
finding requiring separate correction - it's the same, already
well-documented pattern from [baseline-profile.md](baseline-profile.md)
showing up again because this scan's term list includes it directly.
The corrected estimate ranges reflect "Agree?" counted once instead of
thousands of times in each affected dataset.

## Reading these numbers

podawaa2024 has both the highest raw rate and the heaviest reliance on
the single "Agree?" template - once that's accounted for, its
non-engagement-bait signals (congratulations, awards, follower
milestones) are still the largest of the three datasets in absolute
terms, suggesting genuine credibility-signaling content beyond just the
bait template.

HyperClapper is the only dataset where the duplicate-template check
doesn't fire at all - its engagement-bait numbers (173) are
comparatively modest and spread across genuinely distinct posts.

## Caveats

Same as every keyword scan in this repo: a match means the term or
phrase pattern appears in the text, not that any specific award,
follower count, or anniversary claim is accurate.

<!-- export65-section -->
## The 65 export files

Added 22 October 2026. This is the same scan run on the 65 export files: 56,363 distinct records after the files are de-duplicated on record id, reading each record's `title` field, which holds the post text. These files are a separate set from the three datasets above, and nothing above this heading has changed. Their source, method and limits are in [provenance.md](../provenance.md#the-65-export-files) and [export-65-profile.md](export-65-profile.md). Rates use all 56,363 records as the denominator, and 237 of them have no post text. Command: `python3 analysis/social_proof_scan.py export65 /path/to/folder_with_the_65_files`.

```text
=== 65 export files (56,363 records) ===
Records mentioning any social-proof term: 1,058 (1.877%)
Distinct underlying text values: 603
    engagement bait (Agree?/Thoughts?)       670
    congratulations / anniversary            265
    award / recognition (30 under 30 etc.)   80
    follower milestone                       50
```

1,058 of 56,363 records (1.877%) match. In the three datasets above the same measure is 2.839% in podawaa2024, 0.818% in HyperClapper and 2.196% in LinkBoost-2025 (using the corrected figure where this page gives one), which puts the 65 export files at the second lowest of the four. The scan's duplicate-template check did not fire, and the matching records hold 603 distinct texts. That is 57% of the matches, so repeated texts account for part of the count.

The rates come from different fields and different kinds of record, so a gap between them describes the files and does not describe the tools. A match is a keyword in the text, not a finding about the post or its author.
