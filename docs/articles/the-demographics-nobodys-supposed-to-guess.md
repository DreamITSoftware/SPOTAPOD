# The Demographics Nobody's Supposed to Guess

### This project measures geography and industry vertical, and deliberately stops well short of anything that could be read as demographic profiling

Comparative research across datasets naturally raises the question of who's actually posting: which countries, which industries, which professional backgrounds show up most. This project answers a narrower version of that question than the framing usually implies, on purpose.

## What this project actually measures

**Geographic mentions**: place names appearing in post text, aggregated as a distribution across the dataset, with no attempt to map that back to any specific account's actual location. **Industry verticals**: keyword-based categorization of content topic (real estate, insurance, finance, technology), describing what's discussed, not who is discussing it. Both are aggregate, dataset-level distributions, comparable across the three sources the same way topic-taxonomy percentages are.

## What this project will never measure

Any inference about an individual account's protected characteristics, race, ethnicity, gender, religion, age, or any other personal attribute, is explicitly out of scope, permanently, regardless of whether the underlying data might make some such inference technically possible. This isn't a data-availability limitation. It's a deliberate boundary, consistent with this project's broader no-per-entity-lookup, no-individual-identification architecture described throughout this series.

## Why "demographics" is the wrong word for what's actually here

Calling geographic-mention and industry-vertical distributions "demographics" invites a reader to expect something this project doesn't do and won't do: profiling the people behind the accounts. What's actually being compared across datasets is content characteristics, in aggregate, with the underlying accounts hashed, uncounted individually, and never identifiable even in principle from the published output.

## What this is, and isn't

**VERIFIED**: geographic-mention and industry-vertical distributions across all three datasets, as separately published.

**Never attempted, as a matter of policy**: any protected-characteristic inference about the people behind these accounts.

Full findings: **github.com/DreamITSoftware/SPOTAPOD**.

<!-- export65-note -->
> **Update, 22 October 2026.** The geographic-mention and industry-vertical scans were run on the [65 export files](../provenance.md#the-65-export-files): [geographic mentions](../research/geographic-mentions-content.md#the-65-export-files) and [industry verticals](../research/industry-verticals-content.md#the-65-export-files). The demographics scan of account location and stated occupation was not, because those files carry no location, country, headline or occupation field. Detail: [demographics](../research/demographics.md#the-65-export-files).

---

*Self-published. Not peer-reviewed.*
