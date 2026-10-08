# Research Watch: TesterArmy e2e — Agentic E2E Testing Framework with Replay Cache

- Repo: https://github.com/tester-army/e2e
- Source: Launch HN (hn.svelte.dev/item/48586299), October 2026; GitHub Trending
- Company: TesterArmy (YC P26, Warsaw / San Francisco)

## Why this is worth watching
Most AI-driven test frameworks run an agent on every test execution, making test suites expensive and non-deterministic. TesterArmy's e2e framework takes a different approach: after an agent successfully executes a natural-language test step for the first time, the framework **records the exact actions taken and replays them deterministically** on subsequent runs, calling the model only when the app changes. This record-then-replay model makes agentic test authoring cheap (natural language) while making test execution predictable (no model calls in steady state). It is the testing-layer equivalent of a code-generation workflow that writes tests once and then runs them without AI. The framework is pre-1.0 and APIs are still in flux, but the YC P26 backing and the HN "Launch HN" thread confirm this is active and intentional, not a prototype.

## What stands out immediately
- **Record-and-replay model**: agent.act() steps are executed by an AI agent on first run; successful action sequences are recorded; subsequent runs replay without a model call until the app's UI changes
- **Mixed test types in one file**: natural-language agent steps (`agent.act('click sign in button')`) mix with ordinary locators and assertions in the same test file; locator-only tests run without any model involvement
- **Mobile parity**: `@e2e-dev/mobile` engine runs the same tests on iOS simulators and Android emulators; same authoring model across web and mobile
- **AI SDK agnostic**: any AI SDK-compatible model can be configured for the `agent.act` steps; tests are not locked to a specific LLM vendor
- **Apache 2.0 license**: permissive
- **Pre-1.0 stability warning**: documented in the README — APIs and configuration may change in minor versions (as of October 2026)
- **YC P26 company**: TesterArmy is a YC Spring 2026 batch company; founders Oskar Kwaśniewski and Szymon Rybczak (Warsaw / San Francisco)

## Why clawfit should care
clawfit's current scoring model does not include a testing or evaluation axis. TesterArmy e2e is specifically an agent-side testing tool: it uses AI agents to *test* applications, not to build them. This falls squarely in L5 (evaluation/observability) but targets a different population than existing L5 entries in the research-watch corpus — it serves teams shipping products where AI agents are QA testers, not developers. The record-and-replay cost model is also a direct input to clawfit's `budget` dimension for teams running agent-driven QA at scale: marginal cost per test run drops to zero in steady state (no model calls on replay). The mobile parity also opens a hardware axis: agent-driven E2E testing on simulators is a new hardware deployment scenario not in the current registry.

## Preliminary interpretation
- **L5 — Evaluation / Observability** (primary): agents execute and validate application behavior as a test oracle
- **L6 — Human Interface** (secondary): test authoring is a natural-language human-facing workflow; agent-driven interaction targets web and mobile UIs

## Claims to verify
- Replay fidelity under UI changes: the framework must detect when the app's UI has changed and re-execute the agent step; the detection mechanism and false-negative rate are not specified in available documentation
- Star count: not publicly confirmed in sources consulted; the GitHub repo should be checked directly before assigning significance
- AI SDK compatibility scope: "any AI SDK-compatible model" is a broad claim; it likely means any model exposed through the Vercel AI SDK; models outside that ecosystem may require adapters
- Mobile test stability: iOS and Android simulation environments are notoriously fragile for deterministic replay; failure modes under simulator state drift are not documented

## Status
- Pre-1.0 (APIs unstable), October 2026
- YC P26 backed; active development; star count not confirmed (below 100-star threshold or close to threshold)
- Exception note: YC-batch status and HN Launch HN thread establish legitimacy despite unconfirmed star count; framework addresses a taxonomy gap (agent-driven E2E testing as L5)
- **First dedicated signal for "agentic E2E testing with record-and-replay cost optimization"** in clawfit's research-watch corpus
- Monitor: v1.0 release, star growth, replay detection algorithm documentation, independent benchmarks vs. Playwright/Cypress with AI add-ons
