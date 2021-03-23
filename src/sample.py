'''
A Sample is a Counter where the keys are cdr3 sequences.
'''
import collections
import random


class Sample (collections.Counter):


  # The smallest frequency that is recognized as a valid non-zero frequency.
  CUTOFF = 50

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

  def get_random_sample_items(self, sample_size):
    items = self.items()
    sample_size = min(sample_size, len(items))
    sample_items = random.sample(list(items), sample_size)
    return sample_items




