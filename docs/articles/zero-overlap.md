# Zero Overlap

### Two different LinkedIn engagement-pod tools, 702 and 414 accounts respectively, share no users

If two products are selling the same kind of engagement manipulation, you would expect some crossover, such as customers who shop around or accounts using more than one tool. Checking two such tools against each other directly, across a combined 1,116 accounts, finds **zero** shared users.

## What was actually compared

Two datasets, each drawn from a different commercial LinkedIn engagement-pod tool, were hashed and compared account by account: 702 distinct accounts from one tool, 414 from the other. Every identifier was hashed before comparison and never held in plaintext, so this check only ever produces two numbers: how many accounts are in each set, and how many appear in both.

The overlap is zero. No account out of 1,116 checked appears in both datasets.

## What zero could mean

The market for engagement manipulation may be more segmented than it looks, with different tools serving different customer bases, perhaps by price, region, or word of mouth. Or the total population of users may be large enough that two samples this size would not be expected to overlap, even if many individuals use more than one product.

This project can't tell you which explanation is right. It does show that two common stories about engagement-pod users ("it's basically the same tight community running every tool" and "it's all one interconnected market") are not supported by this comparison. The two products do not appear to be coordinated.

## What this is, and isn't

**VERIFIED**, directly reproducible: hashing and comparing the account identifiers from both datasets returns 0 accounts in common, out of 702 and 414 respectively.

**Not established here**: why the overlap is zero. Both explanations above remain open. This project reports the number, not the cause.

Full methodology: **github.com/DreamITSoftware/SPOTAPOD**.

---

*Self-published. Not peer-reviewed. Independently reproducible from the source files. No account is identified anywhere in this project.*
