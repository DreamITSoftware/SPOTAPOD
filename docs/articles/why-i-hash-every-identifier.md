# Why I Hash Every Identifier Before It Touches My Screen

### The hashing happens in memory, in the first few lines of every script, before a single print statement runs

There's a difference between "we don't publish identifying information" and "our tools are structurally incapable of ever showing it to us." This project is built to the second, stricter standard.

## What the rule actually requires

Every script that loads raw engagement-pod data hashes each direct identifier, a LinkedIn profile URL, an author name, a public identifier field, with SHA-256, in memory, as one of the first operations performed on each record. This happens before any filtering, before any print statement, before any intermediate file gets written. The unhashed identifier exists in memory for the shortest possible span and is never deliberately persisted anywhere.

The practical effect: even during development, even in a debugging session, even in an error message that might get pasted somewhere, the actual name or profile URL of a real person essentially never appears on a screen, because the code that would show it was never written that way to begin with.

## Why "before it touches my screen" is the right bar, not "before publication"

A weaker version of this rule would say "we redact identifiers before publishing." That version still requires someone, at some point, to have looked at unhashed data while working, which is exactly the moment a mistake happens. A debug print left in, a stray file saved, a terminal session screen-shared. Removing the human's ability to ever see the raw identifier in the first place removes that entire failure mode, rather than relying on remembering to redact it later.

## What this doesn't solve, and is not claimed to solve

Hashing a public identifier is not the same as making someone unidentifiable in every possible sense. A sufficiently motivated party with access to the same raw data and the same hash function could recompute the same hashes and re-associate them. This project's own protection here comes from a second, separate commitment: never publishing any per-entity output at all, hashed or otherwise, and never keeping a raw copy anywhere the hash could be reversed against. The hash is one layer, not the whole wall.

## What this is, and isn't

**A verifiable code-level practice, not a promise**: every script in this project's `/analysis` directory can be read directly to confirm the hash-before-use pattern.

**Explicitly not cryptographic anonymity**: hashing a known identifier space doesn't create anonymity on its own. The no-lookup, no-raw-data policies described elsewhere in this series are what actually carry that weight.

Full privacy documentation: **github.com/DreamITSoftware/SPOTAPOD**.

---

*Self-published. Not peer-reviewed.*
