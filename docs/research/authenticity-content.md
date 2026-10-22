# Authenticity content

`analysis/authenticity_content_scan.py` counts mentions of
authenticity-related terms ("authentic," "genuine," "transparent,"
"real talk," "honest truth," "unfiltered," "be yourself," "no BS/no
fluff") across post content in all three datasets. Same discipline as
every other scan in this repo: aggregate counts only, no record,
author, or matched text ever printed beyond the duplicate-template
check described below.

## A specific claim from a disputed document, checked directly

A disputed third-party document referenced in this project's history
(not included in this repo) claimed HyperClapper had 5,193 posts
(10.52%) branding themselves with "the honest truth" or "real talk,"
against only 93 posts (0.19%) acknowledging fake engagement - framed as
a "honesty irony." The actual counts computed here are **15** for
"honest truth" and **46** for "real talk," a combined 61 - nowhere
close to 5,193. (The "acknowledges fake engagement" side of that
claimed comparison is not checked by this script, since it falls
outside this scan's term list; only the "honest truth"/"real talk" side
is addressed here.)

This is consistent with a separate, previously documented discrepancy
in the same document: a claimed 1,706 occurrences of a resume-rewrite
template against an actual, independently verified count of 533-806
depending on spelling variants (see this project's broader research
notes). Both discrepancies point the same direction - the disputed
document's specific statistics do not hold up against direct
verification against the source files.

A third claim from the same document has since been checked directly
against this repo's own copy of the raw source files: that HyperClapper's
"top 20 accounts produce 50.6%... top 100 produce 87.3%" of all posts.
Run via `analysis/top_account_concentration.py` (VERIFIED, reproducible),
the actual figures are **36.2%** (top 20 authors) and **83.5%** (top 100
authors) of posts with an identified author - both real concentration
effects, and both lower than claimed. All three checked statistics from
this document point the same direction: the underlying pattern each one
describes is real, but the specific number attached to it is inflated.

## LinkBoost-2025's lower distinct-string ratio, checked

LinkBoost-2025 triggers the low-distinct-ratio note (204 distinct
strings for 3,410 matches) but not the duplicate-template warning. A
manual check of the top repeated strings (133, 104, 100, 98, 80
occurrences - no single one dominating) confirmed these are genuinely
distinct posts, consistent with LinkBoost-2025's known structure, not a
new artifact requiring correction.

## Results (VERIFIED - reproducible via the script)

| Term | podawaa2024 | HyperClapper | LinkBoost-2025 |
|---|---|---|---|
| Authentic/authenticity | 1,390 | 474 | 1,881 |
| Transparent/transparency | 1,814 | 445 | 794 |
| Genuine | 932 | 346 | 772 |
| Unfiltered | 60 | 42 | 198 |
| No BS/no fluff | 48 | 111 | 97 |
| Be yourself | 58 | 7 | - |
| Real talk | 37 | 46 | 25 |
| Honest truth | 2 | 15 | - |
| **Any mention** | **3,939 (1.845%)** | **1,394 (2.824%)** | **3,410 (4.374%)** |

## Reading these numbers

LinkBoost-2025 has both the highest rate and the most genuinely
distributed content of the three datasets. "Transparent/transparency"
leads in podawaa2024, while "authentic/authenticity" leads in the other
two datasets - a real phrasing difference across datasets, similar in
kind to the "Top N" vs. numbered-listicle style difference documented
in [toplist-content.md](toplist-content.md).

## Caveats

Same as every keyword scan in this repo: a match means the term
appears in the text, not that the post or account is genuinely
authentic, transparent, or honest. If anything, this category's own
subject matter is a reminder that claiming authenticity and being
authentic are two different things - which is exactly the point this
scan was built to check against a specific outside claim.

<!-- export65-section -->
## The 65 export files

Added 22 October 2026. This is the same scan run on the 65 export files: 56,363 distinct records after the files are de-duplicated on record id, reading each record's `title` field, which holds the post text. These files are a separate set from the three datasets above, and nothing above this heading has changed. Their source, method and limits are in [provenance.md](../provenance.md#the-65-export-files) and [export-65-profile.md](export-65-profile.md). Rates use all 56,363 records as the denominator, and 237 of them have no post text. Command: `python3 analysis/authenticity_content_scan.py export65 /path/to/folder_with_the_65_files`.

```text
=== 65 export files (56,363 records) ===
Records mentioning any authenticity-related term: 2,030 (3.602%)
Distinct underlying text values: 1,984
    transparent / transparency       785
    authentic / authenticity         618
    genuine                          497
    no BS / no fluff                 129
    unfiltered                       64
    real talk                        40
    be yourself                      17
    honest truth                     6
```

2,030 of 56,363 records (3.602%) match. In the three datasets above the same measure is 1.845% in podawaa2024, 2.824% in HyperClapper and 4.374% in LinkBoost-2025 (using the corrected figure where this page gives one), which puts the 65 export files at the second highest of the four. The scan's duplicate-template check did not fire, and the matching records hold 1,984 distinct texts.

The rates come from different fields and different kinds of record, so a gap between them describes the files and does not describe the tools. A match is a keyword in the text, not a finding about the post or its author.
