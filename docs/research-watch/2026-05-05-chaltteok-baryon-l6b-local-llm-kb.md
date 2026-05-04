# Research Watch: 찰떡AI (Chaltteok) — Baryon Labs, Seoul

- Repo: https://github.com/baryonlabs/chaltteok-app-mcp (MIT, Rust + JS, 0★)
- Also see: https://chaltteok-app.baryon.ai/ (product site); https://github.com/baryonlabs (parent org, 20 repos); https://github.com/nex-crm/wuphf (L4a/L6b, general-purpose LLM wiki); https://github.com/baryonlabs/win-ai-app (main Tauri app — currently private); https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f (Karpathy LLM Wiki gist, L6b architectural anchor)

## Why this is worth watching

Chaltteok is a closed-beta Windows desktop assistant targeting Korean SMB document workflows (quotations, legal cases, vendor notes) where the LLM maintains a local domain-specific knowledge graph rather than retrieving from an indexed store — a direct implementation of the Karpathy LLM Wiki pattern, but applied narrowly to a single professional vertical rather than as a general-purpose tool. The open-sourced MCP routing layer (`chaltteok-app-mcp`, MIT Rust crate) is a concrete, inspectable artifact confirming the architectural claims, even though the main application remains private. Combined with the local-only data posture (Korean personal data law compliance), this is the first L6b signal where domain specificity and privacy regulation are both primary design constraints rather than secondary features.

## What stands out immediately

- **Domain-narrow L6b implementation.** The knowledge graph is seeded from the user's own past business documents (quotations, vendor price lists, product catalogs, client notes). The LLM maintains nodes and edges for domain terminology, pricing, and practices specific to that user's business — not a general wiki, not a shared KB. This is L6b (LLM maintains the knowledge artifact) at a narrower scope than wuphf (general multi-agent wiki) or GBrain (general markdown graph).
- **Local-only architecture is a hard design constraint, not a configuration option.** The product site states that all data lives on-device only. This is presented as a regulatory compliance stance (Korean personal data protection law) and a sales-trust argument for SMB clients sharing confidential pricing and client data. Privacy-by-design at the KB layer is a new dimension not previously seen in L6b implementations.
- **Open-sourced MCP module is the inspectable artifact.** `chaltteok-app-mcp` was extracted from `tauri-app/src-tauri/src/mcp.rs` in the private main app. The README confirms it normalizes actions from external AI agents (OpenAI Codex, Anthropic Claude) with the host app's internal operations into a safe execution plan. Agent routing is keyword-based: code/implementation/fix keywords → Codex; document/analysis keywords → Claude; default → Codex. Override via `preferred_agent` parameter. The `Plan` output includes a `GraphUpdate` field with `nodes_touched` and `edges_added`, confirming the knowledge graph is updated as a side-effect of each document operation.
- **Tauri + Rust main app architecture (private).** The main application (`baryonlabs/win-ai-app`) is confirmed as a Tauri app from the MCP module README's reference to `tauri-app/src-tauri/src/mcp.rs`. The choice of Tauri for a privacy-first desktop app is consistent with the local-only posture. App is not publicly accessible.
- **Dual-ecosystem MCP module (Rust crate + npm package).** The same routing logic is shipped as both a Cargo crate and an npm package. This is unusual for a Korean-market SMB desktop app and suggests Baryon Labs anticipates embedding the routing logic in environments beyond the native Tauri shell — possibly web-based frontends or server-side Node.js contexts in future versions.
- **Baryon Labs has adjacent signals.** The org's other repos include `glhub` (TypeScript, "open-source system of record for AI agent work — lineage, audit, evolution memory"), `glctl` (Rust CLI for AI agent generation lineage), `experiential-memory-dataset` (dataset for memory systems in long-running AI agents), and `agentixwork-terminal` (Ghostty-based macOS terminal for AI coding agents, 1,212 forks). The KB/memory/lineage axis is consistent across multiple repos — Chaltteok is not an isolated product experiment.
- **Version v1.2.3 closed beta.** The product is past v1.0 but in closed beta; the MCP module was published as an independently installable package but carries 0 stars. No independent reviews or adoption signals confirmed outside this submission.
- **Two-LLM routing without a unified abstraction.** The keyword routing between Codex and Claude is deterministic and simple (keyword match → agent). This is a working implementation, not a sophisticated orchestration layer. It surfaces a practical design choice: rather than paying for a single premium model for all tasks, the app routes cost-sensitive drafting tasks to whichever model fits the verb. The MCP module makes this routing swappable by host apps.

## Why clawfit should care

