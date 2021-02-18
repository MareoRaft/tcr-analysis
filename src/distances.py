'''
Distance functions.

A distance function d(m, n) takes as input 2 CDR3 alpha sequences, and outputs a mathematical "distance".
'''
import numpy as np

def hamming(a, b):
  '''
  Given 2 CDR3 sequences (strings of letters), output the number of letters that are different.  If one sequence is longer than the other, the shorter one is padded with letters that do not match the longer one.
  '''
  min_len = min(len(a), len(b))
  max_len = max(len(a), len(b))
  distance = 0
  # count number of mismatching letters
  for i in range(min_len):
    if a[i] != b[i]:
      distance += 1
  # if one sequence is longer than the other, count the length difference
  distance += (max_len - min_len)
  # return
  return distance

def min_to_set(c, c_seqs, distance_func):
  '''
  Given cdr3 sequence `c`, a distance function `distance_func`, and an iterable `c_seqs` of cdr3 sequences, determine the distance between `c` and `c_seqs`, using the minimum.
  '''
  min_distance = np.inf
  for c_seq in c_seqs:
    distance = distance_func(c, c_seq)
    if distance < min_distance:
      min_distance = distance
  return min_distance
