import nbformat
from pathlib import Path

# Get the path to the scripts folder (where this script lives)
scripts_dir = Path(__file__).parent.resolve()

# Define notebooks directory relative to scripts folder
notebooks_dir = scripts_dir.parent / "notebooks"

for notebook in sorted(notebooks_dir.glob("week*_*.ipynb")):
    # Extract week number with space, e.g. "Week 01"
    parts = notebook.stem.split("_")
    week_num = parts[0]  # like 'week01'
    week_name = f"Week {week_num[-2:]}"  # take last two chars, e.g. '01'

    lang = "Python" if "python" in notebook.stem else "R"

    nb = nbformat.v4.new_notebook()

    # Markdown header
    header = f"# {week_name} – {lang}\n\n" \
             "## Learning Objectives\n" \
             "- [ ] Add objectives here\n\n" \
             "## References\n" \
             "- Add links to resources for this week\n"

    # Starter code cell
    starter_code = "# Your code starts here\n" if lang == "Python" else "# R code starts here\n"

    nb.cells = [
        nbformat.v4.new_markdown_cell(header),
        nbformat.v4.new_code_cell(starter_code)
    ]

    # Write notebook
    nbformat.write(nb, notebook)

print("✅ All notebooks pre-filled successfully!")
