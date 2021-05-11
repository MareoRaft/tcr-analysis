'''
Generate an average pre->post vaccine Delta vector.  Then, given a pair of samples, guess which direction it points in.
'''
import numpy as np
from sklearn.model_selection import LeaveOneOut

from decorators import record_elapsed_time
import data_utils
from main_delta_vector import get_avg
import series
import sample_distances

def run_model(X_train, X_test, y_train, y_test, dist_func):
    # negate series pairs that have a y value of 0
    X_train_oriented = [(v if label == 1 else -v) for v,label in zip(X_train, y_train)]
    # train model (compute the average delta vec D)
    avg_delta_vec = get_avg(X_train_oriented)
    neg_delta_vec = -avg_delta_vec
    print('neg avg delta vec:', neg_delta_vec)
    # predict (see if vec is closer to D or -D)
    y_test_pred = []
    for v in X_test:
        dist_to_avg_delta_vec = dist_func(v, avg_delta_vec)
        dist_to_neg_delta_vec = dist_func(v, neg_delta_vec)
        y_test_label_pred = bool(dist_to_avg_delta_vec < dist_to_neg_delta_vec)
        y_test_pred.append(y_test_label_pred)
    # return prediction
    return y_test, y_test_pred

@record_elapsed_time
def run_loocv(X, y, dist_func):
    ''' internal function. '''
    # data
    num_correct = 0
    num_total = 0
    results = []
    loo = LeaveOneOut()
    for train_indices, test_indices in loo.split(y):
        print(train_indices)
        print(test_indices)
        X_train = X[train_indices]
        X_test = X[test_indices]
        y_train = y[train_indices]
        y_test = y[test_indices]
        y_test, y_pred = run_model(X_train, X_test, y_train, y_test, dist_func)
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
    # weak intersection of CDR3s in samples
    trimmed_delta_vecs = series.weak_intersection(delta_vecs)
    # convert to a dictionary that is compatible with a Pandas DataFrame
    return trimmed_delta_vecs

def detect_vaccine(X, y, dist_func, data_limit=None):
    ''' user facing function '''
    # restrict data
    X = X[:data_limit]
    y = y[:data_limit]
    # preprocess
    X = preprocess_X(X)
    X = np.array(X)
    y = np.array(y)
    # run LOOCV
    results, accuracy = run_loocv(X, y, dist_func)
    print(results)
    print('')
    print('accuracy:', accuracy)

@record_elapsed_time
def main():
    data_limit = 3
    detect_vaccine(
        dist_func=sample_distances.lp(1),
        data_limit=data_limit,
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
