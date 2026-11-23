#!/usr/bin/env python3
"""Convert the official MovieLens 1M ratings.dat file to the notebook CSV schema."""

import argparse
from pathlib import Path

import pandas as pd


def main():
    parser = argparse.ArgumentParser(
        description="Prepare MovieLens 1M ratings for the collaborative-filtering notebook."
    )
    parser.add_argument(
        "ratings_file",
        help="Path to the official MovieLens 1M ratings.dat file."
    )
    parser.add_argument(
        "--output",
        default=str(Path(__file__).with_name("ml1m.csv")),
        help="Output CSV path (default: datasets/ml1m.csv)."
    )
    args = parser.parse_args()

    ratings_path = Path(args.ratings_file)
    if not ratings_path.is_file():
        raise FileNotFoundError(f"Ratings file not found: {ratings_path}")

    ratings = pd.read_csv(
        ratings_path,
        sep="::",
        engine="python",
        header=None,
        names=["userId", "movieId", "rating", "timestamp"]
    )

    user_ids = sorted(ratings["userId"].unique())
    item_ids = sorted(ratings["movieId"].unique())

    user_mapping = {user_id: index for index, user_id in enumerate(user_ids)}
    item_mapping = {item_id: index for index, item_id in enumerate(item_ids)}

    prepared = pd.DataFrame({
        "user": ratings["userId"].map(user_mapping).astype("int32"),
        "item": ratings["movieId"].map(item_mapping).astype("int32"),
        "rating": ratings["rating"].astype("float32")
    })

    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    prepared.to_csv(output_path, index=False)

    print(f"Saved {len(prepared):,} ratings to {output_path}")
    print(f"Users: {prepared['user'].nunique():,}")
    print(f"Items: {prepared['item'].nunique():,}")


if __name__ == "__main__":
    main()
