# Dataset comparison: career-advice content

`analysis/career_advice_scan.py` checks post/comment content across all
three datasets for career-advice language (resume/CV, job search,
interview prep, promotion, networking, layoffs, personal branding, etc.).
This page compares methodology, findings, and limitations across the
three files specifically through that lens. Same discipline as
[book-promotion-content.md](book-promotion-content.md) and
[other-regulatory-signals.md](other-regulatory-signals.md): counts and
percentages only, no matched text or record identified.

## Comparison table

| | **podawaa2024** | **HyperClapper** | **LinkBoost-2025** |
|---|---|---|---|
| **Records** | 213,491 | 49,369 | 77,969 |
| **Content field scanned** | `Content` | `post_title` | `Title` |
| **Career-advice keyword matches** | 9,492 (4.45%) | 8,157 (16.52%) | 5,208 (6.68%) |
| **Methodology** | Keyword/phrase regex match against raw post text; whole-file scan, no sampling | Same pattern set against post title text only | Same pattern set against target-post `Title`; 469 unique target posts drive 77,969 records, so this measures engagement-pod activity repeated across many records, not 77,969 distinct pieces of content |
| **Occupation cross-reference available?** | No, no occupation/headline field exists in this file | Yes, `linkedin_data.headline`/`jobTitle`; "executive_leadership_coaching" (23.0%) overlaps with career-advice framing (see [demographics.md](demographics.md)) | Yes, `Occupation`; "executive_leadership_coaching" dominates at 59.5% of occupation text, the highest of any dataset |
| **Reciprocal-engagement context** | N/A, no like/comment reciprocity flag in schema | 68.6% of records show `like=true` + `comment=true` together | N/A, every record here is by definition pod-driven activity (`SuccessfullLikes`/`SuccessfullComments`) on some target post |
| **Findings** | Lowest prevalence of the three (4.45%), a minority even relative to this dataset's other content patterns | Highest prevalence by a wide margin (16.52%), nearly 1 in 6 records touches career-advice language, consistent with this dataset's occupation skew toward marketing/leadership-coaching profiles | Middle prevalence (6.68%); combined with 59.5% "executive/leadership/coaching" occupation text, pod activity here appears concentrated on a small number of career-coaching-style target posts (469 unique targets total) rather than spread broadly |
| **Limitations specific to career-advice reading** | No occupation field means matches can't be cross-checked against who's posting, "promotion" could mean career promotion or a marketing promotion, with no way to tell which | `post_title` may be truncated/partial depending on how the export captured it; occupation category is self-reported and unverified | 77,969 records map to only 469 unique posts; the 6.68% match rate reflects ~31 distinct target posts repeated at scale, not 5,208 independently-authored pieces of content |

## Reading these numbers

- **Record-level percentages measure different things across files.**
  podawaa2024 and HyperClapper approximate "how much distinct content
  touches career advice." LinkBoost-2025 instead measures "how much
  engagement-pod activity volume is directed at career-advice-adjacent
  posts", the same percentage means something structurally different
  because of the 469-unique-posts-to-77,969-records ratio. Treat
  cross-dataset percentage comparisons with that distinction in mind.
- **Three independent signals point the same direction for HyperClapper**:
  highest career-advice content rate (16.52%), highest reciprocal-
  engagement rate (68.6%), and highest self-help/leadership occupation
  skew (see [demographics.md](demographics.md)). Three aligned signals is
  a stronger pattern than any one alone, though still INFERENCE-tier for
  any claim about *why* they align, see the caveats below.
- **Keyword matching is blunt**, same caveat as every other content scan
  in this repo: a match on "promotion" could mean career promotion or a
  marketing promotion; "layoff" could be advice content or someone
  sharing personal news, not necessarily "advice." No claim is made about
  any specific record, author, or the actual quality/accuracy of any
  matched content.
- **Evidence tier**: VERIFIED for the raw counts (reproducible from the
  checksummed files via `analysis/career_advice_scan.py`); INFERENCE for
  any claim about why career-advice prevalence correlates with a
  dataset's other patterns.

See also [algorithm-strategy-advice.md](algorithm-strategy-advice.md) for
the related (but distinct) case study on platform-strategy advice content,
and [audience-impact.md](audience-impact.md) for the general mechanism by
which inflated engagement could affect readers who trust this kind of
content.

<!-- export65-section -->
## The 65 export files

Added 22 October 2026. This is the same scan run on the 65 export files: 56,363 distinct records after the files are de-duplicated on record id, reading each record's `title` field, which holds the post text. These files are a separate set from the three datasets above, and nothing above this heading has changed. Their source, method and limits are in [provenance.md](../provenance.md#the-65-export-files) and [export-65-profile.md](export-65-profile.md). Rates use all 56,363 records as the denominator, and 237 of them have no post text. Command: `python3 analysis/career_advice_scan.py export65 /path/to/folder_with_the_65_files`.

```text
============================================================
EXPORT65: CAREER-ADVICE CONTENT SCAN (aggregate, de-identified)
============================================================
Total records scanned: 56,363
Records matching career-advice language: 4,723 (8.38%)

Reminder: keyword-pattern SIGNAL, not verified topic classification.
No record, author, or matched text is identified by this script.
```

4,723 of 56,363 records (8.38%) match the career-advice patterns. The three datasets above give 4.45% (podawaa2024), 16.52% (HyperClapper) and 6.68% (LinkBoost-2025), so the 65 export files sit at the second highest of the four. The 65 files carry no occupation or headline field and no like or comment flag, so the occupation cross-reference and the reciprocal-engagement row of the table above have no counterpart for them.

The rates come from different fields and different kinds of record, so a gap between them describes the files and does not describe the tools. A match is a keyword in the text, not a finding about the post or its author.
