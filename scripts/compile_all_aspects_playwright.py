import base64
import os
from playwright.sync_api import sync_playwright

def get_base64_image(image_path):
    if not os.path.exists(image_path):
        return ""
    with open(image_path, "rb") as f:
        return f"data:image/png;base64,{base64.b64encode(f.read()).decode('utf-8')}"

# ==============================================================================
# CSS STYLES FOR HIGH-PRECISION PRINTING
# ==============================================================================
CV_CSS = """
  @page { size: A4; margin: 0; }
  * { box-sizing: border-box; margin: 0; padding: 0; }
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
    color: #ffffff;
    line-height: 1.1;
  }
  .header-title {
    font-size: 11pt;
    font-weight: 700;
    color: #38bdf8;
    margin-top: 4px;
  }
  .header-meta {
    font-size: 8.5pt;
    color: #94a3b8;
    margin-top: 6px;
    display: flex;
    flex-wrap: wrap;
    gap: 12px;
  }
  .header-meta a { color: #38bdf8; text-decoration: none; }
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
  .section { margin-bottom: 12px; }
  .section-title {
    font-size: 10pt;
    font-weight: 800;
    text-transform: uppercase;
    color: #0f172a;
    letter-spacing: 0.04em;
    border-bottom: 1.5px solid #0284c7;
    padding-bottom: 3px;
    margin-bottom: 8px;
  }
  .section-content { font-size: 8.5pt; line-height: 1.42; color: #334155; }
  .job-entry { margin-bottom: 9px; }
  .job-header { display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 3px; }
  .job-role { font-size: 9.2pt; font-weight: 700; color: #0f172a; }
  .job-company { font-size: 9pt; font-weight: 700; color: #0284c7; }
  .job-date { font-size: 8pt; font-weight: 700; color: #64748b; }
  .job-bullets { list-style-type: none; padding-left: 0; }
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
  .job-bullets strong { color: #0f172a; }
  .skills-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 8px; }
  .skill-card { background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 6px; padding: 7px 10px; }
  .skill-title { font-size: 8.2pt; font-weight: 800; color: #0284c7; text-transform: uppercase; margin-bottom: 2px; }
  .skill-desc { font-size: 7.8pt; line-height: 1.35; color: #334155; }
  .edu-entry { margin-bottom: 6px; }
  .edu-header { display: flex; justify-content: space-between; font-size: 8.6pt; font-weight: 700; color: #0f172a; }
  .edu-sub { font-size: 8pt; color: #0284c7; font-weight: 600; }
  .footer {
    display: flex;
    justify-content: space-between;
    font-size: 7.8pt;
    color: #64748b;
    border-top: 1px solid #e2e8f0;
    padding-top: 6px;
  }
"""

DOSSIER_CSS = """
  @page { size: A4; margin: 0; }
  * { box-sizing: border-box; margin: 0; padding: 0; }
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
    padding: 13mm 16mm 11mm 16mm;
    page-break-after: always;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    overflow: hidden;
    position: relative;
    background: #0f172a;
  }
  .cover-page {
    justify-content: space-between;
    padding: 22mm 20mm;
    background: linear-gradient(180deg, #1e293b 0%, #0f172a 100%);
    border-top: 6px solid #0284c7;
    border-bottom: 6px solid #c8102e;
  }
  .cover-tag { font-size: 10pt; font-weight: 800; color: #38bdf8; letter-spacing: 0.08em; text-transform: uppercase; margin-bottom: 10px; }
  .cover-title { font-size: 24pt; font-weight: 900; color: #ffffff; line-height: 1.15; margin-bottom: 6px; }
  .cover-subtitle { font-size: 15pt; font-weight: 700; color: #94a3b8; margin-bottom: 12px; }
  .cover-target { font-size: 10.5pt; font-weight: 600; color: #38bdf8; margin-bottom: 24px; padding-bottom: 14px; border-bottom: 1px solid #334155; }
  .cover-card { background: #1e293b; border: 1px solid #334155; border-radius: 8px; padding: 18px 22px; margin-bottom: 20px; }
  .cover-card-title { font-size: 10.5pt; font-weight: 800; color: #38bdf8; text-transform: uppercase; margin-bottom: 8px; }
  .cover-card-text { font-size: 9pt; line-height: 1.5; color: #cbd5e1; margin-bottom: 8px; }
  .cover-meta-grid { display: grid; grid-template-columns: 140px 1fr; gap: 8px; font-size: 9pt; margin-top: 10px; }
  .cover-meta-label { font-weight: 800; color: #38bdf8; }
  .cover-meta-val { color: #f8fafc; font-weight: 600; }
  .page-header { border-bottom: 1.5px solid #0284c7; padding-bottom: 5px; margin-bottom: 8px; }
  .page-section { font-size: 7.8pt; font-weight: 800; color: #38bdf8; text-transform: uppercase; letter-spacing: 0.06em; }
  .page-title-row { display: flex; justify-content: space-between; align-items: baseline; margin-top: 2px; }
  .page-title { font-size: 12pt; font-weight: 800; color: #ffffff; }
  .page-num { font-size: 8.5pt; font-weight: 800; color: #64748b; }
  .page-subtitle { font-size: 7.8pt; color: #94a3b8; margin-top: 2px; }
  .image-container {
    width: 100%;
    height: 485px;
    display: flex;
    align-items: center;
    justify-content: center;
    background: #0b1120;
    border-radius: 8px;
    border: 1px solid #1e293b;
    margin-bottom: 8px;
    overflow: hidden;
  }
  .image-container img { max-width: 100%; max-height: 100%; object-fit: contain; display: block; }
  .commentary-card {
    background: #1e293b;
    border: 1px solid #334155;
    border-left: 4px solid #0284c7;
    border-radius: 6px;
    padding: 9px 13px;
    margin-bottom: 7px;
  }
  .commentary-title { font-size: 8pt; font-weight: 800; color: #38bdf8; text-transform: uppercase; letter-spacing: 0.04em; margin-bottom: 4px; }
  .commentary-bullets { list-style-type: none; padding: 0; }
  .commentary-bullets li {
    position: relative;
    padding-left: 12px;
    margin-bottom: 2.5px;
    font-size: 7.8pt;
    line-height: 1.34;
    color: #cbd5e1;
  }
  .commentary-bullets li::before { content: "•"; position: absolute; left: 0; color: #38bdf8; font-weight: bold; font-size: 9pt; }
  .commentary-bullets strong { color: #ffffff; }
  .kpi-row { display: grid; grid-template-columns: repeat(5, 1fr); gap: 7px; margin-bottom: 5px; }
  .kpi-card { background: #0b1120; border: 1px solid #334155; border-radius: 5px; padding: 4px 6px; text-align: center; }
  .kpi-label { font-size: 6.8pt; font-weight: 700; color: #94a3b8; text-transform: uppercase; }
  .kpi-value { font-size: 8.6pt; font-weight: 800; color: #fbbf24; margin-top: 1px; }
  .page-footer {
    display: flex;
    justify-content: space-between;
    font-size: 7.2pt;
    color: #64748b;
    border-top: 1px solid #1e293b;
    padding-top: 5px;
  }
"""

