# 0.1.0 검증 기록

- 기준일: 2026-10-12
- 로컬 manifest·Skill·경로·버전 검사: 통과
- 검증기 회귀 테스트: 3개 통과
- Claude Code 공식 manifest 검증: marketplace와 plugin 모두 경고 없이 통과
- GitHub Actions: 설정 검사·회귀 테스트 통과
- Codex CLI 0.153.0: 공개 GitHub marketplace 등록, kitsch@kitsch 0.1.0 설치·활성화 확인
- Claude Code 2.1.140: 공개 GitHub marketplace 등록, 사용자 범위 설치, audio Skill과 plugin:kitsch:kitsch HTTP 서버 등록 확인
- Codex 실제 개발자 계정 OAuth·목소리 조회: 통과, 4개 도구 발견·목소리 15개 조회, 유료 호출 0회
- Codex 검증은 app-server의 임시 세션에서 플러그인이 제공한 서버를 사용했습니다. 별도 수동 MCP 항목 없이 검증했습니다.
- Claude Code 실제 계정 OAuth·목소리 조회: 미검증, 사용자 인증 대기
- 연결 해제·재연결: 미검증
- 유료 합성·전사: 미검증; 입력·요청 수·비용 한도 합의 후 실행
- 공식 제품 디렉터리 등록: 범위 밖

설치 성공은 실제 계정 인증이나 음성 작업 성공을 의미하지 않습니다.
검증 계정은 개발자 본인의 @kitschlabs.com 계정만 사용합니다.
검증 기록에 토큰·API 키·오디오 원문을 넣지 않습니다.

Claude Code의 기존 Confirmo 종료 훅에서 Windows 경로 오류가 발생했습니다.
Kitsch 설치 명령은 종료 코드 0으로 성공했으며, Kitsch 패키지에는 훅이 없습니다.
Claude Code 2.1.140의 plugin details는 inline MCP를 0개로 표시하지만,
mcp list는 plugin:kitsch:kitsch와 인증 필요 상태를 표시했습니다.
