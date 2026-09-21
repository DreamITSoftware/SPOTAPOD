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
