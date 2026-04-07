# Research Watch: autoresearch — AI 에이전트 자율 ML 연구 루프

- Repo/Link: https://github.com/karpathy/autoresearch
- Source: hongsw GitHub stars

## 무엇인가

Andrej Karpathy가 제작한 **자율 ML 연구 루프**다. AI 에이전트가 `train.py`를 직접 수정하며 5분 단위 실험을 인간 개입 없이 반복 실행한다. 시간당 약 12회, 야간 무인 실행 시 약 100회 실험을 수행하며 각 실험 결과를 validation metric(bits per byte)으로 평가·기록한다. 코드베이스는 간결하며 커밋 36개, Python 83.4% + Jupyter 16.6%.

## 주요 특징

- **제약된 탐색 공간**: 에이전트는 `train.py`만 수정 가능 — `prepare.py`와 `program.md`는 고정
- **5분 학습 예산**: 실험당 wall clock 5분 (startup 제외) — 빠른 반복을 위한 설계
- **시간당 ~12 실험**, 야간 실행 시 ~100 실험
- **BPE 토크나이저**: 1회 setup ~2분
- **최적화기**: Muon + AdamW 조합, Full GPT 아키텍처
- 요구 하드웨어: NVIDIA H100 (테스트 기준), Python 3.10+, uv

## clawfit 관점에서 의미

- L5(평가/연구 루프)의 교과서적 사례 — reference-levels에 이미 autoresearch 패턴으로 명시
- `offline_required=True` + 고성능 GPU 프로파일에 해당
- 스타 67,800개, 포크 9,800개: Karpathy 효과로 즉각적 대규모 채택
- clawfit 레지스트리에 `task=research`, `hardware=gpu-server` 조합의 극단 사례

## 분류

**Level 5 — Research / evaluation / autoresearch 루프**

## 상태

- 추적 중: 신규 등록. 스타 67,800개 (포크 9,800, 커밋 36). Karpathy 제작 신뢰도 높음. GPU 의존도가 clawfit edge 프로파일과 불일치 — 연구 신호로만 추적.
