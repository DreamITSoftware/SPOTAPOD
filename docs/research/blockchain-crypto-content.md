# Blockchain / crypto content

`analysis/blockchain_crypto_scan.py` counts mentions of blockchain- and
crypto-related terms across post content in all three datasets. Same
discipline as every other scan in this repo: aggregate counts only, no
record, author, or matched text ever printed beyond the
duplicate-template check described below.

## Results (VERIFIED - reproducible via the script)

| Dataset | Any mention | % of dataset |
|---|---|---|
| podawaa2024 | 6,255 | 2.930% |
| HyperClapper | 382 | 0.774% |
| LinkBoost-2025 | 921 | 1.181% |

**Term breakdown:**

| Term | podawaa2024 | HyperClapper | LinkBoost-2025 |
|---|---|---|---|
| Blockchain | 2,971 | 113 | 221 |
| Crypto/cryptocurrency | 2,361 | 196 | 567 |
| Web3 | 2,251 | 65 | 231 |
| NFT | 1,541 | 19 | 134 |
| Bitcoin | 1,112 | 87 | 254 |
| DeFi | 551 | 29 | 74 |
| Ethereum | 515 | 29 | 178 |
| Altcoin | 82 | 2 | - |

LinkBoost-2025's lower distinct-string count (63 for 921 matches) was
checked manually - the top repeated strings (81, 80, 54, 49, 42
occurrences, none dominating) are genuinely distinct posts, consistent
with that dataset's known structure (a limited set of distinct target
posts, each logged multiple times), not a new artifact requiring
correction.

## Reading these numbers

podawaa2024 has by far the highest rate - nearly 3% of the entire
dataset, roughly 4x HyperClapper's rate and 2.5x LinkBoost-2025's. This
is a real, meaningful divergence between datasets, not something a
duplicate-template or false-positive check explains away.

podawaa2024 is also the only dataset where "blockchain" itself, rather
than "crypto/cryptocurrency" generally, is the single largest term
(2,971 mentions). HyperClapper and LinkBoost-2025 both lean toward
"crypto/cryptocurrency" as the dominant phrasing instead.

**A plausible, but not confirmed, cross-dataset pattern**: podawaa2024
is 2024 data, while HyperClapper and LinkBoost-2025 are 2025-2026 data.
The large drop in blockchain/crypto-specific content alongside a shift
toward general "crypto" phrasing is consistent with a broader trend
already established elsewhere in this project - the topic taxonomy
shows `technology_ai` climbing sharply in the newer datasets (16.39% in
podawaa2024 to 27.97% in HyperClapper, per
[topic-taxonomy.md](topic-taxonomy.md)), suggesting attention in this
content ecosystem may have shifted from blockchain/Web3 toward AI over
that period. This is INFERENCE-tier reasoning from two adjacent data
points across different time periods and different underlying
datasets, not a confirmed time-series trend - no single dataset in this
project tracks the same population over time.

## Caveats

Same as every keyword scan in this repo: a match means the term
appears in the text, not that the post contains genuine, accurate, or
substantive blockchain/crypto commentary.
