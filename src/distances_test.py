import numpy as np

from distances import *

def test_hamming():
  # 0 distances
  assert hamming('', '') == 0
  assert hamming('q', 'q') == 0
  assert hamming('qs', 'qs') == 0
  # 1 distances
  assert hamming('', 't') == 1
  assert hamming('x', 'xy') == 1
  assert hamming('x', 'r') == 1
  assert hamming('ax', 'bx') == 1
  # 2 distances
  assert hamming('tt', '') == 2
  assert hamming('fg', 'uu') == 2
  assert hamming('fg', 'u') == 2

def test_min_to_set():
  assert min_to_set('s', [], hamming) == np.inf
  assert min_to_set('s', ['s'], hamming) == 0
  assert min_to_set('s', ['f', 's'], hamming) == 0
  assert min_to_set('s', ['f', 'g'], hamming) == 1
