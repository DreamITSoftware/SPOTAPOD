#!/usr/bin/env python3
"""
validate.py

Structural / type validation for podawaa2024.json and HyperClaper.json.
Reports errors by record INDEX and error type/count only — never prints
an author name, handle, profile URL, or post content, consistent with the
de-identification rule used everywhere else in this repo.

Usage:
    python3 tools/validate.py podawaa /path/to/podawaa2024.json
    python3 tools/validate.py hyperclapper /path/to/HyperClaper.json
    python3 tools/validate.py podawaa /path/to/podawaa2024.json --checksums checksums/CHECKSUMS.txt

Exit code: 0 if no errors, 1 if any validation errors were found.
"""
import sys
import json
import argparse
import hashlib
import datetime
from collections import Counter


def sha256_of(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def check_checksum(path, checksums_path):
    expected = None
    fname = path.split("/")[-1]
    try:
        with open(checksums_path, "r") as f:
            for line in f:
                parts = line.split()
                if len(parts) == 2 and parts[1] == fname:
                    expected = parts[0]
    except FileNotFoundError:
        print(f"  [WARN] checksums file not found: {checksums_path}")
        return
    if expected is None:
        print(f"  [WARN] no checksum entry found for {fname} in {checksums_path}")
        return
    actual = sha256_of(path)
    if actual == expected:
        print(f"  [OK] sha256 matches: {actual}")
    else:
        print(f"  [MISMATCH] expected {expected}, got {actual}")


def is_int(v):
    return isinstance(v, int) and not isinstance(v, bool)


def validate_podawaa(path):
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)

    errors = Counter()
    error_examples = {}  # error type -> first few record indices
    n_records = 0

    if not isinstance(data, dict) or "Posts" not in data:
        print("  [FATAL] top-level object missing required key 'Posts'")
        return False

    posts = data["Posts"]
    if not isinstance(posts, list):
        print("  [FATAL] 'Posts' is not an array")
        return False

    n_records = len(posts)

    def flag(idx, err):
        errors[err] += 1
        error_examples.setdefault(err, [])
        if len(error_examples[err]) < 5:
            error_examples[err].append(idx)

    for i, rec in enumerate(posts):
        if not isinstance(rec, dict):
            flag(i, "record_not_object")
            continue

        if "linkedinPostId" in rec and rec["linkedinPostId"] is not None:
            if not is_int(rec["linkedinPostId"]):
                flag(i, "linkedinPostId_wrong_type")

        if "Content" in rec and rec["Content"] is not None:
            if not isinstance(rec["Content"], str):
                flag(i, "Content_wrong_type")

        if "AuthorPublicIdentifier" in rec and rec["AuthorPublicIdentifier"] is not None:
            if not isinstance(rec["AuthorPublicIdentifier"], str):
                flag(i, "AuthorPublicIdentifier_wrong_type")

        if "Likes" not in rec:
            flag(i, "Likes_missing")
        elif not is_int(rec["Likes"]):
            flag(i, "Likes_wrong_type")
        elif rec["Likes"] < 0:
            flag(i, "Likes_negative")

        if "Views" not in rec:
            flag(i, "Views_missing")
        elif not is_int(rec["Views"]):
            flag(i, "Views_wrong_type")
        elif rec["Views"] < 0:
            flag(i, "Views_negative")

    return report(n_records, errors, error_examples)


