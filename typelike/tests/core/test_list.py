"""
test_list.py
written in Python3
author: C. Lockhart
"""

from typelike.core import ListLike

from hypothesis import given
import hypothesis.strategies as st
import numpy as np
import pandas as pd
import unittest


# Contents
__all__ = [
    'TestList'
]


# Test typelike/core/list.py
class TestList(unittest.TestCase):
    @given(st.lists(elements=st.one_of(st.integers(), st.floats(), st.booleans(), st.text())))
    def test_list(self, data):
        self.assertTrue(isinstance(data, ListLike))

    @given(st.sets(elements=st.one_of(st.integers(), st.floats(), st.booleans(), st.text())))
    def test_set(self, data):
        self.assertTrue(isinstance(data, ListLike))

    @given(st.tuples())
    def test_tuple(self, data):
        self.assertTrue(isinstance(data, ListLike))

    @given(st.lists(elements=st.one_of(st.integers(), st.floats(), st.booleans(), st.text())))
    def test_numpy_ndarray(self, data):
        data = np.array(data)
        # TODO only 1D arrays acceptable
        self.assertTrue(isinstance(data, ListLike))

    @given(st.lists(elements=st.one_of(st.integers(), st.floats(), st.booleans(), st.text())))
    def test_pandas_series(self, data):
        data = pd.Series(data)
        self.assertTrue(isinstance(data, ListLike))