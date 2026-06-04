# Research Watch: Decepticon — Autonomous Red Team Agent

- Repo: https://github.com/PurpleAILAB/Decepticon
- Also see: Shannon (KeygraphHQ, L1 pentest), Strix (usestrix, L1 CI/CD security), Anthropic-Cybersecurity-Skills (L4b)

## Why this is worth watching
Decepticon is the first security agent in this taxonomy whose 16 specialist agents are organized explicitly by kill-chain phase rather than by task type or capability. It ships a pre-engagement planning layer (RoE, ConOps, OPPLAN with MITRE ATT&CK mapping) before any exploit runs — a behavioral governance signal absent from Shannon and Strix. At 4.2k stars with active commits through April 2026, it sits just below the 5k registry threshold and is worth watching closely.

## What stands out immediately
- 16 specialist agents grouped across Orchestration, Reconnaissance, Exploitation, Post-Exploitation, Vulnerability Research, and Domain Specialist phases — each scoped to a single kill-chain role with a fresh context window per objective
- Pre-execution engagement package generation (Rules of Engagement, ConOps, Deconfliction Plan, MITRE ATT&CK-mapped OPPLAN) is a structured planning gate, not a disclaimer; it runs before LangGraph dispatches any specialist
- LangGraph orchestrates agents via Docker socket into a Kali Linux sandbox on an isolated `sandbox-net`; the sandbox is not an afterthought — it is the execution substrate
- Neo4j dual-homed knowledge graph persists attack-chain state across specialist handoffs — this is a cross-agent memory layer, not session-local context
- Model-agnostic: Anthropic, OpenAI, Gemini, DeepSeek, xAI, Mistral, OpenRouter, Nvidia NIM, Ollama — tier-based fallback chain
- Vendor benchmark: 98.08% pass rate on XBOW validation challenges (102/104); Easy 100%, Hard 87.5% — claim to inspect, vendor-authored, independent reproduction not confirmed
- Apache-2.0; Python 75.6%, TypeScript 15.2%, Go 6.3%

## Why clawfit should care
Shannon and Strix established that `qa` is too broad a task label for security agents. Decepticon adds a third data point but also introduces a new architectural question: is kill-chain-phase specialization a form of L2 orchestration (multi-agent harness dispatching specialists), or is the engagement-package gate a light L3 signal (behavioral governance before execution)?

The MITRE ATT&CK pre-planning layer is structurally similar to what a human red-team lead produces before an engagement — it constrains what the orchestrator is permitted to attempt. If that gate is implemented as a blocking check (not a generated artifact that agents ignore), it crosses from documentation into behavioral governance, strengthening the L3 secondary case. This is unverified.

The Neo4j knowledge graph for cross-agent attack-chain state is the first persistent cross-specialist memory layer seen in any security agent tracked here — a potential L5 secondary signal, though depth is unverified.

For the recommendation engine: a `task: red-team` or `task: security-testing` type is increasingly well-motivated. Shannon + Strix + Decepticon now occupy three distinct deployment models within the same domain cluster: Shannon (autonomous exploit execution, practitioner-facing), Strix (CI/CD shift-left, developer-facing), Decepticon (kill-chain orchestration with pre-engagement governance, red-team-lead-facing).

## Preliminary interpretation
Current best reading:
- **Level 2 — Meta wrapper / harness / orchestration layer** (primary: LangGraph multi-agent dispatch across kill-chain-phase specialists with Docker sandbox execution substrate)
- **Level 3 — Team harness / governance layer** (weak secondary: pre-engagement MITRE ATT&CK planning gate; strength depends on whether it is a blocking constraint or a generated artifact — unverified)
- **Level 5 — Memory / context layer** (candidate secondary: Neo4j cross-agent attack-chain persistence — unverified depth)

Contrast with Shannon (L1 base agent, single autonomous pentester) and Strix (L1 base agent, CI/CD integration). Decepticon is not a base agent — LangGraph orchestration over 16 specialists with a planning gate is harness behavior, not runtime behavior.

## Status
- New signal — first observed 2026-05-31; 4.2k stars, below 5k registry threshold
- No registry entry; no map mutation warranted
- Watch criterion: 5k stars OR independent verification that the engagement-package gate is a blocking constraint (would strengthen L3 secondary classification)
- Flag for schema-analyst: `task: security-testing` or `task: red-team` is now a three-signal cluster (Shannon + Strix + Decepticon); promotion from research-watch hold to schema-addition candidate is warranted at the next schema revision cycle
