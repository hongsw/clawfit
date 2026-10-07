# Research Watch: OpenTPU — Community-Built Full-Stack FPGA AI Accelerator

- Repo/Link: https://github.com/fesens/OpenTPU
- Source: Hacker News front page (210 pts)

## Why this is worth watching
OpenTPU delivers a complete FPGA-based AI inference stack — RTL hardware description, ISA, simulator, compiler, and profiler — in a single repo targeting the Kintex-7 PCIe card. Unlike cloud TPU or GPU approaches, it targets a community-accessible FPGA card and successfully runs modern LLMs (Qwen3, LFM2.5, Qwen3.5). This is the first known full-stack, open-source hardware+software AI inference design in Verilog that reports successful model execution.

## What stands out immediately
- Full vertical stack: RTL (Verilog) + ISA + simulator + compiler + profiler, all open-source
- Runs current models: Qwen3 and LFM2.5 confirmed running on Kintex-7 FPGA PCIe card
- 204★ / 8 forks at time of tracking; 210 HN pts signals real community interest beyond the star count
- Represents a "build your own TPU" approach, structurally distinct from consumer GPU inference (Strata/llama.cpp) and cloud hardware
- Hardware: Kintex-7 is a mid-range Xilinx FPGA, widely available on second-hand market

## Why clawfit should care
Extends the `hardware: local` category into FPGA territory — a governance-friendly, low-power, air-gapped inference substrate not previously represented. Relevant to organizations with `data_sensitivity: confidential` and `governance_need: hard` that cannot use GPU cloud or consumer VRAM-limited devices. May change the `hardware.json` registry as FPGA inference matures from research to deployable option.

## Preliminary interpretation
Current best reading:
- **Level 7 — Inference / Execution Infrastructure** (primary; hardware substrate)

## Status
- First signal for "community-built full-stack FPGA AI accelerator running modern LLMs"
- Monitoring: 204★ is low but HN engagement confirms real interest; check back at 1k+ stars
- Registry entry: not warranted yet (no service; hardware-only; pre-production)
