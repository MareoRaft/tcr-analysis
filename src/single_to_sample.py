import random

from pretty_print import pprint
import clogging
from decorators import record_elapsed_time
import data_utils
import cdr3_distances



# Setup
FILE_NAMES = {
  # 'T': ['cdr3.test.ann'],
  'A': [
    'cdr3.a.A_2000_2001_d_00_47407.ann',
    # 'cdr3.a.A_2017_2018_d_00_53535.ann',
  ],
  'B': ['cdr3.a.B_2017_2018_d_00_32483.ann'],
  'C': ['cdr3.a.C_2017_2018_d_00_26898.ann'],
  # 'D': ['cdr3.a.D_2017_2018_d_00_45294.ann'],
  # 'E': ['cdr3.a.E_2017_2018_d_00_94077.ann'],
}

log = clogging.getLogger('global', 'one_to_many_results.log')


# Functions
def get_dists(c, counters, dist_func):
  # given a cdr3 sequence, find nearest neighbor
  name_to_dist = {counter.id:dist_func(c, counter.keys()) for counter in counters}
  print(name_to_dist)
  return name_to_dist

def get_nearest_neighbor(c, counters, dist_func):
  # get dists
  name_to_dist = get_dists(c, counters, dist_func)
  # get argmin (name of nearest neighbor)
  predicted_person = min(name_to_dist, key=name_to_dist.get)
  # return
  return predicted_person

def calculate_accuracy(dist_func, sample_size):
  # pick a cdr3 seq
  counters = {data_utils.get_cdr3_counter_from_files(n,fl) for n,fl in FILE_NAMES.items()}
  # iterate through all test seqs and calculate accuracy
  total_correct = 0
  total = 0
  for counter in counters:
    print('counter len:', len(counter))
    items = counter.items()
    sample_size = min(sample_size, len(items))
    sample_items = random.sample(list(enumerate(items)), sample_size)
    for i,(c,freq) in sample_items:
      print('index:', i)
      # TODO: LOOCV requires us to remove c_seq from the counter
      freq = counter[c]
      del counter[c]
      # make prediction
      predicted_name = get_nearest_neighbor(c, counters, dist_func)
      # record if prediction was correct or not
      if predicted_name == counter.id:
        total_correct += 1
      total += 1
      # TODO: since this was LOOCV, we must put the c_seq back in
      counter[c] = freq
  accuracy = total_correct / total
  # return results
  return total_correct, total, accuracy

def calculate_combination(sample_size, inner_dist_func_name, dist_agg_func_name):
  '''
  Calculate a metric on a single distance.
  '''
  dist_func = lambda c, c_seqs: cdr3_distances.one_to_many(
    c,
    c_seqs,
    getattr(cdr3_distances, inner_dist_func_name),
    getattr(cdr3_distances, dist_agg_func_name),
  )
  total_correct, total, accuracy = calculate_accuracy(dist_func, sample_size)
  # output results
  print(total_correct, total, f'{accuracy:.0%}')
  log.info(f'{inner_dist_func_name}, {dist_agg_func_name}, {total_correct}, {total}, {accuracy:.0%}')

def calculate_combinations():
  '''
  Try out multiple combinations of input parameters for the sake of comparing them.
  '''
  sample_size = 1
  for inner_dist_func_name in ('jaccard', 'hamming', 'sorensen', 'levenshtein'):
    for dist_agg_func_name in ('min', 'max', 'mean'):
      calculate_combination(sample_size, inner_dist_func_name, dist_agg_func_name)

@record_elapsed_time
def main():
  # calculate_combinations()
  calculate_combination(sample_size=1, inner_dist_func_name='hamming', dist_agg_func_name='min')
  return 'done'

if __name__ == '__main__':
  main()






