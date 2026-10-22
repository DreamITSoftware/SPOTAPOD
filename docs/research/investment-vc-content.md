# Investment / venture capital content

`analysis/investment_vc_scan.py` counts mentions of investment- and
venture-capital-related terms across post content in all three
datasets. Same discipline as every other scan in this repo: aggregate
counts only, no record, author, or matched text ever printed. Includes
the same duplicate-template safeguard introduced in
[nonprofit-content.md](nonprofit-content.md) - it reports distinct
underlying text values alongside every raw count and flags any field
where a single repeated string accounts for 20% or more of the
matching records.

## What this scan does not show

A record mentioning "investor" or "venture capital" is not evidence of
any violation of any law. Establishing that requires specific elements
this keyword scan doesn't and can't measure - a false statement of
fact, materiality, intent, actual reliance or harm, and often
jurisdiction and registration status.

If specific elements were separately established for a specific record,
the frameworks that would actually be relevant are:

- **16 CFR 465.8** - the same rule this whole project is built around.
  Requires scienter and commercial-purpose materiality for that
  specific record, which this scan doesn't establish.
- **FTC Endorsement Guides (16 CFR Part 255)** - relevant if content is
  a paid promotion of a specific investment product without disclosure.
  This scan doesn't check for sponsorship disclosure tied to investment
  content specifically; see [other-regulatory-signals.md](other-regulatory-signals.md)
  for the repo's general endorsement-disclosure-gap check.
- **Securities law (Securities Act 17(a), Exchange Act Rule 10b-5)** -
  relevant only if a post solicits investment in an actual,
  identifiable security and makes materially false or misleading
  statements in connection with that solicitation. Requires an actual
  security, an actual false statement, and reliance/harm - none of
  which a keyword count can show.
- **Investment Advisers Act of 1940** - relevant only if someone holds
  themselves out as providing personalized investment advice for
  compensation without being registered. Not something this scan checks.

## Results (VERIFIED - reproducible via the script)

| Term | podawaa2024 | HyperClapper | LinkBoost-2025 |
|---|---|---|---|
| Investment / investing | 4,754 (2.23%) | 1,233 (2.50%) | 2,397 (3.07%) |
| Investor(s) | 2,676 (1.25%) | 964 (1.95%) | 1,610 (2.07%) |
| VC (abbreviation) | 1,009 (0.47%) | 240 (0.49%) | 351 (0.45%) |
| IPO | 142 (0.07%) | 105 (0.21%) | 198 (0.25%) |
| Venture capital (spelled out) | 440 (0.21%) | 65 (0.13%) | 20 (0.03%) |
| Private equity | 246 (0.12%) | 51 (0.10%) | 131 (0.17%) |
| Seed funding / seed round | 148 (0.07%) | 31 (0.06%) | 47 (0.06%) |
| Series A/B/C funding | 88 (0.04%) | 24 (0.05%) | 15 (0.02%) |
| Angel investor | 92 (0.04%) | 12 (0.02%) | 10 (0.01%) |
| Venture capitalist(s) | 64 (0.03%) | 11 (0.02%) | 34 (0.04%) |
| **Any of the above** | **7,314 (3.43%)** | **2,253 (4.56%)** | **4,029 (5.17%)** |

No field triggered the duplicate-template warning. LinkBoost-2025's
distinct-string count (260 of 4,029 matching records) reflects that
dataset's known structure - many pod actions logged against a limited
set of target posts - documented already in
[baseline-profile.md](baseline-profile.md), not a new distortion.

## Reading these numbers

LinkBoost-2025 has the highest overall rate (5.17%), consistent with
its lean toward higher-level business/executive content already seen in
[entity-mentions.md](entity-mentions.md) (highest McKinsey and Fortune
mention rates) and [simple-titles.md](simple-titles.md) (highest
Founder/CEO title share).

"Venture capital" spelled out in full is inversely related to each
dataset's overall investment-content rate: podawaa2024 uses the full
phrase most (0.21%) while LinkBoost-2025, despite having the highest
overall rate, almost never does (0.03%) - most of its investment
content uses "investor," "investing," or "VC" instead.

This is one of the larger content categories checked in this repo so
far - higher than law-related content or nonprofit-related content,
though still well below the corporation-mention rate (13-23%) in
[entity-mentions.md](entity-mentions.md).

## Caveats

Same as every keyword scan in this repo: a match means the term
appears in the text, not that the post describes a real investment,
a real fund, or a real transaction.

<!-- export65-section -->
## The 65 export files

Added 22 October 2026. This is the same scan run on the 65 export files: 56,363 distinct records after the files are de-duplicated on record id, reading each record's `title` field, which holds the post text. These files are a separate set from the three datasets above, and nothing above this heading has changed. Their source, method and limits are in [provenance.md](../provenance.md#the-65-export-files) and [export-65-profile.md](export-65-profile.md). Rates use all 56,363 records as the denominator, and 237 of them have no post text. Command: `python3 analysis/investment_vc_scan.py export65 /path/to/folder_with_the_65_files`.

```text
=== 65 export files (56,363 records) ===
Records mentioning investment/VC terms: 3,951 (7.010%)
Distinct underlying text values: 3,862
    investment / investing                 2,361 (4.189%)
    investor(s)                            1,859 (3.298%)
    VC (venture capital abbrev.)           262 (0.465%)
    private equity                         191 (0.339%)
    IPO                                    125 (0.222%)
    venture capital                        92 (0.163%)
    seed funding / seed round              29 (0.051%)
    Series A/B/C funding                   20 (0.035%)
    angel investor                         13 (0.023%)
    venture capitalist(s)                  10 (0.018%)
    raised a round / raised funding        6 (0.011%)
    startup funding                        5 (0.009%)
```

3,951 of 56,363 records (7.01%) match. In the three datasets above the same measure is 3.43% in podawaa2024, 4.56% in HyperClapper and 5.17% in LinkBoost-2025 (using the corrected figure where this page gives one), which puts the 65 export files at the highest of the four. The scan's duplicate-template check did not fire, and the matching records hold 3,862 distinct texts.

The rates come from different fields and different kinds of record, so a gap between them describes the files and does not describe the tools. A match is a keyword in the text, not a finding about the post or its author.
