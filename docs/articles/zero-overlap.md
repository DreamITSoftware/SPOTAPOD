# Zero Overlap

### Two different LinkedIn engagement-pod tools, 702 and 414 accounts respectively, share not a single user

If two products are selling the same kind of engagement manipulation, you'd expect some crossover: customers who shop around, or accounts hedging their bets across more than one tool. Checking two such tools against each other directly, across a combined 1,116 accounts, finds **zero** shared users.

## What was actually compared

Two datasets, each drawn from a different commercial LinkedIn engagement-pod tool, were hashed and compared account by account: 702 distinct accounts from one tool, 414 from the other. Every identifier was hashed before comparison and never held in plaintext, so this check only ever produces two numbers: how many accounts are in each set, and how many appear in both.

The overlap: zero. Not "low." Not "a handful, rounding to zero percent." Not one single account, out of 1,116 checked, appears in both datasets.

## Why zero is a real, meaningful finding

Zero could mean the market for engagement manipulation is more segmented than it looks from the outside, with different tools serving genuinely different customer bases, maybe by price point, region, or word of mouth. Or it could mean the total population of people using any such tool is large enough that, statistically, two samples this size wouldn't be expected to overlap even if plenty of individuals use more than one product.

This project can't tell you which explanation is right. What it can tell you is that the two most obvious stories people tell about engagement-pod users ("it's basically the same tight community running every tool" and "it's all one interconnected market") aren't supported by this specific comparison. Whatever is happening here, it isn't obviously coordinated between these two products.

## What this is, and isn't

**VERIFIED**, directly reproducible: hashing and comparing the account identifiers from both datasets returns 0 accounts in common, out of 702 and 414 respectively.

**Not established here**: why the overlap is zero. Both explanations above remain open. This project reports the number, not the cause.

Full methodology: **github.com/DreamITSoftware/SPOTAPOD**.

---

*Self-published. Not peer-reviewed. Independently reproducible from the source files. No account is identified anywhere in this project.*
