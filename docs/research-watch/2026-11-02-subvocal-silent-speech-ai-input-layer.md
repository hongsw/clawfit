# Research Watch: Subvocal — Silent Speech as AI Tool Input Layer

- Repo/Link: https://subvocal.company/ (no public GitHub; YC F26 company)
- Source: Hacker News (#1 Show HN, 114 points, 2026-11-02)

## Why this is worth watching

Subvocal is a Y Combinator Fall 2026 company building a wearable that decodes silent mouthing — subvocalization — into text input for AI tools. The claimed use case is not dictation as a general purpose: it is positioned specifically as an input layer for AI coding assistants (Claude, Cursor) and chat interfaces (ChatGPT), enabling command entry without audible speech. The company raised $1.3M from YC and Afore Capital.

This is the second signal in the "voice/speech as AI tool input infrastructure" cluster after Handy (2026-11-01, 36k stars, Whisper-based spoken dictation). Handy is software-only and works with spoken speech; Subvocal adds a hardware-in-the-loop approach targeting a different constraint: silent environments (open offices, meetings, public spaces).

## What stands out immediately

- **Subvocalization, not speech recognition**: targets the muscle movements of silent mouthing rather than acoustic speech; this means the device works in environments where speaking aloud is socially or practically impossible
- **Claimed 200 WPM speed**: significantly faster than typical spoken dictation (130–160 WPM) and far faster than keyboard input (~40 WPM); treat this as an unverified marketing claim until accuracy benchmarks are published
- **AI-tool-first positioning**: the company explicitly names Claude, Cursor, and ChatGPT as target interfaces rather than general dictation; this is an application-layer choice about where the value sits
- **YC F26 + $1.3M pre-seed**: very early stage; the product is pre-launch as of this writing; form factor is variously described as glasses and as a behind-the-ear wearable — a discrepancy in coverage that suggests rapid spec iteration
- **No accuracy data published**: surface EMG-based silent speech recognition typically achieves ~77% accuracy on limited vocabulary sets (per SilentWear arXiv 2026); 200 WPM at 77% accuracy produces significant correction overhead
- **No open-source SDK confirmed**: a PyPI package called "subvocal" exists (github.com/PranavKalkunte/subvocal) but is not confirmed to be affiliated with The Subvocal Company; treat it as a separate project unless confirmed otherwise
- **No MCP integration or agent harness support**: positioned at the OS input layer (keyboard replacement), not as an MCP tool or agent skill

## Why clawfit should care

Two signals in two days (Handy on 2026-11-01, Subvocal on 2026-11-02) both point at the same pattern: developers are building or adopting dedicated input tooling for AI tool use, ahead of harness-native voice or speech support. The signals differ on approach:
- Handy: software, spoken speech, Whisper/Parakeet, clipboard output
- Subvocal: hardware wearable, silent mouthing, EMG/subvocal, keyboard-replacement mode

These are different enough that the two signals do not confirm the same sub-type for taxonomy purposes (hardware vs. software; silent vs. spoken). However, the convergence reinforces the 2026-11-01 watch note: harness makers (Claude Code, Cursor, Gemini CLI) should expect external pressure to add native voice/speech input modes, and competitors may enter this input layer before harnesses support it natively.

For clawfit's scoring model, input modality is currently unmodeled. If a user's workflow includes frequent voice or subvocal input, the agent's support for structured command input (SKILL.md, CLI completions, natural-language task routing) may become a differentiating factor.

## Preliminary interpretation

Current best reading:
- **Level 6 — Human Interface** (primary): a hardware/software input device that sits at the human-agent interaction surface
- No secondary level: it operates at the input layer and does not implement agent logic, memory, or orchestration

## Claims to verify

- Accuracy of subvocalization decoding at claimed 200 WPM: surface EMG silent speech recognition literature shows ~77% accuracy; 200 WPM at that accuracy is not practical for coding command entry without continuous correction
- Whether the hardware form factor is glasses or behind-ear — the discrepancy in coverage suggests the product design is not finalized
- Whether The Subvocal Company is affiliated with the open-source PyPI "subvocal" package
- YC batch timing: YC F26 is listed, but the company is described as "sub-pre-seed" in some coverage; exact stage and launch timeline are unconfirmed

## Status

- New signal; not previously tracked
- Registry eligibility: hardware product; no GitHub repo; does not fit `agents.json`, `llms.json`, or `hardware.json` schema; no registry addition
- Watch for: public accuracy benchmark; official open-source SDK release; Claude Code / Cursor integration announcement; second hardware silent-speech wearable for AI tools
- Relation to existing signals: second in "voice/speech as AI tool input infrastructure" cluster (Handy, 2026-11-01); two-signal rule met for the cluster's existence — both signals confirm the pattern that developers want dedicated speech/silent input tooling for AI agents ahead of harness-native support; does NOT meet two-signal rule for a canonical taxonomy sub-section (hardware vs. software input are distinct approaches, not the same sub-type)
- 📡 note: "voice/speech input for AI tools" cluster is now two signals strong; watch for a harness-native implementation (Claude Code, Cursor, or Gemini CLI adding speech input) as the potential third-signal confirmation
