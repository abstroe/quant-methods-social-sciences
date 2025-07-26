import os
import shutil

# Source and target directories
src_dir = "notebooks"
week_names = [
    "intro", "data", "visualization", "descriptive_stats", "inference",
    "regression", "logistic", "panel", "time_series", "bayesian",
    "advanced_models", "project"
]

for i, week in enumerate(week_names, start=1):
    # Build folder name like week_01_intro
    week_folder = os.path.join(src_dir, f"week_{i:02d}_{week}")
    os.makedirs(week_folder, exist_ok=True)

    # Move python and r notebooks
    python_src = os.path.join(src_dir, f"week{i:02d}_python.ipynb")
    r_src = os.path.join(src_dir, f"week{i:02d}_r.ipynb")

    python_dest = os.path.join(week_folder, f"{week}_python.ipynb")
    r_dest = os.path.join(week_folder, f"{week}_r.ipynb")

    if os.path.exists(python_src):
        shutil.move(python_src, python_dest)
    if os.path.exists(r_src):
        shutil.move(r_src, r_dest)

print("✅ Notebooks reorganized into week-specific folders.")
