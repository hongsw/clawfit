# Research Watch: Pi (earendil-works) — Minimal-Core Extensible Coding Agent Toolkit

- Repo: https://github.com/earendil-works/pi
- Also see: https://pi.dev/ (product site + docs); https://pi.dev/news/2026/5/7/pi-has-a-new-home (org migration announcement); https://github.com/earendil-works/gondolin (microVM sandbox companion); https://github.com/badlogic/pi-mono (prior home, tracked in docs/research-watch/2026-04-07-pi-mono-fullstack-agent-toolkit.md)

## Why this is worth watching

`earendil-works/pi` is the same project previously tracked as `badlogic/pi-mono` — it migrated from Mario Zechner's personal GitHub org to Earendil Inc. on 2026-04-08 and published its first release under the `@earendil-works` npm scope at v0.74.0 on 2026-05-07. The org transfer did not change the development direction but it is a governance event worth flagging: an open-source coding agent CLI with 46.5k stars and 2,143 community packages has now passed from a solo-maintainer structure to a company. That changes the continuity and commercialization risk profile relative to the April 2026 read. The "minimal-core + TypeScript extensions" architecture, which deliberately excludes MCP, sub-agents, and plan mode from the base runtime, is now confirmed as a design policy under institutional ownership rather than a solo developer's preference — and the 2,143 community packages number (up from an untracked baseline in the April doc) signals that the extension ecosystem is growing faster than the core.

## What stands out immediately

- **46.5k stars, 5.5k forks, 214 releases, v0.74.0 on 2026-05-07.** TypeScript 96.5%. All figures from GitHub as of 2026-05-09. This is the highest-star L1 coding agent CLI tracked in this taxonomy except Warp (which is primarily L6+L2) — well above Claude Code (not public), aider (~21k), and Ruflo (38.8k, L2 primary).
- **Confirmed repo identity.** `earendil-works/pi` is `badlogic/pi-mono` after org migration. Old `@mariozechner/*` npm packages deprecated with redirects; `@earendil-works/pi-coding-agent` is the current install path. The CHANGELOG confirms v0.73.1 was the last release under the old scope. The April 2026 research-watch document for pi-mono should be read in conjunction with this entry.
- **Package surface unchanged from April baseline.** Five packages confirmed: `pi-coding-agent` (interactive CLI), `pi-agent-core` (runtime, tool calling, state), `pi-ai` (multi-provider LLM API: Anthropic, OpenAI, Google, 30+ providers including DeepSeek, Azure, Chinese providers), `pi-tui` (differential-render TUI library), `pi-web-ui` (web components). `pi-mom` (Slack bot) and `pi-pods` (vLLM pod management) are referenced in prior tracking but not surfaced in current README or docs — status unclear after migration.
- **"Minimal-core by policy" is now an explicit design statement.** The README and docs confirm pi deliberately excludes: built-in MCP, sub-agents, plan mode, permission popups, to-do lists, background bash. These are all "add via extensions if you want them." This is a stronger architectural claim than most coding agent CLIs make — it positions pi as a runtime kernel, not a feature bundle. It is the opposite of Ruflo's "210 tools included" approach.
- **Four operational modes: interactive, print/JSON, RPC (stdin/stdout JSONL), SDK (Node.js embed).** The RPC and SDK modes are atypical for a coding agent CLI — they position pi as an embeddable agent runtime that other TypeScript services can wrap. This expands the L1 classification toward L1/L2 boundary.
- **Extension system is the load-bearing architectural component.** TypeScript extensions add tools, commands, shortcuts, event hooks, custom editors, UI components. Skills follow the "Agent Skills standard" (markdown-based, `/skill:name` invocation). Pi packages bundle extensions + skills + prompts + themes and distribute via npm or git. The 2,143 community packages figure is the clearest evidence that the extension model is working at scale.
- **MCP excluded from core, implementable via extension (claim to inspect).** The documentation states MCP is not built in but can be added through extensions. An MCP server extension is listed as an example use case. This is architecturally different from tools that ship MCP as a core transport: pi's MCP support is opt-in at the extension layer rather than mandated at the runtime layer. Independence from MCP as a core dependency is a deliberate positioning against Claude Code and Ruflo.
- **Gondolin as companion sandbox.** A separate `earendil-works/gondolin` repo provides QEMU microVM isolation for pi tool execution. A dedicated pi+gondolin extension mounts the workspace at `/workspace` inside the VM. This is the L7-adjacent infrastructure layer that pi itself does not own — it delegates sandboxing to an independent system rather than shipping a sandbox. The TypeScript control plane in gondolin handles egress policy (HTTP/TLS allowlists, secret injection).
- **Real-world session data collection as a training flywheel.** The README actively solicits users to share OSS coding session data: "Public OSS session data helps improve coding agents with real-world tasks, tool use, failures, and fixes instead of toy benchmarks." This is a training-data flywheel play under Earendil Inc. — the community packages and session data create a competitive moat that pure-OSS forks cannot easily replicate post-migration.
- **AGENTS.md present in repo.** Consistent with Flue (2026-05-03 signal) and other governance-layer actors that are adopting AGENTS.md as a behavior specification artifact. pi's AGENTS.md targets contributors (human and AI), not end-user governance — different use of the same artifact type.
- **No benchmark claims found in current README or docs.** No SWE-Bench, HumanEval, or custom benchmark cited anywhere in the current pi.dev documentation or GitHub README. Contrast with Ruflo's 84.8% SWE-Bench Verified claim (unverified in primary docs). Pi's value proposition is architecture and extensibility, not benchmark score.

