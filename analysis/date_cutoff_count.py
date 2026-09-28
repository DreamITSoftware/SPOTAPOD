#!/usr/bin/env python3
"""
date_cutoff_count.py

Aggregate-only count of how many records in each dataset fall before or
after a given cutoff date. Reports totals per dataset; never prints or
exports any individual record, timestamp, or identifier.

This does NOT determine whether any record represents a transaction that
violates 16 CFR 465.8 (see ../docs/regulatory-context.md). It reports a
date split only. Whether fabricated-influence records on either side of
that split reflect an actual sale of a fake indicator, who the parties
were, and whether that sale meets the rule's other elements, is a legal
determination this script cannot make and does not attempt.

Dataset-specific caveats:
  - podawaa2024.json: the date used is decoded from `linkedinPostId`
    (Snowflake-style bit layout, see ../docs/method.md). This is an
    INFERENCE about the ID encoding, not confirmed by LinkedIn
    documentation, and approximates the POST's own publish date.
  - HyperClapper.json: the date used is `created_at`, which is when the
    pod tool CAPTURED the record, not necessarily when the underlying
    post was originally published. Not directly comparable to
    podawaa2024's decoded post date.
  - LinkBoost-2025.json: has no dedicated timestamp field, but each
    record's `Url` embeds a LinkedIn activity URN
    (`urn:li:activity:<id>`) identifying the TARGET post, and that id
    uses the same Snowflake-style bit layout as podawaa2024's
    linkedinPostId, so the same decode method is applied here (also
    INFERENCE). This approximates the target post's own publish date,
    not when LinkBoost's operator account acted on it. Because many
    records target the same post, this dataset's counts include both a
    per-record split and a per-unique-target-post split.

Usage:
    python3 date_cutoff_count.py /path/to/podawaa2024.json \\
        /path/to/HyperClapper.json /path/to/LinkBoost-2025.json \\
        --cutoff 2024-10-22
"""
import sys
import json
import re
import argparse
import datetime

ACTIVITY_URN_RE = re.compile(r"urn:li:activity:(\d+)")


def decode_snowflake_date(post_id):
    """Shared decode for both podawaa2024's linkedinPostId and the
    activity id embedded in LinkBoost-2025's Url field. See docs/method.md."""
    try:
        ms = post_id >> 22
        return datetime.datetime.fromtimestamp(ms / 1000, datetime.timezone.utc)
    except Exception:
        return None


# Back-compat alias; podawaa2024 and LinkBoost-2025 use the same decode.
decode_podawaa_date = decode_snowflake_date


def count_podawaa(path, cutoff):
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    posts = data["Posts"]
    total = len(posts)
    after = 0
    undecodable = 0
    for p in posts:
        pid = p.get("linkedinPostId")
        dt = decode_podawaa_date(pid) if pid is not None else None
        if dt is None:
            undecodable += 1
            continue
        if dt > cutoff:
            after += 1
    return total, after, undecodable


def count_hyperclapper(path, cutoff):
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    posts = data["data"]["post"]
    total = len(posts)
    after = 0
    missing = 0
    for p in posts:
        ca = p.get("created_at")
        if not ca:
            missing += 1
            continue
        try:
            dt = datetime.datetime.fromisoformat(ca.replace("Z", "+00:00"))
            if dt.tzinfo is None:
                dt = dt.replace(tzinfo=datetime.timezone.utc)
        except Exception:
            missing += 1
            continue
        if dt > cutoff:
            after += 1
    return total, after, missing


def count_linkboost(path, cutoff):
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    total = len(data)
    after = 0
    undecodable = 0
    posts_after = set()
    posts_before = set()
    for rec in data:
        m = ACTIVITY_URN_RE.search(rec.get("Url") or "")
        if not m:
            undecodable += 1
            continue
        pid = int(m.group(1))
        dt = decode_snowflake_date(pid)
        if dt is None:
            undecodable += 1
            continue
        if dt > cutoff:
            after += 1
            posts_after.add(pid)
        else:
            posts_before.add(pid)
    return total, after, undecodable, len(posts_after), len(posts_before)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("podawaa_path")
    parser.add_argument("hyperclapper_path")
    parser.add_argument("linkboost_path")
    parser.add_argument("--cutoff", default="2024-10-22",
                         help="Cutoff date, YYYY-MM-DD (UTC). Default: 2024-10-22")
    args = parser.parse_args()

    cutoff_date = datetime.datetime.strptime(args.cutoff, "%Y-%m-%d").replace(
        tzinfo=datetime.timezone.utc
    )

    total, after, undecodable = count_podawaa(args.podawaa_path, cutoff_date)
    print(
        f"podawaa2024.json: {total} total records | {after} decoded after "
        f"{args.cutoff} | {undecodable} without a decodable linkedinPostId"
    )

    total_hc, after_hc, missing_hc = count_hyperclapper(args.hyperclapper_path, cutoff_date)
    print(
        f"HyperClapper.json: {total_hc} total records | {after_hc} captured "
        f"(created_at) after {args.cutoff} | {missing_hc} without a usable created_at"
    )

    total_lb, after_lb, undecodable_lb, posts_after_lb, posts_before_lb = count_linkboost(
        args.linkboost_path, cutoff_date
    )
    print(
        f"LinkBoost-2025.json: {total_lb} total records | {after_lb} decoded "
        f"(via Url's activity id) after {args.cutoff} | {undecodable_lb} without "
        f"a decodable activity id | unique target posts: {posts_after_lb} after, "
        f"{posts_before_lb} before"
    )


if __name__ == "__main__":
    main()
