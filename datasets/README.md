# Datasets

This project uses FilmTrust and MovieLens 1M.

## FilmTrust

`ft.csv` is included in this repository. It contains three columns:

- `user`: zero-based user index
- `item`: zero-based item index
- `rating`: observed rating

The supplied processed file contains 35,494 ratings from 1,508 users over 2,071 items. The LibRec dataset page describes the FilmTrust source collection as containing 35,497 ratings; the count reported here is the exact row count of the processed file used by this project.

Source: https://guoguibing.github.io/librec/datasets.html

Please acknowledge the FilmTrust dataset and cite:

Guo, G., Zhang, J., & Yorke-Smith, N. (2013). A Novel Bayesian Similarity Measure for Recommender Systems. Proceedings of the 23rd International Joint Conference on Artificial Intelligence (IJCAI), 2619–2625.

## MovieLens 1M

The processed `ml1m.csv` file is not included in this public repository. GroupLens states that public redistribution of MovieLens datasets is generally not permitted without separate permission. Obtain the dataset directly from the official source and review the README and usage conditions distributed with it:

https://grouplens.org/datasets/movielens/1m/

After downloading and extracting MovieLens 1M, run:

```bash
python datasets/prepare_movielens.py /path/to/ml-1m/ratings.dat
```

The script creates `datasets/ml1m.csv` with the columns `user`, `item`, and `rating`. User and item IDs are mapped to zero-based contiguous indices in sorted ID order.

The generated file is intentionally ignored by Git. Keep the local file in `datasets/` to run the notebook, but do not commit it to a public repository unless you have obtained the required redistribution permission.

For publications and research reports using MovieLens, cite:

Harper, F. M., & Konstan, J. A. (2015). The MovieLens Datasets: History and Context. ACM Transactions on Interactive Intelligent Systems, 5(4), Article 19. https://doi.org/10.1145/2827872

Do not imply endorsement by the University of Minnesota or GroupLens Research.
