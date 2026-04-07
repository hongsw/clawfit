# Research Watch: ATLAS — 동결 모델로 74.6% LiveCodeBench 달성하는 로컬 코딩 에이전트

- Repo/Link: https://github.com/itigges22/ATLAS
- Source: hongsw GitHub stars

## 무엇인가

**Adaptive Test-time Learning and Autonomous Specialization** — 파인튜닝 없이 동결된 소형 모델로 제약 주도 생성을 통해 최고 수준의 코딩 성능을 달성하는 로컬 에이전트다. Qwen3-14B 기준 LiveCodeBench pass@1-v(k=3) 74.6% 달성. v3.0.1 (2026-04-06), Python, AGPL-3.0, 스타 1,500개, 포크 127개.

## 성능 수치

| 모델 | LiveCodeBench |
|------|--------------|
| ATLAS (Qwen3-14B) | **74.6%** |
| DeepSeek V3.2 Reasoning | 86.2% |
| Claude 4.5 Sonnet | 71.4% |

- 비용: **~$0.004/작업** (전기 비용만) vs GPT-5: $0.043
- 추론 속도: ~51 tokens/초
- Phase별 개선: 기본 54.9% → Phase 1 +12.4pp → Phase 3 +7.3pp

## 주요 특징

- **3단계 파이프라인**: PlanSearch + Geometric Lens 선택 + 자기검증 반복 수리
- **문법 강제 구조화 출력**: 할루시네이션 억제
- 지원 언어: Python, Rust, Go, C, Shell
- **완전 로컬**: API 호출 없음
- 추론 엔진: llama.cpp (llama-server), Fox (PagedAttention)
- 배포: Docker + nvidia-container-toolkit 또는 Podman
- 최소 요구: 16GB GPU VRAM, 14GB RAM, 20GB 스토리지

## clawfit 관점에서 의미

- `offline_required=True` + `latency=low` + `budget=minimal` 프로파일의 고성능 옵션
- 동결 모델 + 추론 시점 학습 패턴 — fine-tuning 없이 성능 향상하는 L5 연구 신호
- L1(로컬 코딩 에이전트)과 L5(벤치마크 생산) 이중 분류
- 스타 1,500개 (포크 127, 커밋 35+, v3.0.1)

## 분류

**Level 1/5 — 로컬 코딩 에이전트 런타임 + 테스트 시점 학습 연구 (L5 벤치마크 생산)**

## 상태

- 추적 중: 신규 등록. 스타 1,500개 (포크 127, v3.0.1 2026-04-06). CLI 신뢰도 95.8%. 멀티 언어 지원 확장 및 더 큰 모델 적용 결과 모니터링.
