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

# Simple job-title keyword aggregate (no names, no full bios)
python3 analysis/simple_title_aggregate.py hyperclapper /path/to/HyperClaper.json
python3 analysis/simple_title_aggregate.py linkboost /path/to/LinkBoost-2025.json

# Entity mentions: news outlets, magazines, TV/streaming, corporations (no identities)
python3 analysis/entity_mention_scan.py podawaa /path/to/podawaa2024.json --category all
python3 analysis/entity_mention_scan.py hyperclapper /path/to/HyperClaper.json --category all
python3 analysis/entity_mention_scan.py linkboost /path/to/LinkBoost-2025.json --category all

# Law-related content: narrow (legal profession) vs. broader (compliance, legislation, IP)
python3 analysis/law_content_scan.py podawaa /path/to/podawaa2024.json
python3 analysis/law_content_scan.py hyperclapper /path/to/HyperClaper.json
python3 analysis/law_content_scan.py linkboost /path/to/LinkBoost-2025.json

# Speaker / thought leader aggregate (no names, no full bios)
python3 analysis/speaker_thought_leader_scan.py hyperclapper /path/to/HyperClaper.json
python3 analysis/speaker_thought_leader_scan.py linkboost /path/to/LinkBoost-2025.json

# Nonprofit-related content, with automatic duplicate-template detection
python3 analysis/nonprofit_content_scan.py podawaa /path/to/podawaa2024.json
python3 analysis/nonprofit_content_scan.py hyperclapper /path/to/HyperClaper.json
python3 analysis/nonprofit_content_scan.py linkboost /path/to/LinkBoost-2025.json

# Investment/VC content, with duplicate-template detection
python3 analysis/investment_vc_scan.py podawaa /path/to/podawaa2024.json
python3 analysis/investment_vc_scan.py hyperclapper /path/to/HyperClaper.json
python3 analysis/investment_vc_scan.py linkboost /path/to/LinkBoost-2025.json

# Cybersecurity content vs. engagement anomalies (podawaa2024, HyperClapper only)
python3 analysis/cybersecurity_anomaly_scan.py podawaa /path/to/podawaa2024.json
python3 analysis/cybersecurity_anomaly_scan.py hyperclapper /path/to/HyperClaper.json

# Travel agencies and destinations, with duplicate-template and language-artifact notes
python3 analysis/travel_content_scan.py podawaa /path/to/podawaa2024.json
python3 analysis/travel_content_scan.py hyperclapper /path/to/HyperClaper.json
python3 analysis/travel_content_scan.py linkboost /path/to/LinkBoost-2025.json

# National security / NSA content, with duplicate-template detection
python3 analysis/national_security_scan.py podawaa /path/to/podawaa2024.json
python3 analysis/national_security_scan.py hyperclapper /path/to/HyperClaper.json
python3 analysis/national_security_scan.py linkboost /path/to/LinkBoost-2025.json

# Homelessness-related content, narrow vs. broad
python3 analysis/homelessness_content_scan.py podawaa /path/to/podawaa2024.json
python3 analysis/homelessness_content_scan.py hyperclapper /path/to/HyperClaper.json
python3 analysis/homelessness_content_scan.py linkboost /path/to/LinkBoost-2025.json

# Pharma / biotech content, with content-cluster verification
python3 analysis/pharma_content_scan.py podawaa /path/to/podawaa2024.json
python3 analysis/pharma_content_scan.py hyperclapper /path/to/HyperClaper.json
python3 analysis/pharma_content_scan.py linkboost /path/to/LinkBoost-2025.json

# Political party / Trump content
python3 analysis/political_content_scan.py podawaa /path/to/podawaa2024.json
python3 analysis/political_content_scan.py hyperclapper /path/to/HyperClaper.json
python3 analysis/political_content_scan.py linkboost /path/to/LinkBoost-2025.json

# Immunotherapy content, with documented acronym-collision and false-positive fixes
python3 analysis/immunotherapy_content_scan.py podawaa /path/to/podawaa2024.json
python3 analysis/immunotherapy_content_scan.py hyperclapper /path/to/HyperClaper.json
python3 analysis/immunotherapy_content_scan.py linkboost /path/to/LinkBoost-2025.json

# "Top list" / listicle content
python3 analysis/toplist_content_scan.py podawaa /path/to/podawaa2024.json
python3 analysis/toplist_content_scan.py hyperclapper /path/to/HyperClaper.json
python3 analysis/toplist_content_scan.py linkboost /path/to/LinkBoost-2025.json

