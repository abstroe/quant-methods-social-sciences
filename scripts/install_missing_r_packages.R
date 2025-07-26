# Resolve conflicts if conflicted is installed
if ("conflicted" %in% rownames(installed.packages())) {
  suppressMessages(library(conflicted))
  conflicts_prefer(base::`%in%`)
}

pkg_file <- "r_packages.txt"
if (!file.exists(pkg_file)) stop("Package list file not found.")

packages <- readLines(pkg_file)
packages <- packages[nzchar(packages)]

for (pkg in packages) {
  if (!requireNamespace(pkg, quietly = TRUE)) {
    message("Installing package: ", pkg)
    install.packages(pkg, dependencies = TRUE)
  } else {
    message("Package '", pkg, "' already installed.")
  }
}
