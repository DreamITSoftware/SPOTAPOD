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

| Outlet | podawaa2024 | HyperClapper | LinkBoost-2025 |
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

Any-mention rate: 0.88% (podawaa2024), 0.60% (HyperClapper), 1.62%
(LinkBoost-2025). Forbes and Harvard Business Review lead across all
three, consistent with the business/career-advice content skew already
established in [topic-taxonomy.md](topic-taxonomy.md).

### Magazines

| Magazine | podawaa2024 | HyperClapper | LinkBoost-2025 |
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

Any-mention rate: 0.68% (podawaa2024), 0.78% (HyperClapper), 2.52%
(LinkBoost-2025). Fortune (618 mentions, 0.79%) and Psychology Today
(236 mentions, 0.30%) stand out specifically in LinkBoost-2025 - both
essentially absent elsewhere - consistent with that dataset's
leadership/coaching content skew (see
[topic-taxonomy.md](topic-taxonomy.md), where LinkBoost's
`leadership_coaching_motivation` share is roughly 3× the other two
files).

### TV networks and streaming platforms

| Platform | podawaa2024 | HyperClapper | LinkBoost-2025 |
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

Any-mention rate: 1.97% (podawaa2024), 1.65% (HyperClapper), 3.17%
(LinkBoost-2025) - the highest overall mention rate of any category in
this scan. YouTube, TikTok, and Netflix are the top three, in the same
order, in every single dataset; traditional linear TV networks are
negligible everywhere (all under 0.05%). This is consistent with
content-creator-economy material rather than content that engages with
broadcast media.

### Corporations

| Corporation | podawaa2024 | HyperClapper | LinkBoost-2025 |
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
Any-mention rate: 13.00% (podawaa2024), 23.19% (HyperClapper), 15.62%
(LinkBoost-2025) - by far the highest of any category scanned, and the
only one where any single dataset exceeds 20%.

**IBM's share in HyperClapper (8.67%, roughly 24× its share in
podawaa2024 and 26× its share in LinkBoost-2025) is the standout
finding.** This is consistent with, though not independently
re-confirmed by, HyperClapper's elevated `education_certification` topic
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

<!-- export65-section -->
## The 65 export files

Added 22 October 2026. This is the same scan run on the 65 export files: 56,363 distinct records after the files are de-duplicated on record id, reading each record's `title` field, which holds the post text. These files are a separate set from the three datasets above, and nothing above this heading has changed. Their source, method and limits are in [provenance.md](../provenance.md#the-65-export-files) and [export-65-profile.md](export-65-profile.md). Rates use all 56,363 records as the denominator, and 237 of them have no post text. Command: `python3 analysis/entity_mention_scan.py export65 /path/to/folder_with_the_65_files --category all`.

