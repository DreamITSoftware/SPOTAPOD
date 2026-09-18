# Validation tools

Two implementations of the same validator — pick whichever fits your
environment. Both support all three datasets (`podawaa`, `hyperclapper`,
`linkboost`). The fields these validators check for type/range on
(`Likes`, `Views`, `like_count`, `impression_count`, `comment_count`,
`followers`, `SuccessfullLikes`, `SuccessfullComments`) are exactly the
"indicators of social media influence" defined at 16 CFR § 465.1(j), which
[16 CFR § 465.8](../docs/regulatory-context.md) covers — see that doc for
the full rule text. Both:

- Check structural/type conformance against the schemas in
  [../schema](../schema) (required keys present, fields are the right JSON
  type, `Likes`/`Views`/`*_count` fields are non-negative integers,
  `created_at` parses as a real timestamp).
- Optionally verify the source file's sha256 against
  [../checksums/CHECKSUMS.txt](../checksums/CHECKSUMS.txt) before validating.
- Report every problem by **record index and error type/count only** — never
  by author name, handle, or content. That's the same de-identification rule
  the rest of this repo follows.
- Exit 0 if the file is clean, exit 1 if any validation errors were found —
  so either can drop straight into a CI check.

## Python

Standard library only.

```bash
python3 tools/validate.py podawaa /path/to/podawaa2024.json --checksums checksums/CHECKSUMS.txt
python3 tools/validate.py hyperclapper /path/to/HyperClaper.json --checksums checksums/CHECKSUMS.txt
python3 tools/validate.py linkboost /path/to/LinkBoost-2025.json --checksums checksums/CHECKSUMS.txt
```

## C#

Requires the .NET 8 SDK. No third-party packages — `System.Text.Json` is
built in.

```bash
cd tools/csharp
dotnet run -- podawaa /path/to/podawaa2024.json --checksums ../../checksums/CHECKSUMS.txt
dotnet run -- hyperclapper /path/to/HyperClaper.json --checksums ../../checksums/CHECKSUMS.txt
dotnet run -- linkboost /path/to/LinkBoost-2025.json --checksums ../../checksums/CHECKSUMS.txt
```

`Validate.cs` uses `JsonDocument`, which loads the whole file into memory —
fine for these file sizes on a normal dev machine (budget a couple GB of RAM
for the ~220MB `podawaa2024.json`), but swap in a streaming `Utf8JsonReader`
if you point it at something much larger.

## Known data-quality findings (already surfaced by these validators)

Running the Python validator against the checksummed HyperClaper.json turns
up 632 type inconsistencies: `like_count`, `comment_count`, and
`impression_count` are stored as JSON floats (e.g. `5.0`) instead of
integers on a few hundred records. That's a real quirk of the source export,
not a validator bug — worth knowing about before doing arithmetic on those
fields downstream.

# De-identification tool

`tools/deidentify.py` (Python) and `tools/csharp/deidentify/` (C#) produce
a de-identified **copy** of one of the three source files, for your own
local use.

**Read this before trusting the output for anything sensitive.** Default
mode hashes direct identifiers (handles, real names, internal LinkedIn
URNs/IDs, profile links, photos) with SHA-256 and leaves post content
untouched. That stops casual browsing/grep from exposing an identity, but
it does **not** stop re-identification via the post content itself — a
distinctive sentence can be pasted into a search engine and traced back to
its author regardless of what happened to the identifier fields. This is
the same failure mode that de-anonymized the AOL search-log and Netflix
Prize datasets. Pass `--redact-content` to also strip post/comment content
fields entirely, which closes that gap at the cost of removing most of
what the data is useful for.

Quasi-identifiers (headline, occupation, location, country, follower
counts) are left untouched in both modes — see
[../docs/privacy.md](../docs/privacy.md) and
[../docs/research/demographics.md](../docs/research/demographics.md) for
why this repo never aggregates those beyond population-level statistics.

```bash
python3 tools/deidentify.py podawaa /path/to/podawaa2024.json /path/to/output.json
python3 tools/deidentify.py hyperclapper /path/to/HyperClaper.json /path/to/output.json --redact-content
python3 tools/deidentify.py linkboost /path/to/LinkBoost-2025.json /path/to/output.json --salt "$(openssl rand -hex 16)"

# or, C#:
cd tools/csharp/deidentify
dotnet run -- podawaa /path/to/podawaa2024.json /path/to/output.json
```

**This repo's own `.gitignore` blocks `*.json` output outside `schema/`
and `tests/fixtures/` for exactly this reason — the output of this tool is
never meant to be committed here or shared/published anywhere.** Run it
locally, use the output for your own analysis, and delete it when you're
done. See [CONTRIBUTING.md](../CONTRIBUTING.md) rule 1 ("no raw data") —
a de-identified derivative of the raw data is still a derivative of the
raw data, and default-mode output in particular is not safe to treat as
anonymous.
