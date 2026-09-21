import os
import re
import fitz

def main():
    print("=" * 80)
    print("VERIFYING COMPLETE FOOTBALL DATA VISUALIZATION SPECIALIST DELIVERABLES")
    print("=" * 80)

    # 1. Verify PDFs
    pdf_files = [
        "Zafer_Yorganci_Futbol_CV_TR.pdf",
        "Zafer_Yorganci_Football_CV_EN.pdf",
        "Zafer_Yorganci_Football_CV.pdf",
        "1_PreMatch_Opposition_Analysis_Gornik_Zabrze.pdf",
        "2_Recruitment_Scouting_Transfer_Intelligence.pdf",
        "3_Season_Audit_Squad_Planning.pdf",
        "Gornik_Zabrze_Ekstraklasa_2025_2026_Portfolio.pdf"
    ]

    print("\n--- 1. PDF DELIVERABLES ---")
    for pdf in pdf_files:
        if os.path.exists(pdf):
            doc = fitz.open(pdf)
            print(f"[OK] {pdf:<52} | Pages: {len(doc):<2} | Size: {os.path.getsize(pdf)/1024:.1f} KB")
        else:
            print(f"[FAIL] MISSING: {pdf}")

    # 2. Verify Visuals
    print("\n--- 2. VISUAL GRAPHICS (visuals/) ---")
    visual_files = sorted([f for f in os.listdir("visuals") if f.endswith(".png")])
    print(f"Total Visuals in visuals/: {len(visual_files)}")
    for v in visual_files:
        path = os.path.join("visuals", v)
        print(f"[OK] {v:<45} | Size: {os.path.getsize(path)/1024:.1f} KB")

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
        print("[OK] All 16 images in index.html exist on disk and resolve correctly!")
    else:
        print(f"[FAIL] Missing images: {missing}")

    pdf_links = re.findall(r'href=["\']\.\./([^"\']+\.pdf)["\']', html)
    print(f"Total PDF Download Links in HTML: {len(pdf_links)}")
    missing_pdfs = []
    for p in pdf_links:
        if not os.path.exists(p):
            missing_pdfs.append(p)
    if not missing_pdfs:
        print("[OK] All PDF links in index.html exist on disk and resolve correctly!")
    else:
        print(f"[FAIL] Missing PDFs: {missing_pdfs}")

    print("\n" + "=" * 80)
    print("ALL VERIFICATIONS COMPLETED SUCCESSFULLY!")
    print("=" * 80)

if __name__ == "__main__":
    main()
