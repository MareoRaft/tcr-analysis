'''
Distance functions between Samples.  That is, Pandas Series.

A distance function d(m, n) takes as input two samples, and outputs a mathematical "distance".
'''
import numpy as np
import distance



# helper functions
def jaccard_index(a, b):
  # get set of all keys whose values are nonzero
  a_set = set(a[a != 0].keys())
  b_set = set(b[b != 0].keys())
  numerator = len(a_set & b_set)
  denominator = len(a_set | b_set)
  return numerator / denominator


# distance functions
def l2(a, b):
  '''
  The standard Euclidean distance.
  '''
  dist = np.sqrt((a.subtract(b, fill_value=0)**2).sum())
  return dist

def jaccard(a, b):
  return 1 - jaccard_index(a, b)
