# Could the CFAA Apply Here?

### The federal hacking law that looks like the obvious fit, and, checked honestly, mostly isn't

If three tools are automating access to LinkedIn at scale, the Computer Fraud and Abuse Act sounds like the obvious hammer. Checked against what these tools are actually reported to do, it probably isn't. Saying so plainly is more useful than quietly leaving it off the list.

## What the CFAA actually requires now

18 U.S.C. § 1030 criminalizes accessing a computer "without authorization" or in a way that "exceeds authorized access." Before 2021, courts often read that second phrase broadly enough to cover violating a platform's terms of service. Use a website in a way it prohibits, and you'd "exceeded" your access even with a valid login.

*Van Buren v. United States* (2021) changed that. The Supreme Court adopted a "gates-up-or-down" test. Liability only attaches when someone accesses a specific file, folder, or database that is technically off-limits to them, not when they have technical access but break a policy about what they're allowed to do with it.

## Why that test matters for engagement pods specifically

All three tools behind this project's datasets are described by their depositors as operating through the account holder's own authenticated session, not by breaking into someone else's account or bypassing a technical barrier. Under *Van Buren*'s test, a user directing their own authorized, logged-in session to do something LinkedIn's terms of service prohibits is very likely outside the CFAA's reach, however clearly it violates that platform's rules.

*hiQ Labs, Inc. v. LinkedIn Corp.*, the closest real analog, left open whether a cease-and-desist letter or a technical anti-scraping measure creates a "gate." But *Van Buren* forecloses the simpler theory that a mere terms-of-service violation does.

## Why this is worth saying out loud

A project like this one could quietly skip laws that don't fit and only list the ones that make the argument look stronger. That's not the discipline here. The CFAA is the one law in this project's legal research where the honest reading, after checking the actual elements against the actual mechanism these tools describe, is that it probably doesn't apply. That's worth stating as clearly as any finding that does support the case.

## What this is, and isn't

**INFERENCE about legal theory**, not a claim that any specific tool has or hasn't faced CFAA liability. No litigation naming any of the three tools behind this project's datasets was found during its research.

Full legal analysis: **github.com/DreamITSoftware/SPOTAPOD**.

---

*Self-published. Not peer-reviewed. This is not legal advice.*
