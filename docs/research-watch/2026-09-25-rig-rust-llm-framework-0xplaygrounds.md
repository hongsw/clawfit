# Research Watch: Rig — Modular, Scalable LLM Applications in Rust

- Repo: https://github.com/0xPlaygrounds/rig (⭐8,700)
- Source: Weekly agents-radar digest (September 21, 2026 issue)
- Latest release: v0.36.0

## Why this is worth watching

Rig is a Rust library for building modular, scalable LLM applications. With 8,700 stars and 974 forks, it is a well-established (not trending-spike) signal that has been building quietly while the Python-centric agent ecosystem dominated mindshare. The significance here is architectural, not momentary: Rig is not a Python framework with Rust bindings — it is a native Rust-first design with portable `rig-core` contracts that separate provider bindings from orchestration. The v0.36.0 release indicates sustained active development across a long period, not a single big-bang launch.

The Rust framing has concrete implications for agent deployment profiles: Rust's memory safety guarantees and WASM compilation target open paths for agent deployment contexts where Python is unsuitable — edge hardware, WASM browser sandboxes, embedded devices, and security-sensitive execution environments.

## What stands out immediately

- Native Rust design with modular crate architecture: `rig-core` (portable contracts), `rig-agent` (orchestration), `rig-cassette` (recording/replay)
- 20+ model provider integrations under a single unified interface — provider-agnostic agent code
- 10+ vector store integrations under the same provider-abstraction pattern
- Browser/WASM support via `rig-core` portable contracts — enabling agent deployment in browser environments
- "Cassette" recording and replay: agents can be deterministically replayed, enabling reproducible testing of agent behavior
- Multi-turn agentic workflows with streaming support
- Audio transcription, audio generation, and image generation as first-class modalities alongside text

## Why clawfit should care

clawfit's current L1 (Base Runtime) taxonomy is Python-dominated. Rig is the most substantial signal for a Rust-native agent runtime that targets the full capability surface — not just inference, but tooling, vector retrieval, multi-turn orchestration, and multi-modal operations.

The WASM support is the most taxonomically distinctive feature: it introduces a deployment profile (`network: offline`, `hardware: browser`) not currently in clawfit's scoring model. An agent running in a browser WASM sandbox is fundamentally different from a local CLI agent or a cloud-hosted agent — it has browser-context access, no persistent filesystem by default, and can be deployed to any user without installation.

The cassette replay system is an L5 (Observability/Evaluation) secondary signal: test harnesses that replay agent behavior deterministically are a prerequisite for agent CI/CD, and this is the first L1 framework in the tracking corpus to ship replay as a first-class primitive rather than an external layer.

## Preliminary interpretation

Current best reading:
- **Level 1 — Base Runtime Layer** (primary: Rust-native agent runtime with multi-provider orchestration)
- **Level 5 — Observability/Evaluation Layer** (secondary: cassette recording/replay as native testing primitive)

Rust's WASM target could eventually warrant a separate `hardware: browser-wasm` entry in clawfit's hardware taxonomy, but that requires a second signal confirming browser-deployed agents are a practical deployment scenario (Rig is first signal here).

## Claims to verify

- Whether the 20+ provider integrations are maintained and current (large provider counts in LLM frameworks often have long-tail providers with stale bindings)
- Whether WASM deployment is production-grade or experimental
- Whether the cassette replay system is deterministic for tool-calling agents (non-determinism in tool dispatch is a common failure mode)
- Licensing: check for any commercial use restrictions not obvious from Apache/MIT header

## Status

- Above 5k registry threshold (8,700★); registry entry candidate
- Registry entry deferred: no deterministic public cost/latency data specific to Rig's overhead vs. raw API; Rust self-hosted deployment cost is workload-dependent
- **First tracked Rust-native L1 agent runtime** with full provider abstraction, multi-modal support, and WASM deployment
- `hardware: browser-wasm` is a first-signal axis candidate from this entry
