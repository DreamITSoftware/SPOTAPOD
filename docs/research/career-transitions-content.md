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
