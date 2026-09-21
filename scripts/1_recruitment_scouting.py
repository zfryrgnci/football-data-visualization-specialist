import os
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from mplsoccer import PyPizza

os.makedirs("visuals", exist_ok=True)

plt.rcParams["font.family"] = "Segoe UI"
plt.rcParams["font.sans-serif"] = ["Segoe UI", "Arial", "DejaVu Sans"]

df_players = pd.read_csv("data/ekstraklasa_2025_2026_players.csv")

# ==============================================================================
# 1. PIZZA RADAR: DAMIAN RASAK (DEFENSIVE / TRANSITIONAL MIDFIELDER)
# ==============================================================================
def create_rasak_radar():
    p = df_players[df_players["Player"] == "Damian Rasak"].iloc[0]

    params = [
        "Def Duel\nWin %", "PAdj Tackles\n+ Int / 90", "Ball\nRecoveries / 90", "Pressures\n/ 90",
        "Pass\nCompletion %", "Prog Passes\n/ 90", "Key Passes\n/ 90", "xT\n/ 90",
        "Prog Carries\n/ 90", "xA\n/ 90", "npxG\n/ 90"
    ]

    values = [
        int(p["DefDuelWinPct_pctile"]),
        int(p["PAdj_TacklesInterceptions_p90_pctile"]),
        int(p["BallRecoveries_p90_pctile"]),
        int(p["Pressures_p90_pctile"]),
        int(p["PassCompletionPct_pctile"]),
        int(p["ProgPasses_p90_pctile"]),
        int(p["KeyPasses_p90_pctile"]),
        int(p["xT_p90_pctile"]),
        int(p["ProgCarries_p90_pctile"]),
        int(p["xA_p90_pctile"]),
        int(p["npxG_p90_pctile"])
    ]

    slice_colors = ["#1d4ed8"] * 4 + ["#0284c7"] * 4 + ["#e11d48"] * 3
    text_colors = ["#ffffff"] * len(params)

    baker = PyPizza(
        params=params,
        background_color="#0f172a",
        straight_line_color="#334155",
        straight_line_lw=1,
        last_circle_lw=1.5,
        last_circle_color="#64748b",
        other_circle_lw=0.8,
        other_circle_color="#334155",
        inner_circle_size=20
    )

    fig, ax = baker.make_pizza(
        values,
        figsize=(8.5, 9.0),
        color_blank_space="same",
        slice_colors=slice_colors,
        value_colors=text_colors,
        value_bck_colors=slice_colors,
        blank_alpha=0.35,
        param_location=110,
        kwargs_slices=dict(edgecolor="#0f172a", zorder=2, linewidth=1.5),
        kwargs_params=dict(color="#f8fafc", fontsize=10, fontweight="bold", va="center"),
        kwargs_values=dict(color="#ffffff", fontsize=9.5, fontweight="bold", zorder=3,
                           bbox=dict(edgecolor="#0f172a", facecolor="#1e293b", boxstyle="round,pad=0.2", lw=1))
    )

    fig.text(0.515, 0.965, "DAMIAN RASAK | GÓRNIK ZABRZE", size=17, ha="center", weight="bold", color="#ffffff")
    fig.text(0.515, 0.940, "Percentile Rank vs Polish Ekstraklasa Central Midfielders | 2025-2026 Season", size=10.5, ha="center", color="#94a3b8")
    fig.text(0.515, 0.918, "Primary Profile: Anchor #6 / Ball-Winning Transition Engine | Prime Target for Süper Lig", size=9, ha="center", weight="bold", color="#38bdf8")

    # Legend
    fig.text(0.24, 0.045, "■ Defending & Pressing", size=9.5, weight="bold", color="#60a5fa")
    fig.text(0.48, 0.045, "■ Possession & Progression", size=9.5, weight="bold", color="#38bdf8")
    fig.text(0.74, 0.045, "■ Attacking Output", size=9.5, weight="bold", color="#fb7185")

    fig.text(0.515, 0.015, "Visualization by Zafer Yorganci | Football Data Visualization Specialist & AI Engineer", size=8.5, ha="center", color="#64748b")

    plt.savefig("visuals/01_pizza_radar_damian_rasak.png", dpi=300, bbox_inches="tight", facecolor="#0f172a")
    plt.close()
    print("Generated visuals/01_pizza_radar_damian_rasak.png")

