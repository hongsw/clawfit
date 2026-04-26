# Research Watch: Gemini Enterprise Agent Platform

- Repo/Link: https://cloud.google.com/blog/products/ai-machine-learning/introducing-gemini-enterprise-agent-platform
- Source: GeekNews front page (2026-04-26)

## Why this is worth watching
Google Cloud launched the Gemini Enterprise Agent Platform as an evolved evolution of Vertex AI, explicitly designed for enterprise-scale multi-agent systems. It builds on Agent-to-Agent (A2A) protocol and MCP, positioning itself as the enterprise-grade managed orchestration layer for organizations that need governance, audit, and scale guarantees. This is the first named "Enterprise Agent Platform" product from a hyperscaler — distinct from Microsoft's Azure AI Foundry and OpenAI's Managed Agents.

## What stands out immediately
- Enterprise-specific framing: governance, audit, compliance built into agent infrastructure
- A2A + MCP dual-protocol support — signals A2A is being institutionalized alongside MCP
- Extends Vertex AI: existing Google Cloud enterprise customers get agent capabilities via familiar billing/IAM
- Google's second consecutive enterprise agent signal (after TPU v8 "agentic era" branding, 2026-04-23)

## Why clawfit should care
The Gemini Enterprise Agent Platform introduces a new enterprise-segment option for `team_size: large` + `governance_need: hard` profiles that already use Google Cloud. It competes with Claude Code Routines (Anthropic managed), openai-agents-python (OpenAI), and Anthropic Managed Agents on the managed-cloud-agent axis. If Google Cloud IAM/billing integration is tight, this becomes a strong recommendation for existing GCP-locked enterprises — a constraint clawfit's model doesn't currently capture. Register as an early signal; revisit when public pricing and feature docs stabilize.

## Preliminary interpretation
Current best reading:
- **Level 2 — Meta wrappers / harnesses / orchestration layers** (managed-cloud sub-type, enterprise variant)

## Status
- Early signal; tracking pending public documentation stability; no registry entry yet
