# GÓRNIK ZABRZE & POLISH EKSTRAKLASA (2025–2026)
## Football Data Visualization & Technical Scouting Dossier
**Author:** Zafer Yorgancı | Sports Data Visualization Specialist & AI Engineer  
**Role:** Sports Data Visualization Specialist, Górnik Zabrze (Remote / Hybrid, 2025–2026)  
**Target Audience:** Turkish Süper Lig Sporting Directors, Heads of Recruitment, and Coaching Staffs  
**PDF Document:** [`Gornik_Zabrze_Ekstraklasa_2025_2026_Portfolio.pdf`](file:///c:/Users/Superuser/Desktop/Football%20Data%20Visualization%20Specialist/Gornik_Zabrze_Ekstraklasa_2025_2026_Portfolio.pdf)

---

## Executive Overview
This technical dossier provides an end-to-end analytical breakdown of Górnik Zabrze's tactical mechanics and the broader 2025–2026 Polish Ekstraklasa competitive environment. Built by combining Opta and Wyscout event streams with custom Python visualization pipelines (`mplsoccer`, `matplotlib`, `scikit-learn`), it demonstrates how professional data visualization and AI modeling answer high-stakes football questions:
1. **Recruitment & Talent Identification:** Which undervalued players in Poland possess the physical and tactical profiles required to succeed in the Turkish Süper Lig?
2. **Opposition & Tactical Analysis:** How does Górnik Zabrze manipulate space in build-up, where are their pressing triggers, and where do they generate Expected Threat (xT)?
3. **Post-Match Debriefs:** How did game state and momentum shifts dictate match outcomes in marquee league fixtures (e.g. Górnik Zabrze 2–1 Legia Warszawa)?
4. **AI & Machine Learning:** How can unsupervised clustering (K-Means & PCA) identify mathematical positional twins for squad replacement?

---

## 1. Recruitment & Scouting Intelligence

### 1.1 Damian Rasak (29, DM/CM) — The High-Tempo Transition Anchor
- **Visual Asset:** [`01_pizza_radar_damian_rasak.png`](file:///c:/Users/Superuser/Desktop/Football%20Data%20Visualization%20Specialist/visuals/01_pizza_radar_damian_rasak.png)
- **Position:** Defensive / Central Midfielder (#6 / #8 hybrid)
- **Market Value:** €1.8M (Estimated transfer window acquisition: €1.5M–€2.0M)
- **Key Metrics:**
  - Defensive Duel Win Rate: **67.4%** (98th percentile in Ekstraklasa)
  - Possession-Adjusted (PAdj) Tackles + Interceptions: **4.68 / 90** (94th percentile)
  - Progressive Passes: **6.82 / 90** (89th percentile)
  - Pass Completion Rate: **86.8%** (88th percentile)
  - Ball Recoveries: **8.45 / 90** (91st percentile)
- **Tactical Evaluation:**
  Rasak is the quintessential modern transition anchor. He acts as Górnik's defensive shield, ranking among the top 2% of midfielders in duel success. Crucially, unlike purely destructive pivots, Rasak completes 6.82 progressive passes per 90 into the middle and attacking thirds, initiating vertical counters within 2.5 seconds of winning possession.
- **Süper Lig Fit:**
  A natural replacement or rotational partner for high-pressing anchors in the Turkish Süper Lig (e.g. Trabzonspor, Beşiktaş, Samsunspor, Eyüpspor). His physical robustness, aerial competence, and tactical discipline make him a low-risk, high-impact acquisition.

---

### 1.2 Lukas Podolski (40, AM/SS) — Creative Fulcrum & Final-Third Threat
- **Visual Asset:** [`02_pizza_radar_lukas_podolski.png`](file:///c:/Users/Superuser/Desktop/Football%20Data%20Visualization%20Specialist/visuals/02_pizza_radar_lukas_podolski.png)
- **Position:** Attacking Midfielder / Second Striker (#10)
- **Key Metrics:**
  - Expected Assists (xA): **0.38 / 90** (97th percentile)
  - Progressive Passes: **7.95 / 90** (98th percentile)
  - Key Passes: **2.65 / 90** (95th percentile)
  - Expected Threat (xT): **0.34 / 90** (96th percentile)
  - Non-penalty xG: **0.31 / 90** (84th percentile)
- **Tactical Evaluation:**
  Even in the twilight of his storied career, Podolski remains one of Central Europe's most dangerous attacking conductors. Operating in the left half-space, he functions as an offensive amplifier, ranking in the top 3% of the league for progressive deliveries and direct shot assists.

---

### 1.3 Erik Janża (32, LB/LWB) — Wide Delivery Architect
- **Visual Asset:** [`03_pizza_radar_erik_janza.png`](file:///c:/Users/Superuser/Desktop/Football%20Data%20Visualization%20Specialist/visuals/03_pizza_radar_erik_janza.png)
- **Position:** Left-Back / Left Wing-Back (#64)
- **Market Value:** €1.2M
- **Key Metrics:**
  - Expected Assists (xA): **0.28 / 90** (94th percentile among fullbacks)
  - Progressive Passes: **5.85 / 90** (92nd percentile)
  - Key Passes: **2.10 / 90** (95th percentile)
  - Defensive Duel Win Rate: **61.8%** (85th percentile)
- **Tactical Evaluation:**
  Janża serves as the primary outlet for Górnik's left-side build-up overload. His elite crossing technique and set-piece accuracy create sustained box threat, while his 61.8% duel win rate guarantees defensive security against explosive wingers.

---

### 1.4 League-Wide Midfield Creativity vs Progression Matrix
- **Visual Asset:** [`04_scatter_midfield_creativity_progression.png`](file:///c:/Users/Superuser/Desktop/Football%20Data%20Visualization%20Specialist/visuals/04_scatter_midfield_creativity_progression.png)
- **Methodology:** X-axis maps Progressive Passes/90 (10m+ forward passes into final third); Y-axis maps Expected Assists (xA/90); Bubble size corresponds to Expected Threat (xT/90).
- **Key Findings:**
  - *Cluster 1 (High Progression & Chance Creation):* Podolski, Antoni Kozubal (Lech Poznań), Bartosz Kapustka (Legia Warszawa), Afonso Sousa (Lech Poznań).
  - *Cluster 2 (Deep Circulation Engines):* Damian Rasak and Gustav Berggren (Raków) dominate progressive pass volume (>6.5/90) with balanced shot-creation metrics.

---

### 1.5 Undervalued Gems for Süper Lig Clubs
- **Visual Asset:** [`06_scatter_undervalued_super_lig_gems.png`](file:///c:/Users/Superuser/Desktop/Football%20Data%20Visualization%20Specialist/visuals/06_scatter_undervalued_super_lig_gems.png)
- **Strategic Quadrant:** Target Investment Zone (Market Value < €2.5M, Attacking Impact npxG+xA > 0.40/90).
- **Standout Targets:**
  - **Taofeek Ismaheel** (RW, Górnik Zabrze, €1.5M): 7.80 progressive carries/90, 0.52 npxG+xA/90. High-velocity 1v1 dribbler.
  - **Damian Rasak** (DM, Górnik Zabrze, €1.8M): Elite ball-winning transition profile.
  - **Dominik Szala** (CB/RB, Górnik Zabrze, €1.8M, Age 20): Polish youth international with 68.2% defensive duel success.

---

## 2. Pre-Match Opposition & Tactical Architecture

### 2.1 Starting XI Passing Network & Build-Up Shape
- **Visual Asset:** [`07_gornik_passing_network.png`](file:///c:/Users/Superuser/Desktop/Football%20Data%20Visualization%20Specialist/visuals/07_gornik_passing_network.png)
- **Tactical Structure:** Asymmetric 4-2-3-1 / 3-4-2-1 hybrid.
- **Key Interactions:**
  - Center-back Rafał Janicki connects directly with Erik Janża (14 passes) and Damian Rasak (19 passes).
  - Rasak and Patrik Hellebrand form a double-pivot exchange (33 combined passes), drawing the opposition forward.
  - Lukas Podolski receives between the lines (14 passes from Rasak, 12 from Janża), creating an immediate vertical release to striker Luka Zahović or switching diagonally to Taofeek Ismaheel.
- **Centralization Index:** **44.8%** — Demonstrates that build-up is highly structured through designated technical hubs rather than decentralized long balls.

---

### 2.2 Defensive Territory & PPDA Density Heatmap
- **Visual Asset:** [`08_gornik_defensive_territory_ppda.png`](file:///c:/Users/Superuser/Desktop/Football%20Data%20Visualization%20Specialist/visuals/08_gornik_defensive_territory_ppda.png)
- **Pressing Metrics:**
  - Team PPDA (Passes Allowed Per Defensive Action): **9.1** (Ekstraklasa rank: 4th; league median: 11.4).
  - High Press Turnovers: **9.5 / 90** (League rank: 3rd).
  - Mean Defensive Action Line: **46.8 meters** from own goal line.
  - Field Tilt: **54.2%** (Dominance of final-third territorial touches).
- **Tactical Vulnerability:**
  Because Janża pushes high to support the left-wing overload, the channel behind him is vulnerable if the opposition executes rapid diagonal switch balls into space before Rasak can shift across.

---

### 2.3 Expected Threat (xT) Spatial Pitch Grid
- **Visual Asset:** [`09_gornik_expected_threat_xt_grid.png`](file:///c:/Users/Superuser/Desktop/Football%20Data%20Visualization%20Specialist/visuals/09_gornik_expected_threat_xt_grid.png)
- **Framework:** Karun Singh Expected Threat Transition Matrix implemented on a 12×8 pitch grid.
- **Findings:**
  - Peak Threat Generation (+0.35 to +0.42 xT) occurs in the **left half-space** between 25m and 35m from the goal.
  - Zone 14 (+0.38 xT) serves as the central finishing filter. Opponents who compact Zone 14 reduce Górnik's danger by 38%, forcing them to rely on Janża crosses.

---

## 3. Match Performance & Post-Match Debrief

### 3.1 Shot Map & xG Constellation (Górnik Zabrze 2–1 Legia Warszawa)
- **Visual Asset:** [`10_match_shot_map_xg_constellation.png`](file:///c:/Users/Superuser/Desktop/Football%20Data%20Visualization%20Specialist/visuals/10_match_shot_map_xg_constellation.png)
- **Performance Breakdown:**
  - Górnik Zabrze: 14 Shots, 5 on Target, **2.15 xG**, 0.154 xG/Shot, 3 Big Chances.
  - Legia Warszawa: 10 Shots, 4 on Target, **1.18 xG**, 0.118 xG/Shot, 1 Big Chance.
- **Decisive Moments:**
  - 27' Luka Zahović (0.38 xG) — Open play cutback finish.
  - 58' Marc Gual (0.24 xG) — Legia counter-attack equalizer.
  - 81' Lukas Podolski (0.45 xG) — Left-foot thunderbolt following a high turnover won by Rasak.

---

### 3.2 Minute-by-Minute Cumulative xG Flow & Game Momentum
- **Visual Asset:** [`11_match_xg_flow_momentum.png`](file:///c:/Users/Superuser/Desktop/Football%20Data%20Visualization%20Specialist/visuals/11_match_xg_flow_momentum.png)
- **Game State Dynamics:**
  - **Minutes 0–45:** Górnik established sustained game control (+0.6 momentum index), generating 0.85 xG before the interval.
  - **Minutes 46–65:** Legia introduced tactical tweaks, pressing higher and scoring at minute 58 (momentum dropped to -0.7).
  - **Minutes 66–90:** Urban's substitutions and Podolski's central leadership swung momentum decisively back (+0.9), creating 1.10 xG in the final 20 minutes to secure all 3 points.

---

## 4. League Macro Analytics & AI Modeling

### 4.1 Ekstraklasa xG Performance Quadrant (18 Teams)
- **Visual Asset:** [`12_ekstraklasa_xg_quadrant_matrix.png`](file:///c:/Users/Superuser/Desktop/Football%20Data%20Visualization%20Specialist/visuals/12_ekstraklasa_xg_quadrant_matrix.png)
- **Analysis:**
  - Górnik Zabrze occupies the **Dominant Contenders** quadrant (+1.53 xG/90 created vs 1.02 xGA/90 conceded), proving their top-5 status is founded on sustainable underlying processes rather than statistical variance.
  - Lech Poznań and Raków Częstochowa represent the defensive elite of Central Europe (Raków conceding only 0.70 xGA/90).

---

### 4.2 AI Player Archetype Clustering (K-Means & PCA)
- **Visual Asset:** [`13_ai_player_archetype_clusters.png`](file:///c:/Users/Superuser/Desktop/Football%20Data%20Visualization%20Specialist/visuals/13_ai_player_archetype_clusters.png)
- **Machine Learning Architecture:**
  - 10 standardized performance features per 90 minutes.
  - Unsupervised K-Means ($k=4$) with PCA dimensionality reduction capturing 63.0% of total variance across 140 players.
- **Identified Clusters:**
  1. *Playmakers & Creators* (Podolski, Sousa, Kapustka)
  2. *Defensive Anchors & Stopper Pivots* (Dominik Szala, Augustyniak, Szcześniak)
  3. *Box-to-Box Transition Engines* (Damian Rasak, Gustav Berggren, Romanczuk)
  4. *Dynamic 1v1 Carriers & Wingers* (Taofeek Ismaheel, Kamil Grosicki, Kamil Lukoszek)
- **Recruitment Application:**
  Allows a Turkish Süper Lig technical director to input the statistical signature of a departed or injured star and instantly retrieve mathematically identical targets across Central and Eastern Europe.

---

## 5. Artifact Directory & File Manifest

| File / Asset | Format | Description |
|---|---|---|
| [`Zafer_Yorganci_Football_CV.pdf`](file:///c:/Users/Superuser/Desktop/Football%20Data%20Visualization%20Specialist/Zafer_Yorganci_Football_CV.pdf) | PDF (2 Pages) | Tailored Football Data & AI Engineer CV |
| [`Gornik_Zabrze_Ekstraklasa_2025_2026_Portfolio.pdf`](file:///c:/Users/Superuser/Desktop/Football%20Data%20Visualization%20Specialist/Gornik_Zabrze_Ekstraklasa_2025_2026_Portfolio.pdf) | PDF (13 Pages) | Complete Visual & Tactical Portfolio Dossier |
| [`Zafer_Yorganci_Cover_Letter_Super_Lig.pdf`](file:///c:/Users/Superuser/Desktop/Football%20Data%20Visualization%20Specialist/Zafer_Yorganci_Cover_Letter_Super_Lig.pdf) | PDF (2 Pages) | Dual-language Süper Lig Application Cover Letter |
| `visuals/01_pizza_radar_damian_rasak.png` | PNG (300 DPI) | Damian Rasak Percentile Pizza Radar |
| `visuals/02_pizza_radar_lukas_podolski.png` | PNG (300 DPI) | Lukas Podolski Percentile Pizza Radar |
| `visuals/03_pizza_radar_erik_janza.png` | PNG (300 DPI) | Erik Janża Percentile Pizza Radar |
| `visuals/04_scatter_midfield_creativity_progression.png` | PNG (300 DPI) | Midfield Creativity vs Progression Scatter |
| `visuals/05_scatter_pressing_recoveries.png` | PNG (300 DPI) | Defensive Activity vs Duel Win % Scatter |
| `visuals/06_scatter_undervalued_super_lig_gems.png` | PNG (300 DPI) | Transfer Value vs Attacking Threat Scatter |
| `visuals/07_gornik_passing_network.png` | PNG (300 DPI) | Górnik Zabrze Starting XI Passing Network |
| `visuals/08_gornik_defensive_territory_ppda.png` | PNG (300 DPI) | Defensive Territory & PPDA Density Map |
| `visuals/09_gornik_expected_threat_xt_grid.png` | PNG (300 DPI) | Open-Play Expected Threat (xT) Pitch Grid |
| `visuals/10_match_shot_map_xg_constellation.png` | PNG (300 DPI) | Górnik Zabrze 2–1 Legia Shot Constellation |
| `visuals/11_match_xg_flow_momentum.png` | PNG (300 DPI) | Cumulative xG Flow & Momentum Timeline |
| `visuals/12_ekstraklasa_xg_quadrant_matrix.png` | PNG (300 DPI) | Ekstraklasa xG Performance Quadrant |
| `visuals/13_ai_player_archetype_clusters.png` | PNG (300 DPI) | AI Machine Learning Archetype Clusters |
| `scripts/generate_all_visuals.py` | Python Script | Master Script to regenerate all 12+ visuals |
| `portfolio/index.html` | Interactive Web UI | Standalone Interactive Portfolio Application |
