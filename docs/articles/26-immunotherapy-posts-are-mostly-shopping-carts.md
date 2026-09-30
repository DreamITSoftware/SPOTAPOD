# LinkedIn's "Immunotherapy" Posts Are Mostly Shopping Carts

### A cell-therapy keyword search returned 107, 60, and 58 false positives before a single line of the shipped script was written

Searching LinkedIn content for "CAR-T," a real and specific cell-therapy term, should be about as unambiguous as keyword scans get. An early draft of the pattern proved otherwise. Written to also catch "CAR T" written as two words, the case-insensitive regex also matched the ordinary word "cart": shopping cart, cart abandonment, price comparisons.

The result was 107, 60, and 58 false-positive matches across the three datasets, none of them about cell therapy at all. Sampling the actual matches made it obvious immediately. These were posts about online shopping, Shopify stores, subscription services, grocery habits.

## The fix, and what it cost

The shipped version requires "CAR-T" to appear near the words "cell" or "therapy." That eliminates the shopping-cart noise at the cost of missing a bare "CAR-T" mention with no qualifying word nearby. It's an acceptable trade, given how completely the unqualified pattern was dominated by noise.

## A second false positive, caught a different way

Even after that fix, LinkBoost-2025 showed 40 "immunotherapy" matches, all tracing to a single post. Checked directly, it wasn't medical content at all. It was a generic business-transformation and AI-leadership post ("Transformation fails when we forget the human core... how AI, values, and human creativity must work together") that happened to use the word "immunotherapy" once, probably as an illustrative example, then got boosted 40 times by the platform's own structure.

## Why this is worth a whole article

This category ended up being one of the smallest genuine content categories this project has found. Getting to that small, accurate number took catching two completely different kinds of false positive. One was a regex design flaw caught before it ever reached a committed script. The other was a duplicate-template artifact caught by the same safeguard that's caught similar issues elsewhere in this project.

## What this is, and isn't

**VERIFIED**, reproducible via the published scan: the false-positive counts, the qualifying-word fix, and the single-post LinkBoost-2025 correction.

Full methodology: **github.com/DreamITSoftware/SPOTAPOD**.

---

*Self-published. Not peer-reviewed. Independently reproducible from the source files.*
