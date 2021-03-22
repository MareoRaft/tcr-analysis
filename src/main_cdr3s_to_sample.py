import random

from pretty_print import pprint
import clogging
from decorators import record_elapsed_time, on_n_gram
import data_utils
import cdr3_distances



# Setup
FILE_NAMES = {
  'A': ['cdr3.a.A_2000_2001_d_00_47407.ann'],
  'B': ['cdr3.a.B_2017_2018_d_00_32483.ann'],
  'C': ['cdr3.a.C_2017_2018_d_00_26898.ann'],
  # 'D': ['cdr3.a.D_2017_2018_d_00_45294.ann'],
  # 'E': ['cdr3.a.E_2017_2018_d_00_94077.ann'],
}

long_log = clogging.getLogger('cdr3s_to_sample_results_long', 'long/cdr3s_to_sample_results_long.log')
short_log = clogging.getLogger('cdr3s_to_sample_results_short', 'cdr3s_to_sample_results_short.log', fmt='short')


# Functions
def get_dists(cdr3s, counters, dist_func):
  # given a list of cdr3 sequences, find nearest neighbor
  name_to_dist = {counter.id:dist_func(cdr3s, counter.keys()) for counter in counters}
  print(name_to_dist)
  return name_to_dist

def get_nearest_neighbor(cdr3s, counters, dist_func):
  # get dists
  name_to_dist = get_dists(cdr3s, counters, dist_func)
  # get argmin (name of nearest neighbor)
  predicted_person = min(name_to_dist, key=name_to_dist.get)
  # return
  return predicted_person

def get_random_sample(sample_size):

def run_trial(counters, counter, dist_func, num_cdr3s):
  '''
    `num_cdr3s` -- The number of CDR3s to remove and use for a single sample guess.  More CDR3s is more information, so we expect the accuracy to stay the same or increase as num_cdr3s increases.
  '''
  # setup totals
  num_correct = 0
  num_incorrect = 0
  # take a random sample of cdr3s
  cdr3s = random.sample(set(counter.keys()), num_cdr3s)
  # LOOCV requires us to remove cdr3s from the counter
  freq = dict()
  for c in cdr3s:
    freq[c] = counter[c]
    del counter[c]
  # make prediction
  predicted_name = get_nearest_neighbor(cdr3s, counters, dist_func)
  # record if prediction was correct or not
  if predicted_name == counter.id:
    num_correct += 1
  else:
    num_incorrect += 1
  # TODO: since this was LOOCV, we must put the c_seq back in
  for c in cdr3s:
    counter[c] = freq[c]
  # return results of trial
  return num_correct, num_incorrect

def calculate_accuracy(dist_func, num_trials_per_sample, num_cdr3s):
  # pick a cdr3 seq
  counters = {data_utils.get_cdr3_counter_from_files(n,fl) for n,fl in FILE_NAMES.items()}
  # iterate through all test seqs and calculate accuracy
  total_correct = 0
  total_incorrect = 0
  for counter in counters:
    num_trials_per_sample = min(num_trials_per_sample, len(items))
    for _ in range(num_trials_per_sample):
      num_correct, num_incorrect = run_trial(counters, counter, dist_func, num_cdr3s)
      total_correct += num_correct
      total_incorrect += num_incorrect
  total = total_correct + total_incorrect
  accuracy = total_correct / total
  # return results
  return total_correct, total, accuracy

@record_elapsed_time
def calculate_combination(num_trials_per_sample, n_gram_len, inner_dist_func_name, dist_agg_func_name, num_cdr3s):
  '''
  Calculate a metric on a single distance.
  '''
  dist_func = lambda c_seqs_1, c_seqs_2: cdr3_distances.many_to_many(
    c_seqs_1,
    c_seqs_2,
    on_n_gram(n_gram_len)(getattr(cdr3_distances, inner_dist_func_name)),
    getattr(cdr3_distances, dist_agg_func_name),
  )
  total_correct, total, accuracy = calculate_accuracy(dist_func, num_trials_per_sample, num_cdr3s)
  # output results
  print(total_correct, total, f'{accuracy:.0%}')
  long_log.info(f'{inner_dist_func_name}, {dist_agg_func_name}, {total_correct}, {total}, {accuracy:.0%}, {n_gram_len}, {num_cdr3s}')
  # short log
  formatted_dist_func_name = inner_dist_func_name.rjust(11, ' ')
  accuracy_str = f'{accuracy:.0%}'.rjust(4, ' ')
  short_log.info(f'{accuracy_str}, nsamp={total:03}, {formatted_dist_func_name}, ngram={n_gram_len}, ncdr3s={num_cdr3s}')


def calculate_combinations():
  '''
  Try out multiple combinations of input parameters for the sake of comparing them.
  '''
  num_trials_per_sample = 2**2
  # then try out n-grams with jaccard
  calculate_combination(num_trials_per_sample, 4, 'jaccard', 'min')


@record_elapsed_time
def main():
  # calculate_combinations()
  calculate_combination(num_trials_per_sample=2, n_gram_len=2, inner_dist_func_name='jaccard', dist_agg_func_name='min', num_cdr3s=1)
  return 'done'

if __name__ == '__main__':
  main()






