"""Tests for clawfit.filters."""

import unittest

from clawfit.loader import load_agents, load_llms, load_hardware
from clawfit.filters import filter_agents, filter_llms, filter_hardware, _resolve_budget


class TestFilterAgents(unittest.TestCase):
    def setUp(self):
        self.agents = load_agents()

    def test_filter_by_task(self):
        out = filter_agents(self.agents, task="qa")
        self.assertTrue(len(out) > 0)
        for a in out:
            self.assertIn("qa", a.tasks)

    def test_filter_by_latency_low(self):
        out = filter_agents(self.agents, latency="low")
        for a in out:
            self.assertEqual(a.latency, "low")

    def test_filter_by_latency_medium_includes_low(self):
        out = filter_agents(self.agents, latency="medium")
        latencies = {a.latency for a in out}
        self.assertTrue(latencies <= {"low", "medium"})

    def test_filter_by_network(self):
        out = filter_agents(self.agents, network="offline")
        for a in out:
            self.assertIn(a.network, ("offline", "hybrid"))

    def test_filter_by_statefulness(self):
        out = filter_agents(self.agents, statefulness="stateless")
        for a in out:
            self.assertEqual(a.statefulness, "stateless")

    def test_combined_filters(self):
        out = filter_agents(self.agents, task="qa", latency="low")
        for a in out:
            self.assertIn("qa", a.tasks)
            self.assertEqual(a.latency, "low")

    def test_no_match_returns_empty(self):
        out = filter_agents(self.agents, task="nonexistent-task")
        self.assertEqual(out, [])


class TestFilterLLMs(unittest.TestCase):
    def setUp(self):
        self.llms = load_llms()

    def test_filter_by_task(self):
        out = filter_llms(self.llms, task="code-gen")
        self.assertTrue(len(out) > 0)
        for m in out:
            self.assertIn("code-gen", m.tasks)

    def test_filter_by_budget(self):
        out = filter_llms(self.llms, budget=0.001)
        for m in out:
            self.assertLessEqual(m.cost_per_1k_tokens, 0.001)

    def test_filter_by_network_offline(self):
        out = filter_llms(self.llms, network="offline")
        for m in out:
            self.assertEqual(m.network, "offline")


class TestFilterLLMsKimiK26(unittest.TestCase):
    """Targeted tests for the kimi-k2-6 (moonshot) registry entry."""

    def setUp(self):
        self.llms = load_llms()

    def test_kimi_k26_present_in_registry(self):
        ids = [m.id for m in self.llms]
        self.assertIn("kimi-k2-6", ids)

    def test_kimi_k26_provider_is_moonshot(self):
        entry = next(m for m in self.llms if m.id == "kimi-k2-6")
        self.assertEqual(entry.provider, "moonshot")

    def test_kimi_k26_survives_code_gen_task_filter(self):
        out = filter_llms(self.llms, task="code-gen")
        ids = [m.id for m in out]
        self.assertIn("kimi-k2-6", ids)

    def test_kimi_k26_passes_budget_above_cost(self):
        # cost is 0.00095; a budget of 0.001 must include it
        out = filter_llms(self.llms, budget=0.001)
        ids = [m.id for m in out]
        self.assertIn("kimi-k2-6", ids)

    def test_kimi_k26_excluded_by_budget_below_cost(self):
        # cost is 0.00095; a budget of 0.0009 must exclude it
        out = filter_llms(self.llms, budget=0.0009)
        ids = [m.id for m in out]
        self.assertNotIn("kimi-k2-6", ids)

    def test_kimi_k26_excluded_by_offline_network(self):
        # kimi-k2-6 is online-only; offline filter must exclude it
        out = filter_llms(self.llms, network="offline")
        ids = [m.id for m in out]
        self.assertNotIn("kimi-k2-6", ids)


class TestFilterHardware(unittest.TestCase):
    def setUp(self):
        self.hw = load_hardware()

    def test_filter_by_type(self):
        out = filter_hardware(self.hw, hw_type="edge")
        self.assertTrue(len(out) > 0)
        for h in out:
            self.assertEqual(h.type, "edge")

    def test_filter_by_latency(self):
        out = filter_hardware(self.hw, latency="low")
        for h in out:
            self.assertEqual(h.latency, "low")


