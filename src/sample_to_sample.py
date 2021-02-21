from pretty_print import pprint
import clogging
import data_utils
import distances


# Setup
FILE_NAMES = {
  # 'T': ['cdr3.test.ann'],
  'A': [
    'cdr3.a.A_2000_2001_d_00_47407.ann',
    # 'cdr3.a.A_2017_2018_d_00_53535.ann',
  ],
  'B': ['cdr3.a.B_2017_2018_d_00_32483.ann'],
  # 'C': ['cdr3.a.C_2017_2018_d_00_26898.ann'],
  # 'D': ['cdr3.a.D_2017_2018_d_00_45294.ann'],
  # 'E': ['cdr3.a.E_2017_2018_d_00_94077.ann'],
}

log = clogging.getLogger('global', 'many_to_many_results.log')


# Functions
def calculate_accuracy(dist_func, sample_size):
  # pick a cdr3 seq
  counters = {data_utils.get_cdr3_counter_from_files(n,fl) for n,fl in FILE_NAMES.items()}
  # iterate through all test seqs and calculate accuracy
  total_correct = 0
  total = 0
  pairs = [(ca, cb) for ca in counters for cb in counters if ca.id <= cb.id]
  for (ca, cb) in pairs:
    a_sample_items = ca.get_random_sample_items(sample_size)
    b_sample_items = cb.get_random_sample_items(sample_size)
    dist = dist_func(a_sample_items, b_sample_items)
    print('pair:', ca.id, cb.id, 'dist:', dist)

def calculate_combination(sample_size, inner_dist_func_name, dist_agg_func_name):
  '''
  Calculate a metric on a single distance.
  '''
  dist_func = lambda c_seqs1, c_seqs2: distances.many_to_many(
    c_seqs1,
    c_seqs2,
    getattr(distances, inner_dist_func_name),
    getattr(distances, dist_agg_func_name),
  )
  calculate_accuracy(dist_func, sample_size)

def calculate_combinations():
  '''
  Try out multiple combinations of input parameters for the sake of comparing them.
  '''
  sample_size = 1
  for inner_dist_func_name in ('jaccard', 'sorensen', 'hamming'):
    for dist_agg_func_name in ('min', 'max', 'mean'):
      calculate_combination(sample_size, inner_dist_func_name, dist_agg_func_name)

def main():
  # calculate_combinations()
  calculate_combination(sample_size=50, inner_dist_func_name='hamming', dist_agg_func_name='mean')

if __name__ == '__main__':
  main()






