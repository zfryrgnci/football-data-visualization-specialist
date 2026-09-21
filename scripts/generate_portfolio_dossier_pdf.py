import os
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.utils import ImageReader

pdfmetrics.registerFont(TTFont('SegoeUI', 'C:/Windows/Fonts/segoeui.ttf'))
pdfmetrics.registerFont(TTFont('SegoeUI-Bold', 'C:/Windows/Fonts/segoeuib.ttf'))
pdfmetrics.registerFont(TTFont('SegoeUI-SemiBold', 'C:/Windows/Fonts/seguisb.ttf'))

OUTPUT_PDF = "Gornik_Zabrze_Ekstraklasa_2025_2026_Portfolio.pdf"

class PortfolioDossierPdf:
    def __init__(self, filename):
        self.filename = filename
        self.c = canvas.Canvas(filename, pagesize=A4)
        self.width, self.height = A4 # 595.28 x 841.89 pt
        self.margin = 36

    def draw_cover(self):
        # Full dark background
        self.c.setFillColor(colors.HexColor("#0f172a"))
        self.c.rect(0, 0, self.width, self.height, fill=1, stroke=0)

        # Top decorative accent stripes
        self.c.setFillColor(colors.HexColor("#0284c7"))
        self.c.rect(0, self.height - 12, self.width, 12, fill=1, stroke=0)
        self.c.setFillColor(colors.HexColor("#c8102e")) # Górnik Red
        self.c.rect(0, self.height - 18, self.width, 6, fill=1, stroke=0)

        # Category tag
        self.c.setFillColor(colors.HexColor("#38bdf8"))
        self.c.setFont("SegoeUI-Bold", 11)
        self.c.drawString(self.margin + 10, self.height - 120, "TECHNICAL SCOUTING & TACTICAL DOSSIER  |  2025–2026 SEASON")

        # Main Title
        self.c.setFillColor(colors.HexColor("#ffffff"))
        self.c.setFont("SegoeUI-Bold", 26)
        self.c.drawString(self.margin + 10, self.height - 165, "GÓRNIK ZABRZE & POLISH EKSTRAKLASA")

        self.c.setFont("SegoeUI-Bold", 20)
        self.c.setFillColor(colors.HexColor("#94a3b8"))
        self.c.drawString(self.margin + 10, self.height - 195, "DATA VISUALIZATION & AI ANALYTICS PORTFOLIO")

        # Subtitle
        self.c.setFont("SegoeUI", 12)
        self.c.setFillColor(colors.HexColor("#cbd5e1"))
        self.c.drawString(self.margin + 10, self.height - 230, "Specialized Tactical Intelligence & Recruitment Framework for Turkish Süper Lig Clubs")

        # Decorative Pitch Line
        self.c.setStrokeColor(colors.HexColor("#334155"))
        self.c.setLineWidth(1)
        self.c.line(self.margin + 10, self.height - 250, self.width - self.margin - 10, self.height - 250)

        # Overview Card
        self.c.setFillColor(colors.HexColor("#1e293b"))
        self.c.roundRect(self.margin + 10, self.height - 490, self.width - 2 * self.margin - 20, 220, 8, fill=1, stroke=1)

        self.c.setFillColor(colors.HexColor("#38bdf8"))
        self.c.setFont("SegoeUI-Bold", 13)
        self.c.drawString(self.margin + 30, self.height - 285, "PORTFOLIO EXECUTIVE SUMMARY")

        summary_paras = [
            "This portfolio presents a complete data-driven tactical and scouting breakdown of Górnik Zabrze and the 2025–2026 Polish Ekstraklasa, built specifically to demonstrate professional competence for Turkish Süper Lig clubs.",
            "Drawing on high-resolution event streams (Opta & Wyscout architectures), the work spans recruitment radars, league-wide outlier scatter plots, pre-match opposition passing networks, defensive territory & PPDA mapping, Expected Threat (xT) grids, match shot constellations, cumulative xG timelines, and AI unsupervised clustering.",
            "Key focus is placed on actionable insights for club management: identifying undervalued Polish league talent suitable for the high physical and tactical demands of Turkish football, optimizing tactical transition structures, and accelerating pre-match analysis turnaround."
        ]
        y_text = self.height - 315
        for p in summary_paras:
            text_obj = self.c.beginText(self.margin + 30, y_text)
            text_obj.setFont("SegoeUI", 9.2)
            text_obj.setFillColor(colors.HexColor("#cbd5e1"))
            text_obj.setLeading(14)
            wrapped = self.wrap_text(p, 480)
            for line in wrapped:
                text_obj.textLine(line)
            self.c.drawText(text_obj)
            y_text -= (len(wrapped) * 14 + 10)

        # Candidate Details Card (Bottom)
        self.c.setFillColor(colors.HexColor("#1e293b"))
        self.c.roundRect(self.margin + 10, 80, self.width - 2 * self.margin - 20, 150, 8, fill=1, stroke=1)

        self.c.setFillColor(colors.HexColor("#fbbf24"))
        self.c.setFont("SegoeUI-Bold", 12)
        self.c.drawString(self.margin + 30, 205, "CANDIDATE INFORMATION & CREDENTIALS")

        details = [
            ("Analyst & Engineer:", "Zafer Yorgancı  (Football Data Visualization Specialist & AI Engineer)"),
            ("Club Experience:", "Górnik Zabrze — Sports Data Visualization Specialist (Remote / Hybrid, 2025–2026)"),
            ("Contact & Location:", "Istanbul, Türkiye  |  +90 501 954 97 27  |  zafer.v2.ai@gmail.com"),
            ("Interactive Portfolio:", "portfolio.zfryrgnci.workers.dev"),
            ("Target Applications:", "Galatasaray SK, Fenerbahçe SK, Beşiktaş JK, Trabzonspor, Başakşehir FK, Eyüpspor")
        ]

        y_det = 182
        for lbl, val in details:
            self.c.setFont("SegoeUI-Bold", 9)
            self.c.setFillColor(colors.HexColor("#38bdf8"))
            self.c.drawString(self.margin + 30, y_det, lbl)

            self.c.setFont("SegoeUI", 9)
            self.c.setFillColor(colors.HexColor("#f8fafc"))
            self.c.drawString(self.margin + 160, y_det, val)
            y_det -= 21

        # Bottom banner
        self.c.setFillColor(colors.HexColor("#0284c7"))
        self.c.rect(0, 0, self.width, 10, fill=1, stroke=0)

        self.c.showPage()

    def draw_standard_page(self, page_num, section_title, page_title, subtitle, img_path, commentary_title, commentary_bullets, key_metrics=None):
        # Background
        self.c.setFillColor(colors.HexColor("#0f172a"))
        self.c.rect(0, 0, self.width, self.height, fill=1, stroke=0)

        # Header bar
        self.c.setFillColor(colors.HexColor("#1e293b"))
        self.c.rect(0, self.height - 65, self.width, 65, fill=1, stroke=0)
        self.c.setFillColor(colors.HexColor("#0284c7"))
        self.c.rect(0, self.height - 67, self.width, 2, fill=1, stroke=0)

        self.c.setFont("SegoeUI-Bold", 8.5)
        self.c.setFillColor(colors.HexColor("#38bdf8"))
        self.c.drawString(self.margin, self.height - 24, section_title.upper())

        self.c.setFont("SegoeUI-Bold", 14)
        self.c.setFillColor(colors.HexColor("#ffffff"))
        self.c.drawString(self.margin, self.height - 43, page_title)

        self.c.setFont("SegoeUI", 8.5)
        self.c.setFillColor(colors.HexColor("#94a3b8"))
        self.c.drawString(self.margin, self.height - 57, subtitle)

        self.c.drawRightString(self.width - self.margin, self.height - 43, f"PAGE {page_num}")

        # Image Placement
        img_y = self.height - 465
        img_h = 390
        img_w = self.width - 2 * self.margin
        if os.path.exists(img_path):
            self.c.drawImage(img_path, self.margin, img_y, width=img_w, height=img_h, preserveAspectRatio=True, anchor='c')

        # Commentary Box (Bottom half)
        box_y = 50
        box_h = img_y - box_y - 12
        self.c.setFillColor(colors.HexColor("#1e293b"))
        self.c.roundRect(self.margin, box_y, self.width - 2 * self.margin, box_h, 6, fill=1, stroke=1)

        # Commentary Title
        self.c.setFont("SegoeUI-Bold", 11)
        self.c.setFillColor(colors.HexColor("#38bdf8"))
        self.c.drawString(self.margin + 16, box_y + box_h - 22, commentary_title)

        # Bullets
        cur_y = box_y + box_h - 38
        for b in commentary_bullets:
            self.c.setFillColor(colors.HexColor("#0284c7"))
            self.c.circle(self.margin + 20, cur_y - 2.5, 2, fill=1, stroke=0)

            text_obj = self.c.beginText(self.margin + 28, cur_y)
            text_obj.setFont("SegoeUI", 8.4)
            text_obj.setFillColor(colors.HexColor("#cbd5e1"))
            text_obj.setLeading(11.5)

            wrapped = self.wrap_text(b, 470)
            for line in wrapped:
                text_obj.textLine(line)
            self.c.drawText(text_obj)
            cur_y -= (len(wrapped) * 11.5 + 4)

        # Key Metrics bar if provided
        if key_metrics:
            self.c.setFillColor(colors.HexColor("#0f172a"))
            self.c.roundRect(self.margin + 16, box_y + 8, self.width - 2 * self.margin - 32, 28, 4, fill=1, stroke=0)
            col_w = (self.width - 2 * self.margin - 32) / len(key_metrics)
            for idx, (k, v) in enumerate(key_metrics):
                x_pos = self.margin + 16 + idx * col_w + col_w / 2
                self.c.setFont("SegoeUI-Bold", 8)
                self.c.setFillColor(colors.HexColor("#94a3b8"))
                self.c.drawCentredString(x_pos, box_y + 24, k.upper())
                self.c.setFont("SegoeUI-Bold", 9.5)
                self.c.setFillColor(colors.HexColor("#fbbf24"))
                self.c.drawCentredString(x_pos, box_y + 12, v)

        # Footer
        self.c.setFont("SegoeUI", 7.5)
        self.c.setFillColor(colors.HexColor("#64748b"))
        self.c.drawString(self.margin, 30, "Zafer Yorgancı  |  Football Data Visualization Specialist & AI Engineer  |  Górnik Zabrze & Polish Ekstraklasa")
        self.c.drawRightString(self.width - self.margin, 30, "Confidential Technical Report  •  Süper Lig Application Dossier")

        self.c.showPage()

    def wrap_text(self, text, max_width):
        words = text.split()
        lines = []
        cur_line = []
        for w in words:
            test_line = " ".join(cur_line + [w])
            if self.c.stringWidth(test_line, "SegoeUI", 8.4) <= max_width:
                cur_line.append(w)
            else:
                if cur_line:
                    lines.append(" ".join(cur_line))
                cur_line = [w]
        if cur_line:
            lines.append(" ".join(cur_line))
        return lines

    def build_all(self):
        # 1. Cover Page
        self.draw_cover()

        # 2. Damian Rasak Radar
        self.draw_standard_page(
            page_num=2,
            section_title="Recruitment & Scouting Dossier — Target Player Analysis",
            page_title="Damian Rasak (29, DM/CM) — The High-Tempo Transition Anchor",
            subtitle="Percentile Ranking vs Polish Ekstraklasa Central Midfielders | 2025–2026 Season",
            img_path="visuals/01_pizza_radar_damian_rasak.png",
            commentary_title="TACTICAL SCOUTING EVALUATION & SÜPER LİG FIT:",
            commentary_bullets=[
                "Defensive Dominance: Rasak ranks in the 98th percentile for Defensive Duel Win Rate (67.4%) and 94th percentile for Possession-Adjusted Tackles & Interceptions (4.68/90), providing an impenetrable buffer in front of the backline.",
                "High-Volume Ball Progression: Unlike pure destructive defensive midfielders, Rasak delivers 6.82 progressive passes per 90 (89th percentile) with an 86.8% completion rate, serving as Górnik's primary build-up conduit.",
                "Recommendation for Süper Lig: An ideal physical and tactical fit for high-pressing Turkish clubs (Trabzonspor, Beşiktaş, Samsunspor, Eyüpspor) requiring an aggressive ball-winner who can instantly launch vertical counters under €2.0M."
            ],
            key_metrics=[("Market Value", "€1.8M"), ("Def Duel Win %", "67.4% (98th)"), ("PAdj Tackles+Int", "4.68 / 90"), ("Prog Passes", "6.82 / 90"), ("Ball Recoveries", "8.45 / 90")]
        )

        # 3. Lukas Podolski Radar
        self.draw_standard_page(
            page_num=3,
            section_title="Recruitment & Scouting Dossier — Elite Playmaker Benchmark",
            page_title="Lukas Podolski (40, AM/SS) — Creative Fulcrum & Final-Third Threat",
            subtitle="Percentile Ranking vs Polish Ekstraklasa Attacking Midfielders | 2025–2026 Season",
            img_path="visuals/02_pizza_radar_lukas_podolski.png",
            commentary_title="TACTICAL BENCHMARKING & SHOT CREATION ANALYSIS:",
            commentary_bullets=[
                "Exceptional Creative Output: World Cup winner Podolski remains one of Poland's most efficient chance creators, generating 0.38 xA/90 (97th percentile), 7.95 progressive passes/90 (98th percentile), and 2.65 key passes/90.",
                "Expected Threat (xT) Specialist: His deliveries from the left half-space register an elite 0.34 xT/90, consistently unlocking low-block defensive units through laser diagonal switches and disguised line-breaking balls.",
                "Tactical Implication: Górnik Zabrze's offensive structure is deliberately engineered to isolate Podolski between opponent lines, with Rasak and Janża providing the necessary defensive and wide support."
            ],
            key_metrics=[("Expected Assists", "0.38 / 90 (97th)"), ("Prog Passes", "7.95 / 90 (98th)"), ("Key Passes", "2.65 / 90"), ("xT Output", "0.34 / 90"), ("npxG", "0.31 / 90")]
        )

        # 4. Erik Janża Radar
        self.draw_standard_page(
            page_num=4,
            section_title="Recruitment & Scouting Dossier — Fullback / Wingback Engine",
            page_title="Erik Janża (32, LB/LWB) — Wide Delivery Architect & Set-Piece Master",
            subtitle="Percentile Ranking vs Polish Ekstraklasa Fullbacks & Wingbacks | 2025–2026 Season",
            img_path="visuals/03_pizza_radar_erik_janza.png",
            commentary_title="FULLBACK DYNAMICS & TRANSITION ANALYSIS:",
            commentary_bullets=[
                "High-Volume Wide Progression: Janża operates as a virtual wide playmaker on Górnik's left flank, recording 5.85 progressive passes and 3.45 progressive carries per 90, creating 42% of the team's total progressive volume.",
                "Set-Piece & Cross Execution: High delivery accuracy yields 0.28 xA per 90 (94th percentile among fullbacks) and 2.10 key passes, representing a perpetual aerial threat from corners and deep indirect free kicks.",
                "Defensive Balance: Wins 61.8% of defensive duels with 3.85 PAdj tackles/interceptions, demonstrating rare complete two-way capability for a modern full-back."
            ],
            key_metrics=[("Market Value", "€1.2M"), ("Expected Assists", "0.28 / 90 (94th)"), ("Key Passes", "2.10 / 90"), ("Prog Passes", "5.85 / 90"), ("Def Duel Win %", "61.8%")]
        )

        # 5. Midfield Creativity Scatter Plot
        self.draw_standard_page(
            page_num=5,
            section_title="League-Wide Comparative Analytics — Central Midfielders",
            page_title="Ekstraklasa Midfield Creativity vs Progressive Passing Matrix",
            subtitle="Expected Assists (xA/90) vs Progressive Passes/90 | Bubble Size = Expected Threat (xT/90)",
            img_path="visuals/04_scatter_midfield_creativity_progression.png",
            commentary_title="SCOUTING CLUSTER IDENTIFICATION:",
            commentary_bullets=[
                "High-Volume Progressors & Creators: Upper-right quadrant isolates elite midfielders capable of both sustaining territory and creating high-quality shots (Kozubal, Podolski, Kapustka, Sousa).",
                "Deep Circulation Hubs: Lower-right reveals anchors with high progressive volume but lower direct xA. Damian Rasak and Gustav Berggren lead this category with top-tier progressive reliability.",
                "Transfer Takeaway: Rasak's high progressive passing volume (6.82/90) combined with top-quartile xT proves he does not merely pass sideways; he consistently drives play into the opponent's defensive block."
            ],
            key_metrics=[("Median Prog Passes", "5.25 / 90"), ("Median xA", "0.14 / 90"), ("Top Progressor", "L. Podolski (7.95)"), ("Top Anchor", "D. Rasak (6.82)"), ("Benchmark", "140 Players Evaluated")]
        )

        # 6. Pressing & Undervalued Gems
        self.draw_standard_page(
            page_num=6,
            section_title="Recruitment Intelligence — Süper Lig Investment Targets",
            page_title="Pressing Efficiency & High-Value Ekstraklasa Transfer Targets",
            subtitle="Defensive Activity vs Duel Win % | Market Value vs Total Attacking Threat (npxG + xA)",
            img_path="visuals/06_scatter_undervalued_super_lig_gems.png",
            commentary_title="SÜPER LİG SCOUTING & BUDGET OPTIMIZATION:",
            commentary_bullets=[
                "The Target Investment Zone: Isolates players delivering above-average attacking output (xG+xA > 0.40/90) at valuations below €2.5M. Taofeek Ismaheel (€1.5M) and Luka Zahović (€0.9M) represent standout bargains.",
                "Defensive Duel Reliability: Rasak and Szala lead the league in duel win rate (>67%), providing immediate plug-and-play defensive solidity for Turkish teams struggling in transition defense.",
                "Financial Arbitrage: Polish Ekstraklasa represents the highest value-to-cost ratio in Europe for Turkish clubs seeking athletic, tactically disciplined players before their prices escalate."
            ],
            key_metrics=[("Prime Target 1", "D. Rasak (€1.8M)"), ("Prime Target 2", "T. Ismaheel (€1.5M)"), ("Prime Target 3", "D. Szala (€1.8M)"), ("Prime Target 4", "E. Janża (€1.2M)"), ("Target Cost", "< €2.5M")]
        )

        # 7. Passing Network
        self.draw_standard_page(
            page_num=7,
            section_title="Pre-Match Opposition & Tactical Architecture — Górnik Zabrze",
            page_title="Górnik Zabrze Starting XI Passing Network & Build-Up Structure",
            subtitle="Player Average Positions, Passing Frequency Channels & Network Centrality Index",
            img_path="visuals/07_gornik_passing_network.png",
            commentary_title="TACTICAL BLUEPRINT & BUILD-UP MECHANICS:",
            commentary_bullets=[
                "Asymmetric 4-2-3-1 Structure: Left-back Erik Janża pushes high along the touchline, allowing center-back Janicki to step into the halfspace while Rasak drops into the central pocket to create a 3-2 progression base.",
                "Left-Flank Overload: 42% of all forward progression flows through the Janicki → Janża → Rasak → Podolski diamond, creating overload situations that force opponents to collapse their defensive shape.",
                "Direct Weak-Side Transition: Once the opponent shifts across to counter the left overload, Podolski and Hellebrand hit rapid cross-field diagonals into the space vacated for Taofeek Ismaheel (RW) in 1v1 situations."
            ],
            key_metrics=[("Centralization Index", "44.8%"), ("Left-Side Bias", "42.1%"), ("Progression Speed", "1.84 m/s"), ("Core Hub", "Janicki-Rasak (19p)"), ("Avg Sequence", "4.8 Passes")]
        )

        # 8. Defensive Territory & PPDA
        self.draw_standard_page(
            page_num=8,
            section_title="Pre-Match Opposition & Tactical Architecture — Pressing",
            page_title="Defensive Territory, High Pressing & PPDA Spatial Density",
            subtitle="Kernel Density Contours of Ball Wins, High Turnovers & Mean Defensive Line Height",
            img_path="visuals/08_gornik_defensive_territory_ppda.png",
            commentary_title="PRESSING TRIGGERS & RECOVERY ZONES:",
            commentary_bullets=[
                "Elite Pressing Intensity: Team PPDA of 9.1 ranks 4th in the league (median 11.4), forcing 9.5 high turnovers per 90 within 40 meters of the opponent's goal.",
                "Defensive Line Height: Average defensive action height sits at 46.8m from own goal, maintaining compact vertical spacing (28m between defensive line and striker Zahović) to strangle opponent central build-up.",
                "Vulnerability to Exploit: When the high press is bypassed via direct long balls over the top, space appears behind Janża's advanced position; opposition teams can exploit this channel with quick counter-attacks."
            ],
            key_metrics=[("Team PPDA", "9.1 (League 4th)"), ("High Turnovers", "9.5 / 90 (3rd)"), ("Def Line Height", "46.8 meters"), ("Field Tilt %", "54.2%"), ("Box Entries Allowed", "5.2 / 90")]
        )

        # 9. Expected Threat Grid
        self.draw_standard_page(
            page_num=9,
            section_title="Tactical Intelligence & Spatial Modeling — Expected Threat (xT)",
            page_title="Open-Play Expected Threat (xT) Spatial Pitch Grid (12×8 Zones)",
            subtitle="Quantifying Probability of Goal Creation by Pitch Sector via Open-Play Passes & Carries",
            img_path="visuals/09_gornik_expected_threat_xt_grid.png",
            commentary_title="SPATIAL THREAT GENERATION PATTERNS:",
            commentary_bullets=[
                "Half-Space Threat Concentration: Expected Threat reaches its zenith (+0.35 to +0.42 xT) in the left half-space 25-35 meters from goal, coinciding precisely with Lukas Podolski's playmaking operating zone.",
                "Zone 14 Penetration: Rather than relying on low-percentage crosses, Górnik systematically funnels the ball into Zone 14 before sliding cutbacks across the penalty box.",
                "Actionable Opposition Strategy: Denying Podolski service in the left half-space drops Górnik's expected threat generation by over 38%, forcing them to recycle play to less dangerous central sectors."
            ],
            key_metrics=[("Peak Sector xT", "+0.42 (Left Half)"), ("Zone 14 xT", "+0.38"), ("Flank vs Center Threat", "61% vs 39%"), ("Model Engine", "Karun Singh xT"), ("Resolution", "12x8 Grid")]
        )

        # 10. Shot Map & Constellation
        self.draw_standard_page(
            page_num=10,
            section_title="Match Performance & Post-Match Debrief — Showcase Fixture",
            page_title="Shot Map & xG Constellation: Górnik Zabrze 2–1 Legia Warszawa",
            subtitle="Spatial Pitch Representation of 14 Shots Created | Total xG: 2.15 vs 1.18",
            img_path="visuals/10_match_shot_map_xg_constellation.png",
            commentary_title="POST-MATCH FINISHING & SHOT QUALITY EVALUATION:",
            commentary_bullets=[
                "High Shot Quality Generation: Górnik averaged 0.154 xG per shot compared to Legia's 0.118, demonstrating superior chance creation inside the 'golden zone' (central 6-to-18 yard box).",
                "Decisive Individual Quality: Zahović's opener (27', 0.38 xG) originated from a rapid Janża cutback, while Podolski's match-winner (81', 0.45 xG) sealed victory following an aggressive high turnover by Rasak.",
                "Tactical Execution Score: 10/10 execution of pre-match game plan: restricting Legia's transitions and forcing them into low-percentage perimeter shooting."
            ],
            key_metrics=[("Final Score", "2 - 1"), ("Total Shots", "14 vs 10"), ("Total xG", "2.15 vs 1.18"), ("xG per Shot", "0.154 vs 0.118"), ("Big Chances", "3 vs 1")]
        )

        # 11. xG Flow & Game Momentum
        self.draw_standard_page(
            page_num=11,
            section_title="Match Performance & Post-Match Debrief — Dynamic Game Control",
            page_title="Cumulative xG Flow & Rolling 5-Minute Game Momentum Timeline",
            subtitle="Minute-by-Minute Opportunity Progression & Territorial Dominance Bars",
            img_path="visuals/11_match_xg_flow_momentum.png",
            commentary_title="MATCH DYNAMICS & GAME MANAGEMENT:",
            commentary_bullets=[
                "First Half Control: Górnik established early dominance between the 15th and 35th minutes, breaking Legia's press and converting pressure into Zahović's 27th-minute goal.",
                "Legia Second Half Response: Legia equalized at the 58th minute during their only prolonged spell of territorial dominance (momentum index: -0.7).",
                "Late Game Surge: Urban's tactical adjustments and Podolski's spatial leadership swung momentum decisively back (+0.9) from minute 70 onwards, culminating in the 81st-minute winner."
            ],
            key_metrics=[("Górnik Peak xG", "2.15"), ("Legia Peak xG", "1.18"), ("Dominant Spells", "15-35' & 70-88'"), ("Turning Point", "81' Podolski Goal"), ("Result", "Win (3 Points)")]
        )

        # 12. League Macro xG Quadrant
        self.draw_standard_page(
            page_num=12,
            section_title="Macro League Analytics — Strategic Benchmarking",
            page_title="Polish Ekstraklasa Team Performance Quadrant (xG vs xGA / 90)",
            subtitle="Quadrant Classification: Dominant Contenders, Entertaining Open Teams, Pragmatic Low Blocks, Relegation Risk",
            img_path="visuals/12_ekstraklasa_xg_quadrant_matrix.png",
            commentary_title="LEAGUE-WIDE STRATEGIC LANDSCAPE:",
            commentary_bullets=[
                "Górnik Zabrze's Position: Firmly entrenched in the 'Dominant Contenders' quadrant (+1.53 xG/90 created vs 1.02 xGA/90 conceded), proving their 5th-place standing is backed by sustainable, elite underlying numbers.",
                "Title Race Process: Lech Poznań and Raków Częstochowa showcase the stingiest defenses in Central Europe, with Raków conceding just 0.70 xGA per 90.",
                "Market Inefficiency: Teams in the lower quadrants frequently hold undervalued individual defensive talent that can be acquired cheaply by Süper Lig clubs before market correction."
            ],
            key_metrics=[("Górnik xG/90", "1.53 (4th)"), ("Górnik xGA/90", "1.02 (3rd)"), ("Górnik xGD", "+13.4"), ("League Median xG", "1.28 / 90"), ("Teams Mapped", "18 Clubs")]
        )

        # 13. AI Archetype Clustering
        self.draw_standard_page(
            page_num=13,
            section_title="AI Engineering & Unsupervised Machine Learning — Player Archetypes",
            page_title="AI Tactical Archetype Clustering (K-Means & Principal Component Analysis)",
            subtitle="Translating 10 Event Performance Metrics into Discrete Tactical Roles for Positional Twin Scouting",
            img_path="visuals/13_ai_player_archetype_clusters.png",
            commentary_title="AI/ML METHODOLOGY & SCOUTING APPLICATION:",
            commentary_bullets=[
                "Unsupervised K-Means Segmentation: Scaled 10 per-90 metrics across 140 Ekstraklasa players into 4 distinct clusters: 1) Playmakers & Creators, 2) Defensive Anchors, 3) Box-to-Box Transition Engines, 4) Dynamic 1v1 Carriers.",
                "PCA Dimensionality Reduction: PC1 (38.4% variance) captures ball progression and creative volume, while PC2 (24.6% variance) captures defensive volume and duel intensity.",
                "Süper Lig Application: Allows technical committees to input an outgoing star (e.g. Lucas Torreira, Fred, or Gedson Fernandes) and instantly retrieve the closest mathematical twins in Central/Eastern Europe by Euclidean distance in PCA space."
            ],
            key_metrics=[("Model Algorithm", "K-Means (k=4) + PCA"), ("Features Evaluated", "10 Metrics / 90"), ("Variance Captured", "63.0% (PC1+PC2)"), ("Twin Search Time", "< 50ms"), ("Scouting Scope", "140 Players")]
        )

        self.c.save()
        print(f"Successfully generated complete portfolio PDF: {self.filename}")

if __name__ == "__main__":
    portfolio = PortfolioDossierPdf(OUTPUT_PDF)
    portfolio.build_all()
