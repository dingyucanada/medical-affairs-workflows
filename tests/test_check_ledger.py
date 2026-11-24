from copy import deepcopy
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


SKILL = Path(__file__).resolve().parents[1] / "skills" / "medical-affairs-workflows"
sys.path.insert(0, str(SKILL / "scripts"))
from check_ledger import validate


class EvidenceLedgerTest(unittest.TestCase):
    def setUp(self):
        self.ledger = json.loads((SKILL / "assets" / "synthetic-ledger.json").read_text(encoding="utf-8"))

    def check_error(self, expected):
        errors = validate(self.ledger)
        self.assertTrue(any(expected in error for error in errors), errors)

    def test_example(self):
        self.assertEqual(validate(self.ledger), [])

    def test_archive_without_source_claim_links(self):
        self.ledger["claims"][0]["evidence"] = []
        self.check_error("supported requires located support")

    def test_unavailable_source_cannot_certify_claim(self):
        self.ledger["claims"][0]["evidence"][0]["source_id"] = "full-text-a"
        self.check_error("decisive evidence must be retrieved")

    def test_context_does_not_count_as_support(self):
        self.ledger["claims"][0]["evidence"][0]["relation"] = "context"
        self.check_error("supported requires located support")

    def test_linked_evidence_requires_locator(self):
        del self.ledger["claims"][0]["evidence"][0]["locator"]
        self.check_error("required for decisive evidence")

    def test_overstatement_must_be_withdrawn_or_revised(self):
        self.ledger["claims"][1]["action"] = "request_evidence"
        self.check_error("must be revised, removed, or held")

    def test_claim_marked_for_revision_needs_text(self):
        self.ledger["claims"][1].pop("replacement")
        self.check_error("required for revision")

    def test_conflict_requires_retrieved_contradiction(self):
        claim = self.ledger["claims"][1]
        claim["status"] = "conflicting"
        self.check_error("conflicting requires a located contradiction")
        claim["evidence"][0]["relation"] = "contradicts"
        self.assertEqual(validate(self.ledger), [])

    def test_unresolved_contradiction_cannot_pass_as_supported(self):
        evidence = self.ledger["claims"][0]["evidence"]
        evidence.append({**evidence[0], "relation": "contradicts"})
        self.check_error("no unresolved decisive contradiction")

    def test_keys_are_unique(self):
        self.ledger["sources"].append(deepcopy(self.ledger["sources"][0]))
        self.check_error("duplicates an earlier id")

    def test_date_must_exist(self):
        self.ledger["sources"][0]["accessed_on"] = "2026-02-29"
        self.check_error("needs a real YYYY-MM-DD date")

    def test_unrecognized_source(self):
        self.ledger["claims"][0]["evidence"][0]["source_id"] = "missing"
        self.check_error("unknown source id")

    def test_invalid_shapes_do_not_raise(self):
        self.ledger["claims"][0]["status"] = ["supported"]
        self.ledger["claims"][0]["evidence"][0]["source_id"] = ["abstract-a"]
        self.check_error("unknown evidence state")
        self.check_error("unknown source id")

    def test_cli_rejects_duplicate_json_fields(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "bad.json"
            path.write_text('{"schema_version":1,"schema_version":1}', encoding="utf-8")
            result = self.run_cli(path)
        self.assertEqual(result.returncode, 2, result.stderr)

    def test_cli_reports_structure_failure_without_echoing_claim(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "bad.json"
            self.ledger["claims"][0]["scope"] = ""
            path.write_text(json.dumps(self.ledger), encoding="utf-8")
            result = self.run_cli(path)
        self.assertEqual(result.returncode, 1, result.stderr)
        self.assertIn("claims[0].scope", result.stderr)
        self.assertNotIn(self.ledger["claims"][0]["text"], result.stderr)

    @staticmethod
    def run_cli(path):
        return subprocess.run([sys.executable, str(SKILL / "scripts" / "check_ledger.py"), str(path)],
                              capture_output=True, text=True)


if __name__ == "__main__":
    unittest.main()
