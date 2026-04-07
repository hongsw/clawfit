# Research Watch: DeepTutor — 에이전트 네이티브 개인화 학습 어시스턴트

- Repo/Link: https://github.com/HKUDS/DeepTutor
- Source: hongsw GitHub stars

## 무엇인가

HKUDS(홍콩대학교 데이터 사이언스 연구소)가 만든 **에이전트 네이티브 개인화 학습 플랫폼**이다. RAG 기반 지식 허브, 5가지 모드(채팅/심층 풀이/퀴즈/심층 연구/수학 애니메이션)를 하나의 대화 스레드로 통합하며, 독립 메모리와 개성을 가진 Personal TutorBot을 제공한다. 출시 39일 만에 스타 10,000개 돌파. v1.0.0-beta.2 (2026-04-07), 스타 11,700개, 포크 1,600개.

## 주요 특징

- **5가지 학습 모드**: Chat, Deep Solve, Quiz Generation, Deep Research, Math Animator — 단일 대화 스레드 공유
- **Personal TutorBots**: 독립 메모리 + 개성 + 스킬셋을 가진 자율 튜터
- **Knowledge Hub**: RAG 준비 컬렉션 (PDF, Markdown, 텍스트)
- **AI Co-Writer**: AI 협업 마크다운 편집기
- **Persistent Memory**: 학습 진도를 추적하는 사용자 프로파일
- **Agent-Native CLI**: AI 에이전트용 구조화 JSON 출력 터미널 인터페이스
- **Math Animator**: ManimCat 기반 수학 시각화
- 기술 스택: Python 3.11+ / FastAPI, Next.js 16, React 19, LlamaIndex, nanobot
- 포트: Backend 8001, Frontend 3782

## clawfit 관점에서 의미

- HKUDS는 LightRAG, RAG-Anything 저자 — L6(지식 인프라) 계보를 잇는 교육 특화 버티컬
- L6(RAG 지식 허브) + L7(에이전트 네이티브 CLI, 웹 UI) 하이브리드
- `task=research` + `role=researcher` + `statefulness=persistent` 프로파일에 강력한 신호
- 39일 10k 스타: 교육 도메인의 빠른 채택 확인

## 분류

**Level 6/7 — 지식 인프라 + 에이전트 네이티브 인터페이스 (교육 도메인 버티컬)**

## 상태

- 추적 중: 신규 등록. 스타 11,700개 (포크 1,600, 커밋 450, v1.0.0-beta.2). 출시 39일 만에 10k 스타. TutorBot 독립 메모리 성숙도 모니터링.
