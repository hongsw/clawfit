# Research Watch: cc-connect (multi-platform chat bridge)

- Repo: https://github.com/chenhg5/cc-connect
- Also see: https://agentclientprotocol.com/get-started/agents (ACP, referenced as the abstraction surface), https://github.com/osisdie/claude-code-channels (parallel project), https://github.com/op7418/Claude-to-IM-skill (parallel project)
- Source: GitHub Trending Daily Go (~+171 stars/day, 2026-04-30); 6.7k stars, 634 forks at v1.3.2 (Apr 21, 2026)

## Why this is worth watching
The single-platform messaging bridge pattern (cc-telegram, Happy) is consolidating into a multi-platform abstraction. cc-connect bundles 11 chat platforms and 10+ coding agents behind one Go binary with a TOML config and an embedded web admin — i.e. the "messaging bridge" sub-layer is moving from per-project scripts toward a generalized appliance. The trending velocity on GitHub Trending Daily Go (+171/day) suggests this consolidation has real demand, not just maintainer interest.

## What stands out immediately
- **Single Go binary with embedded web UI** (v1.3.0+): no separate runtime, no Docker required, distribution model closer to Tailscale/Caddy than to a bot framework
- **11 chat platforms** out of the box: Feishu/Lark, DingTalk, Slack, Telegram, Discord, WeChat Work, Weibo, LINE, QQ, QQ Bot (Official), Weixin (personal WeChat via ilink long-polling)
- **10+ agents supported** + any ACP-compatible agent: Claude Code, Codex, Cursor Agent, Gemini CLI, Kimi CLI, Qoder CLI, OpenCode, iFlow CLI, Pi, Devin
- **Bridge API** exposes WebSocket + REST so third-party adapters (custom UIs, bots, scripts) can drive cc-connect sessions — bidirectional messaging including tool calls and permission requests
- **Multi-Bot Relay**: bind multiple bots into one group chat (`/bind <project>` / `/bind -<project>`); bots can route messages between each other in a single conversation
- **Centralized config** (`~/.cc-connect/config.toml`): `[[projects]]` blocks bind agent + platform; global provider list with per-project overrides; `[[hooks]]` for lifecycle events (message, session, cron, permission, error)
- **Connection model varies per platform** rather than per credential type: WebSocket (Feishu, DingTalk, Discord, WeChat Work, Weibo, QQ), long-polling (Telegram, Weixin), Socket Mode (Slack), webhook (LINE, WeCom alt) — claim is "no public IP required for most platforms"
- **Strong CN-region coverage**: Feishu, DingTalk, WeChat Work, Weixin, Weibo, QQ — distinct from Western-focused tools (Happy, cc-telegram)
- **31 releases tracked**, monthly cadence, v1.3.2 most recent — sustained development, not a hackathon prototype

## Why clawfit should care
- Reinforces the L7 "messaging bridge" sub-pattern — three independent datapoints (cc-telegram single-platform, Happy mobile-first, cc-connect multi-platform) now exist. This is no longer a one-off; it is a recurring deployment surface that profile recommendations may need to expose.
- The multi-platform consolidation matters for `governance_need: hard` + `team_size: large` profiles where Slack and Teams (or Slack and Feishu in CN/APAC) are both required by IT policy. cc-connect is the open-source counterpart to the Teams BYOA enterprise pattern documented 2026-04-23.
- ACP-as-abstraction is reinforced again here as the agent-side interface (parallel signal: Happy, cc-canary). The L7 bridge layer is hardening around ACP; clawfit's reference map should track ACP itself as a distinct primitive once a third independent ACP citation lands.
- Explicit non-fit for registry: cc-connect is a deployment utility, not an agent or LLM or hardware option. Stays in research-watch and reference map.

## Distinction from cc-telegram (and Happy)
- **cc-telegram**: single-platform (Telegram), single-agent (Claude Code), Rust, mobile-remote-control framing
- **Happy**: mobile client, multi-agent (Claude Code + Codex), iOS/Android first-class, not platform-bridge framing
- **cc-connect**: multi-platform (11) and multi-agent (10+) by design; web admin + Bridge API turn it into an integration hub rather than a personal remote control. Multi-Bot Relay is novel — none of the prior bridges expose bot-to-bot routing in a shared group chat.

## Preliminary interpretation
Current best reading:
- **Level 7 — Human interface / messaging bridge sub-layer** (per docs/reference-levels.md L7)
- Sub-pattern: "multi-platform messaging bridge" — distinct from single-platform bridges (cc-telegram) and from mobile clients (Happy)
- Secondary touchpoint: Level 5/MCP-adjacent via ACP integration, but the agent protocol layer is consumed, not extended

Not a registry candidate — utility tool, schema does not fit `Agent` / `LLM` / `Hardware`.

## Status
- Tracking. Three messaging-bridge datapoints (cc-telegram, Happy, cc-connect) now justify treating the L7 messaging-bridge sub-pattern as a named cell in the reference map; flag for next reference-levels.md edit cycle. ACP citation count is now ~3 across research-watch — approaching threshold for a dedicated ACP signal doc.
