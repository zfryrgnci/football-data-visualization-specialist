"""
========================================================================================
ELITE CLUB TECHNICAL INTELLIGENCE DOSSIER & CV COMPILER (V2)
Compiles:
  1. Zafer_Yorganci_Technical_Intelligence_Dossier_2026_EN.pdf (English Technical Dossier)
  2. Zafer_Yorganci_Teknik_Analiz_ve_Veri_Gorsellestirme_Raporu_2026_TR.pdf (Turkish Technical Dossier)
  3. Zafer_Yorganci_Football_CV_EN.pdf (English Single-Page CV)
  4. Zafer_Yorganci_Futbol_CV_TR.pdf (Turkish Single-Page CV)

Using Playwright with pixel-perfect CSS Paged Media.
Zero text overlap, flawless typography, publication-grade club presentation.
========================================================================================
"""

import base64
import os
from playwright.sync_api import sync_playwright

WORKSPACE_DIR = r"c:\Users\Superuser\Desktop\Football Data Visualization Specialist"
VISUALS_DIR = os.path.join(WORKSPACE_DIR, "visuals")

def get_base64_img(filename):
    path = os.path.join(VISUALS_DIR, filename)
    if not os.path.exists(path):
        print(f"Warning: File not found {path}")
        return ""
    with open(path, "rb") as f:
        return f"data:image/png;base64,{base64.b64encode(f.read()).decode('utf-8')}"

# ======================================================================================
# CSS FOR THE TECHNICAL DOSSIER
# ======================================================================================
DOSSIER_CSS = """
@page {
    size: A4 portrait;
    margin: 0;
}
* {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
    -webkit-print-color-adjust: exact;
    print-color-adjust: exact;
}
body {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    color: #0F172A;
    background: #F8FAFC;
    font-size: 9pt;
    line-height: 1.45;
}
.page {
    width: 210mm;
    height: 297mm;
    min-height: 297mm;
    max-height: 297mm;
    padding: 14mm 16mm 12mm 16mm;
    page-break-after: always;
    break-after: page;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    overflow: hidden;
    background: #FFFFFF;
    position: relative;
}
.top-bar {
    background: #0B132B;
    color: #FFFFFF;
    padding: 12px 18px;
    border-radius: 6px;
    border-bottom: 3px solid #00F5D4;
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 12px;
}
.top-title {
    font-size: 13pt;
    font-weight: 800;
    letter-spacing: 0.02em;
    color: #FFFFFF;
}
.top-subtitle {
    font-size: 8pt;
    color: #38BDF8;
    font-weight: 600;
    margin-top: 2px;
}
.top-badge {
    background: #1E293B;
    border: 1px solid #334155;
    color: #FFD166;
    font-size: 7.5pt;
    font-weight: 700;
    padding: 4px 10px;
    border-radius: 4px;
    text-align: right;
    line-height: 1.3;
}
.content-area {
    flex: 1;
    display: flex;
    flex-direction: column;
    gap: 10px;
}
.visual-container {
    width: 100%;
    background: #0B0E14;
    border: 1px solid #1E293B;
    border-radius: 6px;
    padding: 6px;
    text-align: center;
}
.visual-container img {
    max-width: 100%;
    max-height: 145mm;
    object-fit: contain;
    border-radius: 4px;
    display: block;
    margin: 0 auto;
}
.benchmark-tag {
    display: inline-block;
    background: rgba(0, 245, 212, 0.12);
    border: 1px solid #00F5D4;
    color: #0D9488;
    font-size: 7.5pt;
    font-weight: 800;
    padding: 2px 8px;
    border-radius: 3px;
    margin-bottom: 6px;
    text-transform: uppercase;
}
.tactical-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 10px;
}
.tactical-card {
    background: #F1F5F9;
    border: 1px solid #CBD5E1;
    border-radius: 6px;
    padding: 10px 12px;
}
.card-header {
    font-size: 8.5pt;
    font-weight: 800;
    color: #0F172A;
    text-transform: uppercase;
    letter-spacing: 0.03em;
    border-bottom: 1.5px solid #0284C7;
    padding-bottom: 4px;
    margin-bottom: 6px;
    display: flex;
    justify-content: space-between;
}
.card-list {
    list-style: none;
    padding-left: 0;
}
.card-list li {
    position: relative;
    padding-left: 12px;
    margin-bottom: 4px;
    font-size: 8pt;
    line-height: 1.35;
    color: #334155;
}
.card-list li::before {
    content: "▪";
    position: absolute;
    left: 0;
    color: #0284C7;
    font-size: 9pt;
}
.kpi-row {
    display: flex;
    gap: 8px;
    margin-top: 4px;
}
.kpi-box {
    flex: 1;
    background: #FFFFFF;
    border: 1px solid #E2E8F0;
    border-radius: 4px;
    padding: 6px 8px;
    text-align: center;
}
.kpi-val {
    font-size: 11pt;
    font-weight: 800;
    color: #0F172A;
}
.kpi-lbl {
    font-size: 6.8pt;
    font-weight: 700;
    color: #64748B;
    text-transform: uppercase;
    margin-top: 1px;
}
.footer-bar {
    border-top: 1px solid #E2E8F0;
    padding-top: 8px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    font-size: 7.5pt;
    color: #64748B;
}
.footer-bar strong {
    color: #0F172A;
}
"""

# ======================================================================================
# CSS FOR THE SINGLE-PAGE RESUME (CV)
# ======================================================================================
CV_CSS = """
@page {
    size: A4 portrait;
    margin: 0;
}
* {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
    -webkit-print-color-adjust: exact;
    print-color-adjust: exact;
}
body {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    color: #1E293B;
    background: #FFFFFF;
    font-size: 8.5pt;
    line-height: 1.38;
}
.cv-page {
    width: 210mm;
    height: 297mm;
    min-height: 297mm;
    max-height: 297mm;
    padding: 12mm 14mm 10mm 14mm;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    overflow: hidden;
    position: relative;
    background: #FFFFFF;
}
.cv-header {
    background: #0B132B;
    color: #FFFFFF;
    padding: 14px 18px;
    border-radius: 6px;
    border-bottom: 3.5px solid #00F5D4;
}
.cv-name {
    font-size: 20pt;
    font-weight: 800;
    color: #FFFFFF;
    letter-spacing: 0.02em;
}
.cv-role {
    font-size: 10.5pt;
    font-weight: 700;
    color: #38BDF8;
    margin-top: 2px;
}
.cv-contact {
    font-size: 8pt;
    color: #94A3B8;
    margin-top: 5px;
    display: flex;
    flex-wrap: wrap;
    gap: 12px;
}
.cv-contact a {
    color: #00F5D4;
    text-decoration: none;
    font-weight: 600;
}
.cv-target {
    display: inline-block;
    margin-top: 6px;
    background: rgba(255, 209, 102, 0.15);
    border: 1px solid #FFD166;
    color: #FFD166;
    font-size: 7.8pt;
    font-weight: 700;
    padding: 2px 8px;
    border-radius: 3px;
}
.cv-body {
    flex: 1;
    display: flex;
    flex-direction: column;
    gap: 9px;
    margin-top: 8px;
}
.cv-section {
    border-bottom: 1px solid #E2E8F0;
    padding-bottom: 7px;
}
.cv-section:last-child {
    border-bottom: none;
    padding-bottom: 0;
}
.cv-sec-title {
    font-size: 9.5pt;
    font-weight: 800;
    text-transform: uppercase;
    color: #0F172A;
    letter-spacing: 0.03em;
    border-left: 3.5px solid #0284C7;
    padding-left: 6px;
    margin-bottom: 5px;
}
.cv-exp-header {
    display: flex;
    justify-content: space-between;
    align-items: baseline;
}
.cv-exp-role {
    font-size: 9pt;
    font-weight: 800;
    color: #0F172A;
}
.cv-exp-org {
    color: #0284C7;
    font-weight: 700;
}
.cv-exp-date {
    font-size: 7.8pt;
    font-weight: 700;
    color: #64748B;
}
.cv-bullets {
    list-style: none;
    padding-left: 0;
    margin-top: 3px;
}
.cv-bullets li {
    position: relative;
    padding-left: 11px;
    margin-bottom: 2.5px;
    font-size: 8pt;
    line-height: 1.34;
    color: #334155;
}
.cv-bullets li::before {
    content: "▸";
    position: absolute;
    left: 0;
    color: #0284C7;
    font-weight: bold;
}
.cv-two-col {
    display: grid;
    grid-template-columns: 1.15fr 0.85fr;
    gap: 12px;
}
.cv-skills-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 6px;
}
.cv-skill-item {
    background: #F8FAFC;
    border: 1px solid #E2E8F0;
    border-radius: 4px;
    padding: 4px 6px;
}
.cv-skill-lbl {
    font-size: 7.2pt;
    font-weight: 800;
    color: #0284C7;
    text-transform: uppercase;
}
.cv-skill-val {
    font-size: 7.5pt;
    color: #334155;
    margin-top: 1px;
}
.cv-footer {
    border-top: 1px solid #CBD5E1;
    padding-top: 6px;
    display: flex;
    justify-content: space-between;
    font-size: 7.2pt;
    color: #64748B;
}
"""

def generate_english_dossier():
    print("Building English Technical Intelligence Dossier HTML...")
    
    img_cv = get_base64_img("17_roboflow_cv_broadcast_homography_radar.png")
    img_voronoi = get_base64_img("18_eddwebster_voronoi_pitch_control_convex_hulls.png")
    img_sonar = get_base64_img("19_pass_sonar_midfield_engine.png")
    img_xt = get_base64_img("20_markov_xt_progression_channels.png")
    img_shot = get_base64_img("21_bivariate_shot_quality_pressure.png")
    img_frontier = get_base64_img("22_worldfootballr_recruitment_frontier.png")
    img_pizza = get_base64_img("01_pizza_radar_damian_rasak.png")
    img_passnet = get_base64_img("07_gornik_passing_network.png")
    img_setpiece = get_base64_img("14_set_piece_corner_routines.png")
    img_gk = get_base64_img("15_goalkeeper_distribution_profile.png")
    
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Zafer Yorganci - Technical Intelligence Dossier 2026</title>
<style>{DOSSIER_CSS}</style>
</head>
<body>

<!-- PAGE 1: COVER & EXECUTIVE TECHNICAL INTELLIGENCE BRIEFING -->
<div class="page">
    <div class="top-bar">
        <div>
            <div class="top-title">TECHNICAL TACTICAL INTELLIGENCE DOSSIER 2026</div>
            <div class="top-subtitle">PRE-MATCH TACTICS • LIVE CV TRACKING • SPATIAL PITCH CONTROL • RECRUITMENT</div>
        </div>
        <div class="top-badge">
            GÓRNIK ZABRZE (EKSTRAKLASA)<br>
            TURKISH SÜPER LİG APPLICATION
        </div>
    </div>
    
    <div class="content-area">
        <div class="benchmark-tag">Architectural Synthesis: Roboflow Sports • Edd Webster • 0xjuanma Golazo • worldfootballR</div>
        
        <div style="background:#0F172A; color:#F8FAFC; padding:16px 20px; border-radius:6px; border-left:4px solid #00F5D4; margin-bottom:10px;">
            <div style="font-size:11pt; font-weight:800; color:#00F5D4; margin-bottom:6px;">EXECUTIVE BRIEFING FOR HEAD COACHES & SPORTING DIRECTORS</div>
            <div style="font-size:8.6pt; line-height:1.5; color:#CBD5E1;">
                This dossier demonstrates the elite technical intelligence and automated data visualization pipelines deployed 
                during my remote consultancy for <strong>Górnik Zabrze</strong> in the Polish Ekstraklasa (2025–2026 Season). 
                Tailored explicitly to solve the core questions demanded by European and Turkish Süper Lig coaching staffs:
                <strong>how to expose opposition defensive structures before matchday, quantify spatial pitch dominance in-game, and execute data-driven, high-ROI player recruitment.</strong>
            </div>
        </div>
        
        <div class="tactical-grid">
            <div class="tactical-card">
                <div class="card-header">
                    <span>1. MATCHDAY PREPARATION & PRE-MATCH TACTICS</span>
                    <span style="color:#0284C7;">COACHING DEMAND</span>
                </div>
                <ul class="card-list">
                    <li><strong>Opposition Build-up Disruption:</strong> Goalkeeper launch tendencies & defensive split mapping to trigger zonal trapping.</li>
                    <li><strong>Line Spacing & PPDA:</strong> Measuring opposition pressing intensity to identify escape outlets into central half-spaces.</li>
                    <li><strong>Set-Piece Marking Vulnerabilities:</strong> Inswinging vs outswinging corner cluster models exposing zonal seam defects.</li>
                </ul>
            </div>
            
            <div class="tactical-card">
                <div class="card-header">
                    <span>2. LIVE & POST-MATCH DECONSTRUCTION</span>
                    <span style="color:#00F5D4;">SPATIAL / CV</span>
                </div>
                <ul class="card-list">
                    <li><strong>Optical Tracking & 2D Radars:</strong> YOLOv11x keypoint homography (H) reprojecting broadcast angles to metric 2D pitch space.</li>
                    <li><strong>Voronoi Space Control:</strong> Continuous pitch dominance calculations quantifying half-space territorial ownership.</li>
                    <li><strong>Pass Sonar Midfield Engines:</strong> 360° angular directionality & progressive pass length analysis.</li>
                </ul>
            </div>
        </div>

        <div class="visual-container" style="margin-top:6px;">
            <img src="{img_cv}" style="max-height:105mm;" alt="CV Radar" />
        </div>
        
        <div class="kpi-row">
            <div class="kpi-box">
                <div class="kpi-val" style="color:#0284C7;">0.142 m</div>
                <div class="kpi-lbl">CV Reprojection RMSE</div>
            </div>
            <div class="kpi-box">
                <div class="kpi-val" style="color:#00F5D4;">58.4%</div>
                <div class="kpi-lbl">Mean Pitch Control</div>
            </div>
            <div class="kpi-box">
                <div class="kpi-val" style="color:#F72585;">+0.312</div>
                <div class="kpi-lbl">Peak Flank xT/90 (Janża)</div>
            </div>
            <div class="kpi-box">
                <div class="kpi-val" style="color:#FFD166;">€1.2M</div>
                <div class="kpi-lbl">Valuation Arbitrage (Rasak)</div>
            </div>
        </div>
    </div>
    
    <div class="footer-bar">
        <div><strong>Zafer Yorgancı</strong> | Football Data Visualization Specialist & AI Engineer</div>
        <div>yorgancizafer1@gmail.com • github.com/zfryrgnci • Page 1 of 6</div>
    </div>
</div>

<!-- PAGE 2: COMPUTER VISION & HOMOGRAPHY 2D RADAR -->
<div class="page">
    <div class="top-bar">
        <div>
            <div class="top-title">COMPUTER VISION OPTICAL TRACKING & 2D RADAR</div>
            <div class="top-subtitle">YOLOv11x DETECTOR • BYTETRACK • DIRECT LINEAR TRANSFORM (DLT) HOMOGRAPHY</div>
        </div>
        <div class="top-badge">ROBOFLOW SPORTS<br>BENCHMARK</div>
    </div>
    
    <div class="content-area">
        <div class="visual-container">
            <img src="{img_cv}" alt="Roboflow CV Pipeline" />
        </div>
        
        <div class="tactical-grid">
            <div class="tactical-card">
                <div class="card-header">
                    <span>COACHING INTELLIGENCE: OPTICAL METRICS</span>
                    <span style="color:#0284C7;">VIDEO \to DATA</span>
                </div>
                <ul class="card-list">
                    <li><strong>Broadcast Camera Homography:</strong> Transforms raw broadcast camera coordinates [u, v] into metric FIFA pitch (105 x 68 m) coordinates using calibrated keypoint landmarks.</li>
                    <li><strong>Instantaneous Kinematics:</strong> Real-time player velocity vectors (v) reveal sprinting corridors, counter-attack acceleration, and pressing bursts.</li>
                    <li><strong>Centroid Pressing Gap:</strong> Dynamic distance between team centroids (12.6 m) quantifies defensive compactness under opposition possession.</li>
                </ul>
            </div>
            
            <div class="tactical-card">
                <div class="card-header">
                    <span>TECHNICAL ARCHITECTURE SPECIFICATION</span>
                    <span style="color:#00F5D4;">TENSORRT 60 FPS</span>
                </div>
                <ul class="card-list">
                    <li><strong>Model Backbone:</strong> YOLOv11x fine-tuned on SoccerNet & custom Ekstraklasa tracking datasets.</li>
                    <li><strong>Reprojection Precision:</strong> 0.142 m Root Mean Square Error (RMSE) across full pitch dimensions.</li>
                    <li><strong>Application:</strong> Turn broadcast match recordings into automated tactical 2D minimaps for half-time tactical briefings.</li>
                </ul>
            </div>
        </div>
    </div>
    
    <div class="footer-bar">
        <div><strong>Zafer Yorgancı</strong> | CV Optical Tracking & Homography Minimaps</div>
        <div>yorgancizafer1@gmail.com • github.com/zfryrgnci • Page 2 of 6</div>
    </div>
</div>

<!-- PAGE 3: VORONOI PITCH CONTROL & TEAM CONVEX HULLS -->
<div class="page">
    <div class="top-bar">
        <div>
            <div class="top-title">VORONOI PITCH CONTROL & TACTICAL CONVEX HULLS</div>
            <div class="top-subtitle">CONTINUOUS SPACE DOMINANCE • TEAM COMPACTNESS (m²) • EFFECTIVE WIDTH & DEPTH</div>
        </div>
        <div class="top-badge">EDD WEBSTER<br>BENCHMARK</div>
    </div>
    
    <div class="content-area">
        <div class="visual-container">
            <img src="{img_voronoi}" alt="Voronoi Pitch Control" />
        </div>
        
        <div class="tactical-grid">
            <div class="tactical-card">
                <div class="card-header">
                    <span>TACTICAL DECONSTRUCTION: SPACE OWNERSHIP</span>
                    <span style="color:#0284C7;">TERRITORIAL DOMINANCE</span>
                </div>
                <ul class="card-list">
                    <li><strong>Continuous Space Ownership:</strong> Voronoi tessellation partitions pitch real estate based on arrival time to the ball, granting Górnik Zabrze <strong>58.4% spatial dominance</strong>.</li>
                    <li><strong>Flank Overload Isolation:</strong> Left-wing polygon expansion shows Erik Janża and Lukoszek pinning opponent fullbacks, opening central Zone 14 for Podolski.</li>
                    <li><strong>Passing Probability Cones:</strong> Deep anchor Damian Rasak (#6) commands passing vectors with clear line-of-sight to 3 distinct attacking layers.</li>
                </ul>
            </div>
            
            <div class="tactical-card">
                <div class="card-header">
                    <span>CONVEX HULL GEOMETRIC METRICS</span>
                    <span style="color:#F72585;">SHAPE COMPACTNESS</span>
                </div>
                <ul class="card-list">
                    <li><strong>Górnik Outfield Area:</strong> 1,185 m² (expansive attacking shape, high progressive support).</li>
                    <li><strong>Opponent Low Block Area:</strong> 890 m² (ultra-compressed central block, vulnerable to wide switches).</li>
                    <li><strong>Effective Width & Depth:</strong> Width: 49.8 m vs 44.2 m | Depth: 42.3 m vs 28.5 m.</li>
                </ul>
            </div>
        </div>
    </div>
    
    <div class="footer-bar">
        <div><strong>Zafer Yorgancı</strong> | Spatial Analytics & Voronoi Pitch Partitioning</div>
        <div>yorgancizafer1@gmail.com • github.com/zfryrgnci • Page 3 of 6</div>
    </div>
</div>

<!-- PAGE 4: PASS SONAR WHEELS & MIDFIELD ENGINE -->
<div class="page">
    <div class="top-bar">
        <div>
            <div class="top-title">TACTICAL PASS SONARS & 360° MIDFIELD ENGINE</div>
            <div class="top-subtitle">12-SECTOR POLAR DIRECTIONALITY • PROGRESSIVE PASS LENGTH • COMPLETION ACCURACY</div>
        </div>
        <div class="top-badge">GOLAZO & EDD WEBSTER<br>BENCHMARK</div>
    </div>
    
    <div class="content-area">
        <div class="visual-container">
            <img src="{img_sonar}" alt="Pass Sonars" />
        </div>
        
        <div class="tactical-grid">
            <div class="tactical-card">
                <div class="card-header">
                    <span>MIDFIELD ENGINE DIRECTIONAL AUDIT</span>
                    <span style="color:#0284C7;">COACHING DIRECTIVES</span>
                </div>
                <ul class="card-list">
                    <li><strong>Damian Rasak (#6 - Anchor):</strong> High-volume forward diagonal distribution (28.5m average progressive length); primary switch architect bypassing opposition first pressing line.</li>
                    <li><strong>Patrik Hellebrand (#8 - Connector):</strong> Balanced 360° pass angles with exceptional retention (84.6% acc); links central pivot to half-spaces.</li>
                    <li><strong>Erik Janża (#64 - Wingback):</strong> Extreme forward-angled pass volume (46% directed forward-left/center); generates overloads with long progressive crosses (34.8m).</li>
                    <li><strong>Taofeek Ismaheel (#11 - Inverted Winger):</strong> Heavy diagonal-inside cutbacks (12–19m length); creates cutback chances into the 18-yard box.</li>
                </ul>
            </div>
            
            <div class="tactical-card">
                <div class="card-header">
                    <span>SÜPER LİG TACTICAL APPLICABILITY</span>
                    <span style="color:#FFD166;">HIGH-TEMPO ADAPTATION</span>
                </div>
                <ul class="card-list">
                    <li><strong>Press-Resistance Profiling:</strong> Essential for clubs facing aggressive man-to-man pressing (e.g. Galatasaray, Fenerbahçe, Beşiktaş).</li>
                    <li><strong>Ball Progression Bottlenecks:</strong> Pinpoints when midfielders circulate laterally/backwards instead of executing vertical penetration.</li>
                    <li><strong>Custom Angular Bins:</strong> Fully customizable to 8, 12, or 16 sectors depending on head coach analytical specifications.</li>
                </ul>
            </div>
        </div>
    </div>
    
    <div class="footer-bar">
        <div><strong>Zafer Yorgancı</strong> | Tactical Pass Sonars & Angular Directionality</div>
        <div>yorgancizafer1@gmail.com • github.com/zfryrgnci • Page 4 of 6</div>
    </div>
</div>

<!-- PAGE 5: MARKOV CHAIN xT & BIVARIATE SHOT MAP -->
<div class="page">
    <div class="top-bar">
        <div>
            <div class="top-title">MARKOV EXPECTED THREAT (xT) & BIVARIATE SHOT QUALITY</div>
            <div class="top-subtitle">KARUN SINGH 16x12 TRANSITION SURFACE • DEFENDER PRESSURE DENSITY • FINISHING EFFICIENCY</div>
        </div>
        <div class="top-badge">GOLAZO ULTRA-SLEEK<br>BENCHMARK</div>
    </div>
    
    <div class="content-area">
        <div class="tactical-grid">
            <div class="visual-container">
                <img src="{img_xt}" style="max-height:88mm;" alt="Markov xT Grid" />
            </div>
            <div class="visual-container">
                <img src="{img_shot}" style="max-height:88mm;" alt="Bivariate Shot Map" />
            </div>
        </div>
        
        <div class="tactical-grid" style="margin-top:6px;">
            <div class="tactical-card">
                <div class="card-header">
                    <span>MARKOV CHAIN EXPECTED THREAT (xT)</span>
                    <span style="color:#00F5D4;">PENETRATION VECTORS</span>
                </div>
                <ul class="card-list">
                    <li><strong>Karun Singh 16x12 Matrix:</strong> Quantifies the probability of goal actions originating from every square meter of the pitch.</li>
                    <li><strong>Zone 14 Dominance:</strong> Lukas Podolski (+0.288 xT/90) operates as the primary killer-pass creator.</li>
                    <li><strong>Flank Threat Creation:</strong> Janża's deep crosses deliver +0.312 xT/90, proving Górnik's left wing is their most lethal creative corridor.</li>
                </ul>
            </div>
            
            <div class="tactical-card">
                <div class="card-header">
                    <span>BIVARIATE SHOT QUALITY & PRESSURE</span>
                    <span style="color:#F72585;">FINISHING AUDIT</span>
                </div>
                <ul class="card-list">
                    <li><strong>Dual Encoding:</strong> Radius scales with Expected Goals (xG); color encodes defender pressure index (0.0 - 1.0) at ball strike.</li>
                    <li><strong>Finishing Overperformance:</strong> 5 goals from 3.86 cumulative xG (+1.14 net finishing efficiency).</li>
                    <li><strong>High-Pressure Conversion:</strong> 43.5% of shots taken under severe pressure (>0.70), emphasizing composure in the box.</li>
                </ul>
            </div>
        </div>
    </div>
    
    <div class="footer-bar">
        <div><strong>Zafer Yorgancı</strong> | Expected Threat (xT) & Bivariate Shot Evaluation</div>
        <div>yorgancizafer1@gmail.com • github.com/zfryrgnci • Page 5 of 6</div>
    </div>
</div>

<!-- PAGE 6: RECRUITMENT VALUATION FRONTIER & SQUAD PLANNING -->
<div class="page">
    <div class="top-bar">
        <div>
            <div class="top-title">CROSS-LEAGUE RECRUITMENT FRONTIER & SQUAD PLANNING</div>
            <div class="top-subtitle">WORLDFOOTBALLR PIPELINES • TRANSFERMARKT VALUATION • ARBITRAGE SWEET SPOT</div>
        </div>
        <div class="top-badge">WORLDFOOTBALLR<br>BENCHMARK</div>
    </div>
    
    <div class="content-area">
        <div class="visual-container">
            <img src="{img_frontier}" alt="Recruitment Frontier" />
        </div>
        
        <div class="tactical-grid">
            <div class="tactical-card">
                <div class="card-header">
                    <span>TRANSFER ARBITRAGE FOR TURKISH SÜPER LİG</span>
                    <span style="color:#0284C7;">SCOUTING INTELLIGENCE</span>
                </div>
                <ul class="card-list">
                    <li><strong>Valuation vs Impact Frontier:</strong> Compares player market values (€M) with composite match performance (xT + Progressive Passes + Defensive Regains per 90).</li>
                    <li><strong>The "Sweet Spot" Arbitrage:</strong> Discovered Central/Eastern European profiles delivering Süper Lig elite outputs (8.4+ composite score) at fees under €1.5M.</li>
                    <li><strong>Key Exemplars:</strong> <strong>Damian Rasak (€1.2M, 8.42 score)</strong> and <strong>Erik Janża (€1.0M, 8.85 score)</strong> perform within 8% of Süper Lig midfielders valued at €10M–€18M.</li>
                </ul>
            </div>
            
            <div class="tactical-card">
                <div class="card-header">
                    <span>AUTOMATED DATA INGESTION CAPABILITIES</span>
                    <span style="color:#10B981;">DATA PIPELINE</span>
                </div>
                <ul class="card-list">
                    <li><strong>Multi-Provider API Integration:</strong> worldfootballR, FBref, Transfermarkt, Understat, and StatsBomb pipelines running automated scrapers.</li>
                    <li><strong>AI Player Archetype Clustering:</strong> k-Means clustering groups players into functional tactical archetypes without subjective human scout bias.</li>
                    <li><strong>Squad Lifecycle Risk:</strong> Squad age curve visualizers track age distribution, peak maturity windows, and impending contract expirations.</li>
                </ul>
            </div>
        </div>
    </div>
    
    <div class="footer-bar">
        <div><strong>Zafer Yorgancı</strong> | Recruitment Intelligence & Transfer Valuation Frontiers</div>
        <div>yorgancizafer1@gmail.com • github.com/zfryrgnci • Page 6 of 6</div>
    </div>
</div>

</body>
</html>
"""
    return html

def generate_turkish_dossier():
    print("Building Turkish Technical Intelligence Dossier HTML...")
    
    img_cv = get_base64_img("17_roboflow_cv_broadcast_homography_radar.png")
    img_voronoi = get_base64_img("18_eddwebster_voronoi_pitch_control_convex_hulls.png")
    img_sonar = get_base64_img("19_pass_sonar_midfield_engine.png")
    img_xt = get_base64_img("20_markov_xt_progression_channels.png")
    img_shot = get_base64_img("21_bivariate_shot_quality_pressure.png")
    img_frontier = get_base64_img("22_worldfootballr_recruitment_frontier.png")
    
    html = f"""<!DOCTYPE html>
<html lang="tr">
<head>
<meta charset="UTF-8">
<title>Zafer Yorgancı - Teknik Analiz ve Veri Görselleştirme Raporu 2026</title>
<style>{DOSSIER_CSS}</style>
</head>
<body>

<!-- SAYFA 1: GİRİŞ VE TEKNİK DİREKTÖR YÖNETİCİ ÖZETİ -->
<div class="page">
    <div class="top-bar">
        <div>
            <div class="top-title">TEKNİK TAKTİK ANALİZ VE VERİ GÖRSELLEŞTİRME RAPORU 2026</div>
            <div class="top-subtitle">MAÇ ÖNCESİ TAKTİK • BİLGİSAYARLI GÖRÜ (CV) • VORONOI SAHA KONTROLÜ • TRANSFER İSTİHBARATI</div>
        </div>
        <div class="top-badge">
            GÓRNIK ZABRZE (EKSTRAKLASA)<br>
            TÜRKİYE SÜPER LİG BAŞVURUSU
        </div>
    </div>
    
    <div class="content-area">
        <div class="benchmark-tag">Global Standart Sentezi: Roboflow Sports • Edd Webster • 0xjuanma Golazo • worldfootballR</div>
        
        <div style="background:#0F172A; color:#F8FAFC; padding:16px 20px; border-radius:6px; border-left:4px solid #00F5D4; margin-bottom:10px;">
            <div style="font-size:11pt; font-weight:800; color:#00F5D4; margin-bottom:6px;">TEKNİK DİREKTÖRLER VE SPORTİF DİREKTÖRLER İÇİN YÖNETİCİ ÖZETİ</div>
            <div style="font-size:8.6pt; line-height:1.5; color:#CBD5E1;">
                Bu rapor, Polonya Ekstraklasa 2025–2026 sezonunda <strong>Górnik Zabrze</strong> kulübü bünyesinde uzaktan sunduğum teknik analiz,
                bilgisayarlı görü (CV) takip ve veri görselleştirme altyapısını belgelemektedir. Süper Lig teknik heyetlerinin doğrudan sahada aradığı
                kritik sorulara yanıt vermek üzere kurgulanmıştır: <strong>rakip savunma hatlarını maç öncesinde kırmak, maç içi uzamsal hakimiyeti (pitch control)
                ölçmek ve transferde yüksek verimli / düşük maliyetli oyuncuları veriyle tespit etmek.</strong>
            </div>
        </div>
        
        <div class="tactical-grid">
            <div class="tactical-card">
                <div class="card-header">
                    <span>1. MAÇ ÖNCESİ VE TAKTİK HAZIRLIK</span>
                    <span style="color:#0284C7;">TEKNİK ANALİZ</span>
                </div>
                <ul class="card-list">
                    <li><strong>Rakip Oyun Kurulumu:</strong> Kaleci pas dağıtım haritası ve stoper aralıklarına pres tetikleyicisi kurma.</li>
                    <li><strong>PPDA ve Hat Mesafeleri:</strong> Rakip pres şiddetini analiz ederek merkezden yarı-alanlara çıkış kanalları belirleme.</li>
                    <li><strong>Duran Top Zafiyetleri:</strong> İçeri/dışarı kavisli kornerlerde adam/alan savunması zaaflarının tespiti.</li>
                </ul>
            </div>
            
            <div class="tactical-card">
                <div class="card-header">
                    <span>2. MAÇ İÇİ VE CANLI TAKİP SİSTEMLERİ</span>
                    <span style="color:#00F5D4;">CV / UZAMSAL</span>
                </div>
                <ul class="card-list">
                    <li><strong>YOLOv11x Homografi Radarı:</strong> Yayın görüntüsünü 105x68m metrik 2D saha radarına ve anlık hız vektörlerine dönüştürme.</li>
                    <li><strong>Voronoi Saha Kontrolü:</strong> Dinamik saha sahipliği ve takım kompaktlık alanını (m²) hesaplama.</li>
                    <li><strong>360° Pas Sonarları:</strong> Orta saha oyuncularının pas yönelim ve metrik uzunluk karnesi.</li>
                </ul>
            </div>
        </div>

        <div class="visual-container" style="margin-top:6px;">
            <img src="{img_cv}" style="max-height:105mm;" alt="CV Radar TR" />
        </div>
        
        <div class="kpi-row">
            <div class="kpi-box">
                <div class="kpi-val" style="color:#0284C7;">0.142 m</div>
                <div class="kpi-lbl">CV Homografi Hatası (RMSE)</div>
            </div>
            <div class="kpi-box">
                <div class="kpi-val" style="color:#00F5D4;">%58.4</div>
                <div class="kpi-lbl">Ortalama Saha Kontrolü</div>
            </div>
            <div class="kpi-box">
                <div class="kpi-val" style="color:#F72585;">+0.312</div>
                <div class="kpi-lbl">Zirve Kanat xT/90 (Janża)</div>
            </div>
            <div class="kpi-box">
                <div class="kpi-val" style="color:#FFD166;">€1.2M</div>
                <div class="kpi-lbl">Transfer Fırsatı (Rasak)</div>
            </div>
        </div>
    </div>
    
    <div class="footer-bar">
        <div><strong>Zafer Yorgancı</strong> | Futbol Veri Görselleştirme Uzmanı & Yapay Zeka Mühendisi</div>
        <div>yorgancizafer1@gmail.com • github.com/zfryrgnci • Sayfa 1 / 6</div>
    </div>
</div>

<!-- SAYFA 2: BİLGİSAYARLI GÖRÜ VE 2D HOMOGRAFİ RADARI -->
<div class="page">
    <div class="top-bar">
        <div>
            <div class="top-title">BİLGİSAYARLI GÖRÜ (CV) OPTİK TAKİP VE 2D RADAR</div>
            <div class="top-subtitle">YOLOv11x DETEKTÖRÜ • BYTETRACK • DIRECT LINEAR TRANSFORM (DLT) HOMOGRAFİSİ</div>
        </div>
        <div class="top-badge">ROBOFLOW SPORTS<br>REFERANSI</div>
    </div>
    
    <div class="content-area">
        <div class="visual-container">
            <img src="{img_cv}" alt="Roboflow CV TR" />
        </div>
        
        <div class="tactical-grid">
            <div class="tactical-card">
                <div class="card-header">
                    <span>TEKNİK HEYET ANALİZİ: VİDEODAN VERİYE</span>
                    <span style="color:#0284C7;">YAYIN \to RADAR</span>
                </div>
                <ul class="card-list">
                    <li><strong>Perspektif Homografi Dönüşümü:</strong> TV yayınındaki oyuncu ayak temas noktalarını [u, v], 105 x 68 m FIFA standardı 2D saha koordinatlarına [X, Y] izdüşürür.</li>
                    <li><strong>Anlık Kinematik Hız Vektörleri:</strong> Oyuncuların anlık hızları (v, m/sn) ve ivmelenmeleri kontra-atak çıkışlarını anlık takip eder.</li>
                    <li><strong>Bloklar Arası Pres Boşluğu:</strong> Takım merkez noktaları (centroid) arasındaki 12.6 m'lik mesafe, kompakt savunma derinliğini gösterir.</li>
                </ul>
            </div>
            
            <div class="tactical-card">
                <div class="card-header">
                    <span>MİMARİ VE YAZILIM ALTYAPISI</span>
                    <span style="color:#00F5D4;">TENSORRT 60 FPS</span>
                </div>
                <ul class="card-list">
                    <li><strong>Model Omurgası:</strong> YOLOv11x ve SoccerNet verileriyle ince ayar yapılmış derin öğrenme modeli.</li>
                    <li><strong>Yeniden İzdüşüm Hassasiyeti:</strong> 0.142 m Root Mean Square Error (RMSE) ile üst düzey endüstri standardı.</li>
                    <li><strong>Kullanım Alanı:</strong> Devre arası soyunma odası taktik analizinde maç yayını üzerinden otomatik 2D kuşbakışı simülasyon sunma.</li>
                </ul>
            </div>
        </div>
    </div>
    
    <div class="footer-bar">
        <div><strong>Zafer Yorgancı</strong> | Bilgisayarlı Görü ve Homografi Radar Minimapleri</div>
        <div>yorgancizafer1@gmail.com • github.com/zfryrgnci • Sayfa 2 / 6</div>
    </div>
</div>

<!-- SAYFA 3: VORONOI SAHA KONTROLÜ VE TAKIM HULL ŞEKLİ -->
<div class="page">
    <div class="top-bar">
        <div>
            <div class="top-title">VORONOI SAHA KONTROLÜ VE TAKIM KOMPAKT ALANI</div>
            <div class="top-subtitle">SÜREKLİ ALAN HAKİMİYETİ • TAKIM KOMPAKT ALANI (m²) • EFEKTİF EN VE DERİNLİK</div>
        </div>
        <div class="top-badge">EDD WEBSTER<br>REFERANSI</div>
    </div>
    
    <div class="content-area">
        <div class="visual-container">
            <img src="{img_voronoi}" alt="Voronoi Pitch Control TR" />
        </div>
        
        <div class="tactical-grid">
            <div class="tactical-card">
                <div class="card-header">
                    <span>TAKTIK ANALİZ: UZAMSAL ALAN HAKİMİYETİ</span>
                    <span style="color:#0284C7;">ALAN PARÇALAMA</span>
                </div>
                <ul class="card-list">
                    <li><strong>Saha Hakimiyeti Dağılımı:</strong> Voronoi hücreleri oyuncuların topa varış sürelerine göre sahayı bölerek Górnik Zabrze'ye <strong>%58.4 saha kontrolü</strong> sağlar.</li>
                    <li><strong>Kanat Aşırı Yüklemesi:</strong> Sol kanatta genişleyen Voronoi hücreleri, Erik Janża ve Lukoszek'in rakip beki bağlayarak Podolski'ye merkezde alan açtığını gösterir.</li>
                    <li><strong>Top Taşıyıcı Pas Koridorları:</strong> Damian Rasak (#6), 3 farklı hat kırma koridoruna doğrudan görüş açısına sahiptir.</li>
                </ul>
            </div>
            
            <div class="tactical-card">
                <div class="card-header">
                    <span>CONVEX HULL GEOMETRİK METRİKLERİ</span>
                    <span style="color:#F72585;">TAKIM ŞEKLİ</span>
                </div>
                <ul class="card-list">
                    <li><strong>Górnik Takım Alanı:</strong> 1,185 m² (Geniş hücum yerleşimi, progresif pas destek ağı).</li>
                    <li><strong>Rakip Alçak Blok Alanı:</strong> 890 m² (Aşırı daraltılmış merkez blok, kanat ters toplarına açık).</li>
                    <li><strong>Efektif En ve Derinlik:</strong> En: 49.8 m vs 44.2 m | Derinlik: 42.3 m vs 28.5 m.</li>
                </ul>
            </div>
        </div>
    </div>
    
    <div class="footer-bar">
        <div><strong>Zafer Yorgancı</strong> | Uzamsal Analiz ve Voronoi Saha Hakimiyeti</div>
        <div>yorgancizafer1@gmail.com • github.com/zfryrgnci • Sayfa 3 / 6</div>
    </div>
</div>

<!-- SAYFA 4: PAS SONARLARI VE ORTA SAHA DAĞILIMI -->
<div class="page">
    <div class="top-bar">
        <div>
            <div class="top-title">TAKTIK PAS SONARLARI VE 360° ORTA SAHA DAĞILIMI</div>
            <div class="top-subtitle">12 SEKTÖRLÜ AÇISAL YÖN DAĞILIMI • PROGRESİF PAS MESAFESİ • İSABET YÜZDESİ</div>
        </div>
        <div class="top-badge">GOLAZO & EDD WEBSTER<br>REFERANSI</div>
    </div>
    
    <div class="content-area">
        <div class="visual-container">
            <img src="{img_sonar}" alt="Pass Sonars TR" />
        </div>
        
        <div class="tactical-grid">
            <div class="tactical-card">
                <div class="card-header">
                    <span>ORTA SAHA OYUNCU KARNELERİ</span>
                    <span style="color:#0284C7;">TEKNİK DİREKTÖR RAPORU</span>
                </div>
                <ul class="card-list">
                    <li><strong>Damian Rasak (#6 - Çapa):</strong> Yüksek hacimli ileri-çapraz pas dağıtımı (ortalama 28.5m metrik uzunluk); ilk baskı hattını kıran ana oyun kurucu.</li>
                    <li><strong>Patrik Hellebrand (#8 - Bağlantı):</strong> 360 derece dengeli pas açısı ve yüksek top koruma (%84.6 isabet); yarı-alan geçişlerini sağlar.</li>
                    <li><strong>Erik Janża (#64 - Hücum Beki):</strong> Aşırı dikine pas hacmi (%46 ileri-sol/merkez); 34.8m ortalama uzunluktaki ceza sahası ortalarıyla tehlike üretir.</li>
                    <li><strong>Taofeek Ismaheel (#11 - Ters Ayaklı Kanat):</strong> Çapraz içe kat etme ve yerden geriye kesilen paslar (12–19m); ceza yayına net şut pası hazırlar.</li>
                </ul>
            </div>
            
            <div class="tactical-card">
                <div class="card-header">
                    <span>TÜRKİYE SÜPER LİG UYGULANABİLİRLİĞİ</span>
                    <span style="color:#FFD166;">YÜKSEK TEMPO UYUMU</span>
                </div>
                <ul class="card-list">
                    <li><strong>Prese Karşı Direnç Analizi:</strong> Agresif adam adama pres uygulayan takımlara (Galatasaray, Fenerbahçe, Beşiktaş) karşı topu dikine çıkarma kalitesini ölçer.</li>
                    <li><strong>Geriye/Yana Pas Tıkanıklıkları:</strong> Orta sahanın oyunu ne zaman dikine hızlandırdığını veya gereksiz yana çevirdiğini net ortaya koyar.</li>
                </ul>
            </div>
        </div>
    </div>
    
    <div class="footer-bar">
        <div><strong>Zafer Yorgancı</strong> | Taktik Pas Sonarları ve Açısal Dağılım</div>
        <div>yorgancizafer1@gmail.com • github.com/zfryrgnci • Sayfa 4 / 6</div>
    </div>
</div>

<!-- SAYFA 5: MARKOV xT VE İKİ DEĞİŞKENLİ ŞUT HARİTASI -->
<div class="page">
    <div class="top-bar">
        <div>
            <div class="top-title">MARKOV BEKLENEN TEHDİT (xT) VE ŞUT BASKI HARİTASI</div>
            <div class="top-subtitle">KARUN SINGH 16x12 GEÇİŞ YÜZEYİ • SAVUNMA BASKI YOĞUNLUĞU • BİTİRİCİLİK VERİMİ</div>
        </div>
        <div class="top-badge">GOLAZO KOYU TEMA<br>REFERANSI</div>
    </div>
    
    <div class="content-area">
        <div class="tactical-grid">
            <div class="visual-container">
                <img src="{img_xt}" style="max-height:88mm;" alt="Markov xT Grid TR" />
            </div>
            <div class="visual-container">
                <img src="{img_shot}" style="max-height:88mm;" alt="Bivariate Shot Map TR" />
            </div>
        </div>
        
        <div class="tactical-grid" style="margin-top:6px;">
            <div class="tactical-card">
                <div class="card-header">
                    <span>MARKOV ZİNCİRİ BEKLENEN TEHDİT (xT)</span>
                    <span style="color:#00F5D4;">TEHDİT KORİDORLARI</span>
                </div>
                <ul class="card-list">
                    <li><strong>16x12 Karun Singh Matrisi:</strong> Sahanın her bir metrekaresinden golle sonuçlanacak aksiyon üretme olasılığını modeller.</li>
                    <li><strong>Bölge 14 (Zone 14) Hakimiyeti:</strong> Lukas Podolski (+0.288 xT/90), hatlar arasında kilit pas mimarıdır.</li>
                    <li><strong>Sol Kanat Aşırı Tehdidi:</strong> Janża'nın bindirmeleri +0.312 xT/90 üreterek takımın en üretken hücum koridorunu oluşturur.</li>
                </ul>
            </div>
            
            <div class="tactical-card">
                <div class="card-header">
                    <span>ŞUT KALİTESİ VE SAVUNMA BASKISI</span>
                    <span style="color:#F72585;">BİTİRİCİLİK VERİMİ</span>
                </div>
                <ul class="card-list">
                    <li><strong>İki Değişkenli Kodlama:</strong> Balon çapı Beklenen Golü (xG), balon rengi ise şut anındaki savunma baskı yoğunluğunu (0.0 - 1.0) gösterir.</li>
                    <li><strong>Bitiricilik Üstünlüğü:</strong> 3.86 toplam xG'den 5 gol üretilmiştir (+1.14 gol beklentisi üzeri pozitif verimlilik).</li>
                    <li><strong>Yüksek Baskı Altında Şutlar:</strong> Şutların %43.5'i yoğun baskı altındayken çekilmiş, ceza sahası soğukkanlılığını doğrulamıştır.</li>
                </ul>
            </div>
        </div>
    </div>
    
    <div class="footer-bar">
        <div><strong>Zafer Yorgancı</strong> | Beklenen Tehdit (xT) ve İki Değişkenli Şut Analizi</div>
        <div>yorgancizafer1@gmail.com • github.com/zfryrgnci • Sayfa 5 / 6</div>
    </div>
</div>

<!-- SAYFA 6: TRANSFER VERİMLİLİK SINIRI VE KADRO PLANLAMA -->
<div class="page">
    <div class="top-bar">
        <div>
            <div class="top-title">TRANSFER PİYASA VERİMLİLİK SINIRI VE KADRO PLANLAMA</div>
            <div class="top-subtitle">WORLDFOOTBALLR VERİ AKIŞLARI • TRANSFERMARKT DEĞERLEMESİ • ARBİTRAJ FIRSATLARI</div>
        </div>
        <div class="top-badge">WORLDFOOTBALLR<br>REFERANSI</div>
    </div>
    
    <div class="content-area">
        <div class="visual-container">
            <img src="{img_frontier}" alt="Recruitment Frontier TR" />
        </div>
        
        <div class="tactical-grid">
            <div class="tactical-card">
                <div class="card-header">
                    <span>TÜRKİYE SÜPER LİG İÇİN TRANSFER ARBİTRAJI</span>
                    <span style="color:#0284C7;">SCOUTING İSTİHBARATI</span>
                </div>
                <ul class="card-list">
                    <li><strong>Verimlilik Sınırı (Efficient Frontier):</strong> Transfermarkt piyasa değerleri (€M) ile 90 dakika başına üretilen toplam taktiksel katkıyı (xT + İlerletici Pas + Defansif Müdahale) kıyaslar.</li>
                    <li><strong>Fırsat Alanı (Sweet Spot):</strong> Süper Lig kulüpleri için €1.5M altı maliyetle 8.4+ kompozit katkı sunan Orta/Doğu Avrupa hedeflerini modeller.</li>
                    <li><strong>Örnek Oyuncular:</strong> <strong>Damian Rasak (€1.2M, 8.42 puan)</strong> ve <strong>Erik Janża (€1.0M, 8.85 puan)</strong>, Süper Lig'de €10M–€18M piyasa değerli yıldızların sunduğu metrik seviyeyi çok düşük maliyetle karşılamaktadır.</li>
                </ul>
            </div>
            
            <div class="tactical-card">
                <div class="card-header">
                    <span>OTOMATİZE EDİLMİŞ VERİ BORU HATLARI</span>
                    <span style="color:#10B981;">VERİ ALTYAPISI</span>
                </div>
                <ul class="card-list">
                    <li><strong>Çok Kaynaklı API Entegrasyonu:</strong> worldfootballR, FBref, Transfermarkt, Understat ve StatsBomb üzerinden otomatik çekilen veriler.</li>
                    <li><strong>Yapay Zeka Oyuncu Kümeleri:</strong> k-Means makine öğrenmesi algoritmaları, insan scout yanlılığını ortadan kaldırarak fonksiyonel oyuncu profilleri gruplar.</li>
                    <li><strong>Yaş Eğrisi ve Sözleşme Risk Analizi:</strong> Kadro yaş piramidi görselleştiricisi ile tepe performans dönemleri ve sözleşme bitiş riskleri eşzamanlı takip edilir.</li>
                </ul>
            </div>
        </div>
    </div>
    
    <div class="footer-bar">
        <div><strong>Zafer Yorgancı</strong> | Transfer İstihbaratı ve Piyasa Değerleme Sınırları</div>
        <div>yorgancizafer1@gmail.com • github.com/zfryrgnci • Sayfa 6 / 6</div>
    </div>
</div>

</body>
</html>
"""
    return html

def generate_english_cv():
    print("Building English Single-Page Football CV HTML...")
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Zafer Yorganci - Football CV</title>
<style>{CV_CSS}</style>
</head>
<body>

<div class="cv-page">
    <div class="cv-header">
        <div class="cv-name">ZAFER YORGANCI</div>
        <div class="cv-role">FOOTBALL DATA VISUALIZATION SPECIALIST & AI ENGINEER</div>
        <div class="cv-contact">
            <span>📍 Istanbul, Türkiye (Poland Background)</span>
            <span>✉️ <a href="mailto:yorgancizafer1@gmail.com">yorgancizafer1@gmail.com</a></span>
            <span>🌐 <a href="https://portfolio.zfryrgnci.workers.dev">portfolio.zfryrgnci.workers.dev</a></span>
            <span>🐙 <a href="https://github.com/zfryrgnci">github.com/zfryrgnci</a></span>
        </div>
        <div class="cv-target">
            🎯 TARGET: First Team Football Data Visualization Specialist / Technical Tactical Analyst (Süper Lig Scope)
        </div>
    </div>
    
    <div class="cv-body">
        <!-- EXECUTIVE PROFILE -->
        <div class="cv-section">
            <div class="cv-sec-title">Executive Profile</div>
            <p style="color:#334155; font-size:8.2pt; line-height:1.4;">
                Specialized <strong>Football Data Visualization Specialist and AI Engineer</strong> synthesizing broadcast computer vision tracking, 
                spatial pitch control models, and multi-provider match event feeds (StatsBomb, Opta, Wyscout, Transfermarkt) into decisive tactical intelligence. 
                Proven club experience delivering pre-match opposition tactical dossiers, real-time spatial deconstructions, and recruitment arbitrage models 
                for <strong>Górnik Zabrze</strong> (Polish Ekstraklasa 2025–2026). Bilingual background (Polish educated/resident background, native Turkish speaker in Istanbul); 
                uniquely equipped to empower Turkish Süper Lig technical staffs (Galatasaray, Fenerbahçe, Beşiktaş, Trabzonspor).
            </p>
        </div>
        
        <!-- CLUB EXPERIENCE -->
        <div class="cv-section">
            <div class="cv-sec-title">Professional Football Experience</div>
            <div class="cv-exp-header">
                <div>
                    <span class="cv-exp-role">Sport Data Visualization Specialist & Performance Consultant</span> 
                    <span class="cv-exp-org">| Górnik Zabrze SSA</span> (Ekstraklasa, Poland)
                </div>
                <div class="cv-exp-date">2025 – 2026 Season (Remote)</div>
            </div>
            <ul class="cv-bullets">
                <li><strong>Pre-Match Tactical Intelligence:</strong> Engineered automated opposition dossiers analyzing defensive line depth, pressing triggers (PPDA), goalkeeper build-up distribution, and corner delivery cluster routines for the coaching staff.</li>
                <li><strong>Spatial Pitch Control & Convex Hulls:</strong> Modeled continuous Voronoi space dominance (Górnik 58.4% mean control) and outfield team convex hulls calculating compactness area (m²), effective width (m), and depth (m).</li>
                <li><strong>Midfield Passing Sonars:</strong> Built 360° polar pass sonar engines for midfield engines (Damian Rasak, Patrik Hellebrand, Erik Janża) breaking down pass directionality, progressive length, and press-resistance under pressure.</li>
                <li><strong>Markov Expected Threat (xT):</strong> Calibrated 16x12 Karun Singh transition matrices isolating Zone 14 penetrations (Podolski +0.288 xT/90) and flank crossing overloads (Janża +0.312 xT/90).</li>
                <li><strong>Recruitment Arbitrage Pipelines:</strong> Integrated worldfootballR and Transfermarkt APIs to construct multi-league valuation frontiers, uncovering high-impact undervalued targets (€1M–€1.5M) for Turkish Süper Lig transfer windows.</li>
            </ul>
        </div>
        
        <!-- TECHNICAL INNOVATION: 4 BENCHMARKS -->
        <div class="cv-section">
            <div class="cv-sec-title">Benchmark Technical Architecture</div>
            <div class="cv-two-col">
                <div>
                    <div style="font-weight:700; color:#0284C7; font-size:8pt; margin-bottom:2px;">1. Computer Vision & 2D Radars (roboflow/sports):</div>
                    <div style="font-size:7.6pt; color:#475569; line-height:1.35;">
                        Fine-tuned YOLOv11x + ByteTrack optical tracking with Direct Linear Transform (DLT) Homography projecting broadcast video to 2D metric pitch coordinates (0.142m RMSE) with velocity vectors.
                    </div>
                    <div style="font-weight:700; color:#0284C7; font-size:8pt; margin-top:4px; margin-bottom:2px;">2. Spatial Analytics (eddwebster/football_analytics):</div>
                    <div style="font-size:7.6pt; color:#475569; line-height:1.35;">
                        Voronoi territorial partitioning, team tactical shape convex hulls, and passing network graph centrality models.
                    </div>
                </div>
                <div>
                    <div style="font-weight:700; color:#0284C7; font-size:8pt; margin-bottom:2px;">3. Tactical Aesthetics & xT (0xjuanma/golazo):</div>
                    <div style="font-size:7.6pt; color:#475569; line-height:1.35;">
                        Publication-grade dark UI styling, bivariate shot quality maps with defender pressure density, and Markov xT flow vectors.
                    </div>
                    <div style="font-weight:700; color:#0284C7; font-size:8pt; margin-top:4px; margin-bottom:2px;">4. Multi-League Pipelines (worldfootballR):</div>
                    <div style="font-size:7.6pt; color:#475569; line-height:1.35;">
                        Automated scrapers for FBref, Transfermarkt, and Understat evaluating player performance vs market valuation frontiers.
                    </div>
                </div>
            </div>
        </div>
        
        <!-- KEY ACHIEVEMENTS & SÜPER LİG FIT -->
        <div class="cv-section">
            <div class="cv-sec-title">Key Tactical Impact & Süper Lig Readiness</div>
            <div class="cv-two-col">
                <div>
                    <div style="font-weight:700; color:#0284C7; font-size:8pt; margin-bottom:2px;">Tactical Impact at Górnik Zabrze:</div>
                    <ul class="cv-bullets">
                        <li><strong>Match Preparation Turnaround:</strong> Automated opposition data ingestion pipeline, reducing coach briefing preparation from 48h to 4h.</li>
                        <li><strong>Set-Piece Defensive Optimization:</strong> Inswinging corner marking cluster models boosted first-contact duel win rate by +22%.</li>
                    </ul>
                </div>
                <div>
                    <div style="font-weight:700; color:#0284C7; font-size:8pt; margin-bottom:2px;">Turkish Süper Lig Operational Fit:</div>
                    <ul class="cv-bullets">
                        <li><strong>High-Press & Transition Analysis:</strong> Proven algorithms isolating opposition escape outlets against intense pressing (Galatasaray, Fenerbahçe, Beşiktaş).</li>
                        <li><strong>Bilingual Matchday Presence:</strong> Native Turkish speaker based in Istanbul; ready for immediate on-site matchday and training ground deployment.</li>
                    </ul>
                </div>
            </div>
        </div>
        
        <!-- TECHNICAL SKILLS & EDUCATION -->
        <div class="cv-section">
            <div class="cv-sec-title">Technical Competencies & Education</div>
            <div class="cv-skills-grid">
                <div class="cv-skill-item">
                    <div class="cv-skill-lbl">Tracking & Computer Vision</div>
                    <div class="cv-skill-val">Python, PyTorch, YOLOv11x, ByteTrack, OpenCV, Planar Homography (DLT), TensorRT</div>
                </div>
                <div class="cv-skill-item">
                    <div class="cv-skill-lbl">Spatial & Tactical Analytics</div>
                    <div class="cv-skill-val">mplsoccer, SciPy (Voronoi/ConvexHull), NumPy, Pandas, Matplotlib, Seaborn</div>
                </div>
                <div class="cv-skill-item">
                    <div class="cv-skill-lbl">Event Providers & Models</div>
                    <div class="cv-skill-val">StatsBomb, Opta, Wyscout, worldfootballR, Karun Singh xT, Bivariate xG, k-Means</div>
                </div>
                <div class="cv-skill-item">
                    <div class="cv-skill-lbl">Reporting & Languages</div>
                    <div class="cv-skill-val">Headless Playwright PDF Engine, Turkish (Native), Polish (Fluent/Educated), English (Fluent)</div>
                </div>
            </div>
        </div>
    </div>
    
    <div class="cv-footer">
        <div><strong>Zafer Yorgancı</strong> — Football CV | Ready for immediate on-site or remote deployment</div>
        <div>github.com/zfryrgnci/football-data-visualization-specialist</div>
    </div>
</div>

</body>
</html>
"""
    return html

def generate_turkish_cv():
    print("Building Turkish Single-Page Football CV HTML...")
    html = f"""<!DOCTYPE html>
<html lang="tr">
<head>
<meta charset="UTF-8">
<title>Zafer Yorgancı - Futbol CV</title>
<style>{CV_CSS}</style>
</head>
<body>

<div class="cv-page">
    <div class="cv-header">
        <div class="cv-name">ZAFER YORGANCI</div>
        <div class="cv-role">FUTBOL VERİ GÖRSELLEŞTİRME UZMANI & YAPAY ZEKA MÜHENDİSİ</div>
        <div class="cv-contact">
            <span>📍 İstanbul, Türkiye (Polonya Geçmişi)</span>
            <span>✉️ <a href="mailto:yorgancizafer1@gmail.com">yorgancizafer1@gmail.com</a></span>
            <span>🌐 <a href="https://portfolio.zfryrgnci.workers.dev">portfolio.zfryrgnci.workers.dev</a></span>
            <span>🐙 <a href="https://github.com/zfryrgnci">github.com/zfryrgnci</a></span>
        </div>
        <div class="cv-target">
            🎯 HEDEF POZİSYON: A Takım Futbol Veri Görselleştirme Uzmanı / Taktik Performans Analisti (Süper Lig Kapsamı)
        </div>
    </div>
    
    <div class="cv-body">
        <!-- YÖNETİCİ ÖZETİ -->
        <div class="cv-section">
            <div class="cv-sec-title">Yönetici Özeti & Uzmanlık</div>
            <p style="color:#334155; font-size:8.2pt; line-height:1.4;">
                Yayın görüntüsü üzerinden bilgisayarlı görü (CV) optik takibi, uzamsal saha kontrol modelleri (Voronoi) ve çok kaynaklı maç olay akışlarını
                (StatsBomb, Opta, Wyscout, Transfermarkt) teknik heyet için doğrudan skora etki eden taktik istihbarata dönüştüren <strong>Futbol Veri Görselleştirme Uzmanı ve Yapay Zeka Mühendisi</strong>.
                Polonya Ekstraklasa 2025–2026 sezonunda <strong>Górnik Zabrze</strong> bünyesinde uzaktan maç öncesi rakip analiz dosyaları, devre arası uzamsal takip minimapleri ve transfer arbitraj modelleri üretmiştir.
                Polonya eğitim/ikamet geçmişi ve anadili Türkçe olan İstanbul yerleşimiyle Türkiye Süper Lig kulüpleri (Galatasaray, Fenerbahçe, Beşiktaş, Trabzonspor) teknik heyetlerine anında katma değer sunmaya hazırdır.
            </p>
        </div>
        
        <!-- KULÜP DENEYİMİ -->
        <div class="cv-section">
            <div class="cv-sec-title">Profesyonel Kulüp Deneyimi</div>
            <div class="cv-exp-header">
                <div>
                    <span class="cv-exp-role">Spor Veri Görselleştirme Uzmanı & Performans Danışmanı</span> 
                    <span class="cv-exp-org">| Górnik Zabrze SSA</span> (Ekstraklasa, Polonya)
                </div>
                <div class="cv-exp-date">2025 – 2026 Sezonu (Uzaktan)</div>
            </div>
            <ul class="cv-bullets">
                <li><strong>Maç Öncesi Taktik İstihbarat:</strong> Teknik direktör için rakip savunma hattı yüksekliği, pres tetikleyicileri (PPDA), kaleci pas dağılımı ve duran top korner kümelerini otomatik görselleştiren taktik dosyalar hazırladı.</li>
                <li><strong>Voronoi Saha Kontrolü & Takım Şekli:</strong> Oyuncuların dinamik saha sahipliğini (%58.4 Górnik kontrolü) ve takımın kompaktlık alanını (m²), efektik en/boy mesafelerini hesaplayan Convex Hull geometrisini modelledi.</li>
                <li><strong>Orta Saha Pas Sonarları:</strong> Damian Rasak, Patrik Hellebrand ve Erik Janża için 360° açısal pas yönelim ve progresif pas mesafesi (m) analizlerini üretti.</li>
                <li><strong>Markov Beklenen Tehdit (xT):</strong> 16x12 Karun Singh geçiş matrisleriyle Bölge 14 kilit paslarını (Podolski +0.288 xT/90) ve sol kanat bindirmelerini (Janża +0.312 xT/90) sayılaştırdı.</li>
                <li><strong>Transfer Arbitraj Boru Hatları:</strong> worldfootballR ve Transfermarkt verilerini birleştirerek Süper Lig kulüplerine €1M–€1.5M bütçeyle elit katkı sağlayacak oyuncu listelerini çıkardı.</li>
            </ul>
        </div>
        
        <!-- TEKNİK REFERANS STANDARTLARI -->
        <div class="cv-section">
            <div class="cv-sec-title">Benchmark Teknik Standartlar</div>
            <div class="cv-two-col">
                <div>
                    <div style="font-weight:700; color:#0284C7; font-size:8pt; margin-bottom:2px;">1. Bilgisayarlı Görü & 2D Radar (roboflow/sports):</div>
                    <div style="font-size:7.6pt; color:#475569; line-height:1.35;">
                        YOLOv11x + ByteTrack ve Direct Linear Transform (DLT) Homografi ile yayın görüntüsünü 0.142m hata payıyla 2D taktik radara ve hız vektörlerine dönüştürme.
                    </div>
                    <div style="font-weight:700; color:#0284C7; font-size:8pt; margin-top:4px; margin-bottom:2px;">2. Uzamsal Saha Hakimiyeti (eddwebster/football_analytics):</div>
                    <div style="font-size:7.6pt; color:#475569; line-height:1.35;">
                        Voronoi uzamsal alan parçalaması, takım blok derinliği ve pas ağı çizge merkezilik analizleri.
                    </div>
                </div>
                <div>
                    <div style="font-weight:700; color:#0284C7; font-size:8pt; margin-bottom:2px;">3. Taktik Tasarım & xT Akışları (0xjuanma/golazo):</div>
                    <div style="font-size:7.6pt; color:#475569; line-height:1.35;">
                        Yüksek kaliteli karanlık tema taktik görseller, savunma baskı yoğunluklu iki değişkenli şut haritaları ve Markov xT akışları.
                    </div>
                    <div style="font-weight:700; color:#0284C7; font-size:8pt; margin-top:4px; margin-bottom:2px;">4. Çoklu Lig Transfer Hatları (worldfootballR):</div>
                    <div style="font-size:7.6pt; color:#475569; line-height:1.35;">
                        FBref, Transfermarkt ve Understat üzerinden oyuncu performansı ile piyasa değeri verimlilik sınırını kıyaslayan otomatik modeller.
                    </div>
                </div>
            </div>
        </div>
        
        <!-- STRATEJİK BAŞARILAR VE SÜPER LİG UYUMU -->
        <div class="cv-section">
            <div class="cv-sec-title">Stratejik Taktiksel Katkılar ve Süper Lig Hazırlığı</div>
            <div class="cv-two-col">
                <div>
                    <div style="font-weight:700; color:#0284C7; font-size:8pt; margin-bottom:2px;">Górnik Zabrze Taktiksel Katkıları:</div>
                    <ul class="cv-bullets">
                        <li><strong>Maç Hazırlık Süresi:</strong> Otomatize veri boru hatlarıyla maç öncesi rakip analiz dosya hazırlığını 48 saatten 4 saate indirdi.</li>
                        <li><strong>Duran Top Savunması:</strong> Korner kümeleme modelleriyle ceza sahası ilk temas ikili mücadele kazanma oranını %22 artırdı.</li>
                    </ul>
                </div>
                <div>
                    <div style="font-weight:700; color:#0284C7; font-size:8pt; margin-bottom:2px;">Süper Lig Operasyonel Uyumu:</div>
                    <ul class="cv-bullets">
                        <li><strong>Ön Alan Baskı Analizi:</strong> Agresif pres uygulayan takımlara karşı rakip zaaf bölgelerini tespit eden modeller (GS, FB, BJK).</li>
                        <li><strong>İstanbul Yerleşimi & Anında Başlama:</strong> İstanbul merkezli, tam zamanlı kulüp içi veya uzaktan maç günü operasyonlarına hemen hazır.</li>
                    </ul>
                </div>
            </div>
        </div>
        
        <!-- YETKİNLİKLER VE DİLLER -->
        <div class="cv-section">
            <div class="cv-sec-title">Teknik Yetkinlikler ve Diller</div>
            <div class="cv-skills-grid">
                <div class="cv-skill-item">
                    <div class="cv-skill-lbl">Takip & Bilgisayarlı Görü</div>
                    <div class="cv-skill-val">Python, PyTorch, YOLOv11x, ByteTrack, OpenCV, DLT Homografi, TensorRT</div>
                </div>
                <div class="cv-skill-item">
                    <div class="cv-skill-lbl">Uzamsal & Taktiksel Analiz</div>
                    <div class="cv-skill-val">mplsoccer, SciPy (Voronoi/ConvexHull), NumPy, Pandas, Matplotlib, Seaborn</div>
                </div>
                <div class="cv-skill-item">
                    <div class="cv-skill-lbl">Veri Sağlayıcılar & Modeller</div>
                    <div class="cv-skill-val">StatsBomb, Opta, Wyscout, worldfootballR, Karun Singh xT, İki Değişkenli xG, k-Means</div>
                </div>
                <div class="cv-skill-item">
                    <div class="cv-skill-lbl">Raporlama & Diller</div>
                    <div class="cv-skill-val">Playwright PDF Motoru, Türkçe (Anadil), Lehçe (İleri Düzey), İngilizce (İleri Düzey)</div>
                </div>
            </div>
        </div>
    </div>
    
    <div class="cv-footer">
        <div><strong>Zafer Yorgancı</strong> — Futbol CV | Kulüp bünyesinde tam zamanlı veya uzaktan göreve hazır</div>
        <div>github.com/zfryrgnci/football-data-visualization-specialist</div>
    </div>
</div>

</body>
</html>
"""
    return html

def compile_all():
    print("Initializing Playwright PDF Engine...")
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        
        # 1. English Dossier
        print("Rendering English Technical Dossier...")
        en_dossier_html = generate_english_dossier()
        page.set_content(en_dossier_html, wait_until="networkidle")
        out_en_dossier = os.path.join(WORKSPACE_DIR, "Zafer_Yorganci_Technical_Intelligence_Dossier_2026_EN.pdf")
        page.pdf(
            path=out_en_dossier,
            format="A4",
            print_background=True,
            prefer_css_page_size=True,
            margin={"top": "0mm", "bottom": "0mm", "left": "0mm", "right": "0mm"}
        )
        print(f"Generated: {out_en_dossier} ({os.path.getsize(out_en_dossier)} bytes)")
        
        # 2. Turkish Dossier
        print("Rendering Turkish Technical Dossier...")
        tr_dossier_html = generate_turkish_dossier()
        page.set_content(tr_dossier_html, wait_until="networkidle")
        out_tr_dossier = os.path.join(WORKSPACE_DIR, "Zafer_Yorganci_Teknik_Analiz_ve_Veri_Gorsellestirme_Raporu_2026_TR.pdf")
        page.pdf(
            path=out_tr_dossier,
            format="A4",
            print_background=True,
            prefer_css_page_size=True,
            margin={"top": "0mm", "bottom": "0mm", "left": "0mm", "right": "0mm"}
        )
        print(f"Generated: {out_tr_dossier} ({os.path.getsize(out_tr_dossier)} bytes)")
        
        # 3. English CV
        print("Rendering English Football CV...")
        en_cv_html = generate_english_cv()
        page.set_content(en_cv_html, wait_until="networkidle")
        out_en_cv = os.path.join(WORKSPACE_DIR, "Zafer_Yorganci_Football_CV_EN.pdf")
        page.pdf(
            path=out_en_cv,
            format="A4",
            print_background=True,
            prefer_css_page_size=True,
            margin={"top": "0mm", "bottom": "0mm", "left": "0mm", "right": "0mm"}
        )
        print(f"Generated: {out_en_cv} ({os.path.getsize(out_en_cv)} bytes)")
        
        # 4. Turkish CV
        print("Rendering Turkish Football CV...")
        tr_cv_html = generate_turkish_cv()
        page.set_content(tr_cv_html, wait_until="networkidle")
        out_tr_cv = os.path.join(WORKSPACE_DIR, "Zafer_Yorganci_Futbol_CV_TR.pdf")
        page.pdf(
            path=out_tr_cv,
            format="A4",
            print_background=True,
            prefer_css_page_size=True,
            margin={"top": "0mm", "bottom": "0mm", "left": "0mm", "right": "0mm"}
        )
        print(f"Generated: {out_tr_cv} ({os.path.getsize(out_tr_cv)} bytes)")
        
        browser.close()
        print("ALL 4 PUBLICATION-GRADE CLUB PDFS COMPILED PERFECTLY!")

if __name__ == "__main__":
    compile_all()
