'''
Utilities for reading and writing data.
'''
import pandas as pd

def get_cdr3_counter(filepath):
  '''
  Given a `filepath` for a .ann file, load the data and return a {cdr3_sequence:frequency} dictionary.
  '''
  df = pd.read_csv(filepath,
    encoding='utf_8',
    delimiter=',',
    names=['cdr3-sequence', 'frequency'],
    index_col='cdr3-sequence',
  )
  return df
