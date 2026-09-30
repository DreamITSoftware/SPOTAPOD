# Four of the Top Ten Are Fake

### The most-liked posts in a 213,491-post LinkedIn dataset, checked one by one

If you wanted to find the best evidence of manufactured engagement on LinkedIn, the obvious place to start is the top of the leaderboard: the single most-liked posts in the dataset. Surely the biggest numbers are the most scrutinized, the least likely to be broken.

They aren't. Ranking all 213,491 posts in a 2024 dataset by like count and looking at the top ten, **four** show zero recorded views.

| Rank | Likes | Views |
|---|---|---|
| 1 | 215,818 | 14,771,715 |
| 2 | 88,028 | 0 |
| 3 | 87,465 | 0 |
| 4 | 83,962 | 0 |
| 5 | 77,371 | 0 |
| 6 | 71,390 | 3,175,760 |
| 7 | 69,407 | 773 |
| 8 | 58,527 | 1,715,327 |
| 9 | 56,322 | 10,115,319 |
| 10 | 55,020 | 1,241,411 |

Positions two through five, four posts in a row holding roughly a third of all the likes in the top ten combined, show exactly zero views. Position seven shows 69,407 likes against 773 views, a ratio of 90 likes for every view, itself far outside any normal range.

## Why this is worth publishing as its own piece

An earlier version of this finding, published elsewhere, claimed nine of the ten highest-liked posts showed this pattern. That number was wrong, because it went out before it was checked directly against the source file. Rerunning the count properly gives four, not nine. That correction matters more than the headline number: a project built on evidence tiers only means something if it holds itself to the same standard it applies to outside claims, including its own earlier, unverified ones.

Four out of ten is still a real finding. It means two in five of the single most successful posts by engagement in this entire dataset carry an engagement signature that could not have happened as displayed.

## What this is, and isn't

**VERIFIED**, directly reproducible: sorting the 213,491-post dataset by `Likes` descending and checking `Views` on the top 10 produces exactly the table above.

**Corrected from an earlier, unverified claim of "nine of ten."** That number is not used anywhere in this project going forward.

Full dataset and scripts: **github.com/DreamITSoftware/SPOTAPOD**.

---

*Self-published. Not peer-reviewed. Independently reproducible from the source file.*
