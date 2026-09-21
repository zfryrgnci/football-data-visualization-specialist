import json
import os
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from mplsoccer import VerticalPitch

os.makedirs("visuals", exist_ok=True)

plt.rcParams["font.family"] = "Segoe UI"
plt.rcParams["font.sans-serif"] = ["Segoe UI", "Arial", "DejaVu Sans"]

with open("data/gornik_match_events.json", "r", encoding="utf-8") as f:
    match_data = json.load(f)

# ==============================================================================
# 10. MATCH SHOT MAP & xG CONSTELLATION
# ==============================================================================
def create_shot_map():
    pitch = VerticalPitch(half=True, pitch_type="statsbomb", pitch_color="#0f172a", line_color="#334155", linewidth=1.2, goal_type="box")
    fig, ax = pitch.draw(figsize=(9.5, 10.5), constrained_layout=False)
    fig.set_facecolor("#0f172a")

    g_shots = match_data["gornik_shots"]

    outcome_colors = {
        "Goal": "#10b981",       # Emerald Green
        "Saved": "#38bdf8",      # Sky Blue
        "Blocked": "#f59e0b",    # Amber
        "Off Target": "#64748b"  # Slate
    }

    for s in g_shots:
        size = s["xG"] * 700 + 70
        color = outcome_colors.get(s["outcome"], "#cbd5e1")
        pitch.scatter(s["x"], s["y"], s=size, color=color, edgecolors="#ffffff",
                      linewidth=2.0 if s["outcome"] == "Goal" else 1.0, alpha=0.9, ax=ax, zorder=4)

        if s["outcome"] == "Goal":
            pitch.annotate(f"GOAL {s['minute']}'\n{s['player']} ({s['xG']:.2f} xG)",
                           (s["x"] - 2.8, s["y"]), color="#ffffff",
                           fontsize=9, fontweight="bold", ha="center", va="top",
                           bbox=dict(boxstyle="round,pad=0.25", facecolor="#065f46", edgecolor="#10b981", lw=1.5),
                           ax=ax, zorder=6)

    # Clean Match Summary Card top-right
    summary_box = (
        "MATCH SUMMARY: GÓRNIK 2 - 1 LEGIA\n"
        "Arena Zabrze | Ekstraklasa 2025-2026\n"
        "-----------------------------------\n"
        "Metric                 Górnik  Legia\n"
        "Shots (On Target)      14 (5)  10 (4)\n"
        "Expected Goals (xG)     2.15    1.18\n"
        "xG per Shot            0.154   0.118\n"
        "Big Chances                3       1\n"
        "Field Tilt %           54.2%   45.8%"
    )
    ax.text(78, 62, summary_box, fontfamily="Consolas", fontsize=8.5, color="#cbd5e1", va="top",
            bbox=dict(boxstyle="round,pad=0.4", facecolor="#1e293b", edgecolor="#475569", lw=1.2, alpha=0.95))

    # Legend for outcomes
    fig.text(0.18, 0.08, "● Goal", color="#10b981", fontsize=10.5, fontweight="bold")
    fig.text(0.36, 0.08, "● Saved", color="#38bdf8", fontsize=10.5, fontweight="bold")
    fig.text(0.53, 0.08, "● Blocked", color="#f59e0b", fontsize=10.5, fontweight="bold")
    fig.text(0.72, 0.08, "● Off Target", color="#64748b", fontsize=10.5, fontweight="bold")

    fig.text(0.12, 0.965, "GÓRNIK ZABRZE | SHOT MAP & xG CONSTELLATION", fontsize=15, fontweight="bold", color="#f8fafc")
    fig.text(0.12, 0.940, "Fixture: Górnik Zabrze 2-1 Legia Warszawa | 14 Shots, 2.15 xG Created", fontsize=10.5, color="#94a3b8")
    fig.text(0.88, 0.02, "Bubble size proportional to Expected Goals (xG) | Visualization by Zafer Yorganci", ha="right", fontsize=8.5, color="#64748b")

    plt.savefig("visuals/10_match_shot_map_xg_constellation.png", dpi=300, bbox_inches="tight", facecolor="#0f172a")
    plt.close()
    print("Generated visuals/10_match_shot_map_xg_constellation.png")

