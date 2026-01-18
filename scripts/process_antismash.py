#!/usr/bin/env python3
"""
Prepare antiSMASH 5 compatible dataset for BiG-SLiCE
- Extract zip
- Convert antiSMASH 8 → 5
- Create BiG-SLiCE dataset structure
- Create datasets.tsv and taxonomy file
"""

import os
import zipfile
import shutil

# =====================
# USER SETTINGS
# =====================
ZIP_FILE = "Streptomyces_sp_PB17.zip"

MASTER_DIR = "Streptomyces_sp_PB17"
DATASET_NAME = MASTER_DIR
GENOME_NAME = "Streptomyces_sp_PB17"

OLD_VERSION = "Version     :: 8.0.4"
NEW_VERSION = "Version     :: 5.0.0"

# =====================
# PATHS
# =====================
EXTRACT_DIR = "tmp_extract"

DATASET_DIR = os.path.join(
    MASTER_DIR,
    DATASET_NAME,
    GENOME_NAME
)

TAXONOMY_DIR = os.path.join(MASTER_DIR, "taxonomy")

DATASETS_TSV = os.path.join(MASTER_DIR, "datasets.tsv")

TAXONOMY_TSV = os.path.join(
    TAXONOMY_DIR,
    f"{DATASET_NAME}_taxonomy.tsv"
)

# =====================
# TAXONOMY (EDIT IF NEEDED)
# =====================
TAXONOMY_LINE = (
    f"{GENOME_NAME}/\tBacteria\tActinobacteria\t"
    "Actinobacteria (high G+C)\tStreptomycetales\t"
    "Streptomycetaceae\tStreptomyces\t"
    "Streptomyces coelicolor\tStreptomyces coelicolor A3(2)\n"
)

# =====================
# FUNCTIONS
# =====================
def extract_zip():
    if os.path.exists(EXTRACT_DIR):
        shutil.rmtree(EXTRACT_DIR)

    print(f"📦 Extracting {ZIP_FILE}")
    with zipfile.ZipFile(ZIP_FILE, "r") as z:
        z.extractall(EXTRACT_DIR)


def setup_folders():
    print("📁 Creating BiG-SLiCE folder structure")

    if os.path.exists(MASTER_DIR):
        shutil.rmtree(MASTER_DIR)

    os.makedirs(DATASET_DIR, exist_ok=True)
    os.makedirs(TAXONOMY_DIR, exist_ok=True)


def convert_and_copy_gbk():
    converted = 0

    for root, _, files in os.walk(EXTRACT_DIR):
        for file in files:
            if not file.endswith(".gbk"):
                continue

            src = os.path.join(root, file)
            rel = os.path.relpath(src, EXTRACT_DIR)
            dst = os.path.join(DATASET_DIR, rel)

            os.makedirs(os.path.dirname(dst), exist_ok=True)

            with open(src, "r", encoding="utf-8", errors="ignore") as f:
                content = f.read()

            if OLD_VERSION in content:
                content = content.replace(OLD_VERSION, NEW_VERSION)
                converted += 1

            with open(dst, "w", encoding="utf-8") as f:
                f.write(content)

    print(f"✅ Converted {converted} GBK files")


def write_datasets_tsv():
    print("📝 Writing datasets.tsv")

    with open(DATASETS_TSV, "w") as f:
        f.write("# Dataset name\tPath to folder\tPath to taxonomy\tDescription\n")
        f.write(
            f"{DATASET_NAME}\t{DATASET_NAME}/\t"
            f"taxonomy/{DATASET_NAME}_taxonomy.tsv\t"
            "Converted antiSMASH5 dataset\n"
        )


def write_taxonomy():
    print("🧬 Writing taxonomy file")

    with open(TAXONOMY_TSV, "w") as f:
        f.write(
            "# Genome folder\tKingdom\tPhylum\tClass\tOrder\tFamily\tGenus\tSpecies\tOrganism\n"
        )
        f.write(TAXONOMY_LINE)


def cleanup():
    shutil.rmtree(EXTRACT_DIR)


# =====================
# MAIN
# =====================
if __name__ == "__main__":
    extract_zip()
    setup_folders()
    convert_and_copy_gbk()
    write_datasets_tsv()
    write_taxonomy()
    cleanup()

    print("\n🎉 DONE SUCCESSFULLY!")
    print(f"📂 Final folder: {MASTER_DIR}")
    print(f"🚀 Run BiG-SLiCE with:\n   bigslice -i {DATASET_NAME} output_folder")
