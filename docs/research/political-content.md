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
