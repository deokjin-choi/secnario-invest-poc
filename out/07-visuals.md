---
chapter: 7
title: Scenario 시각화 — 4 시나리오 헤로 이미지
status: 진행            # 1차 초안. 보고서 통합 직전 톤·시리즈성 점검 필요
source_prompts:
  - prompts/00-system_v1.md
  - prompts/07-visuals_v1.md      # v2 (4분면 균등, 16:9, photoreal, 영문 타이틀+부제)
inputs:
  - out/06-scenarios.md           # §6.1~§6.4 시나리오 narrative + 시각 메타포
assets:
  - assets/07-q1-pax-silica.png
  - assets/07-q2-bunkered-ai.png
  - assets/07-q3-green-concord.png
  - assets/07-q4-open-boom.png
generated_via: Cursor 내장 이미지 생성 도구 (cinematic photoreal, 16:9)
updated: 2026-04-26
note: |
  본 장은 6장 시나리오 4개를 보고서·덱 헤로용 16:9 이미지로 시각화한 결과다.
  - 4장 모두 동일 톤(사실적 미래 풍경) + 동일 텍스트 포맷 (Q? — NAME / SUBTITLE)으로 한 시리즈로 보이도록.
  - 이미지 내 텍스트는 영문만 (한글은 모델이 깨뜨릴 가능성). 한글 캡션은 본 마크다운에서 별도 처리.
  - 동영상은 본 POC 단계에서는 제외, 후속 라운드에서 시나리오별 15초 컷 검토.
---

# 제7장 — Scenario 시각화

> 6장의 4 시나리오 narrative를 한 장면으로 압축한 헤로 이미지 4장. 각 이미지는 보고서 헤로 슬롯(16:9)에 직접 들어가도록 작성되었고, 마크다운에서 한글 캡션과 결합한다.

## 한눈에 보기

| 분면 | 시나리오 | 이미지 | 핵심 메타포 한 줄 |
|------|---------|-------|------------------|
| Q1 (B+ × D−) | **Pax Silica** | `assets/07-q1-pax-silica.png` | 골든아워 사막, 동맹 깃발, 메가 DC 지평선까지 줄지어 |
| Q2 (B+ × D+) | **Bunkered AI** | `assets/07-q2-bunkered-ai.png` | 블루아워, 멈춘 공사장 + SMR 모듈 + 모라토리엄 표지 + 시위 라인 |
| Q3 (B− × D+) | **Green Concord** | `assets/07-q3-green-concord.png` | 트와일라잇 피오르, 풍력·SMR·태양광 통합 캠퍼스, 다국 깃발 |
| Q4 (B− × D−) | **Open Boom** | `assets/07-q4-open-boom.png` | 새벽빛, 신흥 시장 스카이라인 + 항만 + 휴머노이드 산업 라인 |

> **시각 일관성 규칙**: 모든 이미지가 16:9 / 사실적 미래 풍경 / 영문 타이틀 좌상단 / 부제 1줄. 색감만 시나리오별로 차등 (Q1 황금·청동 / Q2 슬레이트·앰버 / Q3 청록·에메랄드 / Q4 푸른 새벽).

---

## 7.1 Q1 — Pax Silica (B+ × D−)

![Q1 Pax Silica — 미·동맹 컴퓨트 우위 + 자유 빌드 시나리오의 헤로 이미지: 황금빛 사막에 늘어선 메가 데이터센터와 동맹국 깃발](../assets/07-q1-pax-silica.png)

**한글 캡션**: 골든아워 미 남서부 사막 분지에 메가 데이터센터가 지평선까지 줄지어 있고, 능선 위에 미·일·한·대·EU의 깃발이 함께 서 있다. 두 인물이 단지를 내려다보는 구도로 “미·동맹의 컴퓨트 우위가 인프라로 굳어진 풍경”을 압축한다.

