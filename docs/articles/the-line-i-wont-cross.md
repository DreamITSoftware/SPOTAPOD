# The Line I Won't Cross: No Raw Data, Ever

### Three datasets, hundreds of thousands of records, and not one raw row has ever been committed to this project's public repository

Of every rule governing this project, this is the one with zero exceptions, zero staging environments, and zero "just this once for a compelling example."

## What the rule says

No raw data file, not a row, not a redacted excerpt, not a "representative sample," is ever committed to the public repository, published in an article, or included in any output this project produces. Everything that leaves this project is an aggregate: a count, a rate, a percentage, a distribution. The raw files themselves live only in a private, access-controlled location and are never checked into version control.

## Why "just one illustrative example" is exactly the failure mode this prevents

The most tempting exception to a rule like this is always the smallest one: "surely one anonymized example post, to make the finding concrete, can't hurt." That instinct is exactly backwards. A single real post, even with the author's name removed, can often be re-identified through the content itself. A distinctive phrase, a specific combination of details, a timestamp that narrows down who could have posted it. Aggregate statistics don't carry that risk because there's no specific record left to trace back to anyone. The moment an exception gets made for "just one example," the entire privacy architecture depends on that one example being untraceable, which is a much weaker guarantee than never publishing an example at all.

## What this costs the writing

It's a real constraint on how vivid these articles can be. "One post received 88,028 likes on zero recorded views" is a finding this project can and does report, because it's a count derived from the data, not the post itself. "Here's a screenshot of that exact post" is something this project will never publish, no matter how illustrative it would be, because a screenshot is the raw record, and the raw record is the thing that must never leave.

## Why draw an absolute line instead of a case-by-case judgment call

A case-by-case standard eventually erodes. Each individual exception looks reasonable in isolation, and the cumulative effect is a policy that's absolute in name only. An actual absolute rule, with no carve-out mechanism at all, is the only version of this commitment that survives contact with a compelling-enough example.

## What this is, and isn't

**Verifiable directly**: search this project's public repository for any raw record, in any commit, in its history. There isn't one.

Full data-handling policy: **github.com/DreamITSoftware/SPOTAPOD**.

---

*Self-published. Not peer-reviewed.*
