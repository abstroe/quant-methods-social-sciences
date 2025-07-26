import os
import shutil

# Directory containing all notebooks
src_dir = "notebooks"

# Week folder name suffixes
week_names = [
    "intro", "data", "visualization", "descriptive_stats", "inference",
    "regression", "logistic", "panel", "time_series", "bayesian",
    "advanced_models", "project"
]

for i, week in enumerate(week_names, start=1):
    week_folder = os.path.join(src_dir, f"week_{i:02d}_{week}")
    os.makedirs(week_folder, exist_ok=True)

    python_src = os.path.join(src_dir, f"week{i:02d}_python.ipynb")
    r_src = os.path.join(src_dir, f"week{i:02d}_r.ipynb")

    python_dest = os.path.join(week_folder, f"{week}_python.ipynb")
    r_dest = os.path.join(week_folder, f"{week}_r.ipynb")

    moved_any = False

    if os.path.exists(python_src):
        shutil.move(python_src, python_dest)
        print(f"Moved {python_src} -> {python_dest}")
        moved_any = True
    else:
        print(f"Missing {python_src}, skipping.")

    if os.path.exists(r_src):
        shutil.move(r_src, r_dest)
        print(f"Moved {r_src} -> {r_dest}")
        moved_any = True
    else:
        print(f"Missing {r_src}, skipping.")

    if not moved_any:
        print(f"No notebooks moved for week {i}: {week}")

print("✅ Notebooks reorganized into week-specific folders.")
