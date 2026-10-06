# Impact on unknowing participants

Every other document in this repo treats "the account" as a single
unit. That is adequate for aggregate statistics, but it ignores a
difference that matters: knowing and unknowing participation in
engagement-pod activity are different situations with different harms,
and this repo's data cannot distinguish between them. This document
traces what that difference means for the people who never knew, using
the actual findings in this repo.

## Why this data can't tell the two groups apart

A zero-view-with-likes anomaly, a reciprocal like-and-comment pairing,
or a sustained high posting rate looks identical whether it comes from
someone who knowingly bought a growth-hacking subscription or from
someone whose account was swept into reciprocal-engagement activity
without real understanding of what a tool's terms of service
authorized it to do. None of the datasets analyzed in this repo record
intent, consent, or awareness, only outcomes. See
[limitations.md](limitations.md) for the fuller version of this
constraint as it applies to every finding in this repo.

## How this plays out across the actual findings

Unknowing exposure is not one uniform harm. It differs depending on
which category of finding a given account or post falls into.

**Baseline engagement anomalies**
([baseline-profile.md](research/baseline-profile.md)). The core
signals (zero views with likes present, extreme like/view ratios,
reciprocal like+comment pairing) can't distinguish someone who
knowingly joined a pod from someone whose account was added to a
reciprocal-engagement pool by a tool they signed up for without reading
carefully. HyperClapper's 68.6% reciprocal-pairing rate includes both
populations, indistinguishably.

**Posting velocity**
([posting-velocity.md](research/posting-velocity.md)). The top-10
accounts sustaining 1.2-3.7 posts/day for up to 712 days are the
accounts most likely to belong to executives who pay a ghostwriter
or social media manager. The account holder may have little or no idea
what their profile's posting behavior looks like, because someone else
is operating it. This is a different kind of "unknowing" from the
reciprocal-engagement case: the holder is unaware of their own
account's behavior, not of manipulation.

**Repeated templates** ([decision-points.md](research/decision-points.md),
[social-proof-content.md](research/social-proof-content.md)). Two very
different populations sit inside numbers like the 533+ occurrences of
the "silence for 90 days... ran my resume through ChatGPT" template.
Some people chose to copy a viral format, which is knowing template use
and not fraud. Others may have had the same text posted by an
automated tool acting on their account, which they never wrote and may
never have seen. The finding can't tell these apart, and neither
population is accurately described as "engagement-farming."

**Real tribute and advocacy content**
([veteran-content.md](research/veteran-content.md),
[homelessness-content.md](research/homelessness-content.md)). This is
the sharpest version of the problem. The genuine content found
alongside a boosted political post (widows honoring husbands, a young
army doctor's death, someone's "overcame homelessness" story) comes
almost by definition from unknowing participants in whatever
pod-boosting elevated its reach. Someone writing a real tribute to a
family member has no reason to expect the post to become a data point
in fraud research because a platform-gaming tool amplified it. The
research-inclusion-without-consent harm described below is most acute
here: personal, often grief-related content sitting in a dataset built
to study something else.

**Political content**
([political-content.md](research/political-content.md)). This differs
from the tribute content above. A public political candidate's campaign
material is not a private individual's content, which is a materially
different privacy posture. That is part of why this repo treats
candidate identification differently: it never names the candidate, but
it does not treat the post itself as an unknowing-victim case the way
personal tribute content is treated.

**False-positive category placement**
([immunotherapy-content.md](research/immunotherapy-content.md),
[university-content.md](research/university-content.md)). A smaller
but real harm: someone's ordinary post about online shopping or
German workplace politics was briefly, wrongly counted as medical or
academic content before the error was caught and corrected. No
identity was exposed, but it shows that even category placement, not
just a fraud accusation, is something a real person has no visibility
into or control over while research is being built.

**Demographic and occupation data**
([demographics.md](research/demographics.md),
[simple-titles.md](research/simple-titles.md)). Almost every person
whose stated location or job title contributes to these aggregate
breakdowns has no idea their profile data is being counted for this
purpose. Separate from any question of fraud, this is the baseline
"unknowing subject of research" condition that applies to essentially
the entire underlying population, fraud participant or not.

## What is at stake across all of the above

**Self-deception about their own traction.**
[audience-impact.md](research/audience-impact.md) documents how
inflated engagement misleads *readers* into overweighting a claim's
credibility. The same mechanism works on the poster. Someone who
doesn't know their engagement is manufactured is reading a false signal
about their own market position, and may raise rates, change careers,
or double down on a content strategy based on numbers that don't
reflect real reach.

**Negligence-style legal exposure despite no intent.**
[regulatory-context.md](regulatory-context.md) explains that 16 CFR
465.8 requires the actor "knew or should have known" an indicator was
fake. That is a negligence standard, not a pure-intent one. Someone with
no actual knowledge could still face an argument that a reasonable
person would have noticed unusual metrics on their own account.

**Reputational exposure from a signal they can't explain.** If
engagement-pod research becomes more widely publicized and scrutinized,
an account with an anomalous pattern becomes something a colleague,
employer, or journalist could point to. "I genuinely don't know why my
metrics look like that" is a weak defense even when true.

**Research inclusion without notice or consent.** Real names, photos,
and profile links for people who most likely have no idea sit in the
datasets this repo analyzes. Only podawaa2024 is CORROBORATED against
an independently archived, public record; the other two rest on
STATED, unverified collection claims (see
[provenance.md](provenance.md)).

**Possible unauthorized use of the account itself.** Some
growth-hacking tools operate with a level of automation or access the
account holder may not have fully understood when granting it. For at
least some of the population in these datasets, "their content" may not
be something they fully controlled the posting of.

## Why this shapes the repo's design, not just its findings

This is the population this repo's privacy rules exist to protect most
directly. The people most exposed to real harm from this research are
the ones this repo is least able to distinguish from anyone else in the
data. For that reason, de-identification (see [privacy.md](privacy.md)),
the ban on any per-record lookup capability, and the refusal to name any
individual account are binding constraints throughout this project
rather than optional privacy practice.

None of this resolves the unfairness to someone who was caught up in
engagement manipulation without knowing it. It does keep this repo from
being the mechanism that turns a data anomaly into a real reputational
or legal consequence for someone who may have done nothing wrong.

## What this repo cannot and does not claim

This repo does not, and cannot, determine what share of any dataset's
population knew about the engagement patterns associated with their
account and what share did not. No figure in this repo should be read as
an estimate of "how many people were victims" versus "how many people
knowingly participated." Every method used here is blind to that
distinction, and treating an aggregate statistic as if it answered the
question would misrepresent what the data can support.
