# Law-related content

`analysis/law_content_scan.py` counts how many records touch legal/law
language, at two levels of breadth. Same discipline as every other scan
in this repo: aggregate counts only, no record or author ever identified.

## Method

**NARROW** (legal-profession-specific): lawyer, attorney, law firm,
litigation, paralegal, bar exam, JD, legal counsel, general counsel.

**BROADER**: everything in NARROW, plus legislation, compliance,
intellectual property, contract law, employment law, lawsuit, court
case/courtroom, and the bare adjective "legal."

"Compliance" and bare "legal" are deliberately reported as their own
line items within the broader tally rather than folded in silently,
because both terms are heavily used in general business/HR contexts
(data compliance, workplace compliance) that aren't really "about law"
the way a lawyer or law-firm post is. For most questions this scan is
likely to be asked to answer, the **narrow** tally is the more
meaningful number.

## Results (VERIFIED - reproducible via the script)

### Narrow: legal-profession-specific content

| Dataset | Records | % |
|---|---|---|
| podawaa2024 | 459 | 0.22% |
| HyperClapper | 168 | 0.34% |
| LinkBoost-2025 | 447 | 0.57% |

Top term in every dataset is "lawyer," followed by "attorney" and
"litigation."

### Broader: includes compliance, legislation, IP, etc.

| Dataset | Records | % |
|---|---|---|
| podawaa2024 | 3,064 | 1.44% |
| HyperClapper | 1,235 | 2.50% |
| LinkBoost-2025 | 3,473 | 4.45% |

"Compliance" alone accounts for roughly half of all broader-category
hits in every dataset (1,556 of 3,064 in podawaa2024; 712 of 1,235 in
HyperClapper; 1,794 of 3,473 in LinkBoost-2025).

## Reading these numbers

Genuine legal-profession content is small in absolute terms everywhere
(under 0.6% of any dataset by the narrow measure). LinkBoost-2025 has
the highest concentration under both measures, consistent with its
broader lean toward professional-services content already noted for
consulting firms in [entity-mentions.md](entity-mentions.md) (McKinsey
mentions there are also highest in LinkBoost-2025).

## Caveats

Same as every keyword scan in this repo: a match means the term appears
in the text, not that the post is meaningfully about a legal topic.
"Legal" and "compliance" in particular are broad enough to catch
tangential or unrelated mentions, which is exactly why they're broken
out as separate line items rather than blended into a single combined
count.
