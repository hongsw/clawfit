# Research Watch: DureClaw

- Repo/Link: https://github.com/DureClaw/dureclaw
- Source: hongsw GitHub stars (hongsw 본인 제작)

## 무엇인가

DureClaw는 **물리적으로 분리된 여러 머신에 분산된 AI 에이전트를 Claude Code 오케스트레이터가 조율하는 멀티머신 에이전트 오케스트레이션 플랫폼**이다. 이름은 한국의 협동 농경 전통 '두레(dure)'에서 따왔으며 분산되었지만 통합된 협력이라는 철학을 반영한다. claude-peers-mcp가 머신 내 피어 메시라면, DureClaw는 머신 간 크루 오케스트레이션이다.

## 아키텍처

3층 구조:
1. **Claude Code 오케스트레이터** — 작업을 분해하고 워커에 배분
2. **Phoenix WebSocket 서버** — 메시지 버스 역할, Docker로 실행 (Elixir 불필요), Tailscale 네트워킹
3. **oah-agent 데몬** — Mac/Linux/Windows/Raspberry Pi 4·5·Zero W 등 각 워커 머신에서 실행

## 주요 특징

- **이종 AI 백엔드**: 워커가 claude / opencode / gemini / aider 중 어떤 에이전트든 실행 가능 (Claude 고정 아님)
- **워커 역할 분리**: Builder(코드 작성), Tester(테스트), Analyst(리뷰), Executor(작업 실행)
- **MCP 플러그인 배포**: `@dureclaw/mcp` npm 패키지 + MCP Registry + Smithery 등록 — 정식 배포 경로 완비
- **자연어 + 슬래시 명령**: `/setup-team`, `/team-status` 또는 자연어로 대체 가능
- **웹 대시보드**: 실시간 워커 상태 모니터링
- 다국어 README: 한국어, 영어, 중국어, 일본어

## clawfit 관점에서 의미

- hongsw 직접 제작 → 향후 clawfit 레지스트리 카테고리(이종 백엔드 오케스트레이션, 크로스 머신 에이전트 크루) 설계 방향에 직접적 영향
- L2(오케스트레이션 하네스)와 L4c(MCP 서버) 하이브리드 — 가장 아키텍처적으로 야심찬 항목
- 스타 1개이지만 작성자가 hongsw이므로 추적 우선순위 높음

## 분류

**Level 2 — 메타 래퍼 / 오케스트레이션 하네스 (크로스 머신 멀티 에이전트 크루 via MCP + Phoenix)**

## 상태

- 추적 중: 신규 등록, 개인 프로젝트 신호. 스타 1개, 커밋 109개, 포크 0 (hongsw가 작성자). 커밋 109개는 신규 프로젝트치고 상당한 작업량. 커뮤니티 채택 및 MCP Registry 등록 상태 모니터링.