# ==============================================================================
# 11. CUMULATIVE xG FLOW & GAME MOMENTUM TIMELINE
# ==============================================================================
def create_xg_flow():
    fig, (ax_main, ax_mom) = plt.subplots(2, 1, figsize=(13, 8.2), facecolor="#0f172a",
                                          gridspec_kw={"height_ratios": [3.2, 1], "hspace": 0.25})
    ax_main.set_facecolor("#1e293b")
    ax_mom.set_facecolor("#1e293b")

    g_shots = sorted(match_data["gornik_shots"], key=lambda s: s["minute"])
    l_shots = sorted(match_data["legia_shots"], key=lambda s: s["minute"])

    minutes = list(range(0, 96))
    g_cum_xg = [0.0] * len(minutes)
    l_cum_xg = [0.0] * len(minutes)

    cur_g = 0.0
    cur_l = 0.0
    for m in minutes:
        for s in g_shots:
            if s["minute"] == m:
                cur_g += s["xG"]
        for s in l_shots:
            if s["minute"] == m:
                cur_l += s["xG"]
        g_cum_xg[m] = cur_g
        l_cum_xg[m] = cur_l

    ax_main.step(minutes, g_cum_xg, where="post", color="#38bdf8", lw=3.0, label="Górnik Zabrze (Final xG: 2.15)")
    ax_main.step(minutes, l_cum_xg, where="post", color="#f43f5e", lw=2.5, linestyle="--", label="Legia Warszawa (Final xG: 1.18)")

    ax_main.fill_between(minutes, g_cum_xg, step="post", color="#38bdf8", alpha=0.18)
    ax_main.fill_between(minutes, l_cum_xg, step="post", color="#f43f5e", alpha=0.12)

    goals = [
        {"minute": 27, "scorer": "Luka Zahovic 27' (1-0)", "val": g_cum_xg[27], "y_off": 0.32, "col": "#10b981"},
        {"minute": 58, "scorer": "Marc Gual 58' (1-1)", "val": l_cum_xg[58], "y_off": 0.35, "col": "#f43f5e"},
        {"minute": 81, "scorer": "Lukas Podolski 81' (2-1)", "val": g_cum_xg[81], "y_off": 0.30, "col": "#10b981"}
    ]

    for g in goals:
        ax_main.scatter(g["minute"], g["val"], s=120, color=g["col"], edgecolors="#ffffff", lw=2, zorder=5)
        ax_main.axvline(g["minute"], color=g["col"], linestyle=":", lw=1.2, alpha=0.7)
        ax_main.annotate(
            f"GOAL {g['scorer']}",
            xy=(g["minute"], g["val"]),
            xytext=(g["minute"] - 4, g["val"] + g["y_off"]),
            arrowprops=dict(arrowstyle="->", color=g["col"], lw=1.5),
            fontsize=9, fontweight="bold", color="#ffffff",
            bbox=dict(boxstyle="round,pad=0.25", facecolor="#0f172a", edgecolor=g["col"], lw=1.2)
        )

    ax_main.axvline(45, color="#64748b", linestyle="-", lw=1.2, alpha=0.8)
    ax_main.text(45.5, 0.15, "HALF TIME", color="#94a3b8", fontsize=8.5, fontweight="bold", rotation=90)

    ax_main.set_xlim(0, 95)
    ax_main.set_ylim(0, 2.5)
    ax_main.set_ylabel("Cumulative Expected Goals (xG)", fontsize=10.5, fontweight="bold", color="#cbd5e1", labelpad=8)
    ax_main.tick_params(colors="#94a3b8", labelsize=9.5)
    ax_main.legend(loc="upper left", facecolor="#0f172a", edgecolor="#334155", labelcolor="#f8fafc", fontsize=9.5)
    ax_main.grid(True, color="#334155", linestyle=":", alpha=0.6)

    # Subplot 2: Game Momentum
    bins = list(range(0, 100, 5))
    momentum_values = [
        -0.2, 0.1, 0.4, 0.6, 0.8, 0.7, 0.5, 0.2, 0.1,
        -0.3, -0.6, -0.7, -0.2, 0.2, 0.5, 0.8, 0.9, 0.4, 0.2
    ]
    bar_colors = ["#38bdf8" if v >= 0 else "#f43f5e" for v in momentum_values]
    ax_mom.bar(bins[:-1], momentum_values, width=4.2, color=bar_colors, alpha=0.85, align="edge", edgecolor="#0f172a", lw=0.8)
    ax_mom.axhline(0, color="#64748b", lw=1)
    ax_mom.set_xlim(0, 95)
    ax_mom.set_ylim(-1.0, 1.0)
    ax_mom.set_xlabel("Match Minute", fontsize=10.5, fontweight="bold", color="#cbd5e1", labelpad=6)
    ax_mom.set_ylabel("Dominance", fontsize=9, fontweight="bold", color="#cbd5e1")
    ax_mom.tick_params(colors="#94a3b8", labelsize=8.5)
    ax_mom.grid(True, color="#334155", linestyle=":", alpha=0.4)

    ax_mom.text(2, 0.6, "^ Górnik Territorial Control", color="#38bdf8", fontsize=8, fontweight="bold")
    ax_mom.text(2, -0.75, "v Legia Territorial Control", color="#f43f5e", fontsize=8, fontweight="bold")

    for s in ax_main.spines.values():
        s.set_color("#334155")
    for s in ax_mom.spines.values():
        s.set_color("#334155")

    fig.text(0.08, 0.965, "MATCH PERFORMANCE: xG FLOW & GAME MOMENTUM TIMELINE", fontsize=15, fontweight="bold", color="#f8fafc")
    plt.suptitle("Górnik Zabrze 2-1 Legia Warszawa | PKO Bank Polski Ekstraklasa 2025-2026", fontsize=10.5, color="#94a3b8", x=0.08, y=0.935, ha="left")
    fig.text(0.92, 0.01, "Opta / StatsBomb-compliant xG model tracking | Visualization by Zafer Yorganci", ha="right", fontsize=8.5, color="#64748b")

    plt.savefig("visuals/11_match_xg_flow_momentum.png", dpi=300, bbox_inches="tight", facecolor="#0f172a")
    plt.close()
    print("Generated visuals/11_match_xg_flow_momentum.png")

if __name__ == "__main__":
    create_shot_map()
    create_xg_flow()
