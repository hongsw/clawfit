# Research Watch: getpaseo/paseo — Mobile-First Multi-Agent Orchestration Shell

- Repo: https://github.com/getpaseo/paseo (⭐12,800)
- Source: GeekNews (2026-08-08, 4 pts), GitHub Python Trending #19
- License: AGPL-3.0
- Language: TypeScript
- Created: October 2025

## Why this is worth watching

paseo occupies a distinct niche from stablyai/orca (tracked 2026-06-25, 40k stars) even though both carry the "ADE" tag. Orca is a deep worktree-isolated parallel agent environment with IDE-grade tooling built around desktop execution. paseo's architectural center of gravity is a **mobile-first remote control layer**: a local daemon on the user's machine communicates over an end-to-end encrypted relay to native iOS, Android, and Electron clients. The phone is a first-class control surface, not an afterthought. Three agent-to-agent delegation primitives — `/paseo-handoff`, `/paseo-loop`, and committee/advisor mode — are absent from orca's model entirely.

At 12,800 stars, created October 2025, and still receiving commits on the day of this scan, paseo is actively growing in the ADE space without being a direct orca substitute.

## What stands out immediately

- **E2E encrypted relay**: agent execution always stays on the user's own hardware; the relay transports control messages, not code or credentials — specifically addresses enterprise data residency concerns
- **`/paseo-handoff` skill**: agent-to-agent work transfer primitive invocable from the mobile app or CLI; no equivalent in orca
- **Committee mode**: multiple models analyze the same problem in parallel and produce a synthesized output; differentiates from simple round-robin or sequential agent routing
- **Advisor mode**: one model consults a second model before responding — explicit consultation hierarchy without a full orchestrator
- **`/paseo-loop` skill**: retry/polling loop run by one agent on behalf of another; enables background delegation from mobile
- **Voice control**: local-first speech interface on desktop client — distinct from Cortex/MSFT enterprise voice agents; no cloud STT dependency stated
- **Agent support breadth**: Claude Code, Codex, GitHub Copilot, OpenCode, Pi, Hermes as explicit harness targets — broader than orca's default
- **No forced authentication or telemetry**: explicit privacy stance in README; contrast with cloud-first orchestration platforms

## Why clawfit should care

paseo introduces **mobile-triggered agent delegation** as a first-class pattern. The existing registry has no category for "cross-device agent control" — all current entries assume a developer is seated at a terminal. A `deployment_surface: mobile-companion` axis (distinct from `web-ui` and `terminal`) would capture this emerging niche.

The committee and advisor modes also represent structured multi-agent topologies not modeled in current `agents.json`. Current multi-agent entries (Crystal, Claude Squad, swarm-forge) model parallel isolation or sequential handoff; paseo's committee mode models **synchronous parallel deliberation with a synthesis step** — a different coordination pattern.

**AGPL-3.0 license** is a meaningful constraint for commercial use — commercial users at `governance_need: hard` profiles that require proprietary deployment would face licensing review. This is not modeled in the current `agents.json` schema.

## Preliminary interpretation

- **Level 3 — Team Workflows** (primary): daemon-managed multi-agent orchestration, handoff/loop/committee/advisor delegation primitives — workflow coordination is the differentiated value
- **Level 6 — Human Interface** (secondary): cross-device control surface (iOS, Android, Electron, CLI, Docker) with E2E relay — the interface layer is architecturally significant but secondary to the orchestration primitives
- **Cross-watch**: stablyai/orca (2026-06-25, L2/L3 ADE — more feature-complete on desktop, less mobile-first); qm (2026-08-01, L2 team harness — governance postures but no mobile delegation); unclebob/swarm-forge (2026-08-08, L2 tmux-based swarm — role-separated coordination but no cross-device model)

## Claims to verify

- **Relay security model**: E2E encryption claim needs independent verification — what key exchange mechanism, who holds key material, what happens if relay provider is compromised
- **Committee synthesis quality**: whether the multi-model committee synthesis step produces coherent output rather than lowest-common-denominator summaries
- **AGPL-3.0 commercial implications**: verify whether the "public network use" clause triggers copyleft for enterprise internal deployments — if so, this limits commercial adoption significantly
- **Mobile feature parity**: iOS/Android described as native Expo apps; verify that handoff/committee/advisor primitives are actually usable from mobile, not only from desktop Electron
- **12,800 stars trajectory**: growing from October 2025 to 12.8k — verify organic vs. coordinated growth pattern; commit velocity and fork ratio are relevant signals

## Status

- Active; last commit on day of scan (2026-08-08)
- 12,800 stars well above research-watch threshold; AGPL-3.0 limits direct registry use for `governance_need: hard` profiles
- Registry eligibility: borderline — needs `tasks` mapping and deterministic cost/latency data; mobile harness type absent from schema; AGPL consideration
- Schema watch: `deployment_surface: mobile-companion`; `license_copyleft: bool`; `agent_topology: [sequential | parallel-isolated | committee | advisor]`
- Cross-reference: stablyai/orca (2026-06-25), qm (2026-08-01), unclebob/swarm-forge (2026-08-08)
