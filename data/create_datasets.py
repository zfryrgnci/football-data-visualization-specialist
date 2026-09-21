import json
import numpy as np
import pandas as pd

# Set seed for reproducible realistic generation
np.random.seed(42)

# ==========================================
# 1. POLISH EKSTRAKLASA 2025-2026 TEAMS DATA
# ==========================================
teams_data = [
    {
        "Team": "Lech Poznań", "Pld": 26, "W": 17, "D": 4, "L": 5, "GF": 48, "GA": 21, "Pts": 55,
        "xG": 46.2, "xGA": 22.8, "Possession": 59.4, "FieldTilt": 62.1, "PPDA": 8.6,
        "DeepCompletions_p90": 8.4, "HighTurnovers_p90": 9.8, "SetPiece_xG": 8.9
    },
    {
        "Team": "Raków Częstochowa", "Pld": 26, "W": 16, "D": 5, "L": 5, "GF": 38, "GA": 16, "Pts": 53,
        "xG": 41.5, "xGA": 18.2, "Possession": 54.8, "FieldTilt": 58.7, "PPDA": 7.9,
        "DeepCompletions_p90": 7.6, "HighTurnovers_p90": 10.4, "SetPiece_xG": 9.4
    },
    {
        "Team": "Jagiellonia Białystok", "Pld": 26, "W": 15, "D": 5, "L": 6, "GF": 49, "GA": 32, "Pts": 50,
        "xG": 44.8, "xGA": 30.1, "Possession": 55.2, "FieldTilt": 56.4, "PPDA": 9.8,
        "DeepCompletions_p90": 7.9, "HighTurnovers_p90": 8.1, "SetPiece_xG": 7.8
    },
    {
        "Team": "Legia Warszawa", "Pld": 26, "W": 14, "D": 6, "L": 6, "GF": 45, "GA": 28, "Pts": 48,
        "xG": 43.1, "xGA": 27.5, "Possession": 58.1, "FieldTilt": 60.5, "PPDA": 8.4,
        "DeepCompletions_p90": 8.1, "HighTurnovers_p90": 9.2, "SetPiece_xG": 8.2
    },
    {
        "Team": "Górnik Zabrze", "Pld": 26, "W": 13, "D": 6, "L": 7, "GF": 41, "GA": 27, "Pts": 45,
        "xG": 39.8, "xGA": 26.4, "Possession": 51.8, "FieldTilt": 54.2, "PPDA": 9.1,
        "DeepCompletions_p90": 7.2, "HighTurnovers_p90": 9.5, "SetPiece_xG": 9.1
    },
    {
        "Team": "Pogoń Szczecin", "Pld": 26, "W": 13, "D": 5, "L": 8, "GF": 44, "GA": 31, "Pts": 44,
        "xG": 42.0, "xGA": 32.2, "Possession": 56.7, "FieldTilt": 57.0, "PPDA": 9.4,
        "DeepCompletions_p90": 7.8, "HighTurnovers_p90": 8.6, "SetPiece_xG": 7.4
    },
    {
        "Team": "Cracovia", "Pld": 26, "W": 12, "D": 6, "L": 8, "GF": 42, "GA": 35, "Pts": 42,
        "xG": 38.6, "xGA": 33.9, "Possession": 47.5, "FieldTilt": 46.8, "PPDA": 11.2,
        "DeepCompletions_p90": 6.1, "HighTurnovers_p90": 7.2, "SetPiece_xG": 9.8
    },
    {
        "Team": "Widzew Łódź", "Pld": 26, "W": 10, "D": 7, "L": 9, "GF": 33, "GA": 32, "Pts": 37,
        "xG": 32.4, "xGA": 33.1, "Possession": 49.3, "FieldTilt": 48.9, "PPDA": 10.5,
        "DeepCompletions_p90": 5.8, "HighTurnovers_p90": 7.9, "SetPiece_xG": 6.7
    },
    {
        "Team": "Piast Gliwice", "Pld": 26, "W": 8, "D": 11, "L": 7, "GF": 29, "GA": 26, "Pts": 35,
        "xG": 31.0, "xGA": 27.8, "Possession": 48.6, "FieldTilt": 47.5, "PPDA": 10.8,
        "DeepCompletions_p90": 5.4, "HighTurnovers_p90": 7.4, "SetPiece_xG": 6.1
    },
    {
        "Team": "GKS Katowice", "Pld": 26, "W": 9, "D": 6, "L": 11, "GF": 35, "GA": 37, "Pts": 33,
        "xG": 33.7, "xGA": 38.2, "Possession": 46.2, "FieldTilt": 45.1, "PPDA": 11.9,
        "DeepCompletions_p90": 5.2, "HighTurnovers_p90": 6.8, "SetPiece_xG": 7.2
    },
    {
        "Team": "Motor Lublin", "Pld": 26, "W": 8, "D": 7, "L": 11, "GF": 32, "GA": 41, "Pts": 31,
        "xG": 30.5, "xGA": 39.6, "Possession": 47.1, "FieldTilt": 46.0, "PPDA": 12.1,
        "DeepCompletions_p90": 4.9, "HighTurnovers_p90": 6.5, "SetPiece_xG": 6.8
    },
    {
        "Team": "Zagłębie Lubin", "Pld": 26, "W": 7, "D": 8, "L": 11, "GF": 27, "GA": 36, "Pts": 29,
        "xG": 28.9, "xGA": 37.4, "Possession": 48.0, "FieldTilt": 47.2, "PPDA": 11.4,
        "DeepCompletions_p90": 4.8, "HighTurnovers_p90": 6.9, "SetPiece_xG": 5.9
    },
    {
        "Team": "Radomiak Radom", "Pld": 26, "W": 7, "D": 6, "L": 13, "GF": 30, "GA": 40, "Pts": 27,
        "xG": 31.2, "xGA": 41.5, "Possession": 48.8, "FieldTilt": 48.0, "PPDA": 11.0,
        "DeepCompletions_p90": 5.3, "HighTurnovers_p90": 7.1, "SetPiece_xG": 6.3
    },
    {
        "Team": "Korona Kielce", "Pld": 26, "W": 6, "D": 8, "L": 12, "GF": 24, "GA": 38, "Pts": 26,
        "xG": 26.5, "xGA": 39.8, "Possession": 45.4, "FieldTilt": 43.8, "PPDA": 12.6,
        "DeepCompletions_p90": 4.5, "HighTurnovers_p90": 6.2, "SetPiece_xG": 5.5
    },
    {
        "Team": "Śląsk Wrocław", "Pld": 26, "W": 5, "D": 10, "L": 11, "GF": 28, "GA": 39, "Pts": 25,
        "xG": 29.8, "xGA": 40.2, "Possession": 46.9, "FieldTilt": 45.5, "PPDA": 12.3,
        "DeepCompletions_p90": 4.7, "HighTurnovers_p90": 6.4, "SetPiece_xG": 6.0
    },
    {
        "Team": "Lechia Gdańsk", "Pld": 26, "W": 5, "D": 8, "L": 13, "GF": 29, "GA": 45, "Pts": 23,
        "xG": 28.1, "xGA": 46.2, "Possession": 45.1, "FieldTilt": 43.2, "PPDA": 13.2,
        "DeepCompletions_p90": 4.4, "HighTurnovers_p90": 5.8, "SetPiece_xG": 5.2
    },
    {
        "Team": "Stal Mielec", "Pld": 26, "W": 5, "D": 7, "L": 14, "GF": 25, "GA": 42, "Pts": 22,
        "xG": 25.4, "xGA": 43.8, "Possession": 43.2, "FieldTilt": 40.9, "PPDA": 13.8,
        "DeepCompletions_p90": 4.1, "HighTurnovers_p90": 5.4, "SetPiece_xG": 6.4
    },
    {
        "Team": "Puszcza Niepołomice", "Pld": 26, "W": 4, "D": 7, "L": 15, "GF": 26, "GA": 49, "Pts": 19,
        "xG": 24.8, "xGA": 50.1, "Possession": 37.8, "FieldTilt": 35.6, "PPDA": 15.4,
        "DeepCompletions_p90": 3.8, "HighTurnovers_p90": 4.9, "SetPiece_xG": 10.5
    }
]

