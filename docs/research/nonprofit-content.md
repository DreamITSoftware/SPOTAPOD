# Nonprofit-related content

`analysis/nonprofit_content_scan.py` counts mentions of nonprofit-related
terms (charity, nonprofit, NGO, philanthropy, 501(c)(3)) across post
content and, where available, occupation/headline text. Same discipline
as every other scan in this repo: aggregate counts only, no record,
author, or matched text ever printed.

## The safeguard this script has that earlier ones didn't

A first, manual pass at this question found a 1.38% "any mention" rate
in HyperClaper's headline field \u2014 the highest of any field checked \u2014
which looked like a real, notable signal. It wasn't. Checking the
underlying text showed all but 23 of those 681 matching records shared
the exact same headline, repeated 658 times, because HyperClaper's
structure logs one row per reciprocal-engagement action and captures
that account's headline snapshot every time. The corrected rate, once
that single repeated string is treated as one occurrence rather than
658, is 0.05% \u2014 the lowest of any field checked, not the highest.

`nonprofit_content_scan.py` builds that check in permanently. For every
field, it reports both the raw record count and the number of distinct
underlying text values behind it, and prints an explicit warning
whenever a single repeated string accounts for 20% or more of the
matching records. Running it surfaced two more instances of the same
distortion that the original manual check hadn't caught, in
LinkBoost-2025's Title and Occupation fields.

## Results (VERIFIED \u2014 reproducible via the script)

| Field | Raw "any mention" | Distinct strings | Dominant string | Corrected rate |
|---|---|---|---|---|
| podawaa2024 \u2014 Content | 657 (0.308%) | 616 | none flagged | 0.308% (no correction needed) |
| HyperClaper \u2014 post_title | 142 (0.288%) | 141 | none flagged | 0.288% (no correction needed) |
| HyperClaper \u2014 headline | 681 (1.379%) | 5 | 658 records (96.6%) | **0.049%** |
| LinkBoost-2025 \u2014 Title | 413 (0.530%) | 21 | 99 records (24.0%) | **0.404%** |
| LinkBoost-2025 \u2014 Occupation | 120 (0.154%) | 3 | 67 records (55.8%) | **0.069%** |

Only podawaa2024's Content field and HyperClaper's post_title field have
enough distinct strings behind their raw counts (616 of 657, and 141 of
142) to trust the raw percentage directly. Every other field needed the
correction shown above.

### Term breakdown (raw, pre-correction \u2014 see table above for which fields need adjusting)

| Term | podawaa2024 | HyperClaper (posts) | HyperClaper (headline) | LinkBoost-2025 (Title) | LinkBoost-2025 (Occupation) |
|---|---|---|---|---|---|
| Charity / charitable | 279 | 77 | 658\u2020 | 248\u2020 | 29 |
| Nonprofit / non-profit | 221 | 45 | 10 | 51 | \u2014 |
| Philanthropy / philanthropic | 147 | 22 | 5 | 111\u2020 | 91\u2020 |
| NGO | 77 | 8 | 13 | 3 | \u2014 |
| Nonprofit organization | 27 | 3 | \u2014 | \u2014 | \u2014 |
| 501(c)(3) | 10 | 2 | \u2014 | \u2014 | \u2014 |

\u2020 Term totals in flagged fields include the dominant repeated string;
see the corrected-rate table above for the field-level adjustment. The
script does not break the correction down per term, only per field.

## Reading these numbers

Once corrected, genuine nonprofit-related content sits consistently in
a narrow band \u2014 roughly 0.05% to 0.40% \u2014 across every dataset and
field. There's no meaningful nonprofit-sector concentration anywhere in
this data; these are professional/business/marketing datasets, and the
presence of charity or philanthropy language is small and unremarkable
once duplicate profile snapshots and repeated templates are accounted
for.

## Caveats

Same as every keyword scan in this repo: a match means the term appears
in the text, not that the account or post is meaningfully affiliated
with a nonprofit. The duplicate-template warning threshold (20% of
matching records sharing one string) is a heuristic, not a certainty \u2014
a field that doesn't trigger it can still contain some duplication, just
not enough to dominate the total.
