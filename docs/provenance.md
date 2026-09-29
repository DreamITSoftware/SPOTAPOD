# Provenance

## Source sites

| Dataset | Reported source | Reported collection method |
|---|---|---|
| `podawaa2024.json` | podawaa.com; also archived on Harvard Dataverse (see [Citations](#citations) below) | Navigated to the site directly and captured the resulting data to a local server |
| `HyperClaper.json` | hyperclapper.com | Navigated to the site directly and captured the resulting data to a local server |
| `LinkBoost-2025.json` | Not yet stated | Not yet stated |

The first two entries are **STATED**, asserted by whoever collected the
data, not independently verified by this repo. `LinkBoost-2025.json`'s
source and collection method haven't been provided yet; this repo isn't
filling in "linkboost.com" as a guess just because it matches the filename.
See [limitations.md](limitations.md) for why guessing at provenance isn't
how this repo operates. If you can confirm where and how this file was
obtained, that goes here as STATED, same as the other two.

This repo has no way to confirm, from the files themselves, which site a
given record actually came from, what specific requests were made to
obtain it, or when collection occurred. Treat any reported source as the
reported origin, not a confirmed chain of custody.

## Citations

**`podawaa2024.json`**, **CORROBORATED**. This file's sha256
(`2d64e4b274c1b238399a6b1d578b951cac9d5035a980ab70d4c3d66efffb4214`, see
[checksums/CHECKSUMS.txt](../checksums/CHECKSUMS.txt)) matches the checksum
published for `podawaa2024_fixed.json` by the SPOTAPOD companion repo, which
identifies that file as archived on Harvard Dataverse:

> Hall, Daniel. "LinkedIn posts using fake socials." Harvard Dataverse, 2026.
> `doi:10.7910/DVN/WD9AUR`
> https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/WD9AUR

A matching sha256 across independently-obtained copies is about as strong a
corroboration as a file hash can give. It means this repo's copy and the
Dataverse-archived copy are byte-for-byte identical.

**`HyperClaper.json`**, **no citation added**. Nothing about this file
supports linking it to the Dataverse record above: its structure, schema,
and reported source (hyperclapper.com, see the table above) are entirely
different from `podawaa2024.json`, and no checksum or other evidence ties it
to that DOI or to Harvard Dataverse at all. If you have a citation for where
this specific file is archived, that's worth adding. But citing it to the
same Dataverse DOI as `podawaa2024.json` would be inaccurate, since nothing
here supports that connection.

## Terms of service

This repo does not assert, one way or the other, that collecting this data
complied with either site's terms of service. That's a legal conclusion
this repo isn't positioned to make: it would require the actual ToS text in
effect on the site at the time of collection, the specific technical method
used to capture the data (which this repo does not have independent
knowledge of beyond the STATED description above), and a legal analysis of
whether that method fell inside or outside what those terms permitted.
Terms of service for platforms like these commonly restrict automated
access or bulk data capture, so this is not a settled question, and no
document in this repo should be read as having settled it.

If you're relying on any of these datasets for anything beyond your own
private analysis, reviewing the actual current terms of service for the
sites they reportedly came from, and how they read at the time of
collection, if that's knowable, is worth doing before you do, ideally with
an actual lawyer rather than this repo's say-so.

## A documented mechanism for how view counts leak

Every dataset in this repo treats view and impression counts as
"indicators of social media influence" under 16 CFR § 465.1(j) (see
[regulatory-context.md](regulatory-context.md)). One open question those
counts raise on their own: `Views` should be visible to a post's author,
but nothing about LinkedIn's stated design lets a stranger read another
account's view count off a search page or a creator's activity feed.
`HyperClapper.json`'s `impression_count` field being populated for only
2.0% of records is consistent with that: a metric that normally sits
behind the wall of "your own analytics, nobody else's."

A vulnerability disclosure supplied to this project shows that wall did
not always hold. Dated open 2023-07-19 and closed 2023-08-10, the
disclosure documents two related flaws, internally named `UpdatesV2` and
`ProfileUpdatesV2`, in LinkedIn's search-page and creator-activity-page
rendering. Per the disclosure, navigating to either page caused reaction
counts, share counts, and view counts, for any public post on the page,
to be sent to the browser as clear-text JSON, readable by any logged-in
user regardless of whose post it was, and scrapable in a loop at scale.
The disclosure's own [CVSS v3.1](https://www.first.org/cvss/v3-1/specification-document)
scoring puts the flaw at 7.0 to 9.6, network-exploitable, requiring no more
than ordinary low-level user privileges, and rates confidentiality impact
as High. The upper end of that range is reproducible from a supplied
vector,
[`AV:N/AC:L/PR:L/UI:N/S:C/C:H/I:N/A:H/E:H/RL:X/RC:X/CR:X/IR:X/AR:X/MAV:N/MAC:L/MPR:N/MUI:N/MS:C/MC:X/MI:X/MA:X`](https://nvd.nist.gov/vuln-metrics/cvss/v3-calculator?vector=AV:N%2FAC:L%2FPR:L%2FUI:N%2FS:C%2FC:H%2FI:N%2FA:H%2FE:H%2FRL:X%2FRC:X%2FCR:X%2FIR:X%2FAR:X%2FMAV:N%2FMAC:L%2FMPR:N%2FMUI:N%2FMS:C%2FMC:X%2FMI:X%2FMA:X&version=3.1),
which this repo independently recomputed using the official CVSS v3.1
formula (verified against known reference vectors first) and confirms
produces a **Base Score of 9.6**, matching the top of the stated 7.0-9.6
range. The disclosure does not specify which of the two named flaws
(`UpdatesV2` or `ProfileUpdatesV2`) this particular vector belongs to, so
this repo isn't assigning it to one over the other. It states plainly
that this exposed data "views should not be public," raises the exact
same profiling and re-identification concerns [privacy.md](privacy.md)
raises about this repo's own hashed identifiers, and names GDPR
specifically as a regime the exposure could implicate.

This project treats the disclosure's technical detail, the exact
mechanism, the CVSS number, the GDPR analysis, as **STATED**: reported by
the person who found it, not independently re-tested by this repo. One
part of it is **CORROBORATED** by an independent party. The same
document includes LinkedIn's own written reply, from an Executive
Escalations Case Manager, thanking the reporter for "recently
uncover[ing] a vulnerability within our content view reporting" and,
in a follow-up message roughly sixteen hours later, confirming LinkedIn
had "thoroughly investigated and resolved the issue." That is LinkedIn
itself, not this repo and not the person who found the bug, stating in
writing that a real vulnerability in its view-count reporting existed
and got fixed. The disclosure marks the `UpdatesV2` flaw specifically as
fixed; it marks `ProfileUpdatesV2` as unreported to LinkedIn, validated
only by the named LinkedIn creators listed in the disclosure itself, and
this repo has no independent confirmation that LinkedIn ever patched
that second one.

What this does and does not establish for the three datasets in this
repo: it establishes that a real, LinkedIn-acknowledged flaw once let
any user pull another account's view count in clear text, for at least a
three-week window inside the multi-year span these files cover. It does
not establish that Podawaa, HyperClapper, or LinkBoost specifically used
this flaw, a different flaw, or ordinary authenticated access to obtain
whatever view or impression data they show. No tool named in this
project's own provenance notes is named in the disclosure, and the
disclosure does not claim otherwise. The value of citing it here is
narrower and more solid than "proof engagement pods scraped LinkedIn":
it is proof that the specific number this whole project treats as an
indicator of influence has, at least once, leaked to anyone who knew
where to scroll, confirmed by the platform that built the wall around it
in the first place.

## A second, separate disclosure: a pod tool's own vulnerability (LEMPOD)

The disclosure above concerns a flaw in LinkedIn's own systems. A
second, unrelated disclosure, a LinkedIn post by this project's author,
describes a vulnerability in a pod tool itself, LEMPOD, not in
LinkedIn's platform and not in any of the three tools this repo actually
profiles (Podawaa, HyperClapper, LinkBoost). It is included here for
context on the broader pattern, a pod ecosystem with its own security
problems, not as evidence about any dataset in this repo.

Per that post, discovered 2024-03-26: navigating to a pod on the LEMPOD
platform let an attacker read the pod's websocket traffic, which
included other pod members' private information and their LinkedIn
`li_at` session cookie, sent to the client in clear-text JSON. The
`li_at` cookie is what LinkedIn uses to keep a browser logged in, so
per the post, anyone who captured it could log into that member's
LinkedIn account directly, without their password. The post also
describes bypassing LEMPOD's own interaction-tracking protocol, the
possibility of scraping this at scale across multiple accounts
(potentially a denial-of-service risk against LEMPOD and LinkedIn
alike). It names GDPR as implicated for the same reasons as the other
disclosure: mass profiling of the resulting data would be exactly the
kind of processing GDPR restricts.

Per the reporter, this finding carries the same
[CVSS v3.1](https://www.first.org/cvss/v3-1/specification-document) vector
and score as the upper end of the UpdatesV2/ProfileUpdatesV2 range above:
[`AV:N/AC:L/PR:L/UI:N/S:C/C:H/I:N/A:H/E:H/RL:X/RC:X/CR:X/IR:X/AR:X/MAV:N/MAC:L/MPR:N/MUI:N/MS:C/MC:X/MI:X/MA:X`](https://nvd.nist.gov/vuln-metrics/cvss/v3-calculator?vector=AV:N%2FAC:L%2FPR:L%2FUI:N%2FS:C%2FC:H%2FI:N%2FA:H%2FE:H%2FRL:X%2FRC:X%2FCR:X%2FIR:X%2FAR:X%2FMAV:N%2FMAC:L%2FMPR:N%2FMUI:N%2FMS:C%2FMC:X%2FMI:X%2FMA:X&version=3.1),
independently recomputed against the official CVSS v3.1 formula (verified
against known reference vectors first) at a **Base Score of 9.6**. This
repo previously recorded this finding's score as 8.8; the reporter has
since confirmed it should be 9.6, the same figure and vector as the
view-count disclosure, and this page is corrected accordingly. That two
unrelated findings, in different systems, discovered nine months apart,
share the identical vector is the reporter's account and is recorded here
as **STATED**, not independently verified by this repo beyond confirming
the arithmetic the vector itself implies.

The exact technical mechanism (the websocket message contents, the
specific API calls used to reproduce it, the video walkthrough referenced
in the exchange) is **STATED**: supplied by the reporter (this project's
author), not independently re-tested by this repo.

That said, this disclosure now carries independent corroboration beyond
the original post, from LinkedIn's own written case correspondence
(LinkedIn Case #240327-019836, March 27 to April 8, 2024, supplied to this
project directly). On March 27, 2024, LinkedIn's Executive Case Manager
wrote that the report had been "escalated... to our security and
engineering teams for further investigation." On April 8, 2024, the same
case manager confirmed in writing: "our Engineering and Trust teams were
able to replicate the issue you had reported, and actions were put in
place to mitigate the potential risk you had identified."

That confirmation is narrower than it might first look, and this repo is
precise about the boundary. LinkedIn's message does not say which party,
LinkedIn or LEMPOD, implemented whatever fix followed, and it does not
repeat back the specific `li_at` mechanism, the CVSS score, or any other
technical detail from the original report. Separately, the reporter's own
message from a few days earlier states he closed his ticket because "it
seems LEMPOD fixed the vulnerability," which is his own inference, not
something LinkedIn's reply itself confirms. What is **CORROBORATED**, by
LinkedIn's own words, is narrower and still meaningful: LinkedIn's
security and engineering teams reviewed the reported issue, were able to
replicate it, and took some mitigating action in response. The precise
technical mechanism and the CVSS 9.6 scoring remain STATED, reported by
the finder and not independently verified line-by-line by this repo or
confirmed in that specific form by LinkedIn.

This is still a different evidentiary picture than the `UpdatesV2`
disclosure above, which carries a direct written confirmation of the
specific mechanism reported. Here, LinkedIn confirmed the issue was real
and acted on, not the specific technical details of how it worked. It
should be read at that intermediate weight, not the same as UpdatesV2 and
not as thin as an uncorroborated post either.

One commenter on the original post raised a fair counter-read worth
noting rather than omitting: that a pod-tool vulnerability like this could
equally support an operator's claim that suspicious activity on their
account came from being hacked rather than from running a pod, an
alternative explanation this repo has no way to adjudicate from the post
or the case correspondence alone.

The same case correspondence includes one more fact worth recording
separately from the vulnerability itself. In responding to this report,
LinkedIn's Executive Case Manager wrote that "the use of add-ons,
extensions or tooling that scrape, modify the appearance of, or automate
activity on LinkedIn's website is prohibited under LinkedIn's User
Agreement." That is **CORROBORATED**, LinkedIn's own written statement of
its User Agreement's scope, and it concerns LinkedIn's own User
Agreement governing account holders' conduct on LinkedIn. It is a
different question from whether obtaining `podawaa2024.json`,
`HyperClapper.json`, or `LinkBoost-2025.json` from their respective
source sites complied with those sites' own terms of service, addressed
separately above. This statement doesn't resolve that separate question;
it only confirms that LinkedIn's own User Agreement, as LinkedIn describes
it, reaches tools of this general category.

What this does and does not establish: it does not concern, and this
repo does not use it as evidence about, `podawaa2024.json`,
`HyperClapper.json`, or `LinkBoost-2025.json`. Its relevance here is
narrower: another documented instance of the same underlying pattern,
a tool built around LinkedIn engagement handling sensitive account data
insecurely, cited for that pattern and nothing more specific.

A separate question this disclosure raises is what, if any, breach
notification duty applies when something like this is discovered, and to
whom it would run. See
[regulatory-context.md](regulatory-context.md#breach-notification-law-a-different-question-than-16-cfr--4658)
for that analysis. Short version: any such duty would run to LEMPOD, the
platform where the leak occurred, not to LinkedIn, absent separate facts
this repo does not have. This repo also has no information, in either
direction, about whether LEMPOD notified affected users.

## How this fits the rest of the repo

Consistent with [regulatory-context.md](regulatory-context.md) (this repo
makes no legal determination about 16 CFR § 465.8 violations) and
[limitations.md](limitations.md) (provenance of the underlying pod-tooling
claim is STATED, not VERIFIED), the collection-method claims on this page
get the same treatment: recorded as reported, not certified as accurate or
lawful.
