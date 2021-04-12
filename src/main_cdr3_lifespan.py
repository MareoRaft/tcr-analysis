import random

from pretty_print import pprint
import clogging
from decorators import record_elapsed_time
import data_utils
from data_utils import to_beta
import plot



# Setup
short_log = clogging.getLogger('cdr3_lifespan', 'cdr3_lifespan.log', fmt='short')


# Functions
def calculate_lifespan(cdr3s, dates, samples):
  # calculate x and y
  x = dates
  ys = [
    [s[cdr3] for s in samples] # <- single y
    for cdr3 in cdr3s
  ]
  # return results
  return x, ys

@record_elapsed_time
def calculate_one(cdr3s, file_names, show_legend=True):
  '''
  Calculate a metric on a single distance.
  '''
  # get input data
  counters = [data_utils.get_cdr3_counter_from_file(f,f) for f in file_names]
  # calculate
  dates = [data_utils.get_date_from_file_name(f) for f in file_names]
  x, ys = calculate_lifespan(cdr3s, dates, counters)
  # output results
  short_log.info(f'cdr3s={cdr3s}, x={x}, ys={ys}, fnames={file_names}')
  plot.lifespan_graph(cdr3s, x, ys, show_legend)


@record_elapsed_time
def main():
  s = data_utils.get_cdr3_counter_from_file('s', 'cdr3.b.A_2019_2020_d_00_20857.ann')
  calculate_one(
    cdr3s=[s.get_cdr3_by_rank(r) for r in range(1, 5)],
    file_names=to_beta([
      'cdr3.a.A_2017_2018_d_00_53535.ann',
      'cdr3.a.A_2017_2018_d_07_11143.ann',
      'cdr3.a.A_2017_2018_d_28_44887.ann',
      'cdr3.a.A_2017_2018_m_04_73516.ann',
      'cdr3.a.A_2019_2020_d_00_20857.ann',
    ]),
    show_legend=True,
  )
  return 'done'

if __name__ == '__main__':
  main()
