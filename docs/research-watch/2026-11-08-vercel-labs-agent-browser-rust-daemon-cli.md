# Research Watch: vercel-labs/agent-browser — Rust Daemon Browser CLI for Agents

- Repo: https://github.com/vercel-labs/agent-browser (⭐47,420)
- Source: GitHub Trending (all languages, daily, 2026-11-08)

## Why this is worth watching
vercel-labs has shipped a Rust CLI that exposes browser control as a series of composable shell commands driven by a background daemon. With 47,420 stars and 812 added today, it is tracking at the same velocity as agent-desktop (also from vercel-labs, tracked 2026-11-02), which suggests Vercel is systematically occupying the entire L2 control-plane layer — desktop, browser, and skills. The daemon-per-session architecture is a concrete design answer to the "one browser per agent" isolation problem that neither Lightpanda nor Obscura addressed architecturally.

## What stands out immediately
- Written in Rust; persistent background daemon holds the browser open between commands so each agent step is a one-line shell invocation, not a new browser launch
- Returns element refs (e.g., `@e1`) from an accessibility-tree snapshot; the agent acts on a ref, re-snapshots, and loops — no HTML parsing required
- Fails loudly on hidden, disabled, off-screen, or covered elements rather than silently reporting false success; a rare honesty-first design choice
- `agent-browser mcp` starts a stdio MCP server, making the daemon directly composable with any MCP-aware harness
- `agent-browser skills get core` pulls versioned skill packs tied to the installed CLI version — same skills-as-versioned-packages pattern as vercel-labs/skills and anthropics/skills
- Pluggable browser backends: Chrome for Testing (default), attaching to a running Chrome instance, Lightpanda, Obscura, iOS Simulator, and several cloud browser providers — each already tracked in clawfit's ecosystem map
- `--session` flag gives each logical agent its own isolated daemon and browser; default 1-hour idle timeout

## Why clawfit should care
agent-browser is the browser control layer of what is becoming a vercel-labs control-plane trilogy: agent-desktop (accessibility-tree computer-use, 2026-11-02), agent-browser (accessibility-tree browser control, 2026-11-08), and vercel-labs/skills (capability layer, 2026-04-23). Together they cover three of the four surfaces an agent touches (desktop, browser, capabilities; the fourth — files — was addressed by vercel-eve, 2026-10-11). A clawfit recommendation for browser-automation or QA tasks may need to surface the vercel-labs stack as a coherent option, not just individual tools. The MCP server also makes it directly combinable with any clawfit-recommended harness.

## Preliminary interpretation
Current best reading:
- **Level 2 — Harness / Wrapper Layer** (primary) — browser control exposed as a CLI tool and daemon a harness plugs in to
- **Level 4 — Capabilities / Skills / MCP** (secondary) — exposes a stdio MCP server and versioned skill packs

## Claims to verify
- Star count accuracy: 47,420 at time of scan; trending velocity may reflect a recent announcement
- Whether the MCP tool set is complete enough to replace direct page manipulation or only supplements it
- iOS Simulator backend maturity — mentioned in README but not described further
- Whether session isolation (one daemon per session) holds under concurrent agent execution

## Status
- New signal — tracking; registry action deferred (browser automation CLI, no cost/latency data for scoring; eligible for harness registry category when that schema is added)
