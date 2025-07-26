# Quantitative Methods for Social Sciences

An intensive **12-week program** blending **Python** and **R** for statistical analysis, regression, Bayesian modeling, and causal inference — designed for **social science researchers and data analysts**.

---

## 🚀 What You'll Learn
- Descriptive & Inferential Statistics
- Linear & Logistic Regression
- Bayesian Methods (`brms`, `rstan`)
- Matching & Causal Inference
- Data Visualization & Exploration
- Capstone Project using real-world data

---

## 📂 Repository Structure

quant-methods-social-sciences/
├── data/                 # Sample datasets
├── notebooks/            # Weekly Jupyter notebooks (Python + R)
│   ├── week_01_intro/
│   ├── week_02_regression/
│   └── ...
├── scripts/              # Utility scripts for setup & progress tracking
├── capstone_project/     # Final project files
├── docs/                 # Syllabus & lecture notes
├── requirements.txt      # Python dependencies
├── r_packages.txt        # R packages
└── .gitignore


---

## ✅ Quick Start

### 1. Clone the Repository
```bash
git clone https://github.com/abstroe/quant-methods-social-sciences.git
cd quant-methods-social-sciences
```

### 2. Set Up Python Environment

```python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
```

### 3. Install R Packages

```
Rscript scripts/manage_r_packages.R install
```

---

## ▶️  Usage

### Launch JupyterLab

```source env/bin/activate
source env/bin/activate
jupyter lab
```

Open notebooks/week_01_intro/ to begin.

---

## 📈 Track Progress

Generate an HTML progress report:

``` python scripts/check_progress.py 
python scripts/check_progress.py
```

Output: progress_report.html (in /scripts)

---

## 📖 Documentation

* [INSTALL.md](INSTALL.md) — detailed installation guide
*  In docs/` — syllabus ([PDF](docs/quant_methods_social_sciences_syllabus.pdf)), lecture notes, and resources

---

## 🔍 Notes

- Run scripts from the **project root**.
- Use `make` for common tasks:

```make setup         # Python environment
make setup         # Python environment
make setup-r       # R packages
make syllabus-pdf  # Generate syllabus PDF
make notes-pdf     # Generate all lecture notes PDFs
```

