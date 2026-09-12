#!/usr/bin/env python3
"""
test_profilers.py

Runs each analysis/profile_*.py script against the synthetic fixtures in
tests/fixtures/ (fabricated data, no real individuals) and checks that
output contains only aggregate counts — never a name, handle, URN, or
other identifier from the fixture.

Usage:
    python3 -m unittest tests/test_profilers.py
"""
import subprocess
import sys
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
ANALYSIS = REPO_ROOT / "analysis"
FIXTURES = REPO_ROOT / "tests" / "fixtures"


def run_script(script_name, *args):
    result = subprocess.run(
        [sys.executable, str(ANALYSIS / script_name), *args],
        capture_output=True, text=True,
    )
    return result


class TestProfilePodawaa(unittest.TestCase):
    def test_runs_and_reports_counts(self):
        result = run_script("profile_podawaa.py", str(FIXTURES / "podawaa_sample.json"))
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("Total records:                  3", result.stdout)
        self.assertIn("Unique authors (hashed count):  2", result.stdout)

    def test_no_identifier_in_output(self):
        result = run_script("profile_podawaa.py", str(FIXTURES / "podawaa_sample.json"))
        self.assertNotIn("test-user-one", result.stdout)
        self.assertNotIn("test-user-two", result.stdout)


class TestProfileHyperclapper(unittest.TestCase):
    def test_runs_and_reports_counts(self):
        result = run_script("profile_hyperclapper.py", str(FIXTURES / "hyperclapper_sample.json"))
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("Total records:                  2", result.stdout)
        self.assertIn("Unique authors (hashed count):  2", result.stdout)

    def test_no_identifier_in_output(self):
        result = run_script("profile_hyperclapper.py", str(FIXTURES / "hyperclapper_sample.json"))
        self.assertNotIn("Test Testerson", result.stdout)
        self.assertNotIn("test-testerson", result.stdout)
        self.assertNotIn("example.invalid", result.stdout)
        self.assertNotIn("TEST_ID_0001", result.stdout)


class TestProfileLinkboost(unittest.TestCase):
    def test_runs_and_reports_counts(self):
        result = run_script("profile_linkboost.py", str(FIXTURES / "linkboost_sample.json"))
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("Total records:                       2", result.stdout)
        self.assertIn("Unique target posts (hashed ObjectUrn): 1", result.stdout)
        self.assertIn("Unique operator accounts (hashed UserId): 2", result.stdout)

    def test_no_identifier_in_output(self):
        result = run_script("profile_linkboost.py", str(FIXTURES / "linkboost_sample.json"))
        self.assertNotIn("Testerson", result.stdout)
        self.assertNotIn("operator-fixture", result.stdout)
        self.assertNotIn("urn:li:member", result.stdout)


class TestDuplicateContent(unittest.TestCase):
    def test_runs_and_finds_cluster(self):
        # Both fixture records share "Agree?" — but attributed to the same
        # author (test-user-one), so with --min-authors 2 it should NOT
        # count as a cross-author cluster.
        result = run_script("duplicate_content.py", str(FIXTURES / "podawaa_sample.json"),
                             "--min-authors", "2")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("Clusters with >= 2 distinct authors", result.stdout)

    def test_no_identifier_in_output(self):
        result = run_script("duplicate_content.py", str(FIXTURES / "podawaa_sample.json"),
                             "--min-authors", "2")
        self.assertNotIn("test-user-one", result.stdout)
        self.assertNotIn("test-user-two", result.stdout)


if __name__ == "__main__":
    unittest.main()
