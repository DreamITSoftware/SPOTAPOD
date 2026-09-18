# Changelog

## Unreleased

### Added
- `docs/research/hyperclapper-product-context.md` - publicly sourced,
  evidence-tiered context on the HyperClapper product itself (self-reported
  marketing claims: member count, pricing tiers, positioning vs. Lempod and
  Linkboost) contrasted with a single independent, uncorroborated
  extension-usage tracker showing a declining install count roughly an
  order of magnitude below the marketing claim. Draws no new statistic
  from `HyperClaper.json` and does not revise any figure in
  baseline-profile.md or posting-velocity.md; explicitly makes no
  terms-of-service or § 465.8 compliance determination, consistent with
  provenance.md and regulatory-context.md.
- `analysis/honesty_language_scan.py` and
  `docs/research/honesty-language-content.md` - kindness,
  lying/lies/liar, and deception/deceptive term counts, related to but
  distinct from authenticity-content.md (self-description vs. the
  underlying moral vocabulary). "Lying/lies/liar" leads in two of three
  datasets; deception-specific language is small everywhere (under 100
  mentions per dataset).
- `docs/unknowing-participant-impact.md` - a new foundational doc (not
  a content-topic finding, alongside limitations.md and privacy.md)
  addressing a distinction no other doc in this repo makes explicit:
  knowing and unknowing participation in engagement-pod activity are
  different situations with different harms, and this repo's data
  cannot tell them apart. Traces this concretely through the actual
  findings across the repo rather than as an abstract category -
  baseline anomalies, posting velocity (ghostwritten-executive
  accounts), repeated templates, real tribute/advocacy content caught
  alongside a boosted political post, false-positive category
  placement, and demographic aggregation - then works through five
  concrete harms (self-deception about real reach, negligence-style
  legal exposure, reputational exposure from an unexplainable signal,
  non-consensual research inclusion, and possible unauthorized account
  use), tying them to why this repo's privacy rules are binding rather
  than optional.
- Two structural analyses, different in kind from the content keyword
  scans elsewhere in this repo:
  - `analysis/cross_dataset_overlap_scan.py` and
    `docs/research/cross-dataset-account-overlap.md` - checks whether
    the same accounts appear in both HyperClapper and LinkBoost-2025
    using hashed identifiers only (never plaintext). Result: zero
    overlap across 702 and 414 distinct accounts respectively.
  - `analysis/posting_velocity_scan.py` and
    `docs/research/posting-velocity.md` - computes sustained posting
    rate for HyperClapper's highest-volume accounts using real
    timestamps. Interval timing is highly irregular (CV consistently
    above 80%), ruling out simple robotic clockwork, but the top 10
    accounts sustain 1.2-3.7 posts/day for 174-712 consecutive days.
    Accounts identified only by anonymous rank.
- Four new scans covering topics suggested by post titles/content
  review, each with the established duplicate-template safeguard:
  - `analysis/career_transitions_scan.py` and
    `docs/research/career-transitions-content.md` - layoffs, remote
    work, RTO, burnout, and work-life balance. HyperClapper's rate
    (4.851%) is highest, driven by "remote work."
  - `analysis/social_proof_scan.py` and
    `docs/research/social-proof-content.md` - awards/recognition,
    follower milestones, engagement bait, and anniversary posts.
    Confirms the already-documented "Agree?" template (3,918x in
    podawaa2024) also appears in LinkBoost-2025 (888x), a genuine
    cross-dataset pattern rather than a single-dataset artifact.
  - `analysis/industry_verticals_scan.py` and
    `docs/research/industry-verticals-content.md` - real estate,
    insurance, manufacturing/supply chain, retail/e-commerce,
    healthcare, and energy/ESG. HyperClapper's 10.2% "any mention"
    rate is the highest of any niche-topic scan in this repo.
  - `analysis/geographic_mentions_scan.py` and
    `docs/research/geographic-mentions-content.md` - countries/regions
    as content subject matter (distinct from the account-location
    metadata in demographics.md). Confirms content subject matter
    tracks each dataset's own account-location skew.
- `analysis/algorithm_mention_scan.py` and
  `docs/research/algorithm-mention-content.md` - algorithm-related term
  counts, directly relevant to this project's own subject matter and a
  companion to algorithm-strategy-advice.md. LinkBoost-2025 has the
  highest rate, with top repeated posts genuinely about gaming/
  understanding the LinkedIn algorithm; podawaa2024 is the only dataset
  with meaningful "LinkedIn algorithm" specificity rather than generic
  "algorithm" phrasing.
