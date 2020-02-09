"""
test_infer_types.py
written in Python3
author: C. Lockhart
"""

from typelike import infer_type

from hypothesis import given
import hypothesis.strategies as st
import unittest


# Create a test class to help us
class TestClass:
    def __init__(self):
        pass


# Test typelike/core/core.py
class TestInferTypes(unittest.TestCase):
    @given(st.one_of(st.integers(), st.floats(), st.booleans(), st.text()))
    def test_simple(self, data):
        dtype1 = type(data)
        dtype2 = infer_type(data, itemize=False)
        self.assertTrue(dtype1 is dtype2, '{0} {1}'.format(dtype1, dtype2))

    def test_class(self):
        data = TestClass()
        dtype1 = type(data)
        dtype2 = infer_type(data, itemize=False)
        self.assertTrue(dtype1 is dtype2, '{0} {1}'.format(dtype1, dtype2))

    def test_list(self):
        data = [5, True, 'hey', TestClass()]

        # First test that, without itemization, we can infer the type
        dtype1 = type(data)
        dtype2 = infer_type(data, itemize=False)
        self.assertTrue(dtype1 is dtype2, '{0} {1}'.format(dtype1, dtype2))

        # Second test that we can itemize
        dtype1 = [type(item) for item in data]
        dtype2 = infer_type(data, itemize=True)
        for item1, item2 in zip(dtype1, dtype2):
            self.assertTrue(item1 is item2, '{0} {1}'.format(item1, item2))
