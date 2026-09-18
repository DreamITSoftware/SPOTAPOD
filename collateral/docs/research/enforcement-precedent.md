# Enforcement precedent: fake social media engagement

This page catalogs actual enforcement actions and litigation involving
fake or inflated social media engagement, as a companion to
[regulatory-context.md](../regulatory-context.md) (which covers the rule
text) and [audience-impact.md](audience-impact.md) (which reasons about
downstream harm mechanisms). Everything below is **STATED** — drawn from
public case filings, agency press releases, and news coverage of them —
not independently verified by this repo beyond reading the cited source.
As with every other legal-adjacent page in this repo, nothing here is a
claim that any account, post, or dataset in this repo's own files
violates any law; see [limitations.md](../limitations.md).

Compiled from a web search conducted in September 2026. This is an active
enforcement area — the FTC rule this repo is oriented around is not yet
two years old — so treat this as a snapshot, not a complete or
permanently current record.

## Directly on-point: selling/buying fake indicators of influence

**FTC & New York Attorney General v. Devumi (2019)** — the clearest
precedent for this repo's subject matter. Devumi sold fake followers,
likes, and views across Twitter, YouTube, and LinkedIn — including,
per the FTC's complaint, **more than 800 orders of fake LinkedIn
followers**, sold to marketing/advertising/PR firms, software companies,
banking/investment/financial-services firms, and HR firms. The FTC's
complaint alleged this let buyers deceive potential clients, investors,
partners, and employees. The FTC fined owner German Calas $2.5 million
(suspended to $250,000 pending compliance with the settlement's
financial-disclosure terms); the New York Attorney General separately
settled for $50,000 and stated it was the first law-enforcement finding
that selling fake social media engagement, and using stolen identities to
do so, is illegal.
Source: [FTC press release](https://www.ftc.gov/news-events/news/press-releases/2019/10/devumi-owner-ceo-settle-ftc-charges-they-sold-fake-indicators-social-media-influence-cosmetics-firm).

**FTC v. Sunday Riley (2019)**, part of the same enforcement announcement
— a cosmetics company whose CEO allegedly directed employees to post fake
reviews of the company's products on a retail site. Not LinkedIn-related,
but decided alongside Devumi and often cited as a pair establishing the
FTC's fake-engagement/fake-review enforcement posture.
Source: same FTC press release as above.

**The FTC's Trade Regulation Rule on Consumer Reviews and Testimonials**
(16 CFR Part 465, effective October 21, 2024 — full text and the specific
provision, § 465.8, in [regulatory-context.md](../regulatory-context.md))
moved from rulemaking into active enforcement in late 2025: the FTC
issued formal warning letters to close to a dozen companies for alleged
fake-review and fake-engagement practices, with the rule authorizing
civil penalties of roughly $53,000 per violation. Warning letters are a
precursor step, not a lawsuit or settlement — this repo has not found a
completed enforcement action *under this specific rule* (as opposed to
the FTC Act generally, which is what Devumi was charged under) as of the
search date.
Sources: [Benesch Law client alert](https://www.beneschlaw.com/insight/five-stars-zero-tolerance-ftc-turns-up-enforcement-under-consumer-review-rule/), [Crowell & Moring client alert](https://www.crowell.com/en/insights/client-alerts/keeping-it-real-ftc-targets-fake-reviews-in-first-consumer-review-rule).

## Adjacent: real (not fake) followings used to commit fraud

**SEC & DOJ v. Constantinescu et al. ("Atlas Trading"/"Scalper" case,
2022)** — a different fact pattern worth distinguishing clearly: eight
"finfluencers" with genuinely large, real social media followings
(hundreds of thousands of Twitter/Discord followers) were charged in a
roughly $100 million pump-and-dump scheme. They allegedly bought stocks,
promoted them to their real followers without disclosing their own
position, then sold once the price rose on the resulting demand. The SEC
and DOJ both brought charges (securities fraud and conspiracy); a
criminal appeal was pending in the Fifth Circuit as of the source
reporting. This case is about the credibility that comes from a genuine
following being used deceptively — not about a faked follower count — but
it establishes the same underlying legal principle this repo's
[audience-impact.md](audience-impact.md) reasons about: social-media-
derived credibility that a reader relies on to make a financial decision
carries real legal exposure when it's used to mislead.
Sources: [SEC press release](https://www.sec.gov/newsroom/press-releases/2022-221), [DOJ press release](https://www.justice.gov/archives/opa/pr/eight-men-indicted-114-million-securities-fraud-scheme-orchestrated-through-social-media).

## What this search did not find

No lawsuit, FTC action, or public enforcement proceeding was found
against any of the three tools tied to this repo's own datasets —
Podawaa, HyperClapper/LinkBoost, or their predecessor Lempod — as of the
search date. Public reporting on these tools describes **platform-side**
enforcement instead: LinkedIn removed Lempod from the Chrome Web Store
for Terms of Service violations, and multiple sources describe LinkedIn's
algorithm detecting and "sandboxing" (reach-limiting) accounts it
identifies as pod participants, rather than any legal action against the
tool vendors themselves or their users.

This is an absence-of-evidence finding, not evidence of absence — a
narrower or more targeted search, non-English-language sources, or
private settlements that were never made public could all change this
picture. This repo makes no claim that no such action exists, only that
this search didn't surface one.

## Caveats

- This page reports what public sources say happened in named,
  already-public cases. It does not evaluate whether any of these cases
  were correctly decided, and it takes no position on the merits of any
  pending matter (e.g., the Constantinescu appeal).
- None of this is legal advice, and none of it should be read as
  predicting how 16 CFR § 465.8 specifically would be applied to any
  account or company, including any appearing in this repo's own
  datasets. See [regulatory-context.md](../regulatory-context.md) for why
  that determination requires evidence (intent, commercial purpose,
  actual falsity of a given metric) outside what this repo's files or
  scripts can establish.
