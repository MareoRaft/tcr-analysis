from pretty_print import pprint
from decorators import record_elapsed_time, on_n_gram
import clogging
import data_utils
from data_utils import to_beta
import sample_distances


# Setup
short_log = clogging.getLogger('sample_to_sample', 'sample_to_sample.log', fmt='short')


# Functions
def print_ladder_line(name, dists):
  ''' print the name followed by the distances '''
  gap_width = 3
  col_width = 12
  end = ' ' * gap_width
  print('|\n|')
  print(name, end=end)
  for dist in dists:
    if dist == None:
      string = ''
    else:
      string = '{:.3f}'.format(dist)
    print(string.rjust(col_width, ' '), end=end)
  print()

def compare_ladder(dist_func, file_names, max_gap):
  # get data
  samples = [data_utils.get_cdr3_series_from_file(f) for f in file_names]
  # compute distances
  dist_ladder = sample_distances.get_distance_ladder(samples, dist_func, max_gap)
  # display results
  short_log.info('compare ladder results:')
  for i in range(len(samples)):
    print_ladder_line(file_names[i], dist_ladder[i])
    short_log.info(f'fname={file_names[i]}, dists={dist_ladder[i]}')

@record_elapsed_time
def calculate_combination(dist_func, file_names, ladder_width=3):
  '''
  Calculate a metric on a single distance.
  '''
  print(f'Creating a "{dist_func.__name__}" distance ladder...')
  compare_ladder(dist_func, file_names, ladder_width)

def calculate_combinations():
  '''
  Try out multiple combinations of input parameters for the sake of comparing them.
  '''
  for dist_func in (
    sample_distances.lp(1),
    sample_distances.lp(2),
    sample_distances.lp(4),
    sample_distances.lp(8),
    sample_distances.lp(16),
    sample_distances.linfty,
  ):
    calculate_combination(
        dist_func=dist_func,
        file_names=[
            'cdr3.b.A_2017_2018_d_00_53535.ann',
            'cdr3.b.A_2017_2018_d_07_11143.ann',
            'cdr3.b.A_2017_2018_d_28_44887.ann',
        ],
    )

def main():
  # calculate_combinations()
  calculate_combination(
    dist_func=sample_distances.l2,
    file_names=[
        'cdr3.b.A_2017_2018_d_00_53535.ann',
        'cdr3.b.A_2017_2018_d_07_11143.ann',
        'cdr3.b.A_2017_2018_d_28_44887.ann',
        # 'cdr3.b.A_2017_2018_m_04_73516.ann',
        # 'cdr3.b.A_2019_2020_d_00_20857.ann',
    ],
  )


if __name__ == '__main__':
  main()
