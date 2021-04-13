from time import time
from timeit import timeit

import main_cdr3_to_sample
import main_cdr3s_to_sample
import main_sample_to_sample
import main_average_sample_distance
import main_cdr3_lifespan
import main_fit_curve
import main_zipf_curve_fitting

def main():
  out = main_zipf_curve_fitting.main()
  print('out:', out)


if __name__ == '__main__':
  main()
