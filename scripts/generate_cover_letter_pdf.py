import os
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

pdfmetrics.registerFont(TTFont('SegoeUI', 'C:/Windows/Fonts/segoeui.ttf'))
pdfmetrics.registerFont(TTFont('SegoeUI-Bold', 'C:/Windows/Fonts/segoeuib.ttf'))
pdfmetrics.registerFont(TTFont('SegoeUI-SemiBold', 'C:/Windows/Fonts/seguisb.ttf'))

OUTPUT_PATH = "Zafer_Yorganci_Cover_Letter_Super_Lig.pdf"

class CoverLetterPdf:
    def __init__(self, filename):
        self.filename = filename
        self.c = canvas.Canvas(filename, pagesize=A4)
        self.width, self.height = A4
        self.margin = 40

    def draw_header(self, title_lang, target_lang):
        # Header banner
        self.c.setFillColor(colors.HexColor("#0f172a"))
        self.c.rect(0, self.height - 95, self.width, 95, fill=1, stroke=0)
        self.c.setFillColor(colors.HexColor("#0284c7"))
        self.c.rect(0, self.height - 98, self.width, 3, fill=1, stroke=0)

        self.c.setFillColor(colors.HexColor("#ffffff"))
        self.c.setFont("SegoeUI-Bold", 18)
        self.c.drawString(self.margin, self.height - 35, "ZAFER YORGANCI")

        self.c.setFillColor(colors.HexColor("#38bdf8"))
        self.c.setFont("SegoeUI-SemiBold", 10.5)
        self.c.drawString(self.margin, self.height - 52, "FOOTBALL DATA VISUALIZATION SPECIALIST & AI ENGINEER")

        self.c.setFillColor(colors.HexColor("#94a3b8"))
        self.c.setFont("SegoeUI", 8.5)
        self.c.drawString(self.margin, self.height - 68, "Istanbul, Türkiye  •  zafer.v2.ai@gmail.com  •  +90 501 954 97 27  •  portfolio.zfryrgnci.workers.dev")

        self.c.setFillColor(colors.HexColor("#fbbf24"))
        self.c.setFont("SegoeUI-SemiBold", 8.5)
        self.c.drawRightString(self.width - self.margin, self.height - 35, target_lang)
        self.c.setFillColor(colors.HexColor("#94a3b8"))
        self.c.drawRightString(self.width - self.margin, self.height - 50, title_lang)

    def draw_footer(self, page_num, total_pages):
        self.c.setStrokeColor(colors.HexColor("#cbd5e1"))
        self.c.setLineWidth(0.5)
        self.c.line(self.margin, 35, self.width - self.margin, 35)

        self.c.setFont("SegoeUI", 8)
        self.c.setFillColor(colors.HexColor("#64748b"))
        self.c.drawString(self.margin, 22, "Zafer Yorgancı  —  Application Letter  |  Turkish Süper Lig Technical & Scouting Committees")
        self.c.drawRightString(self.width - self.margin, 22, f"Page {page_num} of {total_pages}")

    def draw_turkish_page(self):
        self.draw_header("RESMİ BAŞVURU & ÖN YAZI", "TÜRKİYE SÜPER LİG KULÜPLERİNE")
        y = self.height - 125

        # Recipient info
        self.c.setFont("SegoeUI-Bold", 10)
        self.c.setFillColor(colors.HexColor("#0f172a"))
        self.c.drawString(self.margin, y, "Sayın Kulüp Yöneticileri, Sportif Direktörler ve Teknik Heyet;")
        y -= 18

        self.c.setFont("SegoeUI-SemiBold", 9.5)
        self.c.setFillColor(colors.HexColor("#0284c7"))
        self.c.drawString(self.margin, y, "Konu: Futbol Veri Görselleştirme Uzmanı ve AI Mühendisi Görevi İçin Başvuru")
        y -= 20

        paragraphs = [
            "Modern futbolda şampiyonluklar ve sürdürülebilir başarılar, ham verinin sahada aksiyona dönüşebilme hızıyla belirlenmektedir. 2025–2026 sezonunda Polonya Ekstraklasa kulüplerinden Górnik Zabrze bünyesinde Uzaktan/Hibrit Spor Veri Görselleştirme Uzmanı olarak görev yapmış, aynı zamanda Polonya'da (Wrocław ve Varşova) uzun yıllar eğitim almış ve uluslararası teknoloji projelerinde yöneticilik yapmış bir veri uzmanı olarak, bu birikimimi Türkiye Süper Ligi'nin zirve kulüplerine aktarmak amacıyla başvurmaktayım.",

            "Górnik Zabrze'deki görev sürecimde; teknik direktör ve maç analizi ekibi için Opta ve Wyscout etkinlik verilerini işleyen özel Python/mplsoccer algoritmaları kurdum. Maç öncesi rakip analizinde pas ağları (passing networks), beklerin ve hücum hattının oluşturduğu Beklenen Tehdit (Expected Threat - xT) ısı haritaları, takımın savunma hattı derinliği ve pres yoğunluğu (PPDA) görselleştirilerek teknik heyetin hazırlık süresi %40 oranında kısaltıldı.",

            "Süper Lig kulüplerimizin karşılaştığı en kritik zorluklardan biri, transfer bütçelerini verimli kullanarak yüksek fiziksel ve taktiksel dayanıklılığa sahip oyuncuları değerinin altında keşfetmektir. Geliştirdiğim denetimsiz yapay zeka (K-Means ve PCA) kümeleme modelleri sayesinde, Süper Lig'in yüksek tempolu geçiş oyununa ve pres sistemlerine doğrudan uyum sağlayabilecek Polonya ve Orta/Doğu Avrupa kökenli oyuncuları (örneğin ligin en yüksek savunma ikili mücadele kazanma oranına (%67.4) ve pas ilerletme kalitesine sahip Damian Rasak gibi hedefleri) veri tabanlı olarak tespit edip yönetim kurullarına sundum.",

            "Yapay zeka sistemleri, veri bilimi ve üst düzey görsel iletişim alanındaki 12 yılı aşkın tecrübemi; kulübünüzün scouting ağı, teknik analiz birimi ve sportif direktörlüğü ile tam bir sinerji içinde kullanmaya hazırım. Ekte sunduğum 2025–2026 Górnik Zabrze & Polonya Ekstraklasa Veri Portfolyom ve detaylı özgeçmişim, kulübünüze sağlayabileceğim katma değerin somut bir örneğidir.",

            "Kulübünüzün hedefleri doğrultusunda detaylı bir teknik sunum yapmak ve veri altyapınızı dünya standartlarına taşımak üzere görüşmeyi sabırsızlıkla beklerim."
        ]

        for p in paragraphs:
            text_obj = self.c.beginText(self.margin, y)
            text_obj.setFont("SegoeUI", 8.8)
            text_obj.setFillColor(colors.HexColor("#1e293b"))
            text_obj.setLeading(13)
            wrapped = self.wrap_text(p, 515)
            for line in wrapped:
                text_obj.textLine(line)
            self.c.drawText(text_obj)
            y -= (len(wrapped) * 13 + 10)

        # Signature
        y -= 10
        self.c.setFont("SegoeUI-Bold", 9.5)
        self.c.setFillColor(colors.HexColor("#0f172a"))
        self.c.drawString(self.margin, y, "Saygılarımla,")
        y -= 16
        self.c.setFont("SegoeUI-Bold", 11)
        self.c.setFillColor(colors.HexColor("#0284c7"))
        self.c.drawString(self.margin, y, "Zafer Yorgancı")
        y -= 13
        self.c.setFont("SegoeUI", 8.5)
        self.c.setFillColor(colors.HexColor("#64748b"))
        self.c.drawString(self.margin, y, "Futbol Veri Görselleştirme Uzmanı & Yapay Zeka Mühendisi")
        self.c.drawString(self.margin, y - 12, "Eski Görsel Yönetmen | Górnik Zabrze Veri Uzmanı (2025–2026)")

        self.draw_footer(1, 2)
        self.c.showPage()

    def draw_english_page(self):
        self.draw_header("OFFICIAL APPLICATION & COVER LETTER", "FOR TÜRKİYE SÜPER LİG CLUBS")
        y = self.height - 125

        # Recipient info
        self.c.setFont("SegoeUI-Bold", 10)
        self.c.setFillColor(colors.HexColor("#0f172a"))
        self.c.drawString(self.margin, y, "To the Sporting Director, Head of Recruitment, and Coaching Staff;")
        y -= 18

        self.c.setFont("SegoeUI-SemiBold", 9.5)
        self.c.setFillColor(colors.HexColor("#0284c7"))
        self.c.drawString(self.margin, y, "Subject: Application for Football Data Visualization Specialist / AI Analytics Engineer")
        y -= 20

        paragraphs = [
            "In modern elite football, the difference between winning titles and squandering capital lies in the speed at which raw data translates into actionable on-pitch tactical decisions. Having served as a Remote Sports Data Visualization Specialist for Górnik Zabrze during the 2025–2026 Polish Ekstraklasa campaign, and possessing an extensive academic and professional background in Poland (Wrocław and Warsaw) combined with Istanbul residency, I am writing to apply for analytics and visualization specialist roles within Turkish Süper Lig clubs.",

            "During my work with Górnik Zabrze, I engineered dedicated Python/mplsoccer analytical pipelines that ingested Opta and Wyscout event streams. For the coaching and performance analysis staff, I designed automated pre-match opposition tactical reports (passing networks, zonal Expected Threat [xT] grids, PPDA defensive territory density) and post-match xG flow trackers, accelerating tactical debrief turnaround by 40% while preserving strict visual clarity.",

            "One of the paramount challenges facing Turkish Süper Lig clubs is identifying undervalued, high-tempo, physically resilient talent in Central and Eastern Europe before their transfer valuations escalate. By implementing unsupervised machine learning models (PCA and K-Means clustering), I established automated positional-twin scouting engines that benchmark players against Süper Lig tactical demands—such as uncovering Damian Rasak (leading the league in defensive duel win rate at 67.4% while maintaining 6.82 progressive passes/90) as a prime transfer asset under €2.0M.",

            "Combining over 12 years of enterprise creative direction, AI prompt and software engineering, and rigorous football domain expertise, I offer an end-to-end bridge between data science and the technical coaching bench. The attached 2025–2026 Górnik Zabrze & Ekstraklasa Data Visualization Portfolio provides concrete evidence of my execution standards.",

            "I would welcome the opportunity to present my analytical workflows and discuss how we can establish a world-class, data-driven visual intelligence department at your club."
        ]

        for p in paragraphs:
            text_obj = self.c.beginText(self.margin, y)
            text_obj.setFont("SegoeUI", 8.8)
            text_obj.setFillColor(colors.HexColor("#1e293b"))
            text_obj.setLeading(13)
            wrapped = self.wrap_text(p, 515)
            for line in wrapped:
                text_obj.textLine(line)
            self.c.drawText(text_obj)
            y -= (len(wrapped) * 13 + 10)

        # Signature
        y -= 10
        self.c.setFont("SegoeUI-Bold", 9.5)
        self.c.setFillColor(colors.HexColor("#0f172a"))
        self.c.drawString(self.margin, y, "Sincerely,")
        y -= 16
        self.c.setFont("SegoeUI-Bold", 11)
        self.c.setFillColor(colors.HexColor("#0284c7"))
        self.c.drawString(self.margin, y, "Zafer Yorgancı")
        y -= 13
        self.c.setFont("SegoeUI", 8.5)
        self.c.setFillColor(colors.HexColor("#64748b"))
        self.c.drawString(self.margin, y, "Football Data Visualization Specialist & AI Engineer")
        self.c.drawString(self.margin, y - 12, "Former Creative Director | Data Specialist, Górnik Zabrze (2025–2026)")

        self.draw_footer(2, 2)
        self.c.showPage()

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
        self.draw_turkish_page()
        self.draw_english_page()
        self.c.save()
        print(f"Successfully generated {self.filename}")

if __name__ == "__main__":
    letter = CoverLetterPdf(OUTPUT_PATH)
    letter.build()
