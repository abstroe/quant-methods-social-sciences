# Quantitative Methods for Social Sciences

An intensive **12-week study plan** combining **Python** and **R** to master statistical analysis, regression models, Bayesian methods, and causal inference. Designed for **social sciences researchers and data analysts**.

---

## ✅ Features

- **Hands-on Jupyter Notebooks** (Python + R)

- Covers:
  
  - Descriptive & Inferential Statistics
  
  - Linear & Logistic Regression
  
  - Bayesian Modeling (with `brms`)
  
  - Matching & Causal Inference

- **Interactive Exercises**

- **Capstone Project** with real-world datasets

---

## 👋 Onboarding for Students

Welcome! Here's how to get started quickly and smoothly:

1. **Set up your environment**
   
   Follow the [INSTALL.md](INSTALL.md) instructions or the quick setup in this README to install Python, R, and dependencies.

2. **Launch JupyterLab**
   
   Activate the Python virtual environment and start JupyterLab:
   
   ```bash
   source env/bin/activate
   jupyter lab
   ```

3. **Explore Week-by-Week Notebooks**

Go to the `notebooks/` folder. Open the folder for the current week (e.g., `week_01_intro`) and start working through the `.ipynb` notebooks.

4. **Track Your Progress**

```bash
python check_progress.py
```

Run the progress report generator whenever you want to see your learning progress:

5. **Use Additional Resources**
- Refer to `docs/` for the syllabus and reading materials.

- Use helper scripts like `organize_notebooks.py` as needed.
6. **Ask for Help**

If stuck, review this README first. The structure and instructions here cover most questions.

---

## 📦 Installation

Full installation instructions are in [INSTALL.md](INSTALL.md).

Quick setup:

```bash
# Clone the repository
git clone https://github.com/abstroe/quant-methods-social-sciences.git
cd quant-methods-social-sciences

# Python setup
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt

# R packages
Rscript manage_r_packages.R install
```

## ▶️ Usage

### 1. Start JupyterLab

```bash
source env/bin/activate
jupyter lab
```

### 2. Explore Notebooks

- Navigate to the `notebooks/` folder.

- Each week has its own directory:
  
  - `week_01_intro/`
  
  - `week_02_regression/`
  
  - `week_03_bayes/`
  
  - …

- Open and run the `.ipynb` files.

### 3. Check Progress

Generate a visual progress report:

```bash
python check_progress.py
```

Output: progress_report.html

--- 

## 📂 Folder Structure

```bash
quant-methods-social-sciences/
├── data/                 # Sample datasets
├── notebooks/            # Weekly Jupyter notebooks (Python + R)
│   ├── week_01_intro/
│   ├── week_02_regression/
│   └── ...
├── scripts/              # Helper Python scripts
├── capstone_project/     # Final project notebook & files
├── docs/                 # Documentation (syllabus, INSTALL.md)
├── manage_r_packages.R   # R package manager script
├── r_packages.txt        # List of required R packages
├── requirements.txt      # Python dependencies
├── progress_report.html  # Generated progress report
└── .gitignore
```

--- 

## ✅ Notes

- **Update R packages safely**:

```bash
Rscript manage_r_packages.R update
```

    (Interactive mode – choose which packages to update)

* **Optional utilities**:

    -  `organize_notebooks.py` – arrange notebooks by week

    - `check_progress.py` – track completion status

--- 

## 📖 Documentation

See:

- [INSTALL.md](INSTALL.md) — full installation guide

- `docs/` — syllabus and additional references
