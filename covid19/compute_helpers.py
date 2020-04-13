from multiprocessing import Pool, cpu_count

import numpy as np
import pandas as pd
import Levenshtein
from typing import List


def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


def similarity(s1, s2):
    """
    Get the similarity between two genome sequences represented as strings.
    The similarity is calculated as 1 - L(s1, s2)/H(s1, s2), where
    L(s1, s2) is the Levenshtein distance between s1 and s2 and
    H(s1, s2) is the Hamming distance between s1 and s2.
    """
    return 1 - (Levenshtein.distance(s1, s2) / max(len(s1), len(s2)))


def _similarity_worker(args):
    """
    Genome similarity parallel worker. Takes two genomes and their
    indices as inputs and returns their similarity.
    """
    ((i, j), (g1, g2)) = args
    return i, j, similarity(g1, g2)


def similarity_matrix(genomes, n_workers=cpu_count()):
    """
    Return the similarity matrix of a list of genomes.
    The calculation is by default parallelized, with n_workers=number of CPU cores.
    The similarity matrix of a list of N genomes will be a square NxN matrix named S,
    where S[i][i] = 1.0 (similarity of each element with itself) and
    S[i][j] = S[j][i] = similarity between the i-th and j-th genome.
    """

    # Initialize the matrix with zeros
    matrix = np.zeros((len(genomes), len(genomes)))

    # Elements on the diagonal will be ones
    for i in range(len(genomes)):
        matrix[i][i] = 1.

    # Unwrap the sequences from the objects
    genomes = [g.sequence for _, g in genomes.iterrows()]

    # Generate the pairs to be fed to the workers
    work = [
        ((j, i), (g2, g1))
        for i, g1 in enumerate(genomes)
        for j, g2 in enumerate(genomes)
        if j < i
    ]

    # Parallelize the calculation
    workers = Pool(n_workers)

    # Aggregate the result into the final matrix
    for result in workers.map(_similarity_worker, work):
        (i, j, sim) = result
        matrix[i][j] = sim
        matrix[j][i] = sim

    return matrix


# vim:sw=4:ts=4:et:
