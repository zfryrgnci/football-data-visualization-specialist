# Zafer Yorgancı | Football Data Visualization Specialist & AI Engineer

<div align="center">

[![Python](https://img.shields.io/badge/Python-3.11%20%7C%203.12-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white)](https://pytorch.org)
[![OpenCV](https://img.shields.io/badge/OpenCV-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white)](https://opencv.org)
[![YOLOv11](https://img.shields.io/badge/YOLOv11-Roboflow%20Sports-00F5D4?style=for-the-badge)](https://github.com/roboflow/sports)
[![mplsoccer](https://img.shields.io/badge/mplsoccer-StatsBomb%20%7C%20Opta-10B981?style=for-the-badge)](https://mplsoccer.readthedocs.io)
[![Golazo](https://img.shields.io/badge/Golazo-Aesthetics-F72585?style=for-the-badge)](https://github.com/0xjuanma/golazo)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)

**Elite Technical Intelligence, Computer Vision Optical Tracking & Advanced Spatial Analytics in Professional Football**

[Portfolio Repository](https://github.com/zfryrgnci/football-data-visualization-specialist) • [LinkedIn Profile](https://www.linkedin.com) • [Email Contact](mailto:yorgancizafer1@gmail.com) • [English CV (PDF)](./Zafer_Yorganci_Football_CV_EN.pdf) • [Türkçe CV (PDF)](./Zafer_Yorganci_Futbol_CV_TR.pdf)

</div>

---

## ⚽ Professional Profile & Club Experience

I am a **Football Data Visualization Specialist and AI Engineer** specializing in transforming raw broadcast tracking and multi-provider event streams (StatsBomb, Opta, Wyscout, Transfermarkt) into **actionable tactical intelligence for Head Coaches, Sporting Directors, and Head of Recruitment**.

### 🏟️ Recent Experience: Górnik Zabrze (Ekstraklasa 2025–2026 Season)
* **Role:** Sport Data Visualization Specialist & Performance Consultant (Remote)
* **Scope of Deliverables:**
  * **Pre-Match Opposition Tactical Dossiers:** High-press triggers, defensive line spacing, goalkeeper distribution tendencies, and set-piece marking vulnerabilities.
  * **Post-Match Spatial Deconstruction:** Real-time Voronoi pitch control, team shape convex hulls (width/depth/compactness in $m^2$), and 360° polar pass sonars for midfield engines (Damian Rasak, Patrik Hellebrand, Erik Janża).
  * **Recruitment & Market Arbitrage:** Algorithmic player clustering, age curve lifecycle profiling, and multi-league valuation frontiers for Turkish Süper Lig transfer targets.

---

## 🔬 Benchmark Methodology & Architectural Pillars

My visualization architecture synthesizes the elite standards of four foundational industry benchmarks:

```
                  ┌────────────────────────────────────────────────────────┐
                  │              ZAFER YORGANCI ANALYTICS STACK            │
                  └────────────────────────────────────────────────────────┘
                                               │
         ┌──────────────────┬──────────────────┴──────────────────┬──────────────────┐
         ▼                  ▼                                     ▼                  ▼
┌─────────────────┐┌─────────────────┐                  ┌─────────────────┐┌─────────────────┐
│ ROBOFLOW SPORTS ││   EDD WEBSTER   │                  │  0xJUANMA GOLAZO││ worldfootballR  │
│ Computer Vision ││ Spatial Control │                  │ High-End Design ││ Data Pipelines  │
│  & Homography   ││ & Pass Sonars   │                  │  & Markov xT    ││  & Recruitment  │
└─────────────────┘└─────────────────┘                  └─────────────────┘└─────────────────┘
```

### 1. 🎥 Computer Vision & Perspective Homography (`roboflow/sports`)
* **Broadcast Optical Tracking:** Automated player, goalkeeper, referee, and ball detection using fine-tuned **YOLOv11x + ByteTrack**.
* **Direct Linear Transform (DLT) Homography:** Planar homography matrix $H \in \mathbb{R}^{3 \times 3}$ projecting camera pixel coordinates $[u, v, 1]^T$ into metric top-down pitch coordinates $[X, Y, 1]^T$ on a FIFA standard $105 \times 68\,m$ surface with $< 0.15\,m$ reprojection error.
* **Instantaneous Kinematics:** Player velocity vectors ($\vec{v}$ in $m/s$), acceleration bursts, and pressing distance metrics.

<div align="center">
  <img src="./visuals/17_roboflow_cv_broadcast_homography_radar.png" width="95%" alt="Roboflow CV Homography Radar Minimap" />
  <p><em>Figure 1: Dual-view tactical pipeline — Broadcast camera bounding boxes & pitch keypoints (Left) mapped to 2D Top-Down Metric Radar with velocity vectors (Right).</em></p>
</div>

---

### 2. 📐 Spatial Pitch Control & Tactical Convex Hulls (`eddwebster/football_analytics`)
* **Voronoi Space Dominance:** Continuous territorial partitioning evaluating spatial control percentages between possession phase and defensive low blocks.
* **Convex Hull Geometry:** Dynamic measurement of team tactical shape, including outfield compactness area ($m^2$), defensive line depth ($m$), and lateral stretch ($m$).
* **Ball Carrier Progression Cones:** Passing lane probability vectors from deep anchors (Damian Rasak) to half-space creators (Lukas Podolski).

<div align="center">
  <img src="./visuals/18_eddwebster_voronoi_pitch_control_convex_hulls.png" width="95%" alt="Voronoi Pitch Control and Convex Hulls" />
  <p><em>Figure 2: Voronoi pitch control tessellation and tactical convex hulls for Górnik Zabrze vs compact defensive opponent block.</em></p>
</div>

---

### 3. 🧭 360° Polar Pass Sonars & Progression Wheel (`eddwebster` & `0xjuanma/golazo`)
* **Angular Directionality:** 12 discrete $30^\circ$ angular sectors measuring passing frequency and progressive intention.
* **Bivariate Length Encoding:** Wedge distance colored by average pass length in meters (short circulation vs long diagonal switches) normalized across 90-minute outputs.
* **Midfield Engine Profiles:** Direct comparative analysis between defensive ball-winners (Damian Rasak), central progressors (Patrik Hellebrand), attacking crossers (Erik Janża), and 1v1 wingers (Taofeek Ismaheel).

<div align="center">
  <img src="./visuals/19_pass_sonar_midfield_engine.png" width="95%" alt="Tactical Pass Sonars" />
  <p><em>Figure 3: Tactical Pass Sonars demonstrating 360-degree passing angles, completion rates, and average distance for Górnik Zabrze midfield.</em></p>
</div>

---

### 4. ⚡ Markov Chain Expected Threat (xT) & Progression Corridors (`0xjuanma/golazo`)
* **Karun Singh 16x12 Transition Matrix:** Spatial value surface quantifying probability of a goal being scored within the next $N$ actions originating from pitch cell $(x, y)$.
* **Zone 14 Penetration Channels:** Highlighting progressive line-breaking passes, half-space underlaps, and cutbacks generating $> +0.25\,xT$ per action.

<div align="center">
  <img src="./visuals/20_markov_xt_progression_channels.png" width="95%" alt="Markov Chain Expected Threat Grid" />
  <p><em>Figure 4: 16x12 Karun Singh Expected Threat (xT) transition matrix and key progression channels for Górnik Zabrze.</em></p>
</div>

---

### 5. 🎯 Bivariate Shot Quality & Defender Pressure Constellation (`0xjuanma/golazo`)
* **Dual-Variable Encoding:** Bubble radius scales proportionally with Expected Goals ($xG$); bubble fill represents defensive pressure density index ($0.0 - 1.0$) at the exact moment of ball strike.
* **Finishing Efficiency:** Comparison between post-shot expected goals ($PSxG$) and actual goal conversion (+1.14 $xG$ overperformance).

<div align="center">
  <img src="./visuals/21_bivariate_shot_quality_pressure.png" width="90%" alt="Bivariate Shot Map" />
  <p><em>Figure 5: Vertical attacking half-pitch bivariate shot map with defensive pressure density and finishing efficiency.</em></p>
</div>

---

### 6. 💰 Recruitment Frontier & Market Arbitrage (`JaseZiv/worldfootballR`)
* **Cross-League Valuation Frontier:** Automated data pipelines merging Transfermarkt valuations with FBref/StatsBomb composite performance indices.
* **Turkish Süper Lig Transfer Arbitrage:** Identifying high-impact, undervalued profiles across Central and Eastern Europe (Ekstraklasa, Fortuna Liga, HNL) with high tactical compatibility for Galatasaray, Fenerbahçe, Beşiktaş, and Trabzonspor.

<div align="center">
  <img src="./visuals/22_worldfootballr_recruitment_frontier.png" width="95%" alt="Recruitment Frontier" />
  <p><em>Figure 6: Cross-league scouting frontier highlighting undervalued gems and recruitment sweet spots for Turkish Süper Lig clubs.</em></p>
</div>

---

## 🛠️ Technical Stack & Tooling

| Domain | Technologies & Libraries |
| :--- | :--- |
| **Computer Vision & Tracking** | Python 3.11+, PyTorch, YOLOv11x, ByteTrack, OpenCV, Direct Linear Transform (DLT), Homography Matrix Estimation |
| **Spatial & Pitch Analytics** | `mplsoccer`, `scipy.spatial` (Voronoi, Delaunay, ConvexHull), NumPy, Pandas, Matplotlib, Seaborn |
| **Advanced Models** | Karun Singh Markov xT, Bivariate xG, Expected Assists (xA), PPDA Pressing Intensity, k-Means Archetype Clustering |
| **Data Scraping & Ingestion** | `worldfootballR`, FBref API, Transfermarkt Scraper, Understat, StatsBomb Open Data, Opta Event Schemas |
| **Dossier & Report Delivery** | Headless Playwright PDF Engine, publication CSS Grid / Flexbox, SVG vector rendering, A4 Print Optimization |

---

## 📂 Repository Structure

```
├── .github/
│   └── workflows/
│       └── verify_analytics.yml     # Automated CI verification of analytics scripts
├── data/
│   ├── ekstraklasa_2025_2026_players.csv   # Polish league player season stats
│   ├── ekstraklasa_2025_2026_teams.csv     # League table & tactical macro metrics
│   └── gornik_match_events.json            # Match tracking & event coordinates
├── scripts/
│   ├── 1_recruitment_scouting.py           # Pizza radars, scatter plots, undervalued gems
│   ├── 2_tactical_opposition.py            # Passing networks, PPDA defensive territory
│   ├── 3_match_performance.py              # Shot constellation, xG momentum flow
│   ├── 4_league_macro_analytics.py         # Ekstraklasa xG quadrant matrices
│   ├── 5_coach_and_scouting_specialties.py  # k-Means player clusters, set pieces, age curves
│   └── 6_advanced_cv_and_spatial_analytics.py # CV tracking, Voronoi pitch control, Pass sonars, Markov xT
├── src/
│   ├── cv_tracking/                        # Computer vision & homography transforms
│   ├── spatial/                            # Voronoi tessellation & convex hulls
│   ├── event_models/                       # Pass sonars & Karun Singh xT
│   └── scouting/                           # Multi-league valuation frontiers
├── visuals/                                # 22 High-Resolution 300 DPI Tactical Visuals
├── Zafer_Yorganci_Football_CV_EN.pdf       # Professional Football CV (English)
├── Zafer_Yorganci_Futbol_CV_TR.pdf         # Profesyonel Futbol CV (Türkçe)
└── Zafer_Yorganci_Technical_Intelligence_Dossier_2026_EN.pdf # Club Application Briefing
```

---

## 📬 Contact & Club Inquiries

* **Candidate:** Zafer Yorgancı
* **Target Position:** Football Data Visualization Specialist / AI Performance Engineer
* **Target Competitions:** Turkish Süper Lig (Galatasaray, Fenerbahçe, Beşiktaş, Trabzonspor, Başakşehir) & European Leagues
* **Email:** [yorgancizafer1@gmail.com](mailto:yorgancizafer1@gmail.com)
* **GitHub:** [https://github.com/zfryrgnci](https://github.com/zfryrgnci)

*Ready to deploy automated data pipelines, custom tactical visuals, and computer vision tracking for immediate competitive advantage.*
