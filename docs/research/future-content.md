# "Future" content

`analysis/future_content_scan.py` counts mentions of "future"-related
terms (future(s), futuristic, future of work) across post content in
all three datasets. Same discipline as every other scan in this repo:
aggregate counts only, no record, author, or matched text ever printed
beyond the duplicate-template check described below.

## LinkBoost-2025's low-distinct-ratio note, checked

The low-distinct-ratio note fires on LinkBoost-2025 (403 distinct
strings for 6,929 matches), but the duplicate-template warning does
not - no single string dominates (the top is 104 of 6,929, about
1.5%). Checked manually: the top repeated strings span many distinct,
on-theme posts (AI-skills career advice, business-transformation
commentary, emotional-intelligence-in-children content, "future of
work" AI-course promotion). This is genuine signal, not an artifact.

## Results (VERIFIED - reproducible via the script)

| Term | podawaa2024 | HyperClapper | LinkBoost-2025 |
|---|---|---|---|
| Future(s) | 11,728 | 3,512 | 6,887 |
| Future of work | 323 | 110 | 289 |
| Futuristic | 107 | 65 | 42 |
| **Any mention** | **11,795 (5.525%)** | **3,558 (7.207%)** | **6,929 (8.887%)** |

## Reading these numbers

This is the largest niche-topic category found in this repo so far -
nearly 1 in 11 posts in LinkBoost-2025 mentions "future" in some form.
All three datasets show a clean, steady climb from podawaa2024 (5.5%)
through HyperClapper (7.2%) to LinkBoost-2025 (8.9%) - a consistent
gradient rather than one sharp outlier, which is itself notable given
how many other scans in this repo show LinkBoost-2025 as a sharp
outlier against the other two rather than the top of a smooth
progression.

"Future of work" tracks closely with the AI-productivity content
already documented elsewhere in this repo - the term appears at a
similar share of "future" mentions across all three datasets (roughly
2-4%), and the sample content confirms this: AI-skills career advice
and "AI is changing the future of work" framing dominate the genuinely
distinct LinkBoost-2025 posts checked above.

"Futuristic" is comparatively rare and declining as a share of the
category - the smallest of the three terms in every dataset, and drops
most sharply in LinkBoost-2025 (42, the smallest raw count despite that
dataset having the highest overall "future" rate). This suggests a
shift from describing things as "futuristic" (an adjective about
novelty) toward discussing "the future" directly (a noun, often paired
with AI/career anxiety), consistent with the AI-productivity content
genre already documented in [algorithm-strategy-advice.md](algorithm-strategy-advice.md)
and [decision-points.md](decision-points.md).

## Caveats

Same as every keyword scan in this repo: a match means the term
appears in the text, not that the post contains substantive
forward-looking analysis or accurate predictions.
