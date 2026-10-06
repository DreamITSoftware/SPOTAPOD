# How Three Datasets Taught Me to Distrust My Own First Draft

### The most recent correction this project made was to a number it had already published

The methodology series so far has mostly covered other people's errors: a disputed third-party document, a keyword collision, a claim that did not survive rechecking. This one covers an error in this project's own work.

## What happened

A previously published piece in this project stated that nine of the ten single highest-liked posts in a 213,491-post dataset showed zero recorded views. That number had been written, committed, and published. On review, it turned out never to have been checked against the raw data before it went out. It came from a remembered impression of the finding, not from a rerun of the script.

Rechecking directly against the raw file, sorting all 213,491 posts by like count, taking the top ten, and counting how many showed zero views, produced a different answer: four, not nine.

## Why this one was harder

Catching someone else's bad number feels like doing the job right. Catching your own, in a piece you already published, feels like a process failure. The lesson from three datasets' worth of work is that "verify before publishing" is not a one-time gate. It has to be applied to your own prior output with the same skepticism as anyone else's.

## What happened next

The number was corrected in every location it appeared: the repository's commentary file, a standalone copy of the article, and a delivered output copy. The correction was logged in this project's changelog, stating the original claim, the corrected figure, and how the correction was found. Nothing was edited without a trace. The other statistics in the same original piece had been independently verified in an earlier pass and were left unchanged.

## Takeaway

Three datasets in, this project does not assume its published numbers are reliable because it is careful. Every published number is a claim anyone should feel free to recheck, including us. Someone will eventually find one we got wrong, and it is better if that someone is us.

## What this is, and isn't

**Corrected, transparently**: "nine of ten" became "four of ten," logged in full in this project's public changelog.

**A standing practice**: this project rechecks its own prior claims the same way it checks anyone else's.

Full correction log: **github.com/DreamITSoftware/SPOTAPOD**.

---

*Self-published. Not peer-reviewed.*
