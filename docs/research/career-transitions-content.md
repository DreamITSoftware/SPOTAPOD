# Career transitions (layoffs, remote work, burnout)

`analysis/career_transitions_scan.py` counts mentions of layoffs,
remote work, return-to-office, burnout, and work-life balance across
post content in all three datasets. Same discipline as every other
scan in this repo: aggregate counts only, no record, author, or
matched text ever printed beyond the duplicate-template check below.

## Results (VERIFIED - reproducible via the script)

| Term | podawaa2024 | HyperClapper | LinkBoost-2025 |
|---|---|---|---|
| Burnout | 803 | 415 | 1,937 |
| Remote work | 607 | 1,716 | 202 |
| Work-life balance | 384 | 38 | 66 |
| Layoffs | 229 | 239 | 193 |
| Return to office / RTO | 33 | 13 | - |
| **Any mention** | **1,898 (0.889%)** | **2,395 (4.851%)** | **2,398 (3.076%)** |

LinkBoost-2025's low distinct-string ratio (139 for 2,398 matches,
mostly "burnout") was checked manually - the top repeated string is
under 5% of matches, and the top several are genuinely distinct posts
(an executive-burnout post, a solopreneur-burnout post, a security
operations center overload post, an empathy-in-leadership post), not a
new artifact.

## Reading these numbers

HyperClapper's rate (4.851%) is by far the highest, driven almost
entirely by "remote work" (1,716, nearly triple its next-highest term)
- consistent with HyperClapper being the most recent dataset and remote
work remaining a live, contested topic through 2025-2026.

LinkBoost-2025 leans heavily toward "burnout" specifically (1,937,
81% of its total) rather than a spread across terms - connects to the
"authentic"/"honest truth" vulnerability-posting genre documented in
[authenticity-content.md](authenticity-content.md); burnout content is
a natural fit for that same performed-vulnerability pattern.

"Return to office" is the smallest term everywhere, which is itself
notable given how contentious RTO mandates have been in general tech
and business news coverage over this period - this content ecosystem
doesn't reflect that intensity.

## Caveats

Same as every keyword scan in this repo: a match means the term
appears in the text, not that the post describes a genuine layoff,
remote-work situation, or burnout experience.

<!-- export65-section -->
## The 65 export files

Added 22 October 2026. This is the same scan run on the 65 export files: 56,363 distinct records after the files are de-duplicated on record id, reading each record's `title` field, which holds the post text. These files are a separate set from the three datasets above, and nothing above this heading has changed. Their source, method and limits are in [provenance.md](../provenance.md#the-65-export-files) and [export-65-profile.md](export-65-profile.md). Rates use all 56,363 records as the denominator, and 237 of them have no post text. Command: `python3 analysis/career_transitions_scan.py export65 /path/to/folder_with_the_65_files`.

```text
=== 65 export files (56,363 records) ===
Records mentioning any career-transition term: 1,698 (3.013%)
Distinct underlying text values: 1,383
    remote work                  775
    burnout                      638
    layoffs                      235
    work-life balance            84
    return to office / RTO       22
```

1,698 of 56,363 records (3.013%) match. In the three datasets above the same measure is 0.889% in podawaa2024, 4.851% in HyperClapper and 3.076% in LinkBoost-2025 (using the corrected figure where this page gives one), which puts the 65 export files at the second lowest of the four. The scan's duplicate-template check did not fire, and the matching records hold 1,383 distinct texts.

The rates come from different fields and different kinds of record, so a gap between them describes the files and does not describe the tools. A match is a keyword in the text, not a finding about the post or its author.
