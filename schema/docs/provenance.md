# Provenance

## Source sites

| Dataset | Reported source | Reported collection method |
|---|---|---|
| `podawaa2024.json` | podawaa.com; also archived on Harvard Dataverse (see [Citations](#citations) below) | Navigated to the site directly and captured the resulting data to a local server |
| `HyperClaper.json` | hyperclapper.com | Navigated to the site directly and captured the resulting data to a local server |
| `LinkBoost-2025.json` | Not yet stated | Not yet stated |

The first two entries are **STATED** — asserted by whoever collected the
data, not independently verified by this repo. `LinkBoost-2025.json`'s
source and collection method haven't been provided yet; this repo isn't
filling in "linkboost.com" as a guess just because it matches the filename
— see [limitations.md](limitations.md) for why guessing at provenance isn't
how this repo operates. If you can confirm where and how this file was
obtained, that goes here as STATED, same as the other two.

This repo has no way to confirm, from the files themselves, which site a
given record actually came from, what specific requests were made to
obtain it, or when collection occurred. Treat any reported source as the
reported origin, not a confirmed chain of custody.

## Citations

**`podawaa2024.json`** — **CORROBORATED**. This file's sha256
(`2d64e4b274c1b238399a6b1d578b951cac9d5035a980ab70d4c3d66efffb4214`, see
[checksums/CHECKSUMS.txt](../checksums/CHECKSUMS.txt)) matches the checksum
published for `podawaa2024_fixed.json` by the SPOTAPOD companion repo, which
identifies that file as archived on Harvard Dataverse:

> Hall, Daniel. "LinkedIn posts using fake socials." Harvard Dataverse, 2026.
> `doi:10.7910/DVN/WD9AUR`
> https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/WD9AUR

A matching sha256 across independently-obtained copies is about as strong a
corroboration as a file hash can give — it means this repo's copy and the
Dataverse-archived copy are byte-for-byte identical.

**`HyperClaper.json`** — **no citation added**. Nothing about this file
supports linking it to the Dataverse record above: its structure, schema,
and reported source (hyperclapper.com, see the table above) are entirely
different from `podawaa2024.json`, and no checksum or other evidence ties it
to that DOI or to Harvard Dataverse at all. If you have a citation for where
this specific file is archived, that's worth adding — but citing it to the
same Dataverse DOI as `podawaa2024.json` would be inaccurate, since nothing
here supports that connection.

## Candidate duplicate: a file named `hyperclapper-gamers.json`

A file compared against this repo's `HyperClaper.json` — referred to in
this repo as `hyperclapper-gamers.json` at the requester's choice — was
checked for a match. This is an **INFERENCE**, not a CORROBORATED
match — recorded here because it bears directly on how much independent
weight `HyperClaper.json`'s figures should carry, not because the two
files have been shown to be identical. The name above is a labeling
choice made in this repo, not a claim about the file's original source or
collection method; nothing about the file's actual provenance changes.

- **Checksums differ.** `hyperclapper-gamers.json` hashes to
  `74986bcc38098cbaf8ed814544c17604541649f2cf24138270cc5ab9569805cb`
  (sha256) — it does not match the `HyperClaper.json` entry in
  [checksums/CHECKSUMS.txt](../checksums/CHECKSUMS.txt)
  (`913e28d4abd4e2b827d5c56b818b10581cef6880b645b10038ea02a108dc51f6`),
  even after normalizing JSON whitespace/key ordering to rule out a pure
  formatting difference. These are not the same bytes.
- **Structure and scale match exactly.** `hyperclapper-gamers.json` contains precisely
  49,369 post records and 702–703 distinct profiles by name — the same
  totals [baseline-profile.md](research/baseline-profile.md) reports for
  `HyperClaper.json` (49,369 records, 702 unique hashed authors), with the
  same field-completeness pattern (`like_count`/`comment_count` sparse in
  the mid-teens percent, `impression_count` around 2%).
- **Every existing scan reproduces exactly.** All 30 applicable analysis
  scripts in this repo were run against `hyperclapper-gamers.json` and
  compared line-by-line against the published `HyperClaper.json` figures
  in every `docs/research/*.md` page — zero discrepancies, including the
  per-account posting-velocity and month-by-month baseline-profile time
  series, which would be very unlikely to coincide across genuinely
  different data. See
  [hyperclapper-gamers-verification.md](research/hyperclapper-gamers-verification.md)
  for the full script-by-script breakdown.
- **Reading:** the size/structure match without a hash match is consistent
  with the same underlying export re-saved or re-scraped through a
  different process (different serialization, a fresh capture run, or a
  rename), but it is not proof of a common origin. Nothing in this repo
  treats `hyperclapper-gamers.json` and `HyperClaper.json` as confirmed-identical, and no
  figure anywhere in this repo has been computed from `hyperclapper-gamers.json` — every
  number attributed to `HyperClaper.json` in this repo was computed only
  from the file checksummed above.

## Terms of service

This repo does not assert, one way or the other, that collecting this data
complied with either site's terms of service. That's a legal conclusion
this repo isn't positioned to make: it would require the actual ToS text in
effect on the site at the time of collection, the specific technical method
used to capture the data (which this repo does not have independent
knowledge of beyond the STATED description above), and a legal analysis of
whether that method fell inside or outside what those terms permitted.
Terms of service for platforms like these commonly restrict automated
access or bulk data capture, so this is not a settled question, and no
document in this repo should be read as having settled it.

If you're relying on any of these datasets for anything beyond your own
private analysis, reviewing the actual current terms of service for the
sites they reportedly came from — and how they read at the time of
collection, if that's knowable — is worth doing before you do, ideally with
an actual lawyer rather than this repo's say-so.

## How this fits the rest of the repo

Consistent with [regulatory-context.md](regulatory-context.md) (this repo
makes no legal determination about 16 CFR § 465.8 violations) and
[limitations.md](limitations.md) (provenance of the underlying pod-tooling
claim is STATED, not VERIFIED), the collection-method claims on this page
get the same treatment: recorded as reported, not certified as accurate or
lawful.
