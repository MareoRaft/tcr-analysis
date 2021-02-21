from pretty_print import pprint
import clogging
import data_utils
import sample_distances


# Setup
FILE_NAMES = {
  'A': 'cdr3.a.A_2000_2001_d_00_47407.ann',
  'B': 'cdr3.a.B_2017_2018_d_00_32483.ann',
  'C': 'cdr3.a.C_2017_2018_d_00_26898.ann',
  'D': 'cdr3.a.D_2017_2018_d_00_45294.ann',
  # 'E': 'cdr3.a.E_2017_2018_d_00_94077.ann',
}

log = clogging.getLogger('global', 'sample_to_sample_freq_results.log')


# Functions
def calculate_accuracy(dist_func):
  # pick a cdr3 seq
  counters = {n:data_utils.get_cdr3_series_from_file(fl) for n,fl in FILE_NAMES.items()}
  # iterate through all test seqs and calculate accuracy
  total_correct = 0
  total = 0
  pairs = [((na, ca), (nb, cb)) for na,ca in counters.items() for nb,cb in counters.items() if na <= nb]
  for ((na, ca), (nb, cb)) in pairs:
    dist = dist_func(ca, cb)
    print('pair:', na, nb, f'dist:{dist:f}')

def calculate_combination(dist_func_name):
  '''
  Calculate a metric on a single distance.
  '''
  dist_func = getattr(sample_distances, dist_func_name)
  calculate_accuracy(dist_func)

def calculate_combinations():
  '''
  Try out multiple combinations of input parameters for the sake of comparing them.
  '''
  for dist_func_name in ('l2'):
      calculate_combination(dist_func_name)

def main():
  # calculate_combinations()
  calculate_combination(dist_func_name='l2')

if __name__ == '__main__':
  main()






