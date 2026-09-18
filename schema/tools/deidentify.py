#!/usr/bin/env python3
"""
deidentify.py

Produces a de-identified COPY of one of the three source files, for your
own local use. This script is meant to run on your machine against your
own copy of the data — its output is NOT something this repo ever
generates, stores, or ships, and it should not be committed to git or
shared/published anywhere. See tools/README.md.

What "de-identified" means here, precisely — read this before trusting
the output for anything sensitive:

  DEFAULT MODE hashes direct identifiers (handles, real names, internal
  LinkedIn URNs/IDs, profile links, photos) with SHA-256 and leaves post
  content untouched. This stops casual browsing/grep from exposing an
  identity, but it does NOT stop re-identification via the post content
  itself — a distinctive sentence in a post's text can be pasted into a
  search engine and traced back to its original author regardless of
  what happened to the identifier fields. This is the same failure mode
  that de-anonymized the AOL search-log and Netflix Prize datasets:
  removing the ID column doesn't remove identifiability when the
  retained content is unique enough to fingerprint.

  --redact-content ALSO removes post/comment content fields entirely
  (Content / post_title / Title / Comment), closing that gap — at the
  cost of removing most of what the data is useful for. Use this mode if
  you actually need re-identification-resistant output, not just
  identifier-scrubbed output.

  Quasi-identifiers (headline, occupation, location, country, follower
  counts, etc.) are left untouched in both modes — combinations of these
  can still narrow to an individual. See docs/privacy.md and
  docs/demographics.md for why this repo never aggregates those beyond
  population-level statistics.

Usage:
    python3 deidentify.py podawaa /path/to/podawaa2024.json /path/to/output.json
    python3 deidentify.py hyperclapper /path/to/HyperClaper.json /path/to/output.json
    python3 deidentify.py linkboost /path/to/LinkBoost-2025.json /path/to/output.json

Options:
    --redact-content     Also strip post/comment content fields (see above)
    --salt SALT          Salt the hash (default: unsalted, so the same real
                          identifier always maps to the same hash within and
                          across runs — needed if you want to group/count by
                          hashed identity later). A salted hash is NOT
                          reproducible across runs unless you reuse the same
                          salt value yourself.
"""
import sys
import json
import argparse
import hashlib


def make_hasher(salt):
    def h(value):
        if value is None or value == "":
            return value
        raw = f"{salt}:{value}" if salt else str(value)
        return "anon_" + hashlib.sha256(raw.encode("utf-8")).hexdigest()[:16]
    return h


def deidentify_podawaa(data, hash_fn, redact_content):
    stats = {"identifiers_hashed": 0, "content_redacted": 0}
    for rec in data.get("Posts", []):
        if rec.get("AuthorPublicIdentifier"):
            rec["AuthorPublicIdentifier"] = hash_fn(rec["AuthorPublicIdentifier"])
            stats["identifiers_hashed"] += 1
        if redact_content and rec.get("Content") is not None:
            rec["Content"] = None
            stats["content_redacted"] += 1
    return data, stats


def deidentify_hyperclapper(data, hash_fn, redact_content):
    stats = {"identifiers_hashed": 0, "content_redacted": 0}
    for rec in data.get("data", {}).get("post", []):
        profile = rec.get("profile") or {}
        if profile.get("name"):
            profile["name"] = hash_fn(profile["name"])
            stats["identifiers_hashed"] += 1
        if profile.get("profile_picture"):
            profile["profile_picture"] = hash_fn(profile["profile_picture"])
            stats["identifiers_hashed"] += 1
        ld = profile.get("linkedin_data") or {}
        for field in ("fullName", "public_identifier", "linkedin_profile_link",
                      "linkedin_profile_id", "profilePicture"):
            if ld.get(field):
                ld[field] = hash_fn(ld[field])
                stats["identifiers_hashed"] += 1
        if redact_content and rec.get("post_title") is not None:
            rec["post_title"] = None
            stats["content_redacted"] += 1
    return data, stats


def deidentify_linkboost(data, hash_fn, redact_content):
    stats = {"identifiers_hashed": 0, "content_redacted": 0}
    for rec in data:
        for field in ("FirstName", "LastName", "piFirstName", "piLastName",
                      "DashEntityUrn", "ObjectUrn", "liProfileLink",
                      "liDigitalMarketer", "UserId"):
            if rec.get(field):
                rec[field] = hash_fn(rec[field])
                stats["identifiers_hashed"] += 1
        if redact_content:
            for field in ("Title", "Comment"):
                if rec.get(field) is not None:
                    rec[field] = None
                    stats["content_redacted"] += 1
    return data, stats


HANDLERS = {
    "podawaa": deidentify_podawaa,
    "hyperclapper": deidentify_hyperclapper,
    "linkboost": deidentify_linkboost,
}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("dataset", choices=list(HANDLERS.keys()))
    ap.add_argument("input_path")
    ap.add_argument("output_path")
    ap.add_argument("--redact-content", action="store_true",
                     help="Also strip post/comment content fields (see module docstring)")
    ap.add_argument("--salt", default=None,
                     help="Salt for hashing (default: unsalted, reproducible across runs)")
    args = ap.parse_args()

    with open(args.input_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    hash_fn = make_hasher(args.salt)
    data, stats = HANDLERS[args.dataset](data, hash_fn, args.redact_content)

    with open(args.output_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False)

    print(f"De-identified copy written to {args.output_path}")
    print(f"  Identifiers hashed:  {stats['identifiers_hashed']:,}")
    print(f"  Content fields redacted: {stats['content_redacted']:,}")
    if not args.redact_content:
        print()
        print("  NOTE: post/comment content was left intact. This output is")
        print("  NOT re-identification-resistant on its own — see the module")
        print("  docstring. Re-run with --redact-content if you need that.")
    print()
    print("  Do not commit this output to git or share/publish it. See")
    print("  tools/README.md.")


if __name__ == "__main__":
    main()
