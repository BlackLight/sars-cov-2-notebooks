import json
import os

import pandas as pd
from typing import Iterable


def _path(p: str) -> str:
    return os.path.abspath(os.path.expanduser(p))


def save_genomes(genomes: pd.DataFrame, file: str):
    """
    Save a list of genome objects to a JSON file.
    """
    file = _path(file)
    with open(file, 'w') as f:
        json.dump([g.to_dict() for _, g in genomes.iterrows()], f)


def load_genomes(file: str) -> pd.DataFrame:
    """
    Load a list of genome objects from a JSON file.
    """
    file = _path(file)
    with open(file, 'r') as f:
        genomes = json.load(f)

    return pd.DataFrame.from_records(genomes)


def save_similarity_matrix(matrix: Iterable[Iterable[float]], file: str):
    """
    Save a genome similarity matrix to a JSON file.
    """
    file = _path(file)
    with open(file, 'w') as f:
        json.dump(matrix, f)


def load_similarity_matrix(file: str) -> Iterable[Iterable[float]]:
    """
    Load a genome similarity matrix from a JSON file.
    """
    file = _path(file)
    with open(file, 'r') as f:
        return json.load(f)


# vim:sw=4:ts=4:et:
