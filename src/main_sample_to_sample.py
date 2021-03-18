import re

from pretty_print import pprint
from decorators import record_elapsed_time, on_n_gram
import clogging
import data_utils
import sample_distances


# Setup
FILE_NAMES = [
  # 'cdr3.a.B_2017_2018_d_00_32483.ann',
  # 'cdr3.a.C_2017_2018_d_00_26898.ann',
  # 'cdr3.a.D_2017_2018_d_00_45294.ann',
  # 'cdr3.a.E_2017_2018_d_00_94077.ann',
  'cdr3.a.A_2017_2018_d_00_53535.ann',
  'cdr3.a.A_2017_2018_d_07_11143.ann',
  'cdr3.a.A_2017_2018_d_28_44887.ann',
  # 'cdr3.a.A_2017_2018_m_04_73516.ann',
  # 'cdr3.a.A_2019_2020_d_00_20857.ann',
]
# switch to BETA data
FILE_NAMES = [re.sub(r'\.a\.', '.b.', f) for f in FILE_NAMES]


long_log = clogging.getLogger('sample_to_sample_results_long', 'long/sample_to_sample_results_long.log')
short_log = clogging.getLogger('sample_to_sample_results_short', 'sample_to_sample_results_short.log', fmt='short')


# Functions
def print_ladder_line(name, dists):
  ''' print the name followed by the distances '''
  gap_width = 3
  col_width = 12
  end = ' ' * gap_width
  print('|\n|')
  print(name, end=end)
  for dist in dists:
    if dist == None:
      string = ''
    else:
      string = '{:.3f}'.format(dist)
    print(string.rjust(col_width, ' '), end=end)
  print()

def compare_ladder(dist_func, file_names):
  # get data
  samples = [data_utils.get_cdr3_series_from_file(f) for f in file_names]
  # compute distances
  dist_ladder = sample_distances.get_distance_ladder(samples, dist_func, 3)
  # display results
  for i in range(len(samples)):
    print_ladder_line(FILE_NAMES[i], dist_ladder[i])

@record_elapsed_time
def calculate_combination(dist_func, file_names):
  '''
  Calculate a metric on a single distance.
  '''
  print(f'Creating a compare ladder using distance "{dist_func}".')
  compare_ladder(dist_func, file_names)

def calculate_combinations():
  '''
  Try out multiple combinations of input parameters for the sake of comparing them.
  '''
  for dist_func in (
    sample_distances.lp(1),
    sample_distances.lp(2),
    sample_distances.lp(4),
    sample_distances.lp(8),
    sample_distances.lp(16),
    sample_distances.linfty,
  ):
    calculate_combination(dist_func, FILE_NAMES)

def main():
  calculate_combinations()
  # calculate_combination(dist_func_name='l2')

if __name__ == '__main__':
  main()