# ==============================================================================
# 2. PIZZA RADAR: LUKAS PODOLSKI
# ==============================================================================
def create_podolski_radar():
    p = df_players[df_players["Player"] == "Lukas Podolski"].iloc[0]

    params = [
        "npxG\n/ 90", "xA\n/ 90", "Key Passes\n/ 90", "xT\n/ 90",
        "Prog Passes\n/ 90", "Pass\nCompletion %", "Prog Carries\n/ 90",
        "Pressures\n/ 90", "Ball\nRecoveries / 90", "Def Duel\nWin %"
    ]

    values = [
        int(p["npxG_p90_pctile"]),
        int(p["xA_p90_pctile"]),
        int(p["KeyPasses_p90_pctile"]),
        int(p["xT_p90_pctile"]),
        int(p["ProgPasses_p90_pctile"]),
        int(p["PassCompletionPct_pctile"]),
        int(p["ProgCarries_p90_pctile"]),
        int(p["Pressures_p90_pctile"]),
        int(p["BallRecoveries_p90_pctile"]),
        int(p["DefDuelWinPct_pctile"])
    ]

    slice_colors = ["#e11d48"] * 4 + ["#0284c7"] * 3 + ["#1d4ed8"] * 3
    text_colors = ["#ffffff"] * len(params)

    baker = PyPizza(
        params=params,
        background_color="#0f172a",
        straight_line_color="#334155",
        straight_line_lw=1,
        last_circle_lw=1.5,
        last_circle_color="#64748b",
        other_circle_lw=0.8,
        other_circle_color="#334155",
        inner_circle_size=20
    )

    fig, ax = baker.make_pizza(
        values,
        figsize=(8.5, 9.0),
        color_blank_space="same",
        slice_colors=slice_colors,
        value_colors=text_colors,
        value_bck_colors=slice_colors,
        blank_alpha=0.35,
        param_location=110,
        kwargs_slices=dict(edgecolor="#0f172a", zorder=2, linewidth=1.5),
        kwargs_params=dict(color="#f8fafc", fontsize=10, fontweight="bold", va="center"),
        kwargs_values=dict(color="#ffffff", fontsize=9.5, fontweight="bold", zorder=3,
                           bbox=dict(edgecolor="#0f172a", facecolor="#1e293b", boxstyle="round,pad=0.2", lw=1))
    )

    fig.text(0.515, 0.965, "LUKAS PODOLSKI | GÓRNIK ZABRZE", size=17, ha="center", weight="bold", color="#ffffff")
    fig.text(0.515, 0.940, "Percentile Rank vs Polish Ekstraklasa Attacking Midfielders & Wingers | 2025-2026", size=10.5, ha="center", color="#94a3b8")
    fig.text(0.515, 0.918, "Primary Profile: Playmaker #10 / Deep Threat Creator / Set-Piece Conductor", size=9, ha="center", weight="bold", color="#fbbf24")

    fig.text(0.24, 0.045, "■ Attacking Threat", size=9.5, weight="bold", color="#fb7185")
    fig.text(0.48, 0.045, "■ Ball Progression", size=9.5, weight="bold", color="#38bdf8")
    fig.text(0.74, 0.045, "■ Defensive Work", size=9.5, weight="bold", color="#60a5fa")

    fig.text(0.515, 0.015, "Visualization by Zafer Yorganci | Football Data Visualization Specialist & AI Engineer", size=8.5, ha="center", color="#64748b")

    plt.savefig("visuals/02_pizza_radar_lukas_podolski.png", dpi=300, bbox_inches="tight", facecolor="#0f172a")
    plt.close()
    print("Generated visuals/02_pizza_radar_lukas_podolski.png")

