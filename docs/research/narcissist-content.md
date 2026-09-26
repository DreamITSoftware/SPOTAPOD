# Narcissist content

`analysis/narcissist_content_scan.py` counts mentions of narcissist/
narcissistic/narcissism across post content in all three datasets. Same
discipline as every other scan in this repo: aggregate counts only, no
record, author, or matched text ever printed beyond the
duplicate-template check described below.

## The smallest content category in this project so far

Only 156 total records across all 340,829 combined records mention
narcissism in any form, before the LinkBoost-2025 correction below is
even applied. This is smaller than every other content category
documented in this repo, including
[immunotherapy-content.md](immunotherapy-content.md) (16 genuine
mentions total) and
[national-security-content.md](national-security-content.md).

## A duplicate string that turned out to be genuine content

The duplicate-template check fires on LinkBoost-2025 (52 of 116
matches share one string), but checking the underlying text directly
showed this is genuine content - a personal recovery/psychedelic-
journey narrative ("free from the NARCISSISTS spider web... significantly
helped me get clarity") - boosted by the platform's structure, not a
false positive. Corrected, LinkBoost-2025's real any-mention count is
65, not 116.

This is the same kind of outcome as
[homelessness-content.md](homelessness-content.md) and
[diabetes-content.md](diabetes-content.md), where a flagged duplicate
turned out to be real content rather than noise, and the opposite of
[immunotherapy-content.md](immunotherapy-content.md),
[university-content.md](university-content.md), and
[children-content.md](children-content.md), where flagged or dominant
patterns turned out to be outright false positives or language
collisions.

## Results (VERIFIED - reproducible via the script)

| Term | podawaa2024 | HyperClapper | LinkBoost-2025 |
|---|---|---|---|
| Narcissistic | 20 | 5 | 116 |
| Narcissist(s) | 9 | 4 | 52 |
| Narcissism | 5 | 2 | - |
| **Any mention (raw)** | **30 (0.0141%)** | **10 (0.0203%)** | **116 (0.1488%)** |
| **Any mention (corrected)** | 30 (no correction needed) | 10 (no correction needed) | **65 (0.083%)** |

## Reading these numbers

Even the corrected LinkBoost-2025 figure (65, 0.083%) is the smallest
"any mention" percentage documented anywhere in this repo. There is
essentially no meaningful narcissism-discourse content in these
datasets - the topic simply doesn't have a foothold in this
professional-networking content ecosystem, unlike the broader
kindness/honesty vocabulary documented in
[honesty-language-content.md](honesty-language-content.md).

## Caveats

Same as every keyword scan in this repo: a match means the term
appears in the text, not that the post contains a genuine clinical or
substantive discussion of narcissism, or that any named or unnamed
individual has been diagnosed with anything. No claim about any
person's mental health status is made or implied anywhere in this
repo.
