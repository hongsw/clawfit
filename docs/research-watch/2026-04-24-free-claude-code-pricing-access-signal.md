# Research Watch: free-claude-code — Pricing Pressure Signal for Claude Code Access

- Repo/Link: https://github.com/Alishahryar1/free-claude-code
- Source: GitHub Trending (2026-04-24, #7, +1,962 today — highest daily velocity on trending list)

## Why this is worth watching
`free-claude-code` (5,544★, +1,962 today) provides Claude Code access "for free in the terminal, VSCode extension or via discord." Its extraordinary daily velocity (+1,962 — highest on today's trending list) is a direct response to Anthropic removing Claude Code from the $20/month Pro tier (tracked 2026-04-22). The demand signal reveals how pricing changes cascade into community workarounds.

## What stands out immediately
- +1,962 stars in one day — exceptional velocity, likely driven by the Pro-tier removal (2026-04-22)
- Provides free Claude Code access in terminal, VS Code, and Discord
- Python; may use alternative API routing, shared tokens, or open-weight model substitutes
- Raises Anthropic ToS questions — status of compliance unknown

## Why clawfit should care
- **Pricing pressure → harness fragmentation:** When Anthropic raised the pricing floor, the community created a free alternative within 48 hours. This is a leading indicator of user sensitivity to `pricing_tier: paid` in solo/small profiles.
- clawfit's `claude_code` registry entry now shows `pricing_tier: paid` (corrected 2026-04-22). The velocity of `free-claude-code` validates that the pricing tier metadata is now a material selection signal, not just metadata.
- If compliance is uncertain, this tool represents a `data_sensitivity` risk: routing through third-party APIs leaks user code.
- Monitor for ToS enforcement action — if it's removed, the velocity signal is even more telling about demand for affordable agent access.

## Preliminary interpretation
Current best reading:
- **Pricing / access signal** (not a product to add to registry; context signal about demand elasticity for affordable AI coding agent access)

## Status
- Tracking velocity only; not adding to registry pending ToS clarification
