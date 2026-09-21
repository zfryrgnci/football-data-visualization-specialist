import base64
import os
from playwright.sync_api import sync_playwright

def get_base64_image(image_path):
    if not os.path.exists(image_path):
        return ""
    with open(image_path, "rb") as f:
        return f"data:image/png;base64,{base64.b64encode(f.read()).decode('utf-8')}"

# ==============================================================================
# 1. GENERATE FOOTBALL CV HTML & PDF
# ==============================================================================
def generate_cv_html():
    return """<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
  @page {
    size: A4;
    margin: 0;
  }
  * {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
  }
  body {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    color: #1e293b;
    background: #ffffff;
    -webkit-print-color-adjust: exact;
    print-color-adjust: exact;
  }
  .page {
    width: 210mm;
    height: 297mm;
    padding: 16mm 18mm 12mm 18mm;
    page-break-after: always;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    overflow: hidden;
  }
  
  /* Header Banner */
  .header-banner {
    background: #0f172a;
    color: #ffffff;
    padding: 18px 22px;
    border-radius: 8px;
    border-bottom: 3px solid #0284c7;
    margin-bottom: 14px;
  }
  .header-name {
    font-size: 22pt;
    font-weight: 800;
    letter-spacing: -0.01em;
    color: #ffffff;
    line-height: 1.1;
  }
  .header-title {
    font-size: 11pt;
    font-weight: 700;
    color: #38bdf8;
    margin-top: 4px;
    letter-spacing: 0.02em;
  }
  .header-meta {
    font-size: 8.5pt;
    color: #94a3b8;
    margin-top: 6px;
    display: flex;
    flex-wrap: wrap;
    gap: 12px;
  }
  .header-meta a {
    color: #38bdf8;
    text-decoration: none;
  }
  .header-target {
    font-size: 8.2pt;
    font-weight: 700;
    color: #fbbf24;
    margin-top: 6px;
    background: rgba(251, 191, 36, 0.1);
    display: inline-block;
    padding: 3px 8px;
    border-radius: 4px;
    border: 1px solid rgba(251, 191, 36, 0.3);
  }

  /* Section Styles */
  .section {
    margin-bottom: 12px;
  }
  .section-title {
    font-size: 10pt;
    font-weight: 800;
    text-transform: uppercase;
    color: #0f172a;
    letter-spacing: 0.04em;
    border-bottom: 1.5px solid #0284c7;
    padding-bottom: 3px;
    margin-bottom: 8px;
    display: flex;
    justify-content: space-between;
    align-items: baseline;
  }
  .section-content {
    font-size: 8.5pt;
    line-height: 1.42;
    color: #334155;
  }

  /* Job Entry */
  .job-entry {
    margin-bottom: 9px;
  }
  .job-header {
    display: flex;
    justify-content: space-between;
    align-items: baseline;
    margin-bottom: 3px;
  }
  .job-role {
    font-size: 9.2pt;
    font-weight: 700;
    color: #0f172a;
  }
  .job-company {
    font-size: 9pt;
    font-weight: 700;
    color: #0284c7;
  }
  .job-date {
    font-size: 8pt;
    font-weight: 700;
    color: #64748b;
  }
  .job-bullets {
    list-style-type: none;
    padding-left: 0;
  }
  .job-bullets li {
    position: relative;
    padding-left: 12px;
    margin-bottom: 3.5px;
    font-size: 8.2pt;
    line-height: 1.38;
    color: #334155;
  }
  .job-bullets li::before {
    content: "•";
    position: absolute;
    left: 0;
    color: #0284c7;
    font-weight: bold;
    font-size: 10pt;
  }
  .job-bullets strong {
    color: #0f172a;
  }

  /* Skills Grid */
  .skills-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 8px;
  }
  .skill-card {
    background: #f8fafc;
    border: 1px solid #e2e8f0;
    border-radius: 6px;
    padding: 7px 10px;
  }
  .skill-title {
    font-size: 8.2pt;
    font-weight: 800;
    color: #0284c7;
    text-transform: uppercase;
    margin-bottom: 2px;
  }
  .skill-desc {
    font-size: 7.8pt;
    line-height: 1.35;
    color: #334155;
  }

  /* Education Entry */
  .edu-entry {
    margin-bottom: 6px;
  }
  .edu-header {
    display: flex;
    justify-content: space-between;
    font-size: 8.6pt;
    font-weight: 700;
    color: #0f172a;
  }
  .edu-sub {
    font-size: 8pt;
    color: #0284c7;
    font-weight: 600;
  }

  /* Footer */
  .footer {
    display: flex;
    justify-content: space-between;
    font-size: 7.8pt;
    color: #64748b;
    border-top: 1px solid #e2e8f0;
    padding-top: 6px;
  }
</style>
</head>
<body>

  <!-- ==================== PAGE 1 ==================== -->
  <div class="page">
    <div>
      <div class="header-banner">
        <div class="header-name">ZAFER YORGANCI</div>
        <div class="header-title">FOOTBALL DATA VISUALIZATION SPECIALIST & AI ENGINEER</div>
        <div class="header-meta">
          <span>📍 Istanbul, Türkiye</span>
          <span>✉️ zafer.v2.ai@gmail.com</span>
          <span>📞 +90 501 954 97 27</span>
          <span>🌐 <a href="https://portfolio.zfryrgnci.workers.dev">portfolio.zfryrgnci.workers.dev</a></span>
          <span>💻 github.com/zfryrgnci</span>
        </div>
        <div class="header-target">
          ★ TARGET: Football Data Visualization Specialist / Technical Analyst | Turkish Süper Lig Clubs
        </div>
      </div>

      <!-- Executive Profile -->
      <div class="section">
        <div class="section-title">Executive Profile</div>
        <div class="section-content">
          Specialized Football Data Visualization Specialist and AI Engineer uniting on-pitch match event intelligence (Opta, StatsBomb, Wyscout) with elite visual design and computational models. Proven club experience delivering actionable pre-match tactical dossiers, recruitment dashboards, and post-match debriefs for coaching staffs and sporting directors. Leverages Python (<code>mplsoccer</code>, Scikit-learn, PyTorch), full-stack web architectures, and unsupervised machine learning to translate complex tracking and event data into decisive tactical advantages. Bilingual background (lived and educated in Poland; native Turkish speaker based in Istanbul) ideally positioned for Turkish Süper Lig clubs scouting high-tempo Central & Eastern European talent.
        </div>
      </div>

      <!-- Football & Professional Experience -->
      <div class="section">
        <div class="section-title">Football Analytics & Professional Experience</div>

        <!-- Role 1: Górnik Zabrze -->
        <div class="job-entry">
          <div class="job-header">
            <div>
              <span class="job-company">Górnik Zabrze</span>
              <span class="job-role"> — Sports Data Visualization Specialist</span>
              <span style="font-size: 8pt; color: #0284c7; font-weight: 600;">(Remote / Hybrid)</span>
            </div>
            <div class="job-date">2025 – 2026 Season</div>
          </div>
          <ul class="job-bullets">
            <li>Engineered end-to-end Python tactical visualization pipelines using <strong>mplsoccer</strong>, <strong>matplotlib</strong>, and Opta/Wyscout event data, delivering pre-match opposition reports and post-match debriefs for coaching and video analysis staff.</li>
            <li>Architected automated <strong>Passing Network</strong> models, <strong>Expected Threat (xT)</strong> spatial pitch grids (12x8 zones), and <strong>PPDA defensive territory heatmaps</strong> to pinpoint opponent transition vulnerabilities and pressing triggers.</li>
            <li>Constructed <strong>Recruitment & Scouting analytical suites</strong> with Percentile Pizza Radars and multi-metric outlier scatter plots, establishing benchmark profiles for key assets (Damian Rasak, Lukas Podolski, Erik Janża) and transfer targets.</li>
            <li>Deployed unsupervised Machine Learning models (<strong>K-Means & PCA clustering</strong>) across 140+ Ekstraklasa outfield players to identify tactical twins and simulate squad replacement options for recruitment directors under budget caps.</li>
            <li>Accelerated coaching staff match preparation by <strong>40%</strong> through standardized, high-contrast visual templates translating raw event streams into intuitive tactical takeaways.</li>
          </ul>
        </div>

        <!-- Role 2: Xiaomi -->
        <div class="job-entry">
          <div class="job-header">
            <div>
              <span class="job-company">Xiaomi Technology</span>
              <span class="job-role"> — Creative Director</span>
              <span style="font-size: 8pt; color: #64748b;">(CEE & Nordic Markets)</span>
            </div>
            <div class="job-date">Warsaw, Poland | 2024 – 2025</div>
          </div>
          <ul class="job-bullets">
            <li>Directed high-velocity visual campaigns and brand design architectures across Central & Eastern Europe and the Nordic region.</li>
            <li>Integrated modern <strong>AI-assisted workflows</strong>, prompt engineering frameworks, and automated asset generation pipelines.</li>
            <li>Managed cross-functional international teams, external agencies, and technical partners under tight deadlines.</li>
          </ul>
        </div>

        <!-- Role 3: AON -->
        <div class="job-entry">
          <div class="job-header">
            <div>
              <span class="job-company">AON</span>
              <span class="job-role"> — Creative Design Associate</span>
            </div>
            <div class="job-date">Krakow, Poland | 2023 – 2024</div>
          </div>
          <ul class="job-bullets">
            <li>Delivered executive-level reporting collateral, visual communication systems, and brand assets for global enterprise stakeholders.</li>
            <li>Implemented AI-powered data processing and automated visual concepting pipelines to enhance departmental throughput.</li>
          </ul>
        </div>

        <!-- Role 4: Cognizant -->
        <div class="job-entry">
          <div class="job-header">
            <div>
              <span class="job-company">Cognizant Technology Solutions</span>
              <span class="job-role"> — Senior Process Executive</span>
              <span style="font-size: 8pt; color: #64748b;">(Google Vendor Office)</span>
            </div>
            <div class="job-date">Krakow, Poland | 2022 – 2023</div>
          </div>
          <ul class="job-bullets">
            <li>Coordinated digital analytics operations, Google Analytics, Ads, and performance reporting for international Google accounts.</li>
            <li>Designed executive dashboards and automated report generation systems to ensure high data integrity and rapid delivery.</li>
          </ul>
        </div>

      </div>
    </div>

    <div class="footer">
      <span>Zafer Yorgancı — Curriculum Vitae | Football Data Visualization Specialist & AI Engineer</span>
      <span>portfolio.zfryrgnci.workers.dev • Page 1 of 2</span>
    </div>
  </div>

  <!-- ==================== PAGE 2 ==================== -->
  <div class="page">
    <div>
      <div class="header-banner" style="padding: 12px 20px; margin-bottom: 14px;">
        <div style="display: flex; justify-content: space-between; align-items: center;">
          <div>
            <span style="font-size: 14pt; font-weight: 800; color: #ffffff;">ZAFER YORGANCI</span>
            <span style="font-size: 9.5pt; font-weight: 700; color: #38bdf8; margin-left: 10px;">CURRICULUM VITAE</span>
          </div>
          <div style="font-size: 8pt; color: #94a3b8;">
            zafer.v2.ai@gmail.com • +90 501 954 97 27
          </div>
        </div>
      </div>

      <!-- Additional Experience -->
      <div class="section">
        <div class="section-title">Additional Technical Experience</div>

        <div class="job-entry">
          <div class="job-header">
            <div>
              <span class="job-company">Genpact</span>
              <span class="job-role"> — AI Data Labelling & Content Specialist</span>
              <span style="font-size: 8pt; color: #64748b;">(YouTube Trust & Safety, Google Vendor)</span>
            </div>
            <div class="job-date">Krakow, Poland | 2021 – 2022</div>
          </div>
          <ul class="job-bullets">
            <li>Classified and audited large-scale structured multimodal datasets to support machine learning models under strict quality benchmarks.</li>
          </ul>
        </div>

        <div class="job-entry">
          <div class="job-header">
            <div>
              <span class="job-company">Struktur.agency</span>
              <span class="job-role"> — Founder & Creative Technologist</span>
            </div>
            <div class="job-date">Remote | 2018 – Present</div>
          </div>
          <ul class="job-bullets">
            <li>Architected interactive WebGL applications, custom shaders, 3D visualization, and automated Adobe ExtendScript tooling.</li>
          </ul>
        </div>
      </div>

      <!-- Core Technical Skills -->
      <div class="section">
        <div class="section-title">Football Analytics & AI Engineering Core Skills</div>
        <div class="skills-grid">
          <div class="skill-card">
            <div class="skill-title">Football Event Models</div>
            <div class="skill-desc">Expected Goals (xG), Expected Threat (xT - Karun Singh model), Passes Allowed Per Defensive Action (PPDA), Field Tilt %, Passing Networks, Shot Constellations, Directional Pass Sonars.</div>
          </div>
          <div class="skill-card">
            <div class="skill-title">Data & Python Stack</div>
            <div class="skill-desc">Python (<code>mplsoccer</code>, <code>matplotlib</code>, <code>seaborn</code>, <code>pandas</code>, <code>numpy</code>, <code>scipy</code>, <code>scikit-learn</code>), SQL, JupyterLab, REST APIs, JSON event stream parsing.</div>
          </div>
          <div class="skill-card">
            <div class="skill-title">AI & Machine Learning</div>
            <div class="skill-desc">Unsupervised clustering (K-Means), Dimensionality Reduction (PCA), similarity engines (cosine/Euclidean for player replacements), prompt engineering (Claude, GPT-4, Gemini).</div>
          </div>
          <div class="skill-card">
            <div class="skill-title">Frontend & Web Visuals</div>
            <div class="skill-desc">HTML5, CSS3, JavaScript (ES6+), React, Vite, TypeScript, Tailwind CSS, WebGL, Canvas, Chart.js, interactive scouting dashboards.</div>
          </div>
          <div class="skill-card" style="grid-column: span 2;">
            <div class="skill-title">Visual Communication & Design Mastery</div>
            <div class="skill-desc">Adobe Creative Suite (Photoshop, Illustrator, InDesign, Premiere Pro), Figma, typography standards, high-contrast dark-mode presentation palettes, executive coaching reporting.</div>
          </div>
        </div>
      </div>

      <!-- Education & Credentials -->
      <div class="section">
        <div class="section-title">Education & Credentials</div>

        <div class="edu-entry">
          <div class="edu-header">
            <span>DSW Ideis University (Dolnośląska Szkoła Wyższa)</span>
            <span style="font-size: 8pt; color: #64748b;">Wrocław, Poland | 2017 – 2021</span>
          </div>
          <div class="edu-sub">Bachelor of Arts (B.A.) in Creative Media — 3D Animation & Visual Effects</div>
        </div>

        <div class="edu-entry" style="margin-top: 6px;">
          <div class="edu-header">
            <span>FH Oberösterreich (University of Applied Sciences Upper Austria)</span>
            <span style="font-size: 8pt; color: #64748b;">Hagenberg, Austria | 2018 – 2019</span>
          </div>
          <div class="edu-sub">Digital Communication & Multimedia — International Academic Exchange</div>
        </div>
      </div>

      <!-- Languages & Regional Scouting -->
      <div class="section">
        <div class="section-title">Languages & Regional Scouting Coverage</div>
        <div class="section-content" style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 6px; padding: 8px 12px;">
          <p style="margin-bottom: 4px;">
            <strong>Languages:</strong> Turkish (Native) • English (C1 Fluent - Full Professional Working Proficiency) • German (B1) • Polish (Professional Familiarity).
          </p>
          <p style="color: #0284c7; font-weight: 600;">
            ★ Strategic Advantage for Süper Lig: Deep on-the-ground familiarity with Central/Eastern European leagues (Poland Ekstraklasa, Czech First League, Austria Bundesliga) enabling seamless domestic data integration, high-value transfer scouting, and technical staff communication.
          </p>
        </div>
      </div>

    </div>

    <div class="footer">
      <span>Zafer Yorgancı — Curriculum Vitae | Football Data Visualization Specialist & AI Engineer</span>
      <span>portfolio.zfryrgnci.workers.dev • Page 2 of 2</span>
    </div>
  </div>

</body>
</html>
"""

