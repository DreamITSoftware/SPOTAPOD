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
