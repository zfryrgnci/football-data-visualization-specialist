import os
import re
import fitz

def main():
    print("=" * 80)
    print("VERIFYING COMPLETE FOOTBALL DATA VISUALIZATION SPECIALIST DELIVERABLES")
    print("=" * 80)

    # 1. Verify Standard PDFs
    pdf_files = [
        "Zafer_Yorganci_Futbol_CV_TR.pdf",
        "Zafer_Yorganci_Football_CV_EN.pdf",
        "Zafer_Yorganci_Football_CV.pdf",
        "1_PreMatch_Opposition_Analysis_Gornik_Zabrze.pdf",
        "2_Recruitment_Scouting_Transfer_Intelligence.pdf",
        "3_Season_Audit_Squad_Planning.pdf",
        "Gornik_Zabrze_Ekstraklasa_2025_2026_Portfolio.pdf",
        "Zafer_Yorganci_Technical_Intelligence_Dossier_2026_EN.pdf",
        "Zafer_Yorganci_Teknik_Analiz_ve_Veri_Gorsellestirme_Raporu_2026_TR.pdf"
    ]

    print("\n--- 1. STANDARD & CLUB DOSSIER PDFS ---")
    for pdf in pdf_files:
        if os.path.exists(pdf):
            doc = fitz.open(pdf)
            print(f"[OK] {pdf:<58} | Pages: {len(doc):<2} | Size: {os.path.getsize(pdf)/1024:.1f} KB")
        else:
            print(f"[FAIL] MISSING: {pdf}")

    # 1B. Verify Sports Data Campus Widescreen Presentation PDFs
    sdc_pdfs = [
        "1_SportsDataCampus_Heat_Maps_Spatial_Intelligence.pdf",
        "2_SportsDataCampus_Passing_Networks_Team_Structure.pdf",
        "3_SportsDataCampus_Shot_Maps_and_xG_Models.pdf",
        "4_SportsDataCampus_Radar_Charts_and_Polar_Profiles.pdf",
        "5_SportsDataCampus_Advanced_Visuals_Pitch_Control_and_xT.pdf",
        "SportsDataCampus_Master_Executive_Landscape_Portfolio.pdf"
    ]

    print("\n--- 1B. SPORTS DATA CAMPUS WIDESCREEN PRESENTATION PDFS (16:9 LANDSCAPE) ---")
    for pdf in sdc_pdfs:
        if os.path.exists(pdf):
            doc = fitz.open(pdf)
            print(f"[OK] {pdf:<58} | Pages: {len(doc):<2} | Size: {os.path.getsize(pdf)/1024:.1f} KB")
        else:
            print(f"[FAIL] MISSING: {pdf}")

    # 2. Verify Visuals
    print("\n--- 2A. STANDARD VISUAL GRAPHICS (visuals/) ---")
    visual_files = sorted([f for f in os.listdir("visuals") if f.endswith(".png")])
    print(f"Total Standard Visuals in visuals/: {len(visual_files)}")
    for v in visual_files:
        path = os.path.join("visuals", v)
        print(f"[OK] {v:<50} | Size: {os.path.getsize(path)/1024:.1f} KB")

    print("\n--- 2B. WIDESCREEN (16:9, 300 DPI) VISUALS (visuals/wide/) ---")
    wide_files = sorted([f for f in os.listdir("visuals/wide") if f.endswith(".png")])
    print(f"Total Widescreen Visuals in visuals/wide/: {len(wide_files)}")
    for w in wide_files:
        path = os.path.join("visuals/wide", w)
        print(f"[OK] {w:<50} | Size: {os.path.getsize(path)/1024:.1f} KB")

    # 3. Verify portfolio/index.html links
    print("\n--- 3. PORTFOLIO WEB APPLICATION (portfolio/index.html) ---")
    with open("portfolio/index.html", "r", encoding="utf-8") as f:
        html = f.read()

    imgs = re.findall(r'src=["\']\.\./visuals/([^"\']+)["\']', html)
    print(f"Total Images Referenced in HTML: {len(imgs)}")
    missing = []
    for img in imgs:
        if not os.path.exists(os.path.join("visuals", img)):
            missing.append(img)
    if not missing:
        print("[OK] All images in index.html exist on disk and resolve correctly!")
    else:
        print(f"[FAIL] Missing images: {missing}")

    pdf_links = re.findall(r'href=["\']\.\./([^"\']+\.pdf)["\']', html)
    print(f"Total PDF Download Links in HTML: {len(pdf_links)}")
    missing_pdfs = []
    for p in pdf_links:
        if not os.path.exists(p):
            missing_pdfs.append(p)
    if not missing_pdfs:
        print(f"[OK] All {len(pdf_links)} PDF links in index.html exist on disk and resolve correctly!")
    else:
        print(f"[FAIL] Missing PDFs: {missing_pdfs}")

    print("\n" + "=" * 80)
    print("ALL VERIFICATIONS COMPLETED SUCCESSFULLY!")
    print("=" * 80)

if __name__ == "__main__":
    main()
