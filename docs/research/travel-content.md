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
