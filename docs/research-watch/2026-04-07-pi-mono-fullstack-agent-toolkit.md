# Research Watch: pi-mono — L1~L7 전체 스택 에이전트 툴킷 모노레포

- Repo/Link: https://github.com/badlogic/pi-mono
- Source: hongsw GitHub stars

## 무엇인가

Mario Zechner(badlogic)가 만든 **AI 에이전트 풀스택 모노레포**다. 코딩 에이전트 CLI, 멀티 프로바이더 LLM API, 차등 렌더링 TUI, 웹 채팅 컴포넌트, Slack 봇, vLLM GPU 포드 관리를 7개 npm 패키지로 통합한다. v0.65.2 (2026-04-06), TypeScript 95.9%, 스타 32,600개, 포크 3,600개, 커밋 3,476개.

## 7개 핵심 패키지

| 패키지 | 역할 | 레이어 |
|--------|------|--------|
| `@mariozechner/pi-ai` | 멀티 프로바이더 LLM API (OpenAI, Anthropic, Google 등) | L1 |
| `@mariozechner/pi-agent-core` | 에이전트 런타임 (도구 호출, 상태 관리) | L1/L2 |
| `@mariozechner/pi-coding-agent` | 코딩 작업용 인터랙티브 CLI | L1 |
| `@mariozechner/pi-tui` | 차등 렌더링 터미널 UI 라이브러리 | L7 |
| `@mariozechner/pi-web-ui` | 채팅용 웹 컴포넌트 | L7 |
| `@mariozechner/pi-mom` | Slack 봇 통합 레이어 | L4c |
| `@mariozechner/pi-pods` | vLLM 배포 GPU 포드 관리 | L1 (인프라) |

## 주요 특징

- **단일 모노레포로 L1~L7 커버**: 런타임, 오케스트레이션, 도구 통합, 인터페이스 모두 포함
- **pi-generative-ui의 모체**: 앞서 추적한 pi-generative-ui가 이 모노레포의 플러그인 생태계 위에서 작동
- 최근 6일간 34+ 커밋, v0.65.0→0.65.1→0.65.2 연속 릴리스: 매우 활발한 개발 중
- npm 모노레포 워크스페이스 구조로 개별 패키지 독립 사용 가능

## clawfit 관점에서 의미

- **pi-generative-ui 맥락 완성**: 기존 추적 중인 pi-generative-ui가 이 모노레포의 플러그인임을 확인 → 두 문서 연결 필요
- L1부터 L7까지 단일 프로젝트로 커버하는 "합성 제품" 패턴의 가장 완전한 사례
- `pi-tui`는 clawfit TUI 구현의 직접적 참고 대상
- 스타 32,600개 (포크 3,600, 커밋 3,476): 대규모 실무 채택 확인

## 분류

**Level 1+2+4c+7 — 풀스택 에이전트 툴킷 (런타임 + 오케스트레이션 + 도구 + 인터페이스)**

## 상태

- 추적 중: 신규 등록. 스타 32,600개 (포크 3,600, 커밋 3,476, v0.65.2 2026-04-06). pi-generative-ui와 연계 추적. GPU 포드 관리 및 TUI 라이브러리 성숙도 모니터링.
