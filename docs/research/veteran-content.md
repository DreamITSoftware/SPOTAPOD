# Veteran / military content

`analysis/veteran_content_scan.py` counts mentions of veteran- and
military-related terms across post content in all three datasets. Same
discipline as every other scan in this repo: aggregate counts only, no
record, author, or matched text ever printed beyond the
duplicate-template check described below. No individual is identified
by name in this script's output or in this document.

## Another appearance of an already-documented artifact

The duplicate-template safeguard fires on LinkBoost-2025: 97 of its 476
matches trace to the same repeated political campaign-endorsement post
already documented - without naming the candidate - in
[decision-points.md](decision-points.md) and
[political-content.md](political-content.md). That post describes the
candidate as a "decorated 20-year veteran and combat aviator," which is
why it surfaces here too. Corrected, LinkBoost-2025's real any-mention
count is 380, not 476.

**Unlike that artifact, the rest of LinkBoost-2025's veteran content is
genuine and substantive.** The remaining matches are real, distinct
tributes to Indian Armed Forces personnel - a fighter pilot's widow
continuing his legacy, a soldier's wife honoring her husband, a young
army doctor killed saving fellow soldiers, a third-generation officer.
This is a meaningfully different character than most niche categories
checked in this repo, similar to the genuine advocacy content found
alongside a duplicate template in
[homelessness-content.md](homelessness-content.md).

## Results (VERIFIED - reproducible via the script)

| Term | podawaa2024 | HyperClapper | LinkBoost-2025 |
|---|---|---|---|
| Veteran(s) | 444 | 77 | 476 |
| Armed forces | 20 | 29 | 219 |
| Service member(s) | 25 | 1 | - |
| Veteran-owned | 15 | 1 | - |
| Combat veteran | 2 | 2 | - |
| Veterans Affairs / VA benefits | 6 | - | - |
| Disabled veteran | - | 1 | - |
| Military veteran | - | 1 | - |
| Ex-military | 2 | - | - |
| **Any mention (raw)** | **472 (0.221%)** | **82 (0.166%)** | **476 (0.610%)** |
| **Any mention (corrected)** | 472 (no correction needed) | 82 (no correction needed) | **380 (0.488%)** |

## Reading these numbers

podawaa2024 shows the most diverse term usage - the only dataset with
meaningful "veteran-owned" business content and "VA benefits"
mentions, suggesting some genuine veteran-entrepreneurship and
benefits-related content specifically in that dataset. HyperClapper has
the smallest and least diverse veteran-related presence of the three.

## A note on a term deliberately excluded

Bare "VA" is not checked in this scan, unlike some short acronyms
elsewhere in this repo (see the "MIT" case-sensitivity fix in
[university-content.md](university-content.md) for a related lesson).
"VA" collides too readily with the state abbreviation for Virginia and
other unrelated uses to be reliable even with a case constraint; only
"Veterans Affairs," "VA benefits," "VA loan," and "VA disability" are
checked, each of which requires enough surrounding context to be
trustworthy on its own.

## Caveats

Same as every keyword scan in this repo: a match means the term
appears in the text, not that the account or post has a verified
connection to military or veteran status.

<!-- export65-section -->
## The 65 export files

Added 22 October 2026. This is the same scan run on the 65 export files: 56,363 distinct records after the files are de-duplicated on record id, reading each record's `title` field, which holds the post text. These files are a separate set from the three datasets above, and nothing above this heading has changed. Their source, method and limits are in [provenance.md](../provenance.md#the-65-export-files) and [export-65-profile.md](export-65-profile.md). Rates use all 56,363 records as the denominator, and 237 of them have no post text. Command: `python3 analysis/veteran_content_scan.py export65 /path/to/folder_with_the_65_files`.

```text
=== 65 export files (56,363 records) ===
Records mentioning any veteran/military term: 213 (0.378%)
Distinct underlying text values: 210
    veteran(s)                         187
    armed forces                       64
    service member(s)                  9
    ex-military                        4
    Veterans Affairs / VA benefits     2
    combat veteran                     1
    military veteran                   1
```

213 of 56,363 records (0.378%) match. In the three datasets above the same measure is 0.221% in podawaa2024, 0.166% in HyperClapper and 0.488% in LinkBoost-2025 (using the corrected figure where this page gives one), which puts the 65 export files at the second highest of the four. The scan's duplicate-template check did not fire, and the matching records hold 210 distinct texts.

The rates come from different fields and different kinds of record, so a gap between them describes the files and does not describe the tools. A match is a keyword in the text, not a finding about the post or its author.
