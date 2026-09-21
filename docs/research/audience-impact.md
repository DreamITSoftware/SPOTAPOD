# Audience impact (INFERENCE — mechanism, not measured outcome)

This page reasons about who could be affected *downstream* — the people
who saw this content, not the accounts that posted it — when a post gets
artificially inflated engagement. It's built on the category counts in
[other-regulatory-signals.md](other-regulatory-signals.md), but it's a
different kind of claim: not "how much of this content matches a
category," but "what could plausibly happen to a reader who trusted it
because the engagement looked real." This repo has no data on actual
readers, so everything below is a reasoned mechanism, tagged INFERENCE,
not a measured outcome.

## The mechanism

Likes, comments, and view counts function as *social proof* — signals
people use, consciously or not, to decide how much to trust unfamiliar
content and its author. This is precisely the harm 16 CFR § 465.8 is
built around: the rule doesn't ban fake engagement because the number
itself matters, it bans it because inflated numbers "materially
misrepresent influence or importance" to the people relying on them (see
[regulatory-context.md](../regulatory-context.md)). A post with 200 fake
likes reads, to a viewer, as 200 real people vouching for it. That
inflated credibility transfers to whatever claim the post is making —
which is where downstream audience risk comes from, independent of
whether the poster's account itself is ever identified or sanctioned.

## Plausible impact by content category

| Category | % of records (see other-regulatory-signals.md) | Plausible audience impact if trust was inflated by fake engagement |
|---|---|---|
| `health_medical_claims` | 0.66–3.38% across the three files | A reader could delay seeking real medical care, try an unproven remedy, or make a diet/health change based on a claim that looked more credible than it was. This is the exact harm the FTC's Health Products Compliance Guidance is meant to prevent — inflated social proof compounds it by making the claim look independently corroborated by hundreds of "real" reactions. |
| `financial_investment_claims` | 0.07–0.26% | A reader could make an investment or spending decision — e.g. treating "passive income" or "guaranteed return" language as credible because a post looked popular — based on claims that would ordinarily need to pass advertising or securities-disclosure standards. |
| `professional_licensing_language` | 0.01–0.09% | A reader could act on stated medical/legal/tax advice believing the poster's credentials and the content's popularity both vouch for its reliability, without any actual verification of licensure or accuracy. |
| `endorsement_disclosure_gap` | 1.27–3.02% | A reader could mistake sponsored or affiliated content for an independent, organic opinion — the exact scenario 16 CFR Part 255 (Endorsement Guides) requires disclosure to prevent — with fake engagement adding a second, unrelated layer of false credibility on top of the undisclosed relationship. |

For a fifth category — algorithm/creator-strategy advice content — see the
dedicated case study: [algorithm-strategy-advice.md](algorithm-strategy-advice.md).
It's split out on its own page because it's a distinct genre worth
reasoning about in more depth, not because it's about any specific real
report; that page names no real report, author, or company.

## Why this stays at INFERENCE, and what would move it further

- **No audience data exists in any of these three files.** There's no
  record of who saw a given post, whether they acted on it, or what
  happened if they did. Everything above is "what this mechanism would
  predict," grounded in why these rules exist in the first place — not a
  measurement of actual harm to actual people.
- **The category counts themselves are blunt keyword signals** (see
  [other-regulatory-signals.md](other-regulatory-signals.md)) — the same
  caveats apply here: base rates aren't established, matches can be
  figurative or negated, and a match says nothing about a specific post's
  actual truth or falsity.
- **This says nothing about any specific account, post, or reader.** It's
  a category-level statement about what kind of harm becomes more likely
  when content in that category gets inflated engagement — not a claim
  that any particular post caused any particular outcome for any
  particular person.
- Moving any of this from INFERENCE toward something stronger would
  require actual audience research (survey data, behavioral studies, or
  documented complaints/harm reports tied to specific claims) — which is
  outside what a dataset of posts and engagement counts can provide.
