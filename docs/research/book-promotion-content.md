# Book-promotion content (aggregate, keyword-based)

`analysis/book_genre_scan.py` checks post/comment content across all three
datasets for book-promotion language ("my new book," "pre-order,"
"bestseller," "grab your copy," etc.), then breaks matching records down
by a secondary set of genre-keyword categories. Same discipline as
[other-regulatory-signals.md](other-regulatory-signals.md): counts and
percentages only, no matched text or record identified.

## Results (VERIFIED — reproducible via the script)

| Dataset | Records scanned | Book-promotion matches |
|---|---|---|
| podawaa2024 | 213,491 | 559 (0.26%) |
| HyperClaper | 49,369 | 478 (0.97%) |
| LinkBoost-2025 | 77,969 | 767 (0.98%) |

### Genre breakdown (% of that dataset's book-promotion records; a record can match more than one genre)

| Genre | podawaa2024 | HyperClaper | LinkBoost-2025 |
|---|---|---|---|
| business_entrepreneurship | 35.2% | 49.2% | 32.5% |
| writing_craft | 22.0% | 51.0% | 24.4% |
| technology_ai | 21.5% | 21.3% | 40.0% |
| career_sales_marketing | 13.8% | 12.3% | 12.9% |
| finance_investing | 13.6% | 13.0% | 11.2% |
| self_help_personal_dev | 10.4% | 50.2% | — |
| parenting_relationships | 7.0% | 8.8% | 8.7% |
| health_wellness_fitness | 4.7% | 3.8% | 1.3% |
| spiritual_religious | 3.2% | 4.2% | 3.5% |
| childrens_book | — | 5.2% | — |
| memoir_biography | 2.0% | 1.7% | — |
| fiction_novel | 1.6% | 1.3% | 7.4% |
| poetry | 0.9% | — | — |
| uncategorized | 23.8% | 11.5% | 15.5% |

## Reading these numbers

- **Book promotion is a small minority in all three files** — under 1%
  each. It's present, but it doesn't characterize these datasets.
- **Business/entrepreneurship and "writing craft" dominate across all
  three**, which is consistent with LinkedIn's overall content mix
  (professional self-promotion) rather than anything distinctive to
  pod-engagement content specifically.
- **Fiction, poetry, and children's books are minor everywhere** — expected
  on a professional-networking platform.
- Same caveats as [other-regulatory-signals.md](other-regulatory-signals.md):
  keyword matching is blunt, a record can double-count across genres, and
  no claim is made about any specific record, author, or actual book.
