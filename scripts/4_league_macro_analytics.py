import os
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

os.makedirs("visuals", exist_ok=True)

plt.rcParams["font.family"] = "Segoe UI"
plt.rcParams["font.sans-serif"] = ["Segoe UI", "Arial", "DejaVu Sans"]

df_teams = pd.read_csv("data/ekstraklasa_2025_2026_teams.csv")
df_players = pd.read_csv("data/ekstraklasa_2025_2026_players.csv")

# ==============================================================================
# 12. EKSTRAKLASA TEAM PERFORMANCE MATRIX (xG FOR vs xGA AGAINST)
# ==============================================================================
def create_team_matrix():
    fig, ax = plt.subplots(figsize=(13, 9), facecolor="#0f172a")
    ax.set_facecolor("#1e293b")

    med_xg = df_teams["xG_p90"].median()
    med_xga = df_teams["xGA_p90"].median()

    # Median lines
    ax.axvline(med_xg, color="#475569", linestyle="--", lw=1.2, alpha=0.75)
    ax.axhline(med_xga, color="#475569", linestyle="--", lw=1.2, alpha=0.75)

    # Invert y-axis so elite defenses (lowest xGA) are at the top
    ax.invert_yaxis()

    # Four Quadrant Labels
    ax.text(df_teams["xG_p90"].max() + 0.04, df_teams["xGA_p90"].min() - 0.05,
            "DOMINANT CONTENDERS / ELITE PROCESS\n(High xG Created, Low xGA Conceded)",
            ha="right", va="top", fontsize=10.5, fontweight="bold", color="#38bdf8", alpha=0.9)

    ax.text(df_teams["xG_p90"].min() - 0.04, df_teams["xGA_p90"].min() - 0.05,
            "PRAGMATIC LOW-BLOCK DEFENSES\n(Solid Structure, Low Chance Creation)",
            ha="left", va="top", fontsize=10, fontweight="bold", color="#94a3b8", alpha=0.75)

    ax.text(df_teams["xG_p90"].max() + 0.04, df_teams["xGA_p90"].max() + 0.05,
            "HIGH-EVENT TRANSITIONAL SIDES\n(Dangerous Attack, Exposed Defense)",
            ha="right", va="bottom", fontsize=10, fontweight="bold", color="#f59e0b", alpha=0.85)

    ax.text(df_teams["xG_p90"].min() - 0.04, df_teams["xGA_p90"].max() + 0.05,
            "RELEGATION RISK / STRUCTURAL CRISIS\n(Low Chance Creation, High xGA Allowed)",
            ha="left", va="bottom", fontsize=10, fontweight="bold", color="#f43f5e", alpha=0.85)

    # Plot each club
    for _, row in df_teams.iterrows():
        team = row["Team"]
        x = row["xG_p90"]
        y = row["xGA_p90"]
        pts = int(row["Pts"])

        if team == "Górnik Zabrze":
            ax.scatter(x, y, s=260, color="#38bdf8", edgecolors="#ffffff", lw=2.5, zorder=6)
            ax.annotate(
                f"[TOP] {team}\n({pts} Pts | xGD: +{row['xGD']:.1f})",
                (x, y), xytext=(x + 0.04, y - 0.03),
                fontsize=10.5, fontweight="bold", color="#ffffff",
                bbox=dict(boxstyle="round,pad=0.3", facecolor="#0f172a", edgecolor="#38bdf8", lw=1.8),
                zorder=7
            )
        elif team in ["Lech Poznań", "Raków Częstochowa", "Legia Warszawa", "Jagiellonia Białystok"]:
            ax.scatter(x, y, s=180, color="#60a5fa", edgecolors="#ffffff", lw=1.5, zorder=5)
            ax.annotate(f"{team} ({pts}p)", (x, y), xytext=(x + 0.03, y + 0.02),
                        fontsize=9.5, fontweight="bold", color="#e2e8f0", zorder=6)
        else:
            ax.scatter(x, y, s=120, color="#64748b", edgecolors="#334155", lw=1, alpha=0.85, zorder=4)
            ax.annotate(f"{team}", (x, y), xytext=(x + 0.02, y + 0.02),
                        fontsize=8.5, color="#cbd5e1", zorder=5)

    ax.set_title("POLISH EKSTRAKLASA 2025–2026: EXPECTED GOALS MATRIX", fontsize=16, fontweight="bold", color="#f8fafc", pad=28, loc="left")
    plt.suptitle("Comparative Quadrant Analysis: Expected Goals For (xG/90) vs Expected Goals Conceded (xGA/90)", fontsize=11, color="#94a3b8", x=0.125, y=0.935, ha="left")

    ax.set_xlabel("Expected Goals (xG) Created per 90", fontsize=11, fontweight="semibold", color="#cbd5e1", labelpad=10)
    ax.set_ylabel("Expected Goals Against (xGA) Conceded per 90 (Inverted: Better Defense ↑)", fontsize=11, fontweight="semibold", color="#cbd5e1", labelpad=10)

    ax.tick_params(colors="#94a3b8", labelsize=10)
    for spine in ax.spines.values():
        spine.set_color("#334155")
    ax.grid(True, color="#334155", linestyle=":", alpha=0.6)

    fig.text(0.9, 0.01, "Based on Opta/StatsBomb underlying metrics | Visualization by Zafer Yorgancı", ha="right", fontsize=9, color="#64748b")

    plt.savefig("visuals/12_ekstraklasa_xg_quadrant_matrix.png", dpi=300, bbox_inches="tight", facecolor="#0f172a")
    plt.close()
    print("Generated visuals/12_ekstraklasa_xg_quadrant_matrix.png")

