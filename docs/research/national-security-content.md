# National security / NSA content

`analysis/national_security_scan.py` counts mentions of
national-security-related terms (national security, NSA, CIA, FBI,
intelligence agency, homeland security, classified information,
national defense) across post content in all three datasets. Same
discipline as every other scan in this repo: aggregate counts only, no
record, author, or matched text ever printed beyond the
duplicate-template check below.

## The correction this scan's safeguard caught

Same duplicate-template safeguard as
[nonprofit-content.md](nonprofit-content.md) and
[travel-content.md](travel-content.md): the script reports distinct
underlying text values alongside every raw count, and flags a field
where a single repeated string accounts for 20% or more of matches. It
fired on first run: LinkBoost-2025's "FBI" count of 15 is one boosted
news-commentary post about the Jordan Belfort/Wolf of Wall Street
financial-fraud case, not 15 distinct posts actually about the FBI.
Corrected, LinkBoost-2025's real any-mention count is 21, not 35.

## Results (VERIFIED - reproducible via the script)

| Term | podawaa2024 | HyperClapper | LinkBoost-2025 |
|---|---|---|---|
| CIA | 40 | 2 | - |
| FBI | 36 | 4 | 15\* |
| NSA | 24 | 1 | - |
| National security | 23 | 31 | 20 |
| Intelligence agency/agencies | 6 | - | - |
| Homeland security | 4 | - | - |
| National defense | 3 | 2 | - |
| **Any mention (raw)** | **118 (0.055%)** | **40 (0.081%)** | **35 (0.045%)** |
| **Any mention (corrected)** | 118 (no correction needed) | 40 (no correction needed) | **21 (0.027%)** |

\* See correction above - this is one repeated post, not 15 distinct ones.

## Reading these numbers

This is the smallest content category checked in this repo so far -
smaller than law-related content, nonprofit-related content,
investment/VC content, cybersecurity content, or travel content, all of
which sit well below 10% but still meaningfully above this one. Every
figure here is under 0.1% of its dataset. NSA specifically is almost
nonexistent: 24 mentions in podawaa2024 (213,491 records), 1 in
HyperClapper, and 0 in LinkBoost-2025.

These are professional/business/career datasets. National-security
content isn't a meaningful presence in any of them, and the low counts
here are consistent with that rather than a surprising finding on their
own.

## Caveats

Same as every keyword scan in this repo: a match means the term
appears in the text, not that the post contains genuine national
security information, commentary, or expertise. At counts this small,
individual posts can shift the percentage meaningfully, which is
exactly why the duplicate-template check matters even more here than in
larger categories.

<!-- export65-section -->
## The 65 export files

Added 22 October 2026. This is the same scan run on the 65 export files: 56,363 distinct records after the files are de-duplicated on record id, reading each record's `title` field, which holds the post text. These files are a separate set from the three datasets above, and nothing above this heading has changed. Their source, method and limits are in [provenance.md](../provenance.md#the-65-export-files) and [export-65-profile.md](export-65-profile.md). Rates use all 56,363 records as the denominator, and 237 of them have no post text. Command: `python3 analysis/national_security_scan.py export65 /path/to/folder_with_the_65_files`.

```text
=== 65 export files (56,363 records) ===
Records mentioning any national-security term: 112 (0.1987%)
Distinct underlying text values: 108
    national security                  54
    FBI                                34
    NSA                                13
    CIA                                6
    homeland security                  5
    intelligence agency / agencies     4
    national defense                   4
```

112 of 56,363 records (0.199%) match. In the three datasets above the same measure is 0.055% in podawaa2024, 0.081% in HyperClapper and 0.027% in LinkBoost-2025 (using the corrected figure where this page gives one), which puts the 65 export files at the highest of the four. The scan's duplicate-template check did not fire, and the matching records hold 108 distinct texts.

The rates come from different fields and different kinds of record, so a gap between them describes the files and does not describe the tools. A match is a keyword in the text, not a finding about the post or its author.
