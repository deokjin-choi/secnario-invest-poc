"""
2장 — Impact–Uncertainty 매트릭스 시각화 스크립트.

입력: out/02-impact-uncertainty.md 의 §2.3.1 평가표(이 파일에 dict로 임베드).
출력: assets/02-iu-matrix.png

사용법 (이미 matplotlib/numpy 가 있는 conda 환경에서):
    python scripts/02_iu_matrix.py

원칙:
- MD가 단일 출처 (Source of Truth). 본 스크립트는 그 결과를 시각화하는 파생물.
- 평가가 바뀌면 MD 표를 먼저 수정하고, 본 파일 하단 DATA dict를 동기화한 뒤 재실행한다.
"""

from __future__ import annotations

import sys
import urllib.request
from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from matplotlib.patches import Rectangle


# ------------------------------------------------------------------
# 1) 데이터 (out/02-impact-uncertainty.md §2.3.1 평가표와 동일해야 함)
# 형식: factor_id -> (P1_I, P1_U, P2_I, P2_U, P3_I, P3_U, domain)
# ------------------------------------------------------------------
DATA: dict[str, tuple[int, int, int, int, int, int, str]] = {
    # Social
    "S-1.1": (5, 2, 4, 4, 5, 3, "Social"),
    "S-1.2": (4, 2, 5, 4, 4, 4, "Social"),
    "S-2.1": (5, 1, 4, 3, 5, 2, "Social"),
    "S-2.2": (4, 2, 3, 4, 5, 3, "Social"),
    "S-3.1": (2, 3, 5, 4, 4, 4, "Social"),
    "S-3.2": (2, 3, 4, 4, 3, 4, "Social"),
    "S-4.1": (4, 2, 5, 5, 4, 4, "Social"),
    "S-4.2": (2, 3, 5, 3, 4, 3, "Social"),
    "S-5.1": (5, 2, 4, 4, 4, 3, "Social"),
    "S-5.2": (4, 2, 3, 4, 3, 4, "Social"),
    # Technological
    "T-1.1": (5, 3, 5, 5, 4, 4, "Tech"),
    "T-1.2": (5, 2, 4, 3, 4, 3, "Tech"),
    "T-2.1": (5, 2, 4, 4, 3, 3, "Tech"),
    "T-2.2": (4, 3, 5, 5, 3, 4, "Tech"),
    "T-3.1": (5, 2, 5, 4, 5, 4, "Tech"),
    "T-3.2": (3, 3, 2, 3, 4, 5, "Tech"),
    "T-4.1": (4, 2, 5, 4, 3, 3, "Tech"),
    "T-4.2": (5, 3, 4, 4, 4, 4, "Tech"),
    "T-5.1": (2, 3, 5, 4, 3, 3, "Tech"),
    "T-5.2": (3, 3, 5, 4, 2, 3, "Tech"),
    # Economic
    "E-1.1": (4, 3, 4, 4, 2, 3, "Econ"),
    "E-1.2": (4, 3, 5, 4, 3, 3, "Econ"),
    "E-2.1": (5, 2, 4, 4, 3, 3, "Econ"),
    "E-2.2": (5, 2, 5, 4, 3, 4, "Econ"),
    "E-3.1": (4, 2, 5, 4, 4, 3, "Econ"),
    "E-3.2": (4, 3, 4, 4, 4, 4, "Econ"),
    "E-4.1": (5, 2, 3, 3, 5, 3, "Econ"),
    "E-4.2": (3, 3, 4, 4, 4, 4, "Econ"),
    "E-5.1": (3, 3, 4, 3, 2, 3, "Econ"),
    "E-5.2": (5, 2, 4, 4, 3, 3, "Econ"),
    # Environmental
    "Env-1.1": (4, 3, 5, 4, 3, 3, "Env"),
    "Env-1.2": (4, 3, 5, 5, 2, 3, "Env"),
    "Env-2.1": (2, 3, 5, 4, 2, 3, "Env"),
    "Env-2.2": (2, 3, 5, 5, 2, 3, "Env"),
    "Env-3.1": (5, 2, 3, 3, 3, 3, "Env"),
    "Env-3.2": (4, 3, 5, 5, 2, 3, "Env"),
    "Env-4.1": (5, 2, 3, 3, 4, 3, "Env"),
    "Env-4.2": (4, 3, 3, 3, 4, 3, "Env"),
    # Political
    "P-1.1": (3, 3, 5, 4, 2, 3, "Pol"),
    "P-1.2": (4, 3, 5, 4, 2, 3, "Pol"),
    "P-2.1": (3, 3, 5, 4, 4, 3, "Pol"),
    "P-2.2": (4, 3, 5, 5, 3, 4, "Pol"),
    "P-3.1": (5, 3, 5, 5, 4, 4, "Pol"),
    "P-3.2": (4, 3, 5, 5, 3, 4, "Pol"),
    "P-4.1": (3, 3, 5, 4, 4, 3, "Pol"),
    "P-4.2": (4, 3, 5, 5, 3, 4, "Pol"),
    "P-5.1": (2, 3, 5, 5, 2, 3, "Pol"),
    "P-5.2": (3, 3, 5, 4, 2, 3, "Pol"),
}

