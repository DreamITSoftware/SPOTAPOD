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

<!-- export65-section -->
## The 65 export files

Added 22 October 2026. This is the same scan run on the 65 export files: 56,363 distinct records after the files are de-duplicated on record id, reading each record's `title` field, which holds the post text. These files are a separate set from the three datasets above, and nothing above this heading has changed. Their source, method and limits are in [provenance.md](../provenance.md#the-65-export-files) and [export-65-profile.md](export-65-profile.md). Rates use all 56,363 records as the denominator, and 237 of them have no post text. Command: `python3 analysis/blockchain_crypto_scan.py export65 /path/to/folder_with_the_65_files`.

```text
=== 65 export files (56,363 records) ===
Records mentioning any blockchain/crypto term: 578 (1.025%)
Distinct underlying text values: 566
    crypto / cryptocurrency      333
    blockchain                   200
    Bitcoin                      150
    Web3                         78
    DeFi                         58
    Ethereum                     44
    NFT                          13
    altcoin                      10
```

578 of 56,363 records (1.025%) mention a blockchain or crypto term. The three datasets above give 2.930% (podawaa2024), 0.774% (HyperClapper) and 1.181% (LinkBoost-2025), so the 65 export files sit at the second lowest of the four. The most frequent term is crypto or cryptocurrency (333 records), then blockchain (200) and Bitcoin (150). NFT appears in 13 records in the 65 files, against 1,541 in podawaa2024. The scan's duplicate-template check did not fire, and the matching records hold 566 distinct texts.

The rates come from different fields and different kinds of record, so a gap between them describes the files and does not describe the tools. A match is a keyword in the text, not a finding about the post or its author.
