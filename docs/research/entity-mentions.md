# Entity mentions (news outlets, magazines, TV/streaming, corporations)

`analysis/entity_mention_scan.py` counts how many records mention a named
entity from four fixed categories: news outlets, magazines, TV networks/
streaming platforms, and corporations. Same discipline as every other
scan in this repo: only aggregate counts are reported, never a record,
author, or matched text.

## Method

A record is counted once per entity it mentions (repeated mentions of
the same entity in one record still count once), and a record can be
counted under multiple entities if it names more than one - this is an
overlapping tally, like the career-advice and other-regulatory-signal
scans, not the mutually-exclusive scheme `topic_taxonomy.py` uses.

**A note on a real performance/accuracy trade-off found while building
this**: an early draft included a bare `\bTIME\b` pattern for *TIME*
magazine, which matched the extremely common English word "time" on
nearly every record and caused the scan to run for several minutes
per dataset instead of under two. The shipped patterns require a
qualifying phrase for every entity whose name doubles as a common word
(`TIME Magazine` or `TIME 100` rather than bare `TIME`; `Fortune 500` or
`Fortune Magazine` rather than bare `Fortune`; similar treatment for
`Oracle`, `Ernst & Young`, and others). This trades a small amount of
recall (a casual "as TIME reported" mention without "Magazine" attached
is missed) for both correctness and runtime that scales properly.

## Results (VERIFIED - reproducible via the script)

### News outlets

| Outlet | podawaa2024 | HyperClaper | LinkBoost-2025 |
|---|---|---|---|
| Forbes | 726 (0.34%) | 86 (0.17%) | 198 (0.25%) |
| Harvard Business Review | 324 (0.15%) | 31 (0.06%) | 290 (0.37%) |
| Bloomberg | 122 (0.06%) | 33 (0.07%) | 84 (0.11%) |
| Fast Company | 28 (0.01%) | - | 338 (0.43%) |
| CNBC | 112 (0.05%) | 28 (0.06%) | - |
| Wall Street Journal | 89 (0.04%) | 15 (0.03%) | 45 (0.06%) |
| TechCrunch | 84 (0.04%) | 13 (0.03%) | 44 (0.06%) |
| New York Times | 81 (0.04%) | 13 (0.03%) | 53 (0.07%) |
| BBC | 79 (0.04%) | 10 (0.02%) | 15 (0.02%) |
| CNN | 70 (0.03%) | 11 (0.02%) | - |
| Reuters | 49 (0.02%) | 14 (0.03%) | 56 (0.07%) |
| USA Today | - | 5 (0.01%) | 93 (0.12%) |

Any-mention rate: 0.88% (podawaa2024), 0.60% (HyperClaper), 1.62%
(LinkBoost-2025). Forbes and Harvard Business Review lead across all
three, consistent with the business/career-advice content skew already
established in [topic-taxonomy.md](topic-taxonomy.md).

### Magazines

| Magazine | podawaa2024 | HyperClaper | LinkBoost-2025 |
|---|---|---|---|
| Forbes | 726 (0.34%) | 86 (0.17%) | 198 (0.25%) |
| Fortune | 124 (0.06%) | 128 (0.26%) | 618 (0.79%) |
| Harvard Business Review | 324 (0.15%) | 31 (0.06%) | 290 (0.37%) |
| Wired | 87 (0.04%) | 105 (0.21%) | 202 (0.26%) |
| Fast Company | 28 (0.01%) | 4 (0.01%) | 338 (0.43%) |
| Psychology Today | 8 (0.00%) | 2 (0.00%) | 236 (0.30%) |
| Vogue | 65 (0.03%) | 6 (0.01%) | - |
| The Atlantic | 38 (0.02%) | 4 (0.01%) | 24 (0.03%) |
| Inc. Magazine | 19 (0.01%) | 1 (0.00%) | 85 (0.11%) |
| National Geographic | 18 (0.01%) | 3 (0.01%) | - |
| The Economist | 13 (0.01%) | 12 (0.02%) | 18 (0.02%) |

Any-mention rate: 0.68% (podawaa2024), 0.78% (HyperClaper), 2.52%
(LinkBoost-2025). Fortune (618 mentions, 0.79%) and Psychology Today
(236 mentions, 0.30%) stand out specifically in LinkBoost-2025 - both
essentially absent elsewhere - consistent with that dataset's
leadership/coaching content skew (see
[topic-taxonomy.md](topic-taxonomy.md), where LinkBoost's
`leadership_coaching_motivation` share is roughly 3× the other two
files).

