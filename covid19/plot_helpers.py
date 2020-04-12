import pandas as pd
from matplotlib.figure import Figure


def plot_genomes_by_length(genomes: pd.DataFrame, fig: Figure):
    """
    Plot a given list of genomes by genome length.
    """

    bars = fig.add_subplot()
    genomes_by_length = {}

    for _, genome in genomes.iterrows():
        l = len(genome.sequence)
        if l not in genomes_by_length:
            genomes_by_length[l] = []

        genomes_by_length[l].append(genome)

    x = sorted(genomes_by_length.keys())
    y = [len(genomes_by_length[_]) for _ in x]
    bars.bar(x, y, width=5.0)
    bars.set_xlabel('Number of sequenced nucleotides')
    bars.set_ylabel('Number of sequenced genomes')
    bars.set_title('Genomes grouped by length')
    return bars


# vim:sw=4:ts=4:et:
