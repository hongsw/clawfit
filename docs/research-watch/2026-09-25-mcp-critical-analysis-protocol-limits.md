# Research Watch: MCP Critical Analysis — Protocol Limits Signal

- Repo/Link: https://maharship.com/blog/why-mcp-was-always-a-bad-idea/
- Source: GeekNews (front page)

## Why this is worth watching
A GeekNews-front-page essay arguing "MCP was always a bad idea" is a leading indicator of MCP ecosystem fatigue. When critical analysis surfaces on Korean tech news, it reflects accumulated practitioner pain — not just early-adopter hype. This follows months of MCP server proliferation and mirrors the pattern seen with REST → GraphQL criticism.

## What stands out immediately
- Argues MCP over-specifies the transport layer while under-specifying semantics
- Claims per-server auth and session management create combinatorial friction at scale
- Points to treg-style routing abstractions as evidence the base protocol is leaking
- Raises security concerns about untrusted tool exposure in shared registries

## Why clawfit should care
clawfit uses `network` and `setup_complexity` fields heavily in scoring. If MCP adoption fragments into competing routing layers (treg, MetaMCP, MCPJungle), the effective complexity of "online" tools may be rising — warranting a scoring adjustment that slightly penalizes pure-MCP tools for non-developer personas. This also reinforces the governance_need dimension for enterprise profiles.

## Preliminary interpretation
Current best reading:
- **Ecosystem signal — Level 3 (MCP Protocol Layer) counter-pressure**

## Status
- Counter-signal to MCP adoption — watch for ecosystem fragmentation vs consolidation