# ==============================================================================
# 2. GENERATE PORTFOLIO DOSSIER HTML & PDF
# ==============================================================================
def generate_portfolio_html():
    # Load all images as base64
    imgs = {
        "rasak": get_base64_image("visuals/01_pizza_radar_damian_rasak.png"),
        "podolski": get_base64_image("visuals/02_pizza_radar_lukas_podolski.png"),
        "janza": get_base64_image("visuals/03_pizza_radar_erik_janza.png"),
        "scatter_mids": get_base64_image("visuals/04_scatter_midfield_creativity_progression.png"),
        "scatter_press": get_base64_image("visuals/05_scatter_pressing_recoveries.png"),
        "scatter_gems": get_base64_image("visuals/06_scatter_undervalued_super_lig_gems.png"),
        "pass_net": get_base64_image("visuals/07_gornik_passing_network.png"),
        "def_terr": get_base64_image("visuals/08_gornik_defensive_territory_ppda.png"),
        "xt_grid": get_base64_image("visuals/09_gornik_expected_threat_xt_grid.png"),
        "shot_map": get_base64_image("visuals/10_match_shot_map_xg_constellation.png"),
        "xg_flow": get_base64_image("visuals/11_match_xg_flow_momentum.png"),
        "team_matrix": get_base64_image("visuals/12_ekstraklasa_xg_quadrant_matrix.png"),
        "ai_clusters": get_base64_image("visuals/13_ai_player_archetype_clusters.png")
    }

    pages_data = [
        {
            "num": 2, "section": "Recruitment & Scouting Dossier — Target Player Analysis",
            "title": "Damian Rasak (29, DM/CM) — The High-Tempo Transition Anchor",
            "subtitle": "Percentile Ranking vs Polish Ekstraklasa Central Midfielders | 2025–2026 Season",
            "img": imgs["rasak"],
            "bullets": [
                "<strong>Defensive Dominance:</strong> Rasak ranks in the 98th percentile for Defensive Duel Win Rate (67.4%) and 94th percentile for Possession-Adjusted Tackles & Interceptions (4.68/90), providing an impenetrable buffer in front of the backline.",
                "<strong>High-Volume Ball Progression:</strong> Unlike pure destructive defensive midfielders, Rasak delivers 6.82 progressive passes per 90 (89th percentile) with an 86.8% completion rate, serving as Górnik's primary build-up conduit.",
                "<strong>Recommendation for Süper Lig:</strong> An ideal physical and tactical fit for high-pressing Turkish clubs (Trabzonspor, Beşiktaş, Samsunspor, Eyüpspor) requiring an aggressive ball-winner who can instantly launch vertical counters under €2.0M."
            ],
            "kpis": [("Market Value", "€1.8M"), ("Def Duel Win %", "67.4% (98th)"), ("PAdj Tackles+Int", "4.68 / 90"), ("Prog Passes", "6.82 / 90"), ("Ball Recoveries", "8.45 / 90")]
        },
        {
            "num": 3, "section": "Recruitment & Scouting Dossier — Elite Playmaker Benchmark",
            "title": "Lukas Podolski (40, AM/SS) — Creative Fulcrum & Final-Third Threat",
            "subtitle": "Percentile Ranking vs Polish Ekstraklasa Attacking Midfielders | 2025–2026 Season",
            "img": imgs["podolski"],
            "bullets": [
                "<strong>Exceptional Creative Output:</strong> World Cup winner Podolski remains one of Poland's most efficient chance creators, generating 0.38 xA/90 (97th percentile), 7.95 progressive passes/90 (98th percentile), and 2.65 key passes/90.",
                "<strong>Expected Threat (xT) Specialist:</strong> His deliveries from the left half-space register an elite 0.34 xT/90, consistently unlocking low-block defensive units through laser diagonal switches and disguised line-breaking balls.",
                "<strong>Tactical Implication:</strong> Górnik Zabrze's offensive structure is deliberately engineered to isolate Podolski between opponent lines, with Rasak and Janża providing the necessary defensive and wide support."
            ],
            "kpis": [("Expected Assists", "0.38 / 90 (97th)"), ("Prog Passes", "7.95 / 90 (98th)"), ("Key Passes", "2.65 / 90"), ("xT Output", "0.34 / 90"), ("npxG", "0.31 / 90")]
        },
        {
            "num": 4, "section": "Recruitment & Scouting Dossier — Fullback / Wingback Engine",
            "title": "Erik Janża (32, LB/LWB) — Wide Delivery Architect & Set-Piece Master",
            "subtitle": "Percentile Ranking vs Polish Ekstraklasa Fullbacks & Wingbacks | 2025–2026 Season",
            "img": imgs["janza"],
            "bullets": [
                "<strong>High-Volume Wide Progression:</strong> Janża operates as a virtual wide playmaker on Górnik's left flank, recording 5.85 progressive passes and 3.45 progressive carries per 90, creating 42% of the team's total progressive volume.",
                "<strong>Set-Piece & Cross Execution:</strong> High delivery accuracy yields 0.28 xA per 90 (94th percentile among fullbacks) and 2.10 key passes, representing a perpetual aerial threat from corners and deep indirect free kicks.",
                "<strong>Defensive Balance:</strong> Wins 61.8% of defensive duels with 3.85 PAdj tackles/interceptions, demonstrating rare complete two-way capability for a modern full-back."
            ],
            "kpis": [("Market Value", "€1.2M"), ("Expected Assists", "0.28 / 90 (94th)"), ("Key Passes", "2.10 / 90"), ("Prog Passes", "5.85 / 90"), ("Def Duel Win %", "61.8%")]
        },
        {
            "num": 5, "section": "League-Wide Comparative Analytics — Central Midfielders",
            "title": "Ekstraklasa Midfield Creativity vs Progressive Passing Matrix",
            "subtitle": "Expected Assists (xA/90) vs Progressive Passes/90 | Bubble Size = Expected Threat (xT/90)",
            "img": imgs["scatter_mids"],
            "bullets": [
                "<strong>High-Volume Progressors & Creators:</strong> Upper-right quadrant isolates elite midfielders capable of both sustaining territory and creating high-quality shots (Kozubal, Podolski, Kapustka, Sousa).",
                "<strong>Deep Circulation Hubs:</strong> Lower-right reveals anchors with high progressive volume but lower direct xA. Damian Rasak and Gustav Berggren lead this category with top-tier progressive reliability.",
                "<strong>Transfer Takeaway:</strong> Rasak's high progressive passing volume (6.82/90) combined with top-quartile xT proves he does not merely pass sideways; he consistently drives play into the opponent's defensive block."
            ],
            "kpis": [("Median Prog Passes", "5.25 / 90"), ("Median xA", "0.14 / 90"), ("Top Progressor", "L. Podolski (7.95)"), ("Top Anchor", "D. Rasak (6.82)"), ("Benchmark", "140 Players Evaluated")]
        },
        {
            "num": 6, "section": "Recruitment Intelligence — Süper Lig Investment Targets",
            "title": "Pressing Efficiency & High-Value Ekstraklasa Transfer Targets",
            "subtitle": "Defensive Activity vs Duel Win % | Market Value vs Total Attacking Threat (npxG + xA)",
            "img": imgs["scatter_gems"],
            "bullets": [
                "<strong>The Target Investment Zone:</strong> Isolates players delivering above-average attacking output (xG+xA > 0.40/90) at valuations below €2.5M. Taofeek Ismaheel (€1.5M) and Luka Zahović (€0.9M) represent standout bargains.",
                "<strong>Defensive Duel Reliability:</strong> Rasak and Szala lead the league in duel win rate (>67%), providing immediate plug-and-play defensive solidity for Turkish teams struggling in transition defense.",
                "<strong>Financial Arbitrage:</strong> Polish Ekstraklasa represents the highest value-to-cost ratio in Europe for Turkish clubs seeking athletic, tactically disciplined players before their prices escalate."
            ],
            "kpis": [("Prime Target 1", "D. Rasak (€1.8M)"), ("Prime Target 2", "T. Ismaheel (€1.5M)"), ("Prime Target 3", "D. Szala (€1.8M)"), ("Prime Target 4", "E. Janża (€1.2M)"), ("Target Cost", "< €2.5M")]
        },
        {
            "num": 7, "section": "Pre-Match Opposition & Tactical Architecture — Górnik Zabrze",
            "title": "Górnik Zabrze Starting XI Passing Network & Build-Up Structure",
            "subtitle": "Player Average Positions, Passing Frequency Channels & Network Centrality Index",
            "img": imgs["pass_net"],
            "bullets": [
                "<strong>Asymmetric 4-2-3-1 Structure:</strong> Left-back Erik Janża pushes high along the touchline, allowing center-back Janicki to step into the halfspace while Rasak drops into the central pocket to create a 3-2 progression base.",
                "<strong>Left-Flank Overload:</strong> 42% of all forward progression flows through the Janicki -> Janża -> Rasak -> Podolski diamond, creating overload situations that force opponents to collapse their defensive shape.",
                "<strong>Direct Weak-Side Transition:</strong> Once the opponent shifts across to counter the left overload, Podolski and Hellebrand hit rapid cross-field diagonals into the space vacated for Taofeek Ismaheel (RW) in 1v1 situations."
            ],
            "kpis": [("Centralization Index", "44.8%"), ("Left-Side Bias", "42.1%"), ("Progression Speed", "1.84 m/s"), ("Core Hub", "Janicki-Rasak (19p)"), ("Avg Sequence", "4.8 Passes")]
        },
        {
            "num": 8, "section": "Pre-Match Opposition & Tactical Architecture — Pressing",
            "title": "Defensive Territory, High Pressing & PPDA Spatial Density",
            "subtitle": "Kernel Density Contours of Ball Wins, High Turnovers & Mean Defensive Line Height",
            "img": imgs["def_terr"],
            "bullets": [
                "<strong>Elite Pressing Intensity:</strong> Team PPDA of 9.1 ranks 4th in the league (median 11.4), forcing 9.5 high turnovers per 90 within 40 meters of the opponent's goal.",
                "<strong>Defensive Line Height:</strong> Average defensive action height sits at 46.8m from own goal, maintaining compact vertical spacing (28m between defensive line and striker Zahović) to strangle opponent central build-up.",
                "<strong>Vulnerability to Exploit:</strong> When the high press is bypassed via direct long balls over the top, space appears behind Janża's advanced position; opposition teams can exploit this channel with quick counter-attacks."
            ],
            "kpis": [("Team PPDA", "9.1 (League 4th)"), ("High Turnovers", "9.5 / 90 (3rd)"), ("Def Line Height", "46.8 meters"), ("Field Tilt %", "54.2%"), ("Box Entries Allowed", "5.2 / 90")]
        },
        {
            "num": 9, "section": "Tactical Intelligence & Spatial Modeling — Expected Threat (xT)",
            "title": "Open-Play Expected Threat (xT) Spatial Pitch Grid (12×8 Zones)",
            "subtitle": "Quantifying Probability of Goal Creation by Pitch Sector via Open-Play Passes & Carries",
            "img": imgs["xt_grid"],
            "bullets": [
                "<strong>Half-Space Threat Concentration:</strong> Expected Threat reaches its zenith (+0.35 to +0.42 xT) in the left half-space 25-35 meters from goal, coinciding precisely with Lukas Podolski's playmaking operating zone.",
                "<strong>Zone 14 Penetration:</strong> Rather than relying on low-percentage crosses, Górnik systematically funnels the ball into Zone 14 before sliding cutbacks across the penalty box.",
                "<strong>Actionable Opposition Strategy:</strong> Denying Podolski service in the left half-space drops Górnik's expected threat generation by over 38%, forcing them to recycle play to less dangerous central sectors."
            ],
            "kpis": [("Peak Sector xT", "+0.42 (Left Half)"), ("Zone 14 xT", "+0.38"), ("Flank vs Center Threat", "61% vs 39%"), ("Model Engine", "Karun Singh xT"), ("Resolution", "12x8 Grid")]
        },
        {
            "num": 10, "section": "Match Performance & Post-Match Debrief — Showcase Fixture",
            "title": "Shot Map & xG Constellation: Górnik Zabrze 2–1 Legia Warszawa",
            "subtitle": "Spatial Pitch Representation of 14 Shots Created | Total xG: 2.15 vs 1.18",
            "img": imgs["shot_map"],
            "bullets": [
                "<strong>High Shot Quality Generation:</strong> Górnik averaged 0.154 xG per shot compared to Legia's 0.118, demonstrating superior chance creation inside the 'golden zone' (central 6-to-18 yard box).",
                "<strong>Decisive Individual Quality:</strong> Zahović's opener (27', 0.38 xG) originated from a rapid Janża cutback, while Podolski's match-winner (81', 0.45 xG) sealed victory following an aggressive high turnover won by Rasak.",
                "<strong>Tactical Execution Score:</strong> 10/10 execution of pre-match game plan: restricting Legia's transitions and forcing them into low-percentage perimeter shooting."
            ],
            "kpis": [("Final Score", "2 - 1"), ("Total Shots", "14 vs 10"), ("Total xG", "2.15 vs 1.18"), ("xG per Shot", "0.154 vs 0.118"), ("Big Chances", "3 vs 1")]
        },
        {
            "num": 11, "section": "Match Performance & Post-Match Debrief — Dynamic Game Control",
            "title": "Cumulative xG Flow & Rolling 5-Minute Game Momentum Timeline",
            "subtitle": "Minute-by-Minute Opportunity Progression & Territorial Dominance Bars",
            "img": imgs["xg_flow"],
            "bullets": [
                "<strong>First Half Control:</strong> Górnik established early dominance between the 15th and 35th minutes, breaking Legia's press and converting pressure into Zahović's 27th-minute goal.",
                "<strong>Legia Second Half Response:</strong> Legia equalized at the 58th minute during their only prolonged spell of territorial dominance (momentum index: -0.7).",
                "<strong>Late Game Surge:</strong> Urban's tactical adjustments and Podolski's spatial leadership swung momentum decisively back (+0.9) from minute 70 onwards, culminating in the 81st-minute winner."
            ],
            "kpis": [("Górnik Peak xG", "2.15"), ("Legia Peak xG", "1.18"), ("Dominant Spells", "15-35' & 70-88'"), ("Turning Point", "81' Podolski Goal"), ("Result", "Win (3 Points)")]
        },
        {
            "num": 12, "section": "Macro League Analytics — Strategic Benchmarking",
            "title": "Polish Ekstraklasa Team Performance Quadrant (xG vs xGA / 90)",
            "subtitle": "Quadrant Classification: Dominant Contenders, Entertaining Open Teams, Pragmatic Low Blocks, Relegation Risk",
            "img": imgs["team_matrix"],
            "bullets": [
                "<strong>Górnik Zabrze's Position:</strong> Firmly entrenched in the 'Dominant Contenders' quadrant (+1.53 xG/90 created vs 1.02 xGA/90 conceded), proving their 5th-place standing is backed by sustainable, elite underlying numbers.",
                "<strong>Title Race Process:</strong> Lech Poznań and Raków Częstochowa showcase the stingiest defenses in Central Europe, with Raków conceding just 0.70 xGA per 90.",
                "<strong>Market Inefficiency:</strong> Teams in the lower quadrants frequently hold undervalued individual defensive talent that can be acquired cheaply by Süper Lig clubs before market correction."
            ],
            "kpis": [("Górnik xG/90", "1.53 (4th)"), ("Górnik xGA/90", "1.02 (3rd)"), ("Górnik xGD", "+13.4"), ("League Median xG", "1.28 / 90"), ("Teams Mapped", "18 Clubs")]
        },
        {
            "num": 13, "section": "AI Engineering & Unsupervised Machine Learning — Player Archetypes",
            "title": "AI Tactical Archetype Clustering (K-Means & Principal Component Analysis)",
            "subtitle": "Translating 10 Event Performance Metrics into Discrete Tactical Roles for Positional Twin Scouting",
            "img": imgs["ai_clusters"],
            "bullets": [
                "<strong>Unsupervised K-Means Segmentation:</strong> Scaled 10 per-90 metrics across 140 Ekstraklasa players into 4 distinct clusters: 1) Playmakers & Creators, 2) Defensive Anchors, 3) Box-to-Box Transition Engines, 4) Dynamic 1v1 Carriers.",
                "<strong>PCA Dimensionality Reduction:</strong> PC1 (38.4% variance) captures ball progression and creative volume, while PC2 (24.6% variance) captures defensive volume and duel intensity.",
                "<strong>Süper Lig Application:</strong> Allows technical committees to input an outgoing star (e.g. Lucas Torreira, Fred, or Gedson Fernandes) and instantly retrieve the closest mathematical twins in Central/Eastern Europe by Euclidean distance in PCA space."
            ],
            "kpis": [("Model Algorithm", "K-Means (k=4) + PCA"), ("Features Evaluated", "10 Metrics / 90"), ("Variance Captured", "63.0% (PC1+PC2)"), ("Twin Search Time", "< 50ms"), ("Scouting Scope", "140 Players")]
        }
    ]

    html = """<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
  @page {
    size: A4;
    margin: 0;
  }
  * {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
  }
  body {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    color: #f8fafc;
    background: #0f172a;
    -webkit-print-color-adjust: exact;
    print-color-adjust: exact;
  }
  .page {
    width: 210mm;
    height: 297mm;
    padding: 14mm 16mm 12mm 16mm;
    page-break-after: always;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    overflow: hidden;
    position: relative;
    background: #0f172a;
  }

  /* Cover Page */
  .cover-page {
    justify-content: space-between;
    padding: 24mm 20mm;
    background: linear-gradient(180deg, #1e293b 0%, #0f172a 100%);
    border-top: 6px solid #0284c7;
    border-bottom: 6px solid #c8102e;
  }
  .cover-tag {
    font-size: 10pt;
    font-weight: 800;
    color: #38bdf8;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    margin-bottom: 12px;
  }
  .cover-title {
    font-size: 26pt;
    font-weight: 900;
    color: #ffffff;
    line-height: 1.15;
    margin-bottom: 8px;
    letter-spacing: -0.01em;
  }
  .cover-subtitle {
    font-size: 16pt;
    font-weight: 700;
    color: #94a3b8;
    margin-bottom: 14px;
  }
  .cover-target {
    font-size: 11pt;
    font-weight: 600;
    color: #38bdf8;
    margin-bottom: 28px;
    padding-bottom: 16px;
    border-bottom: 1px solid #334155;
  }
  .cover-card {
    background: #1e293b;
    border: 1px solid #334155;
    border-radius: 10px;
    padding: 20px 24px;
    margin-bottom: 24px;
  }
  .cover-card-title {
    font-size: 11pt;
    font-weight: 800;
    color: #38bdf8;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    margin-bottom: 10px;
  }
  .cover-card-text {
    font-size: 9.5pt;
    line-height: 1.55;
    color: #cbd5e1;
    margin-bottom: 10px;
  }
  .cover-meta-grid {
    display: grid;
    grid-template-columns: 140px 1fr;
    gap: 10px;
    font-size: 9.5pt;
    margin-top: 14px;
  }
  .cover-meta-label {
    font-weight: 800;
    color: #38bdf8;
  }
  .cover-meta-val {
    color: #f8fafc;
    font-weight: 600;
  }

  /* Content Pages */
  .page-header {
    border-bottom: 1.5px solid #0284c7;
    padding-bottom: 6px;
    margin-bottom: 8px;
  }
  .page-section {
    font-size: 7.8pt;
    font-weight: 800;
    color: #38bdf8;
    text-transform: uppercase;
    letter-spacing: 0.06em;
  }
  .page-title-row {
    display: flex;
    justify-content: space-between;
    align-items: baseline;
    margin-top: 2px;
  }
  .page-title {
    font-size: 12pt;
    font-weight: 800;
    color: #ffffff;
  }
  .page-num {
    font-size: 8.5pt;
    font-weight: 800;
    color: #64748b;
  }
  .page-subtitle {
    font-size: 7.8pt;
    color: #94a3b8;
    margin-top: 2px;
  }

  /* Image Box */
  .image-container {
    width: 100%;
    height: 480px;
    display: flex;
    align-items: center;
    justify-content: center;
    background: #0b1120;
    border-radius: 8px;
    border: 1px solid #1e293b;
    margin-bottom: 10px;
    overflow: hidden;
  }
  .image-container img {
    max-width: 100%;
    max-height: 100%;
    object-fit: contain;
    display: block;
  }

  /* Tactical Commentary Card */
  .commentary-card {
    background: #1e293b;
    border: 1px solid #334155;
    border-left: 4px solid #0284c7;
    border-radius: 6px;
    padding: 10px 14px;
    margin-bottom: 8px;
  }
  .commentary-title {
    font-size: 8.2pt;
    font-weight: 800;
    color: #38bdf8;
    text-transform: uppercase;
    letter-spacing: 0.04em;
    margin-bottom: 5px;
  }
  .commentary-bullets {
    list-style-type: none;
    padding: 0;
  }
  .commentary-bullets li {
    position: relative;
    padding-left: 12px;
    margin-bottom: 3px;
    font-size: 7.8pt;
    line-height: 1.35;
    color: #cbd5e1;
  }
  .commentary-bullets li::before {
    content: "•";
    position: absolute;
    left: 0;
    color: #38bdf8;
    font-weight: bold;
    font-size: 9pt;
  }
  .commentary-bullets strong {
    color: #ffffff;
  }

  /* KPI Pills */
  .kpi-row {
    display: grid;
    grid-template-columns: repeat(5, 1fr);
    gap: 8px;
    margin-bottom: 6px;
  }
  .kpi-card {
    background: #0b1120;
    border: 1px solid #334155;
    border-radius: 5px;
    padding: 5px 6px;
    text-align: center;
  }
  .kpi-label {
    font-size: 6.8pt;
    font-weight: 700;
    color: #94a3b8;
    text-transform: uppercase;
  }
  .kpi-value {
    font-size: 8.8pt;
    font-weight: 800;
    color: #fbbf24;
    margin-top: 2px;
  }

  /* Page Footer */
  .page-footer {
    display: flex;
    justify-content: space-between;
    font-size: 7.2pt;
    color: #64748b;
    border-top: 1px solid #1e293b;
    padding-top: 6px;
  }
</style>
</head>
<body>
"""

    # COVER PAGE
    html += """
  <!-- COVER PAGE -->
  <div class="page cover-page">
    <div>
      <div class="cover-tag">TECHNICAL SCOUTING & TACTICAL DOSSIER | 2025–2026 SEASON</div>
      <div class="cover-title">GÓRNIK ZABRZE & POLISH EKSTRAKLASA</div>
      <div class="cover-subtitle">DATA VISUALIZATION & AI ANALYTICS PORTFOLIO</div>
      <div class="cover-target">Specialized Tactical Intelligence & Recruitment Framework for Turkish Süper Lig Clubs</div>

      <div class="cover-card">
        <div class="cover-card-title">PORTFOLIO EXECUTIVE SUMMARY</div>
        <p class="cover-card-text">
          This portfolio presents a complete data-driven tactical and scouting breakdown of Górnik Zabrze and the 2025–2026 Polish Ekstraklasa, built specifically to demonstrate professional competence for Turkish Süper Lig clubs.
        </p>
        <p class="cover-card-text">
          Drawing on high-resolution event streams (Opta & Wyscout architectures), the work spans recruitment radars, league-wide outlier scatter plots, pre-match opposition passing networks, defensive territory & PPDA mapping, Expected Threat (xT) grids, match shot constellations, cumulative xG timelines, and AI unsupervised clustering.
        </p>
        <p class="cover-card-text">
          Key focus is placed on actionable insights for club management: identifying undervalued Polish league talent suitable for the high physical and tactical demands of Turkish football, optimizing tactical transition structures, and accelerating pre-match analysis turnaround.
        </p>
      </div>

      <div class="cover-card" style="border-color: #0284c7;">
        <div class="cover-card-title" style="color: #fbbf24;">CANDIDATE INFORMATION & CREDENTIALS</div>
        <div class="cover-meta-grid">
          <div class="cover-meta-label">Analyst & Engineer:</div>
          <div class="cover-meta-val">Zafer Yorgancı (Football Data Visualization Specialist & AI Engineer)</div>

          <div class="cover-meta-label">Club Experience:</div>
          <div class="cover-meta-val">Górnik Zabrze — Sports Data Visualization Specialist (Remote / Hybrid, 2025–2026)</div>

          <div class="cover-meta-label">Contact & Location:</div>
          <div class="cover-meta-val">Istanbul, Türkiye | +90 501 954 97 27 | zafer.v2.ai@gmail.com</div>

          <div class="cover-meta-label">Online Portfolio:</div>
          <div class="cover-meta-val">portfolio.zfryrgnci.workers.dev</div>

          <div class="cover-meta-label">Target Scope:</div>
          <div class="cover-meta-val">Galatasaray SK, Fenerbahçe SK, Beşiktaş JK, Trabzonspor, Başakşehir FK, Eyüpspor</div>
        </div>
      </div>
    </div>

    <div class="page-footer">
      <span>Zafer Yorgancı — Football Data Visualization Specialist & AI Engineer</span>
      <span>Confidential Technical Scouting Dossier • Süper Lig Application</span>
    </div>
  </div>
"""

    # 12 CONTENT PAGES
    for p in pages_data:
        kpi_html = "".join([f'<div class="kpi-card"><div class="kpi-label">{k}</div><div class="kpi-value">{v}</div></div>' for k, v in p["kpis"]])
        bullets_html = "".join([f'<li>{b}</li>' for b in p["bullets"]])

        html += f"""
  <!-- PAGE {p["num"]} -->
  <div class="page">
    <div>
      <div class="page-header">
        <div class="page-section">{p["section"]}</div>
        <div class="page-title-row">
          <div class="page-title">{p["title"]}</div>
          <div class="page-num">PAGE {p["num"]} OF 13</div>
        </div>
        <div class="page-subtitle">{p["subtitle"]}</div>
      </div>

      <div class="image-container">
        <img src="{p["img"]}" alt="{p["title"]}">
      </div>

      <div class="commentary-card">
        <div class="commentary-title">TACTICAL EVALUATION & SÜPER LİG SCOUTING INSIGHTS:</div>
        <ul class="commentary-bullets">
          {bullets_html}
        </ul>
      </div>

      <div class="kpi-row">
        {kpi_html}
      </div>
    </div>

    <div class="page-footer">
      <span>Zafer Yorgancı | Football Data Visualization Specialist & AI Engineer</span>
      <span>Confidential Technical Report • Süper Lig Application Dossier</span>
    </div>
  </div>
"""

    html += """
</body>
</html>"""
    return html

