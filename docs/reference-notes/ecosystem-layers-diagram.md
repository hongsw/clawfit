# clawfit Ecosystem Layers — Visual Reference

*Axes, boundary layers, and multi-layer collapse patterns*

---

## 1. The 7-layer stack + substrate

```
┌─────────────────────────────────────────────────────────────────┐
│  L7  Human Interface / Voice / Input-Output                     │
│       Voicebox, VoxCPM, Ghost Pepper, Zed 1.0, cc-connect       │
├─────────────────────────────────────────────────────────────────┤
│  L6  Data / Evidence / Knowledge Infrastructure                 │
│  ├─ L6a  Retrieval-native   MinerU, LightRAG, PageIndex, CocoIndex, airweave    │
│  └─ L6b  LLM-native KB      wuphf, GBrain, 찰떡AI  (Karpathy pattern, 2026-04-04) │
├─────────────────────────────────────────────────────────────────┤
│  L5  Research / Evaluation / Benchmark / Autoresearch           │
│       autoresearch, SWE-bench, mini-swe-agent, memvid, Engram   │
├─────────────────────────────────────────────────────────────────┤
│  L4  Capability Extension (Memory / Skills / Tools / MCP)       │
│  ├─ L4a  Memory        cognee, claude-mem, memvid, GitNexus     │
│  ├─ L4b  Skills        agency-agents (92k★), obra/superpowers   │
│  └─ L4c  Tool/MCP      MCP ecosystem, GoModel, cc-switch        │
├─────────────────────────────────────────────────────────────────┤
│  L3  Team Harness / Executable SSOT / Governance                │
│       CLAUDE.md, gitagent, gsd, acai.sh (ACID), obra/superpowers│
├─────────────────────────────────────────────────────────────────┤
│  L2  Meta Wrappers / Harnesses / Orchestration                  │
│       DureClaw, revfactory/harness, Archon, deepagents, Hashline│
├─────────────────────────────────────────────────────────────────┤
│  L1  Base Runtimes / Primary Agent Surfaces                     │
│       Claude Code, OpenCode, Aider, Goose, OpenHands, Cline     │
├─────────────────────────────────────────────────────────────────┤
│  L0* Inference Runtime Substrate  (companion axis, not a level) │
│       Ollama, llama.cpp, vLLM, MLX, TensorRT-LLM, exo          │
└─────────────────────────────────────────────────────────────────┘
             ↑ sits on hardware (laptop / workstation / cloud)
```

*L0 is a companion axis, not a numbered level — see `inference-runtime-substrate.md`*

---

## 2. Recommendation decision axes

```
                    TASK
                   (what)
                     │
    LATENCY ─────────┼────────── BUDGET
    (how fast)        │          (how much)
                      │
         NETWORK ─────┼───── HARDWARE
         (online/off)  │      (where)
                       │
              STATEFULNESS
              (memory model)

Central node = the recommendation engine
Each axis is a hard filter before scoring begins
```

---

## 3. Online vs offline decision tree

```
network: online                         network: offline
      │                                       │
      ▼                                       ▼
Cloud API / managed                    Inference substrate needed
      │                                       │
      ├─ cloud_api      ┌─────────────────────┤
      │   (Anthropic,   │ hardware: laptop     │ hardware: workstation
      │    OpenAI,      │ Apple Silicon        │ CUDA GPU
      │    Mistral)     │ → Ollama / MLX       │ → vLLM / llama.cpp
      │                 │                     │
      ├─ cloud_managed  │ hardware: edge       │ hardware: home_cluster
      │   (Bedrock,     │ → LiteRT-LM          │ → exo
      │    Azure AI,    │   MLC LLM            │
      │    Vertex AI)   └─────────────────────┘
      │
      └─ cloud_vm
          (self-hosted
           vLLM/TGI on EC2)
```

---

## 4. Multi-layer collapse — how tools span levels

Several tools intentionally span multiple levels. This is a named pattern ("multi-layer collapse"):

