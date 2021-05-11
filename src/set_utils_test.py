from set_utils import *

def test_weak_intersection():
    # for two sets, it is just the intersection
    a = set(['q', 'w'])
    b = set(['e', 'w'])
    assert weak_intersection([a, b]) == {'w'}
    # for three sets, even things that don't appear in the third set work
    a = set(['r', 'q', 'w', 'y'])
    b = set(['r', 'e', 'w', 't'])
    c = set(['r', 's', 't', 'y'])
    assert weak_intersection([a, b, c]) == {'r', 'w', 'y', 't'}