DOMAIN_COLORS = {
    "Social": "#4C78A8",
    "Tech":   "#F58518",
    "Econ":   "#54A24B",
    "Env":    "#72B7B2",
    "Pol":    "#B279A2",
}


# ------------------------------------------------------------------
# 2) 한글 폰트 설정
# 우선순위: ① 이미 등록된 한글 폰트 → ② 잘 알려진 디스크 경로의 .ttf →
#           ③ assets/fonts/NanumGothic-Regular.ttf 자동 다운로드
# ------------------------------------------------------------------
KOREAN_FONT_URL = (
    "https://github.com/google/fonts/raw/main/ofl/nanumgothic/"
    "NanumGothic-Regular.ttf"
)
KOREAN_FAMILY_CANDIDATES = [
    "NanumGothic", "Nanum Gothic", "NanumBarunGothic",
    "Noto Sans CJK KR", "Noto Sans KR",
    "UnDotum", "Baekmuk Dotum",
    "Malgun Gothic",   # Windows
    "AppleGothic",     # macOS
]


def _ensure_korean_font(project_root: Path) -> str | None:
    """Locate (or download) a Korean font and return its family name.

    Returns ``None`` only if all attempts (cache lookup, disk scan,
    download) fail; in that case the caller falls back to DejaVu Sans
    and Korean glyphs render as missing-glyph boxes.
    """
    available = {f.name for f in fm.fontManager.ttflist}
    for name in KOREAN_FAMILY_CANDIDATES:
        if name in available:
            return name

    bundled = project_root / "assets" / "fonts" / "NanumGothic-Regular.ttf"
    candidate_paths = [
        bundled,
        Path.home() / ".fonts" / "NanumGothic.ttf",
        Path.home() / ".local" / "share" / "fonts" / "NanumGothic.ttf",
        Path("/usr/share/fonts/truetype/nanum/NanumGothic.ttf"),
        Path("/usr/share/fonts/opentype/nanum/NanumGothic.ttf"),
        Path("/usr/share/fonts/nanum/NanumGothic.ttf"),
    ]
    for p in candidate_paths:
        if p.exists():
            fm.fontManager.addfont(str(p))
            return fm.FontProperties(fname=str(p)).get_name()

    try:
        bundled.parent.mkdir(parents=True, exist_ok=True)
        print(f"[info] Korean font not found. Downloading NanumGothic to "
              f"{bundled} (one-time, ~4MB) ...")
        urllib.request.urlretrieve(KOREAN_FONT_URL, str(bundled))
        fm.fontManager.addfont(str(bundled))
        name = fm.FontProperties(fname=str(bundled)).get_name()
        print(f"[ok] registered: {name}")
        return name
    except Exception as exc:  # pragma: no cover — network/filesystem
        print(f"[warn] Korean font download failed: {exc}", file=sys.stderr)
        print(
            "[warn] Korean text will render as missing-glyph boxes.\n"
            "       Fix options:\n"
            "         (a) sudo apt install fonts-nanum  (system-wide)\n"
            f"         (b) place any Korean .ttf at {bundled}",
            file=sys.stderr,
        )
        return None


