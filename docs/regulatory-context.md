# Regulatory context: 16 CFR § 465.8

Both datasets in this repo are described by their depositors/collectors as
tied to engagement-pod tooling — coordinated exchanges of likes, comments,
views, and other engagement metrics. The relevant federal rule is
**16 CFR § 465.8, "Misuse of fake indicators of social media influence,"**
part of the FTC's Trade Regulation Rule on the Use of Consumer Reviews and
Testimonials (16 CFR Part 465), effective October 21, 2024.

## Full text of 16 CFR § 465.8

> It is an unfair or deceptive act or practice and a violation of this part
> for anyone to:
>
> (a) Sell or distribute fake indicators of social media influence that they
> knew or should have known to be fake and that can be used by individuals
> or businesses to materially misrepresent their influence or importance
> for a commercial purpose; or
>
> (b) Purchase or procure fake indicators of social media influence that
> they knew or should have known to be fake and that materially
> misrepresent their influence or importance for a commercial purpose.

Source: [eCFR, Title 16, Part 465, § 465.8](https://www.ecfr.gov/current/title-16/chapter-I/subchapter-D/part-465/section-465.8); also available via [Cornell LII](https://www.law.cornell.edu/cfr/text/16/465.8).

"Indicators of social media influence" is defined at **16 CFR § 465.1(j)** as
any metric the public uses to assess an individual's or entity's social
media influence — the rule text names followers, friends, connections,
subscribers, views, plays, likes, saves, shares, reposts, and comments
explicitly. Every metric field in both datasets in this repo (`Likes`,
`Views`, `like_count`, `impression_count`, `comment_count`, `followers`)
falls within that definition.

## The two elements the rule actually requires

16 CFR § 465.8 only reaches conduct that satisfies **both**:

1. **Scienter** — the seller/distributor/buyer "knew or should have known"
   the indicator was fake, and
2. **Materiality for a commercial purpose** — the fake indicator can be or
   is used to materially misrepresent influence or importance *for a
   commercial purpose*.

The FTC has stated it is not seeking to impose liability for unknowing or
unintentional distribution — e.g., a business that unknowingly hires an
influencer who turns out to have fake followers is not itself liable under
this section. See the [FTC's final rule announcement](https://www.ftc.gov/news-events/news/press-releases/2024/08/federal-trade-commission-announces-final-rule-banning-fake-reviews-testimonials)
and its [Consumer Reviews and Testimonials Rule Q&A](https://www.ftc.gov/business-guidance/resources/consumer-reviews-testimonials-rule-questions-answers).

## What this means for how this repo talks about the data

Neither dataset in this repo carries a per-record determination of scienter
or commercial-purpose materiality — those are legal conclusions, not fields
in a JSON file. That is exactly why every figure in this repo is scoped to
**aggregate, population-level statistics** (how many records show which
patterns) rather than **individual-level claims** (whether a specific,
named account violated 16 CFR § 465.8). See
[limitations.md](limitations.md) for the full reasoning and
[privacy.md](privacy.md) for how identifiers are handled.

Nothing in this repo should be read as a legal determination that any
specific account, post, or dataset violates 16 CFR § 465.8 or any other
law. That determination requires evidence (intent, commercial purpose,
actual falsity of a given metric) that is outside the scope of what these
files, or this repo's scripts, can establish.

For an aggregate (not per-record) look at whether post/comment content
contains terms associated with a few *other* regulated categories — health
claims, financial claims, licensing language, endorsement disclosure — see
[other-regulatory-signals.md](other-regulatory-signals.md). Same rule
applies there: signal counts, never individual findings.
