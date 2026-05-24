# Research Watch: google-labs-code/stitch-skills

- Repo: https://github.com/google-labs-code/stitch-skills
- Also see: https://blog.google/innovation-and-ai/models-and-research/google-labs/stitch-ai-ui-design/ · https://github.com/davideast/stitch-mcp · https://codelabs.developers.google.com/design-to-code-with-antigravity-stitch

## Why this is worth watching

At 5,612 stars with +69 in a single day, stitch-skills crosses the 5k registry threshold on its first appearance in this log. The signal gains weight from org provenance: google-labs-code is a Google Labs org, not a community contributor, making this the first non-Anthropic major-model-vendor first-party skill pack in the L4b cluster — a distinct cell in the provenance × vertical matrix that was previously unoccupied (anthropics/financial-services is the only prior first-party model-vendor skill pack, and it is Anthropic-origin). The cross-host compatibility claim (Claude Code, Cursor, Gemini CLI, Antigravity, Codex) also constitutes a fourth corroborating SKILL.md cross-vendor signal, approaching the stable-axis promotion threshold.

## What stands out immediately

- Three installable plugin suites: `stitch-design` (code-to-design, design generation, design system management, HTML extraction), `stitch-build` (React component generation, Remotion video generation, shadcn/ui guidance), `stitch-utilities` (design analysis, prompt enhancement, multi-page site generation)
- Each skill contains a mission control document, executable scripts, knowledge bases, and reference examples — standard Agent Skills open standard format, same SKILL.md-adjacent structure as browserbase/skills and agency-agents
- Hard runtime dependency: the Stitch MCP server must be configured and running in the agent's environment; skills are inert without it
- Apache-2.0 license — permissive, no commercial-use friction
- Google Labs org disclaimer applies: "not an officially supported Google product." This is materially different from a Workspace or Cloud product; continuity risk is higher than a supported GCP API
- `DESIGN.md` is introduced as an agent-friendly design-system artifact — analogous to CLAUDE.md's behavioral-spec role but scoped to design tokens and layout rules; claim to inspect whether this format is independently standardized or Google Stitch-proprietary

## Why clawfit should care

The hard MCP server dependency is the central lock-in signal. Unlike browserbase/skills — which has a local Chrome fallback path — stitch-skills has no degraded mode: without the Stitch MCP server running, all three suites are non-functional. This makes the effective deployment unit not the skill pack alone but the `(stitch-skills) + (Stitch MCP server)` pair, which maps to a `network: online` and `statefulness: session` profile at minimum, and binds the agent to a Google Labs product with no officially supported SLA. For clawfit recommendations, this is a hard `hardware: cloud` / `network: online` coupling with an additional vendor-continuity risk not present in community or Anthropic-first-party packs. The `task: ui-design` and `task: code-gen` surface areas are relevant if those task types are added to the schema; currently neither maps cleanly to an existing clawfit task label.

## Preliminary interpretation

Current best reading:
- **Level 4b — Domain skill pack** (primary): Three suites delivered as installable packs following the Agent Skills open standard, authored by the google-labs-code org. Closest prior art: browserbase/skills (first-party infrastructure vendor, single domain) and anthropics/financial-services (first-party model vendor, regulated vertical). stitch-skills is the first first-party skill pack from a non-Anthropic major model vendor, filling a new provenance cell
- **Level 5 — MCP/context layer** (secondary, via dependency): The required Stitch MCP server is an L5-adjacent runtime dependency; the skills are effectively an L4b interface to an L5 MCP backend. The `(skill pack) + (MCP server)` co-dependency pattern is new to this taxonomy and warrants a structural note
- The `DESIGN.md` artifact, if independently standardized beyond Google Stitch, could become an L3-adjacent SSOT primitive for design systems — parallel to CLAUDE.md for behavior. Single signal; flag for watch

## Status

- 5,612 stars, Apache-2.0, Google Labs provenance — meets star threshold but Google Labs non-supported status, hard MCP server dependency, and single first-party non-Anthropic vendor signal all argue for hold. Registry candidate pending: (1) confirmation that the Stitch MCP server is reliably available outside Google-hosted environments, (2) a second non-Anthropic model-vendor first-party skill pack to confirm the sub-type, or (3) independent community validation of cross-host portability beyond Claude Code and Gemini CLI
