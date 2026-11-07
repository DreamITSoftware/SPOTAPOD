# TED / TEDx content

`analysis/ted_content_scan.py` counts mentions of TED/TEDx-related
content across post content in all three datasets. As with
every other scan in this repo, it reports aggregate counts only, with no record,
author, or matched text printed beyond the duplicate-template
check described below.

## A deliberate design choice: bare "TED" is matched case-sensitively

Bare "TED" risks collisions more than most terms in this repo,
since it is also a common first name (Ted, short for Theodore/Edward).
This script matches bare "TED" case-SENSITIVELY (all-caps only),
unlike every other term-based scan in this repo, which matches
case-insensitively. Personal names are rarely written in
all-caps prose, so this reduces (though does not
eliminate) the collision risk, at the cost of missing any
all-caps sentence that contains the personal name "TED". This is
an acceptable trade, since all-caps personal names are rare in ordinary writing. "TEDx" and "TED
Talk(s)" are unambiguous phrases and are matched case-insensitively as
usual.

## LinkBoost-2025's correction: one listicle post

The duplicate-template warning fires on LinkBoost-2025: 41 of 66
matches trace to a single repeated post, a "5 Habits TED Talk Speakers
Swear By" listicle, boosted by the platform's structure. Checked
directly, it is genuine content, not a false positive. Corrected,
LinkBoost-2025's real any-mention count is 26, not 66.

## Results (VERIFIED - reproducible via the script)

| Term | podawaa2024 | HyperClapper | LinkBoost-2025 |
|---|---|---|---|
| TEDx | 93 | 228 | 0 |
| TED Talk(s) | 102 | 20 | 66 |
| TED (strict, all-caps) | 103 | 30 | 66 |
| **Any mention (raw)** | **228 (0.1068%)** | **256 (0.5185%)** | **66 (0.0846%)** |
| **Any mention (corrected)** | 228 (no correction needed) | 256 (no correction needed) | **26 (0.033%)** |

## Reading these numbers

HyperClapper has the highest overall rate, and it's dominated almost
entirely by "TEDx" specifically (228 of 256, 89%). In podawaa2024,
"TED Talk(s)" and bare "TED" lead instead, and
LinkBoost-2025 never mentions TEDx.

HyperClapper skews toward people
citing their own TEDx speaking credentials, a common LinkedIn
credibility signal that connects to the speaker/thought-leader
self-description pattern already documented in
[speaker-thought-leader.md](speaker-thought-leader.md). podawaa2024 and
LinkBoost-2025 skew toward referencing or
listing TED content generally rather than personal TEDx
involvement.

## Caveats

As with every keyword scan in this repo, a match means the term
appears in the text, not that the post describes a genuine TEDx talk,
speaking credential, or accurate TED-related content. The case-
sensitivity trade-off for bare "TED" described above is a deliberate
precision-over-recall choice specific to this scan.

<!-- export65-section -->
## The 65 export files

Added 22 October 2026. This is the same scan run on the 65 export files: 56,363 distinct records after the files are de-duplicated on record id, reading each record's `title` field, which holds the post text. These files are a separate set from the three datasets above, and nothing above this heading has changed. Their source, method and limits are in [provenance.md](../provenance.md#the-65-export-files) and [export-65-profile.md](export-65-profile.md). Rates use all 56,363 records as the denominator, and 237 of them have no post text. Command: `python3 analysis/ted_content_scan.py export65 /path/to/folder_with_the_65_files`.

```text
=== 65 export files (56,363 records) ===
Records mentioning any TED/TEDx term: 63 (0.1118%)
Distinct underlying text values: 62
    TEDx                     33
    TED Talk(s)              24
    TED (strict, all-caps)   34
```

63 of 56,363 records (0.112%) match. In the three datasets above the same measure is 0.107% in podawaa2024, 0.518% in HyperClapper and 0.033% in LinkBoost-2025 (using the corrected figure where this page gives one), which puts the 65 export files at the second highest of the four. The scan's duplicate-template check did not fire, and the matching records hold 62 distinct texts.

The rates come from different fields and different kinds of record, so a gap between them describes the files and does not describe the tools. A match is a keyword in the text, not a finding about the post or its author.
