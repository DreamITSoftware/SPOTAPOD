# Car maker content

`analysis/car_maker_scan.py` counts mentions of major automaker names
across post content in all three datasets. Same discipline as every
other scan in this repo: aggregate counts only, no record, author, or
matched text ever printed beyond the duplicate-template check
described below.

This is separate from [entity-mentions.md](entity-mentions.md)'s general
corporation-mention scan. It covers only automakers, at a finer
resolution than that broader scan.

## LinkBoost-2025's low-distinct-ratio note, checked

The low-distinct-ratio note fires on LinkBoost-2025 (40 distinct
strings for 508 matches), but the duplicate-template warning does not:
no single string dominates (the top is 95 of 508, about 19%). Checked
manually: the top repeated strings are distinct Tesla/Musk
finance-and-tech posts (a JPMorgan analyst note on humanoid-robot
stocks tied to Tesla, "should you buy a Tesla in cash" investing
advice, Musk/AI business news, a Cathie Wood interview excerpt). This
is real signal, not an artifact.

## Results (VERIFIED: reproducible via the script)

| Maker | podawaa2024 | HyperClapper | LinkBoost-2025 |
|---|---|---|---|
| Tesla | 410 | 63 | 411 |
| Ford | 159 | 23 | 66 |
| Mercedes(-Benz) | 130 | 22 | 44 |
| Audi | 87 | 5 | - |
| BMW | 81 | 16 | - |
| Toyota | 75 | 17 | 19 |
| Volkswagen | 73 | 9 | - |
| Honda | 42 | 4 | - |
| Hyundai | 27 | 4 | - |
| Kia | 27 | 5 | - |
| Chevrolet | 26 | - | - |
| General Motors | 26 | 3 | - |
| Stellantis | 24 | - | - |
| Nissan | 22 | 7 | 2 |
| Rivian | 4 | 1 | - |
| Lucid Motors | - | - | - |
| **Any mention** | **1,054 (0.494%)** | **160 (0.324%)** | **508 (0.652%)** |

## Reading these numbers

Tesla is the most-mentioned automaker in every dataset by a wide margin.
In LinkBoost-2025 it is nearly the only automaker discussed at
meaningful volume (411 of 508 total mentions, 81%). LinkBoost-2025's
content skews toward finance/investing (see
[investment-vc-content.md](investment-vc-content.md)), and Tesla shows
up there mainly as a stock/investment topic rather than as automotive
content.

podawaa2024 has the most manufacturer diversity (14 of 16 tracked
makers present, versus 12 in HyperClapper and 5 in LinkBoost-2025),
consistent with it being the broadest dataset in every other scan in
this repo.

LinkBoost-2025's near-total Tesla concentration means the dataset
does not discuss the auto industry broadly. It discusses one company,
largely as a finance/tech story.

## Caveats

Same as every keyword scan in this repo: a match means the maker's
name appears in the text, not that the post contains substantive or
accurate automotive commentary.