## Why clawfit should care

The org migration makes the April 2026 pi-mono entry structurally incomplete: the star count has grown (from 32.6k in April to 46.5k today), npm scope has changed, and the governance structure has shifted from solo to institutional. A clawfit recommendation engine that references `badlogic/pi-mono` in any registry entry now needs to update the canonical URL and scope coordinates.

The more substantive implication is architectural. Pi's "minimal-core by policy" design — deliberate exclusion of MCP, sub-agents, and plan mode from the base runtime — creates a clean L1 reference point that is missing from the current registry. The existing L1 entries are either model-specific (DeepSeek-TUI), framework-dependent (Ruflo requires Claude Code), or general-but-undifferentiated (aider, jcode). Pi is the only tracked L1 tool with both (a) 40k+ stars and active institutional backing, and (b) an explicit architectural philosophy about what belongs in a base runtime vs. what belongs in extension layers. That philosophy maps directly onto clawfit's recommendation model: a profile asking for `statefulness: stateless` + `latency: low` would benefit from understanding whether a tool's features are in-core (always loaded) or in-extension (opt-in overhead).

The four operational modes (interactive, print, RPC, SDK) also introduce a dimension the current clawfit filter schema does not model: embedding mode vs. interactive mode. A `task: code-gen` profile that wants to embed pi as a library inside another service is a different profile than one that wants a terminal CLI. The RPC/SDK modes push pi toward the L1/L2 boundary in a way that the interactive CLI framing obscures.

The Gondolin companion is a concrete L7 signal that the earendil-works org is deliberately layering infrastructure below pi rather than bundling it — a modular architecture decision worth watching as a counter-pattern to Ruflo's monolithic surface.

## Comparison to closest tracked neighbors

| Axis | Pi (earendil-works) | Ruflo (L2 primary) | Claude Code (L1) | aider (L1) |
|------|---------------------|--------------------|------------------|------------|
| Stars | 46.5k | 38.8k | private | ~21k |
| Core philosophy | Minimal kernel + extensions | Batteries-included swarm | Anthropic-opinionated | Open multi-model |
| MCP | Extension opt-in | 210 tools included | Core transport | Plugin |
| Sub-agents | Extension opt-in | 100+ included | Core | Not native |
| Operational modes | Interactive, print, RPC, SDK | CLI + web UI | CLI + IDE | CLI |
| Governance | Earendil Inc. (since Apr 2026) | ruvnet (solo + community) | Anthropic | aider-chat org |
| Primary clawfit level | L1 (with L2 secondary via SDK/RPC) | L2 primary | L1 | L1 |
| Benchmark claims | None cited | 84.8% SWE-Bench (unverified in primary docs) | Not public | Published |

## Preliminary interpretation

Current best reading:

- **Level 1 — Base runtimes / primary agent surfaces (primary):** Pi is a coding agent CLI and embeddable agent runtime. The interactive mode, print/JSON mode, and four-mode surface are all L1 characteristics. The 30+ LLM provider support and the multi-provider pi-ai abstraction layer reinforce L1 as the primary anchor — this is a runtime that can surface any model to a user or downstream system.
- **Level 2 — Meta wrappers / harnesses / orchestration layers (secondary):** The RPC and SDK modes position pi as an embeddable runtime that other services can wrap. A TypeScript service calling pi via SDK is using it as a harness, not a base agent. The extension system's ability to add sub-agents and plan mode (via third-party packages) further blurs the L1/L2 boundary. The secondary L2 classification reflects capability, not the dominant use pattern.
- **Not L3:** AGENTS.md is present but serves contributor guidelines, not executable SSOT governance. No evidence of policy-enforcement-at-runtime.
- **Not L4:** MCP and tools are extension-layer concerns, not core capabilities. Extension system is L4-adjacent but pi itself is not a capability/skill/plugin provider — it is the host that consumes them.
- **Not L5:** No memory substrate in core. Session branching and compaction are conversation-management features, not a persistent memory layer.

The Gondolin companion is classified separately as **L7 — Infrastructure / hardware / edge layer** (microVM execution sandbox with TypeScript control plane). It is not pi, but it is the earendil-works org's answer to the sandboxing problem, and clawfit should track both together.

## Status

- Existing tracking entry (`badlogic/pi-mono`, 2026-04-07) superseded by this entry. The canonical repo URL is now `earendil-works/pi`; npm scope is `@earendil-works`. **Classified L1 primary** (base runtime + multi-provider agent surface) with **weak L2 secondary** (RPC/SDK embed modes make it a harness substrate for other services). At 46.5k stars MIT-licensed with institutional backing and 214 releases, this exceeds the registry promotion threshold. Registry entry update recommended: change repo URL and npm scope in any existing agents.json entry referencing the old `badlogic/pi-mono` coordinates. No `docs/reference-levels.md` modification today — the L1 sub-type "minimal-core extensible agent runtime" is strong enough to merit a named sub-type entry but should wait for one independent benchmark or deployment case study before promotion. Flag for re-evaluation after Earendil Inc. publishes a public roadmap or the extension count crosses 3,000.