The L6b sub-layer formalized on 2026-05-05 (anchored by Karpathy LLM Wiki + wuphf + GBrain) currently has only general-purpose implementations at confirmed canonical status. Chaltteok is the first submitted signal where L6b is the *primary product architecture* applied to a specific vertical (Korean SMB document workflows) with local-only data as a regulatory requirement. This raises a question the current taxonomy does not distinguish: is domain-specific local L6b a sub-type of L6b, or merely an instance of it?

For the recommendation engine, this matters because a user profile like `task: writing` + `statefulness: persistent` + `network: offline` + `data_sensitivity: confidential` currently scores no L6b-adjacent options — clawfit has no registry entries for domain-adapted knowledge-base agents. Chaltteok, if it reaches public launch and stable star count, would be the first candidate entry for that profile intersection.

The open-sourced MCP routing layer is also structurally relevant to the L4c sub-cluster: it demonstrates a pattern where the MCP abstraction sits between the knowledge graph host and multiple LLM backends, normalizing actions without exposing host internals to the agents. This is architecturally distinct from most L4c MCP tools (which expose capabilities outward to any MCP client). The "safety-first, host-defined actions only" constraint is a new design axis not previously documented in L4c entries.

## Preliminary interpretation

Current best reading:

- **Level 6b — LLM-native KB (primary):** The product's core value proposition is an LLM-maintained domain-specific knowledge graph built from the user's own documents. Write authority belongs to the LLM (graph nodes and edges are LLM-generated and maintained); the human reads outputs (generated documents) but does not maintain the graph manually. This satisfies the operational L6b definition established 2026-05-05.
- **Level 4c — MCP tool-use layer (secondary):** The open-sourced `chaltteok-app-mcp` module is a host-side MCP routing layer that normalizes multi-LLM agent actions. It sits squarely in the L4c MCP adapter sub-cluster, but with a "host-protective safety-first" constraint not previously seen in that cluster.
- **Level 1 (weak tertiary, claim-to-inspect):** The pre-submitted signal notes suggest "Level 1 secondary" but the evidence does not support this. Chaltteok is not a base agent runtime; it is a desktop application with an embedded LLM routing layer. The Tauri app is the agent surface (closer to L6), not a re-usable agent runtime (L1). Reclassify the original suggestion: Level 1 is not warranted here.

**Candidate sub-pattern: domain-specific local L6b.** Chaltteok's profile — vertical-specific domain KB + local-only + privacy-regulation-driven + SMB target — does not match wuphf (general-purpose, multi-agent, cloud-compatible) or GBrain (general-purpose, Markdown+PGLite). If one more signal appears with the same combination (domain-narrowed L6b + local-only + regulatory driver), a named sub-pattern is warranted.

## Limitations and signal quality

- **0 public stars on the MCP module; main app is private.** The product is in closed beta and has not been publicly launched. All architectural observations are sourced from the MCP module README and the product landing page. The main Tauri application has not been independently inspected.
- **Star count is not the only barrier.** The clawfit L6b promotion threshold (established 2026-05-05) is ≥5k stars with L6b as clear primary classification. Chaltteok is not near this threshold and the main app is private. It is not a registry candidate today.
- **Korean-market product with no English documentation.** The product site and README are primarily in Korean. All content cited in this document was translated or extracted via automated tools. Mistranslation risk is non-zero; key claims should be re-verified against primary Korean source material before any promotion decision.
- **Claims in the product site are marketing-framed (claim to inspect).** The "5-minute draft" claim and the description of LLM-maintained graph behavior on the product site have not been independently tested. The MCP module architecture supports the graph-update claim structurally (GraphUpdate field in Plan output), but whether the graph actually improves downstream document quality over time is unverified.
- **win-ai-app is private; only MCP module is inspectable.** The main Tauri app is referenced in the MCP README but not publicly accessible. The knowledge graph storage implementation (how nodes/edges are persisted on-device, what local graph store is used) is not visible.

## What would constitute a promotion signal

1. **Public launch of the main Tauri app** — the win-ai-app repository becomes public or a public installer is released, enabling independent architectural inspection.
2. **Star count crossing a meaningful threshold** — the MCP module reaching ≥500★ or the main app reaching ≥1k★ would indicate non-trivial developer adoption beyond the submitter's own ecosystem.
3. **A second independent domain-specific local L6b tool** — if another product surfaces with the same profile (vertical-narrowed LLM-maintained KB + local-only + regulatory driver), the sub-pattern is real and Chaltteok gains comparative context.
4. **Independent user reports in Korean developer communities** (GeekNews Korea, Blind, OKKY) confirming the closed-beta experience matches the architectural claims.

## Status

- Pre-threshold; no reference-levels.md mutation. Classified L6b primary (domain-specific local LLM-native KB), L4c secondary (host-protective MCP routing layer). Monitor for public app launch, Korean dev community coverage, and a second domain-specific local L6b signal.
