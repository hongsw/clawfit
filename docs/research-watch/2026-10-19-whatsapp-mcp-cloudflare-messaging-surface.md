# Research Watch: finereli/whatsapp-mcp — WhatsApp MCP on Cloudflare Workers

- Repo/Link: https://github.com/finereli/whatsapp-mcp
- Source: Hacker News Show HN (25 points)

## Why this is worth watching
Demonstrates MCP servers running serverlessly on Cloudflare Workers with no infrastructure cost, exposing WhatsApp as an agent-accessible communication surface. The pattern (free serverless MCP host + consumer messaging API) is easily replicated for Telegram, Signal, SMS, etc.

## What stands out immediately
- Cloudflare Workers as zero-cost MCP hosting — lowers barrier to custom MCP surfaces
- WhatsApp Business Cloud API integration shows agents reaching non-developer end-users
- Low HN points (25) but the architectural pattern matters more than this specific instance

## Why clawfit should care
MCP surface expansion into messaging platforms is a clawfit Level 5 signal. It indicates agents acting asynchronously through non-IDE surfaces, which affects `output_destination` and `network` dimensions in org_fit scoring. Organizations with customer-facing use cases could weigh this highly.

## Preliminary interpretation
Current best reading:
- **Level 5 — MCP / Tool Ecosystem** (new MCP surface: consumer messaging via serverless host)

## Status
- Tracking: early signal; watch for pattern spread to other messaging platforms
