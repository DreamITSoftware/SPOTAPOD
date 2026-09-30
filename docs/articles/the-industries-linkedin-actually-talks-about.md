# The Industries LinkedIn Actually Talks About

### Retail leads in two datasets, then falls to last place in the third. It's not a mistake

Real estate, insurance, manufacturing, retail, healthcare, energy and ESG. Checked across three LinkedIn datasets, these six industry categories together form the single largest niche-topic category this project has measured: 14,533 mentions (6.807%) in one dataset, 5,038 (10.205%) in a second, 4,742 (6.082%) in a third. HyperClapper's 10.2% rate is the highest "any mention" figure found anywhere in this project outside broad entity-mention and topic-taxonomy work.

## The industry that swaps places

| Term | podawaa2024 | HyperClapper | LinkBoost-2025 |
|---|---|---|---|
| Retail / e-commerce | 5,308 | 3,071 | 770 |
| Healthcare / hospital | 2,310 | 754 | 1,745 |
| Manufacturing / supply chain | 2,620 | 577 | 848 |
| Energy / climate / ESG | 3,364 | 338 | 772 |
| Insurance | 1,227 | 275 | 752 |
| Real estate | 949 | 348 | 633 |

Retail leads comfortably in podawaa2024 and HyperClapper. In LinkBoost-2025, it drops to dead last, while healthcare and hospital content takes the top spot instead. Checked directly, this isn't an artifact of the scan. A sample of podawaa2024's retail matches confirmed genuine signal (real posts about retail products, retail spaces, retail hashtags), and LinkBoost-2025's lower distinct-string ratio was checked and found to be genuinely varied content, not one dominating template.

## Why a real compositional difference matters more than a bug

It would be easy to assume any dataset-to-dataset swing this large is a keyword-matching error. It isn't, here. It's a real difference in what each dataset's underlying content population actually talks about. That's a more interesting finding than a bug would have been: three different slices of LinkedIn carry three different industry profiles, and the differences hold up under direct manual review.

## What this is, and isn't

**VERIFIED**, reproducible via the published scan: the mention counts and rankings above, cross-checked manually for both the retail matches and the LinkBoost-2025 distinct-string question.

Full methodology: **github.com/DreamITSoftware/SPOTAPOD**.

---

*Self-published. Not peer-reviewed. Independently reproducible from the source files.*
