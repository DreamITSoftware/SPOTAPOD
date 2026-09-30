# How "Son" Became a French Grammar Problem

### A single word looked like the biggest finding in an entire scan, until 98.5% of it turned out to be the wrong language

An early draft of a children-content scan matched the word "son" the same way it matched every other term: bare, case-insensitive. The raw result for one dataset was 17,573 matches, by far the largest single term found anywhere in that scan, wildly out of proportion to how minor a term "son" was in the other two datasets checked.

That size difference was the tell. "Son" isn't just an English noun for a male child. It's also the French possessive pronoun meaning "his" or "her" ("elle a pris le controle de son compte," "she took control of her account"). One of the three datasets in this project contains a meaningful amount of French-language content, the same underlying fact already behind a separate "MIT" and German "mit" collision documented elsewhere in this project.

## The number that confirmed it

A manual check of the raw matches found only **1.5%**, or 269 of 17,573, showed a clear English usage pattern actually referring to a child: "my son," "her son," "son of," "son is." The remaining 98.5% was the French possessive pronoun or otherwise ambiguous.

## The fix

The shipped script now requires "son"/"sons" to appear with a clear English usage marker, a possessive pronoun or article immediately before it, or "of/is/was/are/were/who" immediately after, rather than matching the bare word. Every other term in the same scan (child/children, kid/kids, daughter, toddler, baby/babies, parenting) doesn't have this collision problem and is matched normally.

## Why a caught error is more useful than a clean one

A scan that had simply reported "17,573 mentions of sons" without checking would have produced a number nearly 65 times too large, and nobody reading the headline figure would have had any reason to doubt it. The correction here isn't a footnote. It's the entire reason to trust the numbers this project does publish.

## What this is, and isn't

**VERIFIED**, reproducible via the published scan: the 1.5% English-usage rate and the corrected matching logic.

Full methodology: **github.com/DreamITSoftware/SPOTAPOD**.

---

*Self-published. Not peer-reviewed. Independently reproducible from the source files.*
