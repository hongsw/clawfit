# Research Watch: vercel-labs/zero (ZeroLang)

- Repo: https://github.com/vercel-labs/zero
- Also see: https://techstrong.ai/features/vercel-labs-builds-a-programming-language-designed-for-ai-agents/ · https://www.marktechpost.com/2026/05/17/vercel-labs-introduces-zero-a-systems-programming-language-designed-so-ai-agents-can-read-repair-and-ship-native-programs/

## Why this is worth watching

Zero is not an agent, harness, or capability pack — it is a programming language whose design center is "agent as primary user." The compiler emits structured JSON diagnostics with stable error codes and typed repair IDs by default; fix plans are exposed via `zero fix --plan --json`, not as human-readable prose. This is a paradigm-level signal: if agent-driven code generation matures to the point where the target language is chosen partly on the basis of how well the compiler speaks to agents, it reshapes which substrate choices belong in the L1/L7 scoring model.

## What stands out immediately

- Compiler output is JSON-first, not an opt-in flag: stable error codes (`NAM003`), typed repair identifiers (`declare-missing-symbol`), and dependency graph facts are default, not addon
- Capability-based I/O: functions must explicitly accept a `World` parameter to perform side effects — capabilities are declared in the type signature, not inferred; this makes agent-generated code auditable at the type level
- Single CLI binary with consistent `--json` flags across all subcommands — entire toolchain surface is homogeneous for programmatic consumption
- Compiles to sub-10 KiB native binaries; C (73.5%) implementation; token efficiency and zero-dependency runtime are design priorities alongside the agent-facing interface
- Apache-2.0 license — no commercial adoption friction
- 4.4k stars, pre-1.0, breaking changes expected, known vulnerabilities; repo itself warns it should only run in safe environments
- Source files use `.0` extension; "skills system" bundles language rules — terminology overlap with L4b skill packs is coincidental, not structural

## Why clawfit should care

Zero does not enter clawfit's registry by current schema — it is not an agent, LLM, or hardware option. The relevance is architectural: Zero is evidence that the toolchain layer below L1 is being redesigned around agent consumers. If this pattern spreads (a second language or compiler that adopts JSON-first structured repair output as a design primitive, not a debug flag), clawfit's L7 infrastructure axis will need to distinguish between "substrate that agents execute on" and "substrate that agents compile to." The `task: code-gen` scoring path implicitly assumes the target language is human-designed; Zero challenges that assumption. The capability declaration pattern (`World` parameter, `!` fallibility marker) is also a structural analog to what L3 behavioral specs try to achieve via CLAUDE.md — but expressed in the type system rather than in a markdown prompt.

## Preliminary interpretation

Current best reading:
- **Level 7 — Infrastructure / hardware / edge layer** (primary): Zero is a language runtime substrate, not an agent or harness. It operates below L1 — it is what agents compile programs *into*, not what runs the agent. This places it in the infrastructure axis, alongside inference runtimes and edge execution substrates, rather than inside the agent or capability layers.
- Cross-cutting paradigm signal: the "compiler-as-agent-interface" design pattern is new to this taxonomy and does not fit cleanly inside any single layer. It is closer in kind to the 12-Factor Agents principles doc (a framework-level signal tracked as L3 reference) than to any runtime or harness entry. If a second language or compiler adopts JSON-first agent-facing diagnostics as a primary design goal, a new sub-axis note under L7 (or the `inference-runtime-substrate.md` companion) would be warranted.

## Status

- 4.4k stars, Apache-2.0, pre-1.0; below the 5k registry threshold and categorically outside current registry schema (not an agent, LLM, or hardware option). Not a registry candidate. Track as a paradigm signal: the "agent-native compiler interface" pattern is single-signal; promotion to a named sub-axis in L7 or the infrastructure companion note requires a second independent compiler/language adopting this design philosophy. Revisit if star velocity crosses 5k or if a second agent-native language surface appears.
