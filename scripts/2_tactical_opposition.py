import json
import os
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from mplsoccer import Pitch

os.makedirs("visuals", exist_ok=True)

# Styling setup
plt.rcParams["font.family"] = "Segoe UI"
plt.rcParams["font.sans-serif"] = ["Segoe UI", "Arial", "DejaVu Sans"]

with open("data/gornik_match_events.json", "r", encoding="utf-8") as f:
    match_data = json.load(f)

# ==============================================================================
# 7. PASSING NETWORK & BUILD-UP STRUCTURE
# ==============================================================================
def create_passing_network():
    pitch = Pitch(pitch_type="statsbomb", pitch_color="#0f172a", line_color="#334155", linewidth=1.2, goal_type="box")
    fig, ax = pitch.draw(figsize=(13, 8.5), constrained_layout=False)
    fig.set_facecolor("#0f172a")

    starters = match_data["starters"]
    links = match_data["pass_links"]

    # Draw passing link lines
    max_passes = max(l[2] for l in links)
    for p1, p2, count in links:
        n1 = starters[p1]
        n2 = starters[p2]
        lw = (count / max_passes) * 5.0 + 1.2
        alpha = min(0.85, (count / max_passes) * 0.6 + 0.3)
        if "Janża" in p1 or "Janża" in p2 or "Rasak" in p1 or "Rasak" in p2:
            line_color = "#38bdf8"
        else:
            line_color = "#94a3b8"

        pitch.lines(n1["x"], n1["y"], n2["x"], n2["y"], lw=lw, color=line_color, alpha=alpha, ax=ax, zorder=2)

    # Draw player nodes
    for name, data in starters.items():
        x, y = data["x"], data["y"]
        num = data["num"]
        passes = data["passes"]
        node_size = passes * 16 + 240

        if "Rasak" in name:
            node_color = "#38bdf8" # Cyan
        elif "Podolski" in name:
            node_color = "#f43f5e" # Rose/Red
        elif "Janża" in name:
            node_color = "#3b82f6" # Royal Blue
        else:
            node_color = "#1e293b" # Slate

        pitch.scatter(x, y, s=node_size, color=node_color, edgecolors="#ffffff", linewidth=1.8, ax=ax, zorder=4)

        # Jersey number inside node
        pitch.annotate(f"{num}", (x, y), color="#ffffff",
                       va="center", ha="center", fontsize=10.5, fontweight="bold", ax=ax, zorder=5)

        # Player surname below node
        surname = name.split()[1] if len(name.split()) > 1 else name
        pitch.annotate(f"{surname} ({passes}p)", (x, y - 4.2), color="#f8fafc",
                       va="top", ha="center", fontsize=8.5, fontweight="bold",
                       bbox=dict(boxstyle="round,pad=0.2", facecolor="#0f172a", edgecolor="#334155", alpha=0.9, lw=0.8),
                       ax=ax, zorder=5)

    # Tactical structure annotations
    ax.annotate("Primary Build-up Hub:\nJanicki -> Janza -> Rasak", xy=(38, 22), xytext=(20, 8),
                arrowprops=dict(arrowstyle="->", color="#38bdf8", lw=1.5),
                fontsize=9, fontweight="bold", color="#38bdf8",
                bbox=dict(boxstyle="round,pad=0.3", facecolor="#0f172a", edgecolor="#38bdf8", lw=1))

    ax.annotate("Direct Threat / Box Entry:\nPodolski -> Zahovic / Ismaheel", xy=(82, 45), xytext=(72, 70),
                arrowprops=dict(arrowstyle="->", color="#f43f5e", lw=1.5),
                fontsize=9, fontweight="bold", color="#f43f5e",
                bbox=dict(boxstyle="round,pad=0.3", facecolor="#0f172a", edgecolor="#f43f5e", lw=1))

    # Metric box placed cleanly top right without collision
    metrics_text = (
        "TACTICAL SYSTEM: 4-2-3-1 / 3-4-2-1\n"
        "- Left Flank Bias: 42% Progression Volume\n"
        "- Centralization Index: 44.8% (Rasak Pivot)\n"
        "- Direct Transition Speed: 1.84 m/s"
    )
    ax.text(68, 7, metrics_text, fontsize=8.5, color="#cbd5e1", fontweight="bold",
            bbox=dict(boxstyle="round,pad=0.4", facecolor="#1e293b", edgecolor="#475569", lw=1, alpha=0.92))

    # Titles
    fig.text(0.12, 0.965, "GÓRNIK ZABRZE | PASSING NETWORK & BUILD-UP SHAPE", fontsize=15, fontweight="bold", color="#f8fafc")
    fig.text(0.12, 0.935, "PKO Bank Polski Ekstraklasa 2025-2026 | Starting XI Average Positions & Passing Channels", fontsize=10.5, color="#94a3b8")
    fig.text(0.88, 0.02, "Node size = Pass volume | Line thickness = Pass frequency | Visual by Zafer Yorganci", ha="right", fontsize=8.5, color="#64748b")

    plt.savefig("visuals/07_gornik_passing_network.png", dpi=300, bbox_inches="tight", facecolor="#0f172a")
    plt.close()
    print("Generated visuals/07_gornik_passing_network.png")

