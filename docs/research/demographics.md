# Demographics: what's in the data, and what isn't

This page covers `analysis/demographics_scan.py`. A scope statement comes
before the numbers, because "demographics" usually implies more than
these files contain.

## What is NOT in these files, and won't be inferred

None of the three datasets state race, ethnicity, gender, age, religion,
disability status, or any other protected characteristic for anyone in
them. This repo does not infer any of those from a name, a profile photo,
or any other proxy. Not for an individual record, and not in aggregate.
Name-based or photo-based demographic inference is unreliable (these
methods carry well-documented, substantial error rates) and it profiles a
real person who did not consent, by a protected characteristic they
never stated. That holds even when framed as a population-level statistic
("X% of accounts appear to be..."), because the aggregation does not remove
the individual-level guess underneath it. This analysis is not done in this repo. See [privacy.md](../privacy.md) and
[limitations.md](../limitations.md) for the same principle applied elsewhere.

## What is in the data

Two of the three files have fields that can be aggregated
without inference: a **self-reported location string**
(HyperClaper.json's `location`) or **country** (LinkBoost-2025.json's
`country`), and **stated occupation/headline text**
(HyperClaper.json's `headline`/`jobTitle`; LinkBoost-2025.json's
`Occupation`). `podawaa2024.json` has neither field. There is nothing to report
for it here.

### Geography

| Dataset | Records with a location/country value | Top entries |
|---|---|---|
| HyperClapper | 36,301 / 49,369 (73.5%) | Delhi, India (10.7%); Gurugram, India (6.2%); United Kingdom (4.1%); Bengaluru, India (2.7%); several more Indian cities and US/UK metros |
| LinkBoost-2025 | 47,173 / 77,969 (60.5%) | United States (21.8%); India (15.6%); United Kingdom (8.0%); Canada (3.8%); Serbia (3.1%) |

Full country/location breakdowns are in `docs/research/baseline-profile.md` (this
scan's output is appended there).

### Occupation category (keyword-bucketed, same caveats as the regulatory-category scan)

A record's headline/occupation text is checked against ten broad,
keyword-based category patterns (marketing, sales, technology, healthcare,
finance, education, executive/leadership/coaching, HR, design, legal). A
record can match more than one category or none.

| Category | HyperClapper (% of records with text) | LinkBoost-2025 (% of records with text) |
|---|---|---|
| marketing_content_creation | 33.4% | 21.8% |
| sales_business_development | 11.8% | 2.7% |
| technology_data_ai | 29.6% | 28.6% |
| healthcare_pharma | 2.3% | 2.8% |
| finance_accounting | 0.5% | 1.5% |
| education_student | 13.8% | 1.6% |
| executive_leadership_coaching | 23.0% | 59.5% |
| hr_recruiting | 1.4% | 1.6% |
| design_creative | 0.8% | 0.7% |
| legal | 0.0% | 0.8% |

## Caveats (same discipline as other-regulatory-signals.md)

- **Keyword bucketing is blunt.** "Marketing" catches an actual marketer
  and a post that just mentions marketing in passing. These are signal
  counts, not verified job classifications.
- **Location strings are self-reported and free-text**, not a
  standardized geography field. "Delhi, India" and "New Delhi, Delhi,
  India" are counted separately above, so the true city-level
  concentration is somewhat higher than the raw top-15 list shows.
- **No individual is identified.** Every number above is a population-level
  percentage; there's no way to filter this output down to which specific
  record(s) contributed to any bucket.
- **This still doesn't establish anything about § 465.8 or the other
  regulated categories in [other-regulatory-signals.md](other-regulatory-signals.md).**
  Geography and occupation are demographic/professional context, not
  evidence of any legal element.
