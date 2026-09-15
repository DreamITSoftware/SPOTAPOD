# SPOTAPOD Analysis Repository

*Independent project, not officially affiliated with or endorsed by the
[PolymathWizard/SPOTAPOD](https://github.com/PolymathWizard/SPOTAPOD)
project — this repo takes structural cues from it (see the mirrored
top-level layout) but was built separately, from different source files,
and deliberately diverges on key points: no raw data included, no
per-author/per-record explorer (see [explorer/README.md](explorer/README.md)
and [docs/limitations.md](docs/limitations.md) for why).*

**A de-identified, aggregate-only companion analysis of three engagement-pod-adjacent datasets.**

All three datasets are described by their depositors/collectors as tied to
engagement-pod tooling — the kind of conduct addressed by
[16 CFR § 465.8, "Misuse of fake indicators of social media influence"](docs/regulatory-context.md),
part of the FTC's Trade Regulation Rule on the Use of Consumer Reviews and
Testimonials. See [docs/regulatory-context.md](docs/regulatory-context.md)
for the full rule text and what it does and doesn't cover — this repo makes
no legal determination that any account or record in any file violates it.

This repo does **not** name, hash-link-to-identity, or otherwise expose any individual
author, account, name, photo, or profile URL. It reports only population-level
statistics — distributions, ratios, timelines, and counts — computed directly from
the source files. No script in this repo can print an author identifier; the
identifier fields are used only as one-way SHA-256 hashes, in memory, to de-duplicate
authors for counting purposes, and are discarded immediately after.

See [docs/privacy.md](docs/privacy.md) for the full breakdown of what PII is in
these files and exactly how (and how not) this repo touches it.

If you are looking for a tool that names individual accounts, this isn't it, on purpose —
see [docs/limitations.md](docs/limitations.md) for why.

## What this covers

| Dataset | Records | Description |
|---|---|---|
| `podawaa2024.json` | 213,491 | LinkedIn post records (`linkedinPostId`, `Content`, `AuthorPublicIdentifier`, `Likes`, `Views`) |
| `HyperClaper.json` | 49,369 | Pod-app export: post metadata plus a reciprocal `like`/`comment` flag, and profile metadata (followers, premium/top-voice status) |
| `LinkBoost-2025.json` | 77,969 | Pod-service action log: one record per successful like/comment action against a target LinkedIn post, with the acting account's name/URN and the target post's URN |

Neither raw file is included in this repository — only [checksums](checksums/CHECKSUMS.txt),
scripts, and the aggregate output those scripts produce. Put your own copies of the
three files next to the scripts (or pass a path) to reproduce everything below.
See [docs/provenance.md](docs/provenance.md) for the reported source and
collection method for each file.

## File structures

Placeholder values only below — no real content, handle, or name from any
file appears here. Full field-by-field notes (types, completeness %, which
fields are read vs. never touched) are in [docs/data-dictionary.md](docs/data-dictionary.md);
formal JSON Schema is in [schema/](schema).

### podawaa2024.json

```json
{
  "Posts": [
    {
      "linkedinPostId": 1234567890123456789,
      "Content": "<post text>",
      "AuthorPublicIdentifier": "<linkedin-handle>",
      "Likes": 0,
      "Views": 0
    }
  ]
}
```

### HyperClaper.json

```json
{
  "data": {
    "post": [
      {
        "profile": {
          "name": "<name>",
          "linkedin_data": {
            "school": "",
            "skills": [],
            "company": "",
            "fullName": "<name>",
            "headline": "<headline>",
            "jobTitle": "",
            "location": "<location>",
            "companies": [],
            "followers": "<n> followers",
            "isPremium": false,
            "isTopVoice": false,
            "connections": "500",
            "description": "",
            "jobDescription": "",
            "profilePicture": "<url>",
            "public_identifier": "<linkedin-handle>",
            "linkedin_profile_id": "<internal id>",
            "linkedin_profile_link": "<url>"
          },
          "profile_picture": "<url>",
          "__typename": "profile"
        },
        "comment": true,
        "like": true,
        "post_url": "<url>",
        "created_at": "2026-01-01T00:00:00.000000+00:00",
        "id": "<uuid>",
        "post_title": "<post text>",
        "like_count": 0,
        "impression_count": 0,
        "comment_count": 0,
        "__typename": "post"
      }
    ]
  }
}
```

### LinkBoost-2025.json

```json
[
  {
    "Id": "<record id>",
    "FirstName": "<name>",
    "LastName": "<name>",
    "Occupation": "<headline>",
    "DashEntityUrn": "<internal urn>",
    "ObjectUrn": "urn:li:member:0000000000",
    "SuccessfullLikes": 0,
    "SuccessfullComments": 0,
    "piFirstName": "<name>",
    "piLastName": "<name>",
    "Comment": "<comment text>",
    "Url": "<url>",
    "liProfileLink": "<html anchor with profile urn + name>",
    "liUrl": "<html anchor with url>",
    "liDigitalMarketer": "Digital Marketer: <Lastname, Firstname>",
    "Title": "<target post text>",
    "VolumeId": 0,
    "UserId": "<operator account id>",
    "country": "<country>"
  }
]
```

## Data dictionary

Every "indicator of social media influence" field below (`Likes`, `Views`,
`like_count`, `impression_count`, `comment_count`, `followers`) falls within
the definition at 16 CFR § 465.1(j), which [16 CFR § 465.8](docs/regulatory-context.md)
covers — see that doc for the full rule text and what it requires beyond a
raw metric value.

### podawaa2024.json

Top level: `{"Posts": [ ... ]}`

| Field | Type | Completeness | Notes |
|---|---|---|---|
| `linkedinPostId` | int | 98.4% | Snowflake-style ID; encodes an approximate post timestamp (see [method](docs/method.md)) |
| `Content` | string | 99.7% | Raw post text. Placeholder strings such as `"This post has no content"` / `"postNoContent"` indicate the pipeline that produced this dataset couldn't retrieve real content, not that the post was actually empty |
| `AuthorPublicIdentifier` | string | 88.8% | LinkedIn's public profile slug. **Never printed by any script in this repo** — hashed in memory only |
| `Likes` | int | 100.0% | As recorded at collection time |
| `Views` | int | 100.0% | As recorded at collection time; 44.3% of records show 0, which is a data-completeness gap, not necessarily zero actual views (see [limitations](docs/limitations.md)) |

### HyperClaper.json

Top level: `{"data": {"post": [ ... ]}}`

| Field | Type | Completeness | Notes |
|---|---|---|---|
| `profile.name` | string | — | Author display name. **Never printed by any script in this repo** |
| `profile.linkedin_data.public_identifier` | string | — | LinkedIn slug. Hashed in memory only |
| `profile.linkedin_data.followers` | string (e.g. `"5,381 followers"`) | — | Parsed to int for aggregate stats only |
| `profile.linkedin_data.isPremium` / `isTopVoice` | bool | — | Account status flags |
| `profile.linkedin_data.linkedin_profile_link` / `linkedin_profile_id` | string / string | — | **Never read by any script in this repo except for hashing `public_identifier`** |
| `profile.profile_picture` | URL | — | **Never read by any script in this repo** |
| `comment` | bool | 100.0% | Whether a reciprocal comment action was recorded for this post via the pod tool |
| `like` | bool | 100.0% | Whether a reciprocal like action was recorded for this post via the pod tool |
| `post_url` | URL | 100.0% | Link to the LinkedIn post itself |
| `created_at` | ISO 8601 timestamp | 100.0% | When this record was captured, not necessarily the post's original publish date |
| `post_title` | string | 98.8% | Post text/caption |
| `like_count` / `impression_count` / `comment_count` | int | 15.3% / 2.0% / 15.1% | Sparse — only populated for a minority of records |

### LinkBoost-2025.json

Top level: `[ ... ]` (flat array, no wrapper object)

| Field | Type | Completeness | Notes |
|---|---|---|---|
| `Id` | string | 100.0% | Internal record ID |
| `FirstName` / `LastName` | string | 96.0–96.1% | Real name. **Never printed by any script in this repo** |
| `piFirstName` / `piLastName` | string | 100.0% | Duplicate of FirstName/LastName, always present. **Never printed by any script in this repo** |
| `Occupation` | string | 96.1% | LinkedIn-style headline/bio — a quasi-identifier on its own |
| `DashEntityUrn` | string | 96.1% | LinkedIn internal profile URN. **Never read by any script in this repo** |
| `ObjectUrn` | string | 100.0% | LinkedIn member URN identifying the target post/author (469 unique). Hashed in memory only |
| `SuccessfullLikes` / `SuccessfullComments` | int | 100.0% | Count of successful pod actions recorded for this record (min 2 / min 1, max 261 / max 133) |
| `Comment` | string | 99.9% | Comment text posted as part of the pod action |
| `Url` | string | 100.0% | Link to the target LinkedIn post |
| `liProfileLink` | string (HTML) | 96.1% | Anchor tag embedding a profile URN and a "Digital Marketer: Lastname, Firstname" label. **Never read by any script in this repo** |
| `liUrl` / `liDigitalMarketer` | string | 100.0% | Related HTML/label fields. **Never read by any script in this repo** |
| `Title` | string | 99.6% | Target post's content |
| `VolumeId` | int | 100.0% | Batch identifier — only 1 unique value across the whole file |
| `UserId` | string | 100.0% | LinkBoost operator/account ID (238 unique — not a LinkedIn ID). Hashed in memory only |
| `country` | string | 60.5% | Reported country (22 unique) — a quasi-identifier in combination with other fields |

Fields not covered by scripts beyond hashing/counting as noted above are
internal/structural and carry no additional identity risk beyond what's
already flagged — this includes `id` and `__typename` in HyperClaper.json.

## Reproduce the baseline

```bash
# Verify your local copies match what was analyzed here
sha256sum podawaa2024.json HyperClaper.json LinkBoost-2025.json
# compare against checksums/CHECKSUMS.txt

# Validate structure/types before trusting the numbers below (Python or C#)
python3 tools/validate.py podawaa /path/to/podawaa2024.json --checksums checksums/CHECKSUMS.txt
python3 tools/validate.py hyperclapper /path/to/HyperClaper.json --checksums checksums/CHECKSUMS.txt
python3 tools/validate.py linkboost /path/to/LinkBoost-2025.json --checksums checksums/CHECKSUMS.txt
# or: cd tools/csharp && dotnet run -- podawaa /path/to/podawaa2024.json

# Aggregate profiles (no identities printed)
python3 analysis/profile_podawaa.py /path/to/podawaa2024.json
python3 analysis/profile_hyperclapper.py /path/to/HyperClaper.json
python3 analysis/profile_linkboost.py /path/to/LinkBoost-2025.json

# Cross-author duplicate-content clustering (sizes only, never author lists)
python3 analysis/duplicate_content.py /path/to/podawaa2024.json --min-authors 2

# Aggregate signal counts for other regulated content categories (no identities)
python3 analysis/regulatory_category_scan.py podawaa /path/to/podawaa2024.json
python3 analysis/regulatory_category_scan.py hyperclapper /path/to/HyperClaper.json
python3 analysis/regulatory_category_scan.py linkboost /path/to/LinkBoost-2025.json

# Aggregate geography and occupation-category breakdown (no protected demographics)
python3 analysis/demographics_scan.py hyperclapper /path/to/HyperClaper.json
python3 analysis/demographics_scan.py linkboost /path/to/LinkBoost-2025.json

# Aggregate book-promotion genre breakdown (no identities)
python3 analysis/book_genre_scan.py podawaa /path/to/podawaa2024.json
python3 analysis/book_genre_scan.py hyperclapper /path/to/HyperClaper.json
python3 analysis/book_genre_scan.py linkboost /path/to/LinkBoost-2025.json

# Career-advice content comparison across all three datasets (no identities)
python3 analysis/career_advice_scan.py podawaa /path/to/podawaa2024.json
python3 analysis/career_advice_scan.py hyperclapper /path/to/HyperClaper.json
python3 analysis/career_advice_scan.py linkboost /path/to/LinkBoost-2025.json

# Mutually exclusive topic taxonomy + recurring-pattern decision points (no identities)
python3 analysis/topic_taxonomy.py /path/to/podawaa2024.json /path/to/HyperClaper.json /path/to/LinkBoost-2025.json
python3 analysis/category_title_patterns.py /path/to/podawaa2024.json /path/to/HyperClaper.json /path/to/LinkBoost-2025.json

# Regenerate every chart in figures/
python3 figures/generate_figures.py /path/to/podawaa2024.json /path/to/HyperClaper.json --linkboost-path /path/to/LinkBoost-2025.json --outdir figures
```

All scripts are Python 3 standard library, except `figures/generate_figures.py`
which additionally needs `matplotlib`.

## Headline figures

### podawaa2024

- 213,491 records across 7,033 unique author identifiers (hashed count only)
- 44.3% of records carry zero `Views`; 36.5% show more `Likes` than `Views`
- Decoded post dates span 2018–2024 (decoded from the Snowflake-style post ID — see [method](docs/method.md))
- 28,254 records share exact-match `Content` with at least one other record; the most repeated string appears 3,918 times
- The top 1% of authors (by hashed post count) account for 19.1% of all posts; the top 10% account for 61.9%

### HyperClapper

- 49,369 records across 702 unique author identifiers (hashed count only)
- 68.6% of records carry both `like=true` and `comment=true` — the reciprocal-exchange signature the app itself recorded
- 98.0% of records carry zero recorded impressions, so like/impression ratios are only meaningful for the remaining 2%
- Volume is heavily concentrated in mid-to-late 2025 through mid-2026 (see [fig6](figures/fig6-hyperclapper-timeline.png))
- The top 10% of authors (by hashed post count) account for 73.5% of posts

Full output: [docs/research/baseline-profile.md](docs/research/baseline-profile.md).

### LinkBoost-2025

- 77,969 records across 469 unique target posts and 238 unique operator accounts (hashed counts only)
- `SuccessfullLikes` ranges 2–261 (mean 171.2); `SuccessfullComments` ranges 1–133 (mean 47.5) per record
- 39.5% of records carry no reported `country`; of the rest, the US (21.8%), India (15.6%), and UK (8.0%) lead
- The top 1% of target posts (by hashed record count) account for 18.9% of all records; the top 10% account for 58.2%
- The top 10% of operator accounts (by hashed record count) account for 53.0% of all records
- 76,532 records share exact-match target-post `Title` with at least one other record — expected, since 77,969 records span only 469 distinct target posts

## Evidence discipline

Every figure above is **VERIFIED** — computed directly from the source file, reproducible
by anyone who runs the scripts against their own copy. The interpretation of *why* a
record shows this pattern (bot traffic, tracking pipeline gaps, genuine pod activity,
crawler noise) is **not** verifiable from the records alone — see
[docs/limitations.md](docs/limitations.md).

## Explorer

`explorer/index.html` is a static, offline dashboard of the same aggregate
figures as above, laid out for browsing — open it directly in a browser,
no server or build step required. It deliberately does **not** replicate
SPOTAPOD's per-author explorer (no search, no filter, no click-to-focus,
no per-record data). See [explorer/README.md](explorer/README.md) for why.

