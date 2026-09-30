# What I Refuse to Compute

### No script in this project has ever printed, logged, or written a direct identifier, and no feature will ever let you look up a person

Some research decisions are about what to measure. This one is about what never to build, no matter how easy it would be or how interesting the result might look.

## The rule

Every script that touches raw LinkedIn engagement-pod data in this project hashes direct identifiers, names, profile URLs, author IDs, once, in memory, before anything else happens to the record. The hash exists only long enough to group records by author for an aggregate count. It is never printed to a terminal, never written to a log file, never saved to disk, and never appears in any output this project produces.

More importantly: there is no feature, planned or built, that lets anyone look up a specific person, post, or account in this data. Not a search box, not an API endpoint, not a "look up this profile" utility. This isn't a missing feature waiting to be added later. It's a permanent architectural choice.

## Why this is a harder line than "anonymize the output"

Plenty of data projects anonymize what they publish while keeping an internal, identifiable copy "for the researchers." That's not what happens here. The hash-immediately, never-log rule applies to every script, every time, including exploratory one-off analysis that will never be published. There's no internal identifiable version sitting anywhere, not because it would be hard to keep one, but because keeping one at all creates exactly the kind of re-identification risk this project exists to avoid causing.

## What this costs

It's a real cost, not a free virtue-signal. A per-author lookup would make several of this project's own findings easier to explain and more compelling to read. "Here's exactly which account posted the 88,028-likes-zero-views post" is a much punchier sentence than "one anonymized post in the dataset." That sentence will never get written here, on purpose, because the punch comes directly from the thing this project is committed to never doing: exposing an individual.

## Why draw the line here specifically

Aggregate statistics about engagement manipulation serve a public-interest purpose. Understanding how these systems work doesn't require knowing whose account did what. A per-entity lookup tool serves a completely different purpose: identifying individuals. Those two things don't need to travel together, and keeping them permanently separated is the actual privacy commitment, not a caveat at the bottom of a page.

## What this is, and isn't

**A hard architectural constraint, not a policy statement**: verifiable by reading every script in this project's `/analysis` directory. None of them retain or output a direct identifier.

Full privacy documentation: **github.com/DreamITSoftware/SPOTAPOD**.

---

*Self-published. Not peer-reviewed.*
