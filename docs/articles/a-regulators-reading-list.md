# A Regulator's Reading List: Every Law This Project Actually Checked

### Ten articles, ten legal frameworks, no claim that any of them was violated

This is the index for the regulatory series. It lists every law, rule, and doctrine this project checked LinkedIn engagement-pod data against, what each one requires, and what this project did and did not establish about it.

## The federal frameworks

**16 CFR § 465.8** (FTC's fake indicators of social media influence rule) is the most directly applicable rule, because § 465.1(j) defines likes, views, comments, and followers as "indicators of social media influence." It requires a fake indicator, knowledge it's fake, and use for a commercial purpose to materially misrepresent influence. This project found the metric fields fit the definition. It did not establish knowledge or commercial-misrepresentation intent for any specific record.

**FTC Act § 5** (unfair or deceptive acts or practices) is broader and older than § 465.8. It requires a practice likely to mislead a reasonable consumer, material to a purchasing decision, causing or likely to cause substantial injury not outweighed by benefits. No specific transaction or misled consumer is identified anywhere in this project's data.

**Computer Fraud and Abuse Act** (18 U.S.C. § 1030) requires unauthorized access to a protected computer, examined here against *Van Buren v. United States*'s narrowed "exceeds authorized access" standard. Whether an engagement-pod tool that automates actions inside a legitimately logged-in account "exceeds authorized access" under *Van Buren* is an unresolved question this project can name but not answer.

**Lanham Act § 43(a)** (false advertising and unfair competition) requires a false or misleading statement of fact in commercial advertising that deceives, is material, and causes competitive injury, read against *Lexmark v. Static Control*'s standing test. No specific competitor or advertised claim is examined here.

**FTC Endorsement Guides** (16 CFR Part 255) require disclosure of material connections between endorsers and brands. This project's keyword-based "disclosure gap" check (1.27% to 3.02% across datasets) is a pattern-detection exercise and not a violation finding, for reasons covered in its own article.

## The state and international frameworks

**New York General Business Law § 349** is a deceptive-practices law requiring consumer-oriented conduct, a materially misleading act, and actual injury. It reaches a misled third-party reader, not just a pod service's own paying customer, which federal transaction-based frameworks do not naturally reach.

**California Business & Professions Code § 17200** (Unfair Competition Law) is a borrowing statute. It adds no substantive test of its own but makes another law's violation independently actionable, once that violation is established elsewhere.

**State data breach notification statutes** (all 50 states, in some form) and **GDPR Articles 33-34** were examined only in the context of a separately documented LEMPOD session-credential vulnerability, not in the context of the engagement metrics themselves. Whether a session credential counts as reportable "personal information" varies significantly by state and is an open question in several states.

## How to use this list

Every framework above names legal requirements that this project's authors read from the primary source, the statute or regulation's own text, and checked against what the datasets contain. None of that checking produces a violation finding. A violation finding requires facts (knowledge, intent, actual commercial harm, a specific injured party) that an aggregate, de-identified, VERIFIED-tier dataset cannot supply. Naming the applicable law is the whole claim. Anything beyond that belongs to a regulator with subpoena power.

## What this is, and isn't

**An index of laws, not a finding of violations**: every law named here is real and was read from its primary source. No claim is made anywhere in this project that any of them was violated.

Full text of every framework, with citations: **github.com/DreamITSoftware/SPOTAPOD**.

---

*Self-published. Not peer-reviewed. This is not legal advice.*
