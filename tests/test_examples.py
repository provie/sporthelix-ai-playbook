"""Offline checks for synthetic examples; not a real-world factual verification."""
import json
import unittest
from pathlib import Path

from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[1]


def load_json(path):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


class FixtureTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.schema = load_json("schemas/sport-event.schema.json")
        cls.events = load_json("examples/synthetic-events.json")["events"]
        cls.sources = {
            item["source_id"]: item
            for item in load_json("examples/synthetic-sources.json")["sources"]
        }

    def test_schema_and_iso_datetime_formats(self):
        Draft202012Validator.check_schema(self.schema)
        validator = Draft202012Validator(self.schema, format_checker=FormatChecker())
        self.assertEqual(len(self.events), 2)
        for event in self.events:
            with self.subTest(event=event["event_id"]):
                validator.validate(event)

    def test_evidence_quotes_are_present_and_references_resolve(self):
        for event in self.events:
            ids = {source["source_id"] for source in event["sources"]}
            for src in event["sources"]:
                fixture = self.sources[src["source_id"]]
                self.assertEqual(src["url"], fixture["url"])
                self.assertEqual(src["retrieved_at"], fixture["retrieved_at"])
            for proof in event["evidence"]:
                self.assertIn(proof["source_id"], ids)
                self.assertIn(
                    proof["quote"],
                    self.sources[proof["source_id"]]["raw_text"],
                    f"Unmatched evidence quote: {proof}",
                )
            for conflict in event["conflicts"]:
                for candidate in conflict["candidates"]:
                    self.assertIn(candidate["source_id"], ids)

    def test_conflict_is_not_silently_resolved(self):
        match = next(e for e in self.events if e["event_id"] == "synthetic:match-100")
        self.assertEqual(match["verification_status"], "conflicting")
        self.assertIsNone(match["start_datetime"])
        self.assertTrue(match["review_required"])
        values = {p["value"] for p in match["conflicts"][0]["candidates"]}
        self.assertEqual(
            values,
            {"2026-11-07T15:00:00+01:00", "2026-11-07T16:00:00+01:00"},
        )

    def test_missing_venue_is_not_invented(self):
        match = next(e for e in self.events if e["event_id"] == "synthetic:match-200")
        self.assertIsNone(match["venue"])
        self.assertTrue(match["review_required"])
        self.assertEqual(match["verification_status"], "source_supported")


if __name__ == "__main__":
    unittest.main()