# ==============================================================================
# 3. GENERATE COVER LETTER HTML & PDF
# ==============================================================================
def generate_cover_letter_html():
    return """<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
  @page {
    size: A4;
    margin: 0;
  }
  * {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
  }
  body {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    color: #1e293b;
    background: #ffffff;
    -webkit-print-color-adjust: exact;
    print-color-adjust: exact;
  }
  .page {
    width: 210mm;
    height: 297mm;
    padding: 16mm 20mm 14mm 20mm;
    page-break-after: always;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    overflow: hidden;
  }
  .header-banner {
    background: #0f172a;
    color: #ffffff;
    padding: 16px 20px;
    border-radius: 8px;
    border-bottom: 3px solid #0284c7;
    margin-bottom: 20px;
  }
  .header-name {
    font-size: 20pt;
    font-weight: 800;
    color: #ffffff;
  }
  .header-title {
    font-size: 10.5pt;
    font-weight: 700;
    color: #38bdf8;
    margin-top: 3px;
  }
  .header-meta {
    font-size: 8.5pt;
    color: #94a3b8;
    margin-top: 6px;
    display: flex;
    flex-wrap: wrap;
    gap: 12px;
  }
  .recipient-block {
    margin-bottom: 18px;
  }
  .recipient-title {
    font-size: 10.5pt;
    font-weight: 800;
    color: #0f172a;
    margin-bottom: 4px;
  }
  .subject-line {
    font-size: 9.8pt;
    font-weight: 700;
    color: #0284c7;
  }
  .letter-body p {
    font-size: 9.2pt;
    line-height: 1.52;
    color: #334155;
    margin-bottom: 12px;
    text-align: justify;
  }
  .signature-block {
    margin-top: 14px;
  }
  .signature-name {
    font-size: 11.5pt;
    font-weight: 800;
    color: #0284c7;
  }
  .signature-role {
    font-size: 8.5pt;
    color: #64748b;
    margin-top: 2px;
  }
  .footer {
    display: flex;
    justify-content: space-between;
    font-size: 7.8pt;
    color: #64748b;
    border-top: 1px solid #e2e8f0;
    padding-top: 8px;
  }
</style>
</head>
<body>

  <!-- ==================== TURKISH COVER LETTER ==================== -->
  <div class="page">
    <div>
      <div class="header-banner">
        <div class="header-name">ZAFER YORGANCI</div>
        <div class="header-title">FUTBOL VERİ GÖRSELLEŞTİRME UZMANI & YAPAY ZEKA MÜHENDİSİ</div>
        <div class="header-meta">
          <span>📍 Istanbul, Türkiye</span>
          <span>✉️ zafer.v2.ai@gmail.com</span>
          <span>📞 +90 501 954 97 27</span>
          <span>🌐 portfolio.zfryrgnci.workers.dev</span>
        </div>
      </div>

      <div class="recipient-block">
        <div class="recipient-title">Sayın Kulüp Yöneticileri, Sportif Direktörler ve Teknik Heyet;</div>
        <div class="subject-line">Konu: Futbol Veri Görselleştirme Uzmanı ve AI Mühendisi Görevi İçin Başvuru</div>
      </div>

      <div class="letter-body">
        <p>
          Modern futbolda şampiyonluklar ve sürdürülebilir başarılar, ham verinin sahada aksiyona dönüşebilme hızıyla belirlenmektedir. 2025–2026 sezonunda Polonya Ekstraklasa kulüplerinden Górnik Zabrze bünyesinde Uzaktan/Hibrit Spor Veri Görselleştirme Uzmanı olarak görev yapmış, aynı zamanda Polonya'da (Wrocław ve Varşova) uzun yıllar eğitim almış ve uluslararası teknoloji projelerinde yöneticilik yapmış bir veri uzmanı olarak, bu birikimimi Türkiye Süper Ligi'nin zirve kulüplerine aktarmak amacıyla başvurmaktayım.
        </p>
        <p>
          Górnik Zabrze'deki görev sürecimde; teknik direktör ve maç analizi ekibi için Opta ve Wyscout etkinlik verilerini işleyen özel Python/mplsoccer algoritmaları kurdum. Maç öncesi rakip analizinde pas ağları (passing networks), beklerin ve hücum hattının oluşturduğu Beklenen Tehdit (Expected Threat - xT) ısı haritaları, takımın savunma hattı derinliği ve pres yoğunluğu (PPDA) görselleştirilerek teknik heyetin hazırlık süresi %40 oranında kısaltıldı.
        </p>
        <p>
          Süper Lig kulüplerimizin karşılaştığı en kritik zorluklardan biri, transfer bütçelerini verimli kullanarak yüksek fiziksel ve taktiksel dayanıklılığa sahip oyuncuları değerinin altında keşfetmektir. Geliştirdiğim denetimsiz yapay zeka (K-Means ve PCA) kümeleme modelleri sayesinde, Süper Lig'in yüksek tempolu geçiş oyununa ve pres sistemlerine doğrudan uyum sağlayabilecek Polonya ve Orta/Doğu Avrupa kökenli oyuncuları (örneğin ligin en yüksek savunma ikili mücadele kazanma oranına (%67.4) ve pas ilerletme kalitesine sahip Damian Rasak gibi hedefleri) veri tabanlı olarak tespit edip yönetim kurullarına sundum.
        </p>
        <p>
          Yapay zeka sistemleri, veri bilimi ve üst düzey görsel iletişim alanındaki 12 yılı aşkın tecrübemi; kulübünüzün scouting ağı, teknik analiz birimi ve sportif direktörlüğü ile tam bir sinerji içinde kullanmaya hazırım. Ekte sunduğum 2025–2026 Górnik Zabrze & Polonya Ekstraklasa Veri Portfolyom ve detaylı özgeçmişim, kulübünüze sağlayabileceğim katma değerin somut bir örneğidir.
        </p>
        <p>
          Kulübünüzün hedefleri doğrultusunda detaylı bir teknik sunum yapmak ve veri altyapınızı dünya standartlarına taşımak üzere görüşmeyi sabırsızlıkla beklerim.
        </p>
      </div>

      <div class="signature-block">
        <div style="font-size: 9pt; color: #64748b; margin-bottom: 4px;">Saygılarımla,</div>
        <div class="signature-name">Zafer Yorgancı</div>
        <div class="signature-role">Futbol Veri Görselleştirme Uzmanı & Yapay Zeka Mühendisi</div>
        <div class="signature-role">Górnik Zabrze Veri Uzmanı (2025–2026) | Eski Görsel Yönetmen (Xiaomi CEE & Nordic)</div>
      </div>
    </div>

    <div class="footer">
      <span>Zafer Yorgancı — Başvuru Ön Yazısı | Süper Lig Teknik Heyet ve Sportif Direktörlükleri</span>
      <span>Sayfa 1 / 2 (Türkçe)</span>
    </div>
  </div>

  <!-- ==================== ENGLISH COVER LETTER ==================== -->
  <div class="page">
    <div>
      <div class="header-banner">
        <div class="header-name">ZAFER YORGANCI</div>
        <div class="header-title">FOOTBALL DATA VISUALIZATION SPECIALIST & AI ENGINEER</div>
        <div class="header-meta">
          <span>📍 Istanbul, Türkiye</span>
          <span>✉️ zafer.v2.ai@gmail.com</span>
          <span>📞 +90 501 954 97 27</span>
          <span>🌐 portfolio.zfryrgnci.workers.dev</span>
        </div>
      </div>

      <div class="recipient-block">
        <div class="recipient-title">To the Sporting Director, Head of Recruitment, and Coaching Staff;</div>
        <div class="subject-line">Subject: Application for Football Data Visualization Specialist / AI Analytics Engineer</div>
      </div>

      <div class="letter-body">
        <p>
          In modern elite football, the difference between winning titles and squandering capital lies in the speed at which raw data translates into actionable on-pitch tactical decisions. Having served as a Remote Sports Data Visualization Specialist for Górnik Zabrze during the 2025–2026 Polish Ekstraklasa campaign, and possessing an extensive academic and professional background in Poland (Wrocław and Warsaw) combined with Istanbul residency, I am writing to apply for analytics and visualization specialist roles within Turkish Süper Lig clubs.
        </p>
        <p>
          During my work with Górnik Zabrze, I engineered dedicated Python/mplsoccer analytical pipelines that ingested Opta and Wyscout event streams. For the coaching and performance analysis staff, I designed automated pre-match opposition tactical reports (passing networks, zonal Expected Threat [xT] grids, PPDA defensive territory density) and post-match xG flow trackers, accelerating tactical debrief turnaround by 40% while preserving strict visual clarity.
        </p>
        <p>
          One of the paramount challenges facing Turkish Süper Lig clubs is identifying undervalued, high-tempo, physically resilient talent in Central and Eastern Europe before their transfer valuations escalate. By implementing unsupervised machine learning models (PCA and K-Means clustering), I established automated positional-twin scouting engines that benchmark players against Süper Lig tactical demands—such as uncovering Damian Rasak (leading the league in defensive duel win rate at 67.4% while maintaining 6.82 progressive passes/90) as a prime transfer asset under €2.0M.
        </p>
        <p>
          Combining over 12 years of enterprise creative direction, AI prompt and software engineering, and rigorous football domain expertise, I offer an end-to-end bridge between data science and the technical coaching bench. The attached 2025–2026 Górnik Zabrze & Ekstraklasa Data Visualization Portfolio provides concrete evidence of my execution standards.
        </p>
        <p>
          I would welcome the opportunity to present my analytical workflows and discuss how we can establish a world-class, data-driven visual intelligence department at your club.
        </p>
      </div>

      <div class="signature-block">
        <div style="font-size: 9pt; color: #64748b; margin-bottom: 4px;">Sincerely,</div>
        <div class="signature-name">Zafer Yorgancı</div>
        <div class="signature-role">Football Data Visualization Specialist & AI Engineer</div>
        <div class="signature-role">Former Creative Director | Data Specialist, Górnik Zabrze (2025–2026)</div>
      </div>
    </div>

    <div class="footer">
      <span>Zafer Yorgancı — Cover Letter | Turkish Süper Lig Technical & Scouting Committees</span>
      <span>Page 2 of 2 (English)</span>
    </div>
  </div>

</body>
</html>
"""

