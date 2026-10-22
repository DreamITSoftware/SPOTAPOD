# Diabetes content

`analysis/diabetes_content_scan.py` counts mentions of diabetes-related
terms (diabetes, diabetic, type 1/2 diabetes, insulin, blood sugar,
glucose monitoring, prediabetes) across post content in all three
datasets. Same discipline as every other scan in this repo: aggregate
counts only, no record, author, or matched text ever printed beyond
the duplicate-template check described below.

## A duplicate string that turned out to be genuine content

The duplicate-template check fires on LinkBoost-2025 (40 of 172
matches share one string), but checking the underlying text directly
showed this is genuine health/nutrition content - a post about sugar
consumption and its effect on blood sugar - boosted by the platform's
structure, not a false positive. Corrected, LinkBoost-2025's real
any-mention count is 133, not 172.

This is the same kind of outcome as
[homelessness-content.md](homelessness-content.md) and
[veteran-content.md](veteran-content.md), where a flagged duplicate
turned out to be real content rather than noise, and the opposite of
[immunotherapy-content.md](immunotherapy-content.md) and
[university-content.md](university-content.md), where flagged patterns
turned out to be outright false positives. The lesson standing across
all four: the safeguard tells you a number needs a second look, not
what you'll find when you look.

## Results (VERIFIED - reproducible via the script)

| Term | podawaa2024 | HyperClapper | LinkBoost-2025 |
|---|---|---|---|
| Diabetes | 85 | 29 | 35 |
| Blood sugar | 12 | 23 | 105 |
| Insulin | 28 | 16 | 63 |
| Diabetic | 17 | 1 | 4 |
| Type 2 diabetes | 6 | 10 | 17 |
| Type 1 diabetes | 6 | - | - |
| Prediabetes | 1 | - | 17 |
| Glucose monitoring | - | 1 | - |
| **Any mention (raw)** | **126 (0.0590%)** | **41 (0.0830%)** | **172 (0.2206%)** |
| **Any mention (corrected)** | 126 (no correction needed) | 41 (no correction needed) | **133 (0.1706%)** |

## Reading these numbers

This is one of the smallest genuine content categories found in this
project, comparable in scale to
[national-security-content.md](national-security-content.md) and
[immunotherapy-content.md](immunotherapy-content.md), all under 0.25%
of any dataset.

"Blood sugar" is LinkBoost-2025's dominant term (105, mostly the
boosted post above), while podawaa2024 leans toward the clinical term
"diabetes" itself (85) - a real phrasing difference between
general-wellness framing and more clinical language, similar in kind to
the framing differences documented in
[authenticity-content.md](authenticity-content.md) and
[toplist-content.md](toplist-content.md).

## Caveats

Same as every keyword scan in this repo: a match means the term
appears in the text, not that the account or post has any verified
connection to diabetes, medical expertise, or accurate health
information. This is a health-adjacent content category; as with
everywhere else in this repo, no claim is made or inferred about any
individual's health status.

<!-- export65-section -->
## The 65 export files

Added 22 October 2026. This is the same scan run on the 65 export files: 56,363 distinct records after the files are de-duplicated on record id, reading each record's `title` field, which holds the post text. These files are a separate set from the three datasets above, and nothing above this heading has changed. Their source, method and limits are in [provenance.md](../provenance.md#the-65-export-files) and [export-65-profile.md](export-65-profile.md). Rates use all 56,363 records as the denominator, and 237 of them have no post text. Command: `python3 analysis/diabetes_content_scan.py export65 /path/to/folder_with_the_65_files`.

```text
=== 65 export files (56,363 records) ===
Records mentioning any diabetes-related term: 289 (0.5127%)
Distinct underlying text values: 280
    blood sugar              135
    diabetes                 109
    insulin                  101
    diabetic                 22
    type 2 diabetes          13
    prediabetes              6
    glucose monitoring       6
    type 1 diabetes          3
```

289 of 56,363 records (0.513%) match. In the three datasets above the same measure is 0.059% in podawaa2024, 0.083% in HyperClapper and 0.171% in LinkBoost-2025 (using the corrected figure where this page gives one), which puts the 65 export files at the highest of the four. The scan's duplicate-template check did not fire, and the matching records hold 280 distinct texts.

The rates come from different fields and different kinds of record, so a gap between them describes the files and does not describe the tools. A match is a keyword in the text, not a finding about the post or its author.
