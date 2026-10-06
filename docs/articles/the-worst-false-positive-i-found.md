# The Worst False Positive I Found

### A keyword search for "cat" mentions on LinkedIn mostly finds "education," "certificate," and "indication"

Keyword-based content classification is fast, cheap, and reproducible. It also fails in ways that are obvious in hindsight and invisible until you check.

## What happened

Building a topic taxonomy across three engagement-pod datasets meant picking keyword patterns for dozens of categories, including one for posts mentioning animals. "Cat" seemed like a reasonable substring to check for pet-related content.

It was not. A substring match for "cat" catches every occurrence of "cat" inside a longer word: education, certificate, indication, application, communication. On a dataset full of career-advice content, those words are everywhere. The hit rate for "cat" came almost entirely from these false positives, not from anyone posting about a pet.

## The fix, and what it implies

The fix was mechanical: word-boundary matching instead of substring matching, a one-line change in most regex implementations.

The larger point concerns every other keyword-based finding in this project. Any short, common substring can collide with longer words, and the only way to know is to look at a sample of what the keyword matched instead of trusting the count. This project caught "cat" because someone looked at example matches. Other, less obvious collisions probably exist in categories that were not checked as closely. That is why every keyword-based finding in this project carries a "not manually verified per-record" caveat and is not presented as exact.

## The broader pattern

This is not a one-off. Automated text classification runs into this kind of error constantly. See also this project's own "immunotherapy" category, which turned out to be dominated by shopping-cart page text, and the "son" collision with French-language grammar constructions. A spreadsheet of counts will not show these collisions on its own.

## What this is, and isn't

**VERIFIED**: the "cat" substring-match failure mode, and the word-boundary fix that resolved it.

**A standing caveat**: every keyword-based category in this project is presented with the explicit acknowledgment that undiscovered collisions like this one may still exist.

Full methodology notes: **github.com/DreamITSoftware/SPOTAPOD**.

---

*Self-published. Not peer-reviewed.*
