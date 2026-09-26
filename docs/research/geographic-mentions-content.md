# Geographic content mentions

`analysis/geographic_mentions_scan.py` counts mentions of countries and
regions as CONTENT SUBJECT MATTER - a post actually discussing India,
China, Europe, and so on - across post content in all three datasets.
This is distinct from [demographics.md](demographics.md), which covers
self-reported location METADATA about accounts, not what a post's text
is about. Same discipline as every other scan in this repo: aggregate
counts only, no record, author, or matched text ever printed beyond the
duplicate-template check below.

## Results (VERIFIED - reproducible via the script)

| Term | podawaa2024 | HyperClapper | LinkBoost-2025 |
|---|---|---|---|
| India | 1,731 | 2,023 | 1,525 |
| Europe | 2,800 | 850 | 231 |
| China | 559 | 228 | 306 |
| Africa | 1,099 | 87 | 131 |
| United States / America | 357 | 86 | 8 |
| Middle East | 332 | 86 | 40 |
| United Kingdom / Britain | 103 | 19 | 51 |
| **Any mention** | **6,421 (3.008%)** | **3,180 (6.441%)** | **2,190 (2.809%)** |

LinkBoost-2025's lower distinct-string ratio (154 for 2,190 matches)
was checked manually - the top repeated strings (a retail-street-shop
tribute post, an AI-productivity post, a "life can only be understood
backwards" quote post) are genuinely distinct, none dominating, so no
correction is needed.

## Reading these numbers

Europe leads podawaa2024 by a wide margin (2,800, nearly double
India's count there), but India leads both HyperClapper and
LinkBoost-2025 - and by the widest margin of any single term in either
dataset. This lines up directly with the geographic *account* metadata
already documented in [demographics.md](demographics.md), where
HyperClapper's location field skews heavily toward Delhi, Gurugram, and
Bengaluru: the content people post about tracks the geography of who's
posting, which is an intuitive but still useful confirmation that these
two independently collected signals (what accounts say they're located,
and what countries their posts actually discuss) point the same
direction.

The United States is a surprisingly minor presence everywhere,
especially in LinkBoost-2025 (8 mentions total, the smallest figure in
this entire table) - notable given that dataset's Occupation field
skewed toward executive/leadership content in
[demographics.md](demographics.md) and its country field led with the
US at 21.8% there. Account location and content subject matter clearly
diverge for this dataset specifically.

## Caveats

Same as every keyword scan in this repo: a match means the country or
region name appears in the text, not that the post contains substantive
commentary about that place. This scan also does not capture every
possible country or region - only the seven checked above - so absence
from this table does not mean absence from the data.