# ==============================================================================
# 3. PIZZA RADAR: ERIK JANŻA
# ==============================================================================
def create_janza_radar():
    p = df_players[df_players["Player"] == "Erik Janża"].iloc[0]

    params = [
        "xA\n/ 90", "Key Passes\n/ 90", "xT\n/ 90", "Prog Passes\n/ 90",
        "Prog Carries\n/ 90", "Pass\nCompletion %", "PAdj Tackles\n+ Int / 90",
        "Def Duel\nWin %", "Ball\nRecoveries / 90", "Pressures\n/ 90"
    ]

    values = [
        int(p["xA_p90_pctile"]),
        int(p["KeyPasses_p90_pctile"]),
        int(p["xT_p90_pctile"]),
        int(p["ProgPasses_p90_pctile"]),
        int(p["ProgCarries_p90_pctile"]),
        int(p["PassCompletionPct_pctile"]),
        int(p["PAdj_TacklesInterceptions_p90_pctile"]),
        int(p["DefDuelWinPct_pctile"]),
        int(p["BallRecoveries_p90_pctile"]),
        int(p["Pressures_p90_pctile"])
    ]

    slice_colors = ["#e11d48"] * 3 + ["#0284c7"] * 3 + ["#1d4ed8"] * 4
    text_colors = ["#ffffff"] * len(params)

    baker = PyPizza(
        params=params,
        background_color="#0f172a",
        straight_line_color="#334155",
        straight_line_lw=1,
        last_circle_lw=1.5,
        last_circle_color="#64748b",
        other_circle_lw=0.8,
        other_circle_color="#334155",
        inner_circle_size=20
    )

    fig, ax = baker.make_pizza(
        values,
        figsize=(8.5, 9.0),
        color_blank_space="same",
        slice_colors=slice_colors,
        value_colors=text_colors,
        value_bck_colors=slice_colors,
        blank_alpha=0.35,
        param_location=110,
        kwargs_slices=dict(edgecolor="#0f172a", zorder=2, linewidth=1.5),
        kwargs_params=dict(color="#f8fafc", fontsize=10, fontweight="bold", va="center"),
        kwargs_values=dict(color="#ffffff", fontsize=9.5, fontweight="bold", zorder=3,
                           bbox=dict(edgecolor="#0f172a", facecolor="#1e293b", boxstyle="round,pad=0.2", lw=1))
    )

    fig.text(0.515, 0.965, "ERIK JANŻA | GÓRNIK ZABRZE", size=17, ha="center", weight="bold", color="#ffffff")
    fig.text(0.515, 0.940, "Percentile Rank vs Polish Ekstraklasa Fullbacks & Wingbacks | 2025-2026", size=10.5, ha="center", color="#94a3b8")
    fig.text(0.515, 0.918, "Primary Profile: Wide Delivery Architect / Elite Set-Piece & Crossing Specialist", size=9, ha="center", weight="bold", color="#38bdf8")

    fig.text(0.24, 0.045, "■ Creation & Delivery", size=9.5, weight="bold", color="#fb7185")
    fig.text(0.48, 0.045, "■ Ball Progression", size=9.5, weight="bold", color="#38bdf8")
    fig.text(0.74, 0.045, "■ Defending & Pressing", size=9.5, weight="bold", color="#60a5fa")

    fig.text(0.515, 0.015, "Visualization by Zafer Yorganci | Football Data Visualization Specialist & AI Engineer", size=8.5, ha="center", color="#64748b")

    plt.savefig("visuals/03_pizza_radar_erik_janza.png", dpi=300, bbox_inches="tight", facecolor="#0f172a")
    plt.close()
    print("Generated visuals/03_pizza_radar_erik_janza.png")