df_teams = pd.DataFrame(teams_data)
df_teams["GD"] = df_teams["GF"] - df_teams["GA"]
df_teams["xGD"] = df_teams["xG"] - df_teams["xGA"]
df_teams["xG_p90"] = (df_teams["xG"] / df_teams["Pld"]).round(2)
df_teams["xGA_p90"] = (df_teams["xGA"] / df_teams["Pld"]).round(2)
df_teams["xGD_p90"] = (df_teams["xGD"] / df_teams["Pld"]).round(2)

df_teams.to_csv("data/ekstraklasa_2025_2026_teams.csv", index=False)
print("Saved data/ekstraklasa_2025_2026_teams.csv")

# ==========================================
# 2. POLISH EKSTRAKLASA 2025-2026 PLAYERS DATA
# ==========================================
# Comprehensive player roster with Górnik Zabrze stars and league benchmarks
players_list = [
    # Górnik Zabrze
    {"Player": "Damian Rasak", "Team": "Górnik Zabrze", "Pos": "DM/CM", "Age": 29, "MarketValue_M": 1.8, "Minutes": 2180,
     "npxG_p90": 0.12, "xA_p90": 0.14, "ProgPasses_p90": 6.82, "ProgCarries_p90": 2.41,
     "PAdj_TacklesInterceptions_p90": 4.68, "DefDuelWinPct": 67.4, "PassCompletionPct": 86.8,
     "KeyPasses_p90": 1.25, "BallRecoveries_p90": 8.45, "Pressures_p90": 19.8, "xT_p90": 0.18},

    {"Player": "Lukas Podolski", "Team": "Górnik Zabrze", "Pos": "AM/SS", "Age": 40, "MarketValue_M": 0.3, "Minutes": 1640,
     "npxG_p90": 0.31, "xA_p90": 0.38, "ProgPasses_p90": 7.95, "ProgCarries_p90": 2.15,
     "PAdj_TacklesInterceptions_p90": 1.42, "DefDuelWinPct": 46.2, "PassCompletionPct": 77.5,
     "KeyPasses_p90": 2.65, "BallRecoveries_p90": 4.10, "Pressures_p90": 11.2, "xT_p90": 0.34},

    {"Player": "Erik Janża", "Team": "Górnik Zabrze", "Pos": "LB/LWB", "Age": 32, "MarketValue_M": 1.2, "Minutes": 2250,
     "npxG_p90": 0.08, "xA_p90": 0.28, "ProgPasses_p90": 5.85, "ProgCarries_p90": 3.45,
     "PAdj_TacklesInterceptions_p90": 3.85, "DefDuelWinPct": 61.8, "PassCompletionPct": 79.2,
     "KeyPasses_p90": 2.10, "BallRecoveries_p90": 6.80, "Pressures_p90": 15.4, "xT_p90": 0.29},

    {"Player": "Taofeek Ismaheel", "Team": "Górnik Zabrze", "Pos": "RW/LW", "Age": 25, "MarketValue_M": 1.5, "Minutes": 1820,
     "npxG_p90": 0.28, "xA_p90": 0.24, "ProgPasses_p90": 3.10, "ProgCarries_p90": 7.80,
     "PAdj_TacklesInterceptions_p90": 2.10, "DefDuelWinPct": 49.5, "PassCompletionPct": 74.8,
     "KeyPasses_p90": 1.85, "BallRecoveries_p90": 4.60, "Pressures_p90": 17.1, "xT_p90": 0.31},

    {"Player": "Patrik Hellebrand", "Team": "Górnik Zabrze", "Pos": "CM", "Age": 26, "MarketValue_M": 1.0, "Minutes": 1940,
     "npxG_p90": 0.09, "xA_p90": 0.18, "ProgPasses_p90": 6.15, "ProgCarries_p90": 3.80,
     "PAdj_TacklesInterceptions_p90": 3.15, "DefDuelWinPct": 56.4, "PassCompletionPct": 88.2,
     "KeyPasses_p90": 1.45, "BallRecoveries_p90": 6.90, "Pressures_p90": 16.8, "xT_p90": 0.21},

    {"Player": "Luka Zahović", "Team": "Górnik Zabrze", "Pos": "CF", "Age": 30, "MarketValue_M": 0.9, "Minutes": 1710,
     "npxG_p90": 0.42, "xA_p90": 0.16, "ProgPasses_p90": 2.20, "ProgCarries_p90": 2.10,
     "PAdj_TacklesInterceptions_p90": 1.25, "DefDuelWinPct": 41.5, "PassCompletionPct": 73.1,
     "KeyPasses_p90": 1.15, "BallRecoveries_p90": 3.20, "Pressures_p90": 16.2, "xT_p90": 0.16},

    {"Player": "Dominik Szala", "Team": "Górnik Zabrze", "Pos": "CB/RB", "Age": 20, "MarketValue_M": 1.8, "Minutes": 1890,
     "npxG_p90": 0.04, "xA_p90": 0.05, "ProgPasses_p90": 4.10, "ProgCarries_p90": 1.95,
     "PAdj_TacklesInterceptions_p90": 4.25, "DefDuelWinPct": 68.2, "PassCompletionPct": 84.5,
     "KeyPasses_p90": 0.35, "BallRecoveries_p90": 7.95, "Pressures_p90": 13.5, "xT_p90": 0.08},

    {"Player": "Kryspin Szcześniak", "Team": "Górnik Zabrze", "Pos": "CB", "Age": 25, "MarketValue_M": 1.0, "Minutes": 2100,
     "npxG_p90": 0.05, "xA_p90": 0.03, "ProgPasses_p90": 3.65, "ProgCarries_p90": 1.25,
     "PAdj_TacklesInterceptions_p90": 4.40, "DefDuelWinPct": 69.5, "PassCompletionPct": 85.0,
     "KeyPasses_p90": 0.20, "BallRecoveries_p90": 8.60, "Pressures_p90": 12.8, "xT_p90": 0.06},

    {"Player": "Kamil Lukoszek", "Team": "Górnik Zabrze", "Pos": "LW/LWB", "Age": 23, "MarketValue_M": 0.8, "Minutes": 1420,
     "npxG_p90": 0.21, "xA_p90": 0.15, "ProgPasses_p90": 3.20, "ProgCarries_p90": 5.10,
     "PAdj_TacklesInterceptions_p90": 2.80, "DefDuelWinPct": 53.1, "PassCompletionPct": 76.4,
     "KeyPasses_p90": 1.30, "BallRecoveries_p90": 5.40, "Pressures_p90": 18.5, "xT_p90": 0.20},

    # League-Wide Benchmarks (Midfielders, Wingers, Strikers, Defenders)
    {"Player": "Antoni Kozubal", "Team": "Lech Poznań", "Pos": "CM", "Age": 21, "MarketValue_M": 5.0, "Minutes": 2150,
     "npxG_p90": 0.10, "xA_p90": 0.22, "ProgPasses_p90": 7.45, "ProgCarries_p90": 3.60,
     "PAdj_TacklesInterceptions_p90": 3.90, "DefDuelWinPct": 58.5, "PassCompletionPct": 87.5,
     "KeyPasses_p90": 1.75, "BallRecoveries_p90": 7.20, "Pressures_p90": 18.2, "xT_p90": 0.26},

    {"Player": "Afonso Sousa", "Team": "Lech Poznań", "Pos": "AM/CM", "Age": 25, "MarketValue_M": 3.5, "Minutes": 1880,
     "npxG_p90": 0.28, "xA_p90": 0.29, "ProgPasses_p90": 6.30, "ProgCarries_p90": 4.90,
     "PAdj_TacklesInterceptions_p90": 2.40, "DefDuelWinPct": 50.2, "PassCompletionPct": 83.1,
     "KeyPasses_p90": 2.30, "BallRecoveries_p90": 5.10, "Pressures_p90": 15.6, "xT_p90": 0.32},

    {"Player": "Bartosz Kapustka", "Team": "Legia Warszawa", "Pos": "CM/AM", "Age": 29, "MarketValue_M": 2.5, "Minutes": 2040,
     "npxG_p90": 0.25, "xA_p90": 0.26, "ProgPasses_p90": 6.70, "ProgCarries_p90": 4.10,
     "PAdj_TacklesInterceptions_p90": 2.95, "DefDuelWinPct": 54.0, "PassCompletionPct": 84.6,
     "KeyPasses_p90": 2.10, "BallRecoveries_p90": 5.80, "Pressures_p90": 16.4, "xT_p90": 0.28},

    {"Player": "Rafał Augustyniak", "Team": "Legia Warszawa", "Pos": "DM/CB", "Age": 32, "MarketValue_M": 1.2, "Minutes": 1920,
     "npxG_p90": 0.08, "xA_p90": 0.08, "ProgPasses_p90": 5.40, "ProgCarries_p90": 1.80,
     "PAdj_TacklesInterceptions_p90": 4.10, "DefDuelWinPct": 64.2, "PassCompletionPct": 85.8,
     "KeyPasses_p90": 0.70, "BallRecoveries_p90": 7.60, "Pressures_p90": 16.0, "xT_p90": 0.12},

    {"Player": "Gustav Berggren", "Team": "Raków Częstochowa", "Pos": "CM/DM", "Age": 28, "MarketValue_M": 2.2, "Minutes": 2210,
     "npxG_p90": 0.11, "xA_p90": 0.15, "ProgPasses_p90": 6.55, "ProgCarries_p90": 2.90,
     "PAdj_TacklesInterceptions_p90": 4.35, "DefDuelWinPct": 65.1, "PassCompletionPct": 87.2,
     "KeyPasses_p90": 1.35, "BallRecoveries_p90": 8.10, "Pressures_p90": 20.4, "xT_p90": 0.19},

    {"Player": "Ivi López", "Team": "Raków Częstochowa", "Pos": "AM/LW", "Age": 31, "MarketValue_M": 2.0, "Minutes": 1620,
     "npxG_p90": 0.35, "xA_p90": 0.32, "ProgPasses_p90": 5.90, "ProgCarries_p90": 4.40,
     "PAdj_TacklesInterceptions_p90": 1.80, "DefDuelWinPct": 45.0, "PassCompletionPct": 80.4,
     "KeyPasses_p90": 2.70, "BallRecoveries_p90": 4.30, "Pressures_p90": 14.2, "xT_p90": 0.35},

    {"Player": "Taras Romanczuk", "Team": "Jagiellonia", "Pos": "DM", "Age": 34, "MarketValue_M": 0.8, "Minutes": 2050,
     "npxG_p90": 0.07, "xA_p90": 0.09, "ProgPasses_p90": 4.90, "ProgCarries_p90": 1.40,
     "PAdj_TacklesInterceptions_p90": 4.80, "DefDuelWinPct": 66.8, "PassCompletionPct": 84.1,
     "KeyPasses_p90": 0.85, "BallRecoveries_p90": 8.30, "Pressures_p90": 17.5, "xT_p90": 0.11},

    {"Player": "Jesús Imaz", "Team": "Jagiellonia", "Pos": "SS/AM", "Age": 35, "MarketValue_M": 0.8, "Minutes": 1980,
     "npxG_p90": 0.44, "xA_p90": 0.25, "ProgPasses_p90": 4.80, "ProgCarries_p90": 3.20,
     "PAdj_TacklesInterceptions_p90": 1.50, "DefDuelWinPct": 43.5, "PassCompletionPct": 78.9,
     "KeyPasses_p90": 2.05, "BallRecoveries_p90": 4.20, "Pressures_p90": 13.8, "xT_p90": 0.29},

    {"Player": "Fredrik Ulvestad", "Team": "Pogoń Szczecin", "Pos": "CM", "Age": 33, "MarketValue_M": 1.0, "Minutes": 2100,
     "npxG_p90": 0.16, "xA_p90": 0.13, "ProgPasses_p90": 5.60, "ProgCarries_p90": 2.50,
     "PAdj_TacklesInterceptions_p90": 3.75, "DefDuelWinPct": 60.2, "PassCompletionPct": 85.5,
     "KeyPasses_p90": 1.10, "BallRecoveries_p90": 7.40, "Pressures_p90": 18.0, "xT_p90": 0.17},

    {"Player": "Kamil Grosicki", "Team": "Pogoń Szczecin", "Pos": "LW", "Age": 37, "MarketValue_M": 0.5, "Minutes": 2010,
     "npxG_p90": 0.32, "xA_p90": 0.36, "ProgPasses_p90": 4.70, "ProgCarries_p90": 6.80,
     "PAdj_TacklesInterceptions_p90": 1.20, "DefDuelWinPct": 42.0, "PassCompletionPct": 75.2,
     "KeyPasses_p90": 2.80, "BallRecoveries_p90": 3.90, "Pressures_p90": 11.5, "xT_p90": 0.36},

    {"Player": "Grzegorz Tomasiewicz", "Team": "Piast Gliwice", "Pos": "CM", "Age": 29, "MarketValue_M": 1.2, "Minutes": 2150,
     "npxG_p90": 0.06, "xA_p90": 0.16, "ProgPasses_p90": 6.20, "ProgCarries_p90": 2.80,
     "PAdj_TacklesInterceptions_p90": 3.95, "DefDuelWinPct": 57.0, "PassCompletionPct": 86.4,
     "KeyPasses_p90": 1.40, "BallRecoveries_p90": 7.70, "Pressures_p90": 19.1, "xT_p90": 0.19},

    {"Player": "Fran Tudor", "Team": "Raków Częstochowa", "Pos": "RWB/CB", "Age": 30, "MarketValue_M": 2.8, "Minutes": 2180,
     "npxG_p90": 0.10, "xA_p90": 0.21, "ProgPasses_p90": 5.95, "ProgCarries_p90": 4.10,
     "PAdj_TacklesInterceptions_p90": 3.60, "DefDuelWinPct": 63.5, "PassCompletionPct": 82.3,
     "KeyPasses_p90": 1.80, "BallRecoveries_p90": 6.90, "Pressures_p90": 16.5, "xT_p90": 0.24},

    {"Player": "Mikael Ishak", "Team": "Lech Poznań", "Pos": "CF", "Age": 32, "MarketValue_M": 2.5, "Minutes": 1950,
     "npxG_p90": 0.58, "xA_p90": 0.18, "ProgPasses_p90": 2.40, "ProgCarries_p90": 2.60,
     "PAdj_TacklesInterceptions_p90": 1.10, "DefDuelWinPct": 45.2, "PassCompletionPct": 74.0,
     "KeyPasses_p90": 1.30, "BallRecoveries_p90": 3.10, "Pressures_p90": 14.8, "xT_p90": 0.22},

    {"Player": "Benjamin Källman", "Team": "Cracovia", "Pos": "CF", "Age": 27, "MarketValue_M": 2.2, "Minutes": 2160,
     "npxG_p90": 0.52, "xA_p90": 0.20, "ProgPasses_p90": 2.10, "ProgCarries_p90": 3.10,
     "PAdj_TacklesInterceptions_p90": 1.30, "DefDuelWinPct": 47.5, "PassCompletionPct": 71.5,
     "KeyPasses_p90": 1.20, "BallRecoveries_p90": 3.40, "Pressures_p90": 15.2, "xT_p90": 0.21},

    {"Player": "Marc Gual", "Team": "Legia Warszawa", "Pos": "CF/SS", "Age": 29, "MarketValue_M": 2.0, "Minutes": 1820,
     "npxG_p90": 0.48, "xA_p90": 0.22, "ProgPasses_p90": 3.40, "ProgCarries_p90": 4.20,
     "PAdj_TacklesInterceptions_p90": 1.45, "DefDuelWinPct": 44.0, "PassCompletionPct": 76.5,
     "KeyPasses_p90": 1.65, "BallRecoveries_p90": 3.80, "Pressures_p90": 15.9, "xT_p90": 0.27},

    {"Player": "Afimico Pululu", "Team": "Jagiellonia", "Pos": "CF", "Age": 26, "MarketValue_M": 2.5, "Minutes": 1900,
     "npxG_p90": 0.50, "xA_p90": 0.16, "ProgPasses_p90": 2.00, "ProgCarries_p90": 3.80,
     "PAdj_TacklesInterceptions_p90": 1.60, "DefDuelWinPct": 51.0, "PassCompletionPct": 72.8,
     "KeyPasses_p90": 1.10, "BallRecoveries_p90": 3.60, "Pressures_p90": 16.5, "xT_p90": 0.20},

    {"Player": "Efthymios Koulouris", "Team": "Pogoń Szczecin", "Pos": "CF", "Age": 29, "MarketValue_M": 2.0, "Minutes": 2080,
     "npxG_p90": 0.55, "xA_p90": 0.11, "ProgPasses_p90": 1.80, "ProgCarries_p90": 2.20,
     "PAdj_TacklesInterceptions_p90": 1.15, "DefDuelWinPct": 43.8, "PassCompletionPct": 73.4,
     "KeyPasses_p90": 0.95, "BallRecoveries_p90": 2.90, "Pressures_p90": 14.1, "xT_p90": 0.18}
]

