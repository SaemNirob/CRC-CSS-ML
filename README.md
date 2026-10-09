# Explainable Machine Learning for 36-Month Cancer-Specific Survival Prediction in Colorectal Cancer

## Research objective

This repository contains the reproducible implementation of an explainable and uncertainty-aware machine learning pipeline for predicting 36-month cancer-specific survival among patients with colorectal cancer.

## Dataset

The analysis uses the original study cohort and preserves the original cohort definition, inclusion/exclusion criteria, feature construction, and temporal validation strategy.

## Methodology

The pipeline includes:

1. Cohort preparation and clinical feature extraction
2. Missing value handling and preprocessing
3. Machine learning model development
4. Probability calibration
5. Performance evaluation
6. Explainability analysis using SHAP
7. Calibration and uncertainty analyses
8. Sensitivity analyses

The implemented models and statistical methods are identical to those reported in the manuscript.

## Repository structure

```
src/              Reusable analysis modules
notebooks/        Reproducible analysis notebook
results/          Generated figures and tables
```

## Installation

```bash
pip install -r requirements.txt
```

## Reproducibility

Run:

```bash
jupyter notebook notebooks/CRC_CSS_analysis.ipynb
```

The analysis maintains the original random seeds, train-test split, preprocessing pipeline, model parameters, and evaluation framework.

## Citation

If you use this repository, please cite the associated manuscript.
