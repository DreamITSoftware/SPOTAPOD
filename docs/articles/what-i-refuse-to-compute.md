# What I Refuse to Compute

### No script in this project has ever printed, logged, or written a direct identifier, and no feature will ever let you look up a person

Most research decisions are about what to measure. This one is about what never to build, however easy it would be or however interesting the result might look.

## The rule

Every script that touches raw LinkedIn engagement-pod data in this project hashes direct identifiers, names, profile URLs, author IDs, once, in memory, before anything else happens to the record. The hash exists only long enough to group records by author for an aggregate count. It is never printed to a terminal, never written to a log file, never saved to disk, and never appears in any output this project produces.

There is also no feature, planned or built, that lets anyone look up a specific person, post, or account in this data. There is no search box, no API endpoint, and no "look up this profile" utility. This is a permanent architectural choice, not a missing feature to be added later.

## Why this goes further than "anonymize the output"

Many data projects anonymize what they publish while keeping an internal, identifiable copy "for the researchers." This project does not. The hash-immediately, never-log rule applies to every script, every time, including exploratory one-off analysis that will never be published. No identifiable version exists anywhere. Keeping one would create the re-identification risk this project exists to avoid.

## What this costs

This has a real cost. A per-author lookup would make several of this project's findings easier to explain and more compelling to read. "Here's exactly which account posted the 88,028-likes-zero-views post" is a stronger sentence than "one anonymized post in the dataset." That sentence will not be written here, because it depends on exposing an individual.

## Why the line is drawn here

Aggregate statistics about engagement manipulation serve a public-interest purpose, and understanding how these systems work does not require knowing whose account did what. A per-entity lookup tool serves a different purpose: identifying individuals. The two do not need to go together, and keeping them separate is the privacy commitment.

## What this is, and isn't

**A hard architectural constraint**: verifiable by reading every script in this project's `/analysis` directory. None of them retain or output a direct identifier.

Full privacy documentation: **github.com/DreamITSoftware/SPOTAPOD**.

---

*Self-published. Not peer-reviewed.*
