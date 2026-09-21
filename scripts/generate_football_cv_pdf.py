import os
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

# Register Segoe UI fonts
pdfmetrics.registerFont(TTFont('SegoeUI', 'C:/Windows/Fonts/segoeui.ttf'))
pdfmetrics.registerFont(TTFont('SegoeUI-Bold', 'C:/Windows/Fonts/segoeuib.ttf'))
pdfmetrics.registerFont(TTFont('SegoeUI-SemiBold', 'C:/Windows/Fonts/seguisb.ttf'))

OUTPUT_PATH = "Zafer_Yorganci_Football_CV.pdf"

class FootballCVPdf:
    def __init__(self, filename):
        self.filename = filename
        self.c = canvas.Canvas(filename, pagesize=A4)
        self.width, self.height = A4 # 595.27 x 841.89 pt
        self.margin = 36 # 0.5 inch margins

    def draw_header(self, page_num):
        # Top banner background
        self.c.setFillColor(colors.HexColor("#0f172a")) # Slate 900
        self.c.rect(0, self.height - 105, self.width, 105, fill=1, stroke=0)

        # Subtle accent stripe (Górnik blue & gold)
        self.c.setFillColor(colors.HexColor("#0284c7"))
        self.c.rect(0, self.height - 108, self.width, 3, fill=1, stroke=0)

        # Name & Title
        self.c.setFillColor(colors.HexColor("#ffffff"))
        self.c.setFont("SegoeUI-Bold", 22)
        self.c.drawString(self.margin, self.height - 40, "ZAFER YORGANCI")

        self.c.setFillColor(colors.HexColor("#38bdf8")) # Sky blue accent
        self.c.setFont("SegoeUI-SemiBold", 12)
        self.c.drawString(self.margin, self.height - 58, "FOOTBALL DATA VISUALIZATION SPECIALIST & AI ENGINEER")

        self.c.setFillColor(colors.HexColor("#94a3b8")) # Slate 400
        self.c.setFont("SegoeUI", 9)
        contact_line = "Istanbul, Türkiye  •  zafer.v2.ai@gmail.com  •  +90 501 954 97 27  •  portfolio.zfryrgnci.workers.dev"
        self.c.drawString(self.margin, self.height - 76, contact_line)

        target_line = "Target Role: Sports Data Visualization Specialist / Technical Analyst  |  Polish Ekstraklasa & Süper Lig Scope"
        self.c.setFont("SegoeUI-SemiBold", 8.5)
        self.c.setFillColor(colors.HexColor("#fbbf24")) # Amber
        self.c.drawString(self.margin, self.height - 92, target_line)

        # Page number on header right
        self.c.setFont("SegoeUI", 8.5)
        self.c.setFillColor(colors.HexColor("#64748b"))
        self.c.drawRightString(self.width - self.margin, self.height - 35, f"PAGE {page_num} OF 2")

    def draw_footer(self, page_num):
        self.c.setStrokeColor(colors.HexColor("#cbd5e1"))
        self.c.setLineWidth(0.5)
        self.c.line(self.margin, 30, self.width - self.margin, 30)

        self.c.setFont("SegoeUI", 8)
        self.c.setFillColor(colors.HexColor("#64748b"))
        self.c.drawString(self.margin, 18, "Zafer Yorgancı  —  Curriculum Vitae  |  Football Data Visualization Specialist & AI Engineer")
        self.c.drawRightString(self.width - self.margin, 18, f"portfolio.zfryrgnci.workers.dev  •  Page {page_num} of 2")

    def section_title(self, y, title):
        self.c.setFillColor(colors.HexColor("#0f172a"))
        self.c.setFont("SegoeUI-Bold", 11)
        self.c.drawString(self.margin, y, title.upper())

        # Underline bar
        self.c.setFillColor(colors.HexColor("#0284c7"))
        self.c.rect(self.margin, y - 4, 38, 2, fill=1, stroke=0)
        self.c.setFillColor(colors.HexColor("#e2e8f0"))
        self.c.rect(self.margin + 40, y - 3, self.width - 2 * self.margin - 40, 0.6, fill=1, stroke=0)
        return y - 18

    def draw_page_1(self):
        self.draw_header(1)
        y = self.height - 128

        # --- EXECUTIVE PROFILE ---
        y = self.section_title(y, "Executive Profile")
        self.c.setFont("SegoeUI", 8.8)
        self.c.setFillColor(colors.HexColor("#1e293b"))
        summary = (
            "Specialized Football Data Visualization Specialist and AI Engineer uniting on-pitch match event intelligence "
            "(Opta, StatsBomb, Wyscout) with elite visual design and computational models. Proven club experience delivering actionable "
            "pre-match tactical dossiers, recruitment dashboards, and post-match debriefs for coaching staffs and sporting directors. "
            "Leverages Python (mplsoccer, Scikit-learn, PyTorch), full-stack web architectures, and unsupervised machine learning to translate "
            "complex tracking and event data into decisive tactical advantages. Bilingual background (lived and educated in Poland; "
            "native Turkish speaker based in Istanbul) ideally positioned for Turkish Süper Lig clubs scouting high-tempo Central & Eastern European talent."
        )
        text_obj = self.c.beginText(self.margin, y)
        text_obj.setFont("SegoeUI", 8.8)
        text_obj.setLeading(12.5)
        for line in self.wrap_text(summary, 520):
            text_obj.textLine(line)
        self.c.drawText(text_obj)
        y -= 62

        # --- FOOTBALL ANALYTICS & DATA EXPERIENCE ---
        y = self.section_title(y, "Football Analytics & Professional Experience")

        # ROLE 1: Górnik Zabrze
        self.c.setFont("SegoeUI-Bold", 10.5)
        self.c.setFillColor(colors.HexColor("#0f172a"))
        self.c.drawString(self.margin, y, "Górnik Zabrze")
        self.c.setFont("SegoeUI-SemiBold", 9.5)
        self.c.setFillColor(colors.HexColor("#0284c7"))
        self.c.drawString(self.margin + 90, y, "|  Sports Data Visualization Specialist (Remote / Hybrid)")
        self.c.setFont("SegoeUI-Bold", 9)
        self.c.setFillColor(colors.HexColor("#475569"))
        self.c.drawRightString(self.width - self.margin, y, "2025 – 2026 Season")
        y -= 14

        bullets_gornik = [
            "Engineered end-to-end Python tactical visualization pipelines using mplsoccer, matplotlib, and Opta/Wyscout event data, delivering pre-match opposition reports and post-match debriefs for technical coaching and video analysis staff.",
            "Architected automated Passing Network models, Expected Threat (xT) spatial density pitch grids (12x8 zones), and PPDA defensive territory heatmaps to pinpoint opponent transition vulnerabilities and pressing triggers.",
            "Constructed Recruitment & Scouting analytical suites with Percentile Pizza Radars and multi-metric outlier scatter plots, establishing benchmark profiles for key assets (Damian Rasak, Lukas Podolski, Erik Janża) and transfer targets.",
            "Deployed unsupervised Machine Learning models (K-Means & PCA clustering) across 140+ Ekstraklasa outfield players to identify tactical twins and simulate squad replacement options for recruitment directors under budget caps.",
            "Accelerated coaching staff match preparation by 40% through standardized, high-contrast visual templates translating raw event streams into intuitive tactical takeaways."
        ]
        y = self.draw_bullets(y, bullets_gornik)
        y -= 6

        # ROLE 2: Xiaomi
        self.c.setFont("SegoeUI-Bold", 10)
        self.c.setFillColor(colors.HexColor("#0f172a"))
        self.c.drawString(self.margin, y, "Xiaomi Technology")
        self.c.setFont("SegoeUI-SemiBold", 9)
        self.c.setFillColor(colors.HexColor("#0284c7"))
        self.c.drawString(self.margin + 115, y, "|  Creative Director — CEE & Nordic Markets")
        self.c.setFont("SegoeUI-Bold", 9)
        self.c.setFillColor(colors.HexColor("#475569"))
        self.c.drawRightString(self.width - self.margin, y, "Warsaw, Poland  |  2024 – 2025")
        y -= 14

        bullets_xiaomi = [
            "Directed high-velocity visual campaigns and brand design architectures across Central & Eastern Europe and the Nordic region.",
            "Integrated modern AI-assisted workflows, prompt engineering frameworks, and automated asset generation pipelines.",
            "Managed cross-functional international teams, external agencies, and technical partners under tight deadlines."
        ]
        y = self.draw_bullets(y, bullets_xiaomi)
        y -= 6

        # ROLE 3: AON
        self.c.setFont("SegoeUI-Bold", 10)
        self.c.setFillColor(colors.HexColor("#0f172a"))
        self.c.drawString(self.margin, y, "AON")
        self.c.setFont("SegoeUI-SemiBold", 9)
        self.c.setFillColor(colors.HexColor("#0284c7"))
        self.c.drawString(self.margin + 35, y, "|  Creative Design Associate")
        self.c.setFont("SegoeUI-Bold", 9)
        self.c.setFillColor(colors.HexColor("#475569"))
        self.c.drawRightString(self.width - self.margin, y, "Krakow, Poland  |  2023 – 2024")
        y -= 14

        bullets_aon = [
            "Delivered executive-level reporting collateral, visual communication systems, and brand assets for global enterprise stakeholders.",
            "Implemented AI-powered data processing and automated visual concepting pipelines to enhance departmental throughput."
        ]
        y = self.draw_bullets(y, bullets_aon)
        y -= 6

        # ROLE 4: Cognizant (Google Marketing Products)
        self.c.setFont("SegoeUI-Bold", 10)
        self.c.setFillColor(colors.HexColor("#0f172a"))
        self.c.drawString(self.margin, y, "Cognizant Technology Solutions")
        self.c.setFont("SegoeUI-SemiBold", 9)
        self.c.setFillColor(colors.HexColor("#0284c7"))
        self.c.drawString(self.margin + 165, y, "|  Senior Process Executive (Google Vendor)")
        self.c.setFont("SegoeUI-Bold", 9)
        self.c.setFillColor(colors.HexColor("#475569"))
        self.c.drawRightString(self.width - self.margin, y, "Krakow, Poland  |  2022 – 2023")
        y -= 14

        bullets_cognizant = [
            "Coordinated digital analytics operations, Google Analytics, Ads, and performance reporting for international Google accounts.",
            "Designed executive dashboards and automated report generation systems to ensure high data integrity and rapid delivery."
        ]
        y = self.draw_bullets(y, bullets_cognizant)

        self.draw_footer(1)
        self.c.showPage()

    def draw_page_2(self):
        self.draw_header(2)
        y = self.height - 128

        # --- ADDITIONAL EXPERIENCE ---
        y = self.section_title(y, "Additional Experience & Technical Leadership")

        # Genpact
        self.c.setFont("SegoeUI-Bold", 10)
        self.c.setFillColor(colors.HexColor("#0f172a"))
        self.c.drawString(self.margin, y, "Genpact — Google Vendor Office")
        self.c.setFont("SegoeUI-SemiBold", 9)
        self.c.setFillColor(colors.HexColor("#0284c7"))
        self.c.drawString(self.margin + 175, y, "|  AI Data Labelling & Content Specialist")
        self.c.setFont("SegoeUI-Bold", 9)
        self.c.setFillColor(colors.HexColor("#475569"))
        self.c.drawRightString(self.width - self.margin, y, "Krakow, Poland  |  2021 – 2022")
        y -= 14
        bullets_genpact = [
            "Classified and audited large-scale structured multimodal datasets to support machine learning models under strict quality benchmarks."
        ]
        y = self.draw_bullets(y, bullets_genpact)
        y -= 6

        # Struktur.agency
        self.c.setFont("SegoeUI-Bold", 10)
        self.c.setFillColor(colors.HexColor("#0f172a"))
        self.c.drawString(self.margin, y, "Struktur.agency")
        self.c.setFont("SegoeUI-SemiBold", 9)
        self.c.setFillColor(colors.HexColor("#0284c7"))
        self.c.drawString(self.margin + 90, y, "|  Founder & Creative Technologist")
        self.c.setFont("SegoeUI-Bold", 9)
        self.c.setFillColor(colors.HexColor("#475569"))
        self.c.drawRightString(self.width - self.margin, y, "Remote  |  2018 – Present")
        y -= 14
        bullets_struktur = [
            "Architected interactive WebGL experiences, computational shaders, 3D visualization, and automated Adobe ExtendScript tooling."
        ]
        y = self.draw_bullets(y, bullets_struktur)
        y -= 10

        # --- TECHNICAL TOOLKIT & FOOTBALL ANALYTICS DOMAINS ---
        y = self.section_title(y, "Football Analytics & AI Engineering Core Skills")

        skills = [
            ("Football Event Models:", "Expected Goals (xG), Expected Threat (xT - Karun Singh model), Passes Allowed Per Defensive Action (PPDA), Field Tilt %, Passing Networks, Pitch Control, Shot Constellations, Directional Pass Sonars."),
            ("Data & Coding Stack:", "Python (mplsoccer, matplotlib, seaborn, pandas, numpy, scipy, scikit-learn, joblib), SQL, JupyterLab, REST APIs, JSON event stream parsing."),
            ("AI & Machine Learning:", "Unsupervised clustering (K-Means), Dimensionality Reduction (PCA), predictive feature engineering, similarity engines (cosine/Euclidean for player replacements), prompt engineering (Claude, GPT-4, Gemini)."),
            ("Frontend & Web Visuals:", "HTML5, CSS3, JavaScript (ES6+), React, Vite, TypeScript, Tailwind CSS, WebGL, Canvas, Chart.js, interactive dashboards."),
            ("Design & Presentation:", "Adobe Creative Suite (Photoshop, Illustrator, InDesign, Premiere Pro), Figma, typography standards, high-contrast dark-mode presentation palettes, executive reporting.")
        ]

        for category, desc in skills:
            self.c.setFont("SegoeUI-Bold", 9)
            self.c.setFillColor(colors.HexColor("#0284c7"))
            self.c.drawString(self.margin, y, category)

            self.c.setFont("SegoeUI", 8.8)
            self.c.setFillColor(colors.HexColor("#1e293b"))
            text_obj = self.c.beginText(self.margin + 125, y)
            text_obj.setFont("SegoeUI", 8.8)
            text_obj.setLeading(11.5)
            for line in self.wrap_text(desc, 395):
                text_obj.textLine(line)
            self.c.drawText(text_obj)
            lines_count = len(self.wrap_text(desc, 395))
            y -= (lines_count * 11.5 + 4)

        y -= 6

        # --- EDUCATION & ACADEMIC BACKGROUND ---
        y = self.section_title(y, "Education & Credentials")

        self.c.setFont("SegoeUI-Bold", 9.5)
        self.c.setFillColor(colors.HexColor("#0f172a"))
        self.c.drawString(self.margin, y, "DSW Ideis University (Dolnośląska Szkoła Wyższa)")
        self.c.setFont("SegoeUI", 9)
        self.c.setFillColor(colors.HexColor("#475569"))
        self.c.drawRightString(self.width - self.margin, y, "Wrocław, Poland  |  2017 – 2021")
        y -= 12
        self.c.setFont("SegoeUI-SemiBold", 8.8)
        self.c.setFillColor(colors.HexColor("#0284c7"))
        self.c.drawString(self.margin, y, "Bachelor of Arts (B.A.) in Creative Media — 3D Animation & Visual Effects")
        y -= 16

        self.c.setFont("SegoeUI-Bold", 9.5)
        self.c.setFillColor(colors.HexColor("#0f172a"))
        self.c.drawString(self.margin, y, "FH Oberösterreich (University of Applied Sciences Upper Austria)")
        self.c.setFont("SegoeUI", 9)
        self.c.setFillColor(colors.HexColor("#475569"))
        self.c.drawRightString(self.width - self.margin, y, "Hagenberg, Austria  |  2018 – 2019")
        y -= 12
        self.c.setFont("SegoeUI-SemiBold", 8.8)
        self.c.setFillColor(colors.HexColor("#0284c7"))
        self.c.drawString(self.margin, y, "Digital Communication & Multimedia — International Academic Exchange")
        y -= 20

        # --- LANGUAGES & CLUB SCOUTING COVERAGE ---
        y = self.section_title(y, "Languages & Regional Scouting Coverage")

        self.c.setFont("SegoeUI", 8.8)
        self.c.setFillColor(colors.HexColor("#1e293b"))
        lang_text = (
            "• Turkish: Native  |  English: C1 Fluent (Full Professional Proficiency)  |  German: B1  |  Polish: Professional Working Familiarity\n"
            "• Strategic Advantage for Süper Lig: In-depth familiarity with Central/Eastern European leagues (Poland Ekstraklasa, Czech First League, "
            "Austria Bundesliga) enabling seamless domestic data integration, high-value scouting pipelines, and technical staff communication."
        )
        text_obj = self.c.beginText(self.margin, y)
        text_obj.setFont("SegoeUI", 8.8)
        text_obj.setLeading(12)
        for line in lang_text.split("\n"):
            for subline in self.wrap_text(line, 520):
                text_obj.textLine(subline)
        self.c.drawText(text_obj)

        self.draw_footer(2)
        self.c.showPage()

    def draw_bullets(self, y, bullets):
        for b in bullets:
            self.c.setFillColor(colors.HexColor("#0284c7"))
            self.c.circle(self.margin + 4, y - 3, 1.8, fill=1, stroke=0)

            self.c.setFont("SegoeUI", 8.6)
            self.c.setFillColor(colors.HexColor("#334155"))
            text_obj = self.c.beginText(self.margin + 12, y)
            text_obj.setFont("SegoeUI", 8.6)
            text_obj.setLeading(11.5)

            wrapped = self.wrap_text(b, 508)
            for line in wrapped:
                text_obj.textLine(line)
            self.c.drawText(text_obj)
            y -= (len(wrapped) * 11.5 + 3.5)
        return y

    def wrap_text(self, text, max_width):
        words = text.split()
        lines = []
        cur_line = []
        for w in words:
            test_line = " ".join(cur_line + [w])
            if self.c.stringWidth(test_line, "SegoeUI", 8.8) <= max_width:
                cur_line.append(w)
            else:
                if cur_line:
                    lines.append(" ".join(cur_line))
                cur_line = [w]
        if cur_line:
            lines.append(" ".join(cur_line))
        return lines

    def build(self):
        self.draw_page_1()
        self.draw_page_2()
        self.c.save()
        print(f"Successfully generated {self.filename}")

if __name__ == "__main__":
    cv = FootballCVPdf(OUTPUT_PATH)
    cv.build()
