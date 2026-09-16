#!/usr/bin/env python3
"""
cybersecurity_anomaly_scan.py

Cross-tabulates cybersecurity-related content against the same
engagement-anomaly indicators already used in profile_podawaa.py and
profile_hyperclapper.py (zero views with likes present, likes exceeding
views, extreme like/view ratio, reciprocal like+comment pairing, zero
impressions). Same discipline as every other scan in this repo:
aggregate counts only, no record, author, or matched text ever printed.

LinkBoost-2025 is not supported here. It has no per-record engagement
fields to cross-reference against; every record there is, by the
dataset's own construction, a logged successful pod action, so a
per-record anomaly rate isn't a meaningful thing to compute for it.

IMPORTANT: an elevated anomaly rate for a content category is a
population-level pattern, not identification of any specific account or
post as fraudulent. This script cannot and does not determine which
individual posts within a category are anomalous versus which authors
happen to write about that topic and also happen to have organically
unusual engagement. See docs/research/cybersecurity-anomaly.md.

Usage:
    python3 cybersecurity_anomaly_scan.py podawaa /path/to/podawaa2024.json
    python3 cybersecurity_anomaly_scan.py hyperclapper /path/to/HyperClaper.json
"""
import sys
import json
import argparse
import re

CYBER_PAT = re.compile(
    r"\bcybersecurity\b|\bcyber security\b|\binfosec\b|\binformation security\b|"
    r"\bpenetration testing\b|\bpen test(ing)?\b|\bransomware\b|\bphishing\b|"
    r"\bzero-?day\b|\bCISO\b|\bthreat intelligence\b|\bmalware\b|\bfirewall\b|"
    r"\bvulnerabilit(y|ies)\b|\bdata breach\b|\bendpoint security\b|\bincident response\b|"
    r"\bSOC 2\b|\bsecurity operations center\b",
    re.IGNORECASE,
)


def scan_podawaa(path):
    with open(path, "r", encoding="utf-8") as f:
        posts = json.load(f)["Posts"]
    n = len(posts)
    cyber_posts = [p for p in posts if p.get("Content") and CYBER_PAT.search(p.get("Content"))]
    cyber_n = len(cyber_posts)

    def rates(plist):
        zero_view_liked = sum(1 for p in plist if (p.get("Views") or 0) == 0 and (p.get("Likes") or 0) > 0)
        likes_gt_views = sum(1 for p in plist if (p.get("Likes") or 0) > (p.get("Views") or 0))
        extreme = sum(1 for p in plist if (p.get("Views") or 0) > 0 and (p.get("Likes") or 0) / (p.get("Views") or 1) > 0.15)
        return zero_view_liked, likes_gt_views, extreme

    zv_all, lgv_all, ex_all = rates(posts)
    zv_cy, lgv_cy, ex_cy = rates(cyber_posts)

    print(f"podawaa2024 ({n:,} total records)")
    print(f"Cybersecurity-related posts: {cyber_n:,} ({cyber_n/n*100:.3f}%)")
    print()
    print("Anomaly indicator                     All posts (baseline)   Cybersecurity posts only")
    print(f"Zero views with likes present          {zv_all/n*100:6.1f}%                {zv_cy/cyber_n*100:6.1f}%")
    print(f"Likes exceed views                     {lgv_all/n*100:6.2f}%               {lgv_cy/cyber_n*100:6.2f}%")
    print(f"Like/view ratio exceeds 15%            {ex_all/n*100:6.2f}%               {ex_cy/cyber_n*100:6.2f}%")
    print()


def scan_hyperclapper(path):
    with open(path, "r", encoding="utf-8") as f:
        posts = json.load(f)["data"]["post"]
    n = len(posts)
    cyber_posts = [p for p in posts if p.get("post_title") and CYBER_PAT.search(p.get("post_title"))]
    cyber_n = len(cyber_posts)

    def rates(plist):
        reciprocal = sum(1 for p in plist if p.get("like") and p.get("comment"))
        zero_impr = sum(1 for p in plist if (p.get("impression_count") or 0) == 0)
        return reciprocal, zero_impr, len(plist)

    r_all, z_all, n_all = rates(posts)
    r_cy, z_cy, n_cy = rates(cyber_posts)

    print(f"HyperClaper ({n:,} total records)")
    print(f"Cybersecurity-related posts: {cyber_n:,} ({cyber_n/n*100:.3f}%)")
    print()
    print("Anomaly indicator                     All posts (baseline)   Cybersecurity posts only")
    if n_cy:
        print(f"Reciprocal like+comment pair           {r_all/n_all*100:6.1f}%                {r_cy/n_cy*100:6.1f}%")
        print(f"Zero impressions                       {z_all/n_all*100:6.1f}%                {z_cy/n_cy*100:6.1f}%")
    print()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("dataset", choices=["podawaa", "hyperclapper"],
                     help="LinkBoost-2025 is not supported -- no per-record engagement fields to cross-reference")
    ap.add_argument("path")
    args = ap.parse_args()
    if args.dataset == "podawaa":
        scan_podawaa(args.path)
    else:
        scan_hyperclapper(args.path)


if __name__ == "__main__":
    main()
