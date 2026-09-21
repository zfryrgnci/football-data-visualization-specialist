import io
import subprocess
import sys
import time

# Set utf-8 encoding for stdout
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

print("================================================================================")
print("  GORNIK ZABRZE & POLISH EKSTRAKLASA 2025-2026 VISUALIZATION ENGINE")
print("  Developed by Zafer Yorganci | Football Data Visualization Specialist & AI Engineer")
print("================================================================================")

scripts = [
    "data/create_datasets.py",
    "scripts/1_recruitment_scouting.py",
    "scripts/2_tactical_opposition.py",
    "scripts/3_match_performance.py",
    "scripts/4_league_macro_analytics.py"
]

start_time = time.time()
for s in scripts:
    print(f"\n[RUNNING] {s}...")
    res = subprocess.run([sys.executable, s], capture_output=True, text=True, encoding='utf-8')
    if res.returncode != 0:
        print(f"[ERROR in {s}]:\n{res.stderr}")
        sys.exit(1)
    else:
        print(res.stdout.strip())

elapsed = time.time() - start_time
print(f"\n================================================================================")
print(f"  SUCCESS! All 13 High-Resolution 300 DPI Visual Assets generated in {elapsed:.1f}s.")
print(f"  Check the 'visuals/' directory.")
print(f"================================================================================")