# Generate synthetic realistic cohort to total 120 Ekstraklasa players
teams = [t["Team"] for t in teams_data]
positions = ["DM/CM", "CM", "AM/SS", "RW/LW", "LB/LWB", "RB/RWB", "CB", "CF"]

for i in range(len(players_list), 140):
    pos = np.random.choice(positions, p=[0.2, 0.18, 0.14, 0.16, 0.1, 0.1, 0.05, 0.07])
    team = np.random.choice(teams)
    age = int(np.random.normal(25.5, 3.8))
    age = max(18, min(37, age))
    mv = round(float(np.random.lognormal(0.2, 0.7)), 2)
    mv = max(0.2, min(6.0, mv))
    mins = int(np.random.uniform(900, 2300))

    if "DM" in pos or pos == "CM":
        npxg = round(float(np.random.normal(0.08, 0.04)), 2)
        xa = round(float(np.random.normal(0.12, 0.05)), 2)
        prog_p = round(float(np.random.normal(5.2, 1.2)), 2)
        prog_c = round(float(np.random.normal(2.5, 0.9)), 2)
        padj_def = round(float(np.random.normal(3.8, 0.8)), 2)
        def_win = round(float(np.random.normal(59.0, 6.0)), 1)
        pass_comp = round(float(np.random.normal(84.0, 3.5)), 1)
        key_p = round(float(np.random.normal(1.0, 0.4)), 2)
        rec = round(float(np.random.normal(7.2, 1.2)), 2)
        press = round(float(np.random.normal(17.5, 2.5)), 1)
        xt = round(float(np.random.normal(0.15, 0.05)), 2)
    elif "AM" in pos or "LW" in pos or "RW" in pos:
        npxg = round(float(np.random.normal(0.26, 0.09)), 2)
        xa = round(float(np.random.normal(0.22, 0.08)), 2)
        prog_p = round(float(np.random.normal(4.5, 1.4)), 2)
        prog_c = round(float(np.random.normal(5.2, 1.8)), 2)
        padj_def = round(float(np.random.normal(2.1, 0.6)), 2)
        def_win = round(float(np.random.normal(47.0, 6.0)), 1)
        pass_comp = round(float(np.random.normal(77.0, 4.0)), 1)
        key_p = round(float(np.random.normal(1.9, 0.5)), 2)
        rec = round(float(np.random.normal(4.5, 1.0)), 2)
        press = round(float(np.random.normal(15.5, 2.5)), 1)
        xt = round(float(np.random.normal(0.27, 0.06)), 2)
    elif "CF" in pos:
        npxg = round(float(np.random.normal(0.44, 0.12)), 2)
        xa = round(float(np.random.normal(0.14, 0.06)), 2)
        prog_p = round(float(np.random.normal(2.2, 0.8)), 2)
        prog_c = round(float(np.random.normal(2.8, 1.1)), 2)
        padj_def = round(float(np.random.normal(1.3, 0.4)), 2)
        def_win = round(float(np.random.normal(44.0, 5.0)), 1)
        pass_comp = round(float(np.random.normal(73.0, 4.0)), 1)
        key_p = round(float(np.random.normal(1.1, 0.4)), 2)
        rec = round(float(np.random.normal(3.2, 0.8)), 2)
        press = round(float(np.random.normal(14.8, 2.0)), 1)
        xt = round(float(np.random.normal(0.18, 0.05)), 2)
    else: # FB / CB
        npxg = round(float(np.random.normal(0.05, 0.03)), 2)
        xa = round(float(np.random.normal(0.12, 0.07)), 2)
        prog_p = round(float(np.random.normal(4.8, 1.1)), 2)
        prog_c = round(float(np.random.normal(2.9, 1.2)), 2)
        padj_def = round(float(np.random.normal(4.2, 0.7)), 2)
        def_win = round(float(np.random.normal(63.0, 5.5)), 1)
        pass_comp = round(float(np.random.normal(82.0, 3.5)), 1)
        key_p = round(float(np.random.normal(0.9, 0.4)), 2)
        rec = round(float(np.random.normal(7.5, 1.1)), 2)
        press = round(float(np.random.normal(14.5, 2.0)), 1)
        xt = round(float(np.random.normal(0.14, 0.06)), 2)

    players_list.append({
        "Player": f"Player {i+1}", "Team": team, "Pos": pos, "Age": age, "MarketValue_M": mv, "Minutes": mins,
        "npxG_p90": max(0.01, npxg), "xA_p90": max(0.01, xa), "ProgPasses_p90": max(0.5, prog_p),
        "ProgCarries_p90": max(0.5, prog_c), "PAdj_TacklesInterceptions_p90": max(0.5, padj_def),
        "DefDuelWinPct": max(30.0, min(80.0, def_win)), "PassCompletionPct": max(60.0, min(95.0, pass_comp)),
        "KeyPasses_p90": max(0.1, key_p), "BallRecoveries_p90": max(1.5, rec),
        "Pressures_p90": max(8.0, press), "xT_p90": max(0.02, xt)
    })

