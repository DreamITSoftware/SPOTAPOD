# Simple title aggregate

`analysis/simple_title_aggregate.py` reports how many records' stated
occupation/headline text contains a simple, generic professional title
keyword - "CEO," "Founder," "Coach," "Marketer," and so on. Same
discipline as every other scan in this repo: only aggregate counts are
reported. No name, handle, or verbatim occupation/headline sentence is
ever printed by this script or appears on this page.

## Scope

Only **HyperClaper.json** and **LinkBoost-2025.json** are covered.
`podawaa2024.json` has no occupation/headline-equivalent field at all, so
there's nothing to aggregate there.

HyperClaper.json's own `jobTitle` field is almost entirely empty (1 of
49,369 records) - the actual signal lives in `linkedin_data.headline`,
which is what this script reads instead. LinkBoost-2025.json's
`Occupation` field is used directly.

## Method

Each record's headline/occupation text is checked against seventeen
simple-title keyword patterns, in a fixed priority order (broader
seniority titles like "Founder" and "CEO" are checked before narrower
functional ones like "Coach," so "Founder & Marketing Coach" lands under
Founder, not Coach - an arbitrary but fixed and reproducible rule). A
record is assigned to the first matching title, or `unspecified_other` if
none match. Records with no headline/occupation text at all are tracked
separately and excluded from the percentage base for the title buckets.

This is the same "simple, generic keyword, aggregate count only" approach
as [topic-taxonomy.md](topic-taxonomy.md), applied to stated titles
instead of post content.

## Results (VERIFIED - reproducible via the script)

### HyperClapper (49,369 records; 24.0% have no headline text at all)

| Title | Count | % |
|---|---|---|
| Marketer | 5,794 | 11.7% |
| Founder / Co-Founder | 4,221 | 8.5% |
| Manager | 1,709 | 3.5% |
| Specialist | 1,668 | 3.4% |
| Engineer / Developer | 1,651 | 3.3% |
| CEO | 1,097 | 2.2% |
| Coach | 1,013 | 2.1% |
| Speaker / Trainer | 878 | 1.8% |
| Analyst | 563 | 1.1% |
| Director | 436 | 0.9% |
| Consultant / Advisor | 398 | 0.8% |
| Owner / Entrepreneur | 341 | 0.7% |
| Designer | 263 | 0.5% |
| Author / Writer | 175 | 0.4% |
| President | 49 | 0.1% |
| Recruiter | 7 | 0.0% |
| VP / Vice President | 2 | 0.0% |
| `unspecified_other` | 17,235 | 34.9% |

### LinkBoost-2025 (77,969 records; 3.9% have no occupation text at all)

| Title | Count | % |
|---|---|---|
| Founder / Co-Founder | 15,802 | 20.3% |
| Coach | 11,259 | 14.4% |
| CEO | 5,400 | 6.9% |
| Consultant / Advisor | 4,566 | 5.9% |
| Marketer | 4,143 | 5.3% |
| Speaker / Trainer | 2,691 | 3.5% |
| Director | 2,497 | 3.2% |
| Owner / Entrepreneur | 2,293 | 2.9% |
| Engineer / Developer | 1,561 | 2.0% |
| Author / Writer | 1,290 | 1.7% |
| President | 250 | 0.3% |
| Manager | 141 | 0.2% |
| Recruiter | 28 | 0.0% |
| VP / Vice President | 19 | 0.0% |
| Analyst | 10 | 0.0% |
| Specialist | 9 | 0.0% |
| Designer | 0 | 0.0% |
| `unspecified_other` | 22,939 | 29.4% |

## Reading these numbers

- **LinkBoost skews heavily toward Founder/Coach** (34.7% combined) versus
  HyperClapper's lean toward Marketer/Founder (20.2% combined) -
  consistent with the `leadership_coaching_motivation` topic-category
  finding in [topic-taxonomy.md](topic-taxonomy.md), where LinkBoost's
  18.91% far outpaces the ~6% seen in the other two files.
- **`unspecified_other` is large in both files** (34.9% and 29.4%) -
  expected, since seventeen keyword patterns can't exhaustively cover
  every real job title (e.g. "Nurse," "Teacher," "Attorney" aren't in the
  list), and free-text headlines often lead with a personal tagline
  rather than a title at all.
- **Same caveats as every other keyword scan in this repo**: a record's
  bucket depends on which pattern happens to match first in priority
  order, this is not a verified job classification, and no claim is made
  about any specific record or the person behind it.
