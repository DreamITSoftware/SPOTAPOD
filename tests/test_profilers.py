#!/usr/bin/env python3
"""
test_profilers.py

Runs each analysis/profile_*.py script against the synthetic fixtures in
tests/fixtures/ (fabricated data, no real individuals) and checks that
output contains only aggregate counts, never a name, handle, URN, or
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
        # Both fixture records share "Agree?", but attributed to the same
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


class TestExport65Profile(unittest.TestCase):
    FOLDER = str(FIXTURES / "export65")

    def test_runs_and_reports_counts(self):
        result = run_script("export65_profile.py", self.FOLDER)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("Files uploaded:                      3", result.stdout)
        self.assertIn("Distinct files (by content):         2", result.stdout)
        self.assertIn("Byte-identical extra copies:         1", result.stdout)
        self.assertIn("Distinct records (_id):              3", result.stdout)
        self.assertIn("Records present in more than 1 file: 1", result.stdout)
        self.assertIn("Records whose state differs by file: 1", result.stdout)
        self.assertIn("Created before 2024-10-21: 1", result.stdout)

    def test_no_identifier_in_output(self):
        result = run_script("export65_profile.py", self.FOLDER)
        for text in ("Personone", "Persontwo", "Personthree", "FIXTURE_REC",
                     "urn:li:activity", "linkedin.com", "Fixture post text"):
            self.assertNotIn(text, result.stdout)

    def test_manifest_round_trip(self):
        import tempfile
        with tempfile.TemporaryDirectory() as tmp:
            out = str(Path(tmp) / "manifest.csv")
            written = run_script("export65_profile.py", self.FOLDER, "--write-manifest", out)
            self.assertEqual(written.returncode, 0, written.stderr)
            checked = run_script("export65_profile.py", self.FOLDER, "--check-manifest", out)
            self.assertIn("2 of 2 listed files found with matching hash and record count", checked.stdout)
            for text in ("Personone", "FIXTURE_REC", "urn:li:activity"):
                self.assertNotIn(text, Path(out).read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
