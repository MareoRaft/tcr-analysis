import random

import numpy as np
from scipy.optimize import curve_fit
from scipy.special import zetac
import matplotlib.pyplot as plt

from decorators import record_elapsed_time
import data_utils
import plot



# Setup
FILE_NAME = 'cdr3.a.A_2017_2018_d_00_53535.ann'



@record_elapsed_time
def main():
    # get data
    f = FILE_NAME
    sample = data_utils.get_cdr3_counter_from_file(f,f)
    # get x and y
    x,y = sample.get_x_y(20)
    # define function to fit
    def f(x, a, v_shift):
        return (x**-a)/zetac(a) + v_shift
    # fit curve
    fitted_params = curve_fit(f, x, y, p0=[6.1, min(y)])[0]
    # plot data and curve
    x_dense = np.linspace(1, len(x), 100)
    y_dense = f(x_dense, *fitted_params)
    plot.scatter_and_func(x, y, x_dense, y_dense)



if __name__ == '__main__':
  main()