# Blockchain / crypto content
python3 analysis/blockchain_crypto_scan.py podawaa /path/to/podawaa2024.json
python3 analysis/blockchain_crypto_scan.py hyperclapper /path/to/HyperClaper.json
python3 analysis/blockchain_crypto_scan.py linkboost /path/to/LinkBoost-2025.json

# University content, with cross-language false-positive fix
python3 analysis/university_content_scan.py podawaa /path/to/podawaa2024.json
python3 analysis/university_content_scan.py hyperclapper /path/to/HyperClaper.json
python3 analysis/university_content_scan.py linkboost /path/to/LinkBoost-2025.json

# Veteran / military content
python3 analysis/veteran_content_scan.py podawaa /path/to/podawaa2024.json
python3 analysis/veteran_content_scan.py hyperclapper /path/to/HyperClaper.json
python3 analysis/veteran_content_scan.py linkboost /path/to/LinkBoost-2025.json

# Authenticity content
python3 analysis/authenticity_content_scan.py podawaa /path/to/podawaa2024.json
python3 analysis/authenticity_content_scan.py hyperclapper /path/to/HyperClaper.json
python3 analysis/authenticity_content_scan.py linkboost /path/to/LinkBoost-2025.json

# Diabetes content
python3 analysis/diabetes_content_scan.py podawaa /path/to/podawaa2024.json
python3 analysis/diabetes_content_scan.py hyperclapper /path/to/HyperClaper.json
python3 analysis/diabetes_content_scan.py linkboost /path/to/LinkBoost-2025.json

# LinkedIn algorithm mentions
python3 analysis/algorithm_mention_scan.py podawaa /path/to/podawaa2024.json
python3 analysis/algorithm_mention_scan.py hyperclapper /path/to/HyperClaper.json
python3 analysis/algorithm_mention_scan.py linkboost /path/to/LinkBoost-2025.json

# Career transitions (layoffs, remote work, burnout)
python3 analysis/career_transitions_scan.py podawaa /path/to/podawaa2024.json
python3 analysis/career_transitions_scan.py hyperclapper /path/to/HyperClaper.json
python3 analysis/career_transitions_scan.py linkboost /path/to/LinkBoost-2025.json

# Social proof and credibility signaling
python3 analysis/social_proof_scan.py podawaa /path/to/podawaa2024.json
python3 analysis/social_proof_scan.py hyperclapper /path/to/HyperClaper.json
python3 analysis/social_proof_scan.py linkboost /path/to/LinkBoost-2025.json

# Industry verticals
python3 analysis/industry_verticals_scan.py podawaa /path/to/podawaa2024.json
python3 analysis/industry_verticals_scan.py hyperclapper /path/to/HyperClaper.json
python3 analysis/industry_verticals_scan.py linkboost /path/to/LinkBoost-2025.json

