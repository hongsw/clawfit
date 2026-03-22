"""Tests for clawfit.recommend end-to-end."""

import unittest

from clawfit.recommend import recommend


class TestRecommend(unittest.TestCase):
    def test_basic_recommendation(self):
        results = recommend(task="qa")
        self.assertIsInstance(results, list)
        self.assertTrue(len(results) > 0)
        rec = results[0]
        self.assertIn("agent", rec)
        self.assertIn("llm", rec)
        self.assertIn("hardware", rec)
        self.assertIn("architecture", rec)
        self.assertIn("fit_score", rec)
        self.assertIn("why", rec)
        self.assertIn("risk", rec)

    def test_top_n(self):
        results = recommend(task="qa", top_n=1)
        self.assertEqual(len(results), 1)

    def test_no_match_returns_error(self):
        results = recommend(task="nonexistent-task")
        self.assertTrue(len(results) == 1)
        self.assertIn("error", results[0])

    def test_offline_recommendation(self):
        results = recommend(task="qa", network="offline")
        self.assertTrue(len(results) > 0)
        if "error" not in results[0]:
            self.assertIsInstance(results[0]["fit_score"], float)

    def test_low_latency_recommendation(self):
        results = recommend(task="qa", latency="low")
        self.assertTrue(len(results) > 0)

    def test_budget_filter(self):
        results = recommend(task="qa", budget=0.001)
        self.assertTrue(len(results) > 0)

    def test_fit_score_descending(self):
        results = recommend(task="qa", top_n=10)
        scores = [r.get("fit_score", 0) for r in results if "error" not in r]
        self.assertEqual(scores, sorted(scores, reverse=True))


if __name__ == "__main__":
    unittest.main()
