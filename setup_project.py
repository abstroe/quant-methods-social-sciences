import os
from pathlib import Path
import json

# Config
USERNAME = "abstroe"
REPO = "quant-methods-social-sciences"

# Folders to create
folders = [
    "data", "docs", "env", "notebooks", "scripts", "results",
    "capstone_project", ".devcontainer", ".github/workflows"
]

# Files and their content
files_content = {
    ".gitignore": """__pycache__/
*.pyc
.ipynb_checkpoints
env/
.Rhistory
.RData
.Rproj.user/
.DS_Store
Thumbs.db
*.pdf
results/
""",

    "README.md": f"""# Quantitative Methods for Social Sciences

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

For more details, see [INSTALL.md](docs/INSTALL.md).
""",

    "Makefile": """setup:
\tpython3 -m venv env && source env/bin/activate && pip install -r requirements.txt

setup-r:
\tRscript -e '.libPaths("~/R/libs"); dir.create("~/R/libs", showWarnings=FALSE, recursive=TRUE); install.packages(setdiff(readLines("r_packages.txt"), installed.packages()[,"Package"]), repos="https://cloud.r-project.org")'

syllabus-pdf:
\tpandoc docs/syllabus.md -o docs/syllabus.pdf --toc --standalone

update-colab-badges:
\tpython scripts/generate_colab_links.py --username abstroe --repo quant-methods-social-sciences
""",

    "requirements.txt": """pandas
numpy
matplotlib
seaborn
scikit-learn
statsmodels
pymc
jupyter
notebook
linearmodels
""",

    "r_packages.txt": """tidyverse
brms
rstan
MatchIt
fixest
rvest
""",
}

# Create folders
for folder in folders:
    Path(folder).mkdir(parents=True, exist_ok=True)

# Write files
for filename, content in files_content.items():
    Path(filename).write_text(content.strip() + "\n")

# Function to create a minimal Python notebook template
def create_python_notebook(title, tasks):
    nb = {
        "cells": [
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": [f"# {title}\n\nThis notebook covers:\n"] + [f"- {task}\n" for task in tasks]
            },
            {
                "cell_type": "code",
                "execution_count": None,
                "metadata": {},
                "outputs": [],
                "source": [
                    "import pandas as pd\n",
                    "import numpy as np\n",
                    "import matplotlib.pyplot as plt\n",
                    "import seaborn as sns\n",
                    "\n# Your code starts here\n"
                ]
            }
        ],
        "metadata": {
            "kernelspec": {
                "display_name": "Python 3",
                "language": "python",
                "name": "python3"
            }
        },
        "nbformat": 4,
        "nbformat_minor": 5
    }
    return nb

# Create starter notebooks for Week 1 Python and save
week1_tasks = ["Descriptive Statistics", "Data Loading", "Basic Visualization"]
week1_py_nb = create_python_notebook("Week 1 - Python", week1_tasks)
with open("notebooks/week01_python.ipynb", "w") as f:
    json.dump(week1_py_nb, f, indent=2)

print("Project structure created successfully!")
print("Folders, key files, and starter notebooks are ready.")
print("Run 'make setup' to initialize Python environment and install packages.")
print("Run 'make setup-r' to install R packages.")