class TestVerticalTaskTags(unittest.TestCase):
    """Vertical task tags: exact match takes priority, parent fallback works."""

    def setUp(self):
        self.agents = load_agents()
        self.llms = load_llms()

    # --- agents ---

    def test_financial_research_matches_explicit_tag(self):
        # plan-execute has "financial-research" explicitly
        out = filter_agents(self.agents, task="financial-research")
        ids = [a.id for a in out]
        self.assertIn("plan-execute", ids)

    def test_financial_research_fallback_to_research_parent(self):
        # react-agent has "research" but not "financial-research" → still included via parent
        out = filter_agents(self.agents, task="financial-research")
        ids = [a.id for a in out]
        self.assertIn("react-agent", ids)

    def test_security_testing_matches_explicit_tag(self):
        out = filter_agents(self.agents, task="security-testing")
        ids = [a.id for a in out]
        self.assertIn("react-agent", ids)

    def test_legal_review_matches_explicit_tag(self):
        out = filter_agents(self.agents, task="legal-review")
        ids = [a.id for a in out]
        self.assertIn("local-rag", ids)

    def test_legal_review_fallback_for_generic_research_agent(self):
        # plan-execute has "research" → matches legal-review via parent
        out = filter_agents(self.agents, task="legal-review")
        ids = [a.id for a in out]
        self.assertIn("plan-execute", ids)

    def test_unknown_vertical_no_match(self):
        out = filter_agents(self.agents, task="astrology-reading")
        self.assertEqual(out, [])

    # --- llms ---

    def test_llm_financial_research_via_research_parent(self):
        out = filter_llms(self.llms, task="financial-research")
        # all LLMs with "research" in tasks should appear
        self.assertTrue(len(out) > 0)
        for m in out:
            self.assertTrue(
                "financial-research" in m.tasks or "research" in m.tasks,
                f"{m.id} passed financial-research filter but has neither tag",
            )


class TestBudgetTiers(unittest.TestCase):
    """Budget tier strings map to correct ceilings; float backward-compat works."""

    def setUp(self):
        self.llms = load_llms()

    # --- _resolve_budget ---

    def test_resolve_free(self):
        self.assertEqual(_resolve_budget("free"), 0.0)

    def test_resolve_low(self):
        self.assertEqual(_resolve_budget("low"), 0.001)

    def test_resolve_medium(self):
        self.assertEqual(_resolve_budget("medium"), 0.005)

    def test_resolve_high_is_inf(self):
        import math
        self.assertTrue(math.isinf(_resolve_budget("high")))

    def test_resolve_float_passthrough(self):
        self.assertAlmostEqual(_resolve_budget(0.0025), 0.0025)

    def test_resolve_none_returns_none(self):
        self.assertIsNone(_resolve_budget(None))

    def test_resolve_unknown_tier_raises(self):
        with self.assertRaises(ValueError):
            _resolve_budget("ultra")

    # --- filter_llms with tiers ---

    def test_budget_free_returns_only_zero_cost(self):
        out = filter_llms(self.llms, budget="free")
        for m in out:
            self.assertEqual(m.cost_per_1k_tokens, 0.0, f"{m.id} has non-zero cost")

    def test_budget_low_excludes_gpt4o(self):
        # gpt-4o costs 0.0025 > 0.001 ceiling
        out = filter_llms(self.llms, budget="low")
        ids = [m.id for m in out]
        self.assertNotIn("gpt-4o", ids)

    def test_budget_low_includes_deepseek_flash(self):
        # deepseek-v4-flash costs 0.00014 < 0.001
        out = filter_llms(self.llms, budget="low")
        ids = [m.id for m in out]
        self.assertIn("deepseek-v4-flash", ids)

    def test_budget_medium_includes_gpt4o(self):
        # gpt-4o costs 0.0025 < 0.005 medium ceiling
        out = filter_llms(self.llms, budget="medium")
        ids = [m.id for m in out]
        self.assertIn("gpt-4o", ids)

    def test_budget_medium_excludes_claude_opus(self):
        # claude-opus costs 0.015 > 0.005
        out = filter_llms(self.llms, budget="medium")
        ids = [m.id for m in out]
        self.assertNotIn("claude-opus", ids)

    def test_budget_high_returns_all(self):
        all_llms = self.llms
        out = filter_llms(self.llms, budget="high")
        self.assertEqual(len(out), len(all_llms))

    def test_budget_float_backward_compat(self):
        # 0.001 as float should behave same as "low" tier
        out_tier = filter_llms(self.llms, budget="low")
        out_float = filter_llms(self.llms, budget=0.001)
        self.assertEqual(
            sorted(m.id for m in out_tier),
            sorted(m.id for m in out_float),
        )


if __name__ == "__main__":
    unittest.main()
