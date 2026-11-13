# Research Watch: smolmaxxing — LLM Inference on Ultra-Small Consumer Devices

- Repo: https://github.com/hyperionaidev/smolmaxxing (⭐607)
- Source: Hacker News front page (458 points, 2026-11-13)

## Why this is worth watching

smolmaxxing benchmarks LLMs on hardware that is not on any mainstream inference roadmap: a Xiaomi TV box (3rd generation), a jailbroken 2013 iPad Air running iOS 12.5.7, and a OnePlus Nord CE 2 budget Android phone. Where llama-modchip (tracked 2026-11-09) addresses the 64 GB RAM developer workstation, smolmaxxing addresses the sub-2 GB RAM embedded device. The 458 HN points with only 607 GitHub stars indicates that interest in the concept exceeds engagement with the repo itself — a pattern typically seen when a blog or demo generates more attention than the codebase backing it.

## What stands out immediately

- **Hardware targets below mainstream:** The Xiaomi TV box, 2013 iPad, and OnePlus budget phone are outside every existing clawfit hardware profile; they represent a meaningful fraction of actually-deployed device hardware globally
- **Device-specific kernels:** 1-bit lookup-table kernel, repacked 2-bit and ternary formats for Cortex-A55 CPUs, a separate A7 variant (the 2013 iPad's CPU) that lacks dot-product instructions — no code reuse across targets
- **Expert paging from flash for MoE models:** Frequently-used experts kept in RAM; others paged from flash on demand with prefetching; this is an architectural adaptation of llama-modchip's ideas applied to 2 GB RAM constraints
- **Weight streaming for dense models:** Dense models larger than available RAM are streamed from flash at full bus speed; this enables 8B-class models on 2 GB devices
- **Headless mode on the TV box:** Disabling the launcher and Google services while a model runs frees approximately 400 MB RAM — a device-specific optimization not documented in mainstream inference runtimes
- **165 documented experiments including failures** in `EXPERIMENT.md` — a rare disclosure of null results and dead ends; methodological honesty
- **Pre-converted model files on Hugging Face** and a template for submitting new device results — this is scaffolding for a community benchmarking effort, not just personal experiments
- **Patches on llama.cpp:** Not a fork; this reduces the maintenance surface and means experiments can track upstream fixes

## Why clawfit should care

clawfit's `hardware.json` currently covers developer workstations, cloud VMs, and consumer laptops. The embedded/IoT tier is structurally absent. smolmaxxing is not ready to become a registry entry — the accuracy of models at extreme quantization is unverified on coding tasks — but it is the second signal (after llama-modchip) pointing at sub-workstation inference as a real use case. Where llama-modchip optimized a 284B MoE for 64 GB workstation RAM, smolmaxxing does the equivalent for 2 GB TV boxes and old phones. These are different user populations: the former is a privacy-first development team; the latter is any user globally who cannot afford cloud access. Neither is currently scoreable with clawfit.

## Preliminary interpretation

Current best reading:
- **Level 7 — Infrastructure** (primary) — custom inference kernels, flash-streaming, and headless OS mode are infrastructure-layer work that enables higher-level layers to operate on otherwise infeasible hardware
- **Level 1 — Base Runtime** (secondary) — llama.cpp patches constitute a runtime modification; the actual model execution sits at L1

## Claims to verify

- Measured tokens/second on each device — the README mentions speeds but independent replication is needed
- Whether flash-streaming for dense models causes acceptable latency for interactive use or is batch-only
- Whether the Cortex-A55 kernel improvements have been or could be upstreamed to llama.cpp
- Accuracy on coding tasks at the target quantization levels — not documented in the repo

## Status

- New signal — tracking; registry action deferred (accuracy unverified; `hardware.json` has no schema for sub-2 GB embedded devices; `platform` and `ram_gb` fields would need new minimum-spec semantics)
- **Second signal for "small-device inference as a distinct hardware sub-type"** — llama-modchip (2026-11-09) is the first signal (64 GB workstation MoE); smolmaxxing is the complementary second signal for the sub-2 GB embedded device sub-type; two-signal rule is met across adjacent hardware classes but NOT for the same sub-type (64 GB ≠ 2 GB); watch for a third signal targeting the 8–16 GB mid-range (Raspberry Pi 5, Android flagship class) to confirm a continuous "offline inference spectrum" taxonomy worth canonicalizing
