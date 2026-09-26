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
