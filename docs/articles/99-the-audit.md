# The Audit: Series Launch

### A recurring series re-running this project's own scripts against updated or re-checked data to see what, if anything, has changed

Every finding in this project is only as current as the moment it was computed. This series exists to periodically rerun the same scripts against the same or newly supplied data and report, honestly, whether the numbers hold.

## Installment one: rerunning the zero-view anomaly check

Rerunning `analysis/` scripts against the current copy of `podawaa2024.json` reproduces the original figures exactly: 75,442 posts (35.3%) with recorded likes and zero recorded views, out of 213,491 total. No drift, because the underlying source file hasn't changed since the original computation, which is itself worth confirming rather than assuming.

## What an audit installment is actually checking

Not "is the finding still true in some abstract sense," a static historical dataset doesn't change on its own, but two more concrete things: does the script still run correctly and produce the documented number (catching any code rot, dependency changes, or silent script bugs), and has this project received any updated or corrected version of a source file that would change a previously published figure.

## Why this matters even for data that "shouldn't" change

Software rots. A script that ran correctly a year ago can silently break due to a language or library update, and the only way to know is to actually rerun it rather than assume the original result still holds. This series exists specifically to make that check a standing, visible practice rather than something that only happens if someone happens to notice a discrepancy.

## What a future installment looks like when something has changed

If a rerun ever produces a different number than originally published, whether from a script bug, a data update, or a methodology refinement, that becomes a "Corrected" series installment as well, cross-linked here, following this project's standard correction-disclosure practice.

## What this is, and isn't

**VERIFIED, reconfirmed**: 75,442 posts (35.3% of 213,491), rerun and matching the original published figure exactly.

Full scripts: **github.com/DreamITSoftware/SPOTAPOD**.

---

*Self-published. Not peer-reviewed.*
