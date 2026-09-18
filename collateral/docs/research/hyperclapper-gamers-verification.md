# Full cross-check: hyperclapper-gamers.json vs. published HyperClapper figures

This page exists to answer one question thoroughly, since the earlier spot
check in [federal-agency-mentions.md](federal-agency-mentions.md) only
covered four terms: **does every existing scan in this repo reproduce the
same numbers when run against `hyperclapper-gamers.json`?**

See [provenance.md](../provenance.md)'s "Candidate duplicate" section for
the background — `hyperclapper-gamers.json` is a file whose relationship
to this repo's checksummed `HyperClaper.json` is an **INFERENCE**, not a
CORROBORATED match. This page adds evidence to that inference; it does not
change its tier. The sha256 still doesn't match. Nothing here should be
read as "these are now confirmed to be the same file" — only as "every
independently-run scan produced identical output."

## Method

Every script in `analysis/` that accepts a single dataset file was run
against `hyperclapper-gamers.json` in `hyperclapper` mode. Three scripts
were skipped because they require `podawaa2024.json` and/or
`LinkBoost-2025.json`, neither of which is available here (by design —
see [privacy.md](../privacy.md), no raw data is kept in this repo, and no
other party's copy was available to compare against):
`topic_taxonomy.py`, `category_title_patterns.py`,
`cross_dataset_overlap_scan.py`. `duplicate_content.py` was also skipped —
it only reads podawaa2024's `Posts`/`Content` schema, not HyperClapper's.

The remaining **30 scripts** all ran successfully. Every output was
compared, line by line, against the already-published HyperClapper
figures in this repo's own docs.

## Result: exact match, every script, zero discrepancies

| Script | Published doc | Match |
|---|---|---|
| `algorithm_mention_scan.py` | [algorithm-mention-content.md](algorithm-mention-content.md) | Exact |
| `authenticity_content_scan.py` | [authenticity-content.md](authenticity-content.md) | Exact |
| `blockchain_crypto_scan.py` | [blockchain-crypto-content.md](blockchain-crypto-content.md) | Exact |
| `book_genre_scan.py` | [book-promotion-content.md](book-promotion-content.md) | Exact |
| `career_advice_scan.py` | [career-advice-comparison.md](career-advice-comparison.md) | Exact |
| `career_transitions_scan.py` | [career-transitions-content.md](career-transitions-content.md) | Exact |
| `cybersecurity_anomaly_scan.py` | [cybersecurity-anomaly.md](cybersecurity-anomaly.md) | Exact |
| `demographics_scan.py` | [demographics.md](demographics.md) | Exact |
| `diabetes_content_scan.py` | [diabetes-content.md](diabetes-content.md) | Exact |
| `entity_mention_scan.py` | [entity-mentions.md](entity-mentions.md) | Exact (all 4 sub-categories) |
| `geographic_mentions_scan.py` | [geographic-mentions-content.md](geographic-mentions-content.md) | Exact |
| `homelessness_content_scan.py` | [homelessness-content.md](homelessness-content.md) | Exact |
| `honesty_language_scan.py` | [honesty-language-content.md](honesty-language-content.md) | Exact |
| `immunotherapy_content_scan.py` | [immunotherapy-content.md](immunotherapy-content.md) | Exact (0 records, both) |
| `industry_verticals_scan.py` | [industry-verticals-content.md](industry-verticals-content.md) | Exact |
| `investment_vc_scan.py` | [investment-vc-content.md](investment-vc-content.md) | Exact |
| `law_content_scan.py` | [law-content.md](law-content.md) | Exact (narrow + broader) |
| `national_security_scan.py` | [national-security-content.md](national-security-content.md) | Exact |
| `nonprofit_content_scan.py` | [nonprofit-content.md](nonprofit-content.md) | Exact, including the 658-record duplicate-template warning |
| `pharma_content_scan.py` | [pharma-content.md](pharma-content.md) | Exact |
| `political_content_scan.py` | [political-content.md](political-content.md) | Exact |
| `posting_velocity_scan.py` | [posting-velocity.md](posting-velocity.md) | Exact, including per-account posts/active-days/interval-CV% for the top 10 anonymous ranks, and the 2022-07-08 to 2026-07-02 (1,455-day) range |
| `profile_hyperclapper.py` | [baseline-profile.md](baseline-profile.md) | Exact, including the full 49-month time series and both duplicate-title figures |
| `regulatory_category_scan.py` | [data-dictionary.md](../data-dictionary.md) (regulatory-signal section) | Exact |
| `simple_title_aggregate.py` | [simple-titles.md](simple-titles.md) | Exact |
| `social_proof_scan.py` | [social-proof-content.md](social-proof-content.md) | Exact |
| `speaker_thought_leader_scan.py` | [speaker-thought-leader.md](speaker-thought-leader.md) | Exact, including the 100% speaker/thought-leader overlap |
| `toplist_content_scan.py` | [toplist-content.md](toplist-content.md) | Exact |
| `travel_content_scan.py` | [travel-content.md](travel-content.md) | Exact, including every template-inflation warning percentage |
| `university_content_scan.py` | [university-content.md](university-content.md) | Exact |
| `veteran_content_scan.py` | [veteran-content.md](veteran-content.md) | Exact |
| `federal_agency_scan.py` (new, this session) | [federal-agency-mentions.md](federal-agency-mentions.md) | N/A — computed from this file originally, self-consistent |

## Why this matters more than the earlier spot check

`federal-agency-mentions.md` noted that 4 terms (FBI, CIA, NSA, FDA)
matched. That's a small sample and could, in principle, coincide by
chance across two genuinely different but similarly-sourced LinkedIn
datasets. The posting-velocity and baseline-profile matches are a
different order of evidence: they depend on the specific distribution of
timestamps across 702 individual accounts over a 1,455-day window, down
to fractional interval-CV percentages. Two independently collected
datasets landing on identical numbers there is not a plausible
coincidence — this is strong support for the same underlying export,
even though it stops short of a hash match.

## What this still doesn't establish

- **Not a hash match.** `hyperclapper-gamers.json` and `HyperClaper.json`
  remain byte-different files per `checksums/CHECKSUMS.txt` and the
  comparison in `provenance.md`.
- **Not a corrected/updated set of published figures.** No number in any
  existing doc has been changed as a result of this cross-check — every
  existing figure was already correct, computed from the checksummed
  file, and remains the number of record.
- **Not evidence about which file is more "original."** This page does
  not establish that one file was derived from the other, or when, or by
  whom — only that their content, at least across everything these 30
  scripts measure, is indistinguishable.
