# BiNI analysis workflow

The original BiNI analysis was performed using the BiG-FAM web server
(https://bigfam.bioinformatics.nl/home
).
To replicate this analysis locally, we installed BiG-SLiCE v1.0.0, which uses the same distance framework as BiG-FAM.

Installation

BiG-SLiCE was installed using a Conda-based workflow:

```bash
conda create -n bigslice_3.7 python=3.7 -y
conda activate bigslice_3.7

git clone --branch v1.0.0 https://github.com/medema-group/bigslice.git
cd bigslice
pip install .

# Install dependencies
conda install -c bioconda hmmer=3.3.2
```

Alternatively, BiG-SLiCE can be installed using the provided workflow script:

```
chmod +x workflow.sh
bash workflow.sh
```
Data preparation and clustering

```
antiSMASH results were converted into a BiG-SLiCE-compatible format using a custom preprocessing script:

python scripts/process_antismash.py
```

BiG-SLiCE clustering was then performed using a distance threshold of 900:
```
bigslice -i dataset_1 --complete --threshold 900 output_folder
```
Export of BGC distance results


Cluster distance summaries were exported from the BiG-SLiCE SQLite database:
```
python scripts/export_bigslice_summary.py
```
BiNI calculation
```
python scripts/bini_calculator.py
```

additionally if query is using in BIG-SLiCE then 
```
bigslice --query --n_ranks 1 output_folder

#rank can be 3 or any default is 5, here rank filter top 1 python
export_bigslice_summary_from_query.py
python scripts/bini_calculator.py
```

The Biosynthetic Novelty Index (BiNI) was calculated as described by González-Salazar et al. (2023):

BiNI
=
∑
𝑑
𝑛
BiNI=
n
∑d
	​


Where:

n = total number of BGCs identified by antiSMASH for an isolate

d = BiG-SLiCE (BiG-FAM) distance values

Only d > 900 (novel BGCs) are included in the calculation

python scripts/bini_calculator.py

Query-based analysis (optional)

For query-based comparison against an existing BiG-SLiCE run:

bigslice --query Streptomyces_sp_PB17 --n_ranks 1 output_folder_2


(Here, --n_ranks 1 reports only the closest GCF hit; the default is 5.)

The query results were exported and BiNI recalculated:

python scripts/export_bigslice_summary_from_query.py
python scripts/bini_calculator.py

📌 Citation

The Biosynthetic Novelty Index (BiNI) implemented in this repository follows the methodology described in:

González-Salazar, L. A., Quezada, M., Rodríguez-Orduña, L., Ramos-Aboites, H., Capon, R. J., Souza-Saldívar, V., Barona-Gómez, F., & Licona-Cassani, C. (2023).
Biosynthetic novelty index reveals the metabolic potential of rare actinobacteria isolated from highly oligotrophic sediments.
Microbial Genomics, 9(1).
https://doi.org/10.1099/mgen.0.000921
