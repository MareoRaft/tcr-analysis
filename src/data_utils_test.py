from sample import Sample

from data_utils import *

def test_get_cdr3_counter_from_file():
  assert get_cdr3_counter_from_file('A', 'cdr3.test.ann') == Sample('A', {
    'cAVRDRVGGGNKLTf': 23230,
    'cAMSTADKLIf': 8493,
  })

def test_get_cdr3_counter_from_files():
  assert get_cdr3_counter_from_files('G', ['cdr3.test.ann', 'cdr3.test2.ann']) == Sample('G', {
    'cAVRDRVGGGNKLTf': 23230,
    'cAVRDRVGGGNKLTg': 23230,
    'cAMSTADKLIf': 8493*2,
  })
