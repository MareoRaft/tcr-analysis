'''
Distance functions.

A distance function d(m, n) takes as input 2 CDR3 alpha sequences, and outputs a mathematical "distance".
'''
import numpy as np
import distance



# Base distance functions

jaccard = distance.jaccard

# the worst-performing distance we have so far :D
sorensen = distance.sorensen

# The 'Distance' library ALSO provides a Levenshtein iterable which can potentially be used to find the shortest Levenshtein distance between many sequences, hence saving time.
levenshtein = distance.levenshtein

def hamming(a, b):
  '''
  Given 2 CDR3 sequences (tuples of letters), output the number of letters that are different.  If one sequence is longer than the other, the shorter one is padded with letters that do not match the longer one.
  '''
  if len(a) > len(b):
    b += (' ',) * (len(a) - len(b))
  if len(b) > len(a):
    a += (' ',) * (len(b) - len(a))
  return distance.hamming(a, b)



# Aggregation functions

min = min

max = max

mean = np.mean



# Meta distance functions

def one_to_many(c, c_seqs, dist_func, agg_func):
  '''
  Given cdr3 sequence `c`, a distance function `dist_func`, and an iterable `c_seqs` of cdr3 sequences, determine the distance between `c` and `c_seqs`, using the minimum.
  '''
  dists = [dist_func(c, c_seq) for c_seq in c_seqs]
  return agg_func(dists)

def many_to_many(c_seqs_1, c_seqs_2, dist_func, agg_func):
  '''
  Given TWO iterables of cdr3 sequences, `c_seqs_1` and `c_seqs_2`, find the distance between them using the given one-to-one distance function `dist_func` and the aggregation function `agg_func`.
  '''
  dists = [dist_func(c1, c2) for c1 in c_seqs_1 for c2 in c_seqs_2]
  return agg_func(dists)








