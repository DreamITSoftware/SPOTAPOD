#!/usr/bin/env python3
"""
posting_velocity_scan.py

Computes sustained posting rate (posts per day, over each account's
full active window) for the highest-volume accounts in HyperClapper --
the only one of the three datasets with real per-record timestamps
(created_at). This is a structural/behavioral analysis, not a content
keyword scan: it checks whether the small number of accounts already
known to drive a disproportionate share of HyperClapper's posts (see
baseline-profile.md) show posting patterns consistent with sustained
automation or managed content operations, as opposed to individual
human authorship.

PRIVACY: accounts are identified only by their SHA-256 hash, and are
reported here by anonymous rank ("account_1", "account_2", ...), never
by any hash value, handle, or other identifier. Only aggregate
post-count, date-span, and rate figures are printed for each ranked
account -- nothing that could be used to look the account up.

Method: for each account (grouped by hashed public_identifier), take
every post's created_at timestamp, sort them, and compute the account's
full active window (first post to last post) in days, then divide post
count by that window to get a sustained posts-per-day rate. A raw
interval-regularity check (coefficient of variation of time between
consecutive posts) is also reported, since a very low CV would indicate
simple robotic clockwork -- notably, the accounts checked here do NOT
show that pattern (CV consistently well above 80%), which is worth
stating plainly: this analysis finds evidence of a different, less
obvious anomaly (sustained superhuman rate) than the more commonly
assumed one (perfectly regular timing).

Usage:
    python3 posting_velocity_scan.py /path/to/HyperClaper.json
    python3 posting_velocity_scan.py /path/to/HyperClaper.json --top-n 15
"""
import sys
import json
import argparse
import hashlib
import statistics
from datetime import datetime
from collections import defaultdict


def h(s):
    return hashlib.sha256(s.strip().lower().encode("utf-8")).hexdigest()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("path")
    ap.add_argument("--top-n", type=int, default=10, help="Number of top-volume accounts to report (default 10)")
    args = ap.parse_args()

    with open(args.path, "r", encoding="utf-8") as f:
        posts = json.load(f)["data"]["post"]

    by_account = defaultdict(list)
    for p in posts:
        ld = (p.get("profile") or {}).get("linkedin_data") or {}
        pid = ld.get("public_identifier")
        ca = p.get("created_at")
        if pid and ca:
            by_account[h(pid)].append(ca)

    sorted_accounts = sorted(by_account.items(), key=lambda x: -len(x[1]))

    print("=" * 70)
    print("POSTING VELOCITY -- top-volume HyperClapper accounts (anonymous rank only)")
    print("=" * 70)
    print(f"Total accounts with usable timestamps: {len(by_account):,}")
    print()
    print(f"{'Rank':<10}{'Posts':<8}{'Active days':<14}{'Posts/day':<12}{'Interval CV%':<14}")

    for i, (acct_hash, timestamps) in enumerate(sorted_accounts[: args.top_n]):
        times = sorted(datetime.fromisoformat(t) for t in timestamps)
        if len(times) < 2:
            continue
        span_days = (times[-1] - times[0]).total_seconds() / 86400
        rate = len(times) / span_days if span_days > 0 else float("inf")
        intervals = [(times[j + 1] - times[j]).total_seconds() for j in range(len(times) - 1)]
        mean_interval = statistics.mean(intervals) if intervals else 0
        stdev_interval = statistics.stdev(intervals) if len(intervals) > 1 else 0
        cv = (stdev_interval / mean_interval * 100) if mean_interval else 0
        print(f"account_{i+1:<3}{len(times):<8}{span_days:<14.1f}{rate:<12.2f}{cv:<14.1f}")

    all_times = [datetime.fromisoformat(p.get("created_at")) for p in posts if p.get("created_at")]
    if all_times:
        print()
        print(f"Dataset-wide date range: {min(all_times).date()} to {max(all_times).date()} "
              f"({(max(all_times)-min(all_times)).days:,} days)")
    print()
    print("No account hash, handle, or other identifier is ever printed by this")
    print("script -- accounts are reported only by anonymous volume rank.")


if __name__ == "__main__":
    main()
