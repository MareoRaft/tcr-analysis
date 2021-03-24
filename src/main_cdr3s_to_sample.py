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

def remove_cdr3s_from_counters(counters, cdr3s):
  ''' LOOCV helper function for run_trial. Remove the cdr3s from the counters and return a dictionary showing what you removed, so that you can put it back later. '''
  freq = {counter:dict() for counter in counters}
  for counter in counters:
    for c in cdr3s:
      freq[counter][c] = counter[c]
      del counter[c]
  return freq

def add_cdr3s_to_counters(counters, cdr3s, freq):
  ''' LOOCV helper function for run_trial. Add the cdr3s and frequencies back to the counters. '''
  for counter in counters:
    for c in cdr3s:
      counter[c] = freq[counter][c]

def run_trial(counters, counter, dist_func, num_cdr3s):
  '''
    `num_cdr3s` -- The number of CDR3s to remove and use for a single sample guess.  More CDR3s is more information, so we expect the accuracy to stay the same or increase as num_cdr3s increases.
  '''
  # take a random sample of cdr3s
  cdr3s = random.sample(set(counter.keys()), num_cdr3s)
  # LOOCV requires us to remove cdr3s from the counter
  freq = remove_cdr3s_from_counters(counters, cdr3s)
  # make prediction
  predicted_name = get_nearest_neighbor(cdr3s, counters, dist_func)
  # record if prediction was correct or not
  is_prediction_correct = (predicted_name == counter.id)
  # Since this was LOOCV, we must put the c_seq back in
  add_cdr3s_to_counters(counters, cdr3s, freq)
  # return results of trial
  return is_prediction_correct

def calculate_accuracy(dist_func, num_trials_per_sample, num_cdr3s):
  # pick a cdr3 seq
  counters = {data_utils.get_cdr3_counter_from_files(n,fl) for n,fl in FILE_NAMES.items()}
  # iterate through all test seqs and calculate accuracy
  total_correct = 0
  total_incorrect = 0
  for counter in counters:
    for _ in range(num_trials_per_sample):
      is_prediction_correct = run_trial(counters, counter, dist_func, num_cdr3s)
      total_correct += int(is_prediction_correct)
      total_incorrect += int(not is_prediction_correct)
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
  short_log.info(f'{accuracy_str}, ntrials={total:03}, {formatted_dist_func_name}, ngram={n_gram_len}, ncdr3s={num_cdr3s}, nsamp={len(FILE_NAMES)}')


def calculate_combinations():
  '''
  Try out multiple combinations of input parameters for the sake of comparing them.
  '''
  num_trials_per_sample = 30
  for num_cdr3s in range(1, 8):
    # hamming
    calculate_combination(num_trials_per_sample=num_trials_per_sample, n_gram_len=1, inner_dist_func_name='hamming', dist_agg_func_name='min', num_cdr3s=num_cdr3s)
    # jaccard
    for n_gram_len in (1, 3, 4):
      calculate_combination(num_trials_per_sample=num_trials_per_sample, n_gram_len=n_gram_len, inner_dist_func_name='jaccard', dist_agg_func_name='min', num_cdr3s=num_cdr3s)


@record_elapsed_time
def main():
  # calculate_combinations()
  calculate_combination(num_trials_per_sample=5, n_gram_len=1, inner_dist_func_name='jaccard', dist_agg_func_name='min', num_cdr3s=1)
  return 'done'

if __name__ == '__main__':
  main()






