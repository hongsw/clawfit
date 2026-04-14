# Research Watch: SnapState — Persistent State for AI Agent Workflows

- Repo/Link: https://snapstate.dev
- Source: Hacker News (Show HN, 5 points)

## Why this is worth watching
SnapState explicitly targets persistent state management for AI agent workflows — a problem distinct from session memory (claude-mem), knowledge bases (GBrain), or vector stores. It frames the problem as workflow continuity across agent restarts and handoffs. Low HN traction (5 points) but the problem framing is precise and the market timing aligns with increasing agent workflow longevity.

## What stands out immediately
- **Workflow state, not just memory:** Differentiates from memory MCP plugins by targeting execution state checkpointing across agent sessions
- **Agent workflow framing:** Explicitly built for multi-step agent pipelines, not general app state
- **Very early:** Low HN points; likely pre-launch or very early product stage
- **State persistence gap:** Identified a gap distinct from existing Level 4a memory tools

## Why clawfit should care
This adds a sub-category to Level 4a that is currently underrepresented: **execution state persistence** (vs. knowledge/memory persistence). As agents run longer workflows (sprint contracts, PRD loops, ralph-style iterations), they need to checkpoint execution state, not just update a memory store. clawfit's scoring should eventually distinguish between `memory_type: knowledge` vs `memory_type: workflow_state`. For now, this is an early signal of a productizing sub-category.

## Preliminary interpretation
Current best reading:
- **Level 4a — Memory / state layer** (workflow execution state sub-type)

## Status
- Tracking: LOW-MEDIUM priority — early product, low traction; watch for HN/GitHub follow-up signals
- Note: Problem framing is sound; product viability unconfirmed
