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
