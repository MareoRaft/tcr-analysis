'''
Given a sample, perform hierarchical clustering on its CDR3s.
'''
import functools

import numpy as np
import pandas as pd
from sklearn.linear_model import SGDClassifier
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

from decorators import record_elapsed_time
import data_utils
from pretty_print import pprint


@record_elapsed_time
def is_vaccinated(X, y):
    ''' internal function. '''
    # data
    X = pd.DataFrame.from_dict(X, orient='index').fillna(0)
    print(X)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=1, random_state=None)
    print('train:')
    print(X_train)
    print('test:')
    print(X_test)
    # note: docs say 'for best results, the data should have 0 mean and unit variance'
    # note: features may need to be converted to floats
    # TODO: example says 'ALWAYS SCALE INPUT'
    # setup model
    # SGDClassifier uses a Linear SVM by default, and SGD optimization to train it.
    classifier = make_pipeline(
        StandardScaler(),
        SGDClassifier(max_iter=10000),
    )
    # train model
    classifier.fit(X_train, y_train)
    # predict
    y_test_pred = classifier.predict(X_test)
    return y_test, y_test_pred

def detect_vaccine(X, y):
    ''' user facing function '''
    # remove test
    # convert file names to sample vectors
    X = {index:data_utils.get_cdr3_counter_from_file(f,f) for index,f in enumerate(X)}
    y_test, y_pred = is_vaccinated(X, y)
    print(y_test)
    print(y_pred)

@record_elapsed_time
def main():
    detect_vaccine(
        X=[
            'cdr3.a.A_2017_2018_d_00_53535.ann',
            'cdr3.a.A_2017_2018_d_07_11143.ann',
            'cdr3.a.B_2017_2018_d_00_56786.ann',
            'cdr3.a.B_2017_2018_d_09_50844.ann',
            # 'cdr3.a.C_2017_2018_d_00_26898.ann',
            # 'cdr3.a.C_2017_2018_d_07_48996.ann',
            # 'cdr3.a.D_2017_2018_d_00_45294.ann',
            # 'cdr3.a.D_2017_2018_d_07_55841.ann',
            # 'cdr3.a.E_2017_2018_d_00_94077.ann',
            # 'cdr3.a.E_2017_2018_d_07_54569.ann',
        ],
        y=[
            0,
            1,
            0,
            1,
            # 0,
            # 1,
            # 0,
            # 1,
            # 0,
            # 1,
        ],
    )

if __name__ == '__main__':
  main()
