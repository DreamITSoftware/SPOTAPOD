# HyperClapper: external product context

Unlike every other page in `docs/research/`, this page draws no statistics
from any of the three source files. It compiles publicly available,
independently sourced information about the product that produced
`HyperClaper.json`, to give the dataset's own numbers (see
[baseline-profile.md](baseline-profile.md) and
[posting-velocity.md](posting-velocity.md)) external context. Every claim
below is tagged with this repo's evidence tier (see
[limitations.md](../limitations.md)); nothing here is VERIFIED against the
dataset itself, and none of it changes any figure reported elsewhere in this
repo.

## What the product says about itself (STATED)

HyperClapper markets itself as a LinkedIn engagement-automation product,
available as a Chrome extension and (per more recent listings) a cloud-based
platform, that automates likes and AI-drafted comments on members' posts
through "engagement pods" or "channels," concentrating activity in the
first hour after a post goes live to influence LinkedIn's distribution
algorithm. Its own marketing describes a member base of "5,000+ creators"
and cites Lempod and Linkboost — the latter almost certainly the same
product family as this repo's own `LinkBoost-2025.json` — as prior,
now-defunct alternatives it positions itself as replacing. Published
pricing tiers (STATED, self-reported, not independently confirmed) range
from a free "Starter" tier up to $499/month for an "Enterprise" tier.

## Independent extension-usage signal (UNCORROBORATED, single source)

One third-party Chrome-extension analytics tracker reported active-user
counts in the high-400s to low-500s in mid-2026, with a **declining**
30-day trend (roughly -9%) at the time this page was compiled. This is a
single, unverified, third-party tracker — not a HyperClapper-published
figure and not something this repo can independently confirm — but it is
worth noting as a contrast: it puts the *browser-extension* install base at
roughly one order of magnitude below the "5,000+ creators" marketing claim.

**This repo draws no conclusion from that gap.** The marketing claim may
refer to the cloud-platform user base rather than Chrome Web Store installs
specifically, and this repo has no way to reconcile the two from public
information alone.

## How this squares with the dataset's own numbers (cross-reference, no new stat)

[baseline-profile.md](baseline-profile.md) already reports 702 distinct
hashed authors across all of `HyperClaper.json`, and
[posting-velocity.md](posting-velocity.md) shows the top accounts sustaining
multi-year posting streaks. Both figures were computed independently of
this page and are unchanged by anything here. Readers looking for a "how
big is this really" figure should treat the account count in
baseline-profile.md as the dataset's own answer, and the product-context
figures on this page as separate, external, unverified context — not a
correction to it and not additional evidence about it.

## What this page does not do

Consistent with [CONTRIBUTING.md](../../CONTRIBUTING.md): this page makes
no claim about whether HyperClapper's operation complies or fails to comply
with LinkedIn's terms of service, or with [16 CFR § 465.8](../regulatory-context.md).
It does not assert that the extension-usage tracker's figures are accurate,
only that they exist and diverge from the product's own marketing claim.
It does not name, link, or otherwise identify any individual user of the
product — see [privacy.md](../privacy.md).

## Sources

- Chrome Web Store listings for the HyperClapper extension (product
  description, feature list, "5,000+ creators" claim)
- G2 marketplace listing (feature summary, pricing tiers, "curated network
  of 5,000+ professionals" and "critical first hour" positioning)
- A third-party Chrome-extension analytics tracker (independent user-count
  and growth-rate estimate, single source, unverified)

Specific URLs are omitted from this page by the same discipline applied
everywhere else in this repo to third-party links that could go stale or
be mistaken for an endorsement; the underlying pages were live and
consistent with the summary above as of the time this page was written.
