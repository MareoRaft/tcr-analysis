'''
A Sample is a Counter where the keys are cdr3 sequences.
'''
import collections
import random


class Sample (collections.Counter):


  CUTOFF = 50

  def __init__(self, id_, *args, **kwargs):
    # validation
    if type(id_) != str:
      raise TypeError('the id of a Sample must be a string')
    # create Counter object
    super(collections.Counter, self).__init__(*args, **kwargs)
    # restrict to not-too-rare cdr3 sequences
    for k,v in list(self.items()):
      if v < Sample.CUTOFF:
        del self[k]
    # tack on an ID
    self.id = id_

  def __hash__(self):
    return hash(self.id)

  def __add__(self, other):
    new_id = self.id + '+' + other.id
    new_dict = super().__add__(other)
    return Sample(new_id, new_dict)

  def get_random_sample_items(self, sample_size):
    items = self.items()
    sample_size = min(sample_size, len(items))
    sample_items = random.sample(list(items), sample_size)
    return sample_items




