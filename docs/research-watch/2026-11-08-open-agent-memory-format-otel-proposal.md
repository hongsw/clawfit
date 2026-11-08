# Research Watch: Open Agent Memory Format — OpenTelemetry Moment for Agent Memory

- Repo/Link: https://www.lorekit.io/blog/open-agent-memory-format
- Source: Hacker News (131 points, 2026-11-08)

## Why this is worth watching
LoreKit's author argues that agent memory is at the same pre-standardization inflection point observability was in 2018: every tool (Mem0, LangGraph store, Graphiti, LoreKit, OpenMemory, claude-mem) stores memory in its own shape, so none can read the others. The proposal draws the OpenTelemetry analogy explicitly and sketches three coordination layers — data model, semantic conventions, and an MCP contract with conformance tests — leaving storage and ranking to vendors. No spec or working group exists yet, but the framing is architecturally precise enough to influence how memory tools evolve if it gains traction. 131 HN points suggests the developer community recognizes the problem.

## What stands out immediately
- Cleanly separates two distinct open problems: *export* (moving one person's memory between vendors) and *live addressing* (several agents reading and writing the same memory at the same time); most prior proposals (Portable Memory, Open Memory Protocol) only address export
- Proposed data model uses a memory record with explicit fields: address (scope), key, identity, lifecycle (expiry), writer, content type, and namespaced attributes — intentionally not tied to any storage format
- Semantic conventions layer would be a versioned registry of shared address levels, kinds, and attribute namespaces — analogous to OTel's resource and span semantic conventions
- Contract layer proposes a small MCP operation set (write, read, list, search, archive), which would let any MCP-compatible harness reach any conformant memory store without vendor-specific code
- Conformance tests in place of a reference implementation — vendors prove compliance without forking a central lib
- LoreKit's own schema is offered as "one concrete input," MIT-licensed, with explicit acknowledgment that the eventual spec should live somewhere neutral
- The post is careful not to claim the problem is solved — it notes the governance question (who runs the working group?) is open

## Why clawfit should care
clawfit's registry currently treats memory as a capability dimension but does not score or filter on memory interoperability. If a spec like this gains adoption, `statefulness: session | persistent` will not be enough — a future scoring axis would need `memory_portability: none | export | live` or similar. The proposal also matters for the existing "agent memory MCPs" cluster (OpenMemory, claude-mem, Graphiti, all tracked) — a conformance layer would affect which of them remain relevant. This is the second memory-related signal in two days (Memorilla 2026-11-07 proposed latent-space memory); the two signals address complementary problems (representation vs. interoperability).

## Preliminary interpretation
Current best reading:
- **Level 5 — Memory / Observability Layer** (primary) — a standardization proposal for the memory data model and access protocol
- Cross-cutting: if the MCP contract spec is adopted, it affects L1 runtimes, L2 harnesses, and L4 MCP servers that read/write agent state

## Claims to verify
- Whether any existing memory tool maintainers (Mem0, Graphiti, LangGraph) have engaged with the proposal
- Whether LoreKit's MIT-licensed schema aligns with the illustrated data model, or whether it's illustrative only
- Whether "131 HN points" reflects genuine architect-level engagement or general curiosity
- Whether the proposed MCP operation set is compatible with the current MCP spec version

## Status
- New signal — tracking; no implementation artifact to register yet; watch for a neutral governance body or working group forming around this proposal; this is the **first signal for "agent memory interoperability standard"** as a distinct concept from memory MCPs