**시각 메타포 메모**:
- 능선 위 동맹 깃발 = **P-4.2 반도체 동맹 명시화 (Pax Silica 합의)**
- 지평선까지의 메가 DC = **Env-1.2 자유 빌드 + T-2.2 미 DC 집중**
- 골든아워 톤 = **R1 + R2 동시 우상향**의 자기강화 분위기

**생성에 사용한 영문 프롬프트** (재현용):

```text
Cinematic photorealistic wide landscape, 16:9 aspect ratio, golden-hour late afternoon light over a vast Arizona-style desert basin. Foreground: a sweeping row of massive hyperscale data center campuses with cooling towers, transmission lines, and high-voltage substations stretching to the horizon. Mid-ground: a tightly grouped cluster of American and allied flags (USA, Japan, South Korea, Taiwan, EU) standing on a low ridge — small but readable, no logos. Two human figures in business attire (small scale, back to camera) observe from a vantage point. Sky: warm amber and bronze tones, light haze, subtle volumetric light. Mood: confident, ascendant, ordered. Ground: cracked desert clay with sparse vegetation. Composition: 1-point perspective drawing eye to the horizon. Editorial photography quality, no people's faces, no real corporate logos, no cartoon style. Text overlay (top-left corner, clean sans-serif uppercase white text): "Q1 — PAX SILICA" with a thin subtitle below: "BLOCKADED COOPERATION × FREE BUILD". Aspect ratio strictly 16:9.
```

---

## 7.2 Q2 — Bunkered AI (B+ × D+)

![Q2 Bunkered AI — 디커플링 + 환경 제약 시나리오의 헤로 이미지: 블루아워에 멈춘 메가 DC 공사장, SMR 모듈, 모라토리엄 표지와 원거리 시위 라인](../assets/07-q2-bunkered-ai.png)

**한글 캡션**: 블루아워 미 남서부의 멈춘 메가 DC 공사장 — 정지된 크레인, 펜스에 붙은 “MORATORIUM” 표지, 좌측의 SMR 모듈, 원거리 시위 라인. 두 엔지니어가 태블릿을 보는 전경이 “R2(DC 자기강화)가 B1(환경 백래시)에 의해 부분 제동되는 순간”을 압축한다.

**시각 메타포 메모**:
- 정지된 공사 + 모라토리엄 표지 = **Env-1.2 빌드 제약 + Env-2.2 수자원 갈등**
- SMR 모듈 = **Env-3.2 청정전력 PPA 폭증의 결과 (SMR 수혜)**
- 시위 라인 = **B1 환경 백래시 활성**
- 슬레이트·앰버 톤 = R1은 살아 있으나 R2가 둔화되는 “긴장된 전환기”

**생성에 사용한 영문 프롬프트**:

```text
Cinematic photorealistic wide landscape, 16:9 aspect ratio, blue-hour early evening over a dry American Southwest plain. Foreground: a half-built mega data center campus with construction halted — idle yellow construction cranes, fenced-off concrete pads, generic English-language "MORATORIUM" construction signs (no other readable text). Mid-ground left: a small modular Small Modular Reactor (SMR) cylindrical structure with steam vents, surrounded by chain-link fence. Mid-ground right: a small distant line of citizen protesters with generic cloth banners (no readable slogans, no faces). Background: dry mesa silhouettes under slate-blue and amber dusk sky, distant transmission lines and power pylons. Two engineers in hi-vis vests review a tablet in the lower-third foreground (small, back to camera, no faces). Mood: tense, constrained, transitional. Editorial photography quality, no real corporate logos, no cartoon style, no explosions or rubble, no apocalyptic imagery. Text overlay (top-left corner, clean sans-serif uppercase white text): "Q2 — BUNKERED AI" with a thin subtitle below: "BLOCKADED COOPERATION × CONSTRAINED BUILD". Aspect ratio strictly 16:9.
```

---

## 7.3 Q3 — Green Concord (B− × D+)

![Q3 Green Concord — UN/EU 글로벌 표준 수렴 + DC 청정전력 분산 시나리오의 헤로 이미지: 노르딕 피오르 트와일라잇, 풍력·SMR·태양광 통합 캠퍼스, 다국 깃발](../assets/07-q3-green-concord.png)

