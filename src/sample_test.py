from sample import *

def test_init():
  Sample('w', {})
  Sample('w', {'a': 100, 'b': 300})

def test_addition():
  a = Sample('a', {'w': 100})
  b = Sample('b', {'w': 100})
  c = a + b
  assert c['w'] == 200

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
  s = Sample('w', {'a': 1, 'b': 500})
  assert 'a' not in s
  assert 'b' in s

if __name__ == '__main__':
  test_cutoff()
