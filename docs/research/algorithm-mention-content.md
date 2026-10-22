# LinkedIn algorithm mentions

`analysis/algorithm_mention_scan.py` counts mentions of "algorithm" and
LinkedIn-algorithm-specific phrasing across post content in all three
datasets. Same discipline as every other scan in this repo: aggregate
counts only, no record, author, or matched text ever printed beyond
the duplicate-template check described below.

## Why this scan is directly relevant to this project

Unlike most of the niche-topic scans in this repo, this one measures
something close to this whole project's own subject matter. See
[algorithm-strategy-advice.md](algorithm-strategy-advice.md), which
documents the broader genre of algorithm-strategy-advice content this
scan measures the raw prevalence of. LinkBoost-2025's top repeated
posts include content specifically about gaming or understanding the
LinkedIn algorithm - directly on-theme for the datasets this repo
analyzes, not incidental.

## LinkBoost-2025's low-distinct-ratio note, checked

The low-distinct-ratio check fires on LinkBoost-2025 (37 distinct
strings for 594 matches), but the duplicate-template warning does not -
no single string dominates. Checked manually: the top repeated string
is under 10% of matches, and the top several strings are genuinely
distinct, on-topic posts (one about using ChatGPT to analyze a LinkedIn
profile, one directly discussing why "the algorithm hates you"). This
is genuine signal, not a new artifact requiring correction.

## Results (VERIFIED - reproducible via the script)

| Term | podawaa2024 | HyperClapper | LinkBoost-2025 |
|---|---|---|---|
| Algorithm (generic, any platform) | 543 | 321 | 594 |
| LinkedIn algorithm (specific) | 67 | 11 | 0 |
| Algorithm change/update | 28 | 12 | 0 |
| Algorithm favors/rewards | 4 | 20 | 70 |
| Game the algorithm | 2 | - | 0 |
| **Any mention** | **543 (0.254%)** | **321 (0.650%)** | **594 (0.762%)** |

## Reading these numbers

LinkBoost-2025 has the highest overall rate. podawaa2024 is the only
dataset with meaningful "LinkedIn algorithm" specificity - 67 mentions
naming the platform's algorithm directly, versus 11 in HyperClapper and
effectively none in LinkBoost-2025. The other two datasets discuss "the
algorithm" much more generically without naming the platform, even
though all of this content is itself hosted on LinkedIn.

This is a meaningful, if modest, category overall - larger than
[diabetes-content.md](diabetes-content.md),
[national-security-content.md](national-security-content.md), and
[immunotherapy-content.md](immunotherapy-content.md), and in the same
general range as [pharma-content.md](pharma-content.md) and
[cybersecurity-anomaly.md](cybersecurity-anomaly.md) (0.25%-0.76%
across the board).

## Caveats

Same as every keyword scan in this repo: a match means the term
appears in the text, not that the post contains accurate or
substantive commentary on how LinkedIn's algorithm actually works.

<!-- export65-section -->
## The 65 export files

Added 22 October 2026. This is the same scan run on the 65 export files: 56,363 distinct records after the files are de-duplicated on record id, reading each record's `title` field, which holds the post text. These files are a separate set from the three datasets above, and nothing above this heading has changed. Their source, method and limits are in [provenance.md](../provenance.md#the-65-export-files) and [export-65-profile.md](export-65-profile.md). Rates use all 56,363 records as the denominator, and 237 of them have no post text. Command: `python3 analysis/algorithm_mention_scan.py export65 /path/to/folder_with_the_65_files`.

```text
=== 65 export files (56,363 records) ===
Records mentioning any algorithm term: 378 (0.671%)
Distinct underlying text values: 372
    algorithm (generic, any platform)    378
    algorithm change/update              21
    algorithm favors/rewards             20
    LinkedIn algorithm (specific)        12
    beat the algorithm                   3
    game the algorithm                   3
```

378 of 56,363 records (0.671%) match. In the three datasets above the same measure is 0.254% in podawaa2024, 0.65% in HyperClapper and 0.762% in LinkBoost-2025 (using the corrected figure where this page gives one), which puts the 65 export files at the second highest of the four. The scan's duplicate-template check did not fire, and the matching records hold 372 distinct texts.

The rates come from different fields and different kinds of record, so a gap between them describes the files and does not describe the tools. A match is a keyword in the text, not a finding about the post or its author.
