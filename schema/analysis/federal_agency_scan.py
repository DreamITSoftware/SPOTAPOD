#!/usr/bin/env python3
"""
federal_agency_scan.py

Counts mentions of named U.S. federal agencies (and the generic phrases
"federal agency/agencies" / "government agency/agencies") across post
content in all three datasets.

Acronym terms (ICE, SEC, FBI, CIA, NSA, TSA, IRS, EPA, FDA, FTC, FCC,
USDA, DOJ, DOD, HHS, FEMA, NASA, CDC, FAA, ATF, DEA) are matched
CASE-SENSITIVELY and only as whole words. This is deliberate, not an
oversight: several of these acronyms collide with common lowercase
English words or abbreviations ("ice" as in ice cream, "sec" as an
abbreviation for seconds), and a case-insensitive match on this scan
inflates ICE by roughly 15x and SEC by roughly 2x with content that has
nothing to do with the agency. Same discipline as the MIT/German-"mit"
case-sensitivity fix in university_content_scan.py.

Multi-word agency names/phrases (Department of Homeland Security,
Department of Justice, Department of Defense, Pentagon, State
Department, Treasury Department, Securities and Exchange Commission,
White House, Secret Service) are unambiguous enough to match
case-insensitively.

Includes the same duplicate-template safeguard used throughout this
repo: reports distinct underlying text values alongside every raw
count, and flags any field where a single repeated string accounts for
20% or more of matching records.

Usage:
    python3 federal_agency_scan.py podawaa /path/to/podawaa2024.json
    python3 federal_agency_scan.py hyperclapper /path/to/HyperClaper.json
    python3 federal_agency_scan.py linkboost /path/to/LinkBoost-2025.json
"""
import sys
import json
import argparse
import re
from collections import Counter

# (name, pattern, case_sensitive)
TERMS = [
    ("ICE", r"\bICE\b", True),
    ("SEC", r"\bSEC\b", True),
    ("FBI", r"\bFBI\b", True),
    ("CIA", r"\bCIA\b", True),
    ("NSA", r"\bNSA\b", True),
    ("TSA", r"\bTSA\b", True),
    ("IRS", r"\bIRS\b", True),
    ("EPA", r"\bEPA\b", True),
    ("FDA", r"\bFDA\b", True),
    ("FTC", r"\bFTC\b", True),
    ("FCC", r"\bFCC\b", True),
    ("USDA", r"\bUSDA\b", True),
    ("DOJ", r"\bDOJ\b", True),
    ("DOD", r"\bDOD\b", True),
    ("HHS", r"\bHHS\b", True),
    ("FEMA", r"\bFEMA\b", True),
    ("NASA", r"\bNASA\b", True),
    ("CDC", r"\bCDC\b", True),
    ("FAA", r"\bFAA\b", True),
    ("ATF", r"\bATF\b", True),
    ("DEA", r"\bDEA\b", True),
    ("Department of Homeland Security / DHS", r"\b(DHS|Department of Homeland Security|Homeland Security)\b", False),
    ("Department of Justice", r"\bDepartment of Justice\b", False),
    ("Department of Defense / Pentagon", r"\b(Department of Defense|Pentagon)\b", False),
    ("State Department", r"\b(State Department|Department of State)\b", False),
    ("Treasury Department", r"\b(Treasury Department|Department of the Treasury)\b", False),
    ("Securities and Exchange Commission", r"\bSecurities and Exchange Commission\b", False),
    ("White House", r"\bWhite House\b", False),
    ("Secret Service", r"\bSecret Service\b", False),
    ("generic \"federal agency/agencies\"", r"federal agenc(y|ies)", False),
    ("generic \"government agency/agencies\"", r"government agenc(y|ies)", False),
]
COMPILED = [(name, re.compile(pat, 0 if cs else re.IGNORECASE)) for name, pat, cs in TERMS]


def scan(texts, label, n):
    term_counts = Counter()
    matching_strings = Counter()
    any_hit = 0
    for t in texts:
        if not t:
            continue
        hit = False
        for name, pat in COMPILED:
            if pat.search(t):
                term_counts[name] += 1
                hit = True
        if hit:
            any_hit += 1
            matching_strings[t.strip()] += 1

    distinct = len(matching_strings)
    top_count = matching_strings.most_common(1)[0][1] if matching_strings else 0
    dominant_share = (top_count / any_hit * 100) if any_hit else 0

    print(f"=== {label} ({n:,} records) ===")
    print(f"Records mentioning any federal-agency term: {any_hit:,} ({any_hit/n*100:.4f}%)")
    print(f"Distinct underlying text values: {distinct:,}")
    if any_hit and dominant_share >= 20:
        corrected = any_hit - top_count + 1
        print(f"  ^ WARNING: top repeated string = {top_count:,} records ({dominant_share:.1f}%) -- "
              f"likely template inflation. Corrected estimate: {corrected:,}")
    for name, c in term_counts.most_common():
        if c:
            print(f"    {name:<42} {c:,}")
    print()


def load_podawaa(path):
    with open(path, "r", encoding="utf-8") as f:
        return [p.get("Content") for p in json.load(f)["Posts"]]


def load_hyperclapper(path):
    with open(path, "r", encoding="utf-8") as f:
        return [p.get("post_title") for p in json.load(f)["data"]["post"]]


def load_linkboost(path):
    with open(path, "r", encoding="utf-8") as f:
        return [r.get("Title") for r in json.load(f)]


LOADERS = {"podawaa": load_podawaa, "hyperclapper": load_hyperclapper, "linkboost": load_linkboost}
LABELS = {"podawaa": "podawaa2024", "hyperclapper": "HyperClapper", "linkboost": "LinkBoost-2025"}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("dataset", choices=list(LOADERS.keys()))
    ap.add_argument("path")
    args = ap.parse_args()
    texts = LOADERS[args.dataset](args.path)
    scan(texts, LABELS[args.dataset], len(texts))


if __name__ == "__main__":
    main()
