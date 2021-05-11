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

def test_get_sorted_items():
  # limit 1
  s = Sample('w', {'a': 100, 'b': 300})
  assert s.get_sorted_items(1) == [('b', 300)]
  s = Sample('w', {'b': 300, 'a': 100})
  assert s.get_sorted_items(1) == [('b', 300)]
  # limit 2
  s = Sample('w', {'a': 100, 'b': 300})
  assert s.get_sorted_items(2) == [('b', 300), ('a', 100)]
  # no limit
  s = Sample('w', {'a': 100, 'b': 300})
  assert s.get_sorted_items() == [('b', 300), ('a', 100)]

def test_get_sorted_dict():
  # limit 1
  s = Sample('w', {'b': 300, 'a': 100})
  assert s.get_sorted_dict(1) == {'b': 300}
  # limit 2
  s = Sample('w', {'a': 100, 'b': 300})
  assert s.get_sorted_dict(2) == {'b':300, 'a':100}

def test_get_sorted_sample():
  # limit 1
  s = Sample('w', {'b': 300, 'a': 100})
  assert s.get_sorted_sample(1) == Sample('_', {'b': 300})

def test_get_sorted_cdr3s():
  # limit 1
  s = Sample('w', {'a': 100, 'b': 300})
  assert s.get_sorted_cdr3s(1) == ['b']
  s = Sample('w', {'b': 300, 'a': 100})
  assert s.get_sorted_cdr3s(1) == ['b']
  # limit 2
  s = Sample('w', {'a': 100, 'b': 300})
  assert s.get_sorted_cdr3s(2) == ['b', 'a']
  # no limit
  s = Sample('w', {'a': 100, 'b': 300})
  assert s.get_sorted_cdr3s() == ['b', 'a']

def test_get_x_y():
  # limit 1
  s = Sample('w', {'a': 100, 'b': 300})
  assert s.get_x_y(1) == ([1],[300])
  # limit 2
  s = Sample('w', {'a': 100, 'b': 300})
  assert s.get_x_y(2) == ([1, 2],[300, 100])
  # no limit
  s = Sample('w', {'a': 100, 'b': 300})
  assert s.get_x_y() == ([1, 2],[300, 100])

def test_get_cdr3s_by_rank():
  s = Sample('w', {'a': 100, 'b': 300})
  assert s.get_cdr3_by_rank(1) == 'b'
  assert s.get_cdr3_by_rank(2) == 'a'
  # slightly more complex example
  t = Sample('w', {'a': 100, 'b': 300, 'c': 200, 'd': 150, 'e': 250})
  assert t.get_cdr3_by_rank(1) == 'b'
  assert t.get_cdr3_by_rank(2) == 'e'
  assert t.get_cdr3_by_rank(3) == 'c'
  assert t.get_cdr3_by_rank(4) == 'd'
  assert t.get_cdr3_by_rank(5) == 'a'

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

def test_weak_intersection():
    # for two sets, it is just the intersection
    a = Sample('a', {c:100 for c in ['q', 'w']})
    b = Sample('b', {c:100 for c in ['e', 'w']})
    assert Sample.weak_intersection([a, b]) == [
        Sample('a', {'w':100}),
        Sample('b', {'w':100}),
    ]

if __name__ == '__main__':
  test_cutoff()
