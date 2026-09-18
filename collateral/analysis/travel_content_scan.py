#!/usr/bin/env python3
"""
travel_content_scan.py

Counts mentions of travel agencies/booking platforms and travel
destinations across post content in all three datasets. Same
discipline as every other scan in this repo: aggregate counts only, no
record, author, or matched text ever printed beyond the duplicate-
template check below.

Two known artifacts this script guards against or flags, found while
building it:

1. Duplicate-template inflation (the same safeguard used in
   nonprofit_content_scan.py and investment_vc_scan.py): reports
   distinct underlying text values alongside every raw count, and warns
   when a single repeated string accounts for 20%+ of matches. This
   caught a real one -- four LinkBoost-2025 "agency" counts (Expedia,
   Booking.com, TripAdvisor, Hotels.com, all showing exactly 48) turned
   out to be one AI-travel-tool ad post, boosted 47 times by pod
   actions, that happens to name-drop all four platforms.

2. Language artifact, not a template (no automated check catches this
   one -- it required reading a sample of the actual matching text):
   podawaa2024's "France" and "Paris" counts are inflated not by
   duplication (7,695 of 8,010 France matches are genuinely distinct
   posts) but by French-language content discussing French domestic
   topics -- workplace issues, tech news, politics -- where the country
   name appears naturally and has nothing to do with travel
   recommendations. This script prints a fixed warning when scanning
   podawaa2024 for exactly this reason: a distinct-string count alone
   would not have caught it, and did not, until someone actually read
   the posts.

Usage:
    python3 travel_content_scan.py podawaa /path/to/podawaa2024.json
    python3 travel_content_scan.py hyperclapper /path/to/HyperClaper.json
    python3 travel_content_scan.py linkboost /path/to/LinkBoost-2025.json
"""
import sys
import json
import argparse
import re
from collections import Counter

AGENCIES = {
    "Expedia": r"\bExpedia\b", "Booking.com": r"\bBooking\.com\b",
    "TripAdvisor": r"\bTripAdvisor\b", "Airbnb": r"\bAirbnb\b",
    "Kayak": r"\bKayak\b", "Priceline": r"\bPriceline\b",
    "Travelocity": r"\bTravelocity\b", "Orbitz": r"\bOrbitz\b",
    "Hotels.com": r"\bHotels\.com\b", "VRBO": r"\bVRBO\b",
    "Trip.com": r"\bTrip\.com\b", "MakeMyTrip": r"\bMakeMyTrip\b",
    "travel agency (generic)": r"\btravel agenc(y|ies)\b",
}
DESTINATIONS = {
    "Paris": r"\bParis\b", "London": r"\bLondon\b", "Tokyo": r"\bTokyo\b",
    "Dubai": r"\bDubai\b", "Bali": r"\bBali\b", "Rome": r"\bRome\b",
    "Barcelona": r"\bBarcelona\b", "Amsterdam": r"\bAmsterdam\b",
    "Singapore": r"\bSingapore\b", "Thailand": r"\bThailand\b",
    "Italy": r"\bItaly\b", "France": r"\bFrance\b", "Spain": r"\bSpain\b",
    "Japan": r"\bJapan\b", "Maldives": r"\bMaldives\b", "Hawaii": r"\bHawaii\b",
    "Cancun": r"\bCancun\b", "Switzerland": r"\bSwitzerland\b",
    "Iceland": r"\bIceland\b", "Greece": r"\bGreece\b", "Portugal": r"\bPortugal\b",
    "Santorini": r"\bSantorini\b", "New York City": r"\bNew York City\b|\bNYC\b",
    "Los Angeles": r"\bLos Angeles\b", "Miami": r"\bMiami\b",
}
AG_C = [(k, re.compile(v, re.IGNORECASE)) for k, v in AGENCIES.items()]
DEST_C = [(k, re.compile(v, re.IGNORECASE)) for k, v in DESTINATIONS.items()]


def check_dominant(term_name, texts_matching):
    counter = Counter(t.strip() for t in texts_matching)
    total = len(texts_matching)
    if not total:
        return None
    top_str, top_count = counter.most_common(1)[0]
    share = top_count / total * 100
    if share >= 20:
        corrected = total - top_count + 1
        return (f"    ^ WARNING: \"{term_name}\" -- top repeated string = {top_count:,}/{total:,} "
                f"({share:.1f}%) of matches -- likely template inflation, not distinct signal. "
                f"Corrected estimate: {corrected:,}")
    return None


def scan(texts, label, n, is_podawaa=False):
    ag_matches = {name: [] for name, _ in AG_C}
    dest_matches = {name: [] for name, _ in DEST_C}
    for t in texts:
        if not t:
            continue
        for name, pat in AG_C:
            if pat.search(t):
                ag_matches[name].append(t)
        for name, pat in DEST_C:
            if pat.search(t):
                dest_matches[name].append(t)

    print(f"=== {label} ({n:,} records) ===")
    print("Travel agencies/platforms:")
    for name, matches in sorted(ag_matches.items(), key=lambda x: -len(x[1])):
        if not matches:
            continue
        print(f"    {name:<28} {len(matches):,} ({len(matches)/n*100:.4f}%)")
        warn = check_dominant(name, matches)
        if warn:
            print(warn)
    print("Destinations:")
    for name, matches in sorted(dest_matches.items(), key=lambda x: -len(x[1]))[:15]:
        if not matches:
            continue
        print(f"    {name:<28} {len(matches):,} ({len(matches)/n*100:.4f}%)")
        warn = check_dominant(name, matches)
        if warn:
            print(warn)
    if is_podawaa:
        print()
        print("  NOTE: \"France\" and \"Paris\" counts in this dataset are inflated by")
        print("  French-language content discussing French domestic topics (workplace")
        print("  issues, tech news, politics), not travel recommendations. Confirmed by")
        print("  reading a sample of matching posts -- this is not caught by the")
        print("  duplicate-string check above, since the posts are genuinely distinct.")
        print("  See docs/research/travel-content.md.")
    print()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("dataset", choices=["podawaa", "hyperclapper", "linkboost"])
    ap.add_argument("path")
    args = ap.parse_args()

    if args.dataset == "podawaa":
        with open(args.path, "r", encoding="utf-8") as f:
            posts = json.load(f)["Posts"]
        scan([p.get("Content") for p in posts], "podawaa2024", len(posts), is_podawaa=True)
    elif args.dataset == "hyperclapper":
        with open(args.path, "r", encoding="utf-8") as f:
            posts = json.load(f)["data"]["post"]
        scan([p.get("post_title") for p in posts], "HyperClapper", len(posts))
    elif args.dataset == "linkboost":
        with open(args.path, "r", encoding="utf-8") as f:
            recs = json.load(f)
        scan([r.get("Title") for r in recs], "LinkBoost-2025", len(recs))


if __name__ == "__main__":
    main()
