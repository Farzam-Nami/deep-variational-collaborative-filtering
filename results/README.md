# Experimental Results

This directory contains the result artifacts produced by the executed notebook.

## Combined tables

- `rating-metrics-all-datasets.csv`: MAE, MSE, and R² for all four models on both datasets.
- `ranking-metrics-all-datasets.csv`: Precision, Recall, F1, Novelty, and nDCG for recommendation cutoffs N = 2 through N = 10.

## Dataset-specific tables

- `ft-rating-metrics.csv`
- `ft-ranking-metrics.csv`
- `ml1m-rating-metrics.csv`
- `ml1m-ranking-metrics.csv`

## Figures

Each dataset has four figures:

- Precision–Recall
- F1 versus recommendation length
- Novelty versus recommendation length
- nDCG versus recommendation length

The notebook regenerates these CSV files and figures when all cells are executed successfully from the repository root.
