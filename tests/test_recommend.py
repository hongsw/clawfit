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

    def test_maturity_stage_score_in_range(self):
        # maturity_stage가 주어진 모든 결과의 fit_score는 0 이상 1 이하여야 한다
        results = recommend(task="qa", maturity_stage=3, top_n=10)
        self.assertFalse(
            "error" in results[0],
            "maturity_stage=3 should return at least one result for task='qa'",
        )
        for rec in results:
            if "error" in rec:
                continue
            score = rec["fit_score"]
            self.assertGreaterEqual(score, 0.0, f"fit_score {score} is below 0")
            self.assertLessEqual(score, 1.0, f"fit_score {score} exceeds 1")

    def test_maturity_stage_affects_rank(self):
        # stage 1: simple-router(maturity_min=1,max=4)만 범위 내 → top-1은 simple-router
        # stage 5: react-agent(min=4,max=7), local-rag(min=3,max=6)가 범위 내
        #          → simple-router는 범위 밖(score=0)이므로 top-1은 simple-router가 아니다
        results_stage1 = recommend(task="qa", maturity_stage=1, top_n=3)
        results_stage5 = recommend(task="qa", maturity_stage=5, top_n=3)

        # 두 결과 모두 오류 없이 반환되어야 한다
        self.assertFalse("error" in results_stage1[0])
        self.assertFalse("error" in results_stage5[0])

        top_agents_stage1 = [r["agent"] for r in results_stage1 if "error" not in r]
        top_agents_stage5 = [r["agent"] for r in results_stage5 if "error" not in r]

        # stage 1 최상위는 simple-router여야 한다 (유일하게 maturity 범위 내)
        self.assertEqual(top_agents_stage1[0], "simple-router")

        # stage 5 최상위는 simple-router가 아니어야 한다
        # (simple-router의 maturity_max=4 이므로 maturity_score=0.0)
        self.assertNotEqual(top_agents_stage5[0], "simple-router")


    def test_kimi_k26_appears_in_code_gen_results(self):
        # kimi-k2-6 supports code-gen at medium latency, $0.00095/1k;
        # with a permissive budget it must appear somewhere in the ranked list
        results = recommend(task="code-gen", budget=0.01, top_n=20)
        llm_ids = [r["llm"] for r in results if "error" not in r]
        self.assertIn("kimi-k2-6", llm_ids)

    def test_kimi_k26_excluded_when_budget_is_below_its_cost(self):
        # kimi-k2-6 costs $0.00095/1k; a budget of $0.0009 must exclude it
        # while allowing cheaper models (e.g. deepseek-v4-flash at $0.00014)
        results = recommend(task="code-gen", budget=0.0009, top_n=20)
        llm_ids = [r["llm"] for r in results if "error" not in r]
        self.assertNotIn("kimi-k2-6", llm_ids)


if __name__ == "__main__":
    unittest.main()
