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

<!-- export65-section -->
## The 65 export files

Added 22 October 2026. This is the same scan run on the 65 export files: 56,363 distinct records after the files are de-duplicated on record id, reading each record's `title` field, which holds the post text. These files are a separate set from the three datasets above, and nothing above this heading has changed. Their source, method and limits are in [provenance.md](../provenance.md#the-65-export-files) and [export-65-profile.md](export-65-profile.md). Rates use all 56,363 records as the denominator, and 237 of them have no post text. Command: `python3 analysis/law_content_scan.py export65 /path/to/folder_with_the_65_files`.

```text
=== 65 export files (56,363 records, 48.1s) ===
NARROW (legal profession specific): 301 (0.534%)
    lawyer                       159 (0.282%)
    attorney                     91 (0.161%)
    litigation                   39 (0.069%)
    law firm                     35 (0.062%)
    general counsel              7 (0.012%)
    paralegal                    6 (0.011%)
    legal counsel                3 (0.005%)
BROADER (incl. legislation/compliance/IP/etc.): 2,597 (4.608%)
    compliance                   1,765 (3.131%)
    legal (adjective, general)   654 (1.160%)
    lawyer                       159 (0.282%)
    intellectual property        100 (0.177%)
    attorney                     91 (0.161%)
    lawsuit                      74 (0.131%)
    litigation                   39 (0.069%)
    law firm                     35 (0.062%)
    legislation                  30 (0.053%)
    court case                   27 (0.048%)
    general counsel              7 (0.012%)
    employment law               7 (0.012%)
    paralegal                    6 (0.011%)
    legal counsel                3 (0.005%)
    contract law                 3 (0.005%)
```

301 of 56,363 records (0.534%) match the narrow legal-profession patterns, against 0.22% (podawaa2024), 0.34% (HyperClapper) and 0.57% (LinkBoost-2025), which is the second highest of the four. 2,597 (4.608%) match the broader patterns, against 1.44%, 2.50% and 4.45%, which is the highest of the four. Most of the broader count is the word compliance (1,765 records, 3.131%), which a post can use without any link to the legal profession.

The rates come from different fields and different kinds of record, so a gap between them describes the files and does not describe the tools. A match is a keyword in the text, not a finding about the post or its author.
