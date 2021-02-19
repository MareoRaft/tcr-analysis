'''
Distance functions.

A distance function d(m, n) takes as input 2 CDR3 alpha sequences, and outputs a mathematical "distance".
'''
import numpy as np
import distance

# Base distance functions

jaccard = distance.jaccard

sorensen = distance.sorensen

def hamming(a, b):
  '''
  Given 2 CDR3 sequences (strings of letters), output the number of letters that are different.  If one sequence is longer than the other, the shorter one is padded with letters that do not match the longer one.
  '''
  if len(a) > len(b):
    b += ' ' * (len(a) - len(b))
  if len(b) > len(a):
    a += ' ' * (len(b) - len(a))
  return distance.hamming(a, b)



# Aggregation functions

def one_to_many(c, c_seqs, dist_func, agg_func):
  '''
  Given cdr3 sequence `c`, a distance function `dist_func`, and an iterable `c_seqs` of cdr3 sequences, determine the distance between `c` and `c_seqs`, using the minimum.
  '''
  dists = [dist_func(c, c_seq) for c_seq in c_seqs]
  return agg_func(dists)

min = min

max = max

mean = np.mean



