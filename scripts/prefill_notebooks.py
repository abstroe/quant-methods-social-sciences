import nbformat
from pathlib import Path

# Path to notebooks folder
notebooks_dir = Path.home() / "quant_meth" / "notebooks"

for notebook in sorted(notebooks_dir.glob("week*_*.ipynb")):
    week_name = notebook.stem.split("_")[0].capitalize()  # e.g., Week01
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

