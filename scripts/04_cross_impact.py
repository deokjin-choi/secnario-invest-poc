"""04_cross_impact.py — 제4장 Cross-Impact 분석 스크립트.

입력: 인라인 14×14 매트릭스 (0~3 척도, from→to, P1·P2·P3 암묵 평균 관점)
출력:
  - assets/04-cross-impact-heatmap.png
  - assets/04-active-passive-map.png
  - 콘솔에 Active/Passive sum 및 4구역 분류 표

실행:
    # 셸
    python scripts/04_cross_impact.py

    # IPython / Jupyter
    %run scripts/04_cross_impact.py
    # 또는 cell paste 후
    main()

POC 단계의 매트릭스 값은 본 스크립트에 인라인으로 박혀 있다(재현성 위해).
값 변경 시 본 파일과 out/04-backbone.md §4.1.2 표를 함께 갱신할 것.
"""
from __future__ import annotations

from pathlib import Path
import sys
import urllib.request
from collections import Counter

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

# ---------------------------------------------------------------------------
# 한글 폰트 자동 등록 (02_iu_matrix.py와 동일 로직)
# ---------------------------------------------------------------------------
KOREAN_FONT_URL = (
    "https://github.com/google/fonts/raw/main/ofl/nanumgothic/NanumGothic-Regular.ttf"
)


def _project_root() -> Path:
    """`__file__`이 정의되지 않은 IPython cell-paste 환경에도 안전하게 동작."""
    try:
        return Path(__file__).resolve().parent.parent
    except NameError:  # pragma: no cover — IPython %run / cell paste
        return Path.cwd()


def _ensure_korean_font(project_root: Path) -> str | None:
    candidates = [
        "NanumGothic", "Nanum Gothic", "Noto Sans CJK KR", "Noto Sans KR",
        "AppleGothic", "Malgun Gothic", "Apple SD Gothic Neo",
    ]
    available = {f.name for f in fm.fontManager.ttflist}
    for name in candidates:
        if name in available:
            return name

    bundled = project_root / "assets" / "fonts" / "NanumGothic-Regular.ttf"
    if bundled.exists():
        fm.fontManager.addfont(str(bundled))
        return fm.FontProperties(fname=str(bundled)).get_name()

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
        print("       히트맵의 한글이 □로 표시될 수 있음.", file=sys.stderr)
        return None


def _setup_korean_font(project_root: Path) -> str | None:
    name = _ensure_korean_font(project_root)
    if name:
        plt.rcParams["font.sans-serif"] = [name, "DejaVu Sans"]
        plt.rcParams["axes.unicode_minus"] = False
    return name


# ---------------------------------------------------------------------------
# 14 핵심 트렌드 (out/03-core-trends.md §3.1 순서)
# ---------------------------------------------------------------------------
TRENDS: list[tuple[str, str, str]] = [
    # (id, short_label, cluster)
    ("S-4.1",   "AI 컴패니언",            "F"),
    ("T-1.1",   "미·중 모델 격차",        "B"),
    ("T-2.2",   "TSMC·미 DC 집중",        "B"),
    ("T-4.2",   "AI–물리 결합",           "A"),
    ("E-3.2",   "1/3 기업 인력 감축",     "F"),
    ("P-2.2",   "미 디레귤레이션+주",     "C"),
    ("P-3.1",   "미·중 산업 비대칭",      "B"),
    ("P-3.2",   "수출통제+자력갱생",      "B"),
    ("P-4.2",   "반도체 동맹",            "B"),
    ("Env-2.2", "추론 수자원",            "D"),
    ("P-5.1",   "G7/UN vs Paris 분열",    "C"),
    ("Env-1.2", "신규 DC 100MW+",         "D"),
    ("Env-3.2", "청정전력·SMR·PPA",       "D"),
    ("E-2.2",   "NVDA $4T·CUDA 락인",     "E"),
]
N = len(TRENDS)
IDS = [t[0] for t in TRENDS]

