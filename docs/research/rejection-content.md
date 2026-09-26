# Rejection content

`analysis/rejection_content_scan.py` counts mentions of
rejection-related terms (rejection(s), rejected, reject, job rejection,
rejection letter) across post content in all three datasets. Same
discipline as every other scan in this repo: aggregate counts only, no
record, author, or matched text ever printed beyond the
duplicate-template check described below.

## HyperClapper's "job rejection" checked against the known resume-rewrite template

HyperClapper's "job rejection" count (52) was checked directly against
the already-documented "silence for 90 days... ran my resume through
ChatGPT" template (see [decision-points.md](decision-points.md)) to
confirm it isn't simply re-surfacing that same template under a
different keyword. It isn't - zero overlap between the two sets,
confirming these are genuinely separate job-rejection posts, not a
re-discovery of already-counted content.

## LinkBoost-2025's low-distinct-ratio note, checked

The low-distinct-ratio note fires on LinkBoost-2025 (59 distinct
strings for 939 matches), but the duplicate-template warning does not -
no single string dominates (the top is 81 of 939, about 9%). Checked
manually: the top repeated strings are genuinely distinct, on-theme
posts, including a "rejected by 100 VCs, went on to build Canva"
founder-resilience story and two ChatGPT-resume-prompt posts. This is
genuine signal, not an artifact.

## Results (VERIFIED - reproducible via the script)

| Term | podawaa2024 | HyperClapper | LinkBoost-2025 |
|---|---|---|---|
| Rejection(s) | 209 | 326 | 576 |
| Rejected | 107 | 241 | 290 |
| Reject | 72 | 74 | 157 |
| Job rejection | 2 | 52 | - |
| Rejection letter | 4 | 1 | - |
| **Any mention** | **353 (0.165%)** | **584 (1.183%)** | **939 (1.204%)** |

## Reading these numbers

HyperClapper's "job rejection" specificity stands out sharply - 52
mentions there versus just 2 in podawaa2024 and 0 in LinkBoost-2025.
Since this is confirmed to be distinct from the already-documented
resume-rewrite template, it reinforces (with new, independent evidence)
HyperClapper's already-established elevated career/job-search content
share documented in
[career-advice-comparison.md](career-advice-comparison.md).

LinkBoost-2025 has the highest overall rate, and its content is
genuinely distinct across many posts - including a founder-resilience
narrative (rejected by 100 VCs before building Canva) and resume-prompt
content - connecting directly to the resume/career-rejection theme
running through this category.

This is a moderate-sized content category - smaller than
[confidence-content.md](confidence-content.md) or
[future-content.md](future-content.md), but larger than most of the
niche health/geography/entity scans checked elsewhere in this repo.

## Caveats

Same as every keyword scan in this repo: a match means the term
appears in the text, not that the post describes a genuine personal
rejection experience.
