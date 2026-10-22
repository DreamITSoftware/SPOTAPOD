# Political party / Trump content

`analysis/political_content_scan.py` counts mentions of political-party
terms and Trump/Biden across post content in all three datasets. Same
discipline as every other scan in this repo: aggregate counts only, no
record, author, or matched text ever printed beyond the
duplicate-template check described below, and no real individual is
ever identified.

## A correction linked to an artifact already documented elsewhere in this repo

The duplicate-template safeguard from
[nonprofit-content.md](nonprofit-content.md) fired on LinkBoost-2025:
97 of its "Democrat/Democratic Party" matches trace to a single
repeated post. This is not a new discovery - it is the same political
campaign-endorsement template already documented in
[decision-points.md](decision-points.md), which also found 97
occurrences of this exact post, there under the
`business_entrepreneurship` topic category (it was swept in by
incidental keyword overlap, not because it's business content).
Consistent with this repo's privacy rules, the candidate named in that
post was not identified in decision-points.md and is not identified
here either.

## Results (VERIFIED - reproducible via the script)

| Term | podawaa2024 | HyperClapper | LinkBoost-2025 |
|---|---|---|---|
| Trump | 102 | 136 | 173 |
| Biden | 81 | 2 | 15 |
| Democrat(s)/Democratic Party | 11 | 6 | 108\* |
| Republican(s)/GOP | 15 | 7 | - |
| Political party (generic) | 13 | 5 | 28 |
| Libertarian | 3 | 1 | - |
| **Any mention (raw)** | **197 (0.092%)** | **147 (0.298%)** | **309 (0.396%)** |
| **Any mention (corrected)** | 197 (no correction needed) | 147 (no correction needed) | **213 (0.273%)** |

\* See correction above.

## Reading these numbers

Trump is the single largest term in every dataset, and the only one
with meaningful presence across all three - Biden and party-name
mentions are comparatively sparse and unevenly distributed.
HyperClapper's Trump-to-Biden ratio (136:2) is the most lopsided of the
three. podawaa2024 and HyperClapper show genuinely distinct,
broadly-distributed content (182 and 144 distinct strings
respectively, no dominant template); the correction above is specific
to LinkBoost-2025.

This is a small category overall - under 0.4% of any dataset even
before correction - consistent with these being professional/business/
career-focused datasets rather than political-commentary datasets.

## Caveats

Same as every keyword scan in this repo: a match means the term
appears in the text, not that the post is substantively about politics,
policy, or a political figure. As with every scan in this project, no
individual is identified, and none should be inferred, from any finding
here.

<!-- export65-section -->
## The 65 export files

Added 22 October 2026. This is the same scan run on the 65 export files: 56,363 distinct records after the files are de-duplicated on record id, reading each record's `title` field, which holds the post text. These files are a separate set from the three datasets above, and nothing above this heading has changed. Their source, method and limits are in [provenance.md](../provenance.md#the-65-export-files) and [export-65-profile.md](export-65-profile.md). Rates use all 56,363 records as the denominator, and 237 of them have no post text. Command: `python3 analysis/political_content_scan.py export65 /path/to/folder_with_the_65_files`.

```text
=== 65 export files (56,363 records) ===
Any political-term mention: 250 (0.4436%)
Distinct underlying text values: 249
    Trump (Donald/President)           211
    political party (generic)          29
    Democrat(s) / Democratic Party     8
    Republican(s) / GOP                8
    Biden (Joe/President)              6
```

250 of 56,363 records (0.444%) match. In the three datasets above the same measure is 0.092% in podawaa2024, 0.298% in HyperClapper and 0.273% in LinkBoost-2025 (using the corrected figure where this page gives one), which puts the 65 export files at the highest of the four. The scan's duplicate-template check did not fire, and the matching records hold 249 distinct texts.

The rates come from different fields and different kinds of record, so a gap between them describes the files and does not describe the tools. A match is a keyword in the text, not a finding about the post or its author.
