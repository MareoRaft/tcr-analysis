import numpy as np

from data_utils import get_cdr3_series_from_file as get_series
from sample_distances import *

def test_l2():
  a = get_series('cdr3.test.ann')
  b = get_series('cdr3.test2.ann')
  assert l2(a, b) == 23230 * np.sqrt(2)

def test_jaccard_index():
  a = get_series('cdr3.test3.ann')
  b = get_series('cdr3.test4.ann')
  dist = jaccard_index(a, b)
  assert dist == 1 / 2
  a = get_series('cdr3.test3.ann')
  b = get_series('cdr3.test5.ann')
  dist = jaccard_index(a, b)
  assert dist == 1 / 3

def test_get_distance_ladder():
  # vectors len 0
  assert get_distance_ladder([], lambda a, b: 1, 3) == []
  # vectors len 1
  assert get_distance_ladder(['s'], lambda a, b: 1, 0) == [[]]
  assert get_distance_ladder(['s'], lambda a, b: 1, 1) == [[None]]
  # vectors len 2
  assert get_distance_ladder(['s', 't'], lambda a, b: 1, 1) == [[1], [None]]
  assert get_distance_ladder(['s', 't'], lambda a, b: 1, 2) == [[1, None], [None, None]]
  # vectors len 3
  assert get_distance_ladder(['s', 't', 7], lambda a, b: 1, 2) == [[1, 1], [1, None], [None, None]]

if __name__ == '__main__':
  test_jaccard_index()
