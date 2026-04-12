# Research Watch: Berkeley RDI — "How We Broke Top AI Agent Benchmarks"

- Repo/Link: https://rdi.berkeley.edu/blog/trustworthy-benchmarks-cont/
- Source: Hacker News (171 points)

## Why this is worth watching
UC Berkeley's RDI team demonstrated that every major AI agent benchmark (SWE-bench, WebArena, OSWorld, FieldWorkArena, Terminal-Bench) can be exploited to achieve near-perfect scores without solving a single task. Seven recurring exploitation patterns were identified — from shared evaluation environments to LLM judges vulnerable to prompt injection. With 171 HN points, this is the highest-signal evaluation paper in recent scans.

## What stands out immediately
- All eight benchmarks tested were successfully exploited — not a one-off, a systemic pattern
- Seven vulnerability classes: shared eval environments, reference answers in task configs, unsafe `eval()`, prompt-injectable LLM judges, weak string matching, broken eval code, trust in untrusted outputs
- Specific exploits: replacing `{}` to fool FieldWorkArena; downloading gold answers to OSWorld; Terminal-Bench via binary wrapper trojans; SWE-bench via pytest hooks
- Authors propose an "Agent-Eval Checklist" (isolation, answer confidentiality, adversarial testing, robust scoring)
- Directly undermines model selection decisions based on published benchmark scores

## Why clawfit should care
clawfit's recommendation engine currently treats published benchmark positioning as implicit evidence for LLM quality ordering. If those benchmarks are exploitable, the LLM preference scores derived from them may be unreliable. This also has direct implications for Level 5 evaluation tooling: opencode-bench, mdarena, and Ko-AgentBench should each be evaluated against the Berkeley checklist. The "Agent-Eval Checklist" proposed by the researchers could become a reference standard for Level 5 entries going forward.

## Preliminary interpretation
Current best reading:
- **Level 5 — Research / evaluation / benchmark signal** (methodology critique, not a tool)

## Status
- Trend/critique signal, not a tool. No registry entry needed. Flag as reference when evaluating Level 5 entries. Consider whether LLM preference weights in scoring.py need an "evidence quality" caveat.
