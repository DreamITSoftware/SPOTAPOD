# Homelessness-related content

`analysis/homelessness_content_scan.py` counts mentions of
homelessness-related terms across post content in all three datasets,
at two levels of breadth. Same discipline as every other scan in this
repo: aggregate counts only, no record, author, or matched text ever
printed beyond the duplicate-template check described below.

## Method

**NARROW**: homeless/homelessness, unhoused, homeless shelter, housing
insecurity, homeless services/agency.

**BROAD**: narrow, plus affordable housing and the bare word "shelter."
Bare "shelter" is deliberately kept out of the narrow tally - checking
actual matches in podawaa2024 showed it catches real noise, including a
disaster-protection product post ("a spherical shelter designed to
protect against natural disasters such as tsunamis, tornadoes") and
unrelated leadership content. The narrow tally is the more trustworthy
number for most purposes; the broad tally is an upper bound.

## A correction that turned out not to be noise

Same duplicate-template safeguard as
[nonprofit-content.md](nonprofit-content.md),
[travel-content.md](travel-content.md), and
[national-security-content.md](national-security-content.md): the
script flags any field where a single repeated string accounts for 20%
or more of matches. It fired on LinkBoost-2025 (79 of 213 narrow
matches share one string) - but unlike every prior instance of this
warning in this repo, checking the actual text showed the repeated post
is genuinely on-topic: a personal "overcame homelessness" success story
("2018: Homeless and living in a shelter in New York -> 2025: Built a
$50 Million business"), boosted 79 times by LinkBoost's pod-action
structure. It's real homelessness-related content, just heavily
duplicated - not a false positive the way the FBI/Wolf-of-Wall-Street
post or the AI-travel-tool ad were in earlier scans. This is why the
script's warning message for this scan says to check the text rather
than assuming inflation automatically means noise.

## Results (VERIFIED - reproducible via the script)

| Dataset | Narrow | % | Broad | % |
|---|---|---|---|---|
| podawaa2024 | 65 | 0.030% | 143 | 0.067% |
| HyperClapper | 9 | 0.018% | 34 | 0.069% |
| LinkBoost-2025 | 213 raw / ~135 corrected | 0.273% raw | 213 | 0.273% |

## What stands out

LinkBoost-2025 contains genuine homelessness-sector advocacy content
beyond the personal-narrative template - posts along the lines of "The
Power of Collaboration in Ending Homelessness," "The most effective way
to end homelessness? Stop it before it starts," and a piece on digital
exclusion of vulnerable populations from online-only essential services
(benefits applications, housing applications). This reads as genuine
nonprofit/social-sector professional content, a meaningfully different
character than most of the other small content categories checked in
this repo (compare [national-security-content.md](national-security-content.md),
where matches were mostly scattered and tangential).

## Caveats

Same as every keyword scan in this repo: a match means the term
appears in the text, not that the account is affiliated with a real
homeless-services agency, or that the content is accurate or
representative of the sector. The broad tally in particular should be
read as an upper bound inflated by unrelated uses of "shelter," not a
trustworthy standalone figure.
