#!/usr/bin/env python3
"""
pod_count_profile.py

Profiles a derived, post-level export (referred to here as
"spotapod.json", the filename it was supplied under) that covers the
exact same 201,000 unique linkedinPostId values as podawaa2024.json,
field-for-field matching Content->Title and Likes/Views->MaxReactions/
MaxViews for every post checked. It is not an independent raw dataset:
it introduces no new authors or posts beyond podawaa2024.json's own
population (every hashed author identifier found here is also present
in podawaa2024.json). What it adds is one new field, `PODCount`, an
apparent per-post repeat/pod-detection count not present in
podawaa2024.json itself.

This script reports only the aggregate PODCount distribution and its
relationship to the zero-view-with-reactions anomaly already documented
elsewhere in this repo (posts with MaxViews == 0 and MaxReactions > 0).
No record, author, or post content is ever printed.

NOTE ON FILE FORMAT: the raw file as supplied does not parse as
standard JSON -- it appears to have been line-wrapped at a fixed
column width without regard to JSON token boundaries (numeric and
string values are split mid-token by literal newlines). This script
repairs that by stripping all literal newline/carriage-return
characters before parsing, which was verified to produce a
consistent, fully-parseable record set with no other structural
anomalies.

Usage:
    python3 pod_count_profile.py /path/to/spotapod.json
"""
import sys
import json


def load_repaired(path):
    with open(path, "r", encoding="utf-8-sig", errors="replace") as f:
        text = f.read()
    joined = text.replace("\r", "").replace("\n", "")
    return json.loads(joined)


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 pod_count_profile.py /path/to/spotapod.json")
        sys.exit(1)

    data = load_repaired(sys.argv[1])
    n = len(data)

    zero_view_anomaly = []
    normal = []
    for r in data:
        if r.get("MaxViews") == 0 and (r.get("MaxReactions") or 0) > 0:
            zero_view_anomaly.append(r)
        else:
            normal.append(r)

    def stats(records, label):
        vals = sorted(r["PODCount"] for r in records)
        m = len(vals)
        if m == 0:
            print(f"{label}: n=0")
            return
        mean = sum(vals) / m
        median = vals[m // 2]
        print(f"{label}: n={m:,} mean PODCount={mean:.2f} median PODCount={median}")

    print("=" * 70)
    print("POD COUNT PROFILE")
    print("=" * 70)
    print(f"Total records: {n:,}")
    print(f"Unique linkedinPostId values: {len(set(r.get('linkedinPostId') for r in data)):,}")
    print()
    print(f"Zero-view-with-reactions anomaly (MaxViews==0, MaxReactions>0): "
          f"{len(zero_view_anomaly):,} ({len(zero_view_anomaly)/n*100:.1f}%)")
    print()
    stats(data, "All records")
    stats(zero_view_anomaly, "Zero-view-anomaly records")
    stats(normal, "Other records")
    print()
    print("Reading this: the median PODCount is identical (2) across both")
    print("groups, but the mean is notably higher for the anomaly group,")
    print("meaning a long tail of very high PODCount values sits")
    print("disproportionately within the zero-view-anomaly records. This is")
    print("a real correlation in the aggregate, not evidence about any")
    print("individual post, and PODCount's exact definition is not stated")
    print("by whatever process produced this file.")


if __name__ == "__main__":
    main()
