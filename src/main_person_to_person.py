def compare_pairwise(dist_func):
  counters = {f[7:-10]:data_utils.get_cdr3_series_from_file(f) for f in FILE_NAMES}
  # iterate through all test seqs and calculate accuracy
  pairs = [((na, ca), (nb, cb)) for na,ca in counters.items() for nb,cb in counters.items() if na <= nb]
  for ((na, ca), (nb, cb)) in pairs:
    dist = dist_func(ca, cb)
    print(f'pair:{na},  {nb}  ->  dist:{dist:15.4f}')
  long_log.info(f'?, nsamp=?, dist={dist_func}')
  short_log.info(f'?, nsamp=?, dist={dist_func}')