def _setup_korean_font(project_root: Path) -> None:
    name = _ensure_korean_font(project_root)
    if name:
        # Put Korean family at the head of the sans-serif list so ASCII
        # still has DejaVu Sans as a metric-compatible fallback.
        plt.rcParams["font.family"] = "sans-serif"
        plt.rcParams["font.sans-serif"] = [name, "DejaVu Sans"]
    plt.rcParams["axes.unicode_minus"] = False


# ------------------------------------------------------------------
# 3) 통계 계산
# ------------------------------------------------------------------
def _compute_stats() -> list[dict]:
    rows: list[dict] = []
    for fid, (p1i, p1u, p2i, p2u, p3i, p3u, dom) in DATA.items():
        i_scores = np.array([p1i, p2i, p3i], dtype=float)
        u_scores = np.array([p1u, p2u, p3u], dtype=float)
        mean_i = float(i_scores.mean())
        mean_u = float(u_scores.mean())
        std_i = float(i_scores.std(ddof=0))
        std_u = float(u_scores.std(ddof=0))
        spread = std_i + std_u
        rows.append({
            "id": fid, "domain": dom,
            "mean_i": mean_i, "mean_u": mean_u,
            "std_i": std_i, "std_u": std_u, "spread": spread,
            "raw": {"P1": (p1i, p1u), "P2": (p2i, p2u), "P3": (p3i, p3u)},
        })
    rows.sort(key=lambda r: r["spread"], reverse=True)
    return rows


