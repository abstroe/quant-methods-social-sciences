import os
import json

NOTEBOOKS_DIR = "notebooks"
OUTPUT_FILE = "r_packages.txt"

def read_existing_packages():
    if not os.path.exists(OUTPUT_FILE):
        return set()
    with open(OUTPUT_FILE, "r") as f:
        return set(line.strip() for line in f if line.strip())

def extract_r_packages():
    packages = set()
    for root, _, files in os.walk(NOTEBOOKS_DIR):
        for file in files:
            if file.endswith(".ipynb"):
                path = os.path.join(root, file)
                with open(path, "r", encoding="utf-8") as f:
                    nb = json.load(f)
                for cell in nb.get("cells", []):
                    if cell.get("cell_type") == "code":
                        src = "".join(cell.get("source", []))
                        for line in src.splitlines():
                            line = line.strip()
                            if line.startswith("library(") or line.startswith("require("):
                                pkg = line.split("(")[1].split(")")[0].strip('\'"')
                                packages.add(pkg)
    return packages

def main():
    existing_pkgs = read_existing_packages()
    new_pkgs = extract_r_packages()

    combined = existing_pkgs.union(new_pkgs)

    with open(OUTPUT_FILE, "w") as f:
        for pkg in sorted(combined):
            f.write(pkg + "\n")

    print(f"Total packages now in {OUTPUT_FILE}: {len(combined)}")

if __name__ == "__main__":
    main()
