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
