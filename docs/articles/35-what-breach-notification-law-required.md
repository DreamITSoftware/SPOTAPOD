# What Breach Notification Law Would Have Required of LEMPOD

### A leaked session credential raises a completely different legal question than fake engagement does, and it points at a different company

Most of this project's legal research is about fake engagement metrics. A separate, documented vulnerability, a session-credential leak inside LEMPOD, a third-party LinkedIn pod tool, later acknowledged and mitigated by LinkedIn, raises a different question entirely. What duty applies when a company discovers user credentials leaked, and does or doesn't tell affected users?

## Whose duty is it, first

The vulnerability, per the disclosure, sat inside LEMPOD's own platform. LinkedIn did not build or operate the leak. Any notification duty arising from it would run to LEMPOD first, not to LinkedIn, unless separate facts showed LinkedIn had actual knowledge of the exposure and some independent basis for a duty of its own. No such facts are established here, in either direction, including whether LEMPOD ever notified its own users.

## The three frameworks that would matter, if a duty were triggered

**State data breach notification statutes** exist in some form in all 50 states, most defining "personal information" by an enumerated list: Social Security numbers, driver's license numbers, username and password combinations. A session cookie isn't explicitly named on most states' lists, which makes whether it counts as reportable "personal information" a genuinely open legal question. New York's SHIELD Act and a handful of others use broader definitions that could plausibly reach a session credential. Many older statutes likely wouldn't.

**GDPR Articles 33 and 34** would require notifying a supervisory authority within 72 hours and, for high-risk breaches, the affected individuals directly, but only if an entity qualifies as a data controller for EU residents' data, a fact not established here.

**FTC Act § 5** has, in some cases, treated a company's failure to disclose a known security incident as itself an unfair practice, separate from the underlying vulnerability.

## What naming these frameworks does not do

Naming the laws that would apply if a duty were triggered is not the same as concluding a duty was triggered, or that anyone failed to meet one. This project doesn't know whether LEMPOD or LinkedIn had actual knowledge sufficient to trigger any of these obligations, how many users or which jurisdictions were affected, or whether notice was already given through a channel outside this project's visibility.

## What this is, and isn't

**STATED**: the vulnerability's existence and LinkedIn's acknowledgment and mitigation, per case correspondence.

**Not established**: whether any notification duty was actually triggered, or whether it was met.

Full analysis: **github.com/DreamITSoftware/SPOTAPOD**.

---

*Self-published. Not peer-reviewed. This is not legal advice.*