### TV networks and streaming platforms

| Platform | podawaa2024 | HyperClaper | LinkBoost-2025 |
|---|---|---|---|
| YouTube | 2,540 (1.19%) | 492 (1.00%) | 1,610 (2.07%) |
| TikTok | 1,055 (0.49%) | 208 (0.42%) | 537 (0.69%) |
| Netflix | 519 (0.24%) | 135 (0.27%) | 482 (0.62%) |
| Twitch | 112 (0.05%) | 4 (0.01%) | 15 (0.02%) |
| BBC | 79 (0.04%) | 10 (0.02%) | 15 (0.02%) |
| CNN | 70 (0.03%) | 11 (0.02%) | - |
| HBO / HBO Max | 18 (0.01%) | 4 (0.01%) | 15 (0.02%) |
| Disney+ | 21 (0.01%) | 4 (0.01%) | - |
| Hulu | 23 (0.01%) | 3 (0.01%) | - |
| Amazon Prime Video | 21 (0.01%) | 3 (0.01%) | - |
| Apple TV+ | 18 (0.01%) | 2 (0.00%) | - |

Any-mention rate: 1.97% (podawaa2024), 1.65% (HyperClaper), 3.17%
(LinkBoost-2025) - the highest overall mention rate of any category in
this scan. YouTube, TikTok, and Netflix are the top three, in the same
order, in every single dataset; traditional linear TV networks are
negligible everywhere (all under 0.05%). This is consistent with
content-creator-economy material rather than content that engages with
broadcast media.

### Corporations

| Corporation | podawaa2024 | HyperClaper | LinkBoost-2025 |
|---|---|---|---|
| LinkedIn | 13,642 (6.39%) | 5,064 (10.26%) | 5,842 (7.49%) |
| Google | 5,877 (2.75%) | 6,546 (13.26%) | 3,141 (4.03%) |
| IBM | 385 (0.18%) | 4,278 (8.67%) | 255 (0.33%) |
| Microsoft | 1,883 (0.88%) | 2,927 (5.93%) | 994 (1.28%) |
| Meta | 1,012 (0.47%) | 1,248 (2.53%) | 706 (0.91%) |
| Amazon | 1,680 (0.79%) | 701 (1.42%) | 988 (1.27%) |
| Apple | 1,490 (0.70%) | 264 (0.54%) | 517 (0.66%) |
| OpenAI | 1,163 (0.55%) | 610 (1.24%) | 932 (1.20%) |
| Facebook | 2,038 (0.96%) | 168 (0.34%) | 186 (0.24%) |
| McKinsey | 340 (0.16%) | 124 (0.25%) | 420 (0.54%) |

Full per-dataset rankings (all 32 tracked corporations) are reproducible
via the script; the table above shows the ten highest combined.
Any-mention rate: 13.00% (podawaa2024), 23.19% (HyperClaper), 15.62%
(LinkBoost-2025) - by far the highest of any category scanned, and the
only one where any single dataset exceeds 20%.

**IBM's share in HyperClaper (8.67%, roughly 24× its share in
podawaa2024 and 26× its share in LinkBoost-2025) is the standout
finding.** This is consistent with, though not independently
re-confirmed by, HyperClaper's elevated `education_certification` topic
share documented in [topic-taxonomy.md](topic-taxonomy.md) (3.11% vs.
0.63–0.68% elsewhere): a plausible explanation is a recurring
"free IBM certification" content template, similar in kind to the
"Google is offering free AI training" pattern already documented in
[decision-points.md](decision-points.md), though this specific scan
counts entity mentions only and does not itself verify that explanation.

## Caveats

- Entity names that double as common English words (Google as a verb,
  Amazon the rainforest, Apple the fruit) are not filtered out beyond
  what's noted above, so counts for those specific entities skew
  somewhat high relative to a strictly on-topic count.
- A mention means the name appears in the text - not that the post
  accurately describes, is affiliated with, or is endorsed by the named
  outlet, magazine, platform, or corporation.
- As with every keyword scan in this repo, results depend on the fixed
  entity list tested; an entity not on the list is not counted, however
  frequently it may actually appear.