# ==============================================================================
# 4. SCATTER PLOT: MIDFIELD CREATIVITY & PROGRESSION
# ==============================================================================
def create_midfield_creativity_scatter():
    fig, ax = plt.subplots(figsize=(12, 7.8), facecolor="#0f172a")
    ax.set_facecolor("#1e293b")

    mids = df_players[df_players["Pos"].str.contains("CM|DM|AM")].copy()

    med_prog = mids["ProgPasses_p90"].median()
    med_xa = mids["xA_p90"].median()

    ax.axvline(med_prog, color="#475569", linestyle="--", linewidth=1.2, alpha=0.75)
    ax.axhline(med_xa, color="#475569", linestyle="--", linewidth=1.2, alpha=0.75)

    ax.scatter(
        mids["ProgPasses_p90"], mids["xA_p90"],
        s=mids["xT_p90"] * 350 + 40,
        c="#64748b", alpha=0.45, edgecolors="#334155", linewidths=1, label="Ekstraklasa Midfielders"
    )

    highlights = [
        {"player": "Damian Rasak", "color": "#38bdf8", "offset": (0.12, -0.018), "label": "Damian Rasak\n(Górnik Zabrze)"},
        {"player": "Lukas Podolski", "color": "#f43f5e", "offset": (0.12, 0.012), "label": "Lukas Podolski\n(Górnik Zabrze)"},
        {"player": "Patrik Hellebrand", "color": "#fbbf24", "offset": (0.12, -0.018), "label": "Patrik Hellebrand\n(Górnik Zabrze)"},
        {"player": "Bartosz Kapustka", "color": "#10b981", "offset": (-1.6, 0.012), "label": "Bartosz Kapustka\n(Legia Warszawa)"},
        {"player": "Antoni Kozubal", "color": "#a855f7", "offset": (0.12, 0.012), "label": "Antoni Kozubal\n(Lech Poznań)"},
        {"player": "Gustav Berggren", "color": "#fb923c", "offset": (-1.5, -0.022), "label": "Gustav Berggren\n(Raków)"}
    ]

    for h in highlights:
        row = mids[mids["Player"] == h["player"]]
        if not row.empty:
            x = row["ProgPasses_p90"].values[0]
            y = row["xA_p90"].values[0]
            size = row["xT_p90"].values[0] * 350 + 60
            ax.scatter(x, y, s=size, c=h["color"], edgecolors="#ffffff", linewidths=1.8, zorder=5)
            ax.annotate(
                h["label"], (x, y),
                xytext=(x + h["offset"][0], y + h["offset"][1]),
                fontsize=9, fontweight="bold", color="#ffffff",
                bbox=dict(boxstyle="round,pad=0.25", facecolor="#0f172a", edgecolor=h["color"], lw=1.2, alpha=0.92),
                zorder=6
            )

    ax.text(mids["ProgPasses_p90"].max() - 0.2, mids["xA_p90"].max() - 0.01,
            "HIGH-VOLUME PROGRESSORS\n& CHANCE CREATORS",
            ha="right", va="top", fontsize=9.5, fontweight="bold", color="#38bdf8", alpha=0.9)

    ax.set_title("MIDFIELD CREATIVITY & PROGRESSIVE PASSING PROFILE", fontsize=15, fontweight="bold", color="#f8fafc", pad=26, loc="left")
    plt.suptitle("Polish Ekstraklasa 2025-2026 | Central & Attacking Midfielders (Min. 900 Mins)", fontsize=10.5, color="#94a3b8", x=0.125, y=0.935, ha="left")

    ax.set_xlabel("Progressive Passes per 90 (10m+ forward passes into final third)", fontsize=10.5, fontweight="bold", color="#cbd5e1", labelpad=8)
    ax.set_ylabel("Expected Assists (xA) per 90", fontsize=10.5, fontweight="bold", color="#cbd5e1", labelpad=8)

    ax.tick_params(colors="#94a3b8", labelsize=9.5)
    for spine in ax.spines.values():
        spine.set_color("#334155")
    ax.grid(True, color="#334155", linestyle=":", alpha=0.6)

    fig.text(0.9, 0.01, "Bubble Size represents Expected Threat (xT) per 90 | Visualization by Zafer Yorganci", ha="right", fontsize=8.5, color="#64748b")

    plt.savefig("visuals/04_scatter_midfield_creativity_progression.png", dpi=300, bbox_inches="tight", facecolor="#0f172a")
    plt.close()
    print("Generated visuals/04_scatter_midfield_creativity_progression.png")