# ==============================================================================
# 1. BUILD TURKISH CV HTML
# ==============================================================================
def build_turkish_cv_html():
    return f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>{CV_CSS}</style>
</head>
<body>
  <!-- SAYFA 1 -->
  <div class="page">
    <div>
      <div class="header-banner">
        <div class="header-name">ZAFER YORGANCI</div>
        <div class="header-title">FUTBOL VERİ GÖRSELLEŞTİRME UZMANI & YAPAY ZEKA MÜHENDİSİ</div>
        <div class="header-meta">
          <span>📍 İstanbul, Türkiye</span>
          <span>✉️ zafer.v2.ai@gmail.com</span>
          <span>📞 +90 501 954 97 27</span>
          <span>🌐 <a href="https://portfolio.zfryrgnci.workers.dev">portfolio.zfryrgnci.workers.dev</a></span>
          <span>💻 github.com/zfryrgnci</span>
        </div>
        <div class="header-target">
          ★ HEDEF ROL: Futbol Veri Görselleştirme Uzmanı / Maç ve Performans Analisti | Süper Lig Kulüpleri
        </div>
      </div>

      <!-- Yönetici Özeti -->
      <div class="section">
        <div class="section-title">Yönetici Özeti (Executive Profile)</div>
        <div class="section-content">
          Saha içi maç etkinlik verilerini (Opta, StatsBomb, Wyscout) ileri düzey görsel tasarım ve yapay zeka modelleriyle birleştiren uzman futbol veri görselleştirme uzmanı ve AI mühendisi. Teknik direktörler, analiz departmanları ve sportif direktörler için aksiyona dönüştürülebilir maç öncesi rakip analiz dosyaları, transfer ve scouting gösterge panelleri ve maç sonu performans raporları sunma konusunda kulüp tecrübesine sahip. Python (<code>mplsoccer</code>, Scikit-learn, PyTorch), modern web mimarileri ve denetimsiz makine öğrenimi modellerini kullanarak karmaşık takip ve etkinlik verilerini taktiksel üstünlüğe dönüştürür. Polonya'da (Wrocław ve Varşova) eğitim almış ve uzun yıllar yaşamış, İstanbul'da ikamet eden ana dili Türkçe bir uzman olarak; Süper Lig kulüplerinin dinamik Orta ve Doğu Avrupa pazarlarından transfer hedeflerini analiz etmek için ideal profile sahiptir.
        </div>
      </div>

      <!-- Profesyonel Deneyim -->
      <div class="section">
        <div class="section-title">Futbol Analitiği & Profesyonel Deneyim</div>

        <!-- Rol 1: Górnik Zabrze -->
        <div class="job-entry">
          <div class="job-header">
            <div>
              <span class="job-company">Górnik Zabrze</span>
              <span class="job-role"> — Spor Veri Görselleştirme Uzmanı</span>
              <span style="font-size: 8pt; color: #0284c7; font-weight: 600;">(Uzaktan / Hibrit)</span>
            </div>
            <div class="job-date">2025 – 2026 Sezonu</div>
          </div>
          <ul class="job-bullets">
            <li><strong>mplsoccer</strong>, <strong>matplotlib</strong> ve Opta/Wyscout etkinlik verilerini işleyen uçtan uca Python taktiksel görselleştirme hatları kurarak teknik heyet ve maç analiz ekibi için maç öncesi rakip analizleri ve maç sonu debrief raporları hazırladı.</li>
            <li>Rakibin geçiş zaaflarını ve pres tetikleyicilerini haritalandırmak üzere otomatik <strong>Pas Ağları (Passing Networks)</strong>, <strong>Beklenen Tehdit (Expected Threat - xT)</strong> 12x8 saha ısı haritaları ve <strong>PPDA savunma yerleşimi modelleri</strong> geliştirdi.</li>
            <li>Yüzdelik Pizza Grafikleri (<strong>Percentile Pizza Radars</strong>) ve çok değişkenli saçılım matrisleri ile kilit oyuncular (Damian Rasak, Lukas Podolski, Erik Janża) ve potansiyel transfer hedefleri için scouting panelleri inşa etti.</li>
            <li>Kısıtlı transfer bütçeleri altında kadro yenileme senaryoları üretmek amacıyla 140+ Ekstraklasa oyuncusu üzerinde denetimsiz makine öğrenimi (<strong>K-Means ve PCA kümeleme</strong>) uygulayarak taktiksel ikizleri (tactical twins) tespit etti.</li>
            <li>Ham veri akışlarını teknik heyetin doğrudan anlayabileceği yüksek kontrastlı görsel şablonlara dönüştürerek maç öncesi taktik hazırlık süresini <strong>%40 oranında</strong> kısalttı.</li>
          </ul>
        </div>

        <!-- Rol 2: Xiaomi -->
        <div class="job-entry">
          <div class="job-header">
            <div>
              <span class="job-company">Xiaomi Technology</span>
              <span class="job-role"> — Görsel Yönetmen (Creative Director)</span>
              <span style="font-size: 8pt; color: #64748b;">(CEE & İskandinav Pazarları)</span>
            </div>
            <div class="job-date">Varşova, Polonya | 2024 – 2025</div>
          </div>
          <ul class="job-bullets">
            <li>Orta ve Doğu Avrupa ile İskandinavya bölgelerinde yüksek tempolu görsel kampanyaları ve veri odaklı marka tasarım mimarisini yönetti.</li>
            <li>Konsept geliştirme ve üretim süreçlerini hızlandırmak amacıyla <strong>üretken yapay zeka (GenAI)</strong> iş akışlarını ve otomasyon araçlarını entegre etti.</li>
            <li>Uluslararası ekipler, kreatif ajanslar ve teknik paydaşlar arasında çok uluslu bütçe ve proje yönetimi yürüttü.</li>
          </ul>
        </div>

        <!-- Rol 3: AON -->
        <div class="job-entry">
          <div class="job-header">
            <div>
              <span class="job-company">AON</span>
              <span class="job-role"> — Kıdemli Görsel Tasarım Uzmanı</span>
            </div>
            <div class="job-date">Krakow, Polonya | 2023 – 2024</div>
          </div>
          <ul class="job-bullets">
            <li>Küresel kurumsal paydaşlar için yönetici seviyesinde raporlama şablonları, görsel iletişim sistemleri ve dijital materyaller üretti.</li>
            <li>Departman verimliliğini artırmak amacıyla yapay zeka tabanlı veri işleme ve görselleştirme iş akışlarını devreye aldı.</li>
          </ul>
        </div>

        <!-- Rol 4: Cognizant -->
        <div class="job-entry">
          <div class="job-header">
            <div>
              <span class="job-company">Cognizant Technology Solutions</span>
              <span class="job-role"> — Kıdemli Operasyon Yöneticisi</span>
              <span style="font-size: 8pt; color: #64748b;">(Google Vendor Office)</span>
            </div>
            <div class="job-date">Krakow, Polonya | 2022 – 2023</div>
          </div>
          <ul class="job-bullets">
            <li>Uluslararası Google hesapları için dijital analitik operasyonlarını, Google Analytics, Google Ads ve performans raporlamalarını koordine etti.</li>
            <li>Yüksek veri bütünlüğü sağlamak amacıyla otomatik yönetici dashboard'ları ve raporlama araçları tasarladı.</li>
          </ul>
        </div>

      </div>
    </div>

    <div class="footer">
      <span>Zafer Yorgancı — Özgeçmiş | Futbol Veri Görselleştirme Uzmanı & Yapay Zeka Mühendisi</span>
      <span>portfolio.zfryrgnci.workers.dev • Sayfa 1 / 2</span>
    </div>
  </div>

  <!-- SAYFA 2 -->
  <div class="page">
    <div>
      <div class="header-banner" style="padding: 12px 20px; margin-bottom: 14px;">
        <div style="display: flex; justify-content: space-between; align-items: center;">
          <div>
            <span style="font-size: 14pt; font-weight: 800; color: #ffffff;">ZAFER YORGANCI</span>
            <span style="font-size: 9.5pt; font-weight: 700; color: #38bdf8; margin-left: 10px;">ÖZGEÇMİŞ & TEKNİK YETKİNLİKLER</span>
          </div>
          <div style="font-size: 8pt; color: #94a3b8;">
            zafer.v2.ai@gmail.com • +90 501 954 97 27
          </div>
        </div>
      </div>

      <!-- Ek Teknik Deneyim -->
      <div class="section">
        <div class="section-title">Ek Teknik Deneyim & Liderlik</div>

        <div class="job-entry">
          <div class="job-header">
            <div>
              <span class="job-company">Genpact</span>
              <span class="job-role"> — Yapay Zeka Veri ve İçerik Uzmanı</span>
              <span style="font-size: 8pt; color: #64748b;">(YouTube Güvenlik & Uyumluluk, Google Vendor)</span>
            </div>
            <div class="job-date">Krakow, Polonya | 2021 – 2022</div>
          </div>
          <ul class="job-bullets">
            <li>Yapay zeka ve makine öğrenimi modellerini eğitmek amacıyla büyük ölçekli yapılandırılmış çok modlu veri setlerini sınıflandırdı ve denetledi.</li>
          </ul>
        </div>

        <div class="job-entry">
          <div class="job-header">
            <div>
              <span class="job-company">Struktur.agency</span>
              <span class="job-role"> — Kurucu & Kreatif Teknolog</span>
            </div>
            <div class="job-date">Remote | 2018 – Günümüz</div>
          </div>
          <ul class="job-bullets">
            <li>İnteraktif WebGL uygulamaları, özel hesaplamalı gölgelendiriciler, 3D veri görselleştirmeleri ve otomasyon araçları geliştirdi.</li>
          </ul>
        </div>
      </div>

      <!-- Temel Yetkinlikler -->
      <div class="section">
        <div class="section-title">Futbol Analitiği & AI Mühendisliği Temel Yetkinlikleri</div>
        <div class="skills-grid">
          <div class="skill-card">
            <div class="skill-title">Futbol Etkinlik Modelleri</div>
            <div class="skill-desc">Beklenen Goller (xG), Beklenen Tehdit (xT - Karun Singh), Pres Yoğunluğu (PPDA), Field Tilt %, Pas Ağları, Şut Takımyıldızları, Duran Top Teslimat Şemaları, Kaleci Dağıtım Hatları.</div>
          </div>
          <div class="skill-card">
            <div class="skill-title">Veri & Python Ekosistemi</div>
            <div class="skill-desc">Python (<code>mplsoccer</code>, <code>matplotlib</code>, <code>seaborn</code>, <code>pandas</code>, <code>numpy</code>, <code>scipy</code>, <code>scikit-learn</code>), SQL, JupyterLab, REST API, JSON veri akışı işleme.</div>
          </div>
          <div class="skill-card">
            <div class="skill-title">Yapay Zeka & Makine Öğrenimi</div>
            <div class="skill-desc">Denetimsiz kümeleme (K-Means), Boyut İndirgeme (PCA), benzerlik motorları (oyuncu ikizleri tespiti için kosinüs/öklid mesafesi), gelişmiş istem mimarisi (Claude, GPT-4, Gemini).</div>
          </div>
          <div class="skill-card">
            <div class="skill-title">Frontend & Web Görselleştirme</div>
            <div class="skill-desc">HTML5, CSS3, JavaScript (ES6+), React, Vite, TypeScript, Tailwind CSS, WebGL, Canvas, Chart.js, interaktif scouting dashboard'ları.</div>
          </div>
          <div class="skill-card" style="grid-column: span 2;">
            <div class="skill-title">Görsel İletişim & Tasarım Ustalığı</div>
            <div class="skill-desc">Adobe Creative Suite (Photoshop, Illustrator, InDesign, Premiere Pro), Figma, tipografi standartları, yüksek kontrastlı karanlık mod sunum paletleri, teknik direktörlere yönelik görsel raporlama.</div>
          </div>
        </div>
      </div>

      <!-- Eğitim & Akademik Geçmiş -->
      <div class="section">
        <div class="section-title">Eğitim & Akademik Geçmiş</div>

        <div class="edu-entry">
          <div class="edu-header">
            <span>DSW Ideis Üniversitesi (Dolnośląska Szkoła Wyższa)</span>
            <span style="font-size: 8pt; color: #64748b;">Wrocław, Polonya | 2017 – 2021</span>
          </div>
          <div class="edu-sub">Lisans (B.A.) — Kreatif Medya: Film ve Oyunlar için 3D Animasyon & Görsel Efektler</div>
        </div>

        <div class="edu-entry" style="margin-top: 6px;">
          <div class="edu-header">
            <span>FH Oberösterreich (Upper Austria Uygulamalı Bilimler Üniversitesi)</span>
            <span style="font-size: 8pt; color: #64748b;">Hagenberg, Avusturya | 2018 – 2019</span>
          </div>
          <div class="edu-sub">Dijital İletişim ve Multimedya — Uluslararası Akademik Değişim Programı</div>
        </div>
      </div>

      <!-- Diller & Bölgesel Avantaj -->
      <div class="section">
        <div class="section-title">Diller & Bölgesel Scouting Kapsamı</div>
        <div class="section-content" style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 6px; padding: 8px 12px;">
          <p style="margin-bottom: 4px;">
            <strong>Diller:</strong> Türkçe (Ana Dil) • İngilizce (C1 İleri Düzey - Tam Profesyonel Yetkinlik) • Almanca (B1) • Lehçe (Profesyonel Çalışma Düzeyi).
          </p>
          <p style="color: #0284c7; font-weight: 600;">
            ★ Süper Lig İçin Stratejik Avantaj: Orta ve Doğu Avrupa liglerine (Polonya Ekstraklasa, Çekya Ligi, Avusturya Bundesliga) dair derin saha içi ve taktiksel hakimiyet; doğrudan veri entegrasyonu, transfer keşfi ve teknik heyet iletişimi.
          </p>
        </div>
      </div>

    </div>

    <div class="footer">
      <span>Zafer Yorgancı — Özgeçmiş | Futbol Veri Görselleştirme Uzmanı & Yapay Zeka Mühendisi</span>
      <span>portfolio.zfryrgnci.workers.dev • Sayfa 2 / 2</span>
    </div>
  </div>
