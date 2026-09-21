# Children-related content

`analysis/children_content_scan.py` counts mentions of children-related
terms (child/children, kid/kids, daughter, toddler, baby/babies,
parenting, and a corrected "son" check) across post content in all
three datasets. Same discipline as every other scan in this repo:
aggregate counts only, no record, author, or matched text ever printed
beyond the duplicate-template check described below.

## The correction: "son" was catching French, not children

An earlier draft matched bare "son"/"sons" case-insensitively, like
every other term in this scan. That pattern also matches "son," the
French possessive pronoun meaning "his/her" (e.g., "elle a pris le
controle de son compte" - "she took control of her account"), and
podawaa2024 contains a meaningful amount of French-language content -
the same underlying fact already behind the "MIT"/German "mit"
collision in [university-content.md](university-content.md) and this
project's earlier France/Paris finding.

The raw case-insensitive count for podawaa2024 was 17,573 - by far the
largest single term in the entire scan, and wildly inconsistent with
"son" being a minor term in the other two datasets. A manual check
confirmed the problem: only **1.5%** of those matches (269 records) show
a clear English usage pattern referring to an actual child ("my son,"
"her son," "son of," "son is," etc.). The remaining 98.5% is the French
possessive pronoun or otherwise ambiguous.

The shipped script requires "son"/"sons" to appear with a clear English
usage marker (a possessive pronoun or article immediately before it, or
"of/is/was/are/were/who" immediately after) rather than matching the
bare word. Every other term in this scan does not have this problem and
is matched case-insensitively as usual.

## Results (VERIFIED - reproducible via the script)

| Term | podawaa2024 | HyperClapper | LinkBoost-2025 |
|---|---|---|---|
| Kid/kids | 887 | 656 | 2,326 |
| Child/children | 1,171 | 695 | 1,230 |
| Baby/babies | 362 | 98 | 326 |
| Daughter | 242 | 97 | 292 |
| Son (clear English usage only) | 269 | 102 | 516 |
| Parenting | 81 | 73 | 259 |
| Toddler | 42 | 21 | 133 |
| **Any mention** | **2,630 (1.232%)** | **1,417 (2.870%)** | **4,128 (5.294%)** |

LinkBoost-2025's low-distinct-ratio note (204 distinct strings for
4,128 matches) was checked manually - the top repeated string is under
4% of matches, and the top several are genuinely distinct, on-theme
posts (a "young boy's heartfelt expression," a digital-parenting post,
a post on emotional intelligence in children), consistent with that
dataset's known structure, not a new artifact.

## Reading these numbers

Children-related content is small everywhere - 1.2% to 5.3% of any
dataset. LinkBoost-2025 has consistently the highest rate, in line with
its documented lean toward emotional/family-themed content already
established in [authenticity-content.md](authenticity-content.md) and
[honesty-language-content.md](honesty-language-content.md) (kindness,
emotional intelligence, and similar soft-motivational genres).

Nothing in any of the three datasets suggests substantive content
specifically about or targeting children - these are near-uniformly
incidental family-life mentions (parenting stories, "my daughter,"
milestone posts) within otherwise professional/career content, not a
distinct content category in its own right.

## Caveats

Same as every keyword scan in this repo: a match means the term
appears in the text, not that the post substantively concerns a real
child. The corrected "son" pattern trades some recall for precision -
an unusually structured English sentence referencing a son without one
of the checked markers nearby would be missed, though this is a much
smaller error than the 98.5% false-positive rate it replaces.
