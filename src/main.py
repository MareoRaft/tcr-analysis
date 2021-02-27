from time import time
from timeit import timeit

import main_single_to_sample
import main_sample_to_sample

def main():
  out = main_sample_to_sample.main()
  print('out:', out)


if __name__ == '__main__':
  main()
