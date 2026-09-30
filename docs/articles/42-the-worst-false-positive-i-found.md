# The Worst False Positive I Found

### A keyword search for "cat" mentions on LinkedIn mostly finds "education," "certificate," and "indication"

Keyword-based content classification is fast, cheap, and reproducible, and it fails in ways that are obvious in hindsight and invisible until you check.

## What happened

Building a topic taxonomy across three engagement-pod datasets meant picking keyword patterns for dozens of categories, including one for posts mentioning animals. "Cat" seemed like a reasonable substring to check for pet-related content.

It wasn't. A substring match for "cat" doesn't just catch "cat." It catches every occurrence of "cat" inside a longer word: education, certificate, indication, application, communication. On a dataset full of career-advice content, those words are everywhere. The keyword hit rate for "cat" was dominated almost entirely by these false positives, not by anyone posting about their pet.

## The fix, and why it matters more than the fix itself

The actual fix was mechanical: word-boundary matching instead of substring matching, which is a one-line change in most regex implementations. That's not the interesting part.

The interesting part is what this reveals about every other keyword-based finding in this project. Any short, common substring is a landmine, and the only way to know if you've stepped on one is to actually look at a sample of what the keyword matched, not just trust the count. This project caught "cat" because someone looked at example matches out of general caution. It's reasonable to assume other, less obvious collisions exist in categories that weren't checked as closely, which is exactly why every keyword-based finding in this project carries an explicit "not manually verified per-record" caveat rather than being presented as exact.

## The broader pattern

This isn't a one-off embarrassment. It's a category of error that automated text classification runs into constantly. See also this project's own "immunotherapy" category, which turned out to be dominated by shopping-cart page text, and the "son" collision with French-language grammar constructions. Short keywords collide with the world in ways a spreadsheet of counts will never surface on its own.

## What this is, and isn't

**VERIFIED**: the "cat" substring-match failure mode, and the word-boundary fix that resolved it.

**A standing caveat, not a one-time fix**: every keyword-based category in this project is presented with the explicit acknowledgment that undiscovered collisions like this one may still exist.

Full methodology notes: **github.com/DreamITSoftware/SPOTAPOD**.

---

*Self-published. Not peer-reviewed.*