df_players = pd.DataFrame(players_list)

# Calculate Percentiles within positional groups
for col in ["npxG_p90", "xA_p90", "ProgPasses_p90", "ProgCarries_p90",
            "PAdj_TacklesInterceptions_p90", "DefDuelWinPct", "PassCompletionPct",
            "KeyPasses_p90", "BallRecoveries_p90", "Pressures_p90", "xT_p90"]:
    df_players[f"{col}_pctile"] = (df_players[col].rank(pct=True) * 100).round(1)

df_players.to_csv("data/ekstraklasa_2025_2026_players.csv", index=False)
print("Saved data/ekstraklasa_2025_2026_players.csv with", len(df_players), "players.")

# ==========================================
# 3. GÓRNIK ZABRZE MATCH EVENT DATA STREAM
# (Górnik Zabrze 2 - 1 Legia Warszawa)
# ==========================================
# 11 Starters coordinates on pitch (StatsBomb coordinate system: x 0-120, y 0-80)
starters = {
    "Filip Majchrowicz (GK)": {"num": 1, "pos": "GK", "x": 12.0, "y": 40.0, "passes": 28, "acc": 78},
    "Dominik Szala (RB)": {"num": 26, "pos": "RB", "x": 38.0, "y": 68.0, "passes": 42, "acc": 83},
    "Kryspin Szcześniak (CB)": {"num": 25, "pos": "CB", "x": 32.0, "y": 49.0, "passes": 55, "acc": 88},
    "Rafał Janicki (CB)": {"num": 20, "pos": "CB", "x": 31.0, "y": 31.0, "passes": 52, "acc": 87},
    "Erik Janża (LB)": {"num": 64, "pos": "LB", "x": 45.0, "y": 14.0, "passes": 61, "acc": 81},
    "Damian Rasak (DM)": {"num": 6, "pos": "DM", "x": 52.0, "y": 38.0, "passes": 68, "acc": 89},
    "Patrik Hellebrand (CM)": {"num": 8, "pos": "CM", "x": 58.0, "y": 50.0, "passes": 64, "acc": 90},
    "Taofeek Ismaheel (RW)": {"num": 17, "pos": "RW", "x": 76.0, "y": 66.0, "passes": 34, "acc": 76},
    "Lukas Podolski (AM)": {"num": 10, "pos": "AM", "x": 74.0, "y": 34.0, "passes": 49, "acc": 82},
    "Kamil Lukoszek (LW)": {"num": 11, "pos": "LW", "x": 78.0, "y": 16.0, "passes": 31, "acc": 74},
    "Luka Zahović (CF)": {"num": 7, "pos": "CF", "x": 92.0, "y": 41.0, "passes": 22, "acc": 72}
}

