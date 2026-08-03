# Research Watch: graph-tool-call — MCP Multi-Server Overload Pattern

- Repo/Link: https://github.com/SonAIengine
- Source: GeekNews front page

## Why this is worth watching
A Korean developer documented a repeatable failure mode: connecting one MCP server to an agent works well, but accuracy degrades after adding GitHub, Slack, a database connector, a browser, and an internal API simultaneously. The tool selection space becomes too large for the model to navigate reliably. This is an empirically observed pattern, not a theoretical concern.

## What stands out immediately
- Named failure mode: tool-selection degradation under large MCP server counts
- Reported from a production multi-server setup (5+ distinct MCP domains)
- The developer built `graph-tool-call` as a graph-based tool routing intermediary to address it
- Same-day pair with Mu (2026-08-03): Mu solves the problem by aggregating into one endpoint; graph-tool-call solves it by routing at the harness level — two distinct mitigations for the same root cause

## Why clawfit should care
The org_fit field `setup_complexity` does not currently capture the compounding effect of adding multiple MCP servers. An org that installs 5 MCP servers may see worse tool performance than one with 2, even if each server individually is "low" complexity. This is the first documented quantitative threshold signal for MCP tool overload in this corpus. clawfit's current registry treats each MCP tool as independent; this signal argues for a `mcp_server_count` interaction effect in scoring or a harness-level warning threshold.

## Preliminary interpretation
Current best reading:
- **Cross-cutting harness engineering signal** — relevant to L2 (harness) × L4c (MCP tools) interaction layer

## Status
- First signal. No repo (GitHub profile only). Conceptual signal, no registry entry. Schema watch: `mcp_tool_saturation_risk: bool`; threshold appears around 4–6 active MCP servers from this case.
