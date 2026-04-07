# Research Watch: claude-peers-mcp

- Repo/Link: https://github.com/louislva/claude-peers-mcp
- Source: hongsw GitHub stars

## 무엇인가

claude-peers-mcp는 **동일 머신에서 실행 중인 여러 Claude Code 인스턴스가 서로를 발견하고 실시간으로 메시지를 주고받을 수 있게 하는 MCP 서버**다. SQLite 브로커 데몬을 localhost:7899에서 실행해 각 Claude Code 세션을 피어로 등록하고, 네 가지 도구 동사(`list_peers`, `send_message`, `set_summary`, `check_messages`)로 인스턴스 간 통신을 가능하게 한다. Bun 런타임 단일 의존성, 설치 두 명령.

## 주요 특징

- **Peer Discovery**: 머신/디렉토리/리포 스코프 내 다른 Claude Code 세션 탐색
- **즉각적 메시징**: `claude/channel` 푸시 프로토콜로 폴링 없이 실시간 전달
- **상태 공유**: 세션 간 작업 상태 브로드캐스트
- **로컬 한정**: 머신 내 피어 메시의 현재 구현 (크로스 머신은 DureClaw 참조)
- TypeScript, MIT 라이선스

## clawfit 관점에서 의미

- 오케스트레이터-워커가 아닌 **피어 메시 토폴로지**를 레지스트리에서 다루지 않음 → 카테고리 갭
- `network=online` 태그가 부정확함: 메시지 패싱은 로컬이지만 LLM 호출은 온라인 → 혼합 네트워크 모델
- 같은 개발 머신에서 병렬 Claude Code 세션을 운영하는 팀에 직접 관련
- 스타 약 1,800개 (1.8k): L4c MCP 서버 중 높은 채택률

## 분류

**Level 4c — 도구 사용 / 액션 인프라 / MCP 서버 (Claude Code 피어 메시 메시징)**

## 상태

- 추적 중: 신규 등록. 높은 신호. 스타 ~1,800개 (포크 196, 커밋 5, Claude Code v2.1.80+ 필요). 크로스 머신 지원, 인증 모델, Anthropic 공식 채택 여부 모니터링.
