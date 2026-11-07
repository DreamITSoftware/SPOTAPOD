# How to Build an Evidence-Tier System for Your Own Research

### Five labels, applied to every claim, enforce honesty better than a style guide

The main structural decision in this project is a labeling system, not a finding. Every claim gets a label before it is published.

## The five tiers

**VERIFIED**: independently computed by this project directly from raw source data, reproducible by rerunning the script.

**CORROBORATED**: supported by more than one independent source or method, though not a from-scratch computation.

**STATED**: reported as fact by a specific named source (a filing, a case document, a company statement) without independent recomputation.

**UNCORROBORATED**: a claim this project encountered but could not verify or refute with available data.

**INFERENCE**: a reasonable interpretation or hypothesis this project is explicitly proposing, clearly distinguished from a measured fact.

## The rule that makes it work

The system depends on one constraint: later work can only downgrade a claim's tier, never upgrade it. If a VERIFIED number turns out to be wrong on recheck, it gets corrected and the correction is logged. It does not quietly become "STATED" to save face. If an INFERENCE later turns out to align with independently verified data, it still gets re-labeled based on the new check, not promoted on the strength of the original guess.

The opposite temptation is constant. An inference that turns out right feels like it deserves more credit than it earned when it was made, and a verified number that turns out wrong is uncomfortable to downgrade in public. The system requires refusing both.

## Why most research writing doesn't do this

It is slower. Every sentence with a number in it needs a tier decided before it ships, and that sometimes means admitting a claim is weaker than the prose would suggest. Most public data commentary instead states everything in the same confident tone regardless of support and leaves the reader to guess which numbers would survive a fact-check.

## Applying this outside a research project

The same five categories work for any claim-heavy writing, such as a business case, a policy memo or a due-diligence report. Write the label before the sentence, and show a claim's weak evidence as a weaker label rather than a hedge word inside a paragraph.

## What this is, and isn't

**A methodology choice, applied consistently**: every claim in every article in this series carries one of these five labels, without exception.

Full tier definitions and examples: **github.com/DreamITSoftware/SPOTAPOD**.

---

*Self-published. Not peer-reviewed.*
