# Topic taxonomy (mutually exclusive categorization)

`analysis/topic_taxonomy.py` assigns every record across all three datasets
to exactly one of nine content categories, using priority-ordered keyword
pattern matching (first matching category wins, so categories never
overlap). Anything matching none of the nine falls into a tenth catch-all,
`uncategorized_other`. Same discipline as every other scan in this repo:
counts and percentages only, no record or author identified.

## Method

Unlike the earlier category scans in this repo (`other-regulatory-signals.md`,
`book-promotion-content.md`, `career-advice-comparison.md`), which let a
record match more than one category, this taxonomy is **mutually
exclusive by construction**, each record is tested against the nine
categories in a fixed order and assigned to the first one that matches.
This trades some nuance (a record that's genuinely about both career
advice and AI only gets counted once, under whichever category is
checked first) for a property the earlier scans don't have: every record
in every dataset is accounted for in exactly one bucket, so the counts
below sum to the full 340,829-record total across all three files.

## Results (VERIFIED, reproducible via the script)

| Category | Records | % of all 340,829 |
|---|---|---|
| `uncategorized_other` | 146,442 | 42.97% |
| `technology_ai` | 68,526 | 20.11% |
| `leadership_coaching_motivation` | 30,907 | 9.07% |
| `finance_investing` | 29,638 | 8.70% |
| `marketing_sales_branding` | 20,491 | 6.01% |
| `business_entrepreneurship` | 18,853 | 5.53% |
| `career_job_search` | 14,588 | 4.28% |
| `health_wellness_fitness` | 6,481 | 1.90% |
| `education_certification` | 3,404 | 1.00% |
| `book_writing_publishing` | 1,499 | 0.44% |

### Per-dataset breakdown

| Category | podawaa2024 | HyperClapper | LinkBoost-2025 |
|---|---|---|---|
| `career_job_search` | 2.23% | **13.92%** | 3.79% |
| `technology_ai` | 16.39% | 27.97% | 25.29% |
| `finance_investing` | 9.18% | 5.88% | 9.15% |
| `health_wellness_fitness` | 1.38% | 1.75% | 3.44% |
| `leadership_coaching_motivation` | 6.15% | 6.16% | **18.91%** |
| `marketing_sales_branding` | 6.99% | 3.13% | 5.16% |
| `business_entrepreneurship` | 6.39% | 3.24% | 4.62% |
| `education_certification` | 0.63% | 3.11% | 0.68% |
| `book_writing_publishing` | 0.19% | 0.91% | 0.82% |
| `uncategorized_other` | 50.47% | 33.93% | 28.15% |

Two standouts, consistent with earlier findings elsewhere in this repo:
HyperClapper is disproportionately career-content (13.92% vs. 2–4%
elsewhere, see also the reciprocal-engagement and occupation findings in
[demographics.md](demographics.md)), and LinkBoost-2025 is disproportionately
leadership/coaching content (18.91% vs. ~6% elsewhere), matching its
occupation text skewing 59.5% toward "executive/leadership/coaching" per
[demographics.md](demographics.md).

## Reading `uncategorized_other`

At 42.97%, this is the largest single bucket: expected, since nine
keyword-based categories can't exhaustively cover the full range of
professional-networking content (personal announcements, engagement-bait
questions, congratulations posts, industry commentary with no category
keyword, etc.). This bucket is a catch-all by construction, not a finding
in itself. It's too heterogeneous to characterize as a topic the way the
other nine can be.

## Caveats

Same as every other content scan in this repo: keyword matching is blunt,
a record's category assignment depends on which pattern happens to match
first (priority order is a modeling choice, not a ground truth), and no
claim is made about any specific record, author, or the accuracy of any
matched content. See [other-regulatory-signals.md](other-regulatory-signals.md)
for the fuller version of this caveat, which applies here identically.

<!-- export65-section -->
## The 65 export files

Added 22 October 2026. `analysis/topic_taxonomy.py` takes an optional `--export65 /path/to/folder_with_the_65_files` and prints one more block, run separately. The 65 files are not added to the 340,829-record totals above, and nothing above this heading has changed. The classification is the same: each of the 56,363 distinct records goes to the first category whose patterns match its post text, and a record with no post text falls in `uncategorized_other`. The three-dataset figures that this run printed match the table above. The 65 files are a separate set (see [provenance.md](../provenance.md#the-65-export-files) and [export-65-profile.md](export-65-profile.md)).

```text
65 export files, run separately (not included in the totals above)
Records: 56,363
career_job_search                  3,370  ( 5.98% of the 65 export files)
book_writing_publishing              254  ( 0.45% of the 65 export files)
education_certification              750  ( 1.33% of the 65 export files)
technology_ai                     14,713  (26.10% of the 65 export files)
finance_investing                  6,002  (10.65% of the 65 export files)
health_wellness_fitness            2,273  ( 4.03% of the 65 export files)
leadership_coaching_motivation     4,569  ( 8.11% of the 65 export files)
marketing_sales_branding           2,444  ( 4.34% of the 65 export files)
business_entrepreneurship          2,746  ( 4.87% of the 65 export files)
uncategorized_other               19,242  (34.14% of the 65 export files)
```

Technology and AI is the largest named category in the 65 files (26.10%), as it is in each of the other three datasets. Finance and investing is second (10.65%), then leadership, coaching and motivation (8.11%) and career and job search (5.98%). The career and job search share is below HyperClapper (13.92%) and above podawaa2024 (2.23%) and LinkBoost-2025 (3.79%). 34.14% of the 65 files' records fall in no category, against 50.47% (podawaa2024), 33.93% (HyperClapper) and 28.15% (LinkBoost-2025). The categories are keyword signals in priority order, as the caveats above explain, and not verified topic labels.
