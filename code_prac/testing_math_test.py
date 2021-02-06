#!/usr/bin/python3

import unittest
from math_test import square_and_cube

class MyTest(unittest.TestCase):
  def test_good(self):
    self.assertAlmostEqual(square_and_cube(2), (2 ** 2 + 2 ** 3) )
    
    
  def test_bad_value(self):
    self.assertRaises(ValueError, square_and_cube, 0)


if __name__ == '__main__':
  unittest.main()

