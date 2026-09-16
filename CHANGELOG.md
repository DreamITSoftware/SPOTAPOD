# Changelog

## Unreleased

### Added
- `analysis/nonprofit_content_scan.py` and
  `docs/research/nonprofit-content.md` — charity/nonprofit/NGO/
  philanthropy mention counts, with a permanent, automatic safeguard
  against the exact distortion a manual check just caught: a raw
  "any mention" count driven by one repeated headline/template rather
  than genuine distinct signal. The script now reports distinct
  underlying text values alongside every raw count and flags any field
  where a single string accounts for 20%+ of matches. Caught three real
  instances on first run, including HyperClaper's headline field, which
  looked like the highest nonprofit-mention rate of any field (1.38%)
  before correction and the lowest (0.05%) after.
- `analysis/speaker_thought_leader_scan.py` and
  `docs/research/speaker-thought-leader.md` - self-described
  speaker/thought-leader prevalence (HyperClaper and LinkBoost-2025
  only; podawaa2024 has no occupation field). Flags that "thought
  leader" mentions are almost entirely a subset of "speaker" mentions
  (100% overlap in HyperClaper, 97.3% in LinkBoost-2025) rather than
  two independent signals, consistent with one recurring bio template.
- `analysis/law_content_scan.py` and `docs/research/law-content.md` -
  narrow (legal-profession-specific: lawyer, attorney, law firm,
  litigation) vs. broader (adds legislation, compliance, intellectual
  property, and bare "legal") content tallies. "Compliance" alone
  accounts for roughly half of every dataset's broader-count hits, which
  is why it's tracked as its own line rather than blended in.
- `analysis/entity_mention_scan.py` and `docs/research/entity-mentions.md`
  — mention counts for named news outlets, magazines, TV/streaming
  platforms, and corporations across all three datasets. Documents a
  real performance pitfall found while building it (a bare `TIME`
  pattern matching the common word "time" caused multi-minute runtimes)
  and how the shipped patterns avoid it. Corporations are mentioned far
  more than any other category (13–23% of records); IBM's 8.67% share
  in HyperClaper specifically (vs. 0.18–0.33% elsewhere) is flagged as
  plausibly, not confirmedly, tied to that dataset's elevated
  free-certification content share.
- `outreach/` — new top-level folder for finished, aggregate-only
  educational deliverables. First addition: `classroom-case-study.pdf`
  (and its self-contained HTML source), a two-page grades-9–12 media
  literacy lesson plan built from the author-concentration statistic and
  the 533×-repeated "AI resume rewrite" template. Explicitly scoped as
  general media-literacy teaching material, not evidence for any
  teen-focused platform or pending legislation.
- `analysis/simple_title_aggregate.py` and `docs/research/simple-titles.md`
  — aggregate counts of simple, generic professional-title keywords
  (CEO, Founder, Coach, Marketer, etc.) found in stated occupation/
  headline text, for HyperClaper and LinkBoost-2025 only (podawaa2024 has
  no occupation-equivalent field). No name, handle, or verbatim headline/
  occupation sentence is ever printed.
- `analysis/topic_taxonomy.py` and `docs/research/topic-taxonomy.md` —
  mutually exclusive (priority-ordered) categorization of all 340,829
  records across the three datasets into nine content categories plus a
  catch-all, with per-dataset breakdown.
- `analysis/category_title_patterns.py` and `docs/research/decision-points.md`
  — finds recurring (never one-off) title templates within each topic
  category and maps each to the real-world decision it's plausibly aimed
  at, grounded in actual duplicated content rather than generic category
  descriptions. Flags the `business_entrepreneurship` political-endorsement
  finding as a keyword-matching artifact rather than a substantive
  finding, and deliberately doesn't name the candidate involved.
- `tools/deidentify.py` and `tools/csharp/deidentify/` — a local-use-only
  de-identification tool producing a copy of one of the three source
  files with direct identifiers hashed (SHA-256) and, optionally
  (`--redact-content`), post/comment content stripped entirely. Output is
  never generated, stored, or shipped by this repo — the tool's own
  documentation is explicit that default-mode output is not
  re-identification-resistant (post content remains a fingerprinting
  vector) and that output must never be committed or shared.
- `.gitignore` blocking `*.json` output outside `schema/` and
  `tests/fixtures/`, specifically to prevent the above tool's local
  output from ever being accidentally committed.
- `analysis/career_advice_scan.py` and `docs/research/career-advice-comparison.md`
  — side-by-side methodology/findings/limitations comparison of
  career-advice content prevalence across all three datasets, including
  the record-vs-content-volume distinction for LinkBoost-2025.
- `analysis/book_genre_scan.py` and `docs/research/book-promotion-content.md` —
  aggregate keyword scan for book-promotion language across all three
  datasets, with a secondary genre breakdown. Same discipline as the
  regulatory-category scan: counts only, no matched text or record
  identified.