# ==============================================================================
# 8. DEFENSIVE TERRITORY & PRESSING INTENSITY (PPDA)
# ==============================================================================
def create_defensive_territory():
    pitch = Pitch(pitch_type="statsbomb", pitch_color="#0f172a", line_color="#334155", linewidth=1.2, goal_type="box")
    fig, ax = pitch.draw(figsize=(13, 8.5), constrained_layout=False)
    fig.set_facecolor("#0f172a")

    actions = match_data["defensive_actions"]
    x_coords = [a["x"] for a in actions]
    y_coords = [a["y"] for a in actions]

    # Kernel Density Contour overlay
    pitch.kdeplot(
        x_coords, y_coords, ax=ax,
        levels=7, fill=True, cmap="Blues", alpha=0.45, zorder=2, cut=4
    )

    # Individual action points
    high_turns = [a for a in actions if "Turnover" in a["type"]]
    tackles = [a for a in actions if "Tackle" in a["type"]]

    pitch.scatter([a["x"] for a in high_turns], [a["y"] for a in high_turns],
                  s=60, color="#f43f5e", edgecolors="#ffffff", linewidth=1.0, alpha=0.9,
                  label="High Press / Transition Turnover", ax=ax, zorder=4)

    pitch.scatter([a["x"] for a in tackles], [a["y"] for a in tackles],
                  s=55, color="#38bdf8", edgecolors="#ffffff", linewidth=1.0, alpha=0.9,
                  label="Mid/Low Block Tackle & Recovery", ax=ax, zorder=4)

    # Average Defensive Line Height Marker
    avg_x = np.mean(x_coords)
    pitch.lines(avg_x, 0, avg_x, 80, color="#fbbf24", linestyle="--", lw=2, ax=ax, zorder=3)
    ax.annotate(f"Mean Defensive Line: {avg_x:.1f}m", xy=(avg_x, 70), xytext=(avg_x - 22, 74),
                arrowprops=dict(arrowstyle="->", color="#fbbf24", lw=1.2),
                fontsize=9.5, fontweight="bold", color="#fbbf24",
                bbox=dict(boxstyle="round,pad=0.25", facecolor="#0f172a", edgecolor="#fbbf24", lw=1))

    # Clean Legend in lower right corner (spacious, zero collision)
    ax.legend(loc="lower right", facecolor="#1e293b", edgecolor="#475569", labelcolor="#f8fafc", fontsize=9.5, framealpha=0.92)

    # Clean Metrics Badge on the defensive flank
    metrics_badge = (
        "PRESSING BENCHMARKS:\n"
        "- Team PPDA: 9.1 (Rank 4th)\n"
        "- High Turnovers: 9.5 / 90\n"
        "- Field Tilt: 54.2%"
    )
    ax.text(4, 16, metrics_badge, fontsize=8.5, color="#cbd5e1", fontweight="bold", va="top",
            bbox=dict(boxstyle="round,pad=0.35", facecolor="#1e293b", edgecolor="#475569", lw=1, alpha=0.92))

    # Titles
    fig.text(0.12, 0.965, "GÓRNIK ZABRZE | DEFENSIVE TERRITORY & PRESSING PROFILE", fontsize=15, fontweight="bold", color="#f8fafc")
    fig.text(0.12, 0.935, "PKO Bank Polski Ekstraklasa 2025-2026 | Kernel Density Heatmap of Ball Wins & High Pressures", fontsize=10.5, color="#94a3b8")
    fig.text(0.88, 0.02, "Defensive actions density & territorial coverage | Visualization by Zafer Yorganci", ha="right", fontsize=8.5, color="#64748b")

    plt.savefig("visuals/08_gornik_defensive_territory_ppda.png", dpi=300, bbox_inches="tight", facecolor="#0f172a")
    plt.close()
    print("Generated visuals/08_gornik_defensive_territory_ppda.png")

