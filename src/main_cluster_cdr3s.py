'''
Given a sample, perform hierarchical clustering on its CDR3s.
'''
import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial.distance import pdist, squareform
from scipy.cluster.hierarchy import linkage

import clogging
from decorators import record_elapsed_time, on_n_gram
import data_utils
import cdr3_distances
from pretty_print import pprint
import plot


@record_elapsed_time
def hierarchical_clustering_cdr3s(cdr3s, dist_func):
    ''' internal function '''
    # data must be ordered
    # it takes about 11 seconds to do 500 cdr3s, 22 secs for 1000, 55 sec for 2000
    cdr3_list = list(cdr3s)
    # compute the lower-triangular condensed distance matrix of cdr3-pair distances
    # OOTB metrics include ‘hamming’, ‘jaccard’, ‘jensenshannon’
    # see https://docs.scipy.org/doc/scipy/reference/generated/scipy.spatial.distance.pdist.html#scipy.spatial.distance.pdist for more
    # condensed_dist_matrix = pdist(cdr3_list, metric=dist_func)
    num_cdr3s = len(cdr3_list)
    m = num_cdr3s
    num_pairs = (m * (m - 1)) // 2
    condensed_dist_matrix = np.empty((num_pairs,))
    for j in range(m):
        for i in range(j):
            dist = dist_func(cdr3_list[i], cdr3_list[j])
            index = m * i + j - ((i + 2) * (i + 1)) // 2
            condensed_dist_matrix[index] = dist
    # compute the hierarchical clusters based on the condensed distance matrix
    data_linkage = linkage(condensed_dist_matrix)
    # create the dendrogram and plot it
    plot.cdr3_dendrogram(data_linkage, cdr3_list)

def cluster_cdr3s(file_name, dist_func, n_gram_len=1, n=25):
    ''' user facing function '''
    sample = data_utils.get_cdr3_counter_from_file('s', file_name)
    cdr3s = sample.get_sorted_cdr3s(limit=n)
    ngrammed_dist_func = on_n_gram(n_gram_len)(dist_func)
    hierarchical_clustering_cdr3s(
        cdr3s=cdr3s,
        dist_func=ngrammed_dist_func,
    )

@record_elapsed_time
def main():
    cluster_cdr3s(
        file_name='cdr3.a.A_2017_2018_d_00_53535.ann',
        dist_func=cdr3_distances.hamming,
        n_gram_len=1,
        n=30,
    )

if __name__ == '__main__':
  main()
