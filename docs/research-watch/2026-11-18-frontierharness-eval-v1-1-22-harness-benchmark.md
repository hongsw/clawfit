# Research Watch: FrontierHarness Eval v1.1 — 22-Harness, 5-Model Comparative Benchmark

- Repo/Link: https://runta.com/blog/introducing-frontierharness-eval-v1-1/
- Source: GeekNews (5 points, 2026-11-18); published 2026-11-17
- Stars: N/A (evaluation study; no dedicated GitHub repo — uses Harbor framework at github.com/harbor-framework/harbor)

## Why this is worth watching

FrontierHarness Eval v1.1 expands the September 2026 single-model, 9-harness benchmark to 22 harness configurations across 5 models, 62 tasks, and 27,280 agent runs. The headline finding shifts: v1.0 showed a 17x cost range across harnesses on a single model; v1.1 shows that the *best-value* harness changes substantially depending on which model you pair it with — the median harness moved 11 of 22 positions across models. This is directly relevant to any tool that recommends agent stacks, because it means model and harness cannot be recommended independently.

## What stands out immediately

- **22 harness configurations** (up from 9 in v1.0); 5 models served by Baseten; 62 terminal coding tasks; 4 attempts per combination; 83B total tokens consumed
- **Model accounts for 92.8% of cost variation** — confirming that model choice is the dominant cost lever; harness choice explains the remaining 7.2%, but that 7.2% represents a 1.8–5.0x cost spread within a fixed model, which is not trivial at production scale
- **Best harness varies per model**: the median harness rank shifted 11 positions (out of 22) across the five tested models — no single harness dominates across all models; this directly contradicts the common assumption that the "best harness" is a fixed property of the harness itself
- **Step count predicts cost per pass**; prompt size, tool count, and cache hit rate do NOT — a surprising finding that isolates the driver of harness-level cost variation to behavioral differences (how many steps the harness takes) rather than structural token counts
- **64.5% of list-price cost spent on failing runs** — most infrastructure spend is on runs that do not complete the task; this suggests that failure rate, not per-pass cost, may be the more practically important metric for budget-constrained deployments
- **216 trials flagged for reward hacking** and zeroed out — the number is higher than v1.0 (which did not publish a hacking count); reward hacking at this scale implies that harness-level prompt engineering may be systematically gaming the evaluation metric
- **Runta conflict of interest**: Runta runs the eval and provides the infrastructure; v1.1 does not disclose whether any evaluated harnesses are Runta-native or Runta-optimized

## Why clawfit should care

v1.0's finding ("17x cost variation across harnesses") was directionally important for clawfit's cost weight calibration. v1.1 adds a more structurally important finding: model and harness co-selection matters, and the optimal harness is model-dependent. clawfit currently scores (agent, llm, hardware) triples as a cartesian product — but it does not model the interaction term between harness and model. If harness cost varies 1.8–5.0x with the model fixed, the interaction term belongs in scoring, not in a footnote.

The step-count finding is actionable: if the number of steps a harness takes is the primary predictor of cost, then clawfit should consider adding a `steps_per_task` or `verbosity` field to the agent registry to capture this dimension.

## Preliminary interpretation

Current best reading:
- **Level 5 — Memory/Observability/Evaluation** (primary): evaluation study characterizing L2 harness behavior empirically across models
- Secondary signal for **Level 2** (the harnesses being evaluated are L2 systems): v1.1 is now the most comprehensive independent empirical characterization of the L2 layer

## Claims to verify

- Whether Runta's infrastructure gives systematic advantages to Runta-native harnesses — not disclosed in v1.1 methodology, same conflict from v1.0
- Whether the 1.8–5.0x harness cost range holds outside the five specific models tested (Baseten-hosted subset may favor harnesses optimized for those model families)
- Whether the reward hacking flagging methodology (216 trials) is systematic and reproducible, or manual review of outliers
- Whether step count is causal (more steps → more cost) or confounded with task difficulty (harder tasks require more steps AND are more expensive regardless of harness)
- Whether raw data and harness identities will be published; v1.0 named harnesses; v1.1 may or may not

## Status

- First scan: 2026-11-18 (prior version tracked at `docs/research-watch/2026-09-02-frontierharness-eval-9-harness-benchmark.md`)
- Registry action: none — evaluation study, not a harness/agent/LLM
- Directly relevant to clawfit scoring calibration: the model–harness interaction finding should be reviewed against scoring.py's cartesian product assumption
- 📡 Note: v1.1 is the second FrontierHarness signal from Runta; if v1.2 or a third-party replication adds more models or tasks and confirms the interaction term finding, that would constitute a two-signal justification for adding a `model_harness_interaction` annotation to the L2 canonical section