def validate_hyperclapper(path):
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)

    errors = Counter()
    error_examples = {}

    if not isinstance(data, dict) or "data" not in data or not isinstance(data["data"], dict):
        print("  [FATAL] top-level object missing required key 'data'")
        return False
    posts = data["data"].get("post")
    if not isinstance(posts, list):
        print("  [FATAL] 'data.post' is not an array")
        return False

    n_records = len(posts)

    def flag(idx, err):
        errors[err] += 1
        error_examples.setdefault(err, [])
        if len(error_examples[err]) < 5:
            error_examples[err].append(idx)

    required_bool_fields = ["comment", "like"]
    required_str_fields = ["post_url", "created_at"]
    optional_int_fields = ["like_count", "impression_count", "comment_count"]

    for i, rec in enumerate(posts):
        if not isinstance(rec, dict):
            flag(i, "record_not_object")
            continue

        for field in required_bool_fields:
            if field not in rec:
                flag(i, f"{field}_missing")
            elif not isinstance(rec[field], bool):
                flag(i, f"{field}_wrong_type")

        for field in required_str_fields:
            if field not in rec or rec[field] in (None, ""):
                flag(i, f"{field}_missing")
            elif not isinstance(rec[field], str):
                flag(i, f"{field}_wrong_type")

        ca = rec.get("created_at")
        if isinstance(ca, str):
            try:
                datetime.datetime.fromisoformat(ca.replace("Z", "+00:00"))
            except ValueError:
                flag(i, "created_at_unparseable")

        for field in optional_int_fields:
            if field in rec and rec[field] is not None:
                if not is_int(rec[field]):
                    flag(i, f"{field}_wrong_type")
                elif rec[field] < 0:
                    flag(i, f"{field}_negative")

        profile = rec.get("profile")
        if profile is not None and not isinstance(profile, dict):
            flag(i, "profile_wrong_type")

    return report(n_records, errors, error_examples)


def report(n_records, errors, error_examples):
    print(f"  Records checked: {n_records:,}")
    if not errors:
        print("  [PASS] no validation errors found")
        return True

    total_errors = sum(errors.values())
    print(f"  [FAIL] {total_errors:,} validation errors across {len(errors)} error types:")
    for err, count in errors.most_common():
        examples = error_examples[err]
        print(f"    {err:<32} {count:,} occurrences (e.g. record indices {examples})")
    return False


def validate_linkboost(path):
    """Validates a LinkBoost-2025-style export. SuccessfullLikes and
    SuccessfullComments are 'indicators of social media influence' under
    16 CFR § 465.1(j), which 16 CFR § 465.8 governs — see
    ../docs/regulatory-context.md. This function makes no determination
    about whether any record's counts were fake or used to violate that
    rule; it only checks structural/type conformance."""
    with open(path, "r", encoding="utf-8") as f:
        records = json.load(f)

    if not isinstance(records, list):
        print("  [FATAL] top-level value is not an array")
        return False

    errors = Counter()
    error_examples = {}
    n_records = len(records)

    def flag(idx, err):
        errors[err] += 1
        error_examples.setdefault(err, [])
        if len(error_examples[err]) < 5:
            error_examples[err].append(idx)

    required_str_fields = ["Id", "ObjectUrn", "Url", "piFirstName", "piLastName", "UserId"]
    optional_str_fields = ["FirstName", "LastName", "Occupation", "DashEntityUrn",
                            "Comment", "liProfileLink", "liUrl", "liDigitalMarketer",
                            "Title", "country"]
    required_int_fields = ["SuccessfullLikes", "SuccessfullComments", "VolumeId"]

    for i, rec in enumerate(records):
        if not isinstance(rec, dict):
            flag(i, "record_not_object")
            continue

        for field in required_str_fields:
            if field not in rec or rec[field] in (None, ""):
                flag(i, f"{field}_missing")
            elif not isinstance(rec[field], str):
                flag(i, f"{field}_wrong_type")

        for field in optional_str_fields:
            if field in rec and rec[field] is not None and not isinstance(rec[field], str):
                flag(i, f"{field}_wrong_type")

        for field in required_int_fields:
            if field not in rec:
                flag(i, f"{field}_missing")
            elif not is_int(rec[field]):
                flag(i, f"{field}_wrong_type")
            elif rec[field] < 0:
                flag(i, f"{field}_negative")

    return report(n_records, errors, error_examples)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("dataset", choices=["podawaa", "hyperclapper", "linkboost"])
    ap.add_argument("path")
    ap.add_argument("--checksums", default=None,
                     help="Path to CHECKSUMS.txt to verify the file's sha256 before validating")
    args = ap.parse_args()

    print(f"Validating {args.dataset}: {args.path}")

    if args.checksums:
        check_checksum(args.path, args.checksums)

    if args.dataset == "podawaa":
        ok = validate_podawaa(args.path)
    elif args.dataset == "hyperclapper":
        ok = validate_hyperclapper(args.path)
    else:
        ok = validate_linkboost(args.path)

    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
