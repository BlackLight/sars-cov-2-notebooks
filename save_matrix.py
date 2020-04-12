import os
import matplotlib.pyplot as plt

from covid19.compute_helpers import similarity_matrix
from covid19.datasets import datasets_dir
from covid19.file_helpers import save_genomes, load_genomes, save_similarity_matrix, load_similarity_matrix
from covid19.net_helpers import download_genomes
from covid19.plot_helpers import plot_genomes_by_length

genomes_file = os.path.join(datasets_dir, 'genomes.json')
similarity_matrix_file = os.path.join(datasets_dir, 'similarity_matrix.json')

#%%

# genomes = download_genomes()
# save_genomes(genomes, genomes_file)

#%%

genomes = load_genomes(genomes_file)

#%%

# fig = plt.figure()
# plot_genomes_by_length(genomes, fig)
# plt.show()

#%%

matrix = similarity_matrix(genomes)

#%%

save_similarity_matrix(matrix, similarity_matrix_file)

#%%

matrix = load_similarity_matrix(similarity_matrix_file)


# vim:sw=4:ts=4:et:
