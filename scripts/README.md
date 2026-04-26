# scripts/ — 시각화 및 자동화 코드

본 폴더는 **MD 결과(`out/*.md`)를 시각화하거나 집계**하는 코드의 보관처다.  
프로젝트의 **단일 출처(Source of Truth)** 는 항상 `out/*.md` (그리고 그 입력인 `prompts/*.md`)이며, 본 폴더의 코드는 그 결과를 읽거나 동기화하여 그림·표를 생성하는 **파생물**일 뿐이다.

## 원칙

1. **MD가 단일 출처**, 코드는 보조.
2. 데이터(`DATA = {...}`)를 코드에 임베드하는 경우, **반드시 MD를 먼저 수정**한 뒤 코드와 동기화한다.
3. CSV는 따로 보관하지 않는다 — 필요할 때 코드로 즉석 생성.
4. 한 스크립트는 한 일만 한다(읽기 → 계산 → 그림 1장 또는 표 1개).

## 실행 환경

기본 가정: 사용자의 conda 환경(예: `llm-strategy-benchmark`)에 `numpy`, `matplotlib` 가 이미 설치되어 있다.

```bash
conda activate llm-strategy-benchmark
python scripts/02_iu_matrix.py
```

### 한글 폰트

- 시스템에 한글 TTF가 하나도 없으면, 스크립트가 **NanumGothic-Regular.ttf** 를 Google Fonts에서 자동으로 받아 `assets/fonts/` 에 저장하고 등록한다 (최초 1회, 약 4 MB, 네트워크 필요).
- 이미 시스템에 NanumGothic / Noto Sans CJK KR / Malgun Gothic 등이 있으면 그것을 우선 사용한다.
- 다운로드를 원치 않으면, 임의의 한글 .ttf 를 다음 위치 중 하나에 두면 된다:
  - `assets/fonts/NanumGothic-Regular.ttf`
  - `~/.fonts/NanumGothic.ttf`
  - 또는 `sudo apt install fonts-nanum` 으로 시스템 전역 설치
- 다운로드도 시스템 폰트도 없으면 한글이 □ 박스로 렌더된다 (경고 출력).

### IPython / Jupyter 에서 실행

`%run scripts/02_iu_matrix.py` 또는 셀에 붙여넣어 실행해도 동일하게 동작한다. 종료 시 `SystemExit` 경고가 뜨지 않도록 `sys.exit()` 은 사용하지 않는다.

## 스크립트 목록

| 스크립트 | 입력 (MD) | 출력 (asset) |
|----------|-----------|--------------|
| `02_iu_matrix.py` | `out/02-impact-uncertainty.md` §2.3.1 평가표 | `assets/02-iu-matrix.png` |
