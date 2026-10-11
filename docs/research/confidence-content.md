# Confidence content

`analysis/confidence_content_scan.py` counts mentions of
confidence-related terms (confidence, confident, self-confidence,
confidence building/booster) across post content in all three datasets.
It follows the same discipline as every other scan in this repo:
aggregate counts only, no record, author, or matched text ever printed
beyond the duplicate-template check described below.

## LinkBoost-2025's low-distinct-ratio note, checked

The low-distinct-ratio note fires on LinkBoost-2025 (249 distinct
strings for 4,069 matches), but the duplicate-template warning does not:
no single string dominates (the top is 129 of 4,069, about 3%). Checked
manually, the top repeated strings are distinct, on-theme
leadership/career posts (a leadership-metaphor post about a sheepdog, an
AI-personal-branding post, ChatGPT job-search prompts, career-AI-skills
advice).

This is genuine signal, not an artifact.

## Results (VERIFIED: reproducible via the script)

| Term | podawaa2024 | HyperClapper | LinkBoost-2025 |
|---|---|---|---|
| Confidence | 1,584 | 1,576 | 3,391 |
| Confident | 812 | 693 | 981 |
| Self-confidence | 100 | 6 | 93 |
| Confidence building/booster | 3 | 1 | - |
| **Any mention** | **2,269 (1.063%)** | **2,137 (4.329%)** | **4,069 (5.219%)** |

## Reading these numbers

This is one of the larger content categories found across the
niche-topic scans in this repo, well above most categories checked (law,
nonprofit, cybersecurity, travel) and in the same range as
[toplist-content.md](toplist-content.md). LinkBoost-2025 has the highest
rate at over 5%, meaning roughly 1 in 19 posts touches on confidence in
some form.

HyperClapper's jump from podawaa2024's rate (1.06%) to 4.33% is more
than 4x, even though podawaa2024 has a larger raw count of "confidence"
mentions.

It fits the broader pattern across this repo: HyperClapper and
LinkBoost-2025 both skew toward motivational, leadership and soft-skills
content compared to podawaa2024's more general mix.

"Self-confidence" is almost absent in HyperClapper (6 mentions, versus
100 in podawaa2024 and 93 in LinkBoost-2025) even though HyperClapper
has a comparable rate of the general term "confidence". That suggests
HyperClapper's confidence content leans toward business and professional
framing rather than the more personal "self-confidence" framing found in
the other two datasets.

## Caveats

Same as every keyword scan in this repo: a match means the term appears
in the text, not that the post contains substantive or accurate advice
about building confidence.
