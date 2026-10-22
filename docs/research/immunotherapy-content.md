# Immunotherapy content

`analysis/immunotherapy_content_scan.py` counts mentions of
immunotherapy-related terms across post content in all three datasets.
Same discipline as every other scan in this repo: aggregate counts
only, no record, author, or matched text ever printed beyond the
duplicate-template check described below.

## A regex bug caught before it reached the committed script

An earlier draft used the pattern `\bCAR-?T\b` for "CAR-T" (a real
cell-therapy term), with the hyphen made optional to also catch "CAR T"
written as two words. Case-insensitive, that pattern also matches the
common word "cart" - shopping cart, price comparisons, abandoned-cart
marketing content - and completely dominated the raw counts with pure
noise: 107, 60, and 58 false-positive matches in podawaa2024,
HyperClapper, and LinkBoost-2025 respectively, none of which were
actually about cell therapy. Sampling the matches directly (posts about
online shopping, Shopify, subscriptions, grocery habits) made this
obvious immediately.

The shipped pattern requires "CAR-T" to appear with "cell" or "therapy"
nearby, which eliminates the false positives at the cost of missing a
bare "CAR-T" mention with no qualifying word attached - an acceptable
trade given how much noise the unqualified pattern produced. Same class
of lesson as the "TIME" magazine pattern documented in
[entity-mentions.md](entity-mentions.md), but caught before it ever
reached a committed script rather than after.

## A second false positive, caught by the duplicate-template safeguard

LinkBoost-2025's 40 "immunotherapy" matches all trace to a single post
- checked directly, it's a generic business-transformation/AI-
leadership post ("Transformation fails when we forget the human core...
how AI, values, and human creativity must work together") that happens
to use the word "immunotherapy" somewhere in its body, likely as a
passing example, boosted 40 times by the platform's structure. Not
medical content at all.

## Results (VERIFIED - reproducible via the script)

| Dataset | Any mention | % of dataset |
|---|---|---|
| podawaa2024 | 16 | 0.0075% |
| HyperClapper | 0 | 0.0000% |
| LinkBoost-2025 | 40 raw / **0 corrected** | 0.0000% corrected |

**podawaa2024 term breakdown (the only dataset with genuine signal):**

| Term | Count |
|---|---|
| Immunotherapy | 11 |
| Monoclonal antibody/antibodies | 5 |
| Cancer immunotherapy | 2 |
| CAR-T (strict, cell/therapy context) | 1 |

## Reading these numbers

Genuine immunotherapy content is essentially nonexistent across all
340,829 combined records - 16 real mentions total, all in podawaa2024.
This is the smallest genuine content category found in this project so
far, smaller even than [national-security-content.md](national-security-content.md)
(which had real, if sparse, content in all three datasets). HyperClapper
and LinkBoost-2025 have zero real immunotherapy content once the false
positives described above are accounted for.

## Caveats

Same as every keyword scan in this repo, with an extra warning specific
to this one: at counts this small, a single mismatched acronym or a
single off-topic post using a term in passing can dominate or entirely
fabricate an apparent finding. Both things happened while building this
scan. Treat any very-low-count keyword result in this project with the
same scrutiny applied here - check the underlying text, not just the
number - before drawing any conclusion from it.

<!-- export65-section -->
## The 65 export files

Added 22 October 2026. This is the same scan run on the 65 export files: 56,363 distinct records after the files are de-duplicated on record id, reading each record's `title` field, which holds the post text. These files are a separate set from the three datasets above, and nothing above this heading has changed. Their source, method and limits are in [provenance.md](../provenance.md#the-65-export-files) and [export-65-profile.md](export-65-profile.md). Rates use all 56,363 records as the denominator, and 237 of them have no post text. Command: `python3 analysis/immunotherapy_content_scan.py export65 /path/to/folder_with_the_65_files`.

```text
=== 65 export files (56,363 records) ===
Records mentioning any immunotherapy-related term: 14 (0.02484%)
Distinct underlying text values: 14
    immunotherapy                      9
    immuno-oncology                    4
    cancer immunotherapy               2
    checkpoint inhibitor               2
    CAR-T (cell therapy, strict)       1
```

14 of 56,363 records (0.0248%) match the strict immunotherapy patterns, and all 14 are distinct texts. The three datasets above give 0.0075% (podawaa2024), 0.0000% (HyperClapper) and 0.0000% after correction for LinkBoost-2025, so the rate in the 65 files is the highest of the four. This repository prints no matched text, so I have not read the 14 records, and the scan does not show that each is a genuine immunotherapy post. The patterns are the strict ones that this page settled on after the loose search returned false positives.

The rates come from different fields and different kinds of record, so a gap between them describes the files and does not describe the tools. A match is a keyword in the text, not a finding about the post or its author.
