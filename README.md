# Kitsch Labs Plugins

Codex·Claude Code에서 Kitsch Labs 음성 도구를 사용하는 플러그인입니다.
호스팅 MCP 연결 설정과 음성 작업 Skill을 함께 제공합니다.
MCP 서버를 로컬에 설치하거나 API 키를 복사할 필요가 없습니다.

현재 버전: **0.1.0**. 초기 배포이며 실제 OAuth·유료 음성 작업 검증 상태는
[검증 기록](docs/validation.md)을 확인하세요. 공식 제품 디렉터리 입점이 아닌
Kitsch Labs의 GitHub 마켓플레이스입니다.

## 설치

플러그인 기능을 지원하는 Codex 또는 Claude Code가 필요합니다.

### Codex

```bash
codex plugin marketplace add KitschLabs/kitsch-plugins
codex plugin add kitsch@kitsch
```

새 대화를 시작하고 Kitsch 플러그인 연결의 인증 안내를 따르세요.
플러그인이 MCP 연결을 등록하므로 별도 `codex mcp add`는 필요하지 않습니다.

### Claude Code

```bash
claude plugin marketplace add KitschLabs/kitsch-plugins
claude plugin install kitsch@kitsch --scope user
```

새 세션에서 `/mcp`를 열고 플러그인의 Kitsch 연결을 선택해 인증하세요.

### 계정 연결과 확인

브라우저에서 Kitsch 계정으로 로그인하고 본인이 소유자 또는 관리자인 활성
워크스페이스를 선택해 동의하세요. 비밀번호·API 키·토큰은 채팅에 입력하지 마세요.
사용량은 선택한 워크스페이스의 크레딧 또는 후불 요금에 반영됩니다.

설치 확인은 다음처럼 비과금 작업으로 시작하세요.

> Kitsch의 도구 목록과 사용 가능한 목소리를 보여줘. 아직 합성이나 전사는 하지 마.

목소리 조회, 음성 합성, 파일 전사 준비, 기존 작업 조회 도구가 연결됩니다.
파일 전사에는 로컬 파일을 읽고 HTTP로 전송할 수 있는 클라이언트 도구가
추가로 필요합니다. MCP 연결만으로 마이크·실시간 음성 답장이 설정되지는 않습니다.

## 기존 수동 MCP 연결에서 전환

1. 기존 Kitsch 연결의 설정 위치와 범위를 확인하고 복원할 설정을 보관합니다.
2. 플러그인을 설치한 뒤 기존 수동 Kitsch 항목만 비활성화합니다. 다른 서버는 유지합니다.
3. 새 세션에서 플러그인 연결로 로그인하고 도구·목소리 조회를 확인합니다.
4. 성공하면 이전 수동 항목을 제거할 수 있습니다. 실패하면 플러그인을 비활성화하고
   기존 설정을 복원하세요. 두 연결을 동시에 사용하지 마세요.

플러그인 연결 이름에는 클라이언트별 접두사가 붙을 수 있습니다.
실제 표시된 이름을 사용하세요. 실패·timeout 후 유료 작업을 자동 재실행하지 마세요.

## 업데이트와 제거

Codex는 `codex plugin marketplace upgrade kitsch`로 목록을 갱신한 뒤
`codex plugin add kitsch@kitsch`로 최신 패키지를 설치하고 새 대화를 시작합니다.
Claude Code는 `claude plugin marketplace update kitsch` 후
`claude plugin update kitsch@kitsch --scope user`를 실행하고 재시작합니다.
버전 변경 없는 패키지 덮어쓰기는 배포하지 않습니다.

```bash
codex plugin remove kitsch@kitsch
# 또는
claude plugin uninstall kitsch@kitsch --scope user
```

플러그인 제거와 서버 접근 권한 해제는 별개입니다.
Kitsch 앱의 **계정 설정 → 연결된 에이전트**에서 해당 연결을 해제하세요.
이미 시작된 작업과 발생한 과금은 취소되지 않습니다.

## 개발과 릴리스

```bash
python scripts/validate.py
python -m unittest discover -s tests
claude plugin validate .
claude plugin validate ./plugins/kitsch
```

두 manifest의 버전을 함께 올리고 검증 결과를 기록한 후 `v0.1.0` 같은 태그로
배포합니다. CI는 설정·경로·버전과 검증기 회귀 테스트를 실행합니다.
Codex는 지원되는 `.codex-plugin/plugin.json` 호환 형식을 사용하며,
Claude Code와 같은 Skill 디렉터리를 공유합니다.

- [Kitsch MCP 안내](https://www.kitschlabs.com/docs/mcp)
- [서비스 HTTP API 연동](https://www.kitschlabs.com/docs/en/for-agents#service-api)
- [OpenAI 플러그인 규격](https://developers.openai.com/plugins/build/plugins)
- [Claude Code 플러그인 규격](https://code.claude.com/docs/en/plugins-reference)

MIT 라이선스는 이 저장소의 플러그인 파일에 적용됩니다.
호스팅 서비스의 이용 조건과 요금은 Kitsch Labs 서비스 정책을 따릅니다.
