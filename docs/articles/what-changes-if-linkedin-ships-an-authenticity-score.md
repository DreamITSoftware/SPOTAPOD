# What Changes If LinkedIn Ships an "Authenticity Score"

### Speculative, and labeled as such: what this project's methodology suggests such a feature would need

No such feature is known to exist or to be planned, as far as this project is aware. This is a speculative design exercise based on this project's own detection methodology. It is speculation, not prediction.

## What an effective version would need

Based on the pattern types this project has independently verified as detectable from engagement data alone, an authenticity signal would need to account for account-level concentration and velocity (this project's posting-streak and top-account-share findings), content-level duplication (the 533-post resume-template cluster and similar clusters are detectable precisely because duplicate text is straightforward to fingerprint), and metric-relationship anomalies (the zero-view-with-high-likes pattern this project has documented repeatedly). A score built on only one of these three signal types would likely miss manipulation patterns the other two would catch. This project's three-dataset comparison found different manipulation models (like-based vs. comment-based) that a single-signal detector would handle unevenly.

## What this project's data cannot tell you about a hypothetical feature

The data says nothing about implementation feasibility at LinkedIn's scale, nothing about false-positive rates against genuine but unusual posting patterns (a legitimately prolific poster should not be penalized the same as a pod-driven account), and nothing about how such a score would or should be surfaced to users, advertisers, or recruiters. Those are product and policy questions that an aggregate research dataset cannot settle.

## Why speculate at all

Basing a feature discussion on already-verified detection methodology is more useful than speculating in the abstract. It replaces "LinkedIn should fight fake engagement" with a concrete list of pattern types a real system would need to catch.

## What this is, and isn't

**INFERENCE, throughout.** No LinkedIn "authenticity score" feature is known to exist or to be planned.

Full detection methodology: **github.com/DreamITSoftware/SPOTAPOD**.

---

*Self-published. Not peer-reviewed.*
