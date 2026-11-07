# Nobody Talks About Animals on LinkedIn

### Zero. That's how many genuine posts about cats show up in one entire LinkedIn dataset, once you filter out the noise

"Cat" was the hardest word this project has tried to count. Sampling matches for bare "cat"/"cats" across three LinkedIn datasets turned up eight unrelated meanings:

- **CAT**, India's major MBA entrance exam (Common Admission Test)
- The **.cat** domain extension for Catalonia
- **"Cat Nat"**, a French insurance term for natural catastrophes
- **"cat"** as shorthand for the Catalan language in multilingual bios
- **CAT**, the NYSE ticker symbol for Caterpillar Inc.
- **Cat 1 through Cat 5**, the hurricane intensity scale
- **"Fat cats"**, the idiom for wealthy elites
- Jaguar's **"leaping cat"** logo, in a brand-redesign post

## The gap between loose and strict counts

This project ran a loose count (any "cat"/"cats" match) and a strict count (requiring a clear possessive, article, or explicit pairing like "pet cat"). In LinkBoost-2025, the strict count is **zero**. All 15 distinct "cat"-matching strings in that dataset trace to non-animal usage: the Caterpillar stock ticker, hurricane categories, the "fat cats" idiom, dismissive internet-culture references to cat videos, and the Jaguar logo story. None is a post about an actual animal.

In the other two datasets, the strict count is 28.5% of the loose count in podawaa2024 and 39.3% in HyperClapper. Real animal content exists, but it is a minority of what a naive keyword search would have counted.

## Why this gets a whole article

This project runs dozens of keyword scans, and most work fine with straightforward matching. "Cat" shows why manual verification is needed: a term that looks unambiguous can collide with an exam name, a stock ticker, a weather scale, and a car logo in the same dataset.

## What this is, and isn't

**VERIFIED**, reproducible via the published scan: the loose/strict count gap and the zero-genuine-mentions result for LinkBoost-2025.

Full methodology: **github.com/DreamITSoftware/SPOTAPOD**.

<!-- export65-note -->
> **Update, 22 October 2026.** In the [65 export files](../provenance.md#the-65-export-files), 491 of 56,363 records (0.871%) mention an animal term. The loose count for "cat" is 97 and the strict count is 31 (32.0%), so the strict share sits between podawaa2024 (28.5%) and HyperClapper (39.3%), and the strict count is not zero as it is in LinkBoost-2025. The scan's duplicate-template check did not fire, and the matching records hold 476 distinct texts. Detail: [animal content](../research/animal-content.md#the-65-export-files).

---

*Self-published. Not peer-reviewed. Independently reproducible from the source files.*
