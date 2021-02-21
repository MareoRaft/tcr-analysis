import random

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
  'C': ['cdr3.a.C_2017_2018_d_00_26898.ann'],
  'D': ['cdr3.a.D_2017_2018_d_00_45294.ann'],
  'E': ['cdr3.a.E_2017_2018_d_00_94077.ann'],
}

log = clogging.getLogger('global', 'one_to_many_results.log')


# Functions
def get_counter(fl):
  counter = data_utils.get_cdr3_counter_from_files(fl)
  return counter

def get_dists(c, name_to_counter, dist_func):
  # given a cdr3 sequence, find nearest neighbor
  counter_to_dist = {n:dist_func(c, counter.keys()) for n,counter in name_to_counter.items()}
  return counter_to_dist

def get_nearest_neighbor(c, name_to_counter, dist_func):
  # get dists
  name_to_dist = get_dists(c, name_to_counter, dist_func)
  # get argmin (name of nearest neighbor)
  predicted_person = min(name_to_dist, key=name_to_dist.get)
  # return
  return predicted_person

def calculate_accuracy(dist_func, sample_size):
  # pick a cdr3 seq
  name_to_counter = {n:get_counter(fl) for n,fl in FILE_NAMES.items()}
  # iterate through all test seqs and calculate accuracy
  total_correct = 0
  total = 0
  for name,counter in name_to_counter.items():
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
      predicted_name = get_nearest_neighbor(c, name_to_counter, dist_func)
      # record if prediction was correct or not
      if predicted_name == name:
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
  dist_func = lambda c, c_seqs: distances.one_to_many(
    c,
    c_seqs,
    getattr(distances, inner_dist_func_name),
    getattr(distances, dist_agg_func_name),
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
  for inner_dist_func_name in ('jaccard', 'hamming', 'sorensen'):
    for dist_agg_func_name in ('min', 'max', 'mean'):
      calculate_combination(sample_size, inner_dist_func_name, dist_agg_func_name)

def main():
  calculate_combinations()
  # calculate_combination(sample_size=3, inner_dist_func_name='sorensen', dist_agg_func_name='min')

if __name__ == '__main__':
  main()






