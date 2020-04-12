import os

from covid19.compute_helpers import similarity_matrix
from covid19.datasets import datasets_dir
from covid19.file_helpers import load_genomes, save_similarity_matrix, load_similarity_matrix

genomes_file = os.path.join(datasets_dir, 'genomes.json')
similarity_matrix_file = os.path.join(datasets_dir, 'similarity_matrix.npz')

#%%

# genomes = download_genomes()
# save_genomes(genomes, genomes_file)

#%%

genomes = load_genomes(genomes_file)

#%%

matrix = similarity_matrix(genomes)

#%%

save_similarity_matrix(matrix, similarity_matrix_file)

#%%

matrix = load_similarity_matrix(similarity_matrix_file)


# vim:sw=4:ts=4:et:
