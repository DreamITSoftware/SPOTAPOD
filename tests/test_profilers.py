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

    def test_stats_block(self):
        result = run_script("export65_profile.py", self.FOLDER, "--stats")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("Engagement statistics fields as stored", result.stdout)
        self.assertIn("Records with post text (title):      3 of 3", result.stdout)
        self.assertIn("Distinct accounts:                   3", result.stdout)
        self.assertIn("Distinct post texts:                 3 of 3 records with text", result.stdout)
        for text in ("Personone", "Persontwo", "Personthree", "FIXTURE_REC", "urn:li:activity", "Fixture post text"):
            self.assertNotIn(text, result.stdout)

    def test_top_ten_by_likes_block(self):
        """Twelve fabricated records: the ten highest like counts hold one record with no views, one with zero views, and eight with views."""
        import json
        import tempfile
        recs = []
        for i in range(12):
            r = {"_id": "FIXTURE_TOP_%d" % i, "state": "finishedEngagement",
                 "url": "https://www.linkedin.com/feed/update/urn:li:activity:7256145920000000000/",
                 "createdAt": {"$date": 1730000600000 + i}, "engagementType": "normal",
                 "firstName": "Fixture", "lastName": "Person%d" % i,
                 "title": "Fixture post text %d" % i, "engagedUsersCount": 10,
                 "statsLikes": 100 + i, "statsViews": 500 + i}
            recs.append(r)
        recs[11].pop("statsViews")   # highest likes, no view count
        recs[10]["statsViews"] = 0   # second highest likes, zero views
        frame = "a" + json.dumps([json.dumps({"msg": "result", "id": "FIXTURETOP", "result": recs})])
        with tempfile.TemporaryDirectory() as tmp:
            (Path(tmp) / "abcd0000-podUsers_FIXTURETOP_2026-16-10--12-00-00.json").write_text(frame, encoding="utf-8")
            result = run_script("export65_profile.py", tmp, "--stats")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("Records with the 10 highest statsLikes (ties at the tenth value kept): 10", result.stdout)
        self.assertIn("with statsViews of 0:                    1", result.stdout)
        self.assertIn("with no statsViews field:                1", result.stdout)
        self.assertIn("with statsViews above 0:                 8", result.stdout)
        for text in ("Person1", "FIXTURE_TOP", "urn:li:activity", "Fixture post text"):
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


class TestExport65Loader(unittest.TestCase):
    """The shared reader that lets the scan scripts run on the 65 export files."""
    FOLDER = str(FIXTURES / "export65")
    IDENTIFIERS = ("Personone", "Persontwo", "Personthree", "FIXTURE_REC",
                   "urn:li:activity", "linkedin.com", "Fixture post text")

    def test_loader_returns_distinct_records(self):
        sys.path.insert(0, str(ANALYSIS))
        try:
            from export65_loader import load_export65, load_export65_counted
        finally:
            sys.path.pop(0)
        texts = load_export65(self.FOLDER)
        self.assertEqual(len(texts), 3)  # 3 distinct _id values across 3 files (1 is a byte-identical copy)
        self.assertEqual(load_export65_counted(self.FOLDER)[1], 3)

    def test_every_patched_scan_runs_on_the_fixture_without_identifiers(self):
        scripts = sorted(p.name for p in ANALYSIS.glob("*.py")
                         if "export65_loader import" in p.read_text(encoding="utf-8")
                         and p.name not in ("export65_loader.py", "topic_taxonomy.py", "date_cutoff_count.py"))
        self.assertGreaterEqual(len(scripts), 38)
        for name in scripts:
            extra = ["--category", "all"] if name == "entity_mention_scan.py" else []
            result = run_script(name, "export65", self.FOLDER, *extra)
            self.assertEqual(result.returncode, 0, name + ": " + result.stderr)
            for text in self.IDENTIFIERS:
                self.assertNotIn(text, result.stdout, name)

    def test_algorithm_scan_reports_the_record_count(self):
        result = run_script("algorithm_mention_scan.py", "export65", self.FOLDER)
        self.assertIn("65 export files (3 records)", result.stdout)

    def test_date_cutoff_count_adds_a_line(self):
        result = run_script("date_cutoff_count.py", str(FIXTURES / "podawaa_sample.json"),
                            str(FIXTURES / "hyperclapper_sample.json"), str(FIXTURES / "linkboost_sample.json"),
                            "--export65", self.FOLDER)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("65 export files: 3 distinct records", result.stdout)
        for text in self.IDENTIFIERS:
            self.assertNotIn(text, result.stdout)

    def test_topic_taxonomy_adds_a_separate_block(self):
        result = run_script("topic_taxonomy.py", str(FIXTURES / "podawaa_sample.json"),
                            str(FIXTURES / "hyperclapper_sample.json"), str(FIXTURES / "linkboost_sample.json"),
                            "--export65", self.FOLDER)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("65 export files, run separately (not included in the totals above)", result.stdout)
        self.assertIn("Records: 3", result.stdout)
        for text in self.IDENTIFIERS:
            self.assertNotIn(text, result.stdout)


if __name__ == "__main__":
    unittest.main()
