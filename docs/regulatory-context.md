# Regulatory context: which laws actually reach this conduct

Three datasets, 340,829 combined records, and every one of them tied by its
depositor to engagement-pod tooling: software or services built to make a
LinkedIn post look more liked, more viewed, and more commented on than it
organically was. That description matches the fact pattern several federal
and state laws were written for. It does not automatically mean any of them
apply to any specific record in these files. This page checks each law
against what the aggregate data actually shows, element by element, and is
explicit about where the fit breaks down as much as where it holds.

Every comparison below stays at the tier discipline used throughout this
repo. A law's elements are either **STATED** (asserted by the datasets'
depositors, not independently confirmed), **CORROBORATED** (an aggregate
statistic computed directly from a checksummed file), or **INFERENCE** (a
reasoned reading of what a pattern is consistent with). None of it is
**VERIFIED** as to any individual record's legal status, because that would
require facts (intent, actual falsity of one metric, a specific consumer's
reliance) that do not exist as fields in a JSON file and cannot be
manufactured by a Python script. See [limitations.md](limitations.md) for
why that line doesn't move no matter how suggestive an aggregate number
looks.

## 16 CFR § 465.8: the rule written for exactly this conduct

**16 CFR § 465.8, "Misuse of fake indicators of social media influence,"**
is part of the FTC's Trade Regulation Rule on the Use of Consumer Reviews
and Testimonials (16 CFR Part 465), effective October 21, 2024.

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
media influence. The rule text names followers, friends, connections,
subscribers, views, plays, likes, saves, shares, reposts, and comments
explicitly. Every metric field in all three datasets in this repo (`Likes`,
`Views`, `like_count`, `impression_count`, `comment_count`, `followers`,
`SuccessfullLikes`, `SuccessfullComments`) falls within that definition.

### The two elements the rule actually requires

16 CFR § 465.8 only reaches conduct that satisfies **both**:

1. **Scienter**: the seller/distributor/buyer "knew or should have known"
   the indicator was fake, and
2. **Materiality for a commercial purpose**: the fake indicator can be or
   is used to materially misrepresent influence or importance *for a
   commercial purpose*.

