# Pharma / biotech content

`analysis/pharma_content_scan.py` counts mentions of pharma- and
biotech-related terms across post content in all three datasets. Same
discipline as every other scan in this repo: aggregate counts only, no
record, author, or matched text ever printed beyond the
duplicate-template check described below.

## A correction that needed reading the actual posts

The duplicate-template safeguard from
[nonprofit-content.md](nonprofit-content.md) did not fire on this
scan - no single string crossed the 20% threshold in any dataset. But
LinkBoost-2025 still needed a manual check: its distinct-string count
(28) was far below its match count (482), without any one string
dominating. That pattern turned out to reflect roughly 8 distinct
posts, each boosted 29-38 times by LinkBoost's pod-action structure -
not one repeated template, but also not evenly distributed genuine
signal either.

Reading those 8 posts directly showed they're about **FDA
import-compliance and customs-regulatory process** - Import Alerts,
product refusals and seizures at the border, FOIA requests to the FDA,
tariff and import-cost issues for regulated goods. This is trade-
compliance/customs-consulting content that happens to mention the FDA
as a regulator, not pharmaceutical-industry content. `FDA` is 333 of
LinkBoost-2025's 482 total matches, so this distinction changes the
character of that dataset's whole result, not just one line item.

The script now checks for this pattern automatically (a low
distinct-to-match ratio without one dominant string) and prints a note
recommending a manual content check, rather than staying silent the way
an earlier version of this class of scan would have.

## Results (VERIFIED - reproducible via the script)

| Term | podawaa2024 | HyperClapper | LinkBoost-2025 |
|---|---|---|---|
| Pharma / pharmaceutical(s) | 359 | 80 | 90 |
| Biotech | 239 | 48 | 80 |
| FDA | 62 | 15 | 333\* |
| Clinical trial(s) | 47 | 13 | 30 |
| Pharma company/companies | 35 | 3 | - |
| Pharmaceutical industry | 12 | 3 | 2 |
| Big pharma | 8 | 1 | - |
| Drug company/companies | 3 | - | - |
| **Any mention** | **636 (0.298%)** | **146 (0.296%)** | **482 (0.618%)** |

\* See correction above - mostly FDA import-compliance content, not
pharmaceutical-industry content.

## Reading these numbers

podawaa2024 and HyperClapper show genuine, broadly distributed pharma/
biotech content (582 and 144 distinct posts respectively, no dominant
cluster). LinkBoost-2025's higher overall rate is real but
mischaracterized by the raw term breakdown alone - once the FDA/import-
compliance cluster is understood for what it is, LinkBoost-2025's
actual pharmaceutical-industry content (the non-FDA rows: pharma/
pharmaceutical, biotech, clinical trials, pharmaceutical industry) is
smaller in character than the headline 0.618% rate suggests.

## Caveats

Same as every keyword scan in this repo: a match means the term
appears in the text, not that the post is genuine, accurate
pharmaceutical-industry content. This doc's own correction above is a
reminder that a low distinct-string count without a single dominant
string can still mean the topic label doesn't mean what it looks like -
a gap the earlier duplicate-template threshold alone wouldn't have
caught.
