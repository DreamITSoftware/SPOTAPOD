# Nobody Talks About Animals on LinkedIn

### Zero. That's how many genuine posts about cats show up in one entire LinkedIn dataset, once you filter out the noise

"Cat" turned out to be the single worst word this project has ever tried to count. Sampling actual matches for bare "cat"/"cats" across three LinkedIn datasets surfaced eight completely unrelated meanings hiding inside one short word:

- **CAT**, India's major MBA entrance exam (Common Admission Test)
- The **.cat** domain extension for Catalonia
- **"Cat Nat"**, a French insurance term for natural catastrophes
- **"cat"** as shorthand for the Catalan language in multilingual bios
- **CAT**, the NYSE ticker symbol for Caterpillar Inc.
- **Cat 1 through Cat 5**, the hurricane intensity scale
- **"Fat cats"**, the idiom for wealthy elites
- Jaguar's **"leaping cat"** logo, in a brand-redesign post

## The number that makes the point

Running both a loose count (any "cat"/"cats" match) and a strict count (requiring a clear possessive, article, or explicit pairing like "pet cat") produces a stark gap. In LinkBoost-2025, the strict count is **zero**. All 15 distinct "cat"-matching strings in that dataset trace to non-animal usage: the Caterpillar stock ticker, hurricane categories, the "fat cats" idiom, dismissive internet-culture references to cat videos, and the Jaguar logo story. Not one is an actual post about an actual animal.

In the other two datasets, the strict count survives at a real but much-reduced rate: 28.5% of the loose count in podawaa2024, 39.3% in HyperClapper. Real animal content exists. It's just a minority of what a naive keyword search would have counted.

## Why this is worth a whole article

This project runs dozens of keyword scans, and most of them work fine with straightforward matching. "Cat" is the exception that proves why manual verification matters every time: a term that looks unambiguous in isolation can collide with an exam name, a stock ticker, a weather scale, and a car logo, all at once, in the same dataset.

## What this is, and isn't

**VERIFIED**, reproducible via the published scan: the loose/strict count gap and the zero-genuine-mentions result for LinkBoost-2025.

Full methodology: **github.com/DreamITSoftware/SPOTAPOD**.

---

*Self-published. Not peer-reviewed. Independently reproducible from the source files.*