**한글 캡션**: 트와일라잇 피오르 풍경 — 녹화 지붕의 저층 데이터센터 캠퍼스가 풍력·SMR 모듈·태양광 어레이와 통합되어 있고, 광장에 UN·EU·미·중·인·브·캐·일 깃발이 둘러서 있다. 두 연구자가 보드워크를 따라 걷는 구도가 “경쟁적 협력 + 환경 제약 + DC 글로벌 분산”을 압축한다.

**시각 메타포 메모**:
- 다국 깃발 광장 = **P-5.1 거버넌스 수렴 (UN AI 협약 + EU AI Act 글로벌 채택)**
- 청정전력+SMR+녹화 지붕 캠퍼스 = **Env-3.2 + Env-1.2 “탄소 중립 의무 입지”**
- 노르딕 피오르 = DC 글로벌 분산 (북유럽·캐나다·아이슬란드·인도)
- 청록·에메랄드 톤 = B1이 글로벌 표준화의 형태로 고정된 “고요한 절제”

**생성에 사용한 영문 프롬프트**:

```text
Cinematic photorealistic wide landscape, 16:9 aspect ratio, blue-to-teal twilight hour over a Nordic fjord or Icelandic plateau setting. Foreground: a sleek low-rise modern data center campus integrated with the natural landscape, with green-roofed buildings, surrounded by tall offshore wind turbines on water, a single small Small Modular Reactor (SMR) cylindrical module on land, and angled solar arrays. Mid-ground: a multinational gathering of small flagpoles in a circular plaza arrangement — UN, EU, USA, China, India, Brazil, Canada, Japan flags (small but readable, no logos). Background: snow-capped mountains and a long fjord under teal and emerald twilight sky, soft mist hanging low over water. Two researchers in field jackets walk along a wooden boardwalk path (small scale, back to camera, no faces). Mood: cooperative, restrained, hopeful, technically clean, ESG-aligned. Editorial photography quality, no cartoon style, no real corporate logos, no apocalyptic imagery. Text overlay (top-left corner, clean sans-serif uppercase white text): "Q3 — GREEN CONCORD" with a thin subtitle below: "GLOBAL COOPERATION × CONSTRAINED BUILD". Aspect ratio strictly 16:9.
```

---

## 7.4 Q4 — Open Boom (B− × D−)

![Q4 Open Boom — 협력 + 자유 빌드 + 신흥 시장 폭증 시나리오의 헤로 이미지: 새벽빛 신흥 시장 스카이라인 좌측, 항만+휴머노이드 산업 라인 우측, 가운데 고가도로](../assets/07-q4-open-boom.png)

**한글 캡션**: 새벽빛 글로벌 파노라마 — 좌측 신흥 시장 스카이라인의 신규 메가 DC 공사 현장(LED 리본, 크레인), 우측 컨테이너 항만에서 작업하는 휴머노이드 산업 라인, 가운데 다양한 차량·인물이 흐르는 고가도로. “협력 + 효율 폭증 + 글로벌 자유 빌드”의 다극·확장 풍경을 압축한다.

**시각 메타포 메모**:
- 신흥 시장 스카이라인 = **신흥 시장 AI 응용 폭증 (인도·LatAm·아프리카)**
- 휴머노이드 산업 라인 = **T-4.2 AI–물리 결합 글로벌 폭발**
- 고가도로의 다양한 인물·차량 = **다극·다국적 흐름의 자유 (R1 해체)**
- 새벽 푸른·주황 톤 = R2 글로벌 모드의 “시작되는 폭증”

**생성에 사용한 영문 프롬프트**:

```text
Cinematic photorealistic wide landscape, 16:9 aspect ratio, dawn light over a global panorama composed as a single coherent vista. Left side: an Indian or Latin American tropical city skyline with new hyperscale data centers under construction, bright yellow tower cranes, glowing thin LED ribbons on building facades, busy elevated highways. Right side: an African coastal port with shipping containers stacked high and humanoid robots working in industrial assembly lines under bright work lights. Sky: blue-to-orange dawn gradient with high cirrus clouds and a faint rising sun. Mid-ground center: a wide elevated highway with diverse cars and small human figures walking (back to camera, no faces). Background: lush green mountain ranges in the distance, then ocean horizon line. Mood: expansive, optimistic, dynamic, multipolar, abundance. Editorial photography quality, no cartoon style, no real corporate logos, no explosions. Text overlay (top-left corner, clean sans-serif uppercase white text): "Q4 — OPEN BOOM" with a thin subtitle below: "GLOBAL COOPERATION × FREE BUILD". Aspect ratio strictly 16:9.
```

---

## 7.5 4장이 갈라지는 한 줄

> 4장을 동일 시리즈로 보고 한 줄씩 비교하면, 이번 시나리오 플래닝의 “세계관 분기”가 가장 압축된다.

| 축 끝 | D− 자유 빌드 | D+ 빌드 제약 |
|-------|--------------|---------------|
| **B+ 블록화** | **Q1 Pax Silica** — 동맹의 골든아워 | **Q2 Bunkered AI** — 동맹의 블루아워 |
| **B− 협력** | **Q4 Open Boom** — 글로벌 새벽 | **Q3 Green Concord** — 글로벌 트와일라잇 |

- 같은 행(B 같음): **시간대의 차이**로 환경 강도(D)를 표현 — 골든아워(자유) vs 블루/트와일라잇(제약).
- 같은 열(D 같음): **지리적 단서의 차이**로 거버넌스(B)를 표현 — 미 사막(블록) vs 글로벌 풍경(협력).
- 4장이 한 화면에 모이면 “시간대 × 지리”의 2×2가 한 번에 보인다.

---

## 7.6 다음 단계로의 인계

### 보고서 통합 (`report.md`)
- §7.1~§7.4의 4장은 6장 본문(`out/06-scenarios.md`) 각 시나리오 §1 Situation Setup 위 헤로 슬롯에 그대로 임베드 가능.
- 6장 §6.6 시나리오 비교표 위에 4장 2×2 그리드로 동시 노출하는 옵션도 검토 가능 (보고서 표지 다음 페이지 후보).

### P4 라운드 입력
- 본 장의 이미지는 P4(자본 배분자)의 “시나리오 직관”을 빠르게 잡아주는 1차 자료. §6.7 자산군 매트릭스를 함께 펼쳐 읽도록 한다.
- P4 미팅에서 “지금 이 분면에 가장 가까운 현실 신호”를 묻는 워크숍 자료로 사용.

### 후속 라운드 검토 (이번 POC 범위 외)
- **동영상 (15초 컷)**: 시나리오별 짧은 시간 경과 영상 (2026 → 2030 트랜지션). 다음 라운드에 검토.
- **부분 시나리오 인포그래픽**: §6.6 비교표·§6.7 자산 매트릭스를 별도 시각으로. 7장에 추가 슬롯 가능.
- **트렌드별 카드 시각**: 5장 14개 카드 중 Top 5를 작은 일러스트 카드로 시리즈화하는 옵션.

### 본 장의 한계
- 이미지 모델은 한글 텍스트 처리에 한계가 있어 본 장 이미지 내부는 영문만 사용. 한글 표제는 마크다운 캡션에 의존.
- 사실적 미래 풍경 톤은 “구체적 행동을 직관적으로 떠올리게 하지만” 정량 분석을 대체하지 않는다. §6.7 자산 매트릭스·§6.5 확률 표와 함께 봐야 의사결정에 직결된다.
- 4장 모두 “단일 장면” 압축이므로, 시나리오의 시간 진행(§6.x.6 Critical Events 시간선)은 여기에 담기지 않았다 — 후속 라운드의 동영상·시간경과 인포그래픽이 그 역할을 한다.