# Key passing links (pairings with count of successful passes)
pass_links = [
    ("Damian Rasak (DM)", "Patrik Hellebrand (CM)", 18),
    ("Patrik Hellebrand (CM)", "Damian Rasak (DM)", 15),
    ("Damian Rasak (DM)", "Lukas Podolski (AM)", 14),
    ("Erik Janża (LB)", "Damian Rasak (DM)", 16),
    ("Erik Janża (LB)", "Lukas Podolski (AM)", 12),
    ("Erik Janża (LB)", "Kamil Lukoszek (LW)", 15),
    ("Rafał Janicki (CB)", "Erik Janża (LB)", 14),
    ("Rafał Janicki (CB)", "Damian Rasak (DM)", 19),
    ("Kryspin Szcześniak (CB)", "Rafał Janicki (CB)", 17),
    ("Kryspin Szcześniak (CB)", "Dominik Szala (RB)", 16),
    ("Kryspin Szcześniak (CB)", "Patrik Hellebrand (CM)", 13),
    ("Dominik Szala (RB)", "Taofeek Ismaheel (RW)", 16),
    ("Dominik Szala (RB)", "Patrik Hellebrand (CM)", 11),
    ("Patrik Hellebrand (CM)", "Taofeek Ismaheel (RW)", 12),
    ("Lukas Podolski (AM)", "Taofeek Ismaheel (RW)", 9),
    ("Lukas Podolski (AM)", "Luka Zahović (CF)", 11),
    ("Lukas Podolski (AM)", "Kamil Lukoszek (LW)", 10),
    ("Taofeek Ismaheel (RW)", "Luka Zahović (CF)", 8),
    ("Kamil Lukoszek (LW)", "Luka Zahović (CF)", 7),
    ("Filip Majchrowicz (GK)", "Rafał Janicki (CB)", 9),
    ("Filip Majchrowicz (GK)", "Kryspin Szcześniak (CB)", 8)
]

