import random

import scipy as sp

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


short_log = clogging.getLogger('fit_curve', 'fit_curve.log', fmt='short')


def pareto():
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
  distribution = ot.ParetoFactory().build(data)
  print(distribution)

  from openturns.viewer import View

  pdf_graph = distribution.drawPDF()
  pdf_graph.setTitle(str(distribution))
  View(pdf_graph, add_legend=False)

  print('pdf viewed.')

  pdf_data = pdf_graph.drawables.data
  print(pdf_data)




# # Functions
# def fit_curve(x, y):
#   # fit data to curve
#   a,b,c = sp.stats.pareto.fit(data)
#   # return results
#   return a,b,c

# @record_elapsed_time
# def calculate_one(file_name, show_legend=True):
#   # get input data
#   f = file_name
#   sample = data_utils.get_cdr3_counter_from_file(f,f)
#   # calculate
#   # TODO: put curve fitting here
#   a,b,c = fit_curve(sample, sample)
#   # score the fit
#   score =
#   # output results
#   print(a,b,c)
#   print(f'score: {score}')
#   # short_log.info(f'cdr3s={cdr3s}, x={x}, ys={ys}, fnames={FILE_NAMES}')
#   # plot.fit_curve(cdr3s, x, ys, show_legend)


@record_elapsed_time
def main():
  # calculate_one(file_name=FILE_NAME)
  pareto()
  return 'done'

if __name__ == '__main__':
  main()