- `analysis/diabetes_content_scan.py` and
  `docs/research/diabetes-content.md` - diabetes-related term counts,
  one of the smallest genuine content categories found in this project
  (under 0.25% everywhere). LinkBoost-2025's flagged duplicate string
  turned out to be genuine health content boosted by the platform's
  structure, not a false positive - the opposite outcome from the
  immunotherapy and university scans, documented as a reminder that
  the duplicate-template safeguard flags a number to check, not a
  verdict either way.
- `analysis/authenticity_content_scan.py` and
  `docs/research/authenticity-content.md` - authenticity-related term
  counts. Directly checks a specific claim from a disputed third-party
  document referenced in this project's history: that HyperClapper had
  5,193 "honest truth"/"real talk" posts (10.52%). The actual combined
  count is 61. This is consistent with a separately documented
  discrepancy in the same document (a claimed 1,706 vs. an actual
  533-806 occurrences of a resume-rewrite template).
- `analysis/veteran_content_scan.py` and `docs/research/veteran-content.md`
  - veteran/military term counts. LinkBoost-2025's duplicate-template
  warning traces to the same repeated political-endorsement post
  already documented in decision-points.md and political-content.md
  (candidate not named). Unlike that artifact, the rest of
  LinkBoost-2025's veteran content is genuine - real tributes to Indian
  Armed Forces personnel. podawaa2024 has the most diverse term usage.
  Bare "VA" deliberately excluded (collides with the Virginia state
  abbreviation); only "Veterans Affairs"/"VA benefits"/"VA loan"/"VA
  disability" are checked.
- `analysis/university_content_scan.py` and
  `docs/research/university-content.md` - university-related term
  counts, documenting a real cross-language false positive: an earlier
  case-insensitive "MIT" pattern also matched the German preposition
  "mit," inflating podawaa2024's MIT count by roughly 94% (2,601 raw
  vs. 148 genuine). Caught via cross-dataset inconsistency (one
  dataset's top term didn't match the other two) rather than a
  within-dataset duplicate-template or low-distinct-ratio check -
  documented as a reminder that cross-dataset comparison is itself a
  useful safeguard.
- `analysis/blockchain_crypto_scan.py` and
  `docs/research/blockchain-crypto-content.md` - blockchain/crypto term
  counts. podawaa2024's rate (2.93%) is roughly 4x HyperClapper's and
  2.5x LinkBoost-2025's, and is the only dataset where "blockchain"
  outranks general "crypto" phrasing. Documents a plausible,
  INFERENCE-tier cross-dataset pattern: since podawaa2024 is 2024 data
  and the other two are 2025-2026 data, this is consistent with a shift
  in attention from blockchain/Web3 toward AI over that period,
  alongside the technology_ai increase already in topic-taxonomy.md -
  explicitly flagged as not a confirmed time-series trend.
- `analysis/toplist_content_scan.py` and `docs/research/toplist-content.md`
  - "Top 10"/listicle content counts. One of the larger content
  categories found across this repo's niche-topic scans (1.7-3.9% "any
  mention"). HyperClapper and LinkBoost-2025 both run meaningfully
  higher than podawaa2024, consistent with their broader lean toward
  templated content documented elsewhere in this repo, and the two
  datasets show a real style difference (numbered-listicle phrasing vs.
  "Top N" phrasing) rather than just a volume difference.
- `analysis/immunotherapy_content_scan.py` and
  `docs/research/immunotherapy-content.md` - immunotherapy-related term
  counts, documenting two real false positives found while building it:
  an initial "CAR-T" pattern that also matched the common word "cart"
  (100+ false positives per dataset before the fix), and a second false
  positive that survived the fix - LinkBoost-2025's 40 "immunotherapy"
  matches all trace to one unrelated business-transformation post.
  Corrected, genuine immunotherapy content is 16 mentions total, all in
  podawaa2024 - the smallest genuine content category found in this
  project so far.
- `analysis/political_content_scan.py` and
  `docs/research/political-content.md` - Trump/Biden/political-party
  term counts. Trump is the largest term in every dataset. Links a
  LinkBoost-2025 duplicate-template correction back to the same
  repeated political campaign-endorsement post already documented in
  decision-points.md; the candidate is not identified in either doc,
  consistent with this repo's privacy rules.
