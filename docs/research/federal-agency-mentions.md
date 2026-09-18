# Federal agency mentions

`analysis/federal_agency_scan.py` counts mentions of named U.S. federal
agencies, plus the generic phrases "federal agency/agencies" and
"government agency/agencies," across post content. Same discipline as
every other scan in this repo: aggregate counts only, no record, author,
or matched text ever printed beyond the duplicate-template check below.

## A provenance caveat this doc has that the others don't

Every other scan in `docs/research/` was run against the three checksummed
files in [checksums/CHECKSUMS.txt](../../checksums/CHECKSUMS.txt). The
figures below were computed by running `federal_agency_scan.py` against
**`hyperclapper-gamers.json`**, a file whose relationship to this repo's checksummed
`HyperClaper.json` is an unresolved **INFERENCE**, not a confirmed match —
see the "Candidate duplicate: hyperclapper-gamers.json" section of
[provenance.md](../provenance.md) for the full writeup (same record count,
same profile count, same field-completeness pattern, but a different
sha256).

That said, this scan itself adds a data point to that inference, not just
a new topic count: `hyperclapper-gamers.json`'s counts for terms this repo has already
published independently — FBI (4), CIA (2), NSA (1), FDA (15) — match
[national-security-content.md](national-security-content.md)'s and
[pharma-content.md](pharma-content.md)'s previously published
`HyperClaper.json` figures exactly. That's a second, independent line of
agreement (beyond record/profile counts) between the two files, for terms
this doc's script didn't set out to reproduce. It still isn't a hash
match, and this doc does not treat it as one — but it's stronger
corroboration than either file's structure alone.

## Why ICE and SEC needed case-sensitive matching

A first, case-insensitive pass on this dataset returned 89 "ICE" matches
and 45 "SEC" matches — both badly inflated by common-word collisions:
lowercase "ice" turned up in "ice cream," "break the ice," and similar
phrases having nothing to do with Immigration and Customs Enforcement;
lowercase "sec" turned up as an abbreviation for seconds ("60-90 sec,"
"0.41 sec"). Restricting both terms (and every other bare acronym in this
scan) to a case-sensitive, whole-word match dropped ICE to 6 and SEC to
22 — the number in the results table below. This is the same fix
`university_content_scan.py` applies to MIT (to avoid matching German
"mit"); see [university-content.md](university-content.md).

## Results

| Term | Count |
|---|---|
| White House | 24 |
| SEC (Securities and Exchange Commission) | 22 |
| NASA | 17 |
| IRS | 16 |
| FDA | 15 |
| DOD / Pentagon | 14 |
| CDC | 9 |
| ICE | 6 |
| DEA | 6 |
| FTC | 4 |
| FBI | 4 |
| DOJ (acronym) | 4 |
| Department of Justice (spelled out) | 3 |
| Secret Service | 3 |
| generic "federal agency/agencies" | 3 |
| generic "government agency/agencies" | 3 |
| CIA | 2 |
| ATF | 2 |
| HHS | 2 |
| FEMA | 1 |
| FCC | 1 |
| NSA | 1 |
| State Department | 1 |
| **Any mention** | **152 (0.308%)** |

No duplicate-template warning fired: 146 distinct underlying strings
across 152 matches, no single repeated post driving the count.

## Reading these numbers

This is a small category overall — smaller than
[pharma-content.md](pharma-content.md)'s 0.296% for HyperClapper but in
the same general range, and larger than
[national-security-content.md](national-security-content.md)'s narrower
0.081% (that scan's term list is a strict subset of this one: it covers
CIA/FBI/NSA/national security/homeland security/national defense, not the
full federal-agency roster here).

The composition looks like ordinary professional/business content brushing
up against federal agencies as *subject matter*, not agency-affiliated
posting: SEC mentions cluster around IPO speculation (OpenAI, SpaceX) and
disclosure-requirement commentary; FDA/CDC cluster with the existing
pharma/health content already documented in pharma-content.md; NASA
appears in space/tech commentary unrelated to regulatory content; White
House appears mostly in AI-policy and executive-order commentary. No
agency here shows the kind of single-post-driven spike that needed
correcting in national-security-content.md's LinkBoost-2025 FBI count or
pharma-content.md's LinkBoost-2025 FDA count.

## Caveats

Same as every keyword scan in this repo: a match means the term appears
in the text, not that the post contains accurate commentary about, or any
actual connection to, the named agency. And per the provenance caveat
above, treat this specific doc's counts as describing `hyperclapper-gamers.json`, not
as a new, independently-verified figure for the checksummed
`HyperClaper.json` — the two are very likely the same underlying data,
but "very likely" is not "confirmed."
