# Immunotherapy content

`analysis/immunotherapy_content_scan.py` counts mentions of
immunotherapy-related terms across post content in all three datasets.
Same rules as every other scan in this repo: aggregate counts
only, no record, author, or matched text ever printed beyond the
duplicate-template check described below.

## A regex bug caught before it reached the committed script

An earlier draft used the pattern `\bCAR-?T\b` for "CAR-T" (a real
cell-therapy term), with the hyphen made optional to also catch "CAR T"
written as two words. Case-insensitive, that pattern also matches the
common word "cart" (shopping cart, price comparisons, abandoned-cart
marketing content) and dominated the raw counts with noise: 107, 60, and
58 false-positive matches in podawaa2024, HyperClapper, and
LinkBoost-2025 respectively, none of which were about cell therapy.
Sampling the matches directly (posts about online shopping, Shopify,
subscriptions, grocery habits) showed this immediately.

The shipped pattern requires "CAR-T" to appear with "cell" or "therapy"
nearby, which eliminates the false positives at the cost of missing a
bare "CAR-T" mention with no qualifying word attached, an acceptable
trade given the noise the unqualified pattern produced. This is the same
kind of error as the "TIME" magazine pattern documented in
[entity-mentions.md](entity-mentions.md), but it was caught before it
reached a committed script instead of after.

## A second false positive, caught by the duplicate-template safeguard

LinkBoost-2025's 40 "immunotherapy" matches all trace to a single post
- checked directly, it's a generic business-transformation/AI-
leadership post ("Transformation fails when we forget the human core...
how AI, values, and human creativity must work together") that happens
to use the word "immunotherapy" somewhere in its body, likely as a
passing example, boosted 40 times by the platform's structure. It is not
medical content.

## Results (VERIFIED: reproducible via the script)

| Dataset | Any mention | % of dataset |
|---|---|---|
| podawaa2024 | 16 | 0.0075% |
| HyperClapper | 0 | 0.0000% |
| LinkBoost-2025 | 40 raw / **0 corrected** | 0.0000% corrected |

**podawaa2024 term breakdown (the only dataset with genuine signal):**

| Term | Count |
|---|---|
| Immunotherapy | 11 |
| Monoclonal antibody/antibodies | 5 |
| Cancer immunotherapy | 2 |
| CAR-T (strict, cell/therapy context) | 1 |

## Reading these numbers

Genuine immunotherapy content is nearly absent across all
340,829 combined records: 16 real mentions total, all in podawaa2024.
This is the smallest genuine content category found in this project so
far, smaller even than [national-security-content.md](national-security-content.md)
(which had real, if sparse, content in all three datasets). HyperClapper
and LinkBoost-2025 have zero real immunotherapy content once the false
positives described above are accounted for.

## Caveats

Same as every keyword scan in this repo, with one extra warning: at
counts this small, a single mismatched acronym or a single off-topic
post using a term in passing can dominate or fabricate an apparent
finding. Both happened while building this scan. Check the underlying
text as well as the number for any low-count keyword result in this
project before drawing a conclusion from it.