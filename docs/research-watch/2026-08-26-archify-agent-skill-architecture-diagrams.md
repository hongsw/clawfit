# Research Watch: archify — Cross-Runtime Agent Skill for Interactive Architecture Diagrams

- Repo: https://github.com/tt-a1i/archify (⭐17,437)
- Source: GitHub Trending (daily, all languages)

## Why this is worth watching

Architecture documentation is a perennial bottleneck in software development — expensive to create, quick to go stale, and consistently skipped under deadline pressure. archify positions itself as an agent skill that removes that friction by generating interactive, self-contained HTML diagrams directly from codebase context or natural language descriptions. The differentiating claim is "verifiable" diagrams: a typed JSON intermediate representation with deterministic validation means the diagram structure can be checked, not just rendered.

The skill runs across five major agent runtimes (Claude Code, Cursor, opencode, Codex CLI, Raven) without modification. This cross-runtime portability, achieved via the Agent Plugins-compatible format, gives it ecosystem breadth at launch that single-runtime tools take months to accumulate.

## What stands out immediately

- **Five diagram types**: architecture, workflow, sequence, data flow, lifecycle — covers the main artifacts software teams actually produce
- **Self-contained HTML output**: no external server dependency; the rendered diagram ships as a single file with motion, PNG/SVG/WebM export, and dark/light themes
- **Architecture Delta**: before/after comparison on diffs — addresses the code-review use case where reviewers need to see structural impact, not just line changes
- **Interactive exploration**: route tracing, upstream/downstream reach analysis, guided stories — shifts diagrams from static decoration to navigable documentation
- **Typed JSON intermediate representation**: deterministic validation means diagram generation can be unit-tested; this is structurally different from "paste into Mermaid and hope"
- **Cross-runtime compatibility at launch**: Claude Code, Cursor, Codex CLI, opencode, Raven — broad distribution on day one
- **17,437 stars** at time of scan — high velocity for a single-purpose agent skill; suggests strong unmet demand, not a niche use case

## Why clawfit should care

archify is a canonical L4 capability-layer tool: it adds a bounded, well-defined capability (architecture diagram generation) to any agent that supports skill installation. clawfit currently has no `documentation_generation` task type, and no way to surface tools that specialize in structural output (diagrams, specs) rather than code or prose.

More broadly, archify's cross-runtime portable format and interactive output quality set a quality bar for what an "agent skill" can be. The existing clawfit skill entries in the registry are often simpler instruction bundles; archify shows that skills can include substantial rendering infrastructure.

The "Architecture Delta" feature also raises a new dimension: `review_mode: [none | diff-aware]` — for code-review task profiles, a skill that understands structural change is meaningfully different from one that generates from scratch.

## Preliminary interpretation

Current best reading:
- **Level 4 — Capabilities / Skills / MCP**: primary. archify is a bounded capability module that augments agent runtimes with a specific output type (interactive architecture diagrams). It does not orchestrate agents or manage memory; it produces a well-defined artifact.
- **Level 6 secondary** (weak): the interactive HTML output is a human interface layer — architecture diagrams are navigation tools for human engineers, not just machine-readable data.

Cross-signal: archify + garden-skills (also L4, also cross-runtime, also tracked today) are two signals for the "cross-runtime portable agent skill" format pattern — but this pattern is already established (scientific-agent-skills 2026-08-04, awesome-agent-skills 2026-04-24). Today's pair confirms continued growth in this category, not a new sub-type.

## Claims to verify

- Whether the "verifiable" typed JSON intermediate representation is actually checked at render time or is a developer-mode assertion only
- Whether Architecture Delta correctly handles non-trivial rename/move refactors or only detects add/remove
- Whether cross-runtime compatibility relies on Agent Plugins v1.0 (2026-08-22) or a prior skill manifest format — if the former, archify is a confirmation signal for that standard's adoption velocity
- Star velocity: 17k stars for a skill focused on a single output type suggests either genuine demand or a GitHub Trending spike; checking commit frequency and issue resolution rate would disambiguate
- The `guided stories` feature — whether it requires LLM calls to narrate or is purely graph traversal — affects per-use token cost

## Status

- Tracking: first signal 2026-08-26
- Stars: 17,437 — above 100-star threshold; above 5k registry threshold in principle
- Registry decision: skip this cycle. No `documentation_generation` or `diagram_skill` slot in agents.json/llms.json/hardware.json. The tool is a capability layer, not an agent runtime or LLM. Schema field needed: `task: architecture-diagramming` in capability registry.
- Schema watch: `task: [architecture-diagramming | ...]`; `output_format: [code | prose | diagram-html | ...]`; `review_mode: [none | diff-aware]`
- Watch: whether Agent Plugins v1.0 adoption enables archify to ship via `claude plugin install archify` — that would confirm the cross-vendor plugin format is live
