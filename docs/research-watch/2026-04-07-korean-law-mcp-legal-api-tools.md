# Research Watch: korean-law-mcp — 한국 법령 39개 API를 14개 MCP 도구로

- Repo/Link: https://github.com/chrisryugj/korean-law-mcp
- Source: hongsw GitHub stars

## 무엇인가

chrisryugj가 만든 **한국 법령정보원 API 39개를 14개 MCP 도구로 통합한 법률 검색 MCP 서버**다. v3.0.0 (2026-04-07, Unified Architecture)에서 v2의 89개 도구를 14개로 대폭 압축하며 컨텍스트 비용을 82% 절감했다. TypeScript/Node.js 18+, MCP 1.27, 스타 1,200개, 포크 209개.

## 주요 특징

- **v3 아키텍처**: API 39개 → 도구 14개, 컨텍스트 ~110KB → ~20KB (82% 절감)
- **17개 도메인 통합 검색**: 판례, 헌법재판소, 국세청, 공정거래위원회, 노동위원회, 관세심판 등
- **8개 체이닝 도구**: 복합 법률 쿼리 지원
- **캐싱**: 검색 1시간 TTL, 아티클 텍스트 24시간 TTL
- **문서 처리**: HWPX, HWP, PDF, XLSX, DOCX (kordoc 2.1)
- 배포: npm + hosted endpoint (korean-law-mcp.fly.dev)
- 라이선스: MIT

## clawfit 관점에서 의미

- L4c MCP 서버 중 한국어 도메인 특화 첫 추적 사례
- `network=online` + `role=researcher/exec` + 법률 컨텍스트가 필요한 조직 프로파일에 직접 관련
- API 89개→14개 압축 설계는 rtk/caveman의 컨텍스트 절감 트렌드와 동일 방향
- 스타 1,200개 (포크 209): 한국 법률 AI 도구 중 가장 높은 채택률

## 분류

**Level 4c — 도구 사용 / 액션 인프라 / MCP 서버 (한국 법령 도메인 특화)**

## 상태

- 추적 중: 신규 등록. 스타 1,200개 (포크 209, v3.0.0 2026-04-07). 도메인 확장(판례 API 추가 등) 및 영문 법령 지원 여부 모니터링.
