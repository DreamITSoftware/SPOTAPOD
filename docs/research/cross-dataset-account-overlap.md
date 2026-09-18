# Cross-dataset account overlap

`analysis/cross_dataset_overlap_scan.py` checks whether the same
LinkedIn accounts appear in both HyperClapper and LinkBoost-2025 - two
different commercial engagement-pod tools - by hashing each dataset's
account identifiers and comparing the hash sets. This is structurally
different from every other scan in this repo: it's not a content
keyword scan, it's a question about whether two products draw from the
same or different user populations.

## Why this question matters

Every other analysis in this repo treats the three datasets as
independent samples. This scan tests that assumption directly for two
of them. If the same accounts showed up using both tools, that would
suggest a shared "professional pod-participant" community - people who
use more than one engagement-manipulation product. If the populations
are disjoint, that's evidence the market segments by tool, or that the
overall pool of participants is large enough relative to any single
sample that overlap wouldn't be expected regardless.

## Method and privacy

Both datasets use the same LinkedIn vanity-username namespace:
HyperClapper's `profile.linkedin_data.public_identifier` field
(confirmed to contain a real, unhashed LinkedIn username on
inspection), and a username extracted from LinkBoost-2025's
`liProfileLink` field (a `linkedin.com/in/<username>` URL). Every
identifier is hashed (SHA-256, lowercased and stripped) the instant
it's read and never held or printed in plaintext - this script's output
contains only the size of each hash set and the size of their
intersection, never which accounts overlap, if any do.

`podawaa2024.json` is not included in this comparison. It identifies
authors via `AuthorPublicIdentifier`, which on inspection is a
different, non-comparable identifier scheme from the other two files'
vanity usernames, so a direct hash comparison against it would not be
meaningful.

## Results (VERIFIED - reproducible via the script)

| | Count |
|---|---|
| HyperClapper distinct hashed accounts | 702 |
| LinkBoost-2025 distinct hashed accounts | 414 |
| **Overlapping hashed accounts** | **0** |
| Overlap as % of HyperClapper accounts | 0.00% |
| Overlap as % of LinkBoost-2025 accounts | 0.00% |

## Reading this number

Zero is a real, specific finding, not just "low overlap" rounded down -
across 702 and 414 distinct accounts respectively, not one hashed
identifier appears in both sets. This repo does not have enough
information to determine why: it could reflect genuinely segmented
customer bases between different pod-service products, or it could
simply reflect that these sample sizes are small relative to the total
population of LinkedIn accounts using any engagement-manipulation tool,
such that overlap would be statistically unlikely even if some
individuals do use more than one product. Both explanations remain
open; only the zero-overlap fact itself is established here.

## Caveats

This finding is specific to the two datasets and the identifier fields
checked. A different identifier scheme, a different snapshot in time,
or inclusion of podawaa2024 (once a comparable identifier is
established for it, if one exists) could change the result. This scan
also cannot detect overlap between accounts that use different vanity
usernames across the two tools, or accounts that changed their vanity
username between the two datasets' collection windows.
