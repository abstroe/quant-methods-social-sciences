# Quantitative Methods for Social Sciences

An intensive 12-week study plan combining Python and R for statistics, regression, Bayesian methods, and causal inference.

## How to Start

    make setup

---

## Repository Structure

- `data/` — sample datasets  
- `notebooks/` — Jupyter notebooks (Python and R) for each week  
- `scripts/` — helper Python scripts  
- `capstone_project/` — final project notebook and related files  
- `env/` — Python virtual environment (after setup)  
- `docs/` — documentation and syllabus PDF  
- `.devcontainer/` — VS Code devcontainer config for Docker  
- `.github/workflows/` — GitHub Actions workflows  

---

## Setup Instructions

- Install Python 3.8+ and R (if not installed).  
- Run:

    make setup         # Python environment and packages
    make setup-r       # R packages

- To generate the syllabus PDF:

    make syllabus-pdf

- To update Colab badges in README:

    make update-colab-badges

---

For more details, see [Installation Guide](INSTALL.md). 

