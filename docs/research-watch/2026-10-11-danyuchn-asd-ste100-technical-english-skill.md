# Research Watch: danyuchn/asd-ste100-skill — Aerospace Technical Writing Standard Applied to Agent Instructions

- Repo: https://github.com/danyuchn/asd-ste100-skill (⭐4,412)
- Source: GitHub Trending (weekly, +945 this week)

## Why this is worth watching
ASD-STE100 is the Simplified Technical English standard developed for aerospace and defense technical manuals (ASD Aerospace and Defense Industries Association). It enforces vocabulary restriction (900 approved words), active-voice rules, sentence length limits, and a prohibition on ambiguous pronouns — specifically to eliminate the ambiguity that causes maintenance errors when a technician misreads an instruction and does the wrong thing. The author of this skill is applying the same discipline to agent-facing instructions, on the hypothesis that LLMs fail on ambiguous natural language instructions for the same structural reason a mechanic does: when a sentence can be parsed two ways, the parser picks one. This is a genuinely non-trivial transfer from technical documentation theory to agent instruction engineering, not just a "write clear prompts" blog post rebottled as a skill.

## What stands out immediately
- **ASD-STE100 provenance**: a production industrial standard with decades of validation in high-stakes maintenance documentation (avionics, defense, nuclear), not a homegrown writing guide
- **Vocabulary control**: the standard restricts to ~900 approved technical words and their approved meanings — applied to agent instructions, this limits polysemy that causes model confusion
- **Active voice enforcement**: passive-voice agent instructions ("The file should be created") are genuinely ambiguous about agent vs. environment responsibility — the standard's active-voice rule eliminates this
- **Sentence structure rules**: max 20 words per sentence in procedures, no embedded clauses — directly maps to LLM context parsing where long embedded clauses increase hallucination risk
- **Targeting Claude Code explicitly**: the skill integrates into Claude Code's instruction pipeline, not a standalone prompt formatter
- **4,412 stars, +945 in one week**: the velocity (21% growth in one week) is unusually high for a niche technical writing skill
- **Python**: the underlying rewriting logic is open and inspectable, not a black box

## Why clawfit should care
The ASD-STE100 skill addresses a gap in the L4 layer that no tracked tool currently covers: the quality of the natural language instructions passed to agents. clawfit scores agents on their technical capabilities (latency, cost, task fit) but not on the instruction quality pipeline that feeds them. Teams using ASD-STE100-rewritten instructions will likely experience lower hallucination rates on ambiguous tasks — a signal that the `min_maturity` and `setup_complexity` axes may be correlated with instruction quality, not just harness sophistication. Additionally: 4,412 stars in what appears to be a recent project launch suggests that a previously latent problem ("my agent does the wrong thing when I give it ambiguous instructions") has found a concrete solution that developers recognize immediately.

## Preliminary interpretation
Current best reading:
- **Level 4 — Capability layer (agent skills)** (primary): a Claude Code skill that rewrites instruction text to comply with ASD-STE100 grammar rules before the agent reads them

The L4 classification is straightforward. The more interesting question is whether this represents a new sub-type within L4: "instruction preprocessing skills" that transform input quality rather than extending agent capabilities. Prior tracked L4 skills (SwiftUI-Agent-Skill, NVIDIA-Skills, Google-Skills, Cangjie-Skill) all extend what the agent can do; this one changes how clearly the agent reads what it's asked to do — a different axis.

## Claims to verify
- Whether the ASD-STE100 vocabulary restriction (~900 words) is actually applied computationally or only as a style guide (the full STE100 approved word list is a licensed document; unclear if the skill uses the public subset or approximates it)
- The actual failure-mode reduction for agent instruction ambiguity — the aerospace validation is for human technicians; transfer to LLM parsing has not been independently benchmarked
- When the repository was created (no creation date visible on the GitHub page)

## Status
- First signal for "industrial technical writing standard applied as agent instruction preprocessing" — a new sub-type within L4
- Not a registry entry candidate (skill library, not an agent/LLM/hardware entry)
- Second signal check: ASD-STE100 + any other instruction-preprocessing skill using a formal writing standard would constitute a two-signal pattern for "writing-standard-based instruction hardening" at L4
