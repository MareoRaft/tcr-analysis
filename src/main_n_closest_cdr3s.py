import random

import scipy as sp

from pretty_print import pprint
import clogging
from decorators import record_elapsed_time, on_n_gram
import data_utils
import cdr3_distances



def get_closest_cdr3s(cdr3, cdr3s, dist_func, limit):
    ''' internal function '''
    cdr3_to_dist = {c:dist_func(c,cdr3) for c in cdr3s}
    sorted_cdr3_to_dist = sorted(cdr3_to_dist.items(), key=lambda item: item[1])
    top_n_cdr3_to_dist = sorted_cdr3_to_dist[:limit]
    return top_n_cdr3_to_dist

def get_closest_cdr3s_with_frequency(cdr3, sample, dist_func, limit):
    ''' internal function '''
    cdr3_to_dist = {c:(dist_func(c,cdr3),f) for c,f in sample.items()}
    sorted_cdr3_to_dist = sorted(cdr3_to_dist.items(), key=lambda item: (item[1][0],-item[1][1]))
    top_n_cdr3_to_dist = sorted_cdr3_to_dist[:limit]
    return top_n_cdr3_to_dist

def get_n_closest_cdr3s(file_name, cdr3, n, dist_func, n_gram_len=1):
    ''' user facing function '''
    sample = data_utils.get_cdr3_counter_from_file('s', file_name)
    ngrammed_dist_func = on_n_gram(n_gram_len)(dist_func)
    closest_cdr3s = get_closest_cdr3s_with_frequency(
        cdr3=cdr3,
        sample=sample,
        dist_func=ngrammed_dist_func,
        limit=n,
    )
    pprint(closest_cdr3s)

@record_elapsed_time
def main():
    get_n_closest_cdr3s(
        file_name='cdr3.a.A_2017_2018_d_00_53535.ann',
        cdr3='cVVSAFQAGTALIf',
        n=20,
        dist_func=cdr3_distances.hamming,
        n_gram_len=1,
    )

if __name__ == '__main__':
  main()
