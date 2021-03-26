import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib import dates as mpl_dates
plt.style.use('seaborn')
COLORS = {
  'green': '#64bf7b',
  'blue': '#5e88bd',
  'red': '#d06464',
  'purple': '#9388bf',
}


def lifespan_graph(cdr3s, x, ys):
  '''
  Generate graph for a SINGLE metric, showing BOTH control and variant groups.
    * `series` -- data in form of Pandas Series
  '''
  for cdr3,y in zip(cdr3s, ys):
    # plot results
    line, = plt.plot_date(x, y, linestyle='solid')
    # format date strings
    date_format = mpl_dates.DateFormatter('%m-%d')
    axes = plt.gca()
    xaxis = axes.xaxis
    xaxis.set_major_formatter(date_format)
    # make 1 tick per date
    axes.set_xticks(x)
    # make label for legend
    line.set_label(f'cdr3 {cdr3}')
  # label things
  plt.title('cdr3 frequencies over time')
  plt.xlabel('sample date')
  plt.ylabel('cdr3 frequency in sample')
  # add the legend
  plt.legend()
  # finally, print the graph
  plt.show()


