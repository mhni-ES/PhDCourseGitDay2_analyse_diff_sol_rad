"""
Uses unit test

This will be our test to make sure we don not make a faster but erroneous function!

"""

import unittest
import numpy as np
import plot_diff_sol_rad

#plot_diff_sol_rad.mean([10,20,30],2)

#mean_out = sum([10,20,30])/2

import unittest

class TestStringMethods(unittest.TestCase):
    def test_mean(self):
        self.assertEqual(plot_diff_sol_rad.mean(np.array([10,20,30])),20)
        self.assertEqual(plot_diff_sol_rad.mean(np.array([np.nan, 20, 30])), 16.666666666666668)


if __name__ == '__main__':
    unittest.main()