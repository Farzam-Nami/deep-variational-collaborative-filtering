# Deep Variational Models for Collaborative Filtering-Based Recommender Systems

This repository contains a Jupyter Notebook implementation and experimental comparison of four collaborative-filtering models on FilmTrust and MovieLens 1M:

- **DeepMF** — user and item embeddings combined through an inner product.
- **NCF** — user and item embeddings combined through a multilayer perceptron.
- **VDeepMF** — DeepMF with Gaussian variational latent sampling.
- **VNCF** — NCF with Gaussian variational latent sampling.

The notebook processes both datasets in one execution, trains all four models on each dataset, evaluates rating prediction and Top-N recommendation quality, and saves combined result tables and figures.

## Repository structure

```text
deep-variational-collaborative-filtering/
├── Deep_Variational_Recommender.ipynb
├── datasets/
│   ├── ft.csv
│   ├── prepare_movielens.py
│   └── README.md
├── results/
│   ├── ft-rating-metrics.csv
│   ├── ft-ranking-metrics.csv
│   ├── ml1m-rating-metrics.csv
│   ├── ml1m-ranking-metrics.csv
│   ├── rating-metrics-all-datasets.csv
│   ├── ranking-metrics-all-datasets.csv
│   └── [eight evaluation figures]
├── requirements.txt
└── .gitignore
```

The FilmTrust dataset and all result artifacts are included. The MovieLens 1M data file is not redistributed in this public repository; download it from GroupLens and prepare it locally as described below.

## Datasets

| Dataset | Users | Items | Ratings used | Rating range | Sparsity |
|---|---:|---:|---:|---:|---:|
| FilmTrust | 1,508 | 2,071 | 35,494 | 0.5–4.0 | 98.86% |
| MovieLens 1M | 6,040 | 3,706 | 1,000,209 | 1.0–5.0 | 95.53% |

Sparsity is calculated as:

`1 - (number of observed ratings / (number of users × number of items))`.

### FilmTrust

The processed FilmTrust ratings file is available at `datasets/ft.csv`. It has the columns `user`, `item`, and `rating`. The file contains 35,494 rows. The LibRec dataset page describes the source collection as containing 35,497 ratings; the count in this repository refers to the supplied processed CSV.

Source: https://guoguibing.github.io/librec/datasets.html

Please cite the FilmTrust dataset paper:

Guo, G., Zhang, J., & Yorke-Smith, N. (2013). A Novel Bayesian Similarity Measure for Recommender Systems. Proceedings of the 23rd International Joint Conference on Artificial Intelligence (IJCAI), 2619–2625.

### MovieLens 1M

Download MovieLens 1M from the official GroupLens page:

https://grouplens.org/datasets/movielens/1m/

GroupLens generally does not permit public redistribution of MovieLens datasets without separate permission. For that reason, `ml1m.csv` is excluded from this public repository. The `datasets/prepare_movielens.py` helper converts the official `ratings.dat` file to the three-column format required by the notebook.

After downloading and extracting MovieLens 1M, run:

```bash
python datasets/prepare_movielens.py /path/to/ml-1m/ratings.dat
```

The script creates `datasets/ml1m.csv`. This local file is ignored by Git. Keep it in place when running the notebook, but do not commit it to a public repository unless you have obtained the required redistribution permission.

Please cite:

Harper, F. M., & Konstan, J. A. (2015). The MovieLens Datasets: History and Context. ACM Transactions on Interactive Intelligent Systems, 5(4), Article 19. https://doi.org/10.1145/2827872

Do not imply endorsement by the University of Minnesota or GroupLens Research.

## Installation

Python 3.10–3.12 is recommended. Create and activate a virtual environment, then install the dependencies:

```bash
python -m venv .venv
```

Windows:

```powershell
.venv\Scripts\activate
```

macOS / Linux:

```bash
source .venv/bin/activate
```

Install packages:

```bash
pip install -r requirements.txt
```

Ensure that both required input files are present:

```text
datasets/ft.csv
datasets/ml1m.csv
```

`ft.csv` is included. Create `ml1m.csv` by following the MovieLens preparation instructions above.

## Running the notebook

Start JupyterLab from the repository root:

```bash
jupyter lab
```

Open `Deep_Variational_Recommender.ipynb`, then select **Kernel → Restart Kernel and Run All**.

The notebook runs the datasets in this order:

1. FilmTrust (`ft`)
2. MovieLens 1M (`ml1m`)

For each dataset, it trains DeepMF, NCF, VDeepMF, and VNCF. The random seed is set to 42, and deterministic TensorFlow operations are enabled when supported by the installed environment.

Training all eight model instances may take a substantial amount of time. A compatible TensorFlow environment is required. GPU execution is selected automatically when TensorFlow detects a supported GPU; otherwise, the notebook uses the CPU.

## Evaluation

### Rating prediction

The notebook reports:

- **MAE** — mean absolute error; lower is better.
- **MSE** — mean squared error; lower is better.
- **R²** — coefficient of determination; higher is better.

### Top-N recommendation

For recommendation cutoffs N = 2 through N = 10, the notebook reports:

- **Precision**
- **Recall**
- **F1**
- **Novelty**
- **nDCG**

The notebook uses dataset-specific relevance thresholds: 3 for FilmTrust and 4 for MovieLens 1M. VDeepMF and VNCF predictions are averaged over ten stochastic inference passes.

## Experimental results

The following rating-prediction values are taken from the executed notebook results included in this repository.

