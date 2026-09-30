# How to Build an Evidence-Tier System for Your Own Research

### Five labels, applied without exception, that do more honesty-enforcement than any style guide

The single structural decision that shapes every article in this project isn't a finding. It's a labeling system, applied to every claim before it's allowed to be published.

## The five tiers

**VERIFIED**: independently computed by this project directly from raw source data, reproducible by rerunning the script.

**CORROBORATED**: supported by more than one independent source or method, though not a from-scratch computation.

**STATED**: reported as fact by a specific named source (a filing, a case document, a company statement) without independent recomputation.

**UNCORROBORATED**: a claim this project encountered but could not verify or refute with available data.

**INFERENCE**: a reasonable interpretation or hypothesis this project is explicitly proposing, clearly distinguished from a measured fact.

## The rule that makes it work

The system only functions because of one hard constraint: a claim's tier can only be downgraded, never upgraded, by later work. If a VERIFIED number turns out to be wrong on recheck, it gets corrected and the correction is logged. It doesn't quietly become "STATED" to save face. If an INFERENCE later turns out to align with independently verified data, it still gets re-labeled based on the new check, not promoted on the strength of the original guess.

This matters because the opposite temptation is real and constant. An inference that turns out right feels like it deserves more credit than it earned at the time it was made, and a verified number that turns out wrong is uncomfortable to downgrade in public. The discipline is refusing both moves.

## Why most research writing doesn't do this

It's slower. Every sentence with a number in it needs a tier decided before it ships, and that decision sometimes means admitting a claim is weaker than the writing would be if you just didn't label it. But the alternative is what most public data commentary actually does: state everything with the same confident tone regardless of how well-supported it is, and let the reader guess which numbers would survive a fact-check.

## Applying this outside a research project

The same five categories work for any claim-heavy writing, a business case, a policy memo, a due-diligence report. The discipline is the same. Write the label before you write the sentence, and let a claim's evidentiary weakness show up as a weaker label rather than a hedge word buried in the middle of a paragraph.

## What this is, and isn't

**A methodology choice, applied consistently**: every claim in every article in this series carries one of these five labels, without exception.

Full tier definitions and examples: **github.com/DreamITSoftware/SPOTAPOD**.

---

*Self-published. Not peer-reviewed.*
