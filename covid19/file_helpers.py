import json
import os

import numpy as np
import pandas as pd


def _path(p):
    return os.path.abspath(os.path.expanduser(p))


def save_genomes(genomes, file):
    """
    Save a list of genome objects to a JSON file.
    """
    file = _path(file)
    with open(file, 'w') as f:
        json.dump([g.to_dict() for _, g in genomes.iterrows()], f)


def load_genomes(file):
    """
    Load a list of genome objects from a JSON file.
    """
    file = _path(file)
    with open(file, 'r') as f:
        genomes = json.load(f)

    return pd.DataFrame.from_records(genomes)


def save_similarity_matrix(matrix, file):
    """
    Save a genome similarity matrix as a numpy compressed file.
    """
    file = _path(file)
    np.savez_compressed(file, matrix=matrix)


def load_similarity_matrix(file):
    """
    Load a genome similarity matrix from a numpy compressed file
    """
    file = _path(file)
    return np.load(file)['matrix']


# vim:sw=4:ts=4:et:
