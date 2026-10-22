# Law enforcement content

`analysis/law_enforcement_scan.py` counts mentions of law-enforcement-
related terms (law enforcement, police, police officer(s), cop/cops,
sheriff, detective) across post content in all three datasets. Same
discipline as every other scan in this repo: aggregate counts only, no
record, author, or matched text ever printed beyond the
duplicate-template check described below.

Distinct from [national-security-content.md](national-security-content.md),
which covers federal agencies (CIA, FBI, NSA) rather than general or
local law enforcement.

## LinkBoost-2025's low-distinct-ratio note, checked

The low-distinct-ratio note fires on LinkBoost-2025 (32 distinct
strings for 461 matches), but the duplicate-template warning does not -
no single string dominates (the top is 82 of 461, about 18%). Checked
manually: the top several repeated strings are genuinely distinct,
on-topic career-narrative posts - an IPS officer's competitive-exam
story, someone's "worked as a cop" side-hustle recap, a detective's
career-statistics post, a cop's salary-progression post. This is
genuine signal, not an artifact.

## Results (VERIFIED - reproducible via the script)

| Term | podawaa2024 | HyperClapper | LinkBoost-2025 |
|---|---|---|---|
| Police | 203 | 51 | 224 |
| Cop/cops | 53 | 45 | 182 |
| Detective | 52 | 27 | 90 |
| Law enforcement | 49 | 17 | 120 |
| Police officer(s) | 11 | 11 | - |
| Sheriff | 2 | - | 30 |
| **Any mention** | **345 (0.1616%)** | **123 (0.2491%)** | **461 (0.5913%)** |

## Reading these numbers

LinkBoost-2025 has the highest rate by a clear margin - more than
double podawaa2024's rate - and the content is genuinely spread across
many distinct career-narrative posts, consistent with LinkBoost's
broader lean toward personal-narrative/career-journey content already
documented elsewhere in this repo (see, for example, the recurring
"resume rewrite" and career-transition templates in
[decision-points.md](decision-points.md) and
[career-transitions-content.md](career-transitions-content.md)).

"Police" leads in all three datasets, with "cop/cops" a consistent
second - informal phrasing outpacing more formal terms like "law
enforcement" or "police officer(s)" everywhere except HyperClapper,
where the two are close.

## Caveats

Same as every keyword scan in this repo: a match means the term
appears in the text, not that the post describes a genuine or accurate
law-enforcement career, incident, or experience.

<!-- export65-section -->
## The 65 export files

Added 22 October 2026. This is the same scan run on the 65 export files: 56,363 distinct records after the files are de-duplicated on record id, reading each record's `title` field, which holds the post text. These files are a separate set from the three datasets above, and nothing above this heading has changed. Their source, method and limits are in [provenance.md](../provenance.md#the-65-export-files) and [export-65-profile.md](export-65-profile.md). Rates use all 56,363 records as the denominator, and 237 of them have no post text. Command: `python3 analysis/law_enforcement_scan.py export65 /path/to/folder_with_the_65_files`.

```text
=== 65 export files (56,363 records) ===
Records mentioning any law-enforcement term: 189 (0.3353%)
Distinct underlying text values: 185
    police               125
    detective            40
    cop / cops           31
    police officer(s)    22
    law enforcement      20
    sheriff              3
```

189 of 56,363 records (0.335%) match. In the three datasets above the same measure is 0.162% in podawaa2024, 0.249% in HyperClapper and 0.591% in LinkBoost-2025 (using the corrected figure where this page gives one), which puts the 65 export files at the second highest of the four. The scan's duplicate-template check did not fire, and the matching records hold 185 distinct texts.

The rates come from different fields and different kinds of record, so a gap between them describes the files and does not describe the tools. A match is a keyword in the text, not a finding about the post or its author.
