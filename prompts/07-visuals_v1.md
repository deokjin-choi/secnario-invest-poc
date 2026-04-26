# 제7장 — Scenario 시각화 프롬프트 (v2)

> **v1 → v2 변경 요지**
> 1. 옵션 A에 맞춰 **4 시나리오 모두** 이미지화 (Q1~Q4).
> 2. 스타일 고정: **사실적 미래 풍경 (cinematic photoreal)**.
> 3. **종횡비 16:9 정확히** (보고서·덱 헤로 슬롯 기준).
> 4. 이미지 내 **시나리오명(영문)** + **핵심 컨셉 부제** 1줄을 명시 표기. (한글 캡션은 마크다운에서 별도 처리)
> 5. 동일 포맷·동일 톤으로 4장이 한 시리즈로 보이도록 **공통 시각 규칙** 명시.

# 공통 시각 규칙 (모든 시나리오에 동일 적용)

| 항목 | 값 |
|------|----|
| **종횡비** | 16:9 (정확히) |
| **스타일** | 사실적 미래 풍경 (cinematic photorealistic, editorial-grade) |
| **시점·구도** | 와이드 풍경 / 약간 부감 / 깊이감 있는 1점 또는 2점 투시 |
| **시간대** | Q1·Q4 = 골든아워(낙관·확장), Q2·Q3 = 블루아워·이른 저녁(억제·전환) |
| **색감** | Q1 황금·청동 톤 / Q2 슬레이트·앰버 톤 / Q3 청록·에메랄드 톤 / Q4 푸른 새벽·해 뜸 톤 |
| **포함 요소** | 데이터센터 / 전력 인프라 / 인간 스케일 인물 1~2명(작게) / 지역적 단서(스카이라인·자연·국기·플래카드 등 시나리오별 1개) |
| **텍스트 표기** | 좌상단 또는 우하단에 **시나리오명(영문 대문자) + 부제 1줄** — `Q? — SCENARIO NAME / Subtitle`. 다른 텍스트·로고·실제 회사명·실제 인물 얼굴은 금지 |
| **금지** | 만화·애니풍·과장된 SF·디스토피아 클리셰(폭발·잔해), 텍스트 다중·워터마크, 실존 인물·로고·상표 |
| **출력** | PNG, 보고서 헤로 품질, `assets/07-q?-<scenario-slug>.png` |

> **이미지 내 텍스트 가이드**: 영문만, 산세리프 대문자(예: HELVETICA/INTER 톤), 한 행 또는 두 행. 한글은 이미지 모델이 깨뜨릴 가능성이 커서 **마크다운 캡션**에서 처리.

# 시나리오별 프롬프트

## Q1 — Pax Silica  (B+ × D−)
- **핵심 메시지**: 미·동맹 컴퓨트 우위 + DC 자유 빌드. R1+R2 동시 우상향.
- **시각 메타포**: 사막 분지에 줄지어 빛나는 메가 데이터센터 단지, 미국·동맹국 깃발, 골든아워.
- **이미지 텍스트 (영문)**: `Q1 — PAX SILICA` / `Blockaded Cooperation × Free Build`
- **이미지 프롬프트 (영문)**:
  ```
  Cinematic photorealistic wide landscape, 16:9, golden-hour late afternoon light over a vast Arizona-style desert basin. Foreground: a sweeping row of massive hyperscale data center campuses with cooling towers, transmission lines, and high-voltage substations stretching to the horizon. Mid-ground: a tightly grouped cluster of American and allied flags (USA, Japan, South Korea, Taiwan, EU) standing on a low ridge — small but readable, no logos. Two human figures in business attire (small scale, back to camera) observe from a vantage point. Sky: warm amber and bronze tones, light haze, subtle volumetric light. Mood: confident, ascendant, ordered. Ground: cracked desert clay with sparse vegetation. Composition: 1-point perspective drawing eye to the horizon. Editorial photography quality, no people's faces, no real corporate logos, no cartoon style. Text overlay (top-left, sans-serif uppercase, clean white): "Q1 — PAX SILICA" with a thin subtitle below: "BLOCKADED COOPERATION × FREE BUILD". Aspect ratio strictly 16:9.
  ```
- **출력 파일**: `assets/07-q1-pax-silica.png`

## Q2 — Bunkered AI  (B+ × D+)
- **핵심 메시지**: 디커플링 + 환경 압박. 효율·소형화·SMR로 우회.
- **시각 메타포**: 미국 텍사스/애리조나 풍경에 환경평가 모라토리엄 표지·SMR 모듈, 환경 시위 라인, 블루아워.
- **이미지 텍스트 (영문)**: `Q2 — BUNKERED AI` / `Blockaded Cooperation × Constrained Build`
- **이미지 프롬프트 (영문)**:
  ```
  Cinematic photorealistic wide landscape, 16:9, blue-hour early evening over a dry American Southwest plain. Foreground: a half-built mega data center campus with construction halted — idle cranes, fenced-off pads, "moratorium" style construction signs (English text only, generic). Mid-ground left: a small modular Small Modular Reactor (SMR) cylindrical structure with steam vents, surrounded by chain-link fence. Mid-ground right: a small line of citizen protesters in the distance with generic banners (no readable slogans, no faces). Background: dry mesa silhouettes under slate-blue and amber dusk sky, distant transmission lines. Two engineers in hi-vis vests review a tablet in the lower-third foreground (small, back to camera, no faces). Mood: tense, constrained, transitional. Editorial photography quality, no real corporate logos, no cartoon style, no explosions or rubble. Text overlay (top-left, sans-serif uppercase, clean white): "Q2 — BUNKERED AI" with a thin subtitle below: "BLOCKADED COOPERATION × CONSTRAINED BUILD". Aspect ratio strictly 16:9.
  ```
