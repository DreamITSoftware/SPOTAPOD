# Industry verticals

`analysis/industry_verticals_scan.py` counts mentions of real estate,
insurance, manufacturing/supply chain, retail/e-commerce,
healthcare/hospital, and energy/climate/ESG/sustainability terms across
post content in all three datasets. Same discipline as every other
scan in this repo: aggregate counts only, no record, author, or matched
text ever printed beyond the duplicate-template check below.

## Results (VERIFIED - reproducible via the script)

| Term | podawaa2024 | HyperClapper | LinkBoost-2025 |
|---|---|---|---|
| Retail / e-commerce | 5,308 | 3,071 | 770 |
| Healthcare / hospital | 2,310 | 754 | 1,745 |
| Manufacturing / supply chain | 2,620 | 577 | 848 |
| Energy / climate / ESG / sustainability | 3,364 | 338 | 772 |
| Insurance | 1,227 | 275 | 752 |
| Real estate | 949 | 348 | 633 |
| **Any mention** | **14,533 (6.807%)** | **5,038 (10.205%)** | **4,742 (6.082%)** |

This is the largest niche-topic category found in this project to
date - HyperClapper's 10.2% rate is the highest "any mention" figure of
any scan documented in this repo outside the entity-mention and topic-
taxonomy work.

LinkBoost-2025's lower distinct-string ratio (263 for 4,742 matches)
was checked manually - the top repeated strings (a "tribute to
responsible mothers" post, a "life is like a piano" post, and other
already-familiar LinkBoost templates) are genuinely distinct and none
individually dominates, consistent with that dataset's known structure.

## Reading these numbers

"Retail/e-commerce" leads in both podawaa2024 and HyperClapper, but
drops to last place in LinkBoost-2025, where "healthcare/hospital"
leads instead - a real compositional difference between datasets, not
an artifact. A sample check of podawaa2024's retail matches confirmed
genuine signal (posts about retail products, retail spaces, and retail
hashtags), not noise from an overly broad term.

HyperClapper's overall rate (10.2%) is notably higher than the other
two, consistent with its broader lean toward business/professional
content already established via its elevated corporation-mention rates
in [entity-mentions.md](entity-mentions.md).

## Caveats

Same as every keyword scan in this repo: a match means the term
appears in the text, not that the post contains substantive or accurate
industry-specific commentary.
