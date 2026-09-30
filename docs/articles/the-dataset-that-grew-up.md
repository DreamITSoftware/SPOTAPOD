# The Dataset That Grew Up: What spotapod.json's PODCount Reveals

### A field that counts how many pod actions touched a post shows a clear split between records with a zero-view anomaly and records without one

`spotapod.json`, a file supplied to this project and later confirmed to be a derived aggregation of `podawaa2024.json` rather than an independent fourth dataset, carries a field the other files don't: `PODCount`, a per-record count of pod-related activity touching that post.

## The finding

Comparing `PODCount` between the zero-view anomaly group (posts with recorded likes but zero recorded views) and everything else, the zero-view group has a mean `PODCount` of **17.46**, versus **5.78** for other records, roughly three times higher on average. The median, however, is **2 for both groups**, meaning the mean difference is being driven by a smaller number of high-`PODCount` outliers within the zero-view group, not a uniform shift across the whole distribution.

## Why the mean and median split matters for how to read this

If both the mean and median had shifted together, that would suggest zero-view posts are broadly, consistently more pod-touched than other posts. Instead, what the data shows is narrower. Most zero-view-anomaly posts look similar to other posts on `PODCount` (same median), but the group also contains some records with dramatically higher `PODCount` values that pull the average up. That's a meaningfully different and more precise claim than "zero-view posts have more pod activity." It's closer to "a subset of zero-view posts have unusually high pod activity, and the rest look typical."

## What this doesn't establish

`PODCount` being higher for some zero-view records is consistent with the zero-view anomaly being pod-related for those specific records, but consistency isn't proof. This project has no way to confirm that `PODCount` is being measured or defined the same way its name implies, since `spotapod.json`'s exact construction methodology wasn't documented by whoever supplied it. Treat this as a corroborating signal, not an independent confirmation.

## What this is, and isn't

**VERIFIED**: mean and median `PODCount` figures for both groups, reproducible directly from `spotapod.json`.

**CORROBORATED, not independently confirmed**: that elevated `PODCount` in some zero-view records reflects the same underlying manipulation this project documents elsewhere. `spotapod.json` is a derived view of `podawaa2024.json`, not an independent data source.

Full findings: **github.com/DreamITSoftware/SPOTAPOD**.

---

*Self-published. Not peer-reviewed.*
