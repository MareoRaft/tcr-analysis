'''
Given a sample, perform hierarchical clustering on its CDR3s.
'''
import numpy as np

from decorators import record_elapsed_time
import data_utils
from pretty_print import pprint


@record_elapsed_time
def get_common_cdr3s(samples, limit):
    ''' internal function. could potentially belong to Sample class '''
    # all we really need is a set intersection
    restricted_cdr3_lists = [s.get_sorted_cdr3s(limit=limit) for s in samples]
    cdr3_sets = [set(l) for l in restricted_cdr3_lists]
    cdr3_intersection = set.intersection(*cdr3_sets)
    return cdr3_intersection

def find_common_cdr3s(file_names, n):
    ''' user facing function '''
    samples = [data_utils.get_cdr3_counter_from_file(f,f) for f in file_names]
    cdr3s = get_common_cdr3s(
        samples,
        limit=n,
    )
    print(cdr3s)

@record_elapsed_time
def main():
    find_common_cdr3s(
        file_names=[
            'cdr3.a.A_2017_2018_d_00_53535.ann',
            'cdr3.a.B_2017_2018_d_00_32483.ann',
            'cdr3.a.C_2017_2018_d_00_26898.ann',
            'cdr3.a.D_2017_2018_d_00_45294.ann',
            'cdr3.a.E_2017_2018_d_00_94077.ann',
        ],
        # only use the top n highest-frequency cdr3s in each sample (default=None). Put None for no restriction.
        n=4000,
    )

if __name__ == '__main__':
  main()
