# How Three Datasets Taught Me to Distrust My Own First Draft

### The most recent correction this project made wasn't to someone else's claim. It was to a number this project had already published.

The methodology series so far has mostly been about catching other people's errors: a disputed third-party document, a keyword collision, a claim that didn't survive rechecking. This one is about catching this project's own.

## What happened

A previously published piece in this project stated that nine of the ten single highest-liked posts in a 213,491-post dataset showed zero recorded views. That number had been written, committed, and published, and, on review, it turned out to have never actually been independently checked against the raw data before it went out. It was closer to a remembered impression of the finding than a rerun of the script that would have confirmed it.

Rechecking directly against the raw file, sorting all 213,491 posts by like count, taking the top ten, and counting how many showed zero views, produced a different answer: four, not nine.

## Why this one stings more than the others

Catching someone else's bad number feels like doing the job right. Catching your own, in a piece you already published, feels like evidence the process failed somewhere. Both reactions are natural, and only one of them is useful. The actual lesson from three datasets' worth of work is that the discipline of "verify before publishing" isn't a one-time gate you pass through. It has to survive being applied to your own prior output with exactly the same skepticism as anyone else's.

## What happened next

The number was corrected in every location it appeared: the repository's commentary file, a standalone copy of the article, and a delivered output copy, and the correction was logged explicitly in this project's changelog, stating the original claim, the corrected figure, and how the correction was found. Nothing was quietly edited without a trace. The other statistics in the same original piece had already been independently verified in an earlier pass and were left unchanged, because they'd actually earned that status.

## The actual takeaway

Three datasets in, the operating assumption for this project isn't "our published numbers are reliable because we're careful." It's "every published number is a claim someone should feel free to recheck, including us, because eventually someone will find the one we got wrong, and it's better that someone is us."

## What this is, and isn't

**Corrected, transparently**: "nine of ten" became "four of ten," logged in full in this project's public changelog.

**A standing practice, not a one-time event**: this project rechecks its own prior claims the same way it checks anyone else's.

Full correction log: **github.com/DreamITSoftware/SPOTAPOD**.

---

*Self-published. Not peer-reviewed.*
