import random

from pretty_print import pprint
import clogging
from decorators import record_elapsed_time
import data_utils
import plot



# Setup
FILE_NAMES = [
  'cdr3.a.A_2017_2018_d_00_53535.ann',
  'cdr3.a.A_2017_2018_d_07_11143.ann',
  'cdr3.a.A_2017_2018_d_28_44887.ann',
  'cdr3.a.A_2017_2018_m_04_73516.ann',
  'cdr3.a.A_2019_2020_d_00_20857.ann',
]

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
def calculate_one(cdr3s, file_names):
  '''
  Calculate a metric on a single distance.
  '''
  # get input data
  counters = [data_utils.get_cdr3_counter_from_file(f,f) for f in file_names]
  # calculate
  dates = [data_utils.get_date_from_file_name(f) for f in file_names]
  x, ys = calculate_lifespan(cdr3s, dates, counters)
  # output results
  short_log.info(f'cdr3s={cdr3s}, x={x}, ys={ys}, fnames={FILE_NAMES}')
  plot.lifespan_graph(cdr3s, x, ys)


@record_elapsed_time
def main():
  calculate_one(cdr3s=['cAVRDRVGGGNKLTf', 'cVVSAFQAGTALIf', 'cADLSGGSYIPTf', 'cLVGDPGDSSYKLIf', 'cSIKAAGNKLTf', 'cALKAAGNKLTf', 'cAVGLAGGDMRf', 'cAVVTSGTYKYIf',
  ], file_names=FILE_NAMES)
                      # cAVRDRVGGGNKLTf
  return 'done'

if __name__ == '__main__':
  main()






