# Animal content

`analysis/animal_content_scan.py` counts mentions of animal-related
terms (animal(s), pet(s), dog(s), cat(s)) across post content in all
three datasets. Same discipline as every other scan in this repo:
aggregate counts only, no record, author, or matched text ever printed
beyond the duplicate-template check described below.

## "Cat" has real, varied collision problems this repo hasn't seen with any other short word

Bare "cat"/"cats" turned out to have more collision sources than any
other term checked in this repo. Sampling actual matches found:

- **"CAT" as India's major MBA entrance exam** (Common Admission Test)
  - plausible given this dataset's documented Indian-population skew,
  see [demographics.md](demographics.md)
- **The ".cat" domain extension** (Catalonia's country code)
- **A French insurance term** ("Cat Nat" = catastrophes naturelles)
- **"cat" as an abbreviation for the Catalan language** in multilingual
  bio/skills listings
- **"CAT" as the NYSE ticker symbol for Caterpillar Inc.**
- **"Cat 1" through "Cat 5"** - hurricane category scale, referring to
  storm intensity, not animals at all
- **"Fat Cats"** - an idiom for wealthy elites
- **Jaguar's "leaping cat" logo** in a brand-redesign post

The script reports both a LOOSE count (bare "cat"/"cats",
case-insensitive, matching every other term in this scan) and a STRICT
count (requiring "cat"/"cats" to appear with a clear possessive/article
immediately before it, or in an explicit "cats and dogs" / "pet cat(s)"
/ "kitten" pairing).

**The most striking result: LinkBoost-2025's strict count is zero.**
All 15 distinct "cat"-matching strings there trace to non-animal
usage - the Caterpillar stock ticker, hurricane categories, the "fat
cats" idiom, cat-video internet-culture references used dismissively,
and the Jaguar logo story. Not one is a post about an actual animal.

podawaa2024's strict count is 28.5% of its loose count, and
HyperClapper's is 39.3% - both real overcounts, though the strict
pattern itself undercounts some genuine mentions (e.g. "cat videos" or
"cat memes" with no article), so neither number alone is a precise
ground truth.

"Dog(s)," "animal(s)," and "pet(s)" were sampled and confirmed to not
have this problem.

## LinkBoost-2025's low-distinct-ratio note, checked

The low-distinct-ratio note fires on LinkBoost-2025 for the overall
animal-term count (57 distinct strings for 1,054 matches), but the
duplicate-template warning does not - no single string dominates (the
top is 129 of 1,054, about 12%). Checked manually: the top repeated
strings are genuinely distinct, on-theme posts, led by a
leadership-metaphor post about a sheepdog. This is genuine signal for
the overall count, separate from the "cat"-specific contamination
documented above.

## Results (VERIFIED - reproducible via the script)

| Term | podawaa2024 | HyperClapper | LinkBoost-2025 |
|---|---|---|---|
| Dog(s) | 489 | 176 | 444 |
| Animal(s) | 393 | 57 | 331 |
| Pet(s) | 227 | 75 | 204 |
| Cat(s) [loose] | 193 | 89 | 185 |
| Cat(s) [strict] | 55 (28.5%) | 35 (39.3%) | 0 (0.0%) |
| **Any mention (raw, includes loose cat)** | **1,158 (0.542%)** | **356 (0.721%)** | **1,054 (1.352%)** |

## Reading these numbers

Treat "dog(s)," "animal(s)," and "pet(s)" as trustworthy. Treat
"cat(s)" as unreliable everywhere, and treat it as essentially
worthless as a signal in LinkBoost-2025 specifically, where every
sampled match traces to something other than an actual animal.

## Caveats

Same as every keyword scan in this repo: a match means the term
appears in the text, not that the post is genuinely about an animal.
This applies with unusual force to "cat(s)" here, more than to any
other term documented in this repo.

<!-- export65-section -->
## The 65 export files

Added 22 October 2026. This is the same scan run on the 65 export files: 56,363 distinct records after the files are de-duplicated on record id, reading each record's `title` field, which holds the post text. These files are a separate set from the three datasets above, and nothing above this heading has changed. Their source, method and limits are in [provenance.md](../provenance.md#the-65-export-files) and [export-65-profile.md](export-65-profile.md). Rates use all 56,363 records as the denominator, and 237 of them have no post text. Command: `python3 analysis/animal_content_scan.py export65 /path/to/folder_with_the_65_files`.

```text
=== 65 export files (56,363 records) ===
Records mentioning any animal-related term: 491 (0.871%)
Distinct underlying text values: 476
    dog(s)               228
    animal(s)            158
    pet(s)               136
    cat(s) [loose]       97
    cat(s) [strict]      31 (32.0% of loose -- see docstring, 'cat' has real collision problems: CAT exam, .cat TLD, Catalan-language abbreviation)
```

491 of 56,363 records (0.871%) match. In the three datasets above the same measure is 0.542% in podawaa2024, 0.721% in HyperClapper and 1.352% in LinkBoost-2025 (using the corrected figure where this page gives one), which puts the 65 export files at the second highest of the four. The scan's duplicate-template check did not fire, and the matching records hold 476 distinct texts.

The rates come from different fields and different kinds of record, so a gap between them describes the files and does not describe the tools. A match is a keyword in the text, not a finding about the post or its author.
