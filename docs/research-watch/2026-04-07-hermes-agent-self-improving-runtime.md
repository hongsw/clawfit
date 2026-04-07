# Research Watch: Hermes Agent — 자기 개선형 적응 에이전트 런타임

- Repo/Link: https://github.com/NousResearch/hermes-agent
- Source: hongsw GitHub stars

## 무엇인가

Nous Research가 만든 **자기 학습 루프를 내장한 AI 에이전트**다. 경험에서 스킬을 생성하고 사용 중에 지속적으로 개선한다. "$5 VPS, GPU 클러스터, 서버리스 인프라" 어디서나 실행 가능하며 Telegram, Discord, Slack, WhatsApp, Signal 등 메시징 플랫폼과 직접 통합된다. v0.7.0 (2026-04-03), Python 93.4%, 스타 29,600개, 커밋 3,420개.

## 주요 특징

- **Learning Loop**: 세션 경험 → 스킬 생성 → 다음 세션에서 개선 (자율 성장)
- **크로스 세션 메모리**: FTS5 세션 검색 + LLM 요약으로 과거 세션 재호출
- **Persistent User Modeling**: Honcho dialectic 방식 사용자 프로파일 추적
- **40+ 통합 도구**, OpenRouter 경유 200+ 모델 지원
- **메시징 통합**: Telegram, Discord, Slack, WhatsApp, Signal
- **내장 cron 스케줄러**: 무인 자동화
- **병렬 서브에이전트**: 독립 워크스트림용 격리 서브에이전트 스폰
- **MCP 서버 통합**
- 배포: Docker, SSH, Modal, Daytona, Singularity

## clawfit 관점에서 의미

- L1 적응형 런타임 신규 서브타입 — 기존 L1은 정적이나 Hermes는 학습 루프로 L4a(메모리)와 경계를 흐림
- `statefulness=persistent` + `role=researcher/exec` 고복잡도 프로파일에 최적
- 스타 29,600개 (포크 3,900, 커밋 3,420): 대형 생산 채택 확인
- clawfit 스코어링 모델에 `self-improvement` 피처 플래그 필요성 시사

## 분류

**Level 1 — 적응형 기본 에이전트 런타임 (자기 개선 루프 내장)**

## 상태

- 추적 중: 신규 등록. 스타 29,600개 (포크 3,900, 커밋 3,420, v0.7.0). 학습 루프 성숙도 및 스킬 라이브러리 크기 모니터링.
