import random

import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score

from decorators import record_elapsed_time
import data_utils
import plot





@record_elapsed_time
def main():
    # get data
    f = 'cdr3.a.A_2017_2018_d_00_53535.ann'
    sample = data_utils.get_cdr3_counter_from_file(f,f)
    # get x and y
    x,y = sample.get_x_y(500)
    # define function to fit
    def f(x, a, b, c):
        return a * x**b + c
    # fit curve
    fitted_params = curve_fit(f, x, y, p0=[60000, -1.1, min(y)])[0]
    print('fitted params:', fitted_params)
    # measure error
    score = r2_score(y_true=y, y_pred=f(x, *fitted_params))
    print('R^2 score:', score)
    # plot data and curve
    x_dense = np.linspace(1, len(x), 100)
    y_dense = f(x_dense, *fitted_params)
    plot.scatter_and_func(x, y, x_dense, y_dense)



if __name__ == '__main__':
  main()
