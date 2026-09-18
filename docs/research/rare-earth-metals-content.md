# Rare earth metals / critical minerals content

`analysis/rare_earth_metals_scan.py` counts mentions of rare earth
metals/elements and adjacent critical-minerals terms (lithium, cobalt,
critical minerals, neodymium) across post content in all three
datasets. Same discipline as every other scan in this repo: aggregate
counts only, no record, author, or matched text ever printed beyond
the duplicate-template check described below.

## Scope note

Lithium and cobalt are not technically rare earth elements - they are
battery/EV-supply-chain minerals commonly discussed alongside rare
earths in the same policy and industry conversations - but they're
included here because they account for the overwhelming majority of
matches. The specific phrase "rare earth metals/elements/earths"
appears only **7 times total** across all three datasets combined.

## A duplicate string that turned out to be genuine content

The duplicate-template check fires on LinkBoost-2025 (53 of 71 matches
share one string), but checking the underlying text directly showed
this is genuine content - an e-waste/battery-recycling industry post
about an Indian recycling company - boosted by the platform's
structure, not a false positive. Corrected, LinkBoost-2025's real
any-mention count is 19, not 71.

This is the same kind of outcome as
[homelessness-content.md](homelessness-content.md),
[diabetes-content.md](diabetes-content.md), and
[narcissist-content.md](narcissist-content.md), where a flagged
duplicate turned out to be real content rather than noise.

## Results (VERIFIED - reproducible via the script)

| Term | podawaa2024 | HyperClapper | LinkBoost-2025 |
|---|---|---|---|
| Lithium | 52 | 10 | 56 |
| Cobalt | 22 | 6 | 15 |
| Critical minerals | 3 | 13 | - |
| Rare earth metals/elements/earths | 2 | 5 | - |
| Neodymium | - | 1 | - |
| **Any mention (raw)** | **68 (0.0319%)** | **30 (0.0608%)** | **71 (0.0911%)** |
| **Any mention (corrected)** | 68 (no correction needed) | 30 (no correction needed) | **19 (0.0244%)** |

## Reading these numbers

Actual "rare earth" terminology is vanishingly rare - only 7 mentions
total, all combined. Lithium is the dominant term in podawaa2024 and
LinkBoost-2025, while HyperClapper leans more toward the general phrase
"critical minerals." This is one of the smallest content categories
found in this project, comparable in scale to
[narcissist-content.md](narcissist-content.md) and
[immunotherapy-content.md](immunotherapy-content.md).

## Caveats

Same as every keyword scan in this repo: a match means the term
appears in the text, not that the post contains substantive or accurate
commentary on mineral supply chains, mining, or battery technology.
