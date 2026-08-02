# Research Watch: tradingview-mcp — Zero-Credential Financial Market Data MCP Server

- Repo: https://github.com/atilaahmettaner/tradingview-mcp (⭐3,756)
- Source: GitHub Trending Python (2026-08-02, +11 stars today); first trending appearance

## Why this is worth watching

tradingview-mcp is a self-hostable MCP server exposing 37 financial market data tools — price feeds, technical analysis, screeners, backtesting, and sentiment — to any MCP-compatible agent client without requiring credentials or a TradingView account. The zero-authentication design is the structural distinction: financial market data has historically required Bloomberg/Refinitiv subscriptions ($20,000+/year) or at minimum paid API keys. tradingview-mcp bypasses that tier entirely for agents.

This is the second signal for the "live-data-connector MCP server" pattern, after SurfSense (2026-07-25) which established the sub-type by exposing 10+ social/web scrapers as native MCP tools. tradingview-mcp applies the same architectural approach — same data source serves both agent tool calls and human-facing interfaces — but in the financial domain specifically. The pattern now has two confirmed instances across different data domains (web/social → financial).

## What stands out immediately

- **37 MCP tools across six groups:** backtesting (3 tools including walk-forward validation), price/market (3), technical analysis (8+), sentiment/news (3), screeners (6+), exchange-specific tools — a breadth that would require multiple paid subscriptions to replicate via traditional data APIs
- **No credentials required:** tools operate without TradingView login, Refinitiv, Bloomberg, or brokerage API keys; managed hosted tier at $9–29/month is optional
- **Emerging-market exchange coverage:** EGX (Egypt) and BIST (Turkey) screeners are included — financial data for these markets is substantially harder to source via standard data APIs than US equities
- **Walk-forward overfitting detection in backtesting:** the `walk_forward_backtest_strategy` tool exposes Sharpe and Calmar ratio metrics and flags overfitting — more rigorous than simple backtesting; agent-callable quantitative finance at this depth is unusual
- **Reddit + RSS sentiment feeds merged into `combined_analysis`:** multi-source sentiment aggregation available as a single tool call; agents can retrieve sentiment without orchestrating multiple scrapes
- **Async/parallel execution architecture:** relevant for market data which has inherently higher latency than code operations; agent tool-call reliability depends on this
- **OpenClaw integration for delivery:** Telegram/WhatsApp/Discord channel delivery — positions this as a notification/monitoring pipeline tool for agent-generated trading signals, not just a data retrieval layer

## Why clawfit should care

SurfSense (2026-07-25) was tracked as "first signal for live-data-connector MCP server" sub-type. tradingview-mcp is the second signal, in a different domain (financial vs. social/web), with the same core architecture: a single self-hostable server that exposes domain-specific live data as MCP tools. The pattern is: **domain-specific live data → MCP tool surface → any agent can call it without building the connector layer**.

For clawfit specifically, two implications:

1. **`task: research` profiles with `network: online` now have a financial-domain MCP option.** Current `agents.json` entries tagged `task: research` assume general-purpose web research (SurfSense, Agent-Reach). A financial research agent profile (hedge fund analyst, personal finance tracker, automated reporting) cannot be matched to an appropriate MCP connector without this data. tradingview-mcp is a first candidate for a financial-data capability annotation.

2. **The "live-data-connector MCP" pattern is forming a cluster.** Two instances across two domains in 8 days (SurfSense July 25, tradingview-mcp August 2) suggests this is a repeating pattern in L4 tooling. A third instance would confirm a canonical sub-type: `mcp_server_role: live-data-connector`.

## Preliminary interpretation

- **Level 4 — Capabilities/MCP (financial domain live-data connector):** pure tool-server, no runtime or orchestration logic; gives any MCP-compatible agent access to financial market intelligence without credential management
- Secondary: very weak L5 signal (walk-forward backtesting with quality metrics reads as evaluation infrastructure for trading strategies)

## Claims to verify

- **"Real-time" data claim:** many free/scrape-based financial data sources have 15–20 minute delays; TradingView's free data layer often has similar constraints; verify whether tools return live or delayed prices
- **TradingView ToS compliance:** accessing TradingView data without authentication may violate their Terms of Service; a ToS challenge from TradingView would break the zero-credential value proposition entirely
- **37 tools count:** repo is under active development with no formal release tags; current tool count may have changed
- **EGX/BIST data quality:** regional exchange data coverage should be verified for accuracy; smaller exchanges have more variable data quality even from official sources
- **OpenClaw integration:** identify whether OpenClaw is a separate project (potential supply-chain dependency risk) or internal tooling

## Status

- Second signal for "live-data-connector MCP server" pattern (first: SurfSense 2026-07-25, web/social domain); cross-day — two-signal rule met for pattern watch, not yet for canonical section
- No registry entry: 3.7k stars below 5k threshold; per-token cost/latency data not deterministic for an MCP connector
- Schema watch: `mcp_data_domain: [general-web | social | financial | scientific | office]` (extension of `mcp_data_connectors` gap flagged 2026-07-25 for SurfSense); `live_data_auth: [none | api-key | subscription]`
- Cross-watch: SurfSense (2026-07-25, L4c live-data connector, web/social domain) for same-pattern second signal
