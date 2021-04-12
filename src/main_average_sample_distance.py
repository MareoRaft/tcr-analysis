import random

import numpy as np

from pretty_print import pprint
import clogging
from decorators import record_elapsed_time
import data_utils
import sample_distances



# Setup
short_log = clogging.getLogger('average_sample_distance', 'average_sample_distance.log', fmt='short')


# Functions
def avg_dist(dist_func, file_names):
  # get data
  samples = [data_utils.get_cdr3_series_from_file(fl[0]) for fl in file_names.values()]
  # compute distances
  dists = sample_distances.get_pairwise_distances(samples, dist_func)
  dist = np.mean(dists)
  # return results
  return dist

@record_elapsed_time
def calculate_combination(dist_func, file_names):
  '''
  Calculate a metric on a single distance.
  '''
  dist = avg_dist(dist_func, file_names)
  # output results
  short_info_str = f'avgdist={dist:.03f}, distfunc={dist_func.__name__}, nsamp={len(file_names)}'
  short_log.info(short_info_str)
  print(short_info_str)

def calculate_combinations():
  '''
  Try out multiple combinations of input parameters for the sake of comparing them.
  '''
  pass

@record_elapsed_time
def main():
  calculate_combination(
    dist_func=sample_distances.linfty,
    file_names={
      'A': ['cdr3.a.A_2017_2018_d_00_53535.ann'],
      'B': ['cdr3.a.B_2017_2018_d_00_32483.ann'],
      'C': ['cdr3.a.C_2017_2018_d_00_26898.ann'],
      # 'D': ['cdr3.a.D_2017_2018_d_00_45294.ann'],
      # 'E': ['cdr3.a.E_2017_2018_d_00_94077.ann'],
    },
  )
  # calculate_combinations()
  return 'done'

if __name__ == '__main__':
  main()
