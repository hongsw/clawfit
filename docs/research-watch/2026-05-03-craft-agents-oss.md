# Research Watch: craft-agents-oss

- Repo: https://github.com/lukilabs/craft-agents-oss
- Also see: https://craft.do (parent product — document-centric productivity app)

## Why this is worth watching
At 5.7k stars with 61 releases and a v0.9.0 tagged 2026-04-30, craft-agents-oss is not a weekend experiment — it is production tooling shipped by a document-productivity company that claims to build the product using itself exclusively. The Claude Agent SDK + Pi SDK dual-backend design is one of the earliest public examples of a desktop agent surface pairing Anthropic's first-party agent runtime against a competing SDK in the same binary, making it a live datapoint in the multi-vendor anti-lockin pattern tracked since 2026-04-28. The "document vs code centric workflow" framing is a direct challenge to the IDE-threaded model (Zed, Roo Code, Cursor) that currently dominates Level 6.

## What stands out immediately
- Monorepo spans desktop (Electron + React), CLI, headless WebSocket server, and a shared core package set — the surface area is closer to a platform than a single tool
- Three-tier permission model (Explore / Ask to Edit / Auto) maps cleanly onto the `data_sensitivity` axis clawfit already tracks; "Explore" would be relevant for `confidential` profiles
- 32+ MCP server tools for Craft document operations — this is MCP used as the document-layer abstraction, not as an agent capability registry; a distinct usage pattern from the L4c tools tracked elsewhere
- Cron-based event-driven automations and label-triggered workflows are described in the README — positions the product closer to Level 2 harness territory than a pure UI shell
- Large-response summarization via Claude Haiku (>60KB threshold) is a claimed operational detail, not just a design claim; if accurate, represents an internal cost-management pattern worth inspecting
- Headless server mode with TLS and a separate CLI client introduces a thin-client deployment topology not seen in the other L6 entries (cmux, Warp, Zed) — relevant to `network: online` enterprise profiles
- "We build Craft Agents with Craft Agents only — no code editors" is a strong design-origin claim; treat as claim-to-inspect, not validated fact, but if accurate it is a notable dogfooding signal

## Why clawfit should care
The product sits at the intersection of two patterns clawfit is actively tracking: (1) Level 6 fragmentation along workflow surfaces (IDE-threaded / terminal-multiplexed / mobile-remote / web-control), and (2) the multi-vendor anti-lockin cluster (Claude Agent SDK + Pi SDK side by side). If craft-agents-oss stabilizes at 1.0, it represents a distinct workflow-surface subtype — **document-centric desktop agent** — that is not currently represented in the Level 6 taxonomy alongside IDE-threaded (Zed, Roo Code), terminal-multiplexed (cmux, Warp), and messaging-bridge (cc-connect, Happy) entries. The three-tier permission model and headless server mode also touch scoring axes (data_sensitivity, network) that are already in clawfit's filter layer; a registry entry would require mapping those modes to existing filter values. The Apache 2.0 license is clean for any governance profile.

## Preliminary interpretation
Current best reading:
- **Level 6 — Human interface / voice / multimodal layer** (primary — desktop multi-agent UI with document-centric workflow surface; sibling to Zed, cmux, Warp on the IDE/terminal branch but occupying a distinct document-workspace subtype)
- **Level 2 — Meta wrappers / harnesses / orchestration layers** (secondary — event-driven automations, cron scheduling, session-state management, and label-triggered workflows give it non-trivial harness character beyond a pure UI shell; the headless server mode reinforces this)
- **Level 4c — MCP / tool-use layer** (tertiary — 32+ MCP tools for document operations represent a concrete MCP integration, though this is a downstream consumer of MCP rather than a gateway or registry)

Multi-layer collapse is consistent with the pattern observed in Warp (L6 + L2 + L1) and Zed 1.0 (L6 + L2). Document-centric subtype is a new axis not previously named in the L6 internal structure; flag for promotion if a second independent document-workspace desktop agent surfaces.

## Status
- Tracking: medium signal. 5.7k stars and active release cadence meet observation threshold. Registry entry deferred pending v1.0 stability and independent verification of headless-server and large-response-summarization claims. Revisit at 10k stars or v1.0 tag. Document-centric desktop agent subtype flagged as candidate new L6 axis — do not add to reference-levels.md without a second independent datapoint.
