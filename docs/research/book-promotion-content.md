# Book-promotion content (aggregate, keyword-based)

`analysis/book_genre_scan.py` checks post/comment content across all three
datasets for book-promotion language ("my new book," "pre-order,"
"bestseller," "grab your copy," etc.), then breaks matching records down
by a secondary set of genre-keyword categories. Same discipline as
[other-regulatory-signals.md](other-regulatory-signals.md): counts and
percentages only, no matched text or record identified.

## Results (VERIFIED, reproducible via the script)

| Dataset | Records scanned | Book-promotion matches |
|---|---|---|
| podawaa2024 | 213,491 | 559 (0.26%) |
| HyperClapper | 49,369 | 478 (0.97%) |
| LinkBoost-2025 | 77,969 | 767 (0.98%) |

### Genre breakdown (% of that dataset's book-promotion records; a record can match more than one genre)

| Genre | podawaa2024 | HyperClapper | LinkBoost-2025 |
|---|---|---|---|
| business_entrepreneurship | 35.2% | 49.2% | 32.5% |
| writing_craft | 22.0% | 51.0% | 24.4% |
| technology_ai | 21.5% | 21.3% | 40.0% |
| career_sales_marketing | 13.8% | 12.3% | 12.9% |
| finance_investing | 13.6% | 13.0% | 11.2% |
| self_help_personal_dev | 10.4% | 50.2% | N/A |
| parenting_relationships | 7.0% | 8.8% | 8.7% |
| health_wellness_fitness | 4.7% | 3.8% | 1.3% |
| spiritual_religious | 3.2% | 4.2% | 3.5% |
| childrens_book | N/A | 5.2% | N/A |
| memoir_biography | 2.0% | 1.7% | N/A |
| fiction_novel | 1.6% | 1.3% | 7.4% |
| poetry | 0.9% | N/A | N/A |
| uncategorized | 23.8% | 11.5% | 15.5% |

## Reading these numbers

- **Book promotion is a small minority in all three files**, under 1%
  each. It's present, but it doesn't characterize these datasets.
- **Business/entrepreneurship and "writing craft" dominate across all
  three**, which is consistent with LinkedIn's overall content mix
  (professional self-promotion) rather than anything distinctive to
  pod-engagement content specifically.
- **Fiction, poetry, and children's books are minor everywhere**, expected
  on a professional-networking platform.
- Same caveats as [other-regulatory-signals.md](other-regulatory-signals.md):
  keyword matching is blunt, a record can double-count across genres, and
  no claim is made about any specific record, author, or actual book.

<!-- export65-section -->
## The 65 export files

Added 22 October 2026. This is the same scan run on the 65 export files: 56,363 distinct records after the files are de-duplicated on record id, reading each record's `title` field, which holds the post text. These files are a separate set from the three datasets above, and nothing above this heading has changed. Their source, method and limits are in [provenance.md](../provenance.md#the-65-export-files) and [export-65-profile.md](export-65-profile.md). Rates use all 56,363 records as the denominator, and 237 of them have no post text. Command: `python3 analysis/book_genre_scan.py export65 /path/to/folder_with_the_65_files`.

```text
============================================================
EXPORT65: BOOK-PROMOTION GENRE SCAN (aggregate, de-identified)
============================================================
Total records scanned: 56,363
Records matching book-promotion language: 289 (0.51%)

Genre breakdown (of book-promotion records; a record can match
more than one genre, so percentages don't sum to 100%):
  business_entrepreneurship    148 (51.2%)
  self_help_personal_dev       28 (9.7%)
  career_sales_marketing       56 (19.4%)
  finance_investing            71 (24.6%)
  health_wellness_fitness      18 (6.2%)
  memoir_biography             3 (1.0%)
  fiction_novel                5 (1.7%)
  poetry                       3 (1.0%)
  spiritual_religious          5 (1.7%)
  technology_ai                148 (51.2%)
  parenting_relationships      20 (6.9%)
  writing_craft                103 (35.6%)
  uncategorized                18 (6.2%)

Reminder: keyword-pattern SIGNALS, not verified genre classification.
No record, author, or matched text is identified by this script.
```

289 of 56,363 records (0.51%) match book-promotion language. The three datasets above give 0.26% (podawaa2024), 0.97% (HyperClapper) and 0.98% (LinkBoost-2025), so the 65 export files sit at the second lowest of the four. Among the 289, business and entrepreneurship and technology and AI each match 51.2%, writing craft 35.6%, finance and investing 24.6% and career, sales and marketing 19.4%. A record can match more than one genre. The technology and AI share is higher than in any of the three datasets above (21.5%, 21.3% and 40.0%).

The rates come from different fields and different kinds of record, so a gap between them describes the files and does not describe the tools. A match is a keyword in the text, not a finding about the post or its author.
