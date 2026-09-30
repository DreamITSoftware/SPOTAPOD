# The Nonprofit Post That Wasn't

### A "1.38% nonprofit-content rate" turned out to be one headline, copy-pasted 658 times

A first manual pass at nonprofit-related language (charity, NGO, philanthropy, 501(c)(3)) in one dataset's headline field found a 1.38% match rate. That was the highest of any field checked, and it looked like a genuinely notable signal.

It wasn't. Checking the underlying text directly showed 658 of the 681 matching records shared the exact same headline. That one dataset's structure logs a fresh row every time a reciprocal-engagement action happens, capturing that account's headline snapshot each time. So one person's nonprofit-mentioning headline got counted 658 separate times, once per engagement event, not because 658 different people mentioned nonprofit work.

Corrected for that, the real rate is **0.049%**, not the highest of any field checked, but the lowest.

## Building the fix in permanently, and what it caught next

Rather than patch this one instance by hand, the underlying script was rebuilt to report, for every field it checks, both the raw record count and the number of distinct underlying text values behind it, with an automatic warning whenever a single repeated string accounts for 20% or more of the matches. Running that hardened version surfaced two more cases of the exact same distortion, this time in a different dataset entirely.

| Field | Raw rate | Distinct strings | Dominant string | Corrected rate |
|---|---|---|---|---|
| podawaa2024, Content | 0.308% | 616 of 657 | none flagged | 0.308% (no correction needed) |
| HyperClapper, post_title | 0.288% | 141 of 142 | none flagged | 0.288% (no correction needed) |
| HyperClapper, headline | 1.379% | 5 of 681 | 658 records (96.6%) | **0.049%** |
| LinkBoost-2025, Title | 0.530% | 21 of 413 | 99 records (24.0%) | **0.404%** |
| LinkBoost-2025, Occupation | 0.154% | 3 of 120 | 67 records (55.8%) | **0.069%** |

## Why this is the most important nonprofit finding in this project

Not because nonprofit content matters more than any other category, but because the mistake this correction fixes, counting the same repeated headline hundreds of times as if it were hundreds of independent mentions, is exactly the kind of error a less careful research project would have published as a real finding.

## What this is, and isn't

**VERIFIED**, reproducible via the published scan: every raw and corrected rate above.

Full methodology: **github.com/DreamITSoftware/SPOTAPOD**.

---

*Self-published. Not peer-reviewed. Independently reproducible from the source files.*
