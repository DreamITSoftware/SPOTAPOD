# Why I Hash Every Identifier Before It Touches My Screen

### The hashing happens in memory, in the first few lines of every script, before a single print statement runs

Publishing no identifying information is one standard. Having tools that are structurally unable to show it to us is a stricter one. This project is built to the stricter standard.

## What the rule requires

Every script that loads raw engagement-pod data hashes each direct identifier, a LinkedIn profile URL, an author name, a public identifier field, with SHA-256, in memory, as one of the first operations performed on each record. This happens before any filtering, before any print statement, before any intermediate file gets written. The unhashed identifier exists in memory for the shortest possible span and is never deliberately persisted anywhere.

The practical effect: during development, in a debugging session, or in an error message that might get pasted somewhere, the name or profile URL of a real person almost never appears on a screen, because the code that would show it was never written.

## Why the bar is "before it touches my screen" and not "before publication"

A weaker version of this rule would say "we redact identifiers before publishing." That version still requires someone to have looked at unhashed data while working, which is when mistakes happen: a debug print left in, a stray file saved, a terminal session screen-shared. If the raw identifier is never visible, that failure mode does not exist, and nobody has to remember to redact later.

## What this does not solve

Hashing a public identifier does not make someone unidentifiable. A motivated party with access to the same raw data and the same hash function could recompute the same hashes and re-associate them. This project's further protection is a separate commitment: never publishing any per-entity output, hashed or otherwise, and never keeping a raw copy anywhere the hash could be reversed against. The hash is one layer of protection.

## What this is, and isn't

**A verifiable code-level practice**: every script in this project's `/analysis` directory can be read directly to confirm the hash-before-use pattern.

**Not cryptographic anonymity**: hashing a known identifier space does not create anonymity on its own. The no-lookup, no-raw-data policies described elsewhere in this series provide that protection.

Full privacy documentation: **github.com/DreamITSoftware/SPOTAPOD**.

---

*Self-published. Not peer-reviewed.*
