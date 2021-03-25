import random

import numpy as np

from pretty_print import pprint
import clogging
from decorators import record_elapsed_time
import data_utils
import sample_distances



# Setup
FILE_NAMES = {
  'A': ['cdr3.a.A_2017_2018_d_00_53535.ann'],
  'B': ['cdr3.a.B_2017_2018_d_00_32483.ann'],
  'C': ['cdr3.a.C_2017_2018_d_00_26898.ann'],
  'D': ['cdr3.a.D_2017_2018_d_00_45294.ann'],
  'E': ['cdr3.a.E_2017_2018_d_00_94077.ann'],
}

short_log = clogging.getLogger('average_sample_distance', 'average_sample_distance.log', fmt='short')


# Functions
def avg_dist(dist_func):
  # get data
  samples = [data_utils.get_cdr3_series_from_file(fl[0]) for fl in FILE_NAMES.values()]
  # compute distances
  dists = sample_distances.get_pairwise_distances(samples, dist_func)
  dist = np.mean(dists)
  # return results
  return dist

@record_elapsed_time
def calculate_combination(dist_func):
  '''
  Calculate a metric on a single distance.
  '''
  dist = avg_dist(dist_func)
  # output results
  short_log.info(f'avgdist={dist:.03f}, distfunc={dist_func.__name__}, nsamp={len(FILE_NAMES)}')

def calculate_combinations():
  '''
  Try out multiple combinations of input parameters for the sake of comparing them.
  '''
  pass

@record_elapsed_time
def main():
  calculate_combination(dist_func=sample_distances.linfty)
  # calculate_combinations()
  return 'done'

if __name__ == '__main__':
  main()






