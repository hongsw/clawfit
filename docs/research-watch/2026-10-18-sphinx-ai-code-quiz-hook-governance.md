# Research Watch: Sphinx — AI Code Verification Hook as Developer Governance Primitive

- Repo/Link: https://sphinx-six-theta.vercel.app/ (Show HN)
- Source: Hacker News front page (217pts, 73 comments, 2026-10-18)
- Stars: unconfirmed (Show HN launch)

## Why this is worth watching

Sphinx is a Git pre-push hook that pauses to quiz the developer on AI-generated code before it ships. The question comes from a reviewer that never saw the original chat — a fresh model read of the diff only. If the developer answers wrong, the push is blocked; they get follow-up scenarios until they answer correctly or bypass explicitly (every bypass is logged). At 217pts and 73 HN comments, this is the highest-traction Show HN for an AI code governance tool in recent memory. The signal is not just Sphinx itself: at least three independent implementations of the same pattern exist (Examen on PyPI, code-comprehension-skill on skills.cat, mcp-creator-growth quiz tool). **Multiple independent implementations meeting within weeks** is the two-signal rule firing at the pattern level.

## What stands out immediately

- Interactive quiz loop: reviewer model reads only the diff (not the chat), asks a behavioral scenario question, verifies the developer's mental model before push proceeds
- Every explicit bypass (`sphinx yolo`) is logged — an audit trail for when governance is overridden
- Works with Codex, Claude Code, Cursor, OpenCode, and Pi — agent-agnostic by design
- Runs on OpenRouter or any OpenAI-compatible endpoint — cost-minimized, model-flexible
- `.env` files and keys are never read; developer answers are not sent to the coding agent
- Example in the Show HN: webhook handler saves event ID before `charge()` — Sphinx catches "what happens when Stripe retries after a failed charge?" Developer's first answer is wrong; Stripe idempotency gap is surfaced before the push lands
- Complementary to REVIEW.md (claude.dev, 2026-10-17): that signal was reviewer-side config; Sphinx is author-side verification before the review even starts
- Three independent parallel implementations: Sphinx (npm, MIT), Examen (Python/PyPI), code-comprehension-skill (Claude Code skill, skills.cat), mcp-creator-growth quiz tool (MCP server, 6★)

## Why clawfit should care

This is an architecturally new primitive: a **pre-push human-in-the-loop AI code verification gate** that operates at the harness/tool layer, not the review layer. It addresses the "vibe coding" problem (developer ships code they don't understand because the agent wrote it) at the Git workflow level rather than at the PR review level. The REVIEW.md signal (2026-10-17) was post-commit governance; Sphinx is pre-commit verification. Together they represent a two-stage governance stack emerging around AI coding agents:

1. Author-side: Sphinx (pre-push quiz) — first signal today
2. Reviewer-side: REVIEW.md + diff-driven risk tiers (2026-10-17) — already tracked

For clawfit, `governance_need: hard` orgs now have two independent software-layer mechanisms to recommend alongside the existing `self-hosted` + `data_sensitivity: confidential` combination.

## Preliminary interpretation

Current best reading:
- **Level 3 — Governance layer** (author-side verification hook before code leaves the developer's machine)
- **Level 2 secondary** (Git pre-push hook as a harness-adjacent governance primitive)

## Claims to verify

- Whether Sphinx has a public GitHub repo and what its star count is (Show HN launch, GitHub URL not confirmed)
- Whether the multiple parallel implementations (Examen, code-comprehension-skill) coordinate or are independently developed
- Whether the quiz model's judgment quality is consistent — the pattern depends on the reviewer model reliably generating the right scenario questions from a diff
- Whether Sphinx adoption grows or stays at demo stage (Show HN projects frequently stall post-launch)

## Status

- New signal: first tracking entry for "pre-push AI code comprehension quiz as author-side governance primitive"
- Two-signal rule: Sphinx + 3 independent implementations = pattern-level signal; **canonical section addition candidate** at L3 if a second distinct org or project ships this as policy (not just a side project)
- 📡 note: "AI code verification gate" pattern is emerging as a distinct L3 sub-type; today's cluster (Sphinx 217pts + Examen + code-comprehension-skill) is the strongest independent-implementation signal for this category to date
