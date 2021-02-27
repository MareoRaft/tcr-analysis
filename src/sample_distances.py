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


# meta distance functions
def get_distance_ladder(vectors, dist_func, max_gap):
  '''
  Given a list of vectors, a distance function, and a maximum gap, compute for each vector v_i its distance from the following vector v_i+1, from v_i+2, and so forth up to v_i+max_gap.
  '''
  vectors_dists = []
  for i in range(len(vectors)):
    vector_dists = []
    for gap in range(1, max_gap + 1):
      if i + gap < len(vectors):
        dist = dist_func(vectors[i], vectors[i + gap])
      else:
        dist = None
      vector_dists.append(dist)
    vectors_dists.append(vector_dists)
  return vectors_dists