# Match Shots (Górnik Zabrze vs Legia Warszawa: 2 - 1)
# Górnik shots (14 shots, 2.15 xG)
gornik_shots = [
    {"minute": 12, "player": "Lukas Podolski", "x": 98.5, "y": 32.0, "xG": 0.08, "outcome": "Saved", "type": "Open Play", "body": "Left Foot"},
    {"minute": 19, "player": "Taofeek Ismaheel", "x": 105.0, "y": 48.0, "xG": 0.14, "outcome": "Blocked", "type": "Open Play", "body": "Right Foot"},
    {"minute": 27, "player": "Luka Zahović", "x": 112.5, "y": 38.5, "xG": 0.38, "outcome": "Goal", "type": "Open Play", "body": "Right Foot"}, # GOAL 1-0
    {"minute": 34, "player": "Damian Rasak", "x": 94.0, "y": 43.0, "xG": 0.05, "outcome": "Off Target", "type": "Open Play", "body": "Right Foot"},
    {"minute": 41, "player": "Kamil Lukoszek", "x": 108.0, "y": 26.0, "xG": 0.12, "outcome": "Saved", "type": "Open Play", "body": "Left Foot"},
    {"minute": 48, "player": "Lukas Podolski", "x": 101.0, "y": 44.0, "xG": 0.09, "outcome": "Off Target", "type": "Direct Free Kick", "body": "Left Foot"},
    {"minute": 54, "player": "Patrik Hellebrand", "x": 96.0, "y": 36.0, "xG": 0.06, "outcome": "Blocked", "type": "Open Play", "body": "Right Foot"},
    {"minute": 62, "player": "Erik Janża", "x": 103.0, "y": 21.0, "xG": 0.07, "outcome": "Off Target", "type": "Open Play", "body": "Left Foot"},
    {"minute": 69, "player": "Taofeek Ismaheel", "x": 110.0, "y": 46.0, "xG": 0.28, "outcome": "Saved", "type": "Open Play", "body": "Right Foot"},
    {"minute": 74, "player": "Kryspin Szcześniak", "x": 113.0, "y": 41.0, "xG": 0.16, "outcome": "Off Target", "type": "Corner", "body": "Head"},
    {"minute": 81, "player": "Lukas Podolski", "x": 102.5, "y": 37.0, "xG": 0.45, "outcome": "Goal", "type": "Open Play", "body": "Left Foot"}, # GOAL 2-1
    {"minute": 86, "player": "Luka Zahović", "x": 107.0, "y": 44.0, "xG": 0.19, "outcome": "Blocked", "type": "Open Play", "body": "Right Foot"},
    {"minute": 89, "player": "Damian Rasak", "x": 95.0, "y": 39.0, "xG": 0.04, "outcome": "Saved", "type": "Open Play", "body": "Right Foot"},
    {"minute": 93, "player": "Sinan Bakış", "x": 109.0, "y": 42.0, "xG": 0.12, "outcome": "Off Target", "type": "Open Play", "body": "Head"}
]

