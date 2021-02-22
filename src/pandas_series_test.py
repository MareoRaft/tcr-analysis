import numpy as np
import pandas as pd

from data_utils import get_cdr3_series_from_file as get_series

def test_init():
  get_series('cdr3.a.A_2000_2001_d_00_47407.ann')

def test_add():
  a = get_series('cdr3.test.ann')
  b = get_series('cdr3.test2.ann')
  c = a.add(b, fill_value=0)

def test_l2_distance():
  a = get_series('cdr3.test.ann')
  print(a)
  b = get_series('cdr3.test2.ann')
  c = np.sqrt((a.subtract(b, fill_value=0)**2).sum())

if __name__ == '__main__':
  test_l2_distance()