# ------------------------------------------------------------------
# 4) 시각화
# ------------------------------------------------------------------
def plot(rows: list[dict], out_path: Path, top_k: int = 5) -> Path:
    fig, ax = plt.subplots(figsize=(13, 10))

    # 사분면 배경 색
    cuts_i, cuts_u = 3.5, 3.5
    ax.add_patch(Rectangle((cuts_i, cuts_u), 5.5 - cuts_i, 5.5 - cuts_u,
                           facecolor="#FDECEC", alpha=0.5, zorder=0))  # Q1 분기변수
    ax.add_patch(Rectangle((cuts_i, 0.5), 5.5 - cuts_i, cuts_u - 0.5,
                           facecolor="#E8F5E9", alpha=0.5, zorder=0))  # 공통가정
    ax.add_patch(Rectangle((0.5, cuts_u), cuts_i - 0.5, 5.5 - cuts_u,
                           facecolor="#FFF8E1", alpha=0.5, zorder=0))  # 모니터링
    ax.add_patch(Rectangle((0.5, 0.5), cuts_i - 0.5, cuts_u - 0.5,
                           facecolor="#F5F5F5", alpha=0.5, zorder=0))  # 백그라운드

    # 사분면 경계선
    ax.axvline(cuts_i, color="#888", lw=1.0, ls="--", zorder=1)
    ax.axhline(cuts_u, color="#888", lw=1.0, ls="--", zorder=1)

    # 사분면 라벨
    ax.text(5.45, 5.45, "Q1 분기 변수 후보\n(고임팩트·고불확실성)",
            ha="right", va="top", color="#B71C1C", fontsize=10, fontweight="bold")
    ax.text(5.45, 0.55, "Q2 공통 가정\n(고임팩트·저불확실성)",
            ha="right", va="bottom", color="#1B5E20", fontsize=10, fontweight="bold")
    ax.text(0.55, 5.45, "Q3 모니터링\n(저임팩트·고불확실성)",
            ha="left", va="top", color="#7E5A00", fontsize=10, fontweight="bold")
    ax.text(0.55, 0.55, "Q4 배경\n(저임팩트·저불확실성)",
            ha="left", va="bottom", color="#555", fontsize=10, fontweight="bold")

    # 분산 상위 K개 식별
    top_ids = {r["id"] for r in rows[:top_k]}

    # 점/라벨 그리기 (도메인별 색)
    for r in rows:
        is_top = r["id"] in top_ids
        color = DOMAIN_COLORS[r["domain"]]
        if is_top:
            # 분산이 큰 항목: 빨간 별 + 굵은 라벨 + min/max 박스(스프레드 시각화)
            i_min = min(r["raw"]["P1"][0], r["raw"]["P2"][0], r["raw"]["P3"][0])
            i_max = max(r["raw"]["P1"][0], r["raw"]["P2"][0], r["raw"]["P3"][0])
            u_min = min(r["raw"]["P1"][1], r["raw"]["P2"][1], r["raw"]["P3"][1])
            u_max = max(r["raw"]["P1"][1], r["raw"]["P2"][1], r["raw"]["P3"][1])
            ax.add_patch(Rectangle((i_min, u_min), i_max - i_min, u_max - u_min,
                                   facecolor="none", edgecolor="#C62828", lw=1.0,
                                   ls=":", alpha=0.8, zorder=2))
            ax.scatter(r["mean_i"], r["mean_u"], s=200, marker="*",
                       c="#C62828", edgecolors="black", linewidths=0.8, zorder=4)
            ax.annotate(r["id"], (r["mean_i"], r["mean_u"]),
                        xytext=(7, 7), textcoords="offset points",
                        fontsize=10, fontweight="bold", color="#B71C1C", zorder=5)
        else:
            ax.scatter(r["mean_i"], r["mean_u"], s=55, marker="o",
                       c=color, edgecolors="black", linewidths=0.4, alpha=0.9, zorder=3)
            ax.annotate(r["id"], (r["mean_i"], r["mean_u"]),
                        xytext=(5, 4), textcoords="offset points",
                        fontsize=8, color="#222", zorder=4)

    # 도메인 범례 (작은 점 + 텍스트)
    legend_handles = [
        plt.Line2D([0], [0], marker="o", color="w", markerfacecolor=c,
                   markeredgecolor="black", markersize=8, label=d)
        for d, c in DOMAIN_COLORS.items()
    ]
    legend_handles.append(
        plt.Line2D([0], [0], marker="*", color="w", markerfacecolor="#C62828",
                   markeredgecolor="black", markersize=14,
                   label=f"분산 상위 {top_k} (P1·P2·P3)")
    )
    ax.legend(handles=legend_handles, loc="upper left", fontsize=9, framealpha=0.95)

    # 축
    ax.set_xlim(0.5, 5.5)
    ax.set_ylim(0.5, 5.5)
    ax.set_xticks([1, 2, 3, 4, 5])
    ax.set_yticks([1, 2, 3, 4, 5])
    ax.set_xlabel("Impact (영향도) — 평균 (P1+P2+P3) / 3", fontsize=11)
    ax.set_ylabel("Uncertainty (불확실성) — 평균 (P1+P2+P3) / 3", fontsize=11)
    ax.set_title("Impact–Uncertainty Matrix — 48 Factors\n"
                 "(P4 제외 / 분산 상위 5개는 빨간 별 + 점선 박스)", fontsize=13)
    ax.grid(True, alpha=0.25, zorder=0)
    fig.tight_layout()

    out_path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(out_path, dpi=150, bbox_inches="tight")
    plt.close(fig)
    return out_path


# ------------------------------------------------------------------
# 5) Main
# ------------------------------------------------------------------
def _project_root() -> Path:
    """Resolve project root in both `python script.py` and `%run` modes."""
    try:
        return Path(__file__).resolve().parent.parent
    except NameError:  # pragma: no cover — IPython %run / cell paste
        return Path.cwd()


def main() -> Path:
    project_root = _project_root()
    _setup_korean_font(project_root)
    rows = _compute_stats()

    print(f"[info] factors loaded: {len(rows)}")
    print("[info] top-5 by persona spread (std_I + std_U):")
    for r in rows[:5]:
        print(f"  - {r['id']:<8} {r['domain']:<6} "
              f"mean_I={r['mean_i']:.2f} mean_U={r['mean_u']:.2f} "
              f"spread={r['spread']:.2f}")

    out_path = project_root / "assets" / "02-iu-matrix.png"
    saved = plot(rows, out_path, top_k=5)
    print(f"[ok] saved: {saved}")
    return saved


if __name__ == "__main__":
    # Plain `main()` — avoids IPython's "SystemExit: 0" warning when
    # the script is executed via %run inside a notebook/REPL.
    main()
