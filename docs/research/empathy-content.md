# Empathy content

`analysis/empathy_content_scan.py` counts mentions of empathy-related
terms (empathy, empathetic, empathize) across post content in all
three datasets. Same discipline as every other scan in this repo:
aggregate counts only, no record, author, or matched text ever printed
beyond the duplicate-template check described below.

## Cross-category confirmation of an already-documented template

This scan's LinkBoost-2025 sample independently surfaces the "Empathy
isn't just a checkbox for leaders" post already found while checking
the burnout scan in
[career-transitions-content.md](career-transitions-content.md) - 56
occurrences here. Finding it again independently, from a completely
different keyword search, confirms it's a genuinely recurring,
cross-category leadership template rather than a one-off found by
coincidence in a single scan.

## LinkBoost-2025's low-distinct-ratio note, checked

The low-distinct-ratio note fires on LinkBoost-2025 (76 distinct
strings for 1,473 matches), but the duplicate-template warning does
not - no single string dominates (the top is 82 of 1,473, about 5.6%).
Checked manually: the top repeated strings span many distinct,
on-theme leadership/emotional-intelligence posts (a listening-skills
post, an "understand a person" post, a brand-with-heart post, the
empathy-checkbox-for-leaders post, ChatGPT email-writing prompts).
This is genuine signal, not an artifact.

## Results (VERIFIED - reproducible via the script)

| Term | podawaa2024 | HyperClapper | LinkBoost-2025 |
|---|---|---|---|
| Empathy | 1,025 | 399 | 1,357 |
| Empathetic | 195 | 40 | 134 |
| Empathize | 66 | 4 | 172 |
| **Any mention** | **1,188 (0.556%)** | **431 (0.873%)** | **1,473 (1.889%)** |

## Reading these numbers

LinkBoost-2025 has by far the highest rate - more than 2x HyperClapper's
and 3.4x podawaa2024's - continuing the same pattern already documented
across [confidence-content.md](confidence-content.md),
[being-human-content.md](being-human-content.md), and
[honesty-language-content.md](honesty-language-content.md):
LinkBoost-2025 consistently skews hardest toward
emotional/leadership/soft-skills content of every kind checked in this
repo.

HyperClapper shows a notably low "empathize" rate (4 mentions, versus
66 in podawaa2024 and 172 in LinkBoost-2025) despite having a
comparable overall pace to podawaa2024 for the noun form "empathy" -
the verb form barely appears there even though the noun does, a
pattern worth flagging even without a clear explanation for it.

## Caveats

Same as every keyword scan in this repo: a match means the term
appears in the text, not that the post reflects genuine empathetic
content or advice.

<!-- export65-section -->
## The 65 export files

Added 22 October 2026. This is the same scan run on the 65 export files: 56,363 distinct records after the files are de-duplicated on record id, reading each record's `title` field, which holds the post text. These files are a separate set from the three datasets above, and nothing above this heading has changed. Their source, method and limits are in [provenance.md](../provenance.md#the-65-export-files) and [export-65-profile.md](export-65-profile.md). Rates use all 56,363 records as the denominator, and 237 of them have no post text. Command: `python3 analysis/empathy_content_scan.py export65 /path/to/folder_with_the_65_files`.

```text
=== 65 export files (56,363 records) ===
Records mentioning any empathy-related term: 476 (0.845%)
Distinct underlying text values: 469
    empathy              443
    empathetic           45
    empathize            9
```

476 of 56,363 records (0.845%) match. In the three datasets above the same measure is 0.556% in podawaa2024, 0.873% in HyperClapper and 1.889% in LinkBoost-2025 (using the corrected figure where this page gives one), which puts the 65 export files at the second lowest of the four. The scan's duplicate-template check did not fire, and the matching records hold 469 distinct texts.

The rates come from different fields and different kinds of record, so a gap between them describes the files and does not describe the tools. A match is a keyword in the text, not a finding about the post or its author.