# ---------------------------------------------------------------------------
# Cross-Impact 매트릭스 (행 = from, 열 = to, 0~3, 대각선 0)
#
# 평가 관점: P1·P2·P3 페르소나의 암묵 평균.
# 의미:
#   0 = 영향 없음 / 1 = 약(간접·장기) / 2 = 중(직접 영향, 한정적) / 3 = 강(즉각·결정적)
# ---------------------------------------------------------------------------
M = np.array([
    # to: S41 T11 T22 T42 E32 P22 P31 P32 P42 En22 P51 En12 En32 E22
    [    0,  0,  1,  0,  0,  2,  0,  0,  0,   1,  1,   1,    0,   1 ],  # S-4.1
    [    1,  0,  2,  2,  1,  2,  3,  3,  2,   1,  2,   1,    1,   2 ],  # T-1.1
    [    0,  1,  0,  2,  0,  1,  2,  2,  3,   2,  0,   2,    2,   2 ],  # T-2.2
    [    2,  1,  1,  0,  3,  2,  1,  1,  1,   0,  0,   0,    0,   1 ],  # T-4.2
    [    1,  0,  0,  1,  0,  2,  0,  0,  0,   0,  1,   0,    0,   0 ],  # E-3.2
    [    2,  2,  2,  2,  2,  0,  1,  1,  1,   2,  2,   2,    2,   2 ],  # P-2.2
    [    1,  3,  2,  2,  1,  2,  0,  3,  3,   0,  3,   1,    1,   2 ],  # P-3.1
    [    0,  3,  2,  2,  0,  1,  3,  0,  3,   0,  2,   1,    0,   2 ],  # P-3.2
    [    0,  2,  3,  1,  0,  1,  3,  3,  0,   1,  2,   2,    1,   1 ],  # P-4.2
    [    0,  0,  2,  0,  0,  2,  0,  0,  1,   0,  1,   2,    1,   1 ],  # Env-2.2
    [    1,  2,  1,  1,  0,  2,  2,  2,  2,   0,  0,   0,    1,   0 ],  # P-5.1
    [    0,  1,  3,  1,  0,  2,  1,  0,  1,   3,  1,   0,    3,   2 ],  # Env-1.2
    [    0,  0,  2,  0,  0,  2,  0,  0,  0,   1,  1,   2,    0,   0 ],  # Env-3.2
    [    1,  2,  2,  1,  0,  2,  2,  2,  1,   0,  1,   2,    0,   0 ],  # E-2.2
], dtype=int)


CLUSTER_COLORS = {
    "A": "#7e6cf0", "B": "#e74c3c", "C": "#f39c12",
    "D": "#27ae60", "E": "#16a085", "F": "#7f8c8d",
}


# ---------------------------------------------------------------------------
# 분류 / 계산
# ---------------------------------------------------------------------------
def compute_sums(matrix: np.ndarray) -> tuple[np.ndarray, np.ndarray, float, float]:
    if matrix.shape != (N, N):
        raise ValueError(f"matrix shape must be {N}x{N}, got {matrix.shape}")
    if not (np.diag(matrix) == 0).all():
        raise ValueError("대각선은 0 이어야 함")

    a = matrix.sum(axis=1)
    p = matrix.sum(axis=0)
    return a, p, float(np.median(a)), float(np.median(p))


def classify(a: int, p: int, med_a: float, med_p: float) -> str:
    if a > med_a and p <= med_p:
        return "Driving"
    if a > med_a and p > med_p:
        return "Critical"
    if a <= med_a and p > med_p:
        return "Dependent"
    return "Inert"


def print_summary(a: np.ndarray, p: np.ndarray, med_a: float, med_p: float) -> None:
    print(f"[info] median(A) = {med_a:.1f}, median(P) = {med_p:.1f}")
    print()
    print(f"{'ID':<8}{'A':>4}{'P':>4}{'A-P':>5}{'A+P':>5}  Class")
    print("-" * 40)
    for i, (tid, _, _) in enumerate(TRENDS):
        cls = classify(int(a[i]), int(p[i]), med_a, med_p)
        print(f"{tid:<8}{int(a[i]):>4}{int(p[i]):>4}{int(a[i]-p[i]):>+5}{int(a[i]+p[i]):>5}  {cls}")

    counts = Counter(
        classify(int(a[i]), int(p[i]), med_a, med_p) for i in range(N)
    )
    print()
    print("[summary] 4구역 분포:")
    for k in ["Driving", "Critical", "Dependent", "Inert"]:
        print(f"  {k:<10} : {counts.get(k, 0)}개")


# ---------------------------------------------------------------------------
# 시각화
# ---------------------------------------------------------------------------
def plot_heatmap(matrix: np.ndarray, out_path: Path) -> Path:
    fig, ax = plt.subplots(figsize=(11.5, 9.5))
    im = ax.imshow(matrix, cmap="YlOrRd", vmin=0, vmax=3, aspect="auto")
    ax.set_xticks(range(N))
    ax.set_yticks(range(N))
    ax.set_xticklabels(IDS, rotation=45, ha="right", fontsize=9)
    ax.set_yticklabels(IDS, fontsize=9)
    ax.set_xlabel("To (영향을 받는 트렌드)", fontsize=11)
    ax.set_ylabel("From (영향을 주는 트렌드)", fontsize=11)
    ax.set_title("Cross-Impact 매트릭스 (14×14, 0~3, P1·P2·P3 평균 관점)",
                 fontsize=12, pad=14)

    for i in range(N):
        for j in range(N):
            if i == j:
                ax.text(j, i, "—", ha="center", va="center", color="#888", fontsize=8)
            else:
                v = int(matrix[i, j])
                color = "white" if v >= 2 else "#222"
                ax.text(j, i, str(v), ha="center", va="center",
                        color=color, fontsize=8)

    cbar = plt.colorbar(im, ax=ax, shrink=0.8, label="영향 강도 (0~3)")
    cbar.set_ticks([0, 1, 2, 3])

    fig.tight_layout()
    out_path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(out_path, dpi=150, bbox_inches="tight")
    plt.close(fig)
    return out_path


