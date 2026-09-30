# Career advice and reciprocal engagement: a row-level check

[career-advice-comparison.md](career-advice-comparison.md) found that
HyperClapper shows the highest career-advice content rate (16.52%), the
highest reciprocal-engagement rate (68.6% of all records), and the
heaviest leadership-coaching occupation skew of the three datasets, and
flagged that alignment as INFERENCE-tier for any claim about *why* the
three move together. That comparison is dataset-wide. It does not show
whether the specific posts matching career-advice language are the same
posts driving the reciprocal-engagement rate, or whether the whole file
just runs hot on reciprocal engagement for unrelated reasons.

`analysis/career_advice_reciprocal_crosstab.py` answers the narrower
question directly: within HyperClapper alone, does the reciprocal
like-and-comment rate differ between career-advice-matching records and
everything else in the same file.

## Result (VERIFIED, reproducible via the script)

Run against `HyperClapper_1.json`, SHA-256 `913e28d4...51f6` (matches the
`HyperClaper.json` entry in [checksums/CHECKSUMS.txt](../../checksums/CHECKSUMS.txt)):

| | Records | Reciprocal (like AND comment) | Rate |
|---|---|---|---|
| Career-advice-matching | 8,157 (16.52%) | 6,857 | **84.06%** |
| Everything else | 41,212 (83.48%) | 27,006 | **65.53%** |

Difference: **+18.53 percentage points**.

## Reading this number

The file's overall reciprocal-engagement rate (65.53% among non-career
records, close to the 68.6% file-wide figure cited in
[career-advice-comparison.md](career-advice-comparison.md)) is already
high. Career-advice-matching content sits meaningfully above even that
elevated baseline. This is a within-file, row-level comparison, not a
cross-file one, so it isolates the career-advice effect from whatever
makes HyperClapper as a whole more pod-heavy than the other two datasets.

## Limitations

- **Single dataset.** `podawaa2024.json` has no like/comment reciprocity
  field in its schema, so this comparison can't be run there.
  `LinkBoost-2025.json` is entirely pod-engagement records by definition
  (`SuccessfullLikes`/`SuccessfullComments`), so there's no non-pod
  baseline within that file to compare against. This finding currently
  rests on HyperClapper alone.
- **Keyword matching is still blunt.** The same career-advice pattern set
  used in [career-advice-comparison.md](career-advice-comparison.md)
  applies here, "promotion" can mean career promotion or a marketing
  promotion, with no way to tell which from this signal alone.
- **File-identity note.** Several HyperClapper-style export files exist
  outside this repo with different SHA-256 hashes than the one recorded
  in `checksums/CHECKSUMS.txt`. One such non-matching copy produced
  identical record-level results on this specific check, but that should
  never be assumed. Always verify the hash before citing a figure from
  this script.
- **Correlation between category and coordination, not proof of intent.**
  This establishes that career-advice content is disproportionately
  represented among reciprocally engaged records in this file. It does
  not establish who coordinated that engagement, why, or whether any
  specific account's activity was deliberate versus incidental.

## Evidence tier

**VERIFIED**: the 84.06% / 65.53% rates and the 18.53-point gap, all
reproducible from the checksummed source file via
`analysis/career_advice_reciprocal_crosstab.py`.

**Not established**: why career-advice content specifically attracts more
reciprocal engagement (see [career-advice-comparison.md](career-advice-comparison.md)
for the occupation-skew context, still INFERENCE-tier), and any claim
about audience-side impact (see [audience-impact.md](audience-impact.md),
which covers a different set of content categories and does not include
career advice).
