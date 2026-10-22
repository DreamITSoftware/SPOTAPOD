# Genetic disorder content

`analysis/genetic_disorder_scan.py` counts mentions of genetic-
disorder-related terms (genetic disorder(s), genetic condition(s),
genetic disease(s), genetic mutation(s), hereditary disease/condition,
inherited disorder(s), Down syndrome, cystic fibrosis, sickle cell)
across post content in all three datasets. Same discipline as every
other scan in this repo: aggregate counts only, no record, author, or
matched text ever printed beyond the duplicate-template check
described below.

This is a health-adjacent, sensitive topic. Every match reported here
is purely a keyword hit in public post text. No claim is made or
implied about any specific individual's actual health status, genetic
makeup, or diagnosis - this script measures how often terms appear in
text, nothing more.

## LinkBoost-2025's correction: one post, not 46

All 46 of LinkBoost-2025's "genetic condition(s)" matches trace to a
single post - checked directly, it's a genuine, substantive excerpt
from a Cathie Wood interview discussing AI and genomics in healthcare,
naming "rare genetic conditions" alongside cancer and chronic illness
as diseases AI-driven medicine might eventually address. This is real
content, not a false positive, but it is one post boosted 46 times by
the platform's structure, not 46 distinct mentions. Corrected,
LinkBoost-2025's real count is 1.

## Results (VERIFIED - reproducible via the script)

| Term | podawaa2024 | HyperClapper | LinkBoost-2025 |
|---|---|---|---|
| Down syndrome | 17 | 1 | - |
| Genetic disease(s) | 3 | - | - |
| Genetic disorder(s) | 2 | - | - |
| Sickle cell | 2 | - | - |
| Genetic mutation(s) | 2 | - | - |
| Cystic fibrosis | 2 | - | - |
| Inherited disorder(s) | 1 | - | - |
| Genetic condition(s) | - | - | 46 |
| **Any mention (raw)** | **27 (0.0127%)** | **1 (0.0020%)** | **46 (0.0590%)** |
| **Any mention (corrected)** | 27 (no correction needed) | 1 (no correction needed) | **1 (0.0013%)** |

## Reading these numbers

This is one of the smallest content categories found in this project,
comparable to [narcissist-content.md](narcissist-content.md) and
[immunotherapy-content.md](immunotherapy-content.md). podawaa2024 has
the most genuine diversity across named conditions, led by Down
syndrome (17 of 27 total). HyperClapper has essentially none. Once
corrected, LinkBoost-2025's entire contribution to this category is a
single post.

## Caveats

Same as every keyword scan in this repo, with extra emphasis given the
topic: a match means the term appears in the text, not that any post
or account has any connection to a real diagnosis, condition, or
genetic status. No individual's health information is identified,
inferred, or reported anywhere in this document or the underlying
script's output.

<!-- export65-section -->
## The 65 export files

Added 22 October 2026. This is the same scan run on the 65 export files: 56,363 distinct records after the files are de-duplicated on record id, reading each record's `title` field, which holds the post text. These files are a separate set from the three datasets above, and nothing above this heading has changed. Their source, method and limits are in [provenance.md](../provenance.md#the-65-export-files) and [export-65-profile.md](export-65-profile.md). Rates use all 56,363 records as the denominator, and 237 of them have no post text. Command: `python3 analysis/genetic_disorder_scan.py export65 /path/to/folder_with_the_65_files`.

```text
=== 65 export files (56,363 records) ===
Records mentioning any genetic-disorder term: 23 (0.04081%)
Distinct underlying text values: 23
    genetic disorder(s)            10
    sickle cell                    7
    cystic fibrosis                5
    Down syndrome                  3
    genetic mutation(s)            3
    genetic condition(s)           2
    genetic disease(s)             2
```

23 of 56,363 records (0.0408%) match. In the three datasets above the same measure is 0.0127% in podawaa2024, 0.002% in HyperClapper and 0.0013% in LinkBoost-2025 (using the corrected figure where this page gives one), which puts the 65 export files at the highest of the four. The scan's duplicate-template check did not fire, and the matching records hold 23 distinct texts.

The rates come from different fields and different kinds of record, so a gap between them describes the files and does not describe the tools. A match is a keyword in the text, not a finding about the post or its author.
