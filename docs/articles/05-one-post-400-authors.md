# One Post, 400 Authors

### The same piece of content appears under 400 different names in a single LinkedIn dataset

Somewhere in a 2024 LinkedIn export, one specific piece of post content, the same words, character for character, was published under **400 different author identities**.

Not four. Not forty. Four hundred separate accounts, each posting an identical piece of text as if it were their own.

## How this was found

Checking a dataset for duplicate content is straightforward: group every post by its exact text, and count how many distinct authors show up per group. Most duplicate content clusters in this dataset are small. The median cluster spans just two distinct authors, which is roughly what you'd expect from ordinary things like someone quoting a well-known line, or two people independently reposting a popular meme.

But the distribution has a long tail. There are 1,875 clusters where at least two different authors posted identical content. Most of those clusters are small: 1,491 of them involve exactly two authors. A handful climb much higher: one cluster reaches 9 authors, another 11, another 21. And at the very top, one specific piece of content was posted, word for word, by 400 distinct author identities.

## What 400 identical posts implies

A person quoting a famous saying doesn't explain this. Four hundred people independently deciding, unprompted, to write the exact same original sentence doesn't happen by coincidence at any scale. The far more plausible explanation is a shared script or template, distributed to or used by many accounts, each publishing it as if it were their own voice and their own thought.

This is exactly the mechanism this project's other findings point toward: LinkedIn's "authentic professional voice" content, at scale, includes coordinated or templated material presented as individual, original insight.

## What this is, and isn't

**VERIFIED**, reproducible directly from the dataset: cross-author duplicate-content clustering on this file finds 1,875 clusters of two or more distinct authors sharing identical content, with a maximum cluster size of 400 distinct authors and a median of 2.

**Not established here**: which specific content this was, who distributed it, or whether the 400 accounts are real individuals, bot accounts, or some mix. This project does not identify individual posts, authors, or the specific text involved, consistent with its no-identification discipline throughout.

Full methodology: **github.com/DreamITSoftware/SPOTAPOD**.

---

*Self-published. Not peer-reviewed. Independently reproducible from the source file. No individual post, author, or account is identified anywhere in this project.*