| Dataset | Model | MAE ↓ | MSE ↓ | R² ↑ |
|---|---|---:|---:|---:|
| FilmTrust | VDeepMF | 0.636879 | 0.696933 | 0.185261 |
| FilmTrust | DeepMF | 0.798979 | 1.216966 | -0.422677 |
| FilmTrust | VNCF | 0.653174 | 0.693856 | 0.188858 |
| FilmTrust | NCF | **0.626976** | **0.678468** | **0.206847** |
| MovieLens 1M | VDeepMF | **0.684081** | **0.760223** | **0.392178** |
| MovieLens 1M | DeepMF | 0.702945 | 0.802133 | 0.358669 |
| MovieLens 1M | VNCF | 0.698247 | 0.787264 | 0.370557 |
| MovieLens 1M | NCF | 0.699672 | 0.789808 | 0.368523 |

At N = 10, the principal ranking results are:

| Dataset | Model | Precision ↑ | Recall ↑ | F1 ↑ | Novelty ↑ | nDCG ↑ |
|---|---|---:|---:|---:|---:|---:|
| FilmTrust | VDeepMF | 0.657496 | 0.610221 | 0.632977 | 6.766292 | 0.945101 |
| FilmTrust | DeepMF | 0.562076 | 0.511279 | 0.535475 | 6.626994 | 0.942390 |
| FilmTrust | VNCF | 0.564573 | 0.611564 | 0.587130 | **6.785587** | 0.931197 |
| FilmTrust | NCF | **0.679352** | **0.653329** | **0.666086** | 6.772892 | **0.947260** |
| MovieLens 1M | VDeepMF | **0.775662** | **0.370080** | **0.501084** | 10.104746 | **0.922170** |
| MovieLens 1M | DeepMF | 0.730065 | 0.360639 | 0.482789 | **10.122903** | 0.917613 |
| MovieLens 1M | VNCF | 0.768410 | 0.356967 | 0.487476 | 10.061642 | 0.917906 |
| MovieLens 1M | NCF | 0.752557 | 0.345011 | 0.473120 | 10.067385 | 0.918176 |

### Main findings

- **FilmTrust:** NCF achieves the best rating-prediction results and leads the models in Precision, Recall, F1, and nDCG across the evaluated recommendation cutoffs. VDeepMF substantially improves over DeepMF, but it does not surpass NCF on the principal metrics.
- **MovieLens 1M:** VDeepMF achieves the best rating-prediction metrics and leads the models in Precision, Recall, F1, and nDCG across the evaluated recommendation cutoffs. DeepMF has the highest Novelty score.
- **Variational matrix factorization:** VDeepMF improves over DeepMF on both datasets for rating prediction and the principal ranking-quality metrics.
- **Variational neural collaborative filtering:** VNCF does not consistently outperform NCF. Its rating-prediction results are worse on FilmTrust and only marginally better on MovieLens 1M.
- **Dataset dependence:** The strongest model differs by dataset. The results do not support a claim that variational sampling is universally superior for every interaction architecture.

## Evaluation limitations

- The same 20% holdout is used as Keras validation data and for the reported final metrics; there is no separate validation set and test set.
- The experiment uses one random split and one fixed seed. No multi-seed averages, confidence intervals, or statistical significance tests are reported.
- Epoch counts differ across models and datasets.
- Ranking metrics are computed over each user's held-out interactions, not over the complete catalog of unseen items.
- Novelty is estimated using item frequencies in the held-out partition; absolute novelty values should not be compared directly across datasets.
- nDCG uses raw rating values as relevance scores.
- The variational layers use Gaussian sampling and the reparameterization trick, but the implementation does not include a separate KL-divergence term or a decoder/reconstruction objective. The models are therefore described as collaborative-filtering networks with variational latent sampling, not complete encoder-decoder VAEs.
- Ten stochastic inference passes are averaged for VDeepMF and VNCF; these are not independently trained models.

These limitations should be considered when interpreting the results and comparing them with studies that use different data splits, candidate sets, or evaluation protocols.

## Repository artifacts

The `results/` directory contains the combined and dataset-specific CSV tables and eight evaluation figures. These artifacts are included so the reported results can be inspected without running the full training process.

When the notebook is executed successfully, the tables and figures are regenerated in `results/`.

## Citation

This project is based on the research paper that introduced the deep variational collaborative-filtering models studied in this repository. If you use this implementation or build upon its experiments, please cite the original paper:

Bobadilla, J., Ortega, F., Gutiérrez, A., et al. (2023). Deep variational models for collaborative filtering-based recommender systems. Neural Computing and Applications, 35, 7817–7831. https://doi.org/10.1007/s00521-022-08088-2

```bibtex
@article{bobadilla2023deepvariational,
  title   = {Deep variational models for collaborative filtering-based recommender systems},
  author  = {Bobadilla, Jes{'u}s and Ortega, Fernando and Guti{'e}rrez, Abraham and others},
  journal = {Neural Computing and Applications},
  volume  = {35},
  pages   = {7817--7831},
  year    = {2023},
  doi     = {10.1007/s00521-022-08088-2}
}
```
If you use MovieLens 1M, cite:

Harper, F. M., & Konstan, J. A. (2015). The MovieLens Datasets: History and Context. ACM Transactions on Interactive Intelligent Systems, 5(4), Article 19. https://doi.org/10.1145/2827872

If you use FilmTrust, cite:

Guo, G., Zhang, J., & Yorke-Smith, N. (2013). A Novel Bayesian Similarity Measure for Recommender Systems. Proceedings of the 23rd International Joint Conference on Artificial Intelligence (IJCAI), 2619–2625.