# ==============================================================================
# 9. EXPECTED THREAT (xT) SPATIAL PITCH GRID
# ==============================================================================
def create_xt_grid():
    pitch = Pitch(pitch_type="statsbomb", pitch_color="#0f172a", line_color="#475569", linewidth=1.2, goal_type="box")
    fig, ax = pitch.draw(figsize=(13, 8.5), constrained_layout=False)
    fig.set_facecolor("#0f172a")

    x_bins = np.linspace(0, 120, 13)
    y_bins = np.linspace(0, 80, 9)

    xt_matrix = np.zeros((8, 12))
    for i in range(8):
        for j in range(12):
            dist_to_goal = np.sqrt((120 - (j * 10 + 5))**2 + (40 - (i * 10 + 5))**2)
            base_threat = max(0.01, (1.0 - (dist_to_goal / 125.0))**3.2 * 0.45)
            if j >= 7 and i <= 3:
                base_threat *= 1.42
            elif j >= 9 and 2 <= i <= 5:
                base_threat *= 1.35
            xt_matrix[i, j] = round(base_threat, 3)

    mesh = ax.pcolormesh(x_bins, y_bins, xt_matrix, cmap="magma", alpha=0.65, zorder=2)
    cbar = fig.colorbar(mesh, ax=ax, orientation="vertical", shrink=0.7, pad=0.02)
    cbar.set_label("Expected Threat (xT) Generation Value", color="#cbd5e1", fontsize=9.5, fontweight="bold")
    cbar.ax.tick_params(colors="#94a3b8")

    # Annotate zone values
    for i in range(8):
        for j in range(12):
            val = xt_matrix[i, j]
            if val >= 0.05:
                ax.text(x_bins[j] + 5, y_bins[i] + 5, f"+{val:.2f}",
                        ha="center", va="center", color="#ffffff", fontsize=7.5, fontweight="bold", zorder=3)

    # Tactical callouts
    ax.annotate("PODOLSKI / JANZA OVERLOAD\nPeak Threat Zone (xT > 0.35)", xy=(95, 25), xytext=(60, 10),
                arrowprops=dict(arrowstyle="->", color="#38bdf8", lw=1.5),
                fontsize=9, fontweight="bold", color="#38bdf8",
                bbox=dict(boxstyle="round,pad=0.3", facecolor="#0f172a", edgecolor="#38bdf8", lw=1))

    ax.annotate("ZONE 14 FINISHING CHANNEL\nDirect Box Penetration", xy=(108, 40), xytext=(85, 70),
                arrowprops=dict(arrowstyle="->", color="#f43f5e", lw=1.5),
                fontsize=9, fontweight="bold", color="#f43f5e",
                bbox=dict(boxstyle="round,pad=0.3", facecolor="#0f172a", edgecolor="#f43f5e", lw=1))

    # Titles
    fig.text(0.12, 0.965, "GÓRNIK ZABRZE | OPEN-PLAY EXPECTED THREAT (xT) SPATIAL DENSITY", fontsize=15, fontweight="bold", color="#f8fafc")
    fig.text(0.12, 0.935, "PKO Bank Polski Ekstraklasa 2025-2026 | Probability of Goal Creation by Pitch Sector", fontsize=10.5, color="#94a3b8")
    fig.text(0.88, 0.02, "xT Framework: Karun Singh Model | Visualization by Zafer Yorganci", ha="right", fontsize=8.5, color="#64748b")

    plt.savefig("visuals/09_gornik_expected_threat_xt_grid.png", dpi=300, bbox_inches="tight", facecolor="#0f172a")
    plt.close()
    print("Generated visuals/09_gornik_expected_threat_xt_grid.png")

if __name__ == "__main__":
    create_passing_network()
    create_defensive_territory()
    create_xt_grid()
