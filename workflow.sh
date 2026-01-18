#!/usr/bin/env bash

# Create environment
conda create -n bigslice_3.7 python=3.7 -y
conda activate bigslice_3.7

# Install BiG-SLiCE
git clone --branch v1.0.0 https://github.com/medema-group/bigslice.git
cd bigslice
pip install .

# Install HMMER
conda install -c bioconda hmmer=3.3.2 -y

# Check installation
bigslice --version
bigslice --help
which hmmscan

# Download models
download_bigslice_hmmdb.py