# ==============================================================================
# MAIN COMPILATION SCRIPT
# ==============================================================================
def main():
    print("================================================================================")
    print("  COMPILING ALL PDF DELIVERABLES VIA PLAYWRIGHT (HEADLESS CHROMIUM)")
    print("================================================================================")

    with sync_playwright() as p:
        browser = p.chromium.launch()

        # 1. Compile Football CV PDF
        print("\n[1/3] Compiling Zafer_Yorganci_Football_CV.pdf...")
        cv_html = generate_cv_html()
        page = browser.new_page()
        page.set_content(cv_html)
        page.pdf(
            path="Zafer_Yorganci_Football_CV.pdf",
            format="A4",
            print_background=True,
            margin={"top": "0mm", "bottom": "0mm", "left": "0mm", "right": "0mm"}
        )
        page.close()
        print(" -> SUCCESS: Zafer_Yorganci_Football_CV.pdf generated!")

        # 2. Compile Portfolio Dossier PDF
        print("\n[2/3] Compiling Gornik_Zabrze_Ekstraklasa_2025_2026_Portfolio.pdf...")
        portfolio_html = generate_portfolio_html()
        page = browser.new_page()
        page.set_content(portfolio_html)
        page.pdf(
            path="Gornik_Zabrze_Ekstraklasa_2025_2026_Portfolio.pdf",
            format="A4",
            print_background=True,
            margin={"top": "0mm", "bottom": "0mm", "left": "0mm", "right": "0mm"}
        )
        page.close()
        print(" -> SUCCESS: Gornik_Zabrze_Ekstraklasa_2025_2026_Portfolio.pdf generated!")

        # 3. Compile Cover Letter PDF
        print("\n[3/3] Compiling Zafer_Yorganci_Cover_Letter_Super_Lig.pdf...")
        letter_html = generate_cover_letter_html()
        page = browser.new_page()
        page.set_content(letter_html)
        page.pdf(
            path="Zafer_Yorganci_Cover_Letter_Super_Lig.pdf",
            format="A4",
            print_background=True,
            margin={"top": "0mm", "bottom": "0mm", "left": "0mm", "right": "0mm"}
        )
        page.close()
        print(" -> SUCCESS: Zafer_Yorganci_Cover_Letter_Super_Lig.pdf generated!")

        browser.close()

    print("\n================================================================================")
    print("  ALL PDF DELIVERABLES COMPILED FLAWLESSLY WITH CHROMIUM ENGINE!")
    print("================================================================================")

if __name__ == "__main__":
    main()