## Docs

- [Provenance](docs/provenance.md) — reported source and collection method for each file, the Dataverse citation for `podawaa2024.json`, and why this repo doesn't take a position on ToS compliance
- [Regulatory context](docs/regulatory-context.md) — full text of 16 CFR § 465.8 and what it does/doesn't require
- [Other regulatory signals](docs/research/other-regulatory-signals.md) — aggregate, keyword-based signal counts for categories beyond § 465.8, and why they're signals rather than findings
- [Audience impact](docs/research/audience-impact.md) — inferred, category-level downstream risk to readers from inflated social proof, not a measured outcome
- [Algorithm/creator-strategy advice case study](docs/research/algorithm-strategy-advice.md) — a genre-level (not report-specific) illustration of the same mechanism applied to platform-strategy content
- [Book-promotion content](docs/research/book-promotion-content.md) — aggregate genre breakdown of book-promotion language across all three datasets
- [Career-advice comparison](docs/research/career-advice-comparison.md) — side-by-side methodology/findings/limitations table across all three datasets
- [Topic taxonomy](docs/research/topic-taxonomy.md) — nine mutually exclusive content categories covering all 340,829 records, with per-dataset breakdown
- [Decision points](docs/research/decision-points.md) — maps each category to the real-world decision its recurring content templates are aimed at, grounded in actual duplicated title patterns
- [Demographics](docs/research/demographics.md) — aggregate geography and stated-occupation-category breakdown, and why protected characteristics (race, gender, age, etc.) are never inferred
- [Method](docs/method.md) — how each figure is computed
- [Data dictionary](docs/data-dictionary.md) — same content as the [Data dictionary](#data-dictionary) section above, kept as a standalone page for cross-linking from other docs
- [Privacy and PII](docs/privacy.md) — what personal data is in these files and exactly how this repo does and doesn't touch it
- [Limitations](docs/limitations.md) — why this repo stops at aggregates, and what individual-level claims it deliberately does not make
- [Validation tools](tools/README.md) — Python and C# structural/type validators, plus known data-quality findings
- [Schemas](schema) — reference JSON Schema for all three file formats

## Other regulatory signals

Beyond 16 CFR § 465.8, `analysis/regulatory_category_scan.py` reports
aggregate, keyword-based signal counts for content categories that could
intersect with other rules — health/medical claims, financial/investment
claims, professional-licensing language, and endorsement-disclosure gaps.
No record, author, or occupation is ever identified by this script; it
reports population-level percentages only. Full methodology, results
table, and why these are signals rather than findings:
[docs/research/other-regulatory-signals.md](docs/research/other-regulatory-signals.md).

For what those categories could mean for the people who *saw* this
content — not the accounts that posted it — see
[docs/research/audience-impact.md](docs/research/audience-impact.md), an INFERENCE-tier
discussion of plausible downstream harm from inflated social proof, not a
measurement of any actual outcome.

## Demographics

`analysis/demographics_scan.py` aggregates the only demographic-adjacent
fields that actually exist in these files — self-reported location/country
and stated occupation/headline text — into population-level percentages.
It does **not** infer race, ethnicity, gender, age, or any other protected
characteristic from names or photos; that data isn't stated anywhere in
these files and this repo doesn't guess it. See
[docs/research/demographics.md](docs/research/demographics.md) for the full breakdown, scope
statement, and caveats.

## Book-promotion content

`analysis/book_genre_scan.py` checks for book-promotion language across
all three datasets and breaks matches down by genre. Book promotion is a
small minority everywhere (0.26–0.98% of records), dominated by
business/entrepreneurship and "writing craft" categories. Full breakdown:
[docs/research/book-promotion-content.md](docs/research/book-promotion-content.md).

## Career-advice content comparison

`analysis/career_advice_scan.py` checks for career-advice language
(resume, interview prep, promotion, networking, layoffs, etc.) across all
three datasets. HyperClaper leads by a wide margin (16.52%), aligning with
its occupation skew and reciprocal-engagement rate; podawaa2024 is lowest
(4.45%); LinkBoost-2025 sits in between (6.68%) but reflects pod-activity
volume on a small number of target posts rather than distinct content
volume. Full methodology, side-by-side table, and caveats:
[docs/research/career-advice-comparison.md](docs/research/career-advice-comparison.md).

## Topic taxonomy and decision points

`analysis/topic_taxonomy.py` assigns every record across all three
datasets to exactly one of nine mutually exclusive content categories
(plus a catch-all). Headline: `technology_ai` (20.11%) and
`uncategorized_other` (42.97%) dominate overall; HyperClaper skews
sharply toward `career_job_search` (13.92%) and LinkBoost-2025 toward
`leadership_coaching_motivation` (18.91%). Full results:
[docs/research/topic-taxonomy.md](docs/research/topic-taxonomy.md).

`analysis/category_title_patterns.py` finds the recurring (never one-off)
title templates within each category, and
[docs/research/decision-points.md](docs/research/decision-points.md) maps
each category to the real-world decision its dominant template is
plausibly aimed at — e.g. `career_job_search`'s top template (533
occurrences) pushes an "AI resume rewrite" narrative.

