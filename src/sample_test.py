from sample import *

def test_init():
  Sample('w', {})
  Sample('w', {'a': 100, 'b': 300})

def test_get():
  # get something that exists in the dict
  a = Sample('a', {'w': 100, 'x': 0, 'y':Sample.CUTOFF})
  assert a['w'] == 100
  assert a['x'] == 0
  assert a['y'] == Sample.CUTOFF
  w = Sample('w', {'a': 100, 'b': 300})
  assert w['a'] == 100
  assert w['b'] == 300
  # get something that does not exist in the dict
  w = Sample('w', {'a': 100, 'b': 300})
  assert w['c'] == 0

def test_addition():
  a = Sample('a', {'w': 100})
  b = Sample('b', {'w': 100})
  c = a + b
  assert c['w'] == 200

def test_keys():
  # All keys corresponding to nonzero values should appear, provided they are >= CUTOFF
  a = Sample('a', {'w': 100, 'x': 0, 'y':Sample.CUTOFF, 'z':Sample.CUTOFF-1})
  assert set(a.keys()) == {'w', 'y'}
  # even when 0 values are added after-the-fact
  a['t'] = 0
  assert set(a.keys()) == {'w', 'y'}

def test_id():
  s = Sample('w', {})
  assert s.id == 'w'

def test_hash():
  s = Sample('w', {})
  {s}

def test_get_random_sample_items():
  s = Sample('w', {'a': 100, 'b': 300})
  assert len(s.get_random_sample_items(0)) == 0
  assert len(s.get_random_sample_items(2)) == 2
  assert len(s.get_random_sample_items(3)) == 2

def test_cutoff():
  # Things under the cutoff should not appear on init
  s = Sample('w', {'a': 1, 'b': 500})
  assert 'a' not in s
  assert 'b' in s
  # Things equal to the cutoff, as long as nonzero, should appear
  s['c'] = Sample.CUTOFF if Sample.CUTOFF > 0 else 1
  assert 'c' in s
  # Things under the cutoff added after-the-fact should not appear
  s['d'] = Sample.CUTOFF - 1
  assert 'd' not in s


if __name__ == '__main__':
  test_cutoff()
