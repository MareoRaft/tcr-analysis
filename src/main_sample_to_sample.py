from pretty_print import pprint
import clogging
import data_utils
import sample_distances


# Setup
FILE_NAMES = [
  # 'cdr3.a.A_2000_2001_d_00_47407.ann',
  'cdr3.a.A_2017_2018_d_00_53535.ann',
  'cdr3.a.A_2017_2018_d_07_11143.ann',
  'cdr3.a.A_2017_2018_d_28_44887.ann',
  'cdr3.a.A_2017_2018_m_04_73516.ann',
  'cdr3.a.A_2019_2020_d_00_20857.ann',
  # 'cdr3.a.B_2017_2018_d_00_32483.ann',
  # 'cdr3.a.C_2017_2018_d_00_26898.ann',
  # 'cdr3.a.D_2017_2018_d_00_45294.ann',
  # 'cdr3.a.E_2017_2018_d_00_94077.ann',
]

long_log = clogging.getLogger('sample_to_sample_results_long', 'long/sample_to_sample_results_long.log')
short_log = clogging.getLogger('sample_to_sample_results_short', 'sample_to_sample_results_short.log', fmt='short')


# Functions
def compare_pairwise(dist_func):
  counters = {f[7:-10]:data_utils.get_cdr3_series_from_file(f) for f in FILE_NAMES}
  # iterate through all test seqs and calculate accuracy
  pairs = [((na, ca), (nb, cb)) for na,ca in counters.items() for nb,cb in counters.items() if na <= nb]
  for ((na, ca), (nb, cb)) in pairs:
    dist = dist_func(ca, cb)
    print(f'pair:{na},  {nb}  ->  dist:{dist:15.4f}')
  long_log.info(f'?, nsamp=?, dist={dist_func}')
  short_log.info(f'?, nsamp=?, dist={dist_func}')

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

def compare_ladder(dist_func):
  # get data
  samples = [data_utils.get_cdr3_series_from_file(f) for f in FILE_NAMES]
  # compute distances
  dist_ladder = sample_distances.get_distance_ladder(samples, dist_func, 3)
  # display results
  for i in range(len(samples)):
    print_ladder_line(FILE_NAMES[i], dist_ladder[i])

def calculate_combination(dist_func_name):
  '''
  Calculate a metric on a single distance.
  '''
  dist_func = getattr(sample_distances, dist_func_name)
  compare_ladder(dist_func)

def calculate_combinations():
  '''
  Try out multiple combinations of input parameters for the sake of comparing them.
  '''
  for dist_func_name in ('l2', 'jaccard'):
      calculate_combination(dist_func_name)

def main():
  # calculate_combinations()
  calculate_combination(dist_func_name='l2')

if __name__ == '__main__':
  main()






