# Research Watch: phone-harness — Agent-Controlled Phone via MCP and adb

- Repo: https://github.com/phone-harness/phone-harness (⭐5,108)
- Source: GitHub Trending (Python, daily)

## Why this is worth watching

phone-harness lets a coding agent (Claude Code, Codex CLI, or any MCP-compatible host) operate a real physical phone — tapping, scrolling, typing, and reading the screen — without a jailbreak and without installing anything on the device. The 5,108-star traction on a tool with only 148 commits suggests the community perceives a genuine gap: agents can already operate desktop browsers and local filesystems, but phone interaction has remained a manual step or required expensive managed-device providers. phone-harness bridges that by treating the phone as an MCP endpoint or a CLI-accessible interface. The architectural pattern (a shared helper layer abstracting iPhone Mirroring, Android adb, and cloud phone APIs) is the notable contribution, not any single platform binding.

## What stands out immediately

- **Platform-unified helper layer**: a single `phone_harness/helpers.py` provides consistent screen capture, OCR, and input primitives across iPhone (Mirroring window + Apple Vision OCR), Android (adb USB/Wi-Fi), and cloud phones (hosted adb or HTTPS API); a script written for one platform runs on others with minimal changes
- **No jailbreak, nothing on device**: iPhone control uses the macOS iPhone Mirroring window as the interaction surface; Android uses adb, which requires USB debugging or Wi-Fi adb, both standard developer modes; there is no requirement to modify the phone's OS or install agent software on it
- **MCP endpoint for cloud phones**: cloud phone variants expose an MCP server interface, allowing any MCP-host agent to call phone operations as tools — the agent sees `tap`, `scroll`, `type`, `screenshot` as first-class tools in its tool list
- **CLI interface with doctor/cloud/config subcommands**: the `phone-harness doctor` command checks prerequisites before first use — a sign the project anticipates non-expert users
- **Plugin integrations**: explicit support for Hermes Agent and OpenClaw; these are niche but confirm the project is tracking the emerging MCP-host ecosystem rather than targeting only Claude Code
- **Agent workspace**: the agent's helper scripts persist in `~/.phone-harness/agent-workspace` — the project design anticipates multi-session, stateful agent use rather than one-shot demos
- **148 commits, 5,108 stars**: the star-to-commit ratio is unusually high, indicating most stars came quickly after a launch or viral moment rather than incremental community growth

## Why clawfit should care

clawfit's `task` taxonomy currently includes computer-use as a category, but its hardware registry models desktop/server environments, not mobile devices. phone-harness creates a new hardware candidate: a physical or cloud-hosted phone as an execution target for agents. Agents recommended for `task: computer-use` with `hardware: cloud` today may be optimally served by a phone-harness-based setup for mobile-specific tasks (app testing, mobile form filling, SMS-based workflows). The `task` filter may need a `mobile-computer-use` variant, or the hardware registry may need a `phone` or `mobile-device` entry.

The MCP interface is the registration path: if phone-harness's MCP server becomes a standard interface for mobile device access, the "agent + phone-harness MCP" combination becomes a scorable triple alongside the existing (agent, llm, hardware) model.

The governance dimension is non-trivial: a tool that lets an agent send SMS, make purchases, or access authenticator apps on a real phone sits in a different risk tier from tools that operate local filesystems. This is not a reason to exclude it from tracking, but it is a signal that the `governance_need` axis in the registry schema may need a `device-access` tier.

## Preliminary interpretation

Current best reading:
- **Level 6 — Human Interface Layer** (primary): the tool bridges agent capabilities to a physical human-facing device; it operates at the layer where agents interact with real-world interfaces, not just digital file systems
- **Level 4 — Capability/Plugin Layer** (secondary): the MCP server interface means phone operations become callable tools in an agent's capability set — structurally similar to a domain skill pack, but for device I/O rather than domain knowledge

## Claims to verify

- Whether the iPhone Mirroring approach is fragile to macOS or Apple Vision OCR updates — if Apple changes the Mirroring API surface, the iPhone integration breaks; this matters for assessing reliability at the production level
- Whether adb-based Android control is blocked by modern Android security policies (some Android versions restrict adb on non-developer builds) — the README states USB debugging is required, which is a non-trivial setup step for non-developers
- Whether cloud phone providers are free/low-cost or require paid accounts — the architecture distinguishes local (iPhone Mirroring, USB adb) from cloud (HTTPS, hosted adb), but no pricing is stated
- What "Hermes Agent" and "OpenClaw" are — confirming these are real MCP-host projects (not references to the developer's other repos) would validate the claim that phone-harness is integrating into a broader ecosystem
- When the viral moment was — the commit count (148) relative to the star count (5,108) suggests most stars arrived quickly; if the spike was more than 6 months ago and the project has been quiet since, it may be abandoned

## Status

- First scan: 2026-11-19
- Registry action: **deferred** — `phone` or `mobile-device` is not an existing hardware registry category; schema does not currently support device-access hardware types; star count (5,108) meets threshold but no deterministic cost/latency data is available for the mobile-device execution path
- 📡 Note: phone-harness is the first well-starred tool for agent-controlled physical phones; prior signals in mobile device control were limited to managed desktop providers with Android emulation (Maritime, Nov-18) or computer-use frameworks targeting desktops; watch for a second well-starred agent-phone interface tool — that would justify adding a `mobile-device` hardware type and `mobile-computer-use` task variant to the registry schema
- 📡 Note: the `governance_need: device-access` tier is a first signal — agents that can operate a phone's SMS, authenticator, and payment interfaces create a qualitatively different risk profile from agents operating local filesystems or remote cloud APIs; watch for a second tool at this risk tier before adding a canonical governance tier