# Geographic content mentions
python3 analysis/geographic_mentions_scan.py podawaa /path/to/podawaa2024.json
python3 analysis/geographic_mentions_scan.py hyperclapper /path/to/HyperClaper.json
python3 analysis/geographic_mentions_scan.py linkboost /path/to/LinkBoost-2025.json

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
- [Simple title aggregate](docs/research/simple-titles.md) — generic professional-title keyword counts (CEO, Founder, Coach, etc.), no names or full bios
- [Entity mentions](docs/research/entity-mentions.md) — news outlet, magazine, TV/streaming platform, and corporation mention counts across all three datasets
- [Law-related content](docs/research/law-content.md) — narrow (legal-profession) vs. broader (compliance, legislation, IP) content counts
- [Speaker / thought leader](docs/research/speaker-thought-leader.md) — self-described speaker/thought-leader prevalence, with a real overlap finding between the two terms
- [Nonprofit-related content](docs/research/nonprofit-content.md) — charity/NGO/philanthropy mention counts, with a built-in check that catches raw counts inflated by a single repeated template
- [Investment / venture capital content](docs/research/investment-vc-content.md) — investment/VC term mention counts, with a review of what legal frameworks would (and wouldn't) apply if specific elements were separately established
- [Cybersecurity content vs. engagement anomalies](docs/research/cybersecurity-anomaly.md) — cross-tabulates cybersecurity content against the repo's own anomaly indicators; podawaa2024 and HyperClapper only
- [Travel agencies and destinations](docs/research/travel-content.md) — travel platform and destination mentions, with two documented corrections (a duplicate-template artifact and a French-language false positive)
- [National security / NSA content](docs/research/national-security-content.md) — the smallest content category in the repo; under 0.1% of any dataset
- [Homelessness-related content](docs/research/homelessness-content.md) — narrow vs. broad term counts, including a duplicate-template case that turned out to be genuine content, not noise
- [Pharma / biotech content](docs/research/pharma-content.md) — pharma/biotech/FDA term counts; corrects a LinkBoost-2025 miscategorization where most "FDA" matches turned out to be import-compliance content, not pharmaceutical-industry content
- [Political party / Trump content](docs/research/political-content.md) — Trump/Biden/party-name mention counts; links a LinkBoost-2025 correction back to the same repeated campaign post already documented in decision-points.md
- [Immunotherapy content](docs/research/immunotherapy-content.md) — documents two false positives (a "cart"/CAR-T acronym collision and an unrelated boosted post) that made this the smallest genuine content category found so far
- ["Top list" / listicle content](docs/research/toplist-content.md) — one of the larger niche-topic categories found (1.7–3.9%), with a real style difference between datasets
- [Blockchain / crypto content](docs/research/blockchain-crypto-content.md) — podawaa2024's rate is 4x HyperClapper's; a plausible (not confirmed) shift toward AI content over time
- [University content](docs/research/university-content.md) — documents a cross-language false positive (German "mit" vs. the "MIT" acronym) caught via cross-dataset inconsistency rather than a within-dataset check
- [Veteran / military content](docs/research/veteran-content.md) — includes genuine tribute content alongside a correction linking back to the already-documented campaign-post artifact
- [Authenticity content](docs/research/authenticity-content.md) — directly checks and refutes a specific "honesty irony" statistic from a disputed third-party document
- [Diabetes content](docs/research/diabetes-content.md) — one of the smallest genuine categories found; a duplicate-string case that turned out to be real content, not noise
- [LinkedIn algorithm mentions](docs/research/algorithm-mention-content.md) — directly relevant to this project's own subject matter; companion to algorithm-strategy-advice.md
- [Career transitions](docs/research/career-transitions-content.md) — layoffs, remote work, burnout, and work-life balance mentions
- [Social proof and credibility signaling](docs/research/social-proof-content.md) — award claims, follower milestones, and engagement bait; confirms the "Agree?" template across two datasets
- [Industry verticals](docs/research/industry-verticals-content.md) — real estate, insurance, manufacturing, retail, healthcare, and energy/ESG; the largest niche-topic category found
- [Geographic content mentions](docs/research/geographic-mentions-content.md) — countries/regions as content subject matter, cross-checked against account-location metadata
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
three datasets. HyperClapper leads by a wide margin (16.52%), aligning with
its occupation skew and reciprocal-engagement rate; podawaa2024 is lowest
(4.45%); LinkBoost-2025 sits in between (6.68%) but reflects pod-activity
volume on a small number of target posts rather than distinct content
volume. Full methodology, side-by-side table, and caveats:
[docs/research/career-advice-comparison.md](docs/research/career-advice-comparison.md).

## Topic taxonomy and decision points

`analysis/topic_taxonomy.py` assigns every record across all three
datasets to exactly one of nine mutually exclusive content categories
(plus a catch-all). Headline: `technology_ai` (20.11%) and
`uncategorized_other` (42.97%) dominate overall; HyperClapper skews
sharply toward `career_job_search` (13.92%) and LinkBoost-2025 toward
`leadership_coaching_motivation` (18.91%). Full results:
[docs/research/topic-taxonomy.md](docs/research/topic-taxonomy.md).

`analysis/category_title_patterns.py` finds the recurring (never one-off)
title templates within each category, and
[docs/research/decision-points.md](docs/research/decision-points.md) maps
each category to the real-world decision its dominant template is
plausibly aimed at — e.g. `career_job_search`'s top template (533
occurrences) pushes an "AI resume rewrite" narrative.

## Simple title aggregate

`analysis/simple_title_aggregate.py` reports how many records' stated
occupation/headline text contains a simple, generic professional title
keyword ("CEO," "Founder," "Coach," "Marketer," etc.) — aggregate counts
only, never a name, handle, or verbatim headline/occupation sentence.
Covers HyperClapper and LinkBoost-2025 only (podawaa2024 has no
occupation field). LinkBoost skews heavily Founder/Coach (34.7%
combined); HyperClapper leans Marketer/Founder (20.2% combined). Full
results: [docs/research/simple-titles.md](docs/research/simple-titles.md).

## Entity mentions (news outlets, magazines, TV/streaming, corporations)

