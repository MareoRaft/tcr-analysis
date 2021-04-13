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
    import openturns as ot
    data = [
      [2.7018013],
      [8.53280352],
      [1.15643882],
      [1.03359467],
      [1.53152735],
      [32.70434285],
      [12.60709624],
      [2.012235],
      [1.06747063],
      [1.41394096],
    ]
    data = [(i+1,d[0]) for i,d in enumerate(data)]
    x = np.array([d[0] for d in data])
    y = np.array(list(sorted([d[1] for d in data], reverse=True)))
    print(x)
    print(y)

    # # fit curve
    # from scipy.optimize import curve_fit
    # from scipy.special import zetac
    # def f(x, a):
    #     return (x**-a)/zetac(a)
    # result = curve_fit(f, x, y, p0=[0.56])
    # p = result[0]
    # print p

    # plot data and curve
    # plot results
    line = plt.scatter(x, y)
    # format date strings
    # axes = plt.gca()
    # xaxis = axes.xaxis
    # xaxis.set_major_formatter(date_format)
    # # make 1 tick per date
    # axes.set_xticks(x)
    # make label for legend
    # label things
    plt.title('Zipf curve fitting')
    # plt.xlabel('sample date')
    # plt.ylabel('cdr3 frequency in sample')
    # add the legend
    # if show_legend:
    # plt.legend()
    # finally, print the graph
    plt.show()



if __name__ == '__main__':
  main()
