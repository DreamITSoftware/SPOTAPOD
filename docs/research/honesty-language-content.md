# Kindness, lying, and deception language

`analysis/honesty_language_scan.py` counts mentions of kindness,
lying/lies/liar, and deception/deceptive language across post content
in all three datasets. Same discipline as every other scan in this
repo: aggregate counts only, no record, author, or matched text ever
printed beyond the duplicate-template check described below.

This is related to but distinct from
[authenticity-content.md](authenticity-content.md), which covers
self-description ("authentic," "honest truth," "real talk") rather than
this scan's focus on the underlying moral vocabulary of kindness,
dishonesty, and deception.

## Terms deliberately excluded

Bare "kind" and bare "lie" are excluded from their respective terms.
"Kind" collides heavily with filler usage ("what kind of," "kind
regards," "this kind of content") and "lie" collides with the unrelated
physical sense ("lie down"). Both terms require a qualifying form
(kindness, be kind; lying, lies, liar, lied) to stay reliable.

## LinkBoost-2025's low-distinct-ratio note, checked

The low-distinct-ratio note fires on LinkBoost-2025 (103 distinct
strings for 2,334 matches), but the duplicate-template warning does
not - no single string dominates. Checked manually: the top repeated
string is 121 of 2,334 matches (about 5%), and the top several are
genuinely distinct, on-theme posts (digital parenting, emotional
intelligence in children, an "AI & the Hug We Didn't Know We Needed"
post, kindness-as-power, happiness at work). This is genuine signal
consistent with that dataset's known structure, not a new artifact.

## Results (VERIFIED - reproducible via the script)

| Term | podawaa2024 | HyperClapper | LinkBoost-2025 |
|---|---|---|---|
| Lying / lies / liar(s) | 1,318 | 333 | 1,163 |
| Kindness | 818 | 335 | 1,081 |
| Deception / deceptive / deceit | 83 | 21 | 90 |
| **Any mention** | **2,189 (1.025%)** | **675 (1.367%)** | **2,334 (2.993%)** |

## Reading these numbers

"Lying/lies/liar" leads in podawaa2024 and LinkBoost-2025, while
kindness and lying are nearly tied in HyperClapper (335 vs. 333).
Deception-specific language is small everywhere - under 100 mentions in
every dataset, well behind both "kindness" and "lying" - suggesting
people write about honesty and dishonesty using everyday moral
vocabulary far more often than the more clinical term "deception"
itself.

LinkBoost-2025 has the highest overall rate (2.993%), consistent with
its documented lean toward inspirational/emotional content in
[authenticity-content.md](authenticity-content.md) - several of its top
repeated posts here belong to that same soft-motivational genre
(kindness-as-power, emotional intelligence, happiness-at-work).

## Caveats

Same as every keyword scan in this repo: a match means the term appears
in the text, not that the post contains genuine kindness, an actual
lie, or real deception. As with every category in this repo, a mention
of "lying" or "deception" is frequently the subject a post is warning
against, not a description of the post itself.

<!-- export65-section -->
## The 65 export files

Added 22 October 2026. This is the same scan run on the 65 export files: 56,363 distinct records after the files are de-duplicated on record id, reading each record's `title` field, which holds the post text. These files are a separate set from the three datasets above, and nothing above this heading has changed. Their source, method and limits are in [provenance.md](../provenance.md#the-65-export-files) and [export-65-profile.md](export-65-profile.md). Rates use all 56,363 records as the denominator, and 237 of them have no post text. Command: `python3 analysis/honesty_language_scan.py export65 /path/to/folder_with_the_65_files`.

```text
=== 65 export files (56,363 records) ===
Records mentioning any kindness/lying/deception term: 815 (1.446%)
Distinct underlying text values: 791
    lying / lies / liar              507
    kindness                         275
    deception / deceptive / deceit   43
```

815 of 56,363 records (1.446%) match. In the three datasets above the same measure is 1.025% in podawaa2024, 1.367% in HyperClapper and 2.993% in LinkBoost-2025 (using the corrected figure where this page gives one), which puts the 65 export files at the second highest of the four. The scan's duplicate-template check did not fire, and the matching records hold 791 distinct texts.

The rates come from different fields and different kinds of record, so a gap between them describes the files and does not describe the tools. A match is a keyword in the text, not a finding about the post or its author.
