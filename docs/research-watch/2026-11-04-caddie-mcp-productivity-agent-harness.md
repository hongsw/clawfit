# Research Watch: Caddie — Personal Productivity App with MCP Server and Agent Harness

- Repo/Link: https://usecaddie.app
- Blog: https://usecaddie.app/blog/agents
- Source: GeekNews (front page, 2026-11-04)

## Why this is worth watching

Caddie is a Mac-first productivity app (notes, tasks, calendar, meeting recording) that has grown an MCP server and agent harness layer on top. Agents run on the user's own Claude Code or Codex account, have access to MCP tools and local Mac apps, and can be directed via skills. Its blog post on "practical principles for developing with agents" surfaced on GeekNews and signals that Caddie's user base is actively shipping with multi-agent workflows.

## What stands out immediately

- **MCP server for read/write access**: Claude, ChatGPT, Cursor, and other agents can read and write Caddie notes, tasks, and calendar — turning personal context into agent-queryable state
- **Agents on user-owned accounts**: agents run on the developer's own Claude Code or Codex subscription, not a separate cloud; Caddie acts as a task router and context store
- **API catalog and agent skills index**: Caddie publishes its own agent capabilities in a machine-readable form, suggesting it wants to be discoverable by agent orchestration layers
- **Meeting recording without a bot**: native macOS recording (requires macOS 26), producing structured notes and action items that agents can act on
- **"Five or more agents running" principle**: the blog post from their product team argues for running agents continuously and overnight, with a coordinator agent per project — Caddie is designed around this workflow
- **Mac-only constraint**: currently requires macOS 13.3+ on Apple silicon; not cross-platform

## Why clawfit should care

Caddie represents a category of tool that sits at the boundary of L2 (harness) and L4b (domain skill pack): it's a personal context layer that agents query, not an agent framework. This is the emerging "personal AI workspace" pattern where the user's notes, tasks, and calendar become machine-readable state that agents act on. If Caddie gains adoption among developers who run coding agents daily, it becomes relevant as a companion tool that feeds context to agents rather than a tool clawfit recommends directly. The practical principles post is also a useful behavioral spec for the kind of user who would score highest on `current_ai_usage: multi_agent`.

## Preliminary interpretation

Current best reading:
- **Level 2 — Harness / wrapper layer (secondary)**: acts as task router and context store for agents running on user-owned accounts
- **Level 4b — Domain skill pack (primary)**: functions as a personal context layer that agents query through MCP

## Status

- Free beta; $10/month planned
- Mac-only (Apple silicon required); not relevant for Windows/Linux teams
- Watch for: cross-platform support; growth beyond solo developers; registry entry if multi-platform support lands