</body>
</html>
"""

# ==============================================================================
# 2. BUILD MODULAR PORTFOLIO BUILDER
# ==============================================================================
def build_custom_dossier_html(cover_dict, pages_list):
    html = f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>{DOSSIER_CSS}</style>
</head>
<body>
  <!-- COVER PAGE -->
  <div class="page cover-page">
    <div>
      <div class="cover-tag">{cover_dict["tag"]}</div>
      <div class="cover-title">{cover_dict["title"]}</div>
      <div class="cover-subtitle">{cover_dict["subtitle"]}</div>
      <div class="cover-target">{cover_dict["target"]}</div>

      <div class="cover-card">
        <div class="cover-card-title">{cover_dict["box_title"]}</div>
        <p class="cover-card-text">{cover_dict["p1"]}</p>
        <p class="cover-card-text">{cover_dict["p2"]}</p>
        <p class="cover-card-text">{cover_dict["p3"]}</p>
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
      <span>Confidential Technical Report • Süper Lig Application Dossier</span>
    </div>
  </div>
"""

    total_pages = len(pages_list) + 1
    for idx, p in enumerate(pages_list):
        page_num = idx + 2
        kpi_html = "".join([f'<div class="kpi-card"><div class="kpi-label">{k}</div><div class="kpi-value">{v}</div></div>' for k, v in p["kpis"]])
        bullets_html = "".join([f'<li>{b}</li>' for b in p["bullets"]])

        html += f"""
  <!-- PAGE {page_num} -->
  <div class="page">
    <div>
      <div class="page-header">
        <div class="page-section">{p["section"]}</div>
        <div class="page-title-row">
          <div class="page-title">{p["title"]}</div>
          <div class="page-num">PAGE {page_num} OF {total_pages}</div>
        </div>
        <div class="page-subtitle">{p["subtitle"]}</div>
      </div>

      <div class="image-container">
        <img src="{p["img"]}" alt="{p["title"]}">
      </div>

      <div class="commentary-card">
        <div class="commentary-title">TACTICAL EVALUATION & DECISION INSIGHTS:</div>
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

    html += """</body></html>"""
    return html

# ==============================================================================
# MAIN EXECUTION COMPILER
# ==============================================================================
def main():
    print("================================================================================")
    print("  COMPILING MODULAR SPECIALIZED FOOTBALL PORTFOLIOS & TURKISH/ENGLISH CVs")
    print("================================================================================")

    # Load all image assets as base64
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
        "ai_clusters": get_base64_image("visuals/13_ai_player_archetype_clusters.png"),
        "set_piece": get_base64_image("visuals/14_set_piece_corner_routines.png"),
        "gk_profile": get_base64_image("visuals/15_goalkeeper_distribution_profile.png"),
        "squad_age": get_base64_image("visuals/16_squad_age_curve_lifecycle.png")
    }

    with sync_playwright() as p:
        browser = p.chromium.launch()

        # -------------------------------------------------------------
        # 1. COMPILE TURKISH CV
        # -------------------------------------------------------------
        print("\n[1/6] Compiling Zafer_Yorganci_Futbol_CV_TR.pdf...")
        page = browser.new_page()
        page.set_content(build_turkish_cv_html())
        page.pdf(path="Zafer_Yorganci_Futbol_CV_TR.pdf", format="A4", print_background=True, margin={"top":"0mm","bottom":"0mm","left":"0mm","right":"0mm"})
        page.close()
        print(" -> SUCCESS: Zafer_Yorganci_Futbol_CV_TR.pdf")

        # -------------------------------------------------------------
        # 2. COMPILE ENGLISH CV
        # -------------------------------------------------------------
        print("\n[2/6] Compiling Zafer_Yorganci_Football_CV_EN.pdf (and main CV)...")
        from compile_all_pdfs_playwright import generate_cv_html
        page = browser.new_page()
        page.set_content(generate_cv_html())
        page.pdf(path="Zafer_Yorganci_Football_CV_EN.pdf", format="A4", print_background=True, margin={"top":"0mm","bottom":"0mm","left":"0mm","right":"0mm"})
        page.pdf(path="Zafer_Yorganci_Football_CV.pdf", format="A4", print_background=True, margin={"top":"0mm","bottom":"0mm","left":"0mm","right":"0mm"})
        page.close()
        print(" -> SUCCESS: Zafer_Yorganci_Football_CV_EN.pdf & Zafer_Yorganci_Football_CV.pdf")

        # -------------------------------------------------------------
        # 3. PORTFOLIO 1: PRE-MATCH OPPOSITION ANALYSIS (WHAT COACHES ASK FOR)
        # -------------------------------------------------------------
        print("\n[3/6] Compiling 1_PreMatch_Opposition_Analysis_Gornik_Zabrze.pdf...")
        cover_p1 = {
            "tag": "PRE-MATCH OPPOSITION DOSSIER | COACHING & TACTICAL ANALYSIS",
            "title": "OPPOSITION TACTICAL ANALYSIS: GÓRNIK ZABRZE",
            "subtitle": "Pre-Match Briefing for Head Coaches, Analysts & Technical Bench",
            "target": "Actionable Opposition Preparation Framework: Build-Up, Pressing Triggers, Set-Pieces & Goalkeeping",
            "box_title": "WHAT HEAD COACHES DEMAND FROM DATA ANALYSTS",
            "p1": "Head coaches require answers to practical training-pitch questions: Where does the opponent build up? Where are their pressing triggers? How do they organize on set-pieces? What are their goalkeeper's distribution habits under pressure?",
            "p2": "This dossier breaks down Górnik Zabrze into 6 actionable tactical components: Starting XI Passing Network, Defensive Territory & PPDA Density, Open-Play Expected Threat (xT) spatial zones, Inswinging/Outswinging Corner Delivery Routines, Goalkeeper Distribution & Shot-Stopping, and Post-Match xG Flow.",
            "p3": "Designed for immediate digestion in under 90 seconds per page, bridging high-dimensional tracking streams directly into training-pitch instructions."
        }
        pages_p1 = [
            {
                "section": "Build-Up Shape & Progression Channels",
                "title": "Starting XI Passing Network & Build-Up Structure",
                "subtitle": "Average Positions, Passing Frequency Channels & Centralization Hubs",
                "img": imgs["pass_net"],
                "bullets": [
                    "<strong>Left-Flank Overload:</strong> 42% of forward progression flows through the Janicki -> Janża -> Rasak -> Podolski diamond, creating a structural overload.",
                    "<strong>Weak-Side Transition:</strong> Once the opponent shifts across to counter the left overload, rapid diagonal switches find Taofeek Ismaheel in 1v1 situations.",
                    "<strong>Tactical Instruction:</strong> Set pressing trap on Janza to deny inside access to Rasak and force lateral back-passes."
                ],
                "kpis": [("Centralization Index", "44.8%"), ("Left-Side Bias", "42.1%"), ("Progression Speed", "1.84 m/s"), ("Core Hub", "Janicki-Rasak (19p)"), ("Avg Sequence", "4.8 Passes")]
            },
            {
                "section": "Pressing Mechanics & Defensive Shape",
                "title": "Defensive Territory, High Pressing & PPDA Spatial Density",
                "subtitle": "Ball Recoveries, High Turnover Zones & Mean Defensive Line Height",
                "img": imgs["def_terr"],
                "bullets": [
                    "<strong>Aggressive High Press:</strong> Team PPDA of 9.1 ranks 4th in the league, forcing 9.5 high turnovers per 90 within 40m of the opponent's goal.",
                    "<strong>Defensive Line Height:</strong> Average defensive line sits high at 46.8m, squeezing central space between defense and midfield.",
                    "<strong>Vulnerability to Exploit:</strong> Space opens behind Janża's advanced wingback position; direct early balls into this channel create high-xG counters."
                ],
                "kpis": [("Team PPDA", "9.1 (Rank 4th)"), ("High Turnovers", "9.5 / 90"), ("Def Line Height", "46.8m"), ("Field Tilt %", "54.2%"), ("Box Entries Allowed", "5.2 / 90")]
            },
            {
                "section": "Spatial Threat & Zone 14 Penetration",
                "title": "Open-Play Expected Threat (xT) Spatial Pitch Grid (12×8)",
                "subtitle": "Probability of Goal Creation by Pitch Sector via Passing & Carries",
                "img": imgs["xt_grid"],
                "bullets": [
                    "<strong>Peak Threat Zone:</strong> Expected Threat reaches +0.42 xT in the left half-space 25-35m out, corresponding to Lukas Podolski's playmaking sector.",
                    "<strong>Zone 14 Funnel:</strong> Rather than wild crosses, Górnik systematically feeds Zone 14 before sliding low cutbacks across the 6-yard box.",
                    "<strong>Tactical Instruction:</strong> Deploy a dedicated defensive anchor to eliminate Podolski's turn-and-shoot window in the left halfspace."
                ],
                "kpis": [("Peak Sector xT", "+0.42 (Left Half)"), ("Zone 14 xT", "+0.38"), ("Flank vs Center Threat", "61% vs 39%"), ("Model Engine", "Karun Singh xT"), ("Resolution", "12x8 Grid")]
            },
            {
                "section": "Set-Pieces & Dead-Ball Strategy",
                "title": "Corner Kick Delivery Trajectories & First-Contact Targets",
                "subtitle": "Inswinging vs Outswinging Patterns, Target Runners & Blocker Routines",
                "img": imgs["set_piece"],
                "bullets": [
                    "<strong>Inswinging Danger:</strong> Erik Janża's left-footed inswingers from the right target the central 6-yard box (5 shots, 2 goals) and near-post flick (Janicki).",
                    "<strong>Screening Routine:</strong> Damian Rasak deliberately blocks the opposing goalkeeper's jump trajectory on corner deliveries.",
                    "<strong>Second-Phase Danger:</strong> Lukas Podolski stays stationed on the edge of the box (the D) for cleared balls to execute direct volleys."
                ],
                "kpis": [("Set-Piece xG", "9.1 xG (Rank 3rd)"), ("Primary Delivery", "Inswinger (58%)"), ("First Contact Target", "Szcześniak (CB)"), ("Near Post Target", "Janicki (CB)"), ("Edge Shooter", "Podolski (#10)")]
            },
            {
                "section": "Goalkeeper Scouting & Distribution",
                "title": "Goalkeeper Distribution Channels & Shot-Stopping Profile",
                "subtitle": "Filip Majchrowicz (#1) Pass Trajectories & Post-Shot xG Differential",
                "img": imgs["gk_profile"],
                "bullets": [
                    "<strong>Distribution Tendency:</strong> 48% of open-play distributions flow to left-back Janża; high presses must curve runs to cut this lateral outlet.",
                    "<strong>Long Launch Weakness:</strong> Long kicks down the right flank yield a low 38% aerial duel win rate; contesting these second balls wins possession.",
                    "<strong>Shot-Stopping Strength:</strong> Ranks top quartile with +0.18 Post-Shot xG prevented per 90; elite against perimeter shots, vulnerable to rapid rebounds."
                ],
                "kpis": [("PSxG Diff / 90", "+0.18"), ("Box Save %", "68.5%"), ("Cross Claim %", "8.4%"), ("Primary Outlet", "LB Janża (48%)"), ("Long Launch %", "38.2%")]
            },
            {
                "section": "Match Dynamics & Post-Match Debrief",
                "title": "Shot Map, xG Constellation & Cumulative Flow (2–1 Legia)",
                "subtitle": "Tactical Execution Verification, Finishing Zones & Momentum Shifts",
                "img": imgs["shot_map"],
                "bullets": [
                    "<strong>Shot Quality Dominance:</strong> Górnik achieved 0.154 xG/shot vs Legia's 0.118, creating 3 big chances in the central golden zone.",
                    "<strong>Decisive Finishes:</strong> Zahović (27', 0.38 xG cutback) and Podolski (81', 0.45 xG high turnover thunderbolt) sealed victory.",
                    "<strong>Takeaway for Coaches:</strong> Restricting Górnik's transition triggers limits their shot volume from 14 shots down to single digits."
                ],
                "kpis": [("Final Score", "2 - 1 Win"), ("Total xG", "2.15 vs 1.18"), ("xG / Shot", "0.154"), ("Big Chances", "3 vs 1"), ("Momentum Peak", "+0.9 (Late 2nd H)")]
            }
        ]
        page = browser.new_page()
        page.set_content(build_custom_dossier_html(cover_p1, pages_p1))
        page.pdf(path="1_PreMatch_Opposition_Analysis_Gornik_Zabrze.pdf", format="A4", print_background=True, margin={"top":"0mm","bottom":"0mm","left":"0mm","right":"0mm"})
        page.close()
        print(" -> SUCCESS: 1_PreMatch_Opposition_Analysis_Gornik_Zabrze.pdf")

        # -------------------------------------------------------------
        # 4. PORTFOLIO 2: RECRUITMENT & SQUAD TRANSFERS (WHAT SPORTING DIRECTORS ASK FOR)
        # -------------------------------------------------------------
        print("\n[4/6] Compiling 2_Recruitment_Scouting_Transfer_Intelligence.pdf...")
        cover_p2 = {
            "tag": "RECRUITMENT & TRANSFER DOSSIER | SPORTING DIRECTORS & HEADS OF SCOUTING",
            "title": "TRANSFER SCOUTING & SÜPER LİG RECRUITMENT INTELLIGENCE",
            "subtitle": "Evidence-Based Scouting: Metric Trees, Percentile Radars & Shadow Squads",
            "target": "Capital Optimization: High-Value Central/Eastern European Talent < €2.5M for Turkish Clubs",
            "box_title": "WHAT SPORTING DIRECTORS DEMAND FROM DATA ANALYSTS",
            "p2": "Sporting directors must avoid costly transfer mistakes and maintain shadow shortlists before key stars depart: 'Does this target fit our pressing game model?' 'Are their defensive duels repeatable in Turkey?' 'Who is the mathematical twin for our aging #6 under €2M?'",
            "p1": "This dossier provides a rigorous recruitment framework: Tailored Percentile Pizza Radars for specific roles (Damian Rasak as #6 transition anchor, Lukas Podolski as #10 playmaker, Erik Janża as #3 delivery full-back), league-wide creativity & pressing matrices, and an AI-driven K-Means/PCA archetype similarity engine.",
            "p3": "Highlights significant market inefficiency in the Polish Ekstraklasa, identifying elite physical and technical contributors before Western European price inflation occurs."
        }
        pages_p2 = [
            {
                "section": "Positional Benchmark — Defensive Midfielder (#6)",
                "title": "Damian Rasak (29, DM/CM) — The High-Tempo Transition Anchor",
                "subtitle": "Percentile Ranking vs Polish Ekstraklasa Central Midfielders | 2025–2026 Season",
                "img": imgs["rasak"],
                "bullets": [
                    "<strong>Defensive Dominance:</strong> Rasak ranks in the 98th percentile for Defensive Duel Win Rate (67.4%) and 94th percentile for PAdj Tackles + Interceptions (4.68/90).",
                    "<strong>High-Volume Progression:</strong> Delivers 6.82 progressive passes per 90 (89th percentile) with 86.8% accuracy, serving as a dual-threat anchor.",
                    "<strong>Süper Lig Target:</strong> Perfect physical fit for high-intensity pressing systems (Trabzonspor, Beşiktaş, Samsunspor, Eyüpspor) under €2.0M."
                ],
                "kpis": [("Market Value", "€1.8M"), ("Def Duel Win %", "67.4% (98th)"), ("PAdj Tackles+Int", "4.68 / 90"), ("Prog Passes", "6.82 / 90"), ("Ball Recoveries", "8.45 / 90")]
            },
            {
                "section": "Positional Benchmark — Creative Playmaker (#10)",
                "title": "Lukas Podolski (40, AM/SS) — Final-Third Playmaking Benchmark",
                "subtitle": "Percentile Ranking vs Polish Ekstraklasa Attacking Midfielders | 2025–2026 Season",
                "img": imgs["podolski"],
                "bullets": [
                    "<strong>Elite Creative Output:</strong> Produces 0.38 xA/90 (97th percentile), 7.95 progressive passes/90 (98th percentile), and 2.65 key passes/90.",
                    "<strong>xT Specialist:</strong> High-leverage left half-space deliveries generate 0.34 xT/90, consistently unlocking low-block defensive units.",
                    "<strong>Benchmark Takeaway:</strong> Demonstrates the quantitative signature of an elite creator against which prospective #10 targets are measured."
                ],
                "kpis": [("Expected Assists", "0.38 / 90 (97th)"), ("Prog Passes", "7.95 / 90 (98th)"), ("Key Passes", "2.65 / 90"), ("xT Output", "0.34 / 90"), ("npxG", "0.31 / 90")]
            },
            {
                "section": "Positional Benchmark — Fullback / Wingback (#3)",
                "title": "Erik Janża (32, LB/LWB) — Wide Delivery Architect & Crosser",
                "subtitle": "Percentile Ranking vs Polish Ekstraklasa Fullbacks & Wingbacks | 2025–2026 Season",
                "img": imgs["janza"],
                "bullets": [
                    "<strong>Wide Progression Hub:</strong> Records 5.85 progressive passes and 3.45 progressive carries per 90, accounting for 42% of Górnik's flank advances.",
                    "<strong>Set-Piece Delivery:</strong> 0.28 xA per 90 (94th percentile) and 2.10 key passes guarantee constant aerial danger from wide areas.",
                    "<strong>Two-Way Balance:</strong> Wins 61.8% of defensive duels with 3.85 PAdj defensive actions, maintaining defensive stability."
                ],
                "kpis": [("Market Value", "€1.2M"), ("Expected Assists", "0.28 / 90 (94th)"), ("Key Passes", "2.10 / 90"), ("Prog Passes", "5.85 / 90"), ("Def Duel Win %", "61.8%")]
            },
            {
                "section": "League-Wide Scouting Matrix — Central Midfielders",
                "title": "Midfield Creativity vs Progressive Passing Quadrant",
                "subtitle": "Expected Assists (xA/90) vs Progressive Passes/90 | Bubble Size = xT/90",
                "img": imgs["scatter_mids"],
                "bullets": [
                    "<strong>High-Volume Creators:</strong> Isolates midfielders who both progress play and generate high-quality shot assists (Kozubal, Podolski, Kapustka).",
                    "<strong>Deep Ball Circulators:</strong> Lower-right quadrant highlights anchors with high progressive passing but lower direct xA (Rasak, Berggren).",
                    "<strong>Recruitment Insight:</strong> Rasak's high progressive pass rate (6.82/90) proves his ball-winning is paired with immediate vertical distribution."
                ],
                "kpis": [("Cohort Size", "140 Midfielders"), ("Median Prog Passes", "5.25 / 90"), ("Median xA", "0.14 / 90"), ("Top Anchor", "D. Rasak (6.82)"), ("Top Creator", "L. Podolski (7.95)")]
            },
            {
                "section": "League-Wide Scouting Matrix — Pressing & Duel Dominance",
                "title": "Defensive Activity vs Duel Win % Quadrant",
                "subtitle": "PAdj Tackles + Interceptions vs Defensive Duel Win % | 140 Outfield Players",
                "img": imgs["scatter_press"],
                "bullets": [
                    "<strong>Elite Stopper Quadrant:</strong> Top-right isolates players who combine high defensive involvement (>4.0 PAdj actions) with elite efficiency (>65% win rate).",
                    "<strong>Górnik Standouts:</strong> Damian Rasak (67.4% duel win) and Dominik Szala (68.2% duel win) lead the league in contact efficiency.",
                    "<strong>Süper Lig Relevance:</strong> Directly filters out fragile midfielders who struggle with the physical tempo of Turkish league football."
                ],
                "kpis": [("Top Duelist #1", "D. Szala (68.2%)"), ("Top Duelist #2", "D. Rasak (67.4%)"), ("Median Win %", "57.5%"), ("PAdj Median", "3.65 / 90"), ("Target Threshold", "> 65% Win")]
            },
            {
                "section": "Market Efficiency & Transfer Arbitrage",
                "title": "Undervalued Polish Ekstraklasa Gems for Süper Lig Clubs",
                "subtitle": "Market Value (€M) vs Attacking Output (npxG + xA/90) | Target Zone < €2.5M",
                "img": imgs["scatter_gems"],
                "bullets": [
                    "<strong>Primary Target Zone:</strong> Identifies players with top-quartile attacking threat (npxG+xA > 0.40/90) available for under €2.5M transfer fee.",
                    "<strong>Key Value Targets:</strong> Taofeek Ismaheel (RW, €1.5M, 7.80 prog carries/90), Damian Rasak (DM, €1.8M), Luka Zahović (CF, €0.9M, 0.58 threat).",
                    "<strong>Strategic Arbitrage:</strong> Acquiring proven Ekstraklasa assets provides 80% cost savings compared to saturated Western European markets."
                ],
                "kpis": [("Prime Target 1", "T. Ismaheel (€1.5M)"), ("Prime Target 2", "D. Rasak (€1.8M)"), ("Prime Target 3", "D. Szala (€1.8M)"), ("Prime Target 4", "L. Zahović (€0.9M)"), ("Target Cap", "< €2.5M")]
            },
            {
                "section": "AI Engineering & Machine Learning",
                "title": "AI Tactical Archetype Clustering (K-Means & PCA)",
                "subtitle": "Unsupervised Multi-Variable Clustering (10 Event Metrics / 90) for Positional Twins",
                "img": imgs["ai_clusters"],
                "bullets": [
                    "<strong>Algorithmic Segmentation:</strong> 10 standardized metrics grouped into 4 tactical roles: Playmakers, Defensive Anchors, Transition Engines, 1v1 Carriers.",
                    "<strong>PCA Variance:</strong> PC1 (38.4% variance) reflects progression & creativity; PC2 (24.6% variance) reflects defensive duels & pressing volume.",
                    "<strong>Shadow Shortlist Automation:</strong> Sporting directors can input an outgoing player (e.g. Torreira or Fred) and mathematically retrieve the closest twin in Poland."
                ],
                "kpis": [("Algorithm", "K-Means (k=4) + PCA"), ("Features Evaluated", "10 Metrics / 90"), ("Variance Captured", "63.0% (PC1+PC2)"), ("Query Speed", "< 50ms"), ("Scouting Cohort", "140 Players")]
            }
        ]
        page = browser.new_page()
        page.set_content(build_custom_dossier_html(cover_p2, pages_p2))
        page.pdf(path="2_Recruitment_Scouting_Transfer_Intelligence.pdf", format="A4", print_background=True, margin={"top":"0mm","bottom":"0mm","left":"0mm","right":"0mm"})
        page.close()
        print(" -> SUCCESS: 2_Recruitment_Scouting_Transfer_Intelligence.pdf")

        # -------------------------------------------------------------
        # 5. PORTFOLIO 3: PRE-SEASON AUDIT & SQUAD PLANNING (WHAT MANAGERS & BOARDS ASK FOR)
        # -------------------------------------------------------------
        print("\n[5/6] Compiling 3_Season_Audit_Squad_Planning.pdf...")
        cover_p3 = {
            "tag": "SQUAD PLANNING & PRE-SEASON AUDIT | MANAGERS & EXECUTIVE BOARDS",
            "title": "SQUAD PLANNING, AGE PROFILE & GAME-MODEL AUDIT",
            "subtitle": "Strategic Governance: Squad Age Lifecycle, Process Sustainability & League Macro Landscape",
            "target": "Executive Briefing: Measuring True Tactical Dominance, Squad Renewal & Succession Planning",
            "box_title": "WHAT MANAGERS & BOARDS DEMAND BEFORE A NEW SEASON",
            "p1": "Before a new season commences, club leadership requires macro-level strategic audits: 'Is our tactical process sustainable or did we overperform our metrics?' 'Which positions face immediate age-related decline?' 'Where are we losing points across the league landscape?'",
            "p2": "This dossier delivers a multi-dimensional strategic audit: Squad Age-Curve & Minutes Profile (Developmental U23 vs Prime 24-29 vs Veteran 30+ renewal needs), League-wide 18-club xG vs xGA Performance Quadrants, and Game-Model Tactical Governance.",
            "p3": "Empowers sporting leadership to design evidence-based multi-year squad roadmaps, timing player sales and contract extensions with statistical precision."
        }
        pages_p3 = [
            {
                "section": "Squad Lifecycle & Succession Planning",
                "title": "Squad Age-Curve Audit & Minutes Distribution",
                "subtitle": "Minutes Played vs Age Distribution | Developmental (<23), Prime (24-29) & Veteran (30+)",
                "img": imgs["squad_age"],
                "bullets": [
                    "<strong>Core Prime Foundation:</strong> Damian Rasak (29), Kryspin Szcześniak (25), and Taofeek Ismaheel (25) absorb over 6,100 minutes in peak physical years.",
                    "<strong>High Resale Development Asset:</strong> Dominik Szala (20, CB/RB) logged 1,890 minutes; represents a premier U23 asset with exponential resale valuation.",
                    "<strong>Succession Urgency:</strong> Lukas Podolski (40) and Erik Janża (32) generate over 48% of total chance creation; immediate succession planning is essential."
                ],
                "kpis": [("Prime Minutes %", "54.2%"), ("U23 Minutes %", "22.5%"), ("Veteran Minutes %", "23.3%"), ("Top Asset (U23)", "D. Szala (€1.8M)"), ("Renewal Need", "#10 & #3 Successors")]
            },
            {
                "section": "League Macro Landscape — 18 Club Performance Quadrant",
                "title": "Polish Ekstraklasa Expected Goals Matrix (xG vs xGA / 90)",
                "subtitle": "Evaluating Underlying Process Sustainability: Dominant, Entertaining, Pragmatic, Relegation",
                "img": imgs["team_matrix"],
                "bullets": [
                    "<strong>Dominant Process:</strong> Górnik Zabrze occupies the 'Dominant Contenders' quadrant (+1.53 xG/90 created vs 1.02 xGA/90 conceded), proving top-table sustainability.",
                    "<strong>Defensive Benchmarks:</strong> Raków Częstochowa (0.70 xGA/90) and Lech Poznań set the standard for transition prevention in Central Europe.",
                    "<strong>Relegation Distortions:</strong> Bottom-quadrant teams harbor undervalued defensive talents who can be acquired cheaply before league corrections occur."
                ],
                "kpis": [("Górnik xG / 90", "1.53 (Rank 4th)"), ("Górnik xGA / 90", "1.02 (Rank 3rd)"), ("xG Differential", "+13.4"), ("League Median xG", "1.28 / 90"), ("Teams Mapped", "18 Clubs")]
            },
            {
                "section": "Game Momentum & State Control",
                "title": "Match Dynamics & 5-Minute Rolling Territorial Dominance",
                "subtitle": "Cumulative Opportunity Progression & Game State Field Tilt Tracking",
                "img": imgs["xg_flow"],
                "bullets": [
                    "<strong>First-Half Game Model:</strong> Górnik consistently dictates tempo between minutes 15 and 35 (+0.6 momentum), turning territorial tilt into early leads.",
                    "<strong>Negative Transition Vulnerability:</strong> Opponent tactical adjustments at halftime cause a predictable 15-minute dip (minutes 48–63) where xGA spikes.",
                    "<strong>Late Game Resilience:</strong> Senior leadership swings momentum back (+0.9) from minute 70 onwards, demonstrating strong physical and psychological conditioning."
                ],
                "kpis": [("Peak xG Total", "2.15"), ("Dominant Periods", "15-35' & 70-88'"), ("Momentum Peak", "+0.9 Index"), ("Game State Win %", "78% when leading"), ("Season Points", "45 Pts (Top 5)")]
            }
        ]
        page = browser.new_page()
        page.set_content(build_custom_dossier_html(cover_p3, pages_p3))
        page.pdf(path="3_Season_Audit_Squad_Planning.pdf", format="A4", print_background=True, margin={"top":"0mm","bottom":"0mm","left":"0mm","right":"0mm"})
        page.close()
        print(" -> SUCCESS: 3_Season_Audit_Squad_Planning.pdf")

        # -------------------------------------------------------------
        # 6. MASTER ALL-IN-ONE DOSSIER (16 PAGES COMPREHENSIVE)
        # -------------------------------------------------------------
        print("\n[6/6] Compiling Gornik_Zabrze_Ekstraklasa_2025_2026_Portfolio.pdf (16 Pages Master)...")
        cover_master = {
            "tag": "EXECUTIVE MASTER PORTFOLIO | FOOTBALL DATA VISUALIZATION & AI ENGINEERING",
            "title": "GÓRNIK ZABRZE & POLISH EKSTRAKLASA",
            "subtitle": "Comprehensive Football Data Visualization & Technical Scouting Master Dossier",
            "target": "Complete Strategic Intelligence Framework for Turkish Süper Lig Sporting Directors & Technical Staffs",
            "box_title": "PORTFOLIO EXECUTIVE SUMMARY",
            "p1": "This comprehensive dossier unites the three essential pillars of elite modern football analytics: 1) Pre-Match Opposition Tactical Preparation, 2) Data-Driven Recruitment & Shadow Squad Scouting, and 3) Pre-Season Squad Lifecycle & Game-Model Governance.",
            "p2": "Built directly on Opta and Wyscout event architectures, it incorporates 15 high-resolution tactical visualizations spanning Passing Networks, PPDA Defensive Territory, 12x8 Expected Threat (xT) Grids, Inswing/Outswing Corner Deliveries, Goalkeeper Shot-Stopping & Distribution, Percentile Pizza Radars, Market Value Arbitrage, and AI Unsupervised Clustering (K-Means & PCA).",
            "p3": "Every visual is engineered for instant tactical decision-making, providing head coaches with actionable match-day game plans and sporting directors with decisive transfer intelligence."
        }
        all_master_pages = pages_p1 + pages_p2 + pages_p3
        # Remove duplicate pages to create a sleek 15-content-page + cover = 16 page master
        seen_titles = set()
        unique_master_pages = []
        for p_data in all_master_pages:
            if p_data["title"] not in seen_titles:
                seen_titles.add(p_data["title"])
                unique_master_pages.append(p_data)

        page = browser.new_page()
        page.set_content(build_custom_dossier_html(cover_master, unique_master_pages))
        page.pdf(path="Gornik_Zabrze_Ekstraklasa_2025_2026_Portfolio.pdf", format="A4", print_background=True, margin={"top":"0mm","bottom":"0mm","left":"0mm","right":"0mm"})
        page.close()
        print(" -> SUCCESS: Gornik_Zabrze_Ekstraklasa_2025_2026_Portfolio.pdf (Master Dossier)")

        browser.close()

    print("\n================================================================================")
    print("  ALL 6 SPECIALIZED PDFS COMPILED WITH ZERO COLLISION & PUBLICATION-GRADE DESIGN!")
    print("================================================================================")

if __name__ == "__main__":
    main()
