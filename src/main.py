from time import time
from timeit import timeit

import main_cdr3_to_sample
import main_cdr3s_to_sample
import main_sample_to_sample
import main_average_sample_distance
import main_cdr3_lifespan

def main():
  out = main_cdr3_lifespan.main()
  print('out:', out)


if __name__ == '__main__':
  main()
