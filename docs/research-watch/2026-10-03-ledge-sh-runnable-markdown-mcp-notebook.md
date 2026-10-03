# Research Watch: Ledge.sh — Runnable Markdown Notebook with MCP Server

- Repo/Link: https://ledge.sh
- Source: GeekNews

## Why this is worth watching

Ledge.sh turns Markdown notes into executable notebooks — shell commands, SQL, Python, Node.js, and AI prompts all run inline with ⌘↩. Unlike Jupyter (Python-centric) or Notion (execution-free), it targets DevOps and developer workflows where the runbook *is* the tool. It also ships a built-in MCP server, making it a bidirectional agent interface: AI agents can read, search, create, and edit notes programmatically.

## What stands out immediately

- Executes shell, Python, SQL, TypeScript, and AI prompts natively inside Markdown files
- MCP server bundled: Claude and other agents can operate on the note workspace directly
- Remote execution over SSH — run commands on remote servers from the same note
- Profile-based secrets management keeps credentials out of note files
- Syncs via iCloud, Dropbox, git, or Syncthing — no cloud lock-in

## Why clawfit should care

Ledge.sh occupies the intersection of L6 (developer interaction surface) and L4 (MCP capability provider). As agents increasingly need runbook-aware context — incident response, deployment checklists, SQL exploratory queries — a notebook that is itself an MCP server becomes a natural agent memory and tool substrate. This is adjacent to the skills-as-notes pattern seen in obra/superpowers and the persistent-memory angle of Pi Durable.

## Preliminary interpretation

Current best reading:
- **Level 6 — Developer Interaction / Notebook Interface** (primary)
- **Level 4 — MCP Capability Provider** (secondary)

## Status

- New discovery (2026-10-03); monitoring for GitHub repo and adoption signals
