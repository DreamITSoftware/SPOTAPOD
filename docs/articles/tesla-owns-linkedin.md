# Tesla Owns LinkedIn

### Every carmaker mentioned across three LinkedIn datasets, and Tesla beats the runner-up by more than 2 to 1

Count every mention of a major automaker's name across three LinkedIn datasets and one brand towers over the rest. **Tesla**, with 410 mentions in a 213,491-post dataset, 63 in a 49,369-post dataset, and 411 in a 77,969-record dataset. In two of the three files, that's more than double the next-closest competitor.

| Maker | podawaa2024 | HyperClapper | LinkBoost-2025 |
|---|---|---|---|
| Tesla | 410 | 63 | 411 |
| Ford | 159 | 23 | 66 |
| Mercedes(-Benz) | 130 | 22 | 44 |
| Audi | 87 | 5 | - |
| BMW | 81 | 16 | - |
| Toyota | 75 | 17 | 19 |

## The twist: in one dataset, Tesla isn't a car story at all

In LinkBoost-2025, Tesla's 411 mentions were checked directly against the actual post text, and the picture that emerged wasn't automotive. It was financial. The genuinely distinct posts behind those mentions include a JPMorgan analyst note on humanoid-robot stocks tied to Tesla, "should you buy a Tesla in cash" investment advice, general Musk and AI business commentary, and a Cathie Wood interview excerpt. Tesla on LinkedIn, in this dataset, is a stock-and-founder story, not a car story.

## Why this is worth checking before writing the headline

A blunter version of this piece would just report "Tesla dominates automotive discussion on LinkedIn" and stop there. That would flatten a real distinction. podawaa2024 and HyperClapper's Tesla mentions plausibly include genuine car-buyer and industry discussion. LinkBoost-2025's don't seem to, once actually read. Same word, same count method, structurally different content underneath.

## What this is, and isn't

**VERIFIED**, reproducible via the published scan: the mention counts in the table above.

**VERIFIED by manual check**: LinkBoost-2025's top repeated Tesla-mentioning strings are genuinely distinct finance and tech posts, not a duplicate-template artifact.

Full automaker breakdown: **github.com/DreamITSoftware/SPOTAPOD**.

<!-- export65-note -->
> **Update, 22 October 2026.** In the [65 export files](../provenance.md#the-65-export-files), 337 of 56,363 records (0.598%) name a car maker. Tesla leads with 149, then Ford 64, Toyota 40, BMW 30 and Volkswagen 24, so Tesla is ahead of the runner-up by about 2.3 to 1. The matches hold 326 distinct texts and the duplicate-template check did not fire. This project has not read the Tesla matches, so it does not know whether they are about cars or about finance, the distinction found in LinkBoost-2025. Detail: [car-maker content](../research/car-maker-content.md#the-65-export-files).

---

*Self-published. Not peer-reviewed. Independently reproducible from the source files.*
