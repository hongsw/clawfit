# Research Watch: AgentJev-0.6B — System One Decision Model for Agent Control Flow

- Repo: https://github.com/malevrigns/agent-jev (⭐266)
- Source: Web search on Jev pattern; related to "Jev in 25 Lines of Python" HN 513 pts (nobodywho.ai blog)

## Why this is worth watching
AgentJev-0.6B is an open-source Apache-2.0 implementation of the Jev typed decision model architecture — the sixth cross-date signal for this pattern since 2026-09-16. Unlike TypeSafe Jev (closed commercial API), OpenJev (no confirmed repo), and Kev (Qwen3.5 fine-tune, unconfirmed star count), AgentJev is a public, licensed, independently confirmed Apache-2.0 implementation with benchmark data. The underlying architecture is distinct: Qwen3-0.6B with the language model head removed, replaced by a permutation-equivariant scoring head that outputs probability logits over candidate options — no vocabulary projection, no token generation. This is the first tracked Jev-pattern implementation where the architecture is fully documented and reproducible.

## What stands out immediately
- **Zero output-token decoding**: the model never generates text; it scores a set of pre-defined candidate strings and returns probability distributions — eliminating all token-generation overhead for routing and decision tasks
- **Three decision primitives**: boolean (yes/no), multi-option (ranked choice from a provided list), ordinal scoring (1–5 or similar scales) — covers the structural decision types an agent needs for routing, retry, escalate, and rank
- **~50ms forward pass**: consistent with the Jev architecture's latency target (TypeSafe claims 40–200x faster than frontier LLMs on decision tasks); at 0.6B parameters, this should hold on consumer-grade hardware
- **Shared-prefix KV caching**: state is encoded once, then all candidate branches scored in one pass; ~2x speedup on wide candidate sets (benchmarked at 64 options) — scales to agents with large routing tables
- **79.25% top-1 accuracy on Typed Decisions benchmark (2,000 questions)**: first independently verified accuracy number for a Jev-class implementation tracked in this project
- **2,048-token context window**: sufficient for structured decision inputs (diffs, traces, log excerpts) without requiring chunking
- **Apache-2.0 license**: commercially usable without restriction, unlike EUPL-1.2 (NobodyWho) or TypeSafe's proprietary API

## Why clawfit should care
The Jev pattern across six signals now spans: a closed commercial API (TypeSafe), an open replication (OpenJev), an RL-trained policy variant (ConvAI), a compact Qwen3.5 fine-tune (Kev), a benchmark suite (JevBench, today), and now a documented Apache-2.0 implementation with public accuracy data (AgentJev). The last piece — a confirmed open-source implementation with reproducible architecture and benchmark numbers — is what converts a pattern-under-observation into an infrastructure layer the ecosystem is actually building on. If clawfit's scoring model adds a `decision_model` dimension (separate from the full LLM cost dimension) for routing/control-flow decisions, AgentJev is the first concrete candidate to populate that dimension. The 266-star count is modest, but the architecture documentation and Apache-2.0 license make it the highest-clarity Jev signal yet from a reproducibility standpoint.

## Preliminary interpretation
- **Level 1 — Base Runtime (primary)**: standalone inference model providing decision outputs to agent control flow — a callable substrate, not a skill or harness feature
- **Level 4 — Capabilities / Skills (secondary)**: when deployed as a routing/escalation component inside an existing harness, it occupies the capability layer (a component the harness calls, not the harness itself)

## Claims to verify
- Whether 79.25% top-1 accuracy on the Typed Decisions benchmark holds across all three primitive types (boolean vs. multi-option vs. ordinal may differ substantially)
- Whether the ~50ms latency is measured on CPU, GPU, or both (matters for on-device deployments on NobodyWho or similar runtimes)
- Whether the permutation-equivariant scoring head is a novel architectural contribution or a standard multi-class softmax (the description suggests it is non-trivial but this should be verified from the model card or paper)
- Whether the Apache-2.0 license covers both the code and the model weights (some repos are Apache-2.0 on code but more restrictive on weights)
- Star trajectory: 266 stars at first tracking; if it crosses 5k it qualifies for registry consideration

## Status
- **Sixth signal for the Jev/typed-decision-model pattern** (TypeSafe Jev 2026-09-16, OpenJev 2026-09-19, ConvAI RL-NAR 2026-09-20, Kev 2026-09-22, JevBench 2026-09-23, AgentJev today)
- 266 stars — below registry threshold (5k); above minimal monitoring threshold (100)
- **First Jev-pattern signal with a public Apache-2.0 license AND documented architecture AND benchmark data** — highest reproducibility signal in the pattern to date
- Canonical promotion check: Jev pattern is now at six cross-date signals from five independent organizations; the only remaining gap is a production adoption case above 5k stars; monitoring
- Not a registry candidate yet (star count below threshold, no deterministic cost/latency on standard hardware published)
