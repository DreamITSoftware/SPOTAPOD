#!/usr/bin/env python3
"""
cross_dataset_overlap_scan.py

Checks whether the same LinkedIn accounts appear in both HyperClapper
and LinkBoost-2025 by hashing each dataset's account identifiers and
comparing the hash sets. This is different in kind from every other
scan in this repo -- it's not a content keyword scan, it's a structural
question about whether two commercial engagement-pod tools draw from
the same or different user populations.

PRIVACY: every identifier is hashed (SHA-256, lowercased/stripped)
immediately upon extraction and never held or printed in plaintext.
Only the size of each hash set and the size of their intersection are
ever reported -- never which accounts overlap, if any do.

Both datasets use the same LinkedIn vanity-username namespace:
HyperClapper's profile.linkedin_data.public_identifier field, and a
username extracted from LinkBoost-2025's liProfileLink field (a
linkedin.com/in/<username> URL). podawaa2024 is not included in this
comparison -- it identifies authors by AuthorPublicIdentifier, which on
inspection is a different, non-comparable identifier scheme from the
other two files' vanity usernames.

Usage:
    python3 cross_dataset_overlap_scan.py /path/to/HyperClaper.json /path/to/LinkBoost-2025.json
"""
import sys
import json
import argparse
import re
import hashlib


def h(s):
    return hashlib.sha256(s.strip().lower().encode("utf-8")).hexdigest()


VANITY_PATTERN = re.compile(r"linkedin\.com/in/([a-zA-Z0-9\-]+)")


def load_hyperclapper_hashes(path):
    with open(path, "r", encoding="utf-8") as f:
        posts = json.load(f)["data"]["post"]
    hashes = set()
    for p in posts:
        ld = (p.get("profile") or {}).get("linkedin_data") or {}
        pid = ld.get("public_identifier")
        if pid:
            hashes.add(h(pid))
    return hashes


def load_linkboost_hashes(path):
    with open(path, "r", encoding="utf-8") as f:
        recs = json.load(f)
    hashes = set()
    for r in recs:
        lp = r.get("liProfileLink", "") or ""
        m = VANITY_PATTERN.search(lp)
        if m:
            hashes.add(h(m.group(1)))
    return hashes


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("hyperclapper_path")
    ap.add_argument("linkboost_path")
    args = ap.parse_args()

    hc_hashes = load_hyperclapper_hashes(args.hyperclapper_path)
    lb_hashes = load_linkboost_hashes(args.linkboost_path)
    overlap = hc_hashes & lb_hashes

    print("=" * 60)
    print("CROSS-DATASET ACCOUNT OVERLAP (hashed identifiers only)")
    print("=" * 60)
    print(f"HyperClapper distinct hashed accounts:   {len(hc_hashes):,}")
    print(f"LinkBoost-2025 distinct hashed accounts: {len(lb_hashes):,}")
    print(f"Overlapping hashed accounts:             {len(overlap):,}")
    if hc_hashes:
        print(f"Overlap as % of HyperClapper accounts:   {len(overlap)/len(hc_hashes)*100:.2f}%")
    if lb_hashes:
        print(f"Overlap as % of LinkBoost-2025 accounts: {len(overlap)/len(lb_hashes)*100:.2f}%")
    print()
    print("No account identifier, overlapping or otherwise, is ever printed by")
    print("this script -- only aggregate set sizes and the overlap count.")


if __name__ == "__main__":
    main()
