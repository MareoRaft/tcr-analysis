import numpy as np
import pandas as pd


def get_series(filepath):
  '''
  Given a `filepath` for a .ann file, load the data and return a {cdr3_sequence:frequency} dictionary.
  '''
  fp = f'data/ann/{filepath}'
  df = pd.read_csv(fp,
    encoding='utf_8',
    delimiter=',',
    names=['cdr3-sequence', 'frequency'],
    index_col='cdr3-sequence',
  )
  # dict_ = df.to_dict()['frequency']
  # counter = Sample(id_, dict_)
  return df['frequency']

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





