# LinkedIn's "Immunotherapy" Posts Are Mostly Shopping Carts

### A cell-therapy keyword search returned 107, 60, and 58 false positives before the shipped script was written

Searching LinkedIn content for "CAR-T," a specific cell-therapy term, should be an unambiguous keyword scan. An early draft of the pattern was not. Written to also catch "CAR T" written as two words, the case-insensitive regex also matched the ordinary word "cart": shopping cart, cart abandonment, price comparisons.

The result was 107, 60, and 58 false-positive matches across the three datasets, none of them about cell therapy at all. Sampling the matches showed they were posts about online shopping, Shopify stores, subscription services, grocery habits.

## The fix, and what it cost

The shipped version requires "CAR-T" to appear near the words "cell" or "therapy." That eliminates the shopping-cart noise at the cost of missing a bare "CAR-T" mention with no qualifying word nearby. The trade is acceptable because noise dominated the unqualified pattern.

## A second false positive, caught a different way

Even after that fix, LinkBoost-2025 showed 40 "immunotherapy" matches, all tracing to a single post. Checked directly, it was not medical content. It was a generic business-transformation and AI-leadership post ("Transformation fails when we forget the human core... how AI, values, and human creativity must work together") that used the word "immunotherapy" once, probably as an example, and was counted 40 times by the platform's own structure.

## Why this gets a whole article

This is one of the smallest genuine content categories this project has found. Reaching that small, accurate number required catching two different kinds of false positive. One was a regex design flaw caught before it reached a committed script. The other was a duplicate-template artifact caught by the safeguard that has caught similar issues elsewhere in this project.

## What this is, and isn't

**VERIFIED**, reproducible via the published scan: the false-positive counts, the qualifying-word fix, and the single-post LinkBoost-2025 correction.

Full methodology: **github.com/DreamITSoftware/SPOTAPOD**.

---

*Self-published. Not peer-reviewed. Independently reproducible from the source files.*