def plot_active_passive(
    a: np.ndarray, p: np.ndarray, med_a: float, med_p: float, out_path: Path,
) -> Path:
    fig, ax = plt.subplots(figsize=(11, 9))

    for i, (tid, _, cluster) in enumerate(TRENDS):
        color = CLUSTER_COLORS.get(cluster, "#333")
        ax.scatter(p[i], a[i], s=180, color=color, alpha=0.85,
                   edgecolors="black", linewidths=1.0, zorder=3)
        ax.annotate(tid, xy=(p[i], a[i]), xytext=(6, 6),
                    textcoords="offset points",
                    fontsize=9.5, fontweight="bold", zorder=4)

    ax.axvline(med_p, color="#333", linestyle="--", linewidth=1.0, alpha=0.5)
    ax.axhline(med_a, color="#333", linestyle="--", linewidth=1.0, alpha=0.5)

    xmin, xmax = float(p.min()) - 2, float(p.max()) + 2
    ymin, ymax = float(a.min()) - 2, float(a.max()) + 2
    ax.set_xlim(xmin, xmax)
    ax.set_ylim(ymin, ymax)

    ax.text(xmin + 0.5, ymax - 1.5, "Driving\n(高 A · 低 P)",
            fontsize=11, color="#c0392b", fontweight="bold", alpha=0.85)
    ax.text(xmax - 4.5, ymax - 1.5, "Critical\n(高 A · 高 P)\n[피드백 중심]",
            fontsize=11, color="#8e44ad", fontweight="bold", alpha=0.85)
    ax.text(xmin + 0.5, ymin + 1.0, "Inert\n(低 A · 低 P)",
            fontsize=11, color="#7f8c8d", fontweight="bold", alpha=0.85)
    ax.text(xmax - 4.5, ymin + 1.0, "Dependent\n(低 A · 高 P)",
            fontsize=11, color="#16a085", fontweight="bold", alpha=0.85)

    ax.set_xlabel(f"Passive Sum (P, 열 합) — Dependency 강도   [median = {med_p:.1f}]",
                  fontsize=11)
    ax.set_ylabel(f"Active Sum (A, 행 합) — Driving 강도   [median = {med_a:.1f}]",
                  fontsize=11)
    ax.set_title("Active–Passive Map — 14 핵심 트렌드 4구역 분류",
                 fontsize=12, pad=14)
    ax.grid(True, linestyle=":", alpha=0.4, zorder=1)

    handles = [
        plt.Line2D([0], [0], marker="o", color="w",
                   markerfacecolor=CLUSTER_COLORS[c], markersize=11,
                   markeredgecolor="black", label=f"클러스터 {c}")
        for c in ["A", "B", "C", "D", "E", "F"]
    ]
    ax.legend(handles=handles, loc="lower center", bbox_to_anchor=(0.5, -0.16),
              ncol=6, frameon=False, fontsize=10)

    fig.tight_layout()
    out_path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(out_path, dpi=150, bbox_inches="tight")
    plt.close(fig)
    return out_path


# ---------------------------------------------------------------------------
# main
# ---------------------------------------------------------------------------
def main() -> tuple[Path, Path]:
    project_root = _project_root()
    _setup_korean_font(project_root)

    a, p, med_a, med_p = compute_sums(M)
    print_summary(a, p, med_a, med_p)

    assets_dir = project_root / "assets"
    heatmap_path = assets_dir / "04-cross-impact-heatmap.png"
    ap_path = assets_dir / "04-active-passive-map.png"

    saved_heatmap = plot_heatmap(M, heatmap_path)
    print(f"[ok] saved: {saved_heatmap}")

    saved_ap = plot_active_passive(a, p, med_a, med_p, ap_path)
    print(f"[ok] saved: {saved_ap}")

    return saved_heatmap, saved_ap


if __name__ == "__main__":
    # Plain `main()` — avoids IPython's "SystemExit: 0" warning when
    # running via `%run` or cell-paste in Jupyter.
    main()
