# Blockchain / crypto content

`analysis/blockchain_crypto_scan.py` counts mentions of blockchain- and
crypto-related terms across post content in all three datasets. Same
rules as every other scan in this repo: aggregate counts only, no
record, author, or matched text ever printed beyond the
duplicate-template check described below.

## Results (VERIFIED: reproducible via the script)

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
checked manually. The top repeated strings (81, 80, 54, 49, 42
occurrences, none dominating) are distinct posts, consistent with that
dataset's known structure (a limited set of distinct target posts, each
logged multiple times), not a new artifact requiring correction.

## Reading these numbers

podawaa2024 has by far the highest rate: nearly 3% of the entire
dataset, roughly 4x HyperClapper's rate and 2.5x LinkBoost-2025's. A
duplicate-template or false-positive check does not explain this
divergence between datasets.

podawaa2024 is also the only dataset where "blockchain" itself, rather
than "crypto/cryptocurrency" generally, is the single largest term
(2,971 mentions). HyperClapper and LinkBoost-2025 both lean toward
"crypto/cryptocurrency" as the dominant phrasing instead.

**A plausible, but not confirmed, cross-dataset pattern**: podawaa2024
is 2024 data, while HyperClapper and LinkBoost-2025 are 2025 to 2026 data.
The large drop in blockchain/crypto-specific content alongside a shift
toward general "crypto" phrasing is consistent with a broader trend
already established elsewhere in this project: the topic taxonomy
shows `technology_ai` climbing sharply in the newer datasets (16.39% in
podawaa2024 to 27.97% in HyperClapper, per
[topic-taxonomy.md](topic-taxonomy.md)), suggesting attention in this kind of content may have shifted from blockchain/Web3 toward AI over
that period. This is INFERENCE-tier reasoning from two adjacent data
points across different time periods and different underlying
datasets. It is not a confirmed time-series trend, since no single dataset in this
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

<!-- half-year-section -->
## The half-year series

Added 18 November 2026. `analysis/crypto_half_year_scan.py` runs the same eight-term scan on a half-year axis. The scan above compares whole datasets, and the datasets come from different tools and different years, so a gap between them mixes time with tool. Here each post's date is decoded from its LinkedIn post ID (INFERENCE: [method](../method.md)): `linkedinPostId` in podawaa2024, the `urn:li:activity:` id in LinkBoost-2025's `Url`, and the 18 or 19 digit id in HyperClapper's `post_url`. Records with no decodable ID are counted as undated and left out of the rows. HyperClapper's `created_at` is not used, because it records when the tool captured the post. Each post counts once, by post ID, so LinkBoost-2025's repeated logging of one target post does not inflate a half-year. Nothing above this heading has changed.

"web3-era" counts posts with blockchain, NFT, Web3 or DeFi. "coin-era" counts posts with crypto, Bitcoin, Ethereum or altcoin. A post can fall in both. The term columns can overlap.

Command: `python3 analysis/crypto_half_year_scan.py podawaa /path/to/podawaa2024.json`.

```text
=== podawaa2024: 213,491 records, 201,000 distinct dated posts, 3,364 records with no decodable post ID ===
half-year    posts  any term       %  web3-era  coin-era blockchain     crypto    Bitcoin        NFT       Web3       DeFi
2018 H2          2         0    0.00         0         0          0          0          0          0          0          0
2020 H1        111         1    0.90         1         1          1          1          1          0          0          0
2020 H2      4,208        32    0.76        19        22         15         19         15          0          1          4
2021 H1     10,834       187    1.73       125       135        114        106         90         24          4         24
2021 H2     16,969       317    1.87       247       218        191        192         94         77         20         40
2022 H1     24,153       827    3.42       671       425        359        352        105        371        255         95
2022 H2     26,672       989    3.71       850       452        407        381         99        391        467         90
2023 H1     29,723     1,166    3.92     1,007       436        563        367        115        328        583        115
2023 H2     28,648       884    3.09       689       376        408        311        121        188        350         65
2024 H1     35,784       946    2.64       577       510        425        352        290         78        231         39
2024 H2     23,896       544    2.28       404       266        278        175        134         27        178         57
```

Command: `python3 analysis/crypto_half_year_scan.py hyperclapper /path/to/HyperClaper.json`.

```text
=== HyperClapper: 49,369 records, 48,475 distinct dated posts, 225 records with no decodable post ID ===
half-year    posts  any term       %  web3-era  coin-era blockchain     crypto    Bitcoin        NFT       Web3       DeFi
2019 H2          1         0    0.00         0         0          0          0          0          0          0          0
2020 H1          1         0    0.00         0         0          0          0          0          0          0          0
2021 H1          3         0    0.00         0         0          0          0          0          0          0          0
2021 H2          5         0    0.00         0         0          0          0          0          0          0          0
2022 H1          6         0    0.00         0         0          0          0          0          0          0          0
2022 H2        805        18    2.24        14         5          2          3          2          7          6          0
2023 H1        479         2    0.42         1         1          0          1          0          1          0          0
2023 H2        669         0    0.00         0         0          0          0          0          0          0          0
2024 H1        858         1    0.12         0         1          0          0          1          0          0          0
2024 H2      1,969        15    0.76         1        15          1          4         11          0          0          0
2025 H1      3,552        11    0.31         5         6          2          5          0          0          4          0
2025 H2     16,703       131    0.78        69        87         52         66         32          4         20         14
2026 H1     23,143       169    0.73        67       122         50        106         20          4         31         12
2026 H2        281         3    1.07         0         3          0          3          0          0          0          0
```

Command: `python3 analysis/crypto_half_year_scan.py linkboost /path/to/LinkBoost-2025.json`.

```text
=== LinkBoost-2025: 77,969 records, 3,129 distinct dated posts, 0 records with no decodable post ID ===
half-year    posts  any term       %  web3-era  coin-era blockchain     crypto    Bitcoin        NFT       Web3       DeFi
2024 H1          1         0    0.00         0         0          0          0          0          0          0          0
2024 H2          1         0    0.00         0         0          0          0          0          0          0          0
2025 H1          2         0    0.00         0         0          0          0          0          0          0          0
2025 H2      3,125        42    1.34        22        31          9         22         14          5          8          5
```

The three files give three different half-year coverages. podawaa2024 runs from 2020 H2 to 2024 H2, with 2024 H2 partial because the file ends in early November 2024. HyperClapper has fewer than 4,000 dated posts in each half-year before 2025 H2. LinkBoost-2025's 3,129 distinct dated posts are nearly all from 2025 H2, which reflects its structure of many records per target post. A rate from a half-year with a few thousand posts or fewer is too uncertain to read as a trend.

Read together, the rows give a rise inside podawaa2024 from 0.76% (2020 H2) to 3.92% (2023 H1) and a fall to 2.28% (2024 H2). In 2024 H2, the one half-year that podawaa2024 and HyperClapper share, the rates are 2.28% and 0.76%. In 2025 H2, HyperClapper and LinkBoost-2025 give 0.78% and 1.34%. These are keyword matches in the posts each tool holds, not findings about the posts or their authors. The write-up is [Crypto Posts Rose Fivefold, Then Fell by Two-Fifths, Inside One Tool's Files](../articles/crypto-posts-rose-fivefold-then-fell-by-two-fifths.md).
