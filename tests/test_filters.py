"""Tests for clawfit.filters."""

import unittest

from clawfit.loader import load_agents, load_llms, load_hardware
from clawfit.filters import filter_agents, filter_llms, filter_hardware


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


if __name__ == "__main__":
    unittest.main()
