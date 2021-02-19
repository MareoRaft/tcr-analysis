'''
Utilities for reading and writing data.
'''
from collections import Counter
import functools

import pandas as pd

def get_cdr3_counter_from_file(filepath):
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
  dict_ = df.to_dict()['frequency']
  counter = Counter(dict_)
  return counter

def get_cdr3_counter_from_files(filepaths):
  '''
  Given some filepaths, get a counter which contains the data from all the files combined.
  '''
  counters = [get_cdr3_counter_from_file(fp) for fp in filepaths]
  counter = functools.reduce(Counter.__add__, counters)
  return counter
