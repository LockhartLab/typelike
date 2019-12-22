"""
tests.py
written in Python3
author: C. Lockhart <chris@lockhartlab.org>
"""

from typelike.tests import TestList
import unittest
import sys

test_cases = [
    TestList
]


# Function to run tests
def test():
    # Create a test suite
    suite = unittest.TestSuite()

    # Load all our test cases into the suite
    loader = unittest.TestLoader()
    for test_case in test_cases:
        suite.addTests(loader.loadTestsFromTestCase(test_case))

    # Create test runner and run
    runner = unittest.TextTestRunner()
    result = runner.run(suite)

    # If the test was not successful, exit with a code
    if not result.wasSuccessful():
        sys.exit(1)



