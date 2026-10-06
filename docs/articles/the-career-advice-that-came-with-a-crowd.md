# The Career Advice That Came With a Crowd

### LinkedIn is a career platform. Turns out career content on it is also the stuff most likely to be cheering for itself.

Somewhere in a dataset of engagement-pod activity, 469 posts generated 77,969 records of coordinated liking and commenting. That is not a typo. Fewer than 500 pieces of content were hit repeatedly by the same reciprocal engagement, which made them look like broad, organic agreement.

Almost 6 in 10 of the accounts behind those pod-driven posts describe themselves as executive coaches or leadership consultants. So the content most likely to be boosting itself on a career platform is career advice.

## Yes, we know, LinkedIn is about careers

Yes, LinkedIn is a career platform, and career content showing up a lot on it is expected. That is a fair objection. A platform built for careers will have career content, and a dataset full of coaching profiles will talk about coaching. None of that proves anything by itself.

The actual test is whether the posts about resumes and promotions get more coordinated engagement than everything else in the same file, not whether career content and coordinated engagement both appear in it. Run post by post inside one dataset, the objection does not hold. Career-advice posts land a like and a comment together, the fingerprint of a pod, at **84.06%**. Everything else in the same file sits at **65.53%**, which is already a suspiciously high number for a place people supposedly visit to talk about their jobs. Career content still beats it by nearly 19 points.

So the result is not just that LinkedIn talks about careers. Career posts get more coordinated engagement than other posts.

## Why career advice, of all things

Coaches and consultants sell influence, so their posts need to look influential. A post with many likes and comments looks popular and looks like proof the advice works, which is worth paying for. This is likely ordinary business using a shortcut that is illegal.

Rule 16 CFR § 465.8 bans fake engagement because it "materially misrepresents influence or importance" to whoever relies on it. The harm is that readers cannot tell a post that actually landed from one that got help from a group.

## What that number does once it's in your feed

Likes and comments work as social proof, which readers use to judge how much a stranger's opinion is worth without checking it themselves. A post with 200 real likes reads as 200 people vouching for it. That credibility carries over to whatever the post claims: the leadership tip, the "here's exactly how I got promoted" story, the framework with a course attached.

This data does not track who read these posts or what they did afterward. The evidence tiers below separate what is proven from what is a reasonable guess.

## What this is, and isn't

**VERIFIED**, reproducible from the source files: career-advice content ranges from 4.45% to 16.52% across three datasets, one dataset shows 469 unique posts generating 77,969 pod-engagement records, 59.5% of that dataset's occupation text skews toward executive and leadership coaching, and within a single checksummed dataset, career-advice-matching posts show reciprocal engagement at 84.06% against a 65.53% baseline for everything else in that same file, an 18.53 percentage point gap.

**Not established**: this comparison currently rests on one dataset. The other two files either lack the fields needed to run it (no reciprocity flag) or are entirely pod-engagement records by definition (no non-pod baseline to compare against). The keyword matching behind "career-advice" is a blunt signal: "promotion" can mean a career move or a marketing one, so some noise sits on both sides of the comparison.

**INFERENCE**: that inflated engagement on career content specifically shapes how readers, especially people early in their careers who have less experience to check the advice against, judge what's credible or normal. No dataset here tracks actual readers, what they believed, or what they did as a result. The mechanism itself is well established: social proof shapes trust, which is the reason the FTC rule above exists. Whether it plays out this way for career content, and whether younger or less experienced readers are affected more, is a reasonable hypothesis. This data does not measure it.

Full methodology, every dataset, every script: **github.com/DreamITSoftware/SPOTAPOD**.

---

*Self-published. Not peer-reviewed. Every figure above is independently reproducible from the source files using the scripts published in the linked repository.*