- **출력 파일**: `assets/07-q2-bunkered-ai.png`

## Q3 — Green Concord  (B− × D+)
- **시각 메타포**: 노르웨이/아이슬란드/캐나다 같은 청정전력 가용지에 분산된 데이터센터, 풍력·SMR·재생 인프라, 글로벌 깃발 통합 게이트, 청록 에메랄드 톤.
- **핵심 메시지**: UN/EU 표준 글로벌 수렴, DC 청정전력 가용지로 글로벌 분산.
- **이미지 텍스트 (영문)**: `Q3 — GREEN CONCORD` / `Global Cooperation × Constrained Build`
- **이미지 프롬프트 (영문)**:
  ```
  Cinematic photorealistic wide landscape, 16:9, blue-to-teal hour over a Nordic fjord or Icelandic plateau. Foreground: a sleek low-rise data center campus integrated with the landscape, surrounded by offshore wind turbines, a small SMR module, and solar arrays. Mid-ground: a multinational gathering of flags — UN, EU, USA, China, India, Brazil, Canada, Japan — arranged around a circular plaza (small, readable, no logos). Background: snow-capped mountains and a fjord under teal-emerald twilight, soft mist. Two researchers in field jackets walk along a path (small scale, back to camera, no faces). Mood: cooperative, restrained, hopeful, technically clean. Editorial photography quality, no cartoon style, no real corporate logos. Text overlay (top-left, sans-serif uppercase, clean white): "Q3 — GREEN CONCORD" with a thin subtitle below: "GLOBAL COOPERATION × CONSTRAINED BUILD". Aspect ratio strictly 16:9.
  ```
- **출력 파일**: `assets/07-q3-green-concord.png`

## Q4 — Open Boom  (B− × D−)
- **시각 메타포**: 글로벌 빌드 폭증 — 인도·LatAm·아프리카 신흥 시장 데이터센터, 휴머노이드 산업 라인, 새벽빛 폭발적 확장.
- **핵심 메시지**: 협력 + 효율로 AI 글로벌 무한 확장. R2 글로벌 모드 폭주.
- **이미지 텍스트 (영문)**: `Q4 — OPEN BOOM` / `Global Cooperation × Free Build`
- **이미지 프롬프트 (영문)**:
  ```
  Cinematic photorealistic wide landscape, 16:9, dawn light over a global panorama composed as a single coherent vista — left side an Indian/LatAm tropical city skyline with new hyperscale data centers under construction (cranes, glowing LED ribbons), right side an African coastal port with shipping containers and humanoid robots working in industrial lines. Sky: blue-to-orange dawn with high cirrus clouds and a faint sun. Mid-ground center: a wide elevated highway with diverse vehicles and small human figures (back to camera, no faces). Background: lush green mountains, then ocean horizon. Mood: expansive, optimistic, dynamic, multipolar. Editorial photography quality, no cartoon style, no real corporate logos, no explosions. Text overlay (top-left, sans-serif uppercase, clean white): "Q4 — OPEN BOOM" with a thin subtitle below: "GLOBAL COOPERATION × FREE BUILD". Aspect ratio strictly 16:9.
  ```
- **출력 파일**: `assets/07-q4-open-boom.png`

# 검수 체크
- [ ] 4장 모두 16:9 정확
- [ ] 이미지 내 영문 시나리오명·부제 1줄 표기 (`Q? — NAME` + 부제)
- [ ] 사실적 미래 풍경 톤, 만화·애니·디스토피아 클리셰 없음
- [ ] 실존 인물 얼굴·실제 회사 로고·상표 없음
- [ ] 4장이 한 시리즈로 보이도록 톤·구도가 시리즈성 있음
- [ ] 마크다운 캡션 (한글) 별도 추가 — `out/07-visuals.md`에 시나리오별 1줄 캡션과 함께 임베드

# Output (out/07-visuals.md) 구조
1. YAML 메타 + 한눈에 보기 (4장 썸네일 표)
2. §7.1 Q1 Pax Silica — 이미지 + 한글 캡션 + 시각 메타포 메모 + (생성에 사용한) 영문 프롬프트
3. §7.2 Q2 Bunkered AI — 동일 양식
4. §7.3 Q3 Green Concord — 동일 양식
5. §7.4 Q4 Open Boom — 동일 양식
6. §7.5 시리즈 비교 1줄 캡션 (4장이 어떻게 갈라지는지)
7. §7.6 다음 단계 (P4 라운드 입력 / 보고서 통합 / 한계)