`analysis/entity_mention_scan.py` counts mentions of named entities across
four fixed categories. Headline: corporations get named far more than
any other category (13.00–23.19% of records across the three datasets,
led by LinkedIn, Google, and - specifically in HyperClapper - an
outsized 8.67% share for IBM, roughly 24–26× its share elsewhere,
plausibly tied to that dataset's elevated free-certification content
share). YouTube/TikTok/Netflix are the top three streaming/TV platforms,
in that order, in every dataset. Full results across all four categories:
[docs/research/entity-mentions.md](docs/research/entity-mentions.md).

## Law-related content

`analysis/law_content_scan.py` reports two tallies: a narrow one (lawyer,
attorney, law firm, litigation, paralegal, etc.) and a broader one that
adds legislation, compliance, intellectual property, and the bare word
"legal." Genuine legal-profession content is small everywhere (under
0.6% of any dataset, narrow measure); "compliance" alone drives roughly
half of the broader count in every dataset, which is why it's tracked
as its own line rather than folded in silently. Full results:
[docs/research/law-content.md](docs/research/law-content.md).

## Speaker / thought leader

`analysis/speaker_thought_leader_scan.py` covers HyperClapper and
LinkBoost-2025 only (podawaa2024 has no occupation field). The real
finding isn't the raw counts - it's that "thought leader" mentions are
almost entirely a subset of "speaker" mentions (100% overlap in
HyperClapper, 97.3% in LinkBoost-2025), consistent with one recurring
bio template rather than two independent self-descriptions. LinkBoost-2025
skews far higher on both (18.29% "speaker" vs. 3.83% in HyperClapper).
Full results: [docs/research/speaker-thought-leader.md](docs/research/speaker-thought-leader.md).

## Nonprofit-related content

`analysis/nonprofit_content_scan.py` scans for charity, nonprofit, NGO,
philanthropy, and 501(c)(3) mentions, and — unlike earlier scans —
builds in an automatic check for dominant repeated strings inflating a
raw count. It caught a real one: HyperClapper's headline field first
looked like it had the highest nonprofit-mention rate of any field
(1.38%), but 658 of those 681 matching records turned out to share one
repeated headline. Corrected, the real rate is 0.05% — the lowest, not
the highest. The same check caught two more distortions in
LinkBoost-2025. Full results:
[docs/research/nonprofit-content.md](docs/research/nonprofit-content.md).

## Investment / venture capital content

`analysis/investment_vc_scan.py` counts investment- and VC-related term
mentions across post content. This is one of the larger content
categories checked in this repo so far (3.43-5.17% "any mention" across
the three datasets), with LinkBoost-2025 highest, consistent with its
lean toward executive/business content elsewhere in this repo. A
mention is not evidence of any legal violation on its own -- see
[docs/research/investment-vc-content.md](docs/research/investment-vc-content.md)
for why, and for the securities-law and FTC frameworks that would
actually be relevant if specific elements were separately established.

## Cybersecurity content vs. engagement anomalies

`analysis/cybersecurity_anomaly_scan.py` cross-tabulates
cybersecurity-related content against the same engagement-anomaly
indicators used in the baseline profile (zero views with likes,
likes exceeding views, extreme like/view ratio, reciprocal
like+comment pairing). Cybersecurity content shows a higher anomaly
rate than the dataset baseline on 3 of 4 measures checked, most
notably HyperClapper's reciprocal like+comment rate (84.2% vs. 68.6%
baseline). An elevated category-level rate is a population pattern,
not identification of any specific account or post. Full results:
[docs/research/cybersecurity-anomaly.md](docs/research/cybersecurity-anomaly.md).

## Travel agencies and destinations

`analysis/travel_content_scan.py` counts travel agency/platform and
destination mentions, with a built-in duplicate-template safeguard
that caught real inflation in LinkBoost-2025 (a single AI-travel-tool
ad, boosted 47 times, accounted for 48 mentions each of four different
booking platforms) and a separate, non-duplicate artifact in
podawaa2024, where "France" and "Paris" mentions turned out to be
French-language content about French domestic topics, not travel
recommendations. Excluding that artifact, Dubai and London are the
most consistently mentioned destinations across all three datasets.
Full results: [docs/research/travel-content.md](docs/research/travel-content.md).

## National security / NSA content

