# Makefile for Quantitative Methods Study Project

# Create Python virtual environment and install packages
setup:
	python3 -m venv env && bash -c "source env/bin/activate && pip install -r requirements.txt"

# Install R packages to user library
# Note: This command creates ~/R/libs if it doesn't exist and installs packages there
setup-r:
	Rscript -e '.libPaths("~/R/libs"); dir.create("~/R/libs", showWarnings=FALSE, recursive=TRUE); install.packages(setdiff(readLines("r_packages.txt"), installed.packages()[,"Package"]), repos="https://cloud.r-project.org")'

# Generate syllabus as a PDF from Markdown
syllabus-pdf:
	pandoc docs/syllabus.md -o docs/syllabus.pdf --toc --standalone

# Update README.md with Google Colab badges for notebooks
update-colab-badges:
	python scripts/generate_colab_links.py --username abstroe --repo quant-methods-social-sciences

# Optional: Docker build and run targets (if Dockerfile exists)
docker-build:
	docker build -t quant-methods-image .

docker-run:
	docker run -it --rm -v $(PWD):/workspace -p 8888:8888 quant-methods-image

