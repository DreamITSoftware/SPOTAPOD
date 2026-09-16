# Cybersecurity content vs. engagement anomalies

`analysis/cybersecurity_anomaly_scan.py` cross-tabulates
cybersecurity-related content against the same engagement-anomaly
indicators already used in [baseline-profile.md](baseline-profile.md)
(zero views with likes present, likes exceeding views, extreme
like/view ratio, reciprocal like+comment pairing, zero impressions).
Same discipline as every other scan in this repo: aggregate counts
only, no record, author, or matched text ever printed.

## Scope

Only **podawaa2024.json** and **HyperClaper.json** are covered.
**LinkBoost-2025.json is not supported** - it has no per-record
engagement fields to cross-reference against. Every record there is,
by the dataset's own construction, a logged successful pod action, so
a per-record anomaly rate isn't a meaningful thing to compute for it.

## Results (VERIFIED - reproducible via the script)

### podawaa2024

Cybersecurity-related posts: 2,779 of 213,491 (1.30%)

| Anomaly indicator | All posts (baseline) | Cybersecurity posts only |
|---|---|---|
| Zero views with likes present | 35.3% | **39.9%** |
| Likes exceed views | 36.51% | **41.02%** |
| Like/view ratio exceeds 15% | 11.78% | 14.18% |

### HyperClaper

Cybersecurity-related posts: 4,487 of 49,369 (9.09%)

| Anomaly indicator | All posts (baseline) | Cybersecurity posts only |
|---|---|---|
| Reciprocal like+comment pair | 68.6% | **84.2%** |
| Zero impressions | 98.0% | 97.3% |

## Reading these numbers

Cybersecurity content shows a higher anomaly rate than the dataset
baseline on three of the four measures checked, most notably the
reciprocal like+comment flag in HyperClaper (84.2% vs. 68.6% baseline)
- a meaningfully elevated rate, and a genuine, reproducible, aggregate
finding.

Cybersecurity content also makes up a much larger share of HyperClaper
(9.09%) than of podawaa2024 (1.30%), consistent with HyperClaper's
broader skew toward technology/AI content already documented in
[topic-taxonomy.md](topic-taxonomy.md) (`technology_ai` at 27.97% there
vs. 16.39% in podawaa2024).

## What this does not show

An elevated anomaly rate at the category level is a population-level
pattern, not identification of any specific cybersecurity account or
post as fraudulent. This script cannot and does not determine which
individual posts within the cybersecurity-content subset are actually
anomalous versus which authors happen to write about cybersecurity and
also happen to have organically unusual engagement patterns for
unrelated reasons. No name, handle, or individual post is identified by
this scan, and none should be inferred from it. See
[limitations.md](../limitations.md) for the fuller version of this
caveat, which applies here identically.

## Caveats

Same as every keyword scan in this repo: a match means a cybersecurity
term appears in the text, not that the post is a credible, accurate, or
representative piece of security content. The anomaly indicators
themselves are the same blunt population-level signals used everywhere
else in this repo - they flag a statistical pattern, not a confirmed
instance of manipulation for any single record.