## Citations

`podawaa2024.json` (CORROBORATED via matching sha256 — see
[docs/provenance.md](docs/provenance.md#citations)):

> Hall, Daniel. "LinkedIn posts using fake socials." Harvard Dataverse, 2026.
> `doi:10.7910/DVN/WD9AUR`
> https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/WD9AUR

`HyperClaper.json` has no Dataverse citation — nothing ties this file to
that DOI. See [docs/provenance.md](docs/provenance.md#citations) for why
it isn't cited there and where it's reported to come from instead.

`LinkBoost-2025.json` has no citation either — its source hasn't been
confirmed yet (see [docs/provenance.md](docs/provenance.md)).

## License

Code and schemas: MIT (see [LICENSE](LICENSE)). Documentation: CC BY 4.0
(see [LICENSE-CONTENT](LICENSE-CONTENT)). The underlying datasets are not
included and are governed by whatever terms apply to your copies of them.
See [CITATION.cff](CITATION.cff) for how to cite this repo, and
[docs/provenance.md](docs/provenance.md) for how to cite the datasets
themselves.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for the hard rules every change has
to pass — no raw data, no printable identifiers, no per-entity lookup, no
unearned evidence tiers, no legal conclusions asserted as fact, no
inferred protected characteristics. Run `python3 -m unittest discover -s
tests -v` before submitting anything (see [tests/README.md](tests/README.md)).
[CHANGELOG.md](CHANGELOG.md) tracks what's been added and, just as
importantly, what's been declined and why.
