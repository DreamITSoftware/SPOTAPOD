# The Audit: Series Launch

### A recurring series that reruns this project's scripts against updated or re-checked data to see what has changed

Every finding in this project is only as current as the moment it was computed. This series periodically reruns the same scripts against the same or newly supplied data and reports whether the numbers hold.

## Installment one: rerunning the zero-view anomaly check

Rerunning `analysis/` scripts against the current copy of `podawaa2024.json` reproduces the original figures exactly: 75,442 posts (35.3%) with recorded likes and zero recorded views, out of 213,491 total. The source file has not changed since the original computation, which was confirmed rather than assumed.

## What an installment checks

A static historical dataset does not change on its own, so an installment checks two things: whether the script still runs and produces the documented number (catching code rot, dependency changes, or silent script bugs), and whether the project has received an updated or corrected source file that would change a published figure.

## Why rerun data that should not change

A script that ran correctly a year ago can break after a language or library update, and the only way to know is to rerun it. This series makes that check a standing, visible practice rather than something that happens only when someone notices a discrepancy.

## If something has changed

If a rerun ever produces a different number than originally published, whether from a script bug, a data update, or a methodology refinement, that becomes a "Corrected" series installment, cross-linked here, following this project's standard correction-disclosure practice.

## What this is, and isn't

**VERIFIED, reconfirmed**: 75,442 posts (35.3% of 213,491), rerun and matching the original published figure exactly.

Full scripts: **github.com/DreamITSoftware/SPOTAPOD**.

---

*Self-published. Not peer-reviewed.*
