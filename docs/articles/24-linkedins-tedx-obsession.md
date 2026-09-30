# LinkedIn's Quiet Obsession with TEDx Credentials

### One dataset mentions TEDx more than twice as often as any other name-brand credential checked in this project

TEDx shows up 228 times in a 49,369-post dataset. That's more than double its rate anywhere else this project has checked, while a completely different dataset barely touches it at all.

## A name that needed unusual handling

"TED" is a genuine collision risk in a way most terms in this project aren't. It's also a common first name, short for Theodore or Edward. To handle that, the underlying scan matches bare "TED" case-sensitively. Only all-caps "TED" counts, since personal names are essentially never written in all-caps prose. "TEDx" and "TED Talk(s)" are unambiguous phrases and matched normally. This trades a small amount of recall (an all-caps sentence that happens to contain the name "Ted" would be missed) for a real reduction in false positives from the name collision.

## The numbers, and the one that needed a second look

| Term | podawaa2024 | HyperClapper | LinkBoost-2025 |
|---|---|---|---|
| TEDx | 93 | 228 | 0 |
| TED Talk(s) | 102 | 20 | 66 |
| TED (strict) | 103 | 30 | 66 |
| **Any mention (raw)** | 228 | 256 | 66 |

LinkBoost-2025's 66 raw matches looked suspicious. Checking them directly found 41 traced to a single repeated post, a "5 Habits TED Talk Speakers Swear By" listicle, boosted by the platform's own structure. Checked against the actual text, this turned out to be genuine content, not a false positive, just one post amplified at scale. Corrected, LinkBoost-2025's real count is 26, not 66.

## What the gap says about the datasets

HyperClapper's heavy skew toward TEDx specifically (228 of its 256 total mentions), versus podawaa2024's more even split between TEDx and general "TED Talk(s)" language, suggests HyperClapper's population leans harder toward people citing their own TEDx speaking credentials as a personal-brand signal. That's consistent with that dataset's broader thought-leader and speaker self-description patterns documented elsewhere in this project.

## What this is, and isn't

**VERIFIED**, reproducible via the published scan: the raw and corrected counts above.

Full methodology: **github.com/DreamITSoftware/SPOTAPOD**.

---

*Self-published. Not peer-reviewed. Independently reproducible from the source files.*
