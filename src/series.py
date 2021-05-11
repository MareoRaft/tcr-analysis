import pandas as pd

import set_utils

def weak_intersection(series_iterable):
    ''' Take weak intersection of CDR3s of some Series. '''
    cdr3_sets = [set(s.keys()) for s in series_iterable]
    cdr3_sets_wi = set_utils.weak_intersection(cdr3_sets)
    # filter by key
    series_list_wi = [s.filter(cdr3_sets_wi) for s in series_iterable]
    # return
    return series_list_wi