- Appendix to `README.md`: a PII-disclaimer README template (reference
  only, clearly marked as not describing this repository) for the
  different case of a repo whose purpose requires hosting real PII —
  later removed once no longer needed (see Removed, below).
- `docs/research/algorithm-strategy-advice.md` — split out from `audience-impact.md`
  into its own page: a genre-level (not report-specific) case study on
  algorithm/creator-strategy advice content, kept free of any specific
  real report, author, or company name.
- Repo scaffolding: `README.md`, `analysis/`, `figures/`, `docs/`,
  `checksums/`, `schema/` for the initial two datasets (`podawaa2024.json`,
  `HyperClaper.json`), aggregate-only from the start — no raw data, no
  per-author identification.
- `docs/privacy.md` — field-by-field PII breakdown and how (and how not)
  scripts touch it.
- `tools/validate.py` (Python) and `tools/csharp/Validate.cs` (C#) —
  structural/type validators reporting by record index only.
- `docs/regulatory-context.md` — full text of 16 CFR § 465.8, cited
  throughout the repo's docs, scripts, and schemas.
- `docs/provenance.md` — reported source/collection method for each file,
  tagged STATED unless independently corroborated; explicit non-assertion
  of terms-of-service compliance.
- Citation of `podawaa2024.json` to Harvard Dataverse
  (`doi:10.7910/DVN/WD9AUR`), tagged CORROBORATED via matching sha256.
- File structures and full data dictionary inlined into the main README.
- Third dataset added: `LinkBoost-2025.json` (77,969 records) — schema,
  profiler, validator support, and full doc updates across
  data-dictionary/limitations/privacy/provenance/method.
- `analysis/regulatory_category_scan.py` and `docs/research/other-regulatory-signals.md`
  — aggregate keyword-signal counts for content categories beyond § 465.8
  (health claims, financial claims, licensing language, endorsement-
  disclosure gaps), explicitly framed as signals, not findings.
- `docs/research/audience-impact.md` — INFERENCE-tier discussion of plausible
  downstream reader impact from inflated social proof, tied to the
  category-scan results.
- `analysis/demographics_scan.py` and `docs/research/demographics.md` — aggregate
  geography and stated-occupation-category breakdown, with an explicit
  scope statement that protected characteristics are never inferred.
- `LICENSE` (MIT, code/schemas), `LICENSE-CONTENT` (CC BY 4.0, docs),
  `CITATION.cff`, `CONTRIBUTING.md` (encodes the hard rules below as
  review criteria), `tests/` (fixture-based unit tests), and an
  aggregate-only `explorer/` static dashboard.

### Changed
- Renamed the project from `pod-engagement-profile` to **SPOTAPOD
  Analysis Repository** across `README.md`, `CITATION.cff`, `mkdocs.yml`,
  `LICENSE`, and `explorer/index.html`. Added an explicit disclaimer at
  the top of the README that this is an independent project, not
  officially affiliated with or endorsed by PolymathWizard/SPOTAPOD —
  structural cues taken from it, but built separately, from different
  source files, and deliberately diverging on the explorer/PII-handling
  approach.

- Reorganized `docs/`: findings/analysis pages (`baseline-profile.md`,
  `other-regulatory-signals.md`, `audience-impact.md`,
  `algorithm-strategy-advice.md`, `demographics.md`,
  `book-promotion-content.md`, `career-advice-comparison.md`) moved into
  `docs/research/`. Foundational/reference docs (`method.md`,
  `data-dictionary.md`, `limitations.md`, `privacy.md`, `provenance.md`,
  `regulatory-context.md`) stay in `docs/`. All cross-links across
  README, CHANGELOG, mkdocs.yml, CONTRIBUTING.md, analysis/ scripts, and
  explorer/ updated and verified to resolve.

### Removed
- The PII-disclaimer-template appendix from the end of `README.md`, at
  explicit request, after the user confirmed they were not manually
  adding the raw data files after all. This did not touch any of the
  repo's actual privacy documentation — `docs/privacy.md`, the README's
  opening banner, the inlined data dictionary's "never printed" notes,
  and `CONTRIBUTING.md`'s hard rules are unchanged. The appendix was a
  generic reference template that never described this repository.

### Explicitly not added, on request or by design
- Raw source files, zipped or otherwise (declined — see `docs/privacy.md`
  and `docs/limitations.md`).
- A per-author/per-record lookup or browsable identity tool, in any form
  (declined repeatedly — this is the one thing this repo is built to not
  be, unlike the SPOTAPOD explorer it otherwise takes structural cues
  from).
- A "this collection method didn't violate the source sites' terms of
  service" assertion (declined — unverifiable legal conclusion).
- Race/ethnicity/gender/age inference from names or photos, at any
  aggregation level (declined — see `docs/research/demographics.md`).
- Any claim tying a specific real, named person, report, or company to
  fake-engagement conduct without evidence — including hypothetical or
  conditional framing ("if this specific report were pushed via fake
  socials...") naming a real party. The general mechanism is documented
  in `docs/research/audience-impact.md`; the specific accusation is not, regardless
  of hedging.
