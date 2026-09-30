# What Changes If LinkedIn Ships an "Authenticity Score"

### Speculative, explicitly labeled as such: what this project's methodology suggests such a feature would need to actually work

No such feature is known to exist or to be planned, as far as this project is aware. This is a speculative design exercise grounded in this project's own detection methodology, useful precisely because it's honest about being speculation rather than prediction.

## What an effective version would likely need

Based on the pattern types this project has independently verified as detectable from engagement data alone, an authenticity signal would need to account for account-level concentration and velocity (this project's posting-streak and top-account-share findings), content-level duplication (the 533-post resume-template cluster and similar clusters are detectable precisely because duplicate text is straightforward to fingerprint), and metric-relationship anomalies (the zero-view-with-high-likes pattern this project has documented repeatedly). A score built on only one of these three signal types would likely miss manipulation patterns the other two would catch. This project's own three-dataset comparison found genuinely different manipulation models (like-based vs. comment-based) that a single-signal detector would handle very unevenly.

## What this project's data can't tell you about a hypothetical feature

Nothing about implementation feasibility at LinkedIn's actual scale, nothing about false-positive rates against genuine but unusual posting patterns (a legitimately prolific poster shouldn't be penalized the same as a pod-driven account), and nothing about how such a score would or should be surfaced to users, advertisers, or recruiters. Those are product and policy questions well outside what an aggregate research dataset can settle.

## Why speculate about this at all

Grounding a speculative feature discussion in specific, already-verified detection methodology is more useful than speculating in the abstract. It turns "LinkedIn should fight fake engagement" (a platitude) into a concrete list of pattern types a real system would need to catch (a checklist).

## What this is, and isn't

**INFERENCE, throughout, and clearly labeled as such.** No LinkedIn "authenticity score" feature is known to exist or to be planned.

Full detection methodology: **github.com/DreamITSoftware/SPOTAPOD**.

---

*Self-published. Not peer-reviewed.*