# ==============================================================================
# 5. SCATTER PLOT: BALL WINNING & PRESSING INTENSITY
# ==============================================================================
def create_pressing_scatter():
    fig, ax = plt.subplots(figsize=(12, 7.8), facecolor="#0f172a")
    ax.set_facecolor("#1e293b")

    mids = df_players[df_players["Pos"].str.contains("DM|CM|CB|LB|RB")].copy()

    med_padj = mids["PAdj_TacklesInterceptions_p90"].median()
    med_win = mids["DefDuelWinPct"].median()

    ax.axvline(med_padj, color="#475569", linestyle="--", linewidth=1.2, alpha=0.75)
    ax.axhline(med_win, color="#475569", linestyle="--", linewidth=1.2, alpha=0.75)

    ax.scatter(
        mids["PAdj_TacklesInterceptions_p90"], mids["DefDuelWinPct"],
        s=mids["BallRecoveries_p90"] * 18,
        c="#64748b", alpha=0.45, edgecolors="#334155", linewidths=1
    )

    highlights = [
        {"player": "Damian Rasak", "color": "#38bdf8", "offset": (0.08, 1.2), "label": "Damian Rasak\n(Górnik Zabrze #6)"},
        {"player": "Dominik Szala", "color": "#3b82f6", "offset": (0.08, -1.8), "label": "Dominik Szala\n(Górnik CB/RB)"},
        {"player": "Kryspin Szcześniak", "color": "#60a5fa", "offset": (-1.2, 1.2), "label": "Kryspin Szcześniak\n(Górnik CB)"},
        {"player": "Taras Romanczuk", "color": "#f59e0b", "offset": (0.08, 1.0), "label": "Taras Romanczuk\n(Jagiellonia)"},
        {"player": "Gustav Berggren", "color": "#fb923c", "offset": (-1.1, -1.8), "label": "Gustav Berggren\n(Raków)"},
        {"player": "Rafał Augustyniak", "color": "#10b981", "offset": (-1.1, 1.0), "label": "Rafał Augustyniak\n(Legia)"}
    ]

    for h in highlights:
        row = mids[mids["Player"] == h["player"]]
        if not row.empty:
            x = row["PAdj_TacklesInterceptions_p90"].values[0]
            y = row["DefDuelWinPct"].values[0]
            size = row["BallRecoveries_p90"].values[0] * 22
            ax.scatter(x, y, s=size, c=h["color"], edgecolors="#ffffff", linewidths=1.8, zorder=5)
            ax.annotate(
                h["label"], (x, y),
                xytext=(x + h["offset"][0], y + h["offset"][1]),
                fontsize=9, fontweight="bold", color="#ffffff",
                bbox=dict(boxstyle="round,pad=0.25", facecolor="#0f172a", edgecolor=h["color"], lw=1.2, alpha=0.92),
                zorder=6
            )

    ax.text(mids["PAdj_TacklesInterceptions_p90"].max() - 0.1, mids["DefDuelWinPct"].max() + 0.5,
            "ELITE BALL-WINNERS & DUEL DOMINATORS\n(High Activity + High Success Rate)",
            ha="right", va="top", fontsize=9.5, fontweight="bold", color="#38bdf8", alpha=0.9)

    ax.set_title("DEFENSIVE ACTIVITY VS EFFICIENCY: PRESSING & BALL RECOVERY", fontsize=15, fontweight="bold", color="#f8fafc", pad=26, loc="left")
    plt.suptitle("Polish Ekstraklasa 2025-2026 | Possession-Adjusted Defensive Metrics (Min. 900 Mins)", fontsize=10.5, color="#94a3b8", x=0.125, y=0.935, ha="left")

    ax.set_xlabel("Possession-Adjusted (PAdj) Tackles + Interceptions per 90", fontsize=10.5, fontweight="bold", color="#cbd5e1", labelpad=8)
    ax.set_ylabel("Defensive Duel Win Rate (%)", fontsize=10.5, fontweight="bold", color="#cbd5e1", labelpad=8)

    ax.tick_params(colors="#94a3b8", labelsize=9.5)
    for spine in ax.spines.values():
        spine.set_color("#334155")
    ax.grid(True, color="#334155", linestyle=":", alpha=0.6)

    fig.text(0.9, 0.01, "Bubble Size represents Total Ball Recoveries per 90 | Visualization by Zafer Yorganci", ha="right", fontsize=8.5, color="#64748b")

    plt.savefig("visuals/05_scatter_pressing_recoveries.png", dpi=300, bbox_inches="tight", facecolor="#0f172a")
    plt.close()
    print("Generated visuals/05_scatter_pressing_recoveries.png")

