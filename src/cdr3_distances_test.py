import numpy as np

from cdr3_distances import *

# helpers
t = tuple


# tests
def test_hamming():
  # 0 distances
  assert hamming(t(''), t('')) == 0
  assert hamming(t('q'), t('q')) == 0
  assert hamming(t('qs'), t('qs')) == 0
  # 1 distances
  assert hamming(t(''), t('t')) == 1
  assert hamming(t('x'), t('xy')) == 1
  assert hamming(t('x'), t('r')) == 1
  assert hamming(t('ax'), t('bx')) == 1
  # 2 distances
  assert hamming(t('tt'), t('')) == 2
  assert hamming(t('fg'), t('uu')) == 2
  assert hamming(t('fg'), t('u')) == 2

def test_one_to_many():
  assert one_to_many('s', ['s'], hamming, min) == 0
  assert one_to_many('s', ['f', 's'], hamming, min) == 0
  assert one_to_many('s', ['a'], hamming, min) == 1
  assert one_to_many('s', ['f', 'g'], hamming, min) == 1
