from pretty_print import print
import data_utils
import distances

FILE_NAMES = [
  'cdr3.test.ann',
  'cdr3.a.A_2000_2001_d_00_47407.ann',
  'cdr3.a.B_2017_2018_d_00_32483.ann',
  'cdr3.a.C_2017_2018_d_00_26898.ann',
]

def get_counter(file_name):
  counter = data_utils.get_cdr3_counter(f'data/ann/{file_name}')
  dictionary = counter.to_dict()['frequency']
  return dictionary

def get_dist(c, c_seqs):
  return distances.min_to_set(c, c_seqs, distances.hamming)

def main():
  # pick a cdr3 seq
  c = 'cAMSTADKLIf'
  # load data
  counters = {fn:get_counter(fn) for fn in FILE_NAMES}
  # given a cdr3 sequence, find nearest neighbor
  counter_to_dist = {n:get_dist(c, counter.keys()) for n,counter in counters.items()}
  # output results
  print(counter_to_dist)

if __name__ == '__main__':
  main()
