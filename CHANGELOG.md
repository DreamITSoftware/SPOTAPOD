# Changelog

## Unreleased

### Added
- `docs/algorithm-strategy-advice.md` — split out from `audience-impact.md`
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
- `analysis/regulatory_category_scan.py` and `docs/other-regulatory-signals.md`
  — aggregate keyword-signal counts for content categories beyond § 465.8
  (health claims, financial claims, licensing language, endorsement-
  disclosure gaps), explicitly framed as signals, not findings.
- `docs/audience-impact.md` — INFERENCE-tier discussion of plausible
  downstream reader impact from inflated social proof, tied to the
  category-scan results.
- `analysis/demographics_scan.py` and `docs/demographics.md` — aggregate
  geography and stated-occupation-category breakdown, with an explicit
  scope statement that protected characteristics are never inferred.
- `LICENSE` (MIT, code/schemas), `LICENSE-CONTENT` (CC BY 4.0, docs),
  `CITATION.cff`, `CONTRIBUTING.md` (encodes the hard rules below as
  review criteria), `tests/` (fixture-based unit tests), and an
  aggregate-only `explorer/` static dashboard.

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
  aggregation level (declined — see `docs/demographics.md`).
- Any claim tying a specific real, named person, report, or company to
  fake-engagement conduct without evidence — including hypothetical or
  conditional framing ("if this specific report were pushed via fake
  socials...") naming a real party. The general mechanism is documented
  in `docs/audience-impact.md`; the specific accusation is not, regardless
  of hedging.
