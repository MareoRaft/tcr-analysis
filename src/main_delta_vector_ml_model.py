'''
Given a sample, perform hierarchical clustering on its CDR3s.
'''
import functools
import itertools

import numpy as np
import pandas as pd
from sklearn.linear_model import SGDClassifier
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

from decorators import record_elapsed_time
import data_utils
from pretty_print import pprint
from sample import Sample


def run_model(X_train, X_test, y_train, y_test):
    # init model
    classifier = make_pipeline(
        StandardScaler(),
        SGDClassifier(max_iter=4000),
    )
    # train model
    classifier.fit(X_train, y_train)
    # predict
    y_test_pred = classifier.predict(X_test)
    return y_test, y_test_pred

def get_loocv_indices(n):
    ''' Since our LOOCV situation is a bit unique (we want to keep samples in consecutive pairs when removing, I build my own LOOCV index computation. '''
    assert n % 2 == 0
    loocv_indices = []
    # First remove samples 0 and 1, then remove samples 2 and 3, and so on...
    for i in range(n//2):
        print(i)
        # train indices
        train_indices = np.array([i*2, i*2+1])
        # test indices
        test_indices = list(range(n))
        for train_index in train_indices:
            test_indices.remove(train_index)
        test_indices = np.array(test_indices)
        # record
        loocv_indices.append((train_indices, test_indices))
    return loocv_indices

@record_elapsed_time
def run_loocv(X, y):
    ''' internal function. '''
    # data
    num_correct = 0
    num_total = 0
    results = []
    for train_indices, test_indices in get_loocv_indices(len(y)):
        print(train_indices)
        print(test_indices)
        X_train = X.loc[train_indices]
        X_test = X.loc[test_indices]
        y_train = y[train_indices]
        y_test = y[test_indices]
        y_test, y_pred = run_model(X_train, X_test, y_train, y_test)
        for y_test_el,y_pred_el in zip(y_test, y_pred):
            num_correct += bool(y_test_el == y_pred_el)
            num_total += 1
        results.append((y_test, y_pred))
    accuracy = num_correct / num_total
    return results, accuracy

def preprocess_X(X):
    ''' preprocess X '''
    # convert file names to sample vectors
    series_pairs = [(data_utils.get_cdr3_series_from_file(a), data_utils.get_cdr3_series_from_file(b)) for a,b in X]
    delta_vecs = [after.subtract(before, fill_value=0) for before,after in series_pairs]
    print('got delta vecs')
    # TODO: add weak intersection back in
    # weak intersection of CDR3s in samples
    # trimmed_counters = Sample.weak_intersection(counters)
    # convert to a dictionary that is compatible with a Pandas DataFrame
    return delta_vecs

def detect_vaccine(X, y, limit=None):
    ''' user facing function '''
    # restrict data
    X = X[:limit]
    y = y[:limit]
    # preprocess
    X = preprocess_X(X)
    # negated vecs go with negated labels
    X = list(itertools.chain(*[(v, -v) for v in X]))
    y = list(itertools.chain(*[(label, 1-label) for label in y]))
    print('X len, y:')
    print(len(X))
    print(y)
    # put into correct type
    X = {i:c for i,c in enumerate(X)}
    X = pd.DataFrame.from_dict(X, orient='index').fillna(0)
    print('num rows,cols:')
    print(X.shape)
    y = np.array(y)
    results, accuracy = run_loocv(X, y)
    print(results)
    print('')
    print('accuracy:', accuracy)

@record_elapsed_time
def main():
    limit = 2
    detect_vaccine(
        limit=limit,
        X=[
            ('cdr3.a.A_2017_2018_d_00_53535.ann','cdr3.a.A_2017_2018_d_07_11143.ann'),
            ('cdr3.a.B_2017_2018_d_00_56786.ann','cdr3.a.B_2017_2018_d_09_50844.ann'),
            ('cdr3.a.C_2017_2018_d_00_26898.ann','cdr3.a.C_2017_2018_d_07_48996.ann'),
            ('cdr3.a.D_2017_2018_d_00_45294.ann','cdr3.a.D_2017_2018_d_07_55841.ann'),
            ('cdr3.a.E_2017_2018_d_00_94077.ann','cdr3.a.E_2017_2018_d_07_54569.ann'),
        ],
        # labels
        # 1 -> oriented as (before vaccine, after vaccine)
        # 0 -> oriented as (after vaccine, before vaccine)
        y=[1] * 5,
    )

if __name__ == '__main__':
  main()
