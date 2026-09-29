# Pod count profile (spotapod.json)

`analysis/pod_count_profile.py` profiles a file supplied as
`spotapod.json`. See
[provenance.md](../provenance.md#a-fourth-file-supplied-as-spotapodjson-not-independent-data)
for why this is documented as a derived, post-level aggregation of
`podawaa2024.json` rather than a fourth independent dataset: every one
of its 201,000 unique `linkedinPostId` values, and every one of its
6,948 unique authors, is already present in `podawaa2024.json`. Same
discipline as every other script in this repo: aggregate counts only,
no record, author, or post content ever printed.

## What this file adds

One new field not present in `podawaa2024.json`: `PODCount`, an
unexplained per-post integer (min 1, max 1,364, mean 9.97, median 2).
Nothing in the supplied file states what produced this count or what
it's meant to measure, so this repo doesn't guess - it's profiled here
as an unexplained aggregate signal, not asserted to mean "number of pod
actions" or anything more specific than its name suggests.

## Results (VERIFIED - reproducible via the script)

```
Total records: 203,038
Unique linkedinPostId values: 201,000

Zero-view-with-reactions anomaly (MaxViews==0, MaxReactions>0): 72,725 (35.8%)

All records:              n=203,038  mean PODCount=9.97  median PODCount=2
Zero-view-anomaly records: n=72,725  mean PODCount=17.46  median PODCount=2
Other records:             n=130,313  mean PODCount=5.78  median PODCount=2
```

The 35.8% zero-view-with-reactions figure here is close to, but not
identical to, the 35.3% figure computed directly from
`podawaa2024.json`'s own `Likes`/`Views` fields elsewhere in this repo
- the small difference is consistent with this file's dedup pass
(213,491 raw podawaa2024 records collapse to this file's 201,000
unique post IDs), not a new or separate measurement.

## Reading this

The median `PODCount` is identical (2) whether or not a post shows the
zero-view-with-reactions anomaly, but the mean is roughly three times
higher for the anomalous group (17.46 vs. 5.78). That gap comes from a
long tail of very high `PODCount` values sitting disproportionately
within the anomalous records, not from a shift in the typical post. In
other words: most anomalous and most ordinary posts look the same by
this measure, but the small number of posts with an unusually high
`PODCount` are markedly more likely to also show the zero-view
engagement anomaly.

## Caveats

`PODCount`'s definition is not stated by whatever process produced
this file, so this correlation should be read as exactly that - a
correlation between an unexplained count and a previously documented
engagement anomaly - not as confirmation of what causes either one.
This script also does not establish that `spotapod.json` was produced
independently of podawaa2024.json's own known duplicate-record
structure; see [provenance.md](../provenance.md) for what has and
hasn't been established about this file's origin.
