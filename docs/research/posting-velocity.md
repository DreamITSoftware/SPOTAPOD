# Posting velocity

`analysis/posting_velocity_scan.py` computes sustained posting rate
(posts per day, across each account's full active window) for the
highest-volume accounts in HyperClapper - the only one of the three
datasets with real per-record timestamps (`created_at`). This is a
structural/behavioral analysis, not a content keyword scan: it checks
whether the small number of accounts already known to drive a
disproportionate share of HyperClapper's posts (see
[baseline-profile.md](baseline-profile.md)) show posting patterns
consistent with sustained automation or managed content operations,
rather than individual human authorship.

## Method and privacy

Accounts are grouped by the SHA-256 hash of their
`profile.linkedin_data.public_identifier`. For each account, every
post's `created_at` timestamp is sorted, and the account's full active
window (first post to last post) is computed in days, then post count
is divided by that window to get a sustained posts-per-day rate. A raw
interval-regularity check (coefficient of variation of the time between
consecutive posts) is also reported.

Accounts are identified in this script's output and in this document
only by anonymous volume rank ("account_1," "account_2," ...) - never
by hash value, handle, or any other identifier.

## Two different anomaly signatures, and why only one shows up here

A very low coefficient of variation in posting intervals would indicate
simple robotic clockwork - posting at machine-regular fixed intervals.
**That is not what this data shows.** Every top-10 account has a CV
well above 80%, several above 500% - posting intervals are highly
irregular, not mechanically regular.

**The signal that does show up is sustained rate.** Regardless of how
irregular the spacing between individual posts is, the accounts checked
here maintain 1.2 to 3.7 posts per day, every day, across periods
ranging from 174 to 712 consecutive days. That is the harder pattern to
explain as ordinary individual human authorship - not because the
timing looks robotic, but because no realistic individual professional
sustains multiple substantive posts a day, every day, for the better
part of a year or more.

## Results (VERIFIED - reproducible via the script)

| Rank | Posts | Active days | Posts/day | Interval CV% |
|---|---|---|---|---|
| account_1 | 1,138 | 310.0 | 3.67 | 567.2 |
| account_2 | 1,043 | 712.6 | 1.46 | 254.7 |
| account_3 | 1,039 | 378.0 | 2.75 | 562.6 |
| account_4 | 976 | 310.4 | 3.14 | 99.4 |
| account_5 | 801 | 309.2 | 2.59 | 799.0 |
| account_6 | 758 | 273.0 | 2.78 | 85.8 |
| account_7 | 697 | 263.0 | 2.65 | 285.8 |
| account_8 | 658 | 528.3 | 1.25 | 184.2 |
| account_9 | 652 | 235.8 | 2.76 | 123.5 |
| account_10 | 651 | 174.0 | 3.74 | 91.5 |

Dataset-wide date range: 2022-07-08 to 2026-07-02 (1,455 days).
Total accounts with usable timestamps: 702.

## Reading these numbers

Every one of the top 10 accounts by volume sustains a posting rate that
would require substantial daily time investment if done by one person
manually, maintained without a multi-day gap large enough to
meaningfully lower the average, across periods measured in months to
nearly two years. account_2 is the most striking case: a comparatively
modest 1.46 posts/day, but sustained across 712.6 days - just under two
full years without the rate meaningfully dropping.

This is consistent with, though does not on its own prove, either
heavy scheduling-tool automation or a managed content operation
publishing under a single identity - the same structural possibility
already discussed at the dataset level in
[baseline-profile.md](baseline-profile.md) (HyperClapper's top 100
accounts producing a large majority of all posts) and
[decision-points.md](decision-points.md). This scan adds a new,
independent line of evidence toward that same conclusion: not just
that a few accounts post disproportionately often, but that they do so
at a sustained rate difficult to reconcile with ordinary individual
usage.

## Caveats

This is INFERENCE-tier reasoning about what a sustained rate this high
plausibly indicates, not direct proof of automation for any specific
account - this script does not and cannot determine whether a given
account is bot-operated, professionally managed, or a genuine
individual with unusual habits. Only HyperClapper has the timestamp
data this analysis requires; podawaa2024 and LinkBoost-2025 are not
included because neither dataset provides comparable per-record
timestamps.
