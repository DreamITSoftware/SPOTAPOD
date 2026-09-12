# Contributing

This repo exists to demonstrate that engagement-pod patterns can be
documented rigorously *without* exposing anyone's identity. That's not a
style choice — it's the actual constraint every contribution has to pass.
If a change would violate any of the rules below, it doesn't belong here,
no matter how useful the analysis behind it is.

## Hard rules (non-negotiable)

1. **No raw data.** Never commit, zip, or otherwise include any of the
   source JSON files, or any subset/sample of their records, anywhere in
   this repo.

2. **No script may print, log, or write a direct identifier** — name,
   handle, URN, profile link, photo URL, or internal ID — found in any
   source file. If your script needs to touch one of these fields at all,
   pass it through `hashlib.sha256` (Python) or `SHA256.Create()` (C#)
   immediately, use the hash only as an in-memory counting key, and let it
   go out of scope. Never write the hash-to-original mapping anywhere.

3. **No per-entity lookup, browsable table, or search feature.** Not a
   private one, not a hashed one. If a change would let someone filter,
   search, or click down to a specific record/author/target/operator,
   it doesn't ship — see `docs/limitations.md` for why.

4. **Every substantive claim gets an evidence tier**: VERIFIED,
   CORROBORATED, STATED, UNCORROBORATED, or INFERENCE (see
   `docs/limitations.md` and `docs/other-regulatory-signals.md` for how
   these are used in practice). Don't upgrade a tier without new evidence,
   and don't drop the tier label to make a claim read more confidently
   than it should.

5. **No legal conclusions asserted as fact.** This repo can report that
   content matches a keyword pattern or a metric crosses a threshold; it
   cannot report that a specific account, post, or dataset violates 16 CFR
   § 465.8 or any other law. See `docs/regulatory-context.md` and
   `docs/other-regulatory-signals.md` for the pattern to follow.

6. **No inferred protected characteristics.** Never add code or docs that
   guess race, ethnicity, gender, age, religion, disability, or similar
   from a name, photo, or any other proxy — for an individual or in
   aggregate. See `docs/demographics.md` for the line this repo draws and
   why aggregation doesn't move it.

7. **New datasets get the full doc set.** Adding a fourth dataset means
   adding its section to `docs/data-dictionary.md`, `docs/limitations.md`,
   `docs/privacy.md`, and `docs/provenance.md` — not just an analysis
   script. A dataset without a privacy/limitations writeup doesn't belong
   in `analysis/` yet.

8. **Provenance is reported, not assumed.** Don't fill in a dataset's
   source or collection method based on a filename or a guess. If it's not
   confirmed, `docs/provenance.md` says "Not yet stated" until someone
   actually states it. Same goes for terms-of-service compliance — never
   assert it as fact without independent confirmation.

## What review should check

Before merging any change, check it against the list above like a
checklist, not a vibe. A pull request that adds a genuinely useful
aggregate statistic but also introduces a way to filter down to one
person fails review — the useful part doesn't buy back the part that
doesn't belong here. If you're not sure whether something crosses a line,
it probably does; ask before shipping it, not after.

## Adding a new analysis script

1. Read the target file's schema and note every field that's a direct or
   quasi-identifier before writing any code (see `docs/privacy.md`'s
   format for how to document this).
2. Write the script to output only counts, percentages, ratios, or
   distributions — never a filterable/searchable structure.
3. Add a docstring citing the relevant law, if any (see the pattern in
   `analysis/profile_podawaa.py` and `analysis/regulatory_category_scan.py`).
4. Run it against the real file, confirm the output contains zero
   identifiers, and paste the output into `docs/baseline-profile.md`.
5. Add corresponding entries to `README.md`'s headline figures and docs
   index.
