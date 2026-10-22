# 65 export files profile

`analysis/export65_profile.py` profiles a separate set of 65 export files (`podUsers_<id>_<stamp>.json`). Where the files came from, and who reported it, is in [provenance.md](../provenance.md#the-65-export-files). The fields are in [data-dictionary.md](../data-dictionary.md#the-65-export-files-podusers_id_stampjson). What the numbers cannot show is in [limitations.md](../limitations.md#what-the-65-export-files-do-and-dont-tell-you).

Same discipline as every other script in this repo: counts only. The script prints no name, URL, record id or post text, and it uses names only as in-memory hashes to count accounts.

## Results (VERIFIED, reproducible via the script)

Run as `python3 analysis/export65_profile.py /path/to/folder`. The dates are UTC, and the cutoff is 21 October 2024, the date on which [16 CFR § 465.8](../regulatory-context.md) took effect.

```
Files uploaded:                      83
Distinct files (by content):         65
Byte-identical extra copies:         18
Export stamps in file names:         2026-16-10--12-24-12 to 2026-16-10--13-44-05 (yyyy-dd-mm--HH-MM-SS)
Records in the distinct files:       184737
Files holding exactly 5,000 records: 22 (largest file: 5000)
Days between earliest and latest record, median per file: 35 for the 22 files at 5,000 records, 735 for the other 43
Distinct records (_id):              56363
Records present in more than 1 file: 32842
Records whose state differs by file: 8

State (kept copy of each record)
  finishedEngagement        54377   96.5%
  deleted                    1631    2.9%
  stopped                     263    0.5%
  running                      92    0.2%

engagementType
  normal                    42021   74.6%
  human                      8938   15.9%
  viral                      4263    7.6%
  steady                     1141    2.0%

engageTiming as stored (top 12)
  20                        20379   36.2%
  None                      14184   25.2%
  120                        6190   11.0%
  300to900                   3803    6.7%
  60                         2785    4.9%
  40                         2228    4.0%
  300                        2077    3.7%
  180                        2047    3.6%
  240                        1642    2.9%
  1500to1800                  431    0.8%
  3300to3600                  264    0.5%
  300a                        206    0.4%

engagedUsersCount: median 278, mean 249.1, max 1003
  statsLikes present on 46931 records
  statsComments present on 32534 records
  statsViews present on 11987 records

Distinct accounts (first + last name, case-normalised): 1380

Records with createdAt: 56363 of 56363; earliest 2024-10-11, latest 2026-10-16 (UTC)
Created before 2024-10-21: 438 (0.78%); on or after: 55925 (99.22%)

Records created per month (UTC)
  2024-10    1039
  2024-11    1447
  2024-12    1323
  2025-01    1467
  2025-02    1507
  2025-03    1693
  2025-04    1910
  2025-05    2109
  2025-06    1735
  2025-07    2134
  2025-08    1988
  2025-09    2098
  2025-10    2047
  2025-11    1577
  2025-12    1739
  2026-01    1980
  2026-02    1630
  2026-03    1989
  2026-04    2191
  2026-05    2311
  2026-06    2307
  2026-07    2639
  2026-08    3389
  2026-09    7285
  2026-10    4829

Hours from the target post's decoded publish time to record creation (INFERENCE: id decode), n=56363
  min 0.00, 25% 0.08, median 0.39, 75% 3.07, 95% 67.41, max 63721.9
  negative: 0; within 1 hour: 64.0%; within 24 hours: 89.8%; over 7 days: 2.2%
  decoded post dates run from 2019-04-14 to 2026-10-16; before 2024-10-21: 534
```

## Reading the results

- **Files.** 83 files were supplied and 18 are byte-identical copies, so there are 65 distinct files. Their hashes are in [checksums/EXPORT65_MANIFEST.csv](../../checksums/EXPORT65_MANIFEST.csv), and `--check-manifest` compares a folder of files against it.
- **Records.** The 65 files hold 184,737 records and 56,363 distinct `_id` values. 32,842 of the distinct records appear in more than one file, so the files overlap heavily. The profile keeps the copy with the highest `engagedUsersCount`. The state of 8 records differs between files, which moves the counts of `finishedEngagement` and `running` by a few records depending on which copy is kept.
- **The 5,000-record limit.** 22 files hold exactly 5,000 records and no file holds more. Those 22 span a median of 35 days, and the other 43 span a median of 735. The likeliest reading is an export limit that cut off older records (INFERENCE), so the months before the limit are under-counted for those accounts.
- **Dates.** Every record has a creation time. 438 records (0.78%) were created before 21 October 2024 and 55,925 (99.22%) on or after it. The monthly counts rise from about 1,000 to 2,000 a month through 2025 and early 2026, then to 7,285 in September 2026 and 4,829 in the first 16 days of October 2026. Because of the 5,000-record limit, these files cannot say whether that rise is growth in use, an effect of the limit or an effect of which accounts were exported.
- **Creation time and post time.** The post id in each `url` decodes to a publish time for the target post (INFERENCE: see [method.md](../method.md)). Records were created a median of 0.39 hours after that time, 64.0% within an hour and 89.8% within 24 hours, and none before it. The decoded post dates run from 14 April 2019 to 16 October 2026, and 534 target posts decode to a date before 21 October 2024.
- **A date split is not a violation count.** The split shows when a tool's record was made. It does not show a sale of a fake indicator, who the parties were or any other element of 16 CFR § 465.8 (see [regulatory-context.md](../regulatory-context.md)).
