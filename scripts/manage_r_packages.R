#!/usr/bin/env Rscript

args <- commandArgs(trailingOnly = TRUE)

if (length(args) < 1) {
  stop("Usage: Rscript manage_r_packages.R [check|install|update] [--force]")
}

mode <- args[1]
force_update <- "--force" %in% args

pkg_file <- "r_packages.txt"
if (!file.exists(pkg_file)) stop("Package list file not found.")
packages <- readLines(pkg_file)
packages <- packages[nzchar(packages)]

heavy_pkgs <- c("arrow", "brms", "rstan")

# Tracking results
installed <- c()
missing <- c()
updated <- c()
skipped <- c()

check_packages <- function(pkgs) {
  for (pkg in pkgs) {
    if (requireNamespace(pkg, quietly = TRUE)) {
      message("✅ Package '", pkg, "' is installed.")
      installed <<- c(installed, pkg)
    } else {
      message("❌ Package '", pkg, "' is missing.")
      missing <<- c(missing, pkg)
    }
  }
}

install_missing <- function(pkgs) {
  for (pkg in pkgs) {
    if (!requireNamespace(pkg, quietly = TRUE)) {
      message("Installing ", pkg, "...")
      install.packages(pkg, dependencies = TRUE)
      updated <<- c(updated, pkg)
    } else {
      message("Package '", pkg, "' already installed.")
      installed <<- c(installed, pkg)
    }
  }
}

update_packages <- function(pkgs, force = FALSE) {
  for (pkg in pkgs) {
    if (!requireNamespace(pkg, quietly = TRUE)) {
      message("Skipping ", pkg, " (not installed).")
      skipped <<- c(skipped, pkg)
      next
    }

    if (!force && pkg %in% heavy_pkgs) {
      message("⏩ Skipping heavy package: ", pkg)
      skipped <<- c(skipped, pkg)
      next
    }

    ok <- tryCatch({
      suppressMessages(library(pkg, character.only = TRUE))
      TRUE
    }, error = function(e) FALSE)

    if (!ok) {
      if (force) {
        message("⚠ Updating broken package: ", pkg)
        install.packages(pkg, dependencies = TRUE)
        updated <<- c(updated, pkg)
      } else {
        ans <- readline(paste0("Package ", pkg, " is broken. Update now? [y/N]: "))
        if (tolower(ans) == "y") {
          install.packages(pkg, dependencies = TRUE)
          updated <<- c(updated, pkg)
        } else {
          message("Skipped ", pkg)
          skipped <<- c(skipped, pkg)
        }
      }
    } else {
      message("✅ Package '", pkg, "' is OK.")
      installed <<- c(installed, pkg)
    }
  }
}

# Execute mode
if (mode == "check") {
  check_packages(packages)
} else if (mode == "install") {
  install_missing(packages)
} else if (mode == "update") {
  update_packages(packages, force = force_update)
} else {
  stop("Invalid mode. Use one of: check, install, update")
}

# Summary
cat("\n===== SUMMARY =====\n")
cat("Installed: ", length(installed), "\n")
cat("Missing:   ", length(missing), "\n")
cat("Updated:   ", length(updated), "\n")
cat("Skipped:   ", length(skipped), "\n")
cat("====================\n")

# Generate HTML Report
html_file <- "r_packages_report.html"
html <- '<html><head><style>
body { font-family: Arial; margin: 20px; }
h1 { color: #333; }
.table { border-collapse: collapse; width: 100%; }
.table td, .table th { border: 1px solid #ddd; padding: 8px; }
.table th { background-color: #f2f2f2; }
.badge { padding: 4px 8px; border-radius: 4px; color: white; font-weight: bold; }
.green { background-color: #4CAF50; }
.red { background-color: #f44336; }
.yellow { background-color: #ff9800; }
</style></head><body>'
html <- paste0(html, "<h1>R Package Management Report</h1>")
html <- paste0(html, "<p><b>Mode:</b> ", mode, "</p>")
html <- paste0(html, "<table class='table'><tr><th>Status</th><th>Packages</th></tr>")

status_row <- function(label, color, pkgs) {
  if (length(pkgs) == 0) return("")
  paste0("<tr><td><span class='badge ", color, "'>", label, "</span></td><td>", paste(pkgs, collapse=", "), "</td></tr>")
}

html <- paste0(html, status_row("Installed", "green", installed))
html <- paste0(html, status_row("Missing", "red", missing))
html <- paste0(html, status_row("Updated", "yellow", updated))
html <- paste0(html, status_row("Skipped", "yellow", skipped))

html <- paste0(html, "</table></body></html>")
writeLines(html, html_file)

cat("\nHTML report generated: ", html_file, "\n")
browseURL(html_file)