The FTC has stated it is not seeking to impose liability for unknowing or
unintentional distribution. A business that unknowingly hires an influencer
who turns out to have fake followers is not itself liable under this
section. See the [FTC's final rule announcement](https://www.ftc.gov/news-events/news/press-releases/2024/08/federal-trade-commission-announces-final-rule-banning-fake-reviews-testimonials)
and its [Consumer Reviews and Testimonials Rule Q&A](https://www.ftc.gov/business-guidance/resources/consumer-reviews-testimonials-rule-questions-answers).

### What the aggregate data can and can't speak to

| Element | What the data shows | Tier | What's still missing |
|---|---|---|---|
| A metric exists that the rule covers | `Likes`, `Views`, `like_count`, `followers`, `SuccessfullLikes`, etc. are present and populated across all three files | CORROBORATED | Nothing; this element is a schema fact, not a judgment call |
| Coordinated, reciprocal exchange (the mechanism the rule targets) | HyperClapper: 68.6% of records carry a paired `like=true`/`comment=true` flag the depositor describes as the tool executing both actions together. LinkBoost-2025: every one of 77,969 records is, by the file's own structure, a logged "successful" like/comment action against a target post, averaging 171.2 likes and 47.5 comments per action-record | STATED (mechanism) / CORROBORATED (frequency) | Whether any specific flagged action was fake *and* known to be fake by a specific seller or buyer |
| Materiality for a commercial purpose | 213,491 podawaa2024 records skew toward business/professional content categories (see [topic-taxonomy.md](research/topic-taxonomy.md)); LinkBoost-2025's `Occupation` field is populated for 96.1% of records, mostly professional headlines | STATED / INFERENCE | Whether inflated engagement on any one post was actually used to misrepresent influence *to* a specific buyer, employer, or reader, and whether that use was material to a decision they made |
| Scienter | Not a field in any file | Not addressed | This is the element the rule leans on hardest, and it is exactly the element no dataset of engagement records can supply on its own |

Two of four elements have real data behind them. The other two, the ones
that actually decide liability, don't exist in any form a script can check.
That gap is not a technicality this repo is working around. It's the reason
[limitations.md](limitations.md) and [privacy.md](privacy.md) draw the
line where they do.

## FTC Act § 5: the broader net that doesn't need scienter

15 U.S.C. § 45 bars "unfair or deceptive acts or practices in or affecting
commerce," and it splits into two independent tests. An act is **deceptive**
if (1) a representation, omission, or practice misleads or is likely to
mislead, (2) a reasonable consumer's interpretation of it is reasonable
under the circumstances, and (3) the misleading element is material. An act
is **unfair** if it (1) causes or is likely to cause substantial injury to
consumers, (2) that injury isn't reasonably avoidable, and (3) it isn't
outweighed by countervailing benefits to consumers or competition. Source:
[Federal Reserve's Section 5 examination guidance](https://www.federalreserve.gov/boarddocs/supmanual/cch/200806/ftca.pdf).

The unfairness prong is the one worth sitting with, because it does not
require scienter at all. A practice can be unfair under § 5 with no showing
that anyone "knew or should have known" anything. That makes it a wider net
than 16 CFR § 465.8, which is itself a Trade Regulation Rule issued *under*
§ 5's authority. In principle, a coordinated engagement-inflation scheme
could be reachable as unfair (substantial injury to the people who trusted
the inflated numbers, not reasonably avoidable since a reader has no way to
tell a pod-driven like from an organic one, no countervailing benefit to
weigh it against) without ever reaching the harder scienter question 465.8
demands. That is an INFERENCE about legal theory, not a claim that any FTC
action exists or is likely against any party named or unnamed in these
files. No such action is documented anywhere in this repo's provenance
notes.

## The Computer Fraud and Abuse Act: the law that looks like it should fit, and mostly doesn't

18 U.S.C. § 1030 criminalizes accessing a computer "without authorization"
or in a way that "exceeds authorized access." Before 2021, several courts
read that second phrase broadly enough to cover violating a platform's
terms of service. That changed with *Van Buren v. United States*, 593 U.S.
374 (2021), where the Supreme Court adopted a "gates-up-or-down" test:
liability attaches only when someone accesses a file, folder, or database
that is *technically* off-limits to them, not when they have technical
access but violate a policy about what they're allowed to do with it.
Source: [Van Buren opinion](https://www.supremecourt.gov/opinions/20pdf/19-783_k53l.pdf);
[analysis of the ruling's scope](https://cdp.cooley.com/us-supreme-court-narrows-scope-of-computer-fraud-and-abuse-act-in-van-buren/).

*hiQ Labs, Inc. v. LinkedIn Corp.*, on remand to the Ninth Circuit after
*Van Buren*, is the closest analog: a case about automated tools interacting
with LinkedIn data at scale, and whether doing so against LinkedIn's wishes
violates the CFAA. The unresolved question there is whether a cease-and-
desist letter or technical anti-scraping measure creates a "gate," not
whether a mere terms-of-service violation does; *Van Buren* forecloses the
latter theory.

This matters for reading these three files honestly. All three tools
(Podawaa, HyperClapper, LinkBoost) are described by their depositors as
operating through the account holder's own authenticated session, not by
breaking into someone else's account or bypassing a technical barrier. Under
*Van Buren*'s gates-up-or-down test, a user directing their own authorized,
authenticated session to do something LinkedIn's terms of service prohibit
is very likely outside CFAA's reach, however clearly it violates that
platform's rules. This is the one law on this page where the honest
reading, after checking the actual elements against the actual mechanism
these files describe, is that it probably does not apply. That is worth
stating plainly instead of quietly leaving CFAA off the list and hoping
nobody asks.

## The Lanham Act § 43(a): the theory an actual competitor has already used

15 U.S.C. § 1125(a) creates a private right of action for false advertising
and unfair competition. A plaintiff must show (1) a false statement of fact
about goods, services, or commercial activity, (2) actual or likely
deception of a substantial segment of the audience, (3) materiality to a
purchasing decision, (4) dissemination in commerce, and (5) an injury to
the plaintiff's own commercial interest, proximately caused by the false
statement. Since *Lexmark International, Inc. v. Static Control Components,
Inc.*, 572 U.S. 118 (2014), standing turns on whether the plaintiff's
injury falls within the statute's zone of interests and was proximately
caused by the misrepresentation, not on whether the plaintiff is a direct
competitor. Consumers cannot sue under this section; only someone with an
injured commercial interest can. Source: [practical guidance on § 43(a) claims](https://www.bfkn.com/assets/htmldocuments/Lanham%20Act%20Section%2043a%20Claims.pdf).

This is not a hypothetical fit. **LinkedIn Corp. v. TopSocial24 et al.**
(Case No. 5:23-cv-00110, N.D. Cal.) resulted in a $43,086 judgment in
October 2023 against an engagement-pod-style service, using theories
including breach of LinkedIn's user agreement and unfair-competition claims
in the same family as § 43(a). That is a real, citable outcome against a
real defendant, and it is the strongest evidence in this section that a
plaintiff with standing (the platform itself, most plausibly) can and does
win against this category of tooling. It says nothing about whether
Podawaa, HyperClapper, or LinkBoost specifically have faced or would face
the same outcome; no litigation naming any of the three tools behind these
datasets was found during this repo's research (see [provenance.md](provenance.md)
for what was and wasn't independently confirmed).

## State law: New York GBL § 349 and California's borrowing statute

**New York General Business Law § 349** bars "deceptive acts or practices
in the conduct of any business," and requires (1) consumer-oriented
conduct with broad impact on the public, (2) a materially misleading act
judged by whether it's likely to mislead a reasonable consumer acting
reasonably, and (3) actual injury caused by the deception. Unlike 16 CFR
§ 465.8, it does not require scienter, and it carries a private right of
action with a $50 statutory minimum per violation, added to the statute in
1980. Source: [GBL § 349 elements summary](https://openclassactions.com/glossary/ny-general-business-law-349-350.php);
[statute text via Justia](https://law.justia.com/codes/new-york/gbs/article-22-a/349/).

The injury element is the one worth being precise about. The people most
directly deceived by an inflated like count are not the pod-service's own
customers (who know exactly what they're buying), but the third-party
readers who encounter a post with 400 likes and take that as a signal the
content is worth their trust. [audience-impact.md](research/audience-impact.md)
documents that mechanism as an INFERENCE, not a measured outcome, precisely
because no dataset in this repo can show who actually read a given post or
what they did as a result. Without a specific misled reader who can show
actual injury, § 349's third element has no factual home here.

**California Business & Professions Code § 17200** (the Unfair Competition
Law) defines unfair competition as "any unlawful, unfair or fraudulent
business act or practice." Its "unlawful" prong is a borrowing statute: any
other legal violation, a 16 CFR § 465.8 violation, an FTC Act § 5
violation, a GBL § 349 violation, becomes independently actionable under
§ 17200 once established, with its own private right of action and
remedies. Source: [UCL overview](https://www.shouselaw.com/ca/personal-injury/unfair-competition/).
That makes § 17200 structurally dependent on one of the other laws on this
page actually being established first. It adds no new element of its own
to check against the data; it just widens who can sue once someone else's
violation is proven.

## What this repo will not do with any of this

Cross-referencing a law's elements against an aggregate statistic is not
the same thing as applying that law to a record, an author, or a dataset,
and this repo does not do the latter. Nothing above should be read as
alleging that a specific engagement-pod service, its operators, or any
account represented in these files violated 16 CFR § 465.8, the FTC Act,
the CFAA, the Lanham Act, GBL § 349, California's UCL, or any other law.
The elements that would actually establish a violation, intent, a specific
misrepresentation, a specific deceived party, an actual injury, are not
fields in a JSON file and are not something a checksum-verified script can
manufacture. That determination requires a lawyer looking at specific
facts a spreadsheet cannot provide. See [limitations.md](limitations.md)
for the full reasoning.

For an aggregate (not per-record) look at whether post/comment content
contains terms associated with a few *other* regulated categories: health
claims, financial claims, licensing language, endorsement disclosure, see
[other-regulatory-signals.md](research/other-regulatory-signals.md). Same rule
applies there: signal counts, never individual findings.
