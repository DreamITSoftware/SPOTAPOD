# "Top list" / listicle content

`analysis/toplist_content_scan.py` counts mentions of "top list" and
listicle-style content patterns ("Top 10," "5 ways to," "best of,"
"must-read," "ultimate guide") across post content in all three
datasets. Same discipline as every other scan in this repo: aggregate
counts only, no record, author, or matched text ever printed beyond the
duplicate-template check described below.

## Results (VERIFIED - reproducible via the script)

| Dataset | Any mention | % of dataset |
|---|---|---|
| podawaa2024 | 3,700 | 1.733% |
| HyperClapper | 1,784 | 3.614% |
| LinkBoost-2025 | 3,056 | 3.920% |

**Term breakdown:**

| Term | podawaa2024 | HyperClapper | LinkBoost-2025 |
|---|---|---|---|
| Top N (Top 5/10/etc.) | 1,681 | 1,258 | 1,287 |
| N ways/tips/reasons/steps (listicle) | 1,560 | 472 | 1,627 |
| Best of | 387 | 35 | 57 |
| Must-read | 157 | 18 | 104 |
| Ultimate guide | 49 | 3 | 10 |
| Must-know | 20 | 15 | 10 |

Neither the duplicate-template safeguard nor the low-distinct-ratio
check flagged a genuine correction here. LinkBoost-2025's lower
distinct-string count (182 for 3,056 matches) is consistent with that
dataset's known structure - only 469 distinct target posts total,
documented in [baseline-profile.md](baseline-profile.md) - not a new
artifact requiring correction the way earlier scans in this repo
needed.

## Reading these numbers

This is one of the larger content categories found across the
niche-topic scans in this repo - well above
[pharma-content.md](pharma-content.md) (0.3-0.6%),
[cybersecurity-anomaly.md](cybersecurity-anomaly.md),
[law-content.md](law-content.md), [nonprofit-content.md](nonprofit-content.md),
[travel-content.md](travel-content.md),
[political-content.md](political-content.md),
[national-security-content.md](national-security-content.md), and
[immunotherapy-content.md](immunotherapy-content.md), all of which sit
under 1%.

HyperClapper and LinkBoost-2025 both show meaningfully higher rates than
podawaa2024 (3.6% and 3.9% vs. 1.7%), consistent with the broader
pattern already established across multiple scans in this repo that
these two datasets skew more heavily toward templated, formulaic
content generally - the recurring "resume rewrite" template and
free-certification templates already documented in
[decision-points.md](decision-points.md) are the same underlying
pattern.

The two datasets also show a real difference in listicle style:
LinkBoost-2025 leans more on numbered-listicle phrasing ("N ways/tips/
reasons," 1,627, its single largest term) while HyperClapper leans much
more heavily toward "Top N" specifically (1,258 vs. 472 for the
numbered-listicle phrasing) - a style difference, not just a volume
difference, between the two datasets.

## Caveats

Same as every keyword scan in this repo: a match means the phrase
pattern appears in the text, not that the post is a genuine, well-
researched listicle, or that its claims are accurate.

<!-- export65-section -->
## The 65 export files

Added 22 October 2026. This is the same scan run on the 65 export files: 56,363 distinct records after the files are de-duplicated on record id, reading each record's `title` field, which holds the post text. These files are a separate set from the three datasets above, and nothing above this heading has changed. Their source, method and limits are in [provenance.md](../provenance.md#the-65-export-files) and [export-65-profile.md](export-65-profile.md). Rates use all 56,363 records as the denominator, and 237 of them have no post text. Command: `python3 analysis/toplist_content_scan.py export65 /path/to/folder_with_the_65_files`.

```text
=== 65 export files (56,363 records) ===
Records mentioning any top-list/listicle term: 1,897 (3.366%)
Distinct underlying text values: 1,429
    Top N (Top 5/10/etc.)              1,037
    N ways/tips/reasons (listicle)     761
    best of                            87
    must-read                          28
    ultimate guide                     23
    must-know                          5
```

1,897 of 56,363 records (3.366%) match a top-list or listicle pattern, against 1.733% (podawaa2024), 3.614% (HyperClapper) and 3.920% (LinkBoost-2025), which is the second lowest of the four. Top N is the most frequent pattern (1,037 records), then N ways, tips or reasons (761). The matches hold 1,429 distinct texts, so repeated texts account for part of the count.

The rates come from different fields and different kinds of record, so a gap between them describes the files and does not describe the tools. A match is a keyword in the text, not a finding about the post or its author.