# ==============================================================================
# 13. AI ARCHETYPE CLUSTERING (K-MEANS & PCA)
# ==============================================================================
def create_ai_archetype_clusters():
    fig, ax = plt.subplots(figsize=(13, 9), facecolor="#0f172a")
    ax.set_facecolor("#1e293b")

    features = [
        "npxG_p90", "xA_p90", "ProgPasses_p90", "ProgCarries_p90",
        "PAdj_TacklesInterceptions_p90", "DefDuelWinPct", "PassCompletionPct",
        "KeyPasses_p90", "BallRecoveries_p90", "xT_p90"
    ]

    X = df_players[features].copy()
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # Apply K-Means
    kmeans = KMeans(n_clusters=4, random_state=42, n_init=10)
    clusters = kmeans.fit_predict(X_scaled)
    df_players["Cluster"] = clusters

    # Apply PCA for 2D representation
    pca = PCA(n_components=2, random_state=42)
    components = pca.fit_transform(X_scaled)
    df_players["PC1"] = components[:, 0]
    df_players["PC2"] = components[:, 1]

    cluster_names = {
        0: "Playmakers & Chance Creators",
        1: "Defensive Anchors & Stopper Pivots",
        2: "Box-to-Box Transition Engines",
        3: "Dynamic 1v1 Wingers & Carriers"
    }

    cluster_colors = {
        0: "#f43f5e", # Rose
        1: "#10b981", # Emerald
        2: "#38bdf8", # Sky Blue
        3: "#fbbf24"  # Amber
    }

    # Plot clusters
    for c_id, c_name in cluster_names.items():
        c_data = df_players[df_players["Cluster"] == c_id]
        ax.scatter(
            c_data["PC1"], c_data["PC2"],
            s=90, color=cluster_colors[c_id], alpha=0.45,
            edgecolors="#334155", label=f"Cluster {c_id+1}: {c_name}"
        )

    # Highlight Górnik Zabrze key players
    spotlights = [
        {"player": "Damian Rasak", "note": "Damian Rasak\n(Górnik - Cluster 3: Transition Engine)"},
        {"player": "Lukas Podolski", "note": "Lukas Podolski\n(Górnik - Cluster 1: Playmaker)"},
        {"player": "Erik Janża", "note": "Erik Janża\n(Górnik - Cluster 1: Wide Creator)"},
        {"player": "Taofeek Ismaheel", "note": "Taofeek Ismaheel\n(Górnik - Cluster 4: 1v1 Carrier)"},
        {"player": "Dominik Szala", "note": "Dominik Szala\n(Górnik - Cluster 2: Defensive Anchor)"}
    ]

    for sp in spotlights:
        row = df_players[df_players["Player"] == sp["player"]]
        if not row.empty:
            x = row["PC1"].values[0]
            y = row["PC2"].values[0]
            c = cluster_colors[row["Cluster"].values[0]]
            ax.scatter(x, y, s=240, color=c, edgecolors="#ffffff", lw=2.2, zorder=6)
            ax.annotate(
                f"{sp['note']}", (x, y), xytext=(x + 0.25, y + 0.25),
                fontsize=9.5, fontweight="bold", color="#ffffff",
                bbox=dict(boxstyle="round,pad=0.25", facecolor="#0f172a", edgecolor=c, lw=1.5),
                zorder=7
            )

    ax.set_title("AI PLAYER ARCHETYPE CLUSTERING (UNSUPERVISED K-MEANS & PCA)", fontsize=16, fontweight="bold", color="#f8fafc", pad=28, loc="left")
    plt.suptitle("Translating 10 Event Metrics into Tactical Role Profiles for Turkish Süper Lig Transfer Benchmarking", fontsize=11, color="#94a3b8", x=0.125, y=0.935, ha="left")

    ax.set_xlabel(f"Principal Component 1: Ball Progression & Creative Output ({pca.explained_variance_ratio_[0]*100:.1f}% Variance)", fontsize=11, fontweight="semibold", color="#cbd5e1", labelpad=10)
    ax.set_ylabel(f"Principal Component 2: Defensive Volume & Duel Intensity ({pca.explained_variance_ratio_[1]*100:.1f}% Variance)", fontsize=11, fontweight="semibold", color="#cbd5e1", labelpad=10)

    ax.tick_params(colors="#94a3b8", labelsize=10)
    for spine in ax.spines.values():
        spine.set_color("#334155")
    ax.grid(True, color="#334155", linestyle=":", alpha=0.5)

    ax.legend(loc="upper right", facecolor="#0f172a", edgecolor="#334155", labelcolor="#f8fafc", fontsize=9.5)

    fig.text(0.9, 0.01, "AI Engineering Model: K-Means (k=4) + Scikit-Learn PCA | Developed by Zafer Yorgancı", ha="right", fontsize=9, color="#64748b")

    plt.savefig("visuals/13_ai_player_archetype_clusters.png", dpi=300, bbox_inches="tight", facecolor="#0f172a")
    plt.close()
    print("Generated visuals/13_ai_player_archetype_clusters.png")

if __name__ == "__main__":
    create_team_matrix()
    create_ai_archetype_clusters()
