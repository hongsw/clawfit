---
# Research Watch: gitagent — Git-native open standard for agent definition

- Repo: <https://github.com/open-gitagent/gitagent>

## Why this is worth watching
gitagent proposes Git itself as the distribution and versioning layer for AI agents — clone a repo to instantiate an agent. This is a structurally distinct approach from harness plugins, MCP servers, or JSON registries. If it gains traction, it could become a standard for how agents are shared, versioned, and deployed across frameworks.

## What stands out immediately
- **Instantiation model:** `git clone` a repo = spawn an agent — Git as package manager for agents
- **Built-in version control, collaboration, compliance** via standard Git workflows
- **Multi-framework support:** not tied to one runtime
- **Emphasis on Git-native lifecycle:** branches, tags, PRs as agent governance primitives
- Positions Git as the **SSOT (single source of truth)** for agent definitions

## Why clawfit should care
gitagent overlaps directly with the Level 3 pattern (Team harness / executable SSOT / governance layer). It challenges the assumption that agent definitions must live in proprietary plugin registries or JSON files. If the Git-native model spreads, clawfit's registry approach may need to incorporate or reference Git-based agent sources.

Also relevant: this creates a natural comparison axis — plugin/registry-based distribution (Chops, skills-cleaner) vs. Git-native distribution (gitagent).

## Preliminary interpretation
- Primary: **Level 3 — Team harness / executable SSOT / governance layer**
- Secondary: **Level 2 — Meta wrappers / harnesses** (distribution mechanism)

## Status
- Medium priority. Novel distribution model worth watching.
- Not yet a registry entry — needs to stabilize before inclusion.
