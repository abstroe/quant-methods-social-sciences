# Makefile for Quantitative Methods Study Project

# Create Python virtual environment and install packages
setup:
	python3 -m venv env && bash -c "source env/bin/activate && pip install -r requirements.txt"

# Install R packages to user library
setup-r:
	Rscript -e '.libPaths("~/R/libs"); dir.create("~/R/libs", showWarnings=FALSE, recursive=TRUE); install.packages(setdiff(readLines("r_packages.txt"), installed.packages()[,"Package"]), repos="https://cloud.r-project.org")'

# Generate syllabus as a PDF from Markdown
syllabus-pdf:
	pandoc docs/syllabus.md -o docs/syllabus.pdf --toc --standalone

# Generate all lecture notes PDFs
DOCS_DIR = docs
LECTURE_MD = $(wildcard $(DOCS_DIR)/week_*_lecture_notes.md)
LECTURE_PDF = $(LECTURE_MD:.md=.pdf)

pdf-lecture: $(LECTURE_PDF)

$(DOCS_DIR)/%.pdf: $(DOCS_DIR)/%.md
	pandoc $< \
	  -o $@ \
	  --toc \
	  --standalone \
	  -V geometry:margin=1in \
	  -V urlcolor=blue \
	  -V colorlinks=true \
	  -V fontsize=11pt \
	  --pdf-engine=pdflatex

# Generate all PDFs (syllabus + lecture notes)
pdf-all: syllabus-pdf pdf-lecture
	@echo "✅ All PDFs generated in $(DOCS_DIR)"

# Update README.md with Google Colab badges for notebooks
update-colab-badges:
	python scripts/generate_colab_links.py --username abstroe --repo quant-methods-social-sciences

# Optional: Docker build and run targets
docker-build:
	docker build -t quant-methods-image .

docker-run:
	docker run -it --rm -v $(PWD):/workspace -p 8888:8888 quant-methods-image

