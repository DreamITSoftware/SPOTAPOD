# Travel agencies and destinations

`analysis/travel_content_scan.py` counts mentions of travel
agencies/booking platforms and travel destinations across post content
in all three datasets. Same discipline as every other scan in this
repo: aggregate counts only, no record, author, or matched text ever
printed beyond the duplicate-template check described below.

## Two real corrections found while building this

**1. LinkBoost-2025 needs the duplicate-template correction almost
everywhere.** The script's built-in safeguard (same as
[nonprofit-content.md](nonprofit-content.md) and
[investment-vc-content.md](investment-vc-content.md)) flagged dominant
repeated strings in nearly every LinkBoost-2025 term checked - a single
AI-travel-tool ad post, boosted 47 times, accounts for all 48 mentions
each of Expedia, Booking.com, TripAdvisor, and Hotels.com. This isn't a
series of separate discoveries; it's one fact about the dataset's
structure (only 469 distinct target posts across 77,969 records,
documented in [baseline-profile.md](baseline-profile.md)) showing up
every time a keyword happens to match one of a small number of
heavily-boosted posts. Read every LinkBoost-2025 number in this doc as
"how many pod actions touched a post mentioning X," not "how many
distinct posts mentioned X."

**2. podawaa2024's "France" and "Paris" counts are not travel content.**
Unlike the LinkBoost pattern, this one isn't duplication - 7,695 of
8,010 "France" matches are genuinely distinct posts. Reading a sample
showed why: this is French-language content discussing French domestic
topics (workplace sexism reporting, French tech news, French politics),
where the country name appears naturally and has nothing to do with
travel recommendations. No automated distinct-string check catches
this; it required reading actual post text. The script prints a fixed
warning when scanning podawaa2024 for exactly this reason.

## Results (VERIFIED - reproducible via the script)

### Travel agencies/platforms (raw counts; see corrections above for LinkBoost-2025)

| Platform | podawaa2024 | HyperClapper | LinkBoost-2025 (raw / corrected) |
|---|---|---|---|
| Airbnb | 261 (0.12%) | 149 (0.30%) | 189 / ~142 |
| Expedia | 16 | 17 | 48 / ~2 |
| Booking.com | 20 | 10 | 48 / ~2 |
| TripAdvisor | 20 | 5 | 48 / ~2 |
| Hotels.com | 4 | - | 48 / ~2 |
| Kayak | 27 | 4 | - |
| VRBO | 13 | 2 | - |
| MakeMyTrip | 4 | 6 | - |

Airbnb is the only platform with clean, uncorrected, genuinely distinct
signal across all three datasets.

### Destinations (raw counts; podawaa2024's France/Paris excluded per the note above; LinkBoost-2025 needs the same correction as the agencies table)

| Destination | podawaa2024 | HyperClapper | LinkBoost-2025 (raw) |
|---|---|---|---|
| Dubai | 754 | 219 | 111 |
| London | 844 | 161 | 251 |
| Singapore | 467 | 99 | 39 |
| Japan | 231 | 98 | 165 |
| Italy | 413 | 65 | 137 |
| Rome | - | 34 | 164 |
| Thailand | 157 | 29 | 104 |
| Miami | 370 | 76 | 51 |
| New York City | 247 | 43 | 289 |

Excluding the France/Paris artifact, Dubai and London are the most
consistently mentioned destinations across all three datasets.

## Caveats

Same as every keyword scan in this repo: a match means the term
appears in the text, not that the post is a genuine, credible travel
recommendation. This doc's own two corrections above are a reminder
that a raw keyword count on its own, without checking for both
duplicate templates and language/context artifacts, can be actively
misleading rather than just imprecise.

<!-- export65-section -->
## The 65 export files

Added 22 October 2026. This is the same scan run on the 65 export files: 56,363 distinct records after the files are de-duplicated on record id, reading each record's `title` field, which holds the post text. These files are a separate set from the three datasets above, and nothing above this heading has changed. Their source, method and limits are in [provenance.md](../provenance.md#the-65-export-files) and [export-65-profile.md](export-65-profile.md). Rates use all 56,363 records as the denominator, and 237 of them have no post text. Command: `python3 analysis/travel_content_scan.py export65 /path/to/folder_with_the_65_files`.

```text
=== 65 export files (56,363 records) ===
Travel agencies/platforms:
    Airbnb                       76 (0.1348%)
    Expedia                      8 (0.0142%)
    MakeMyTrip                   5 (0.0089%)
    ^ WARNING: "MakeMyTrip" -- top repeated string = 2/5 (40.0%) of matches -- likely template inflation, not distinct signal. Corrected estimate: 4
    travel agency (generic)      5 (0.0089%)
    ^ WARNING: "travel agency (generic)" -- top repeated string = 2/5 (40.0%) of matches -- likely template inflation, not distinct signal. Corrected estimate: 4
    TripAdvisor                  4 (0.0071%)
    ^ WARNING: "TripAdvisor" -- top repeated string = 1/4 (25.0%) of matches -- likely template inflation, not distinct signal. Corrected estimate: 4
    Booking.com                  2 (0.0035%)
    ^ WARNING: "Booking.com" -- top repeated string = 1/2 (50.0%) of matches -- likely template inflation, not distinct signal. Corrected estimate: 2
    Kayak                        1 (0.0018%)
    ^ WARNING: "Kayak" -- top repeated string = 1/1 (100.0%) of matches -- likely template inflation, not distinct signal. Corrected estimate: 1
    Priceline                    1 (0.0018%)
    ^ WARNING: "Priceline" -- top repeated string = 1/1 (100.0%) of matches -- likely template inflation, not distinct signal. Corrected estimate: 1
Destinations:
    Dubai                        388 (0.6884%)
    London                       344 (0.6103%)
    France                       315 (0.5589%)
    Miami                        226 (0.4010%)
    Singapore                    209 (0.3708%)
    Paris                        172 (0.3052%)
    Japan                        156 (0.2768%)
    New York City                123 (0.2182%)
    Italy                        103 (0.1827%)
    Switzerland                  73 (0.1295%)
    Spain                        71 (0.1260%)
    Los Angeles                  62 (0.1100%)
    Bali                         54 (0.0958%)
    Amsterdam                    47 (0.0834%)
    Rome                         45 (0.0798%)
```

Airbnb appears in 76 of 56,363 records (0.1348%), against 0.12% in podawaa2024 and 0.30% in HyperClapper. The other agency and platform names have counts of 8 or fewer, and the scan's duplicate-template warnings fire on six of those lines, where one repeated text is a large share of a count of 1 to 5. Those counts are too small to read anything into. Among destinations, Dubai (388 records) and London (344) lead, then France (315), Miami (226) and Singapore (209).

The rates come from different fields and different kinds of record, so a gap between them describes the files and does not describe the tools. A match is a keyword in the text, not a finding about the post or its author.