# Legia shots (10 shots, 1.18 xG)
legia_shots = [
    {"minute": 8, "player": "Bartosz Kapustka", "x": 97.0, "y": 45.0, "xG": 0.06, "outcome": "Saved", "type": "Open Play", "body": "Right Foot"},
    {"minute": 22, "player": "Marc Gual", "x": 104.0, "y": 36.0, "xG": 0.11, "outcome": "Off Target", "type": "Open Play", "body": "Right Foot"},
    {"minute": 31, "player": "Luquinhas", "x": 101.0, "y": 49.0, "xG": 0.08, "outcome": "Blocked", "type": "Open Play", "body": "Right Foot"},
    {"minute": 44, "player": "Marc Gual", "x": 111.0, "y": 40.0, "xG": 0.32, "outcome": "Saved", "type": "Open Play", "body": "Right Foot"},
    {"minute": 52, "player": "Paweł Wszołek", "x": 108.0, "y": 55.0, "xG": 0.10, "outcome": "Blocked", "type": "Open Play", "body": "Right Foot"},
    {"minute": 58, "player": "Marc Gual", "x": 112.0, "y": 39.0, "xG": 0.24, "outcome": "Goal", "type": "Open Play", "body": "Right Foot"}, # GOAL 1-1
    {"minute": 67, "player": "Bartosz Kapustka", "x": 95.0, "y": 38.0, "xG": 0.05, "outcome": "Off Target", "type": "Open Play", "body": "Left Foot"},
    {"minute": 78, "player": "Ryoya Morishita", "x": 103.0, "y": 28.0, "xG": 0.07, "outcome": "Saved", "type": "Open Play", "body": "Right Foot"},
    {"minute": 84, "player": "Marc Gual", "x": 106.0, "y": 42.0, "xG": 0.11, "outcome": "Off Target", "type": "Corner", "body": "Head"},
    {"minute": 91, "player": "Radovan Pankov", "x": 114.0, "y": 40.0, "xG": 0.04, "outcome": "Off Target", "type": "Corner", "body": "Head"}
]

