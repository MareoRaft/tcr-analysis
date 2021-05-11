'''
Given a sample, perform hierarchical clustering on its CDR3s.
'''
import functools

import numpy as np
import scipy as sp
import pandas as pd

from decorators import record_elapsed_time
import data_utils
from pretty_print import pprint

# TODO: move to series file
def get_avg(series_iterable):
    sum_series = functools.reduce(lambda a,b: a.add(b, fill_value=0), series_iterable)
    avg_series = sum_series / len(sum_series)
    return avg_series

@record_elapsed_time
def get_avg_delta_vector(series_pairs):
    ''' internal function. '''
    # for each (before_vaccine, after_vaccine) pair, compute the series_pairs
    deltas = [after.subtract(before, fill_value=0) for before,after in series_pairs]
    # take the average of the deltas
    avg_delta = get_avg(deltas)
    # return result
    return avg_delta

def compute_vaccine_delta_vector(file_names):
    ''' user facing function '''
    series_pairs = [
        # use Scipy Series since we are going to subtract samples from each other
        tuple(data_utils.get_cdr3_series_from_file(f) for f in pair)
        for pair in file_names
    ]
    vaccine_delta_vector = get_avg_delta_vector(series_pairs)
    print(vaccine_delta_vector)

@record_elapsed_time
def main():
    compute_vaccine_delta_vector(
        file_names=[
            ('cdr3.a.A_2017_2018_d_00_53535.ann', 'cdr3.a.A_2017_2018_d_07_11143.ann'),
            ('cdr3.a.B_2017_2018_d_00_56786.ann', 'cdr3.a.B_2017_2018_d_09_50844.ann'),
            # ('cdr3.a.C_2017_2018_d_00_26898.ann', 'cdr3.a.C_2017_2018_d_07_48996.ann'),
            # ('cdr3.a.D_2017_2018_d_00_45294.ann', 'cdr3.a.D_2017_2018_d_07_55841.ann'),
            # ('cdr3.a.E_2017_2018_d_00_94077.ann', 'cdr3.a.E_2017_2018_d_07_54569.ann'),
        ],
    )

if __name__ == '__main__':
  main()
