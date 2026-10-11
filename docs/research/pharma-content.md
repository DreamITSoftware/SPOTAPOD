# Pharma / biotech content

`analysis/pharma_content_scan.py` counts mentions of pharma- and
biotech-related terms across post content in all three datasets. Same
discipline as every other scan in this repo: aggregate counts only, and no
record, author, or matched text is printed beyond the
duplicate-template check described below.

## A correction found by reading the actual posts

The duplicate-template safeguard from
[nonprofit-content.md](nonprofit-content.md) did not fire on this scan:
no single string crossed the 20% threshold in any dataset.
LinkBoost-2025 still needed a manual check: its distinct-string count
(28) was far below its match count (482), with no single string
dominating. The matches came from roughly 8 distinct posts, each boosted
29 to 38 times by LinkBoost's pod-action structure. That is neither one
repeated template nor evenly distributed genuine signal.

Reading those 8 posts directly showed they are about **FDA
import-compliance and customs-regulatory process**: Import Alerts,
product refusals and seizures at the border, FOIA requests to the FDA,
tariff and import-cost issues for regulated goods. This is
trade-compliance/customs-consulting content that mentions the FDA as a
regulator. It is not pharmaceutical-industry content. `FDA` is 333 of
LinkBoost-2025's 482 total matches, so this changes the whole result for
that dataset rather than one line item.

The script now checks for this pattern automatically (a low
distinct-to-match ratio without one dominant string) and prints a note
recommending a manual content check. Earlier versions of this class of scan stayed silent.

## Results (VERIFIED: reproducible via the script)

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

\* See correction above: mostly FDA import-compliance content, not
pharmaceutical-industry content.

## Reading these numbers

podawaa2024 and HyperClapper show genuine, broadly distributed pharma/
biotech content (582 and 144 distinct posts respectively, no dominant
cluster). LinkBoost-2025's higher overall rate is real, but the raw term
breakdown misdescribes it. Once the FDA/import-
compliance cluster is set aside, LinkBoost-2025's
actual pharmaceutical-industry content (the non-FDA rows: pharma/
pharmaceutical, biotech, clinical trials, pharmaceutical industry) is
smaller than the headline 0.618% rate suggests.

## Caveats

Same as every keyword scan in this repo: a match means the term
appears in the text, not that the post is genuine, accurate
pharmaceutical-industry content. This doc's own correction above shows that a low distinct-string count without a single dominant
string can still mean the topic label does not match the content. The earlier duplicate-template threshold alone would not have
caught it.
