import random

import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

from pretty_print import pprint
import clogging
from decorators import record_elapsed_time
import data_utils
from data_utils import to_beta
import plot



# Setup
FILE_NAMES = [
  'cdr3.a.A_2017_2018_d_00_53535.ann',
  # 'cdr3.a.A_2017_2018_d_07_11143.ann',
  # 'cdr3.a.A_2017_2018_d_28_44887.ann',
  # 'cdr3.a.A_2017_2018_m_04_73516.ann',
  # 'cdr3.a.A_2019_2020_d_00_20857.ann',
]
FILE_NAME = FILE_NAMES[0]




@record_elapsed_time
def main():
    # get data
    f = FILE_NAME
    sample = data_utils.get_cdr3_counter_from_file(f,f)
    print('before sort list')
    sorted_items = list(sorted(sample.items(), key=lambda item: -item[1]))
    data = sorted_items[:20]

    # get x and y
    print('after sort list')
    x = range(1, len(data)+1)
    y = [item[1] for item in data]
    # print(x)
    # print(y)
    print(min(y))
    x_dense = np.linspace(1, len(data), 100)

    # fit curve
    from scipy.optimize import curve_fit
    from scipy.special import zetac
    def f(x, a, v_shift):
        return (x**-a)/zetac(a) + v_shift
    result = curve_fit(f, x, y, p0=[6.1, min(y)])
    print('result:')
    print(result)
    print('fitted param:')
    print(result[0])

    # plot data and curve
    # plot results
    plt.scatter(x, y)
    plt.plot(x, f(x, result[0][0], result[0][1]))
    # label things
    plt.title('Zipf curve fitting')
    # plt.xlabel('sample date')
    # plt.ylabel('cdr3 frequency in sample')
    # finally, print the graph
    plt.show()



if __name__ == '__main__':
  main()
