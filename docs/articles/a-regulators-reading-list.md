# A Regulator's Reading List: Every Law This Project Actually Checked

### Ten articles, ten legal frameworks, zero claims that any of them was violated

This is the index piece for the regulatory series, a single place listing every law, rule, and doctrine this project checked LinkedIn engagement-pod data against, what each one requires, and what this project did and didn't establish about it.

## The federal frameworks

**16 CFR § 465.8** (FTC's fake indicators of social media influence rule) is the most directly applicable rule, because § 465.1(j) explicitly defines likes, views, comments, and followers as "indicators of social media influence." It requires a fake indicator, knowledge it's fake, and use for a commercial purpose to materially misrepresent influence. This project found the metric fields fit the definition. It did not establish knowledge or commercial-misrepresentation intent for any specific record.

**FTC Act § 5** (unfair or deceptive acts or practices) is broader and older than § 465.8, requiring a practice likely to mislead a reasonable consumer, material to a purchasing decision, causing or likely to cause substantial injury not outweighed by benefits. No specific transaction or misled consumer is identified anywhere in this project's data.

**Computer Fraud and Abuse Act** (18 U.S.C. § 1030) requires unauthorized access to a protected computer, examined here against *Van Buren v. United States*'s narrowed "exceeds authorized access" standard. Whether an engagement-pod tool that automates actions inside a legitimately logged-in account "exceeds authorized access" under *Van Buren* is a genuinely unresolved question this project can name but not answer.

**Lanham Act § 43(a)** (false advertising and unfair competition) requires a false or misleading statement of fact in commercial advertising that deceives, is material, and causes competitive injury, read against *Lexmark v. Static Control*'s standing test. No specific competitor or advertised claim is examined here.

**FTC Endorsement Guides** (16 CFR Part 255) require disclosure of material connections between endorsers and brands. This project's keyword-based "disclosure gap" check (1.27% to 3.02% across datasets) is a pattern-detection exercise, not a violation finding, for reasons covered in its own article.

## The state and international frameworks

**New York General Business Law § 349** is a deceptive-practices law requiring consumer-oriented conduct, a materially misleading act, and actual injury, notable because it reaches a misled third-party reader, not just a pod service's own paying customer, in a way federal transaction-based frameworks don't naturally reach.

**California Business & Professions Code § 17200** (Unfair Competition Law) is a borrowing statute. It doesn't add its own substantive test but makes any other law's violation independently actionable, once that violation is separately established elsewhere.

**State data breach notification statutes** (all 50 states, in some form) and **GDPR Articles 33-34** were examined only in the context of a separately documented LEMPOD session-credential vulnerability, not in the context of the engagement metrics themselves. Whether a session credential counts as reportable "personal information" varies significantly by state and is, in several states, a genuinely open question.

## What using this list responsibly looks like

Every framework above names real legal requirements this project's authors read directly from the primary source, the statute or regulation's own text, and checked structurally against what the datasets actually contain. None of that checking produces a violation finding, because a violation finding requires facts (knowledge, intent, actual commercial harm, a specific injured party) that an aggregate, de-identified, VERIFIED-tier dataset is structurally incapable of supplying. Naming the applicable law is the whole and complete claim. Anything beyond that belongs to an actual regulator with subpoena power, not to a public dataset analysis.

## What this is, and isn't

**A map, not a verdict**: every law named here is real and was read directly from its primary source. No claim is made, anywhere in this project, that any of them was actually violated.

Full text of every framework, with citations: **github.com/DreamITSoftware/SPOTAPOD**.

---

*Self-published. Not peer-reviewed. This is not legal advice.*
