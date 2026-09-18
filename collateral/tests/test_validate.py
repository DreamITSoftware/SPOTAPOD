#!/usr/bin/env python3
"""
test_validate.py

Runs tools/validate.py against the synthetic fixtures in tests/fixtures/
(fabricated data, no real individuals) and checks exit codes and output.
Does not require any real dataset file.

Usage:
    python3 -m unittest tests/test_validate.py
    (or) python3 tests/test_validate.py
"""
import subprocess
import sys
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
VALIDATE = REPO_ROOT / "tools" / "validate.py"
FIXTURES = REPO_ROOT / "tests" / "fixtures"


def run_validate(dataset, fixture_name):
    path = FIXTURES / fixture_name
    result = subprocess.run(
        [sys.executable, str(VALIDATE), dataset, str(path)],
        capture_output=True, text=True,
    )
    return result


class TestValidatePodawaa(unittest.TestCase):
    def test_valid_fixture_passes(self):
        result = run_validate("podawaa", "podawaa_sample.json")
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("PASS", result.stdout)
        self.assertIn("Records checked: 3", result.stdout)

    def test_invalid_fixture_fails(self):
        result = run_validate("podawaa", "podawaa_invalid.json")
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        self.assertIn("FAIL", result.stdout)
        self.assertIn("Likes_wrong_type", result.stdout)
        self.assertIn("Views_negative", result.stdout)

    def test_no_identifier_in_output(self):
        # The fixture's AuthorPublicIdentifier values must never appear
        # in validator output, even for records that fail validation.
        result = run_validate("podawaa", "podawaa_sample.json")
        self.assertNotIn("test-user-one", result.stdout)
        self.assertNotIn("test-user-two", result.stdout)


class TestValidateHyperclapper(unittest.TestCase):
    def test_fixture_reports_type_inconsistency(self):
        result = run_validate("hyperclapper", "hyperclapper_sample.json")
        # like_count is 5.0 (float) on the second fixture record — this
        # mirrors the real dataset's known data-quality quirk.
        self.assertIn("like_count_wrong_type", result.stdout)
        self.assertIn("Records checked: 2", result.stdout)

    def test_no_identifier_in_output(self):
        result = run_validate("hyperclapper", "hyperclapper_sample.json")
        self.assertNotIn("Test Testerson", result.stdout)
        self.assertNotIn("test-testerson", result.stdout)
        self.assertNotIn("example.invalid", result.stdout)


class TestValidateLinkboost(unittest.TestCase):
    def test_valid_fixture_passes(self):
        result = run_validate("linkboost", "linkboost_sample.json")
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("PASS", result.stdout)
        self.assertIn("Records checked: 2", result.stdout)

    def test_no_identifier_in_output(self):
        result = run_validate("linkboost", "linkboost_sample.json")
        self.assertNotIn("Testerson", result.stdout)
        self.assertNotIn("Fictional", result.stdout)
        self.assertNotIn("operator-fixture", result.stdout)


if __name__ == "__main__":
    unittest.main()
