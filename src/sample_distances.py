'''
Distance functions between Samples.  That is, Pandas Series.

A distance function d(m, n) takes as input two samples, and outputs a mathematical "distance".
'''
import numpy as np
import pandas as pd



# helper functions
def jaccard_index(a, b):
  # get set of all keys whose values are nonzero
  a_set = set(a[a != 0].keys())
  b_set = set(b[b != 0].keys())
  numerator = len(a_set & b_set)
  denominator = len(a_set | b_set)
  return numerator / denominator

def weighted_jaccard_index(a, b):
  ''' For each key k, we take min(a[k], b[k]), and sum those up.  That's the numerator.  The denominator is the same except is uses max instead of min.'''
  # NOTE: This takes about 30 times longer to run than jaccard_index
  # numerator
  min_ = pd.DataFrame({'a': a, 'b': b}).fillna(0).apply(min, axis=1)
  numerator = min_.sum()
  # denominator
  max_ = pd.DataFrame({'a': a, 'b': b}).fillna(0).apply(max, axis=1)
  denominator = max_.sum()
  # return
  return numerator / denominator



# distance functions
def l2(a, b):
  '''
  The standard Euclidean distance.
  '''
  dist = np.sqrt((a.subtract(b, fill_value=0)**2).sum())
  return dist

def lp(p):
  ''' Given `p`, a real number >= 1, output the `lp` distance function. '''
  if p < 1:
    raise ValueError(f'p={p} illegal. in order for lp to be a distance function, we must have p >=1')
  def dist_func(a, b):
    dist = (np.abs(a.subtract(b, fill_value=0))**p).sum()**(1/p)
    return dist
  return dist_func

def linfty(a, b):
  ''' The l-infinity distance, coming from the L-infinity norm. '''
  dist = np.abs(a.subtract(b, fill_value=0)).max()
  return dist

def jaccard(a, b):
  return 1 - jaccard_index(a, b)

def weighted_jaccard(a, b):
  return 1 - weighted_jaccard_index(a, b)



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