```
Tool                Primary    Secondary   Why it spans
──────────────────  ─────────  ──────────  ──────────────────────────────
deepagents          L2         L1          CLI = base agent; SDK = harness
Warp                L7         L2, L1      Terminal + Oz platform + agent
DureClaw            L2         L4c, L3     Orchestration + MCP + SSOT signals
cc-switch           L4c        L3          Provider switcher + atomic SSOT writes
memvid              L4a        L5          Memory store + research/benchmark signals
GitNexus            L4a        L4c         Graph-RAG memory + 16 MCP tools
Claude Computer Use L1         L7          Agent runtime + desktop interface
NVIDIA OpenShell    L1         L4c         Runtime substrate + egress policy
찰떡AI (Chaltteok)  L6b        L4c         LLM-maintained graph KB + host-protective MCP routing
agency-agents       L4b        —           Cross-tool portable persona skill pack (144 agents, 12 verticals)
```

**Rule:** A tool gets a *primary* level (where it does most of its work) and *secondary* levels (where its features genuinely operate). Being mentioned in a scan signal does not constitute secondary-level membership.

---

## 5. Scoring weight axes (current v0.4)

```
fit_score = Σ weighted components

┌───────────────────────────────────────────────────────────────┐
│  Component              Weight   Hard filter?                  │
├───────────────────────────────────────────────────────────────┤
│  latency match           0.50    Yes (eliminates)              │
│  cost match              0.25    Yes (eliminates)              │
│  LLM preference          0.15    No (soft bonus)               │
│  baseline                0.10    No (always present)           │
│  vertical task bonus    +0.05    No (exact vertical tag hit)   │
│  task mismatch           x0.25   Yes (hard multiplier)         │
│  network mismatch        x0.25   Yes (hard multiplier)         │
│  statefulness miss       x0.50   Yes (hard multiplier)         │
└───────────────────────────────────────────────────────────────┘

Hard multipliers penalize critical mismatches; they do not eliminate
(elimination happens in filters.py before scoring.py runs).

Vertical task bonus: +0.05 when an agent explicitly lists a vertical task tag
(financial-research, security-testing, legal-review, etc.) — rewards purpose-built
vertical agents over generic agents that only match via parent-tag fallback.

Budget filter tiers (BUDGET_CEILINGS in filters.py):
  free   → cost_per_1k_tokens == 0.0       (local/offline models only)
  low    → cost_per_1k_tokens  < $0.001    (DeepSeek Flash, GPT-4o-mini)
  medium → cost_per_1k_tokens  < $0.005    (GPT-4o, Claude Sonnet, Mistral Medium)
  high   → no constraint                   (all models pass)
  float  → absolute ceiling, backward-compatible (e.g. --budget 0.003)
```

---

## 6. Governance / deployment boundary

```
                   governance_need: none
                           │
           ┌───────────────┴───────────────┐
   cloud_api               │           cloud_managed
   (Anthropic/             │           (Bedrock / Azure AI /
    OpenAI API)            │            Vertex AI)
           │               │                │
     No audit trail        │         Audit trail, VPC,
     No data residency      │         data residency,
     Low governance cost    │         SOC 2 / HIPAA support
           │               │                │
           └───────────────┴───────────────┘
                   governance_need: hard

   network: offline + workstation = escape hatch
   (no cloud dependency, data never leaves premises)
```

---

## 7. Ecosystem layer taxonomy vs. recommendation filter axes

These are two separate coordinate systems that clawfit maintains:

```
TAXONOMY (reference-levels.md)            RECOMMENDATION (filters.py + scoring.py)
────────────────────────────────────────  ───────────────────────────────────────
L1  Base runtimes           ←→           agent.tasks (generic: qa, code-gen, research…)
L1  Vertical domain agents  ←→           agent.tasks (vertical: financial-research,
                                           security-testing, legal-review, …)
                                         TASK_PARENTS hierarchy: vertical → generic fallback
L2  Harnesses               ←→           agent.statefulness
L3  SSOT / governance       ←→           (future: governance_need filter)
L4  Capability extension    ←→           (future: capability_tag filter)
L5  Research / evaluation   ←→           (future: benchmark_source field)
L6a Retrieval-native infra  ←→           (future: knowledge_backend: retrieval)
L6b LLM-native KB           ←→           (future: knowledge_backend: llm_native)
L7  Human interfaces        ←→           (implicit in agent delivery)
                                         llm.cost_per_1k_tokens
                                         llm.latency  (LATENCY_RANK: low/medium/high)
                                         budget tiers (BUDGET_CEILINGS: free/low/medium/high)
                                         hardware.type
                                         network: online/offline
```

The taxonomy describes *what something is*. The recommendation filters describe *what you need*.
Schema linkage (Phase 3 of the ontology hardening roadmap) connects the two.
