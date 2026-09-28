#!/usr/bin/env python3
"""
theoretical_penalty_ceiling.py

Computes a single, deliberately extreme arithmetic exercise: what a
per-record count times the current statutory maximum civil penalty for a
Section 5 trade regulation rule violation (15 U.S.C. 465(m)(1)(A), see
../docs/regulatory-context.md) adds up to, if -- and this "if" is doing
all the work -- every single record in these datasets were treated as
its own separate, maximum-penalty violation.

THIS IS NOT A PENALTY ESTIMATE, A DAMAGES CALCULATION, OR A PREDICTION.
No FTC rule, statute, or published enforcement action defines "one
violation" as "one exported data record." Real penalty calculations
turn on facts this repo does not have (how transactions were structured,
whether conduct is treated as continuing or discrete, litigation and
settlement posture) and are decided by FTC enforcement staff and courts,
not by a script counting rows in a JSON file. Every real-world
resolution this repo is aware of for comparable conduct (New York v.
Devumi; LinkedIn Corp. v. TopSocial24) settled for a small fraction of
any theoretical per-record maximum. This script exists only to show, in
concrete numbers, why that maximum should not be mistaken for a
realistic figure.

The $53,088 figure is the FTC's 2025 inflation-adjusted maximum civil
penalty per violation of Sections 5(l), 5(m)(1)(A), and 5(m)(1)(B) of
the FTC Act (up from $51,744 the year before). It changes annually; the
--penalty flag lets you re-run this with a current figure rather than
editing the script.

Usage:
    python3 theoretical_penalty_ceiling.py \\
        --podawaa-count 213491 --hyperclapper-count 49369 \\
        --linkboost-count 77969 --penalty 53088
"""
import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--podawaa-count", type=int, required=True)
    parser.add_argument("--hyperclapper-count", type=int, required=True)
    parser.add_argument("--linkboost-count", type=int, required=True)
    parser.add_argument(
        "--penalty",
        type=int,
        default=53088,
        help="Max civil penalty per violation, USD. Default: $53,088 (FTC 2025 figure).",
    )
    args = parser.parse_args()

    datasets = {
        "podawaa2024.json": args.podawaa_count,
        "HyperClapper.json": args.hyperclapper_count,
        "LinkBoost-2025.json": args.linkboost_count,
    }

    print(
        "THEORETICAL CEILING ONLY -- one record treated as one maximum-penalty "
        "violation. Not a penalty estimate. See docs/research/"
        "theoretical-penalty-ceiling.md for why."
    )
    print(f"Penalty per record used: ${args.penalty:,}")
    print()

    total_records = 0
    total_amount = 0
    for name, count in datasets.items():
        amount = count * args.penalty
        total_records += count
        total_amount += amount
        print(f"{name}: {count:,} records x ${args.penalty:,} = ${amount:,}")

    print(f"Combined ({total_records:,} records): ${total_amount:,}")


if __name__ == "__main__":
    main()
