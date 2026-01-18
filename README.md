# BiG-SLiCE–BiNI Pipeline

This repository provides a reproducible workflow to assess the biosynthetic novelty of microbial genomes using **BiG-SLiCE** and the **Biosynthetic Novelty Index (BiNI)**. following González-Salazar et al., 2023: methods


# BiNI-Analyser

For BiNI analyse auther used this server https://bigfam.bioinformatics.nl/home
so to replicate we have installed BiG-SLiCE software (1.0.0) 
it can be installed using 
chmod +x workflow.sh
bash workflow.sh
or conda installation 
conda env create -f environment.yml
conda activate bigslice_3.7



once installation done download antiSMASH results 
python scripts/process_antismash.py
bigslice -i <processed antismash>  --threshold 900 --n_ranks 3 output_folder
python scripts/export_bigslice_summary.py
python scripts/bini_calculator.py


additionally if query is using BIG-SLiCE
bigslice --query <processed antismash> --n_ranks 1 output_folder
#rank can be 3 or any default is 5, here rank filter top 1

python export_bigslice_summary_from_query.py
python scripts/bini_calculator.py
python scripts/bini_calculator.py




From González-Salazar et al., 2023:

BiNI = Σd / n

Where:

n = number of BGCs identified by antiSMASH for an isolate

d = BiG-FAM / BiG-SLiCE distance values

Only distances > 900 are considered (novel BGCs)


## Citation

The Biosynthetic Novelty Index (BiNI) implemented in this repository follows the
methodology described in:

González-Salazar, L. A., Quezada, M., Rodríguez-Orduña, L., Ramos-Aboites, H., Capon, R. J., Souza-Saldívar, V., Barona-Gómez, F., & Licona-Cassani, C. (2023).
**Biosynthetic novelty index reveals the metabolic potential of rare actinobacteria isolated from highly oligotrophic sediments.** Microbial Genomics, 9(1).
https://doi.org/10.1099/mgen.0.000921
