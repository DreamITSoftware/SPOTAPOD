# Other regulatory signals (aggregate, keyword-based)

This page covers `analysis/regulatory_category_scan.py`, which looks beyond
[16 CFR § 465.8](../regulatory-context.md) at whether post/comment/occupation
text across the three datasets contains terms associated with a handful of
*other* regulated categories. It's included because engagement-pod content
can plausibly overlap with other rules — but the method here is
deliberately blunt, and the results should be read that way.

## Method

For each record, the relevant text fields (post content, comment text,
stated occupation/headline — whichever exist in that file) are checked
against four keyword/phrase pattern sets:

| Category | Example terms | Law it could relate to, in the abstract |
|---|---|---|
| `health_medical_claims` | "cure", "detox", "clinically proven", "guaranteed weight loss" | FTC Act § 5 (15 U.S.C. § 45) prohibition on deceptive health claims; FTC Health Products Compliance Guidance |
| `financial_investment_claims` | "guaranteed return", "passive income", "risk-free investment" | SEC/state securities law on investment adviser registration and misleading investment claims; FTC Act § 5 |
| `professional_licensing_language` | "I am a doctor/attorney/CPA", "legal advice", "medical advice" | State unauthorized-practice-of-law/medicine/accounting statutes (vary by state; not federal) |
| `endorsement_disclosure_gap` | "partnered with", "sponsored", "affiliate link" without a visible disclosure | FTC Endorsement Guides, 16 CFR Part 255 (material-connection disclosure requirements) |

A record counts as a "hit" if any pattern in a category matches, case-
insensitively, anywhere in its available text. That's it — no context, no
sentiment, no check for an actual disclosure elsewhere in the post, no
distinction between literal and figurative use ("this offer won't last,
act now!" marketing copy and an actual unregistered-security pitch match
the same pattern).

## Results (VERIFIED — reproducible via the script, subject to the
INFERENCE caveat below)

| Dataset | Records scanned | Any category | health_medical | financial | licensing | endorsement |
|---|---|---|---|---|---|---|
| podawaa2024 | 213,491 | 1.99% | 0.66% | 0.07% | 0.01% | 1.27% |
| HyperClapper | 49,369 | 5.80% | 2.79% | 0.14% | 0.01% | 3.02% |
| LinkBoost-2025 | 77,969 | 5.69% | 3.38% | 0.26% | 0.09% | 2.07% |

Full script output: `analysis/regulatory_category_scan.py` run directly
against each checksummed file reproduces every number above.

## Why this is INFERENCE, not a finding

- **A keyword match is not a legal element.** None of the laws named above
  turn on whether a specific word appears — they turn on falsity,
  materiality, licensing status, actual disclosure practices, jurisdiction,
  and intent. This script checks none of that. A post saying "this
  supplement won't cure anything, don't believe the hype" would match
  `health_medical_claims` and means the opposite of what the category name
  suggests.
- **No record, author, or occupation is identified anywhere in this
  script's output**, on purpose — see [privacy.md](../privacy.md) and
  [limitations.md](../limitations.md) for why per-record identification isn't
  something this repo does, for this category scan any more than for the
  § 465.8 framing everywhere else.
- **Base rates matter.** A few percent of any large corpus of marketing-
  adjacent social media content will contain phrases like "guaranteed" or
  "sponsored" regardless of whether it came from a pod dataset — these
  numbers are not, by themselves, evidence that pod-tool usage correlates
  with other legal exposure. No comparison corpus was scanned to establish
  a baseline.
- **This is not legal research.** The "law it could relate to" column is a
  plain-language pointer for orientation, not a citation of the actual
  elements of each statute/rule (unlike [regulatory-context.md](../regulatory-context.md),
  which quotes 16 CFR § 465.8 in full). If you want an actual assessment of
  whether specific conduct violates any of these, that requires a lawyer
  reviewing specific facts — not a keyword count.

## What this script will not do, and why

It will not report per-record results, list matched phrases, or let you
filter down to "which occupations tripped the financial-claims category."
That's the same line drawn everywhere else in this repo: aggregate signal
is shareable, individual-level accusation-building is not — regardless of
which law is invoked.

See [audience-impact.md](audience-impact.md) for a discussion of what
these categories could mean for the people who *saw* this content, framed
as an inferred mechanism rather than a measured outcome.
