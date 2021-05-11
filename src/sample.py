'''
A Sample is a Counter where the keys are cdr3 sequences.
'''
import collections
import random
import functools

import numpy as np

import set_utils


class Sample (collections.Counter):


  # The smallest frequency that is recognized as a valid non-zero frequency.
  CUTOFF = 10

  def __init__(self, id_, *args, **kwargs):
    # validation
    if type(id_) != str:
      raise TypeError('the id of a Sample must be a string')
    # create Counter object
    super(collections.Counter, self).__init__(*args, **kwargs)
    # restrict to not-too-rare cdr3 sequences
    self.__prune_items()
    # tack on an ID
    self.id = id_

  def __hash__(self):
    return hash(self.id)

  def __add__(self, other):
    new_id = self.id + '+' + other.id
    new_dict = super().__add__(other)
    return Sample(new_id, new_dict)

  def __setitem__(self, key, value):
    # only valid values will be set
    if self.__is_value_valid(value):
      super().__setitem__(key, value)

  def __is_value_valid(self, value):
    # In addition to cutoff pruning, ALWAYS prune frequency-0 items
    return (value > 0 and value >= Sample.CUTOFF)

  def __prune_items(self):
    # The `list` typecasting is to avoid 'dictionary changed size during iteration' error
    for k,v in list(self.items()):
      # In addition to cutoff pruning, ALWAYS prune frequency-0 items
      if not self.__is_value_valid(v):
        del self[k]

  def get_sorted_items(self, limit=None):
    ''' Get an array of (x,y)-pairs. Limit length if specified. '''
    sorted_items = sorted(self.items(), key=lambda item: -item[1])[:limit]
    return sorted_items

  def get_sorted_cdr3s(self, limit=None):
    ''' Get the top `limit` cdr3s, sorted from most frequent to least. '''
    top_items = self.get_sorted_items(limit=limit)
    top_cdr3s = [cdr3 for cdr3,_ in top_items]
    return top_cdr3s

  def get_x_y(self, limit=None):
    ''' Get x as an array and y as an array. Limit length if specified. '''
    sorted_x_y_pairs = self.get_sorted_items(limit)
    x = list(range(1, len(sorted_x_y_pairs)+1))
    y = [item[1] for item in sorted_x_y_pairs]
    return x,y

  def get_x_y_floats(self, limit=None):
    x,y = self.get_x_y(limit)
    y_float = np.array(y).astype(np.float)
    x_float = np.array(x).astype(np.float)
    return x_float,y_float

  def get_cdr3_by_rank(self, rank):
    ''' This is like getting a cdr3 by line number in an .ann file.  Given a `rank` integer, the cdr3 in the sample with the `rank`-th highest frequency. '''
    sorted_items = self.get_sorted_items(rank)
    # subtract 1 since rank is 1-indexed but sorted_cdr3s are 0-indexed
    item = sorted_items[rank-1]
    cdr3 = item[0]
    return cdr3

  def get_random_sample_items(self, sample_size):
    items = self.items()
    sample_size = min(sample_size, len(items))
    sample_items = random.sample(list(items), sample_size)
    return sample_items

  @classmethod
  def weak_intersection(cls, samples):
    ''' The 'weak intersection' of a bunch of samples is the weak intersection of their keys as sets. '''
    samples_cdr3s_list = [set(s.keys()) for s in samples]
    cdr3s_weak_intersection = set_utils.weak_intersection(samples_cdr3s_list)
    samples_weak_intersection = [
        {k:s[k] for k in cdr3s_weak_intersection}
        for s in samples
    ]
    return samples_weak_intersection