`analysis/national_security_scan.py` counts mentions of
national-security-related terms. This is the smallest content category
checked in this repo so far - under 0.1% of any dataset - and NSA
specifically is almost nonexistent (24 mentions in podawaa2024, 1 in
HyperClapper, 0 in LinkBoost-2025). The duplicate-template safeguard
caught a real correction here too: LinkBoost-2025's "FBI" count of 15
is one boosted post, not 15 distinct posts. Full results:
[docs/research/national-security-content.md](docs/research/national-security-content.md).

## Homelessness-related content

`analysis/homelessness_content_scan.py` reports narrow vs. broad
homelessness-related term counts. LinkBoost-2025's duplicate-template
warning fired here too, but unlike every prior instance in this repo,
the repeated string turned out to be genuine on-topic content, not
noise - a real "overcame homelessness" success story boosted 79 times.
LinkBoost-2025 also contains genuine homelessness-sector advocacy
content beyond that template, a meaningfully different character than
most other small categories checked in this repo. Full results:
[docs/research/homelessness-content.md](docs/research/homelessness-content.md).

## Pharma / biotech content

`analysis/pharma_content_scan.py` counts pharma/biotech term mentions.
The duplicate-template safeguard didn't fire here, but a new check
(low distinct-string count without one dominant string) did on
LinkBoost-2025, and it mattered: 333 of its 482 matches turned out to
be FDA import-compliance/customs content across roughly 8 posts, not
pharmaceutical-industry content. Full results:
[docs/research/pharma-content.md](docs/research/pharma-content.md).

## Political party / Trump content

`analysis/political_content_scan.py` counts political-party and
Trump/Biden mentions. Trump is the largest term in every dataset.
LinkBoost-2025's duplicate-template warning fired again here, linking
back to the same repeated political campaign-endorsement post already
documented in decision-points.md (97 occurrences there too) - the
candidate is not identified in either doc, consistent with this repo's
privacy rules. Full results:
[docs/research/political-content.md](docs/research/political-content.md).

## Immunotherapy content

`analysis/immunotherapy_content_scan.py` counts immunotherapy-related
term mentions - and documents two real false positives found while
building it. An initial "CAR-T" pattern also matched the common word
"cart" (shopping cart, e-commerce content), producing 100+ false
positives per dataset before it was fixed. A second false positive
survived the fix: LinkBoost-2025's 40 "immunotherapy" matches all trace
to one unrelated business-transformation post. Corrected, genuine
immunotherapy content is 16 mentions total, all in podawaa2024 - the
smallest genuine content category found in this project so far. Full
results: [docs/research/immunotherapy-content.md](docs/research/immunotherapy-content.md).

## "Top list" / listicle content

`analysis/toplist_content_scan.py` counts "Top 10," "N ways to," "best
of," and similar listicle patterns. This is one of the larger content
categories found across the niche-topic scans in this repo (1.7-3.9%
"any mention," well above pharma, cybersecurity, law, nonprofit,
travel, political, national security, and immunotherapy content, all
under 1%). HyperClapper and LinkBoost-2025 both run meaningfully higher
than podawaa2024, consistent with their broader lean toward templated
content already seen elsewhere in this repo, and the two datasets show
a real style difference: LinkBoost-2025 leans on numbered-listicle
phrasing while HyperClapper leans on "Top N" specifically. Full results:
[docs/research/toplist-content.md](docs/research/toplist-content.md).

## Blockchain / crypto content

`analysis/blockchain_crypto_scan.py` counts blockchain/crypto term
mentions. podawaa2024 has by far the highest rate (2.93%, roughly 4x
HyperClapper and 2.5x LinkBoost-2025) and is the only dataset where
"blockchain" outranks general "crypto" phrasing. Since podawaa2024 is
2024 data and the other two are 2025-2026 data, this is consistent
with -- though doesn't confirm -- a shift in this content ecosystem's
attention from blockchain/Web3 toward AI over that period, alongside
the technology_ai increase already documented in
[docs/research/topic-taxonomy.md](docs/research/topic-taxonomy.md).
Full results: [docs/research/blockchain-crypto-content.md](docs/research/blockchain-crypto-content.md).

## University content

`analysis/university_content_scan.py` counts university-related term
mentions, and documents a real cross-language false positive: an
earlier draft's case-insensitive "MIT" pattern also matched the German
preposition "mit," inflating podawaa2024's MIT count by roughly 94%
(2,601 raw vs. 148 genuine) and briefly making it look like the top
term in that dataset alone -- an inconsistency with the other two
datasets that prompted the fix. Corrected, "university/universities"
leads in all three datasets, Harvard is the most-mentioned named
institution everywhere, and LinkBoost-2025 leans unusually heavily on
Cambridge relative to the other two. Full results:
[docs/research/university-content.md](docs/research/university-content.md).