# ==============================================================================
# 6. SCATTER PLOT: UNDERVALUED GEMS FOR TÜRKİYE SÜPER LİG
# ==============================================================================
def create_undervalued_gems_scatter():
    fig, ax = plt.subplots(figsize=(12, 7.8), facecolor="#0f172a")
    ax.set_facecolor("#1e293b")

    df_players["TotalThreat_p90"] = df_players["npxG_p90"] + df_players["xA_p90"]
    attackers = df_players[df_players["Minutes"] >= 1000].copy()

    med_val = attackers["MarketValue_M"].median()
    med_threat = attackers["TotalThreat_p90"].median()

    ax.axvline(med_val, color="#475569", linestyle="--", linewidth=1.2, alpha=0.75)
    ax.axhline(med_threat, color="#475569", linestyle="--", linewidth=1.2, alpha=0.75)

    ax.fill_between([0, med_val], med_threat, attackers["TotalThreat_p90"].max() + 0.1, color="#065f46", alpha=0.18)
    ax.text(0.2, attackers["TotalThreat_p90"].max() - 0.02, "PRIMARY TARGET ZONE FOR SÜPER LİG\n(Undervalued High-Impact Assets < €2.5M)",
            fontsize=9.5, fontweight="bold", color="#34d399", va="top")

    ax.scatter(
        attackers["MarketValue_M"], attackers["TotalThreat_p90"],
        s=attackers["ProgCarries_p90"] * 25 + 30,
        c="#64748b", alpha=0.45, edgecolors="#334155", linewidths=1
    )

    gems = [
        {"player": "Taofeek Ismaheel", "color": "#10b981", "offset": (0.08, 0.02), "label": "Taofeek Ismaheel\n(Górnik - €1.5M | Dribbler)"},
        {"player": "Damian Rasak", "color": "#38bdf8", "offset": (0.08, -0.032), "label": "Damian Rasak\n(Górnik - €1.8M | #6 Anchor)"},
        {"player": "Erik Janża", "color": "#60a5fa", "offset": (0.08, 0.02), "label": "Erik Janża\n(Górnik - €1.2M | Crosser)"},
        {"player": "Luka Zahović", "color": "#fbbf24", "offset": (0.08, 0.01), "label": "Luka Zahović\n(Górnik - €0.9M | 0.58 xG+xA)"},
        {"player": "Antoni Kozubal", "color": "#f43f5e", "offset": (-1.0, -0.035), "label": "Antoni Kozubal\n(Lech - €5.0M Premium)"},
        {"player": "Bartosz Kapustka", "color": "#a855f7", "offset": (0.08, 0.01), "label": "Bartosz Kapustka\n(Legia - €2.5M)"},
        {"player": "Benjamin Källman", "color": "#fb923c", "offset": (0.08, 0.02), "label": "Benjamin Källman\n(Cracovia - €2.2M)"}
    ]

    for g in gems:
        row = attackers[attackers["Player"] == g["player"]]
        if not row.empty:
            x = row["MarketValue_M"].values[0]
            y = row["TotalThreat_p90"].values[0]
            size = row["ProgCarries_p90"].values[0] * 28 + 50
            ax.scatter(x, y, s=size, c=g["color"], edgecolors="#ffffff", linewidths=1.8, zorder=5)
            ax.annotate(
                g["label"], (x, y),
                xytext=(x + g["offset"][0], y + g["offset"][1]),
                fontsize=9, fontweight="bold", color="#ffffff",
                bbox=dict(boxstyle="round,pad=0.25", facecolor="#0f172a", edgecolor=g["color"], lw=1.2, alpha=0.92),
                zorder=6
            )

    ax.set_title("RECRUITMENT MATRIX: MARKET VALUE VS ATTACKING IMPACT (npxG + xA / 90)", fontsize=15, fontweight="bold", color="#f8fafc", pad=26, loc="left")
    plt.suptitle("Targeting High-Value Transfers from Polish Ekstraklasa for Turkish Süper Lig Clubs | 2025-2026", fontsize=10.5, color="#94a3b8", x=0.125, y=0.935, ha="left")

    ax.set_xlabel("Estimated Transfer Value (€ Millions)", fontsize=10.5, fontweight="bold", color="#cbd5e1", labelpad=8)
    ax.set_ylabel("Non-Penalty xG + Expected Assists (xA) per 90", fontsize=10.5, fontweight="bold", color="#cbd5e1", labelpad=8)

    ax.tick_params(colors="#94a3b8", labelsize=9.5)
    for spine in ax.spines.values():
        spine.set_color("#334155")
    ax.grid(True, color="#334155", linestyle=":", alpha=0.6)

    fig.text(0.9, 0.01, "Bubble Size represents Progressive Carries per 90 | Analysis & Visual by Zafer Yorganci", ha="right", fontsize=8.5, color="#64748b")

    plt.savefig("visuals/06_scatter_undervalued_super_lig_gems.png", dpi=300, bbox_inches="tight", facecolor="#0f172a")
    plt.close()
    print("Generated visuals/06_scatter_undervalued_super_lig_gems.png")

if __name__ == "__main__":
    create_rasak_radar()
    create_podolski_radar()
    create_janza_radar()
    create_midfield_creativity_scatter()
    create_pressing_scatter()
    create_undervalued_gems_scatter()