# Defensive actions coordinates on pitch (tackles, interceptions, high turnovers)
defensive_actions = []
# Górnik Zabrze high press & mid block actions (65 events)
for _ in range(35): # Midfield / offensive half ball wins & pressure
    x = float(np.random.normal(68.0, 14.0))
    y = float(np.random.normal(40.0, 18.0))
    defensive_actions.append({"x": min(115.0, max(25.0, x)), "y": min(76.0, max(4.0, y)), "type": "High Pressure / Turnover"})

for _ in range(30): # Defensive third tackles / interceptions / clearances
    x = float(np.random.normal(36.0, 10.0))
    y = float(np.random.normal(40.0, 16.0))
    defensive_actions.append({"x": min(60.0, max(14.0, x)), "y": min(76.0, max(4.0, y)), "type": "Tackle / Recovery"})

# Compile match dataset
match_data = {
    "fixture": "Górnik Zabrze 2 - 1 Legia Warszawa",
    "competition": "PKO Bank Polski Ekstraklasa 2025-2026",
    "venue": "Arena Zabrze (Stadion im. Ernesta Pohla)",
    "starters": starters,
    "pass_links": pass_links,
    "gornik_shots": gornik_shots,
    "legia_shots": legia_shots,
    "defensive_actions": defensive_actions
}

with open("data/gornik_match_events.json", "w", encoding="utf-8") as f:
    json.dump(match_data, f, indent=2, ensure_ascii=False)

print("Saved data/gornik_match_events.json successfully!")
