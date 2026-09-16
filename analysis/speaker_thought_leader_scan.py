#!/usr/bin/env python3
"""
speaker_thought_leader_scan.py

Counts how many records' stated occupation/headline text contains
"speaker" and/or "thought leader" -- aggregate counts only, never a
name, handle, or verbatim headline/occupation sentence. Same scope
limit as simple_title_aggregate.py: podawaa2024.json has no occupation/
headline-equivalent field, so it isn't covered here.

Usage:
    python3 speaker_thought_leader_scan.py hyperclapper /path/to/HyperClaper.json
    python3 speaker_thought_leader_scan.py linkboost /path/to/LinkBoost-2025.json
"""
import sys
import json
import argparse
import re

SPEAKER = re.compile(r"\bspeaker\b", re.IGNORECASE)
THOUGHT_LEADER = re.compile(r"\bthought leader\b", re.IGNORECASE)


def load_hyperclapper(path):
    with open(path, "r", encoding="utf-8") as f:
        posts = json.load(f)["data"]["post"]
    out = []
    for p in posts:
        ld = (p.get("profile") or {}).get("linkedin_data") or {}
        out.append(ld.get("headline"))
    return out


def load_linkboost(path):
    with open(path, "r", encoding="utf-8") as f:
        recs = json.load(f)
    return [r.get("Occupation") for r in recs]


LOADERS = {"hyperclapper": load_hyperclapper, "linkboost": load_linkboost}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("dataset", choices=list(LOADERS.keys()),
                     help="podawaa2024.json has no occupation/headline field -- not supported")
    ap.add_argument("path")
    args = ap.parse_args()

    texts = LOADERS[args.dataset](args.path)
    n = len(texts)
    has_text = sum(1 for t in texts if t)
    speaker_hits = sum(1 for t in texts if t and SPEAKER.search(t))
    tl_hits = sum(1 for t in texts if t and THOUGHT_LEADER.search(t))
    both = sum(1 for t in texts if t and SPEAKER.search(t) and THOUGHT_LEADER.search(t))

    print("=" * 60)
    print(f"{args.dataset.upper()} - SPEAKER / THOUGHT LEADER (no names, no full bios)")
    print("=" * 60)
    print(f"Total records: {n:,}")
    print(f"Records with occupation/headline text: {has_text:,}")
    print()
    print(f'"Speaker":        {speaker_hits:,} ({speaker_hits/n*100:.2f}% of all records, '
          f'{speaker_hits/has_text*100:.2f}% of those with text)')
    print(f'"Thought leader": {tl_hits:,} ({tl_hits/n*100:.2f}% of all records, '
          f'{tl_hits/has_text*100:.2f}% of those with text)')
    print(f"Both terms in the same record: {both:,} "
          f"({both/tl_hits*100:.1f}% of \"thought leader\" records also say \"speaker\")" if tl_hits else "Both terms in the same record: 0")
    print()
    print("Reminder: this reports keyword counts only. No name, handle, or")
    print("verbatim occupation/headline text is printed by this script.")


if __name__ == "__main__":
    main()
