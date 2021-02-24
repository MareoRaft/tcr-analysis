from ngrams import to_ngrams

def test_ngram_splitting():
  # 1 letter sequence
  assert to_ngrams(1, 'a') == ('a',)
  assert to_ngrams(2, 'a') == ('$a', 'a$')
  assert to_ngrams(3, 'a') == ('$$a', '$a$', 'a$$')
  # 2 letter sequence
  assert to_ngrams(1, 'ab') == ('a', 'b')
  assert to_ngrams(2, 'ab') == ('$a', 'ab', 'b$')