```text
=== 65 export files - news_outlets (56,363 records, 43.0s) ===
Records mentioning any tracked entity: 801 (1.42%)
  Forbes                     242 (0.429%)
  Harvard Business Review    92 (0.163%)
  TechCrunch                 87 (0.154%)
  Reuters                    77 (0.137%)
  Fast Company               62 (0.110%)
  Bloomberg                  41 (0.073%)
  CNBC                       40 (0.071%)
  New York Times             34 (0.060%)
  Wall Street Journal        33 (0.059%)
  BBC                        22 (0.039%)
  Business Insider           20 (0.035%)
  CNN                        18 (0.032%)
  The Economist              18 (0.032%)
  The Guardian               13 (0.023%)
  Washington Post            9 (0.016%)
  USA Today                  8 (0.014%)
  Fox News                   7 (0.012%)
  Axios                      6 (0.011%)
  NPR                        5 (0.009%)
  Politico                   2 (0.004%)
  HuffPost                   2 (0.004%)
  NBC News                   2 (0.004%)
  MSNBC                      1 (0.002%)
  ABC News                   1 (0.002%)
  Newsweek                   1 (0.002%)

=== 65 export files - magazines (56,363 records, 32.6s) ===
Records mentioning any tracked entity: 750 (1.33%)
  Forbes                     242 (0.429%)
  Fortune                    169 (0.300%)
  Wired                      113 (0.200%)
  Harvard Business Review    92 (0.163%)
  Fast Company               62 (0.110%)
  Psychology Today           24 (0.043%)
  The Economist              18 (0.032%)
  The Atlantic               16 (0.028%)
  Inc. Magazine              8 (0.014%)
  Vogue                      8 (0.014%)
  Entrepreneur Magazine      5 (0.009%)
  TIME Magazine              5 (0.009%)
  Bloomberg Businessweek     2 (0.004%)
  Rolling Stone              1 (0.002%)
  Vanity Fair                1 (0.002%)
  National Geographic        1 (0.002%)
  Newsweek                   1 (0.002%)

=== 65 export files - tv_streaming (56,363 records, 37.6s) ===
Records mentioning any tracked entity: 1,172 (2.08%)
  YouTube                    570 (1.011%)
  TikTok                     306 (0.543%)
  Netflix                    270 (0.479%)
  HBO / HBO Max              23 (0.041%)
  BBC                        22 (0.039%)
  CNN                        18 (0.032%)
  Amazon Prime Video         8 (0.014%)
  Fox News                   7 (0.012%)
  CBS                        6 (0.011%)
  Disney+                    6 (0.011%)
  Twitch                     5 (0.009%)
  Apple TV+                  4 (0.007%)
  PBS                        4 (0.007%)
  NBC                        2 (0.004%)
  Hulu                       2 (0.004%)
  Paramount+                 1 (0.002%)
  MSNBC                      1 (0.002%)
  Fox Business               1 (0.002%)
  ABC                        1 (0.002%)

=== 65 export files - corporations (56,363 records, 53.5s) ===
Records mentioning any tracked entity: 8,822 (15.65%)
  Google                     3,168 (5.621%)
  LinkedIn                   3,112 (5.521%)
  IBM                        1,480 (2.626%)
  Microsoft                  1,460 (2.590%)
  Amazon                     766 (1.359%)
  OpenAI                     645 (1.144%)
  Meta                       582 (1.033%)
  Salesforce                 551 (0.978%)
  Apple                      450 (0.798%)
  Nvidia                     285 (0.506%)
  Nike                       209 (0.371%)
  Facebook                   177 (0.314%)
  McKinsey                   175 (0.310%)
  Tesla                      149 (0.264%)
  Adobe                      137 (0.243%)
  Deloitte                   121 (0.215%)
  Uber                       108 (0.192%)
  Walmart                    90 (0.160%)
  Intel                      90 (0.160%)
  Airbnb                     76 (0.135%)
  PwC                        74 (0.131%)
  SpaceX                     65 (0.115%)
  Samsung                    63 (0.112%)
  JPMorgan                   59 (0.105%)
  Coca-Cola                  52 (0.092%)
  Starbucks                  46 (0.082%)
  Disney                     44 (0.078%)
  Goldman Sachs              41 (0.073%)
  KPMG                       39 (0.069%)
  PepsiCo                    21 (0.037%)
  Morgan Stanley             20 (0.035%)
  Oracle                     7 (0.012%)
  Ernst & Young (EY)         5 (0.009%)
```

The scan ran all four categories on the 65 export files. Among the 56,363 records, 8,822 (15.65%) mention a tracked corporation, led by Google (5.621%), LinkedIn (5.521%), IBM (2.626%) and Microsoft (2.590%). 801 (1.42%) mention a tracked news outlet, led by Forbes (0.429%) and Harvard Business Review (0.163%); 750 (1.33%) mention a tracked magazine, again led by Forbes (0.429%); and 1,172 (2.08%) mention a tracked TV or streaming name, led by YouTube (1.011%), TikTok (0.543%) and Netflix (0.479%). A record that names two entities counts once for each, and a name such as LinkedIn also appears as the platform where the post was written, so the counts show that a name occurs and not that the post is about it.

The rates come from different fields and different kinds of record, so a gap between them describes the files and does not describe the tools. A match is a keyword in the text, not a finding about the post or its author.
