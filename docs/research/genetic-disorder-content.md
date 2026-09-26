# Genetic disorder content

`analysis/genetic_disorder_scan.py` counts mentions of genetic-
disorder-related terms (genetic disorder(s), genetic condition(s),
genetic disease(s), genetic mutation(s), hereditary disease/condition,
inherited disorder(s), Down syndrome, cystic fibrosis, sickle cell)
across post content in all three datasets. Same discipline as every
other scan in this repo: aggregate counts only, no record, author, or
matched text ever printed beyond the duplicate-template check
described below.

This is a health-adjacent, sensitive topic. Every match reported here
is purely a keyword hit in public post text. No claim is made or
implied about any specific individual's actual health status, genetic
makeup, or diagnosis - this script measures how often terms appear in
text, nothing more.

## LinkBoost-2025's correction: one post, not 46

All 46 of LinkBoost-2025's "genetic condition(s)" matches trace to a
single post - checked directly, it's a genuine, substantive excerpt
from a Cathie Wood interview discussing AI and genomics in healthcare,
naming "rare genetic conditions" alongside cancer and chronic illness
as diseases AI-driven medicine might eventually address. This is real
content, not a false positive, but it is one post boosted 46 times by
the platform's structure, not 46 distinct mentions. Corrected,
LinkBoost-2025's real count is 1.

## Results (VERIFIED - reproducible via the script)

| Term | podawaa2024 | HyperClapper | LinkBoost-2025 |
|---|---|---|---|
| Down syndrome | 17 | 1 | - |
| Genetic disease(s) | 3 | - | - |
| Genetic disorder(s) | 2 | - | - |
| Sickle cell | 2 | - | - |
| Genetic mutation(s) | 2 | - | - |
| Cystic fibrosis | 2 | - | - |
| Inherited disorder(s) | 1 | - | - |
| Genetic condition(s) | - | - | 46 |
| **Any mention (raw)** | **27 (0.0127%)** | **1 (0.0020%)** | **46 (0.0590%)** |
| **Any mention (corrected)** | 27 (no correction needed) | 1 (no correction needed) | **1 (0.0013%)** |

## Reading these numbers

This is one of the smallest content categories found in this project,
comparable to [narcissist-content.md](narcissist-content.md) and
[immunotherapy-content.md](immunotherapy-content.md). podawaa2024 has
the most genuine diversity across named conditions, led by Down
syndrome (17 of 27 total). HyperClapper has essentially none. Once
corrected, LinkBoost-2025's entire contribution to this category is a
single post.

## Caveats

Same as every keyword scan in this repo, with extra emphasis given the
topic: a match means the term appears in the text, not that any post
or account has any connection to a real diagnosis, condition, or
genetic status. No individual's health information is identified,
inferred, or reported anywhere in this document or the underlying
script's output.
