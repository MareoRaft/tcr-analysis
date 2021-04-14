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


def scatter_and_func(x, y, x_dense, y_dense):
    '''
    Plot a scatter plot of points, and then plot a curve on the same axis (typically used to show a curve fitting).
    '''
    # plot results
    plt.scatter(x, y)
    plt.plot(x_dense, y_dense)
    # label things
    plt.title('Zipf curve fitting')
    plt.show()


def fit_curve(x, y):
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
  plt.title('cdr3 frequencies left to right')
  plt.xlabel('sample date')
  plt.ylabel('cdr3 frequency in sample')
  # add the legend
  if show_legend:
    plt.legend()
  # finally, print the graph
  plt.show()



def lifespan_graph(cdr3s, x, ys, show_legend=True):
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
  if show_legend:
    plt.legend()
  # finally, print the graph
  plt.show()
