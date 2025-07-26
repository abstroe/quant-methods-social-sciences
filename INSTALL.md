# Installation Guide

This guide explains how to set up the environment for the **Quantitative Methods for Social Sciences** project on **Linux (Debian/Ubuntu)**.


## 1. Clone the Repository

```bash
git clone https://github.com/abstroe/quant-methods-social-sciences.git
cd quant-methods-social-sciences
```

## 2. System Requirements

Install system dependencies required by Python, R, and Arrow:

```bash
sudo apt update
sudo apt install -y \
    build-essential \
    cmake \
    libcurl4-openssl-dev \
    libssl-dev \
    libxml2-dev \
    libfontconfig1-dev \
    libharfbuzz-dev \
    libfribidi-dev \
    libfreetype6-dev \
    libpng-dev \
    libtiff5-dev \
    libjpeg-dev \
    pandoc \
    zlib1g-dev \
    libbz2-dev \
    liblzma-dev \
    git
```

## 3. Python Environment Setup

Create and activate a virtual environment, then install dependencies:

```bash
python3 -m venv env
source env/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

## 4. R Setup

Ensure you have R ≥ 4.2 installed. Then run:

```bash
Rscript manage_r_packages.R install
```

This script:
- Reads `r_packages.txt`
- Installs any missing packages automatically
- Skips packages already installed

## 5. Jupyter & Notebooks

If you want to run notebooks:

```bash
pip install notebook jupyterlab
```

Then start JupyterLab:

```bash
jupyter lab
```

## 6. Optional: Check Progress

To generate a progress report (HTML + Markdown):

```bash
python check_progress.py
```

The script:
- Scans notebooks by week
- Generates color-coded progress bars in `progress_report.html`

## ✅ Notes

- **Arrow Package**: If needed later, check the Arrow R Installation Guide.
- **Update R Packages**: Run `Rscript manage_r_packages.R update` (interactive, safe mode).
- **Organize Notebooks**: Use `organize_notebooks.py` for weekly folder structure.

## Quick Start

1. Clone repo
2. `python3 -m venv env && source env/bin/activate`
3. `pip install -r requirements.txt`
4. `Rscript manage_r_packages.R install`
5. `jupyter lab

