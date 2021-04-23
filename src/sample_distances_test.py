import math

import numpy as np

from data_utils import get_cdr3_series_from_file as get_series
from sample_distances import *

def test_l2():
	a = get_series('cdr3.test.ann')
	b = get_series('cdr3.test2.ann')
	assert l2(a, b) == 23230 * np.sqrt(2)
	a = get_series('cdr3.test3.ann')
	b = get_series('cdr3.test4.ann')
	assert l2(a, b) == math.sqrt(3**2 + 2**2)

def test_lp():
	# p=1
	a = get_series('cdr3.test3.ann')
	b = get_series('cdr3.test4.ann')
	assert lp(1)(a, b) == 3 + 2
	# p=2
	a = get_series('cdr3.test.ann')
	b = get_series('cdr3.test2.ann')
	assert lp(2)(a, b) == 23230 * np.sqrt(2)
	a = get_series('cdr3.test3.ann')
	b = get_series('cdr3.test4.ann')
	assert lp(2)(a, b) == math.sqrt(3**2 + 2**2)
	# p=3
	a = get_series('cdr3.test3.ann')
	b = get_series('cdr3.test4.ann')
	assert lp(3)(a, b) == (3**3 + 2**3)**(1/3)

def test_linfty():
	# two identical samples gives distance 0
	a = get_series('cdr3.test.ann')
	b = get_series('cdr3.test.ann')
	assert linfty(a, b) == 0
	# between two lines, the first one has the max diff
	a = get_series('cdr3.test3.ann')
	b = get_series('cdr3.test4.ann')
	assert linfty(a, b) == 3
	# a letter present in one sample and missing in the other has the max diff
	a = get_series('cdr3.test6.ann')
	b = get_series('cdr3.test7.ann')
	assert linfty(a, b) == 6
	# the max diff isn't from the first line in the file
	a = get_series('cdr3.test7.ann')
	b = get_series('cdr3.test8.ann')
	assert linfty(a, b) == 1	  

def test_jaccard_index():
	a = get_series('cdr3.test3.ann')
	b = get_series('cdr3.test4.ann')
	dist = jaccard_index(a, b)
	assert dist == 1 / 2
	a = get_series('cdr3.test3.ann')
	b = get_series('cdr3.test5.ann')
	dist = jaccard_index(a, b)
	assert dist == 1 / 3

def test_weighted_jaccard_index():
	a = get_series('cdr3.test6.ann')
	b = get_series('cdr3.test7.ann')
	index = weighted_jaccard_index(a, b)
	assert index == 11 / 24

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

def test_get_pairwise_distances():
	# no vectors
	assert get_pairwise_distances([], jaccard) == []
	# 1 vec
	a = get_series('cdr3.test3.ann')
	assert get_pairwise_distances([a], jaccard) == []
	# 2 vecs
	a = get_series('cdr3.test3.ann')
	assert get_pairwise_distances([a, a], jaccard) == [0]
	# 3 vecs
	a = get_series('cdr3.test3.ann')
	b = get_series('cdr3.test4.ann')
	assert get_pairwise_distances([a, a, b], lp(1)) == [0, 5, 5]

if __name__ == '__main__':
	test_jaccard_index()
