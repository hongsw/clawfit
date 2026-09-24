# Research Watch: Google ADK for Kotlin 1.0 — On-Device Agent Runtime

- Repo: https://github.com/google/adk-kotlin (⭐not publicly tracked, Google-official)
- Source: Google Developers Blog (announced September 9, 2026)

## Why this is worth watching
Google ADK for Kotlin reaches 1.0 with feature parity to ADK Python and Java — but its differentiating bet is on-device agent execution. By integrating LiteRT-LM and ML Kit (beta), it supports agents that run inference on-device without cloud round-trips. This is architecturally significant: it extends the ADK runtime from cloud-only (servers, JVM) to Android/embedded, creating a new deployment tier for ADK agents. If on-device ADK adoption follows Android's install base, this could substantially shift where L1 agent runtimes operate.

## What stands out immediately
- **On-device agent execution**: LiteRT-LM integration brings inference to the device; agents can run without a cloud API call
- **Hybrid orchestration via Firebase AI Logic**: allows mixing on-device and cloud LLM calls within the same workflow — agents decide per-step whether to use local or remote model
- **Persistent agent state**: Room (SQLite) and AppSearch for local state — on-device agents have durable memory without a cloud state store
- **Compile-time tool schema generation**: KSP annotations (`@Tool`, `@Param`) generate agent tool schemas at build time, not at runtime — reduces startup latency and avoids reflection
- **Kotlin Multiplatform**: server/JVM and Android in one codebase; not Android-only
- **1.0 milestone**: this is a stability commitment from Google, not an experimental release

## Why clawfit should care
clawfit's hardware registry (`hardware.json`) tracks edge/cloud/local deployment tiers. Google ADK Kotlin 1.0 introduces a new deployment axis: mobile/on-device with hybrid cloud fallback. The `network` filter currently treats `offline` as a binary; ADK Kotlin suggests a hybrid pattern (local inference for latency-sensitive steps, cloud for heavy reasoning) that doesn't map cleanly to either `online` or `offline`. The `hardware.json` schema may need a `hybrid_cloud_on_device` deployment type. For the agents registry, this is a strong candidate for an `agents.json` entry once deterministic cost/latency data is available for the on-device inference path.

## Preliminary interpretation
Current best reading:
- **Level 1 — Base Runtime** (primary: full agent execution environment with LLM routing, state, and tool support)
- **Level 7 — Infrastructure** (secondary: Firebase AI Logic hybrid orchestration, KSP build-time schema generation)

## Claims to verify
- Whether LiteRT-LM supports full tool calling or only text generation (tool calling on-device is the harder problem)
- Whether hybrid cloud fallback is deterministic (rule-based) or model-driven
- Star count / adoption signal for the Kotlin repo specifically
- Cost and latency benchmarks for on-device vs. cloud inference paths in ADK Kotlin

## Status
- First research-watch doc for ADK Kotlin specifically (ADK Python tracked earlier); 1.0 is a new milestone, not an incremental update
- Google-official repo; bypasses star threshold per scan policy
- Registry candidate: agents.json entry appropriate once deterministic latency data for on-device path is confirmed; currently deferred
- Potential `hardware.json` implication: `mobile_on_device` or `hybrid_mobile_cloud` deployment type
