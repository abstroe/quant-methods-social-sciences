# Scripts Directory

This folder contains utility scripts for managing the **Quantitative Methods for Social Sciences** project environment, organizing notebooks, and tracking progress.

---

## 📂 Scripts Overview

| Script                              | Description                                                                                           |
| ----------------------------------- | ----------------------------------------------------------------------------------------------------- |
| **check_progress.py**               | Scans all weekly notebooks, calculates completion percentages, and generates an HTML progress report. |
| **organize_notebooks.py**           | Reorganizes notebooks into week-specific folders (e.g., `week_01_intro`).                             |
| **prefill_notebooks.py**            | Adds a standard header and starter cells (Markdown + code) to empty notebooks.                        |
| **list_R_packages_in_notebooks.py** | Extracts R package references from R notebooks for dependency management.                             |
| **manage_r_packages.R**             | Checks, installs, or updates R packages listed in `r_packages.txt`. Generates an HTML report.         |
| **setup_project.py**                | Creates initial project folder structure, starter files, and configuration.                           |

---

## ✅ How to Use Each Script

### 1. **Check Course Progress**

Generates a color-coded HTML report (`progress_report.html`):

```bash
python scripts/check_progress.py
```

---

### 2. **Organize Notebooks**

Reorganizes notebooks into `notebooks/week_##_topic/` structure:

```bash
python scripts/organize_notebooks.py
```

---

### 3. **Prefill Notebooks**

Adds a standard template to notebooks (learning objectives + starter code):

```bash
python scripts/prefill_notebooks.py
```

---

### 4. **List R Packages in Notebooks**

Scans all `.ipynb` files for `library()` calls and lists unique R packages:

```bash
python scripts/list_R_packages_in_notebooks.py
```

---

### 5. **Manage R Packages**

Manages R dependencies defined in `r_packages.txt`:

```bash
# Check installed/missing packages
Rscript scripts/manage_r_packages.R check

# Install missing packages
Rscript scripts/manage_r_packages.R install

# Update packages (skip heavy ones)
Rscript scripts/manage_r_packages.R update

# Force update all (including heavy packages)
Rscript scripts/manage_r_packages.R update --force
```

Generates an HTML report: `r_packages_report.html`.

---

### 6. **Setup Project**

Initializes the project folder structure and starter files (use only for first setup):

```bash
python scripts/setup_project.py
```

---

## 🔍 Notes

- All scripts assume they are executed from the **project root** directory.
- R scripts require **R ≥ 4.2** and `repos="https://cloud.r-project.org"` is used for package installation.
- Python scripts require dependencies listed in `requirements.txt`.
