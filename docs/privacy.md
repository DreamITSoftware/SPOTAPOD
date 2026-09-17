# Privacy and PII

## What personal data is in these files

Both source files contain personal data about real, identifiable individuals
who did not consent to appearing in either dataset or in this repo.

| Field | File | PII category |
|---|---|---|
| `AuthorPublicIdentifier` | podawaa2024.json | Direct identifier (LinkedIn profile slug) |
| `profile.name` / `linkedin_data.fullName` | HyperClaper.json | Direct identifier (real name) |
| `linkedin_data.public_identifier` | HyperClaper.json | Direct identifier (LinkedIn profile slug) |
| `linkedin_data.linkedin_profile_link` | HyperClaper.json | Direct identifier (resolves straight to the person's profile) |
| `linkedin_data.linkedin_profile_id` | HyperClaper.json | Direct identifier (internal LinkedIn ID) |
| `profile_picture` / `linkedin_data.profilePicture` | HyperClaper.json | Biometric-adjacent identifier (a photo of the person's face) |
| `linkedin_data.headline` / `jobTitle` / `company` / `companies` / `school` / `location` | HyperClaper.json | Quasi-identifiers — combinable to re-identify someone even without the direct identifiers above |
| `FirstName` / `LastName` / `piFirstName` / `piLastName` | LinkBoost-2025.json | Direct identifier (real name) |
| `DashEntityUrn` / `ObjectUrn` | LinkBoost-2025.json | Direct identifier (LinkedIn internal URN, resolves to a specific profile) |
| `liProfileLink` | LinkBoost-2025.json | Direct identifier (embeds both a profile URN and a real name) |
| `Occupation` | LinkBoost-2025.json | Quasi-identifier — a specific bio/headline line is often unique enough to re-identify someone alone |
| `country` | LinkBoost-2025.json | Quasi-identifier in combination with other fields |
| `Content` / `post_title` / `Title` / `Comment` | All three | Not PII on its own in most cases, but first-person posts/comments can incidentally disclose health, family, immigration, or other sensitive details about the author or people they mention |

Taken together, `HyperClaper.json` and `LinkBoost-2025.json` are enough to
fully de-anonymize the records in them — real names and, for HyperClapper, a
photo — no inference required. `podawaa2024.json` is one step removed (a
handle, not a name or photo) but a handle is still a direct identifier: it
resolves to `linkedin.com/in/<handle>` and the real person behind it.

## How this repo handles it

- **No PII field is ever read into a variable that gets printed, logged, or
  written to a file, anywhere in this repo.** The only PII fields any script
  touches at all are `AuthorPublicIdentifier`, `public_identifier`,
  `ObjectUrn`, and `UserId`, and those are passed through
  `hashlib.sha256` / `SHA256.Create()` the instant they're read, used only
  as a dictionary key for counting, and go out of scope immediately after.
  Name, photo, profile link, internal profile ID, headline, company,
  school, location, and occupation are never read by any script here at
  all — see the "never read" notes in
  [data-dictionary.md](data-dictionary.md).
- **A SHA-256 hash of a real identifier is still personal data**, strictly
  speaking (it's a deterministic function of one), so this repo does not
  claim the hashing achieves anonymization in a legal sense — only that it
  prevents *this repo's own output* from re-exposing any identifier. If you
  extend these scripts, don't write the hash-to-original mapping anywhere,
  and don't assume the hash is safe to publish or share outside your own
  analysis.
- **No output in this repo — profiles, figures, docs, validator reports —
  contains a name, handle, photo, URL, or content string tied to a specific
  individual.** Validator and profiler output is scoped to counts, ratios,
  and (for the validators) record *index* — a position in the file, not an
  identity.
- **The raw source files are never included in this repo** and are not meant
  to be. Only checksums (`checksums/CHECKSUMS.txt`), schemas, scripts, and
  aggregate output live here. If you're storing your own copies of
  `podawaa2024.json`, `HyperClaper.json`, or `LinkBoost-2025.json` locally,
  treat them as sensitive: keep them out of version control, off shared
  drives, and delete them when you're done with them.

## What this repo will not do

See [limitations.md](limitations.md) for the full reasoning, but concretely:
this repo will not add a per-author lookup, a browsable table keyed by name
or handle, or any feature that lets someone search "is this person in the
dataset." That's true even in a private/internal build — the moment a tool
can answer that question for one person, it can answer it for everyone in
any of the three files,
and this repo isn't set up to handle the correction, consent, or
due-process obligations that come with that.

## If you're handling the raw files yourself

A few practical points, not legal advice:

- Both files likely fall under GDPR (if any subjects are in the EU/UK) and/or
  US state privacy laws (e.g. CCPA if any subjects are California
  residents) as personal data, regardless of where you're located or where
  you got the files.
- "Publicly available on LinkedIn" does not mean freely reusable for a
  different purpose than the person posted it for — most privacy regimes
  distinguish between data being public and data being *repurposed*, and
  pairing public posts with an accusation of deceptive behavior is a
  different purpose than the original post. Separately, note that
  [16 CFR § 465.8](regulatory-context.md) itself only prohibits *selling,
  distributing, purchasing, or procuring* fake indicators — appearing in a
  dataset because your public metrics look unusual is not the same as
  having engaged in conduct the rule covers, and this repo does not treat
  it as such (see [limitations.md](limitations.md)).
- If someone identified in either file asks you to remove their data or
  explain what you're doing with it, having a real answer ready (what you
  keep, what you don't, for how long, and why) is worth doing before you
  need it, not after.
- If you plan to publish anything beyond this repo's own aggregate-only
  output — including sharing a raw or lightly-processed copy of either file
  with anyone else — that's a materially different, higher-risk step than
  what this repo does, and worth running past someone with actual legal
  expertise in your jurisdiction first.
