# "Top list" / listicle content

`analysis/toplist_content_scan.py` counts mentions of "top list" and
listicle-style content patterns ("Top 10," "5 ways to," "best of,"
"must-read," "ultimate guide") across post content in all three
datasets. Same discipline as every other scan in this repo: aggregate
counts only, and no record, author, or matched text is printed beyond the
duplicate-template check described below.

## Results (VERIFIED - reproducible via the script)

| Dataset | Any mention | % of dataset |
|---|---|---|
| podawaa2024 | 3,700 | 1.733% |
| HyperClapper | 1,784 | 3.614% |
| LinkBoost-2025 | 3,056 | 3.920% |

**Term breakdown:**

| Term | podawaa2024 | HyperClapper | LinkBoost-2025 |
|---|---|---|---|
| Top N (Top 5/10/etc.) | 1,681 | 1,258 | 1,287 |
| N ways/tips/reasons/steps (listicle) | 1,560 | 472 | 1,627 |
| Best of | 387 | 35 | 57 |
| Must-read | 157 | 18 | 104 |
| Ultimate guide | 49 | 3 | 10 |
| Must-know | 20 | 15 | 10 |

Neither the duplicate-template safeguard nor the low-distinct-ratio
check flagged a genuine correction here. LinkBoost-2025's lower
distinct-string count (182 for 3,056 matches) is consistent with that
dataset's known structure - only 469 distinct target posts total,
documented in [baseline-profile.md](baseline-profile.md). It is not a new
artifact requiring correction, as in earlier scans in this repo.

## Reading these numbers

This is one of the larger content categories across the
niche-topic scans in this repo, well above
[pharma-content.md](pharma-content.md) (0.3-0.6%),
[cybersecurity-anomaly.md](cybersecurity-anomaly.md),
[law-content.md](law-content.md), [nonprofit-content.md](nonprofit-content.md),
[travel-content.md](travel-content.md),
[political-content.md](political-content.md),
[national-security-content.md](national-security-content.md), and
[immunotherapy-content.md](immunotherapy-content.md), all of which sit
under 1%.

HyperClapper and LinkBoost-2025 both show higher rates than
podawaa2024 (3.6% and 3.9% vs. 1.7%). This matches the
pattern across multiple scans in this repo: these two datasets skew more toward templated
content. The recurring "resume rewrite" template and
free-certification templates documented in
[decision-points.md](decision-points.md) are examples of the same
pattern.

The two datasets also differ in listicle style:
LinkBoost-2025 leans more on numbered-listicle phrasing ("N ways/tips/
reasons," 1,627, its single largest term) while HyperClapper leans much
more toward "Top N" specifically (1,258 vs. 472 for the
numbered-listicle phrasing). The difference is in style as well as volume.

## Caveats

Same as every keyword scan in this repo: a match means the phrase
pattern appears in the text, not that the post is a genuine, well-
researched listicle, or that its claims are accurate.
