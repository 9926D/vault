#!/usr/bin/python3

import unittest
from num_check import mynum

class Tester(unittest.TestCase):
  def test_sanity(self):
    self.assertAlmostEqual(mynum(2), (2 * 2) )
  
  def test_bad_value(self):
    self.assertRaises(ValueError, mynum, 'a') 

  def test_value_too_large(self):
    self.assertRaises(ValueError, mynum, 100)


if __name__ == '__main__':
  unittest.main()

