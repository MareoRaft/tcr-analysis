import collections
import functools

def weak_intersection(sets):
    ''' The 'weak intersection' of an iterable of sets is the set of elements that appear in at least 2 of the sets. '''
    counters = [collections.Counter(s) for s in sets]
    combined_counter = functools.reduce(collections.Counter.__add__, counters)
    weak_intersection_set = {k for k,v in combined_counter.items() if v > 1}
    return weak_intersection_set
