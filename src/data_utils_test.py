from collections import Counter

from data_utils import *

def test_get_cdr3_counter_from_file():
  assert get_cdr3_counter_from_file('cdr3.test.ann') == Counter({
    'cAVRDRVGGGNKLTf': 23230,
    'cAMSTADKLIf': 8493,
  })

def test_get_cdr3_counter_from_files():
  assert get_cdr3_counter_from_files(['cdr3.test.ann', 'cdr3.test2.ann']) == Counter({
    'cAVRDRVGGGNKLTf': 23230,
    'cAVRDRVGGGNKLTg': 23230,
    'cAMSTADKLIf': 8493*2,
  })
