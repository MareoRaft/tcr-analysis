import numpy as np
import pandas as pd

from series import *

def test_weak_intersection():
    # intersect with self
    s = pd.Series({'a': 1, 'b': 2})
    for wie in weak_intersection([s, s]):
        assert wie.equals(s)
    # intersect with empty
    z = pd.Series({}, dtype=np.int64)
    s = pd.Series({'a': 1, 'b': 2})
    for wie in weak_intersection([s, z]):
        assert wie.equals(z)