- `analysis/pharma_content_scan.py` and `docs/research/pharma-content.md`
  - pharma/biotech/FDA term counts. Extends the duplicate-template
  safeguard with a new check for a low distinct-string count without a
  single dominant string, which caught a real miscategorization: 333 of
  LinkBoost-2025's 482 "pharma" matches are FDA import-compliance/
  customs content across roughly 8 boosted posts, not
  pharmaceutical-industry content.
- `analysis/homelessness_content_scan.py` and
  `docs/research/homelessness-content.md` - narrow vs. broad
  homelessness-related term counts. Notable because the
  duplicate-template safeguard fired on LinkBoost-2025 but, unlike
  every prior instance in this repo, the repeated string turned out to
  be genuine on-topic content (a real "overcame homelessness" success
  story boosted 79 times), not noise - documented as a reminder that
  the safeguard flags a pattern to check, not an automatic verdict.
  LinkBoost-2025 also contains genuine homelessness-sector advocacy
  content beyond that template.
- `analysis/national_security_scan.py` and
  `docs/research/national-security-content.md` - national security/NSA/
  CIA/FBI term mention counts. The smallest content category checked in
  this repo so far (under 0.1% of any dataset); NSA specifically is
  almost nonexistent (24/1/0 mentions across the three datasets). The
  duplicate-template safeguard caught a real correction: LinkBoost-2025's
  "FBI" count of 15 is one boosted post, not 15 distinct ones.
- `analysis/travel_content_scan.py` and `docs/research/travel-content.md`
  - travel agency/platform and destination mention counts. Two real
  corrections documented: LinkBoost-2025's per-platform counts are
  dominated by a single AI-travel-tool ad boosted 47 times (the
  duplicate-template safeguard from nonprofit_content_scan.py catches
  this automatically), and podawaa2024's France/Paris counts are a
  separate, non-duplicate artifact - genuinely distinct French-language
  posts about French domestic topics, not travel content, found only by
  reading a sample of the matching text.
- `analysis/cybersecurity_anomaly_scan.py` and
  `docs/research/cybersecurity-anomaly.md` - cross-tabulates
  cybersecurity-related content against the repo's existing
  engagement-anomaly indicators (zero views with likes, likes
  exceeding views, extreme like/view ratio, reciprocal like+comment
  pairing). podawaa2024 and HyperClapper only; LinkBoost-2025 has no
  per-record engagement fields to cross-reference. Cybersecurity
  content shows an elevated anomaly rate on 3 of 4 measures checked.
  Explicit in both the script and the doc that a category-level
  elevated rate identifies no specific account or post.
- `analysis/investment_vc_scan.py` and
  `docs/research/investment-vc-content.md` - investment/VC term mention
  counts across all three datasets (3.43-5.17% "any mention"), one of
  the larger content categories checked so far. Documents which legal
  frameworks (securities law, FTC Endorsement Guides, Investment
  Advisers Act) would actually be relevant if specific elements were
  separately established, and why a keyword mention alone establishes
  none of them. Uses the same duplicate-template safeguard as
  nonprofit_content_scan.py; no field triggered it.
- `analysis/nonprofit_content_scan.py` and
  `docs/research/nonprofit-content.md` — charity/nonprofit/NGO/
  philanthropy mention counts, with a permanent, automatic safeguard
  against the exact distortion a manual check just caught: a raw
  "any mention" count driven by one repeated headline/template rather
  than genuine distinct signal. The script now reports distinct
  underlying text values alongside every raw count and flags any field
  where a single string accounts for 20%+ of matches. Caught three real
  instances on first run, including HyperClapper's headline field, which
  looked like the highest nonprofit-mention rate of any field (1.38%)
  before correction and the lowest (0.05%) after.
- `analysis/speaker_thought_leader_scan.py` and
  `docs/research/speaker-thought-leader.md` - self-described
  speaker/thought-leader prevalence (HyperClapper and LinkBoost-2025
  only; podawaa2024 has no occupation field). Flags that "thought
  leader" mentions are almost entirely a subset of "speaker" mentions
  (100% overlap in HyperClapper, 97.3% in LinkBoost-2025) rather than
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
  in HyperClapper specifically (vs. 0.18–0.33% elsewhere) is flagged as
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
  headline text, for HyperClapper and LinkBoost-2025 only (podawaa2024 has
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