## Veteran / military content

`analysis/veteran_content_scan.py` counts veteran/military term
mentions. LinkBoost-2025's duplicate-template warning fires again,
tracing to the same repeated political-endorsement post already
documented in decision-points.md and political-content.md (candidate
not named). Unlike that artifact, the rest of LinkBoost-2025's veteran
content is genuine - real, distinct tributes to Indian Armed Forces
personnel. podawaa2024 shows the most diverse term usage, including the
only meaningful "veteran-owned" business content across the three
datasets. Full results:
[docs/research/veteran-content.md](docs/research/veteran-content.md).

## Authenticity content

`analysis/authenticity_content_scan.py` counts authenticity-related
term mentions, and directly checks a specific claim from a disputed
third-party document referenced in this project's history: that
HyperClapper had 5,193 "honest truth"/"real talk" posts (10.52%). The
actual combined count is 61 - nowhere close. LinkBoost-2025 has the
highest overall rate and the most genuinely distributed content;
podawaa2024 leans on "transparent/transparency" while the other two
lean on "authentic/authenticity." Full results:
[docs/research/authenticity-content.md](docs/research/authenticity-content.md).

## Diabetes content

`analysis/diabetes_content_scan.py` counts diabetes-related term
mentions - one of the smallest genuine content categories found in
this project (under 0.25% everywhere). LinkBoost-2025's duplicate
string turned out to be genuine health content boosted by the
platform's structure, not a false positive - the opposite outcome from
the immunotherapy and university scans, a reminder that this
safeguard flags a number to check, not a verdict. Full results:
[docs/research/diabetes-content.md](docs/research/diabetes-content.md).

## LinkedIn algorithm mentions

`analysis/algorithm_mention_scan.py` counts algorithm-related term
mentions - directly relevant to this project's own subject matter, and
a companion to [algorithm-strategy-advice.md](docs/research/algorithm-strategy-advice.md).
LinkBoost-2025 has the highest rate and its top repeated posts are
genuinely about gaming/understanding the LinkedIn algorithm; podawaa2024
is the only dataset with meaningful "LinkedIn algorithm" specificity
rather than generic "algorithm" phrasing. Full results:
[docs/research/algorithm-mention-content.md](docs/research/algorithm-mention-content.md).

## Career transitions (layoffs, remote work, burnout)

`analysis/career_transitions_scan.py` counts layoffs, remote work,
return-to-office, burnout, and work-life balance mentions. HyperClapper
has the highest rate (4.851%), driven mostly by "remote work"; LinkBoost-2025
leans heavily on "burnout" specifically, connecting to the
performed-vulnerability pattern in authenticity-content.md. Full
results: [docs/research/career-transitions-content.md](docs/research/career-transitions-content.md).

## Social proof and credibility signaling

`analysis/social_proof_scan.py` counts award/recognition claims,
follower milestones, engagement-bait formats, and anniversary posts -
one of the most directly on-theme scans in this repo. Confirms the
already-documented "Agree?" template (baseline-profile.md) appears in
LinkBoost-2025 too (888 occurrences), not just podawaa2024. Full
results: [docs/research/social-proof-content.md](docs/research/social-proof-content.md).

## Industry verticals

`analysis/industry_verticals_scan.py` counts real estate, insurance,
manufacturing/supply chain, retail/e-commerce, healthcare, and
energy/ESG mentions. HyperClapper's 10.2% "any mention" rate is the
highest of any niche-topic scan in this repo. Retail/e-commerce leads
in two datasets; healthcare leads in the third. Full results:
[docs/research/industry-verticals-content.md](docs/research/industry-verticals-content.md).

## Geographic content mentions

`analysis/geographic_mentions_scan.py` counts countries/regions as
content subject matter (distinct from account-location metadata in
demographics.md). India leads two datasets, Europe leads the third;
the pattern lines up with each dataset's own account-location skew
already documented elsewhere in this repo. Full results:
[docs/research/geographic-mentions-content.md](docs/research/geographic-mentions-content.md).

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

## Outreach materials

[outreach/](outreach/) contains finished, aggregate-only educational
deliverables built from this research — currently a two-page classroom
media-literacy lesson plan. See [outreach/README.md](outreach/README.md)
for what's there, why it's safe to commit as a finished PDF (unlike raw
data), and the same scope discipline as the rest of this repo.

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
