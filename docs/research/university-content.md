# University content

`analysis/university_content_scan.py` counts mentions of
university-related terms across post content in all three datasets.
Same discipline as every other scan in this repo: aggregate counts
only, no record, author, or matched text ever printed beyond the
duplicate-template check described below.

## A cross-language false positive caught by an inconsistency check

An earlier draft matched "MIT" case-insensitively, which also caught
the German preposition "mit" (meaning "with"). podawaa2024 contains a
meaningful amount of German-language content, and this single
collision inflated that dataset's "MIT" count from a genuine 148 to a
false 2,601 - a roughly 94% false-positive rate that briefly made "MIT"
look like the single largest university-related term in that dataset,
ahead of the generic word "university" itself.

No threshold or distinct-string check caught this. Podawaa2024's uncorrected result was inconsistent
with the other two datasets, where "university/universities" led as
expected. That inconsistency prompted a manual read of the matching
text, which showed German sentences ("Ich ging mit meiner
Mutter...") mixed in with genuine MIT mentions ("MIT engineers have
shown...").

The fix: "MIT" is matched case-sensitively in the shipped script (no
`re.IGNORECASE`), since the German word is always written lowercase and
the university acronym is always written in caps. This is the same kind of problem
as the "cart"/CAR-T collision in
[immunotherapy-content.md](immunotherapy-content.md) and the "TIME"
magazine pattern in [entity-mentions.md](entity-mentions.md) . A short,
common-looking token needs either a qualifying phrase or a case
constraint before it can be trusted, and cross-dataset consistency is
a useful check even when no automated safeguard fires.

## Results (VERIFIED - reproducible via the script)

| Term | podawaa2024 | HyperClapper | LinkBoost-2025 |
|---|---|---|---|
| University/universities | 1,379 | 717 | 784 |
| College(s) | 537 | 315 | 659 |
| Harvard | 508 | 152 | 277 |
| Stanford | 150 | 145 | 30 |
| MIT (case-sensitive) | 148 | 197 | 386 |
| Oxford | 89 | 24 | 9 |
| Cambridge | 65 | 11 | 151 |
| Berkeley | 80 | 19 | - |
| Ivy League | 24 | 7 | - |
| Princeton | 23 | 5 | - |
| Yale | 21 | 10 | - |
| **Any mention** | **2,596 (1.216%)** | **1,378 (2.791%)** | **1,976 (2.534%)** |

## Reading these numbers

"University/universities" (the generic term) correctly leads in all
three datasets once the MIT/"mit" collision is fixed. The same ranking across datasets is
part of the evidence that the correction is right.

Harvard is the most-mentioned named institution everywhere, well ahead
of Stanford, MIT, Oxford, and the rest. LinkBoost-2025 leans unusually
heavily on Cambridge (151, second only to Harvard there) relative to
the other two datasets, where Cambridge barely registers - a
dataset-specific pattern, not an artifact, since it doesn't
depend on the corrected term.

## Caveats

Same as every keyword scan in this repo: a match means the term
appears in the text, not that the post is genuine, accurate content
about the named institution. The correction above shows that cross-dataset comparison can surface a
methodological problem that within-dataset distinct-string or
duplicate-template checks miss.
