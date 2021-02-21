'''
Distance functions between Samples.  That is, Pandas Series.

A distance function d(m, n) takes as input two samples, and outputs a mathematical "distance".
'''
import numpy as np
import distance



# distance functions
def l2(a, b):
  '''
  The standard Euclidean distance.
  '''
  dist = np.sqrt((a.subtract(b, fill_value=0)**2).sum())
  return dist
