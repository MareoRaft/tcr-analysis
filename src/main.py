import random

from pretty_print import pprint
import data_utils
import distances

FILE_NAMES = [
  # 'cdr3.test.ann',
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

def get_dists(c, name_to_counter):
  # given a cdr3 sequence, find nearest neighbor
  counter_to_dist = {n:get_dist(c, counter.keys()) for n,counter in name_to_counter.items()}
  return counter_to_dist

def predict_person(c, name_to_counter):
  # get dists
  name_to_dist = get_dists(c, name_to_counter)
  # get argmin
  predicted_person = min(name_to_dist, key=name_to_dist.get)
  # return
  return predicted_person

def main():
  # pick a cdr3 seq
  name_to_counter = {fn:get_counter(fn) for fn in FILE_NAMES}
  # iterate through all test seqs and calculate accuracy
  total_correct = 0
  total = 0
  for name,counter in name_to_counter.items():
    print('counter len:', len(counter))
    items = counter.items()
    sample_size = min(2, len(items))
    sample_items = random.sample(list(enumerate(items)), sample_size)
    for i,(c,freq) in sample_items:
      print('index:', i)
      # TODO: LOOCV requires us to remove c_seq from the counter
      freq = counter[c]
      del counter[c]
      # make prediction
      predicted_name = predict_person(c, name_to_counter)
      # record if prediction was correct or not
      if predicted_name == name:
        total_correct += 1
      total += 1
      # TODO: since this was LOOCV, we must put the c_seq back in
      counter[c] = freq
  accuracy = total_correct / total
  # output results
  print(total_correct, total, f'{accuracy:.0%}')


if __name__ == '__main__':
  main()
