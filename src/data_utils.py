'''
Utilities for reading and writing data.
'''
import functools

import pandas as pd

from sample import Sample

# dictionaries
def get_cdr3_counter_from_file(id_, filepath):
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
  counter = Sample(id_, dict_)
  return counter

def get_cdr3_counter_from_files(id_, filepaths):
  '''
  Given some filepaths, get a counter which contains the data from all the files combined.
  '''
  counters = [get_cdr3_counter_from_file(id_, fp) for fp in filepaths]
  counter = functools.reduce(Sample.__add__, counters)
  # recristen with single ID
  counter.id = id_
  return counter

# Pandas Series
def get_cdr3_series_from_file(filepath):
  '''
  Given a `filepath` for a .ann file, load the data and return a {cdr3_sequence:frequency} Series.
  '''
  fp = f'data/ann/{filepath}'
  df = pd.read_csv(fp,
    encoding='utf_8',
    delimiter=',',
    names=['cdr3-sequence', 'frequency'],
    index_col='cdr3-sequence',
  )
  return df['frequency']
