import ngram

def to_ngrams(n, string):
  '''
  Convert string to sequence of ngrams.
  '''
  # TODO: need a LOWERCASE preprocessing step?  Maybe in the Sample class?
  index = ngram.NGram(pad_len=(n-1), N=n)
  ngrams = tuple(index.split(string))
  return ngrams
