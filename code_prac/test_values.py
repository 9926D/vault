#!/usr/bin/python3

import unittest
from values import amount

class Testing(unittest.TestCase):
  '''Beginning of unit testing'''
  
  def test_value_true(self):
    '''Quick test to check for equal values'''
    self.assertAlmostEqual( amount([1,2,3,4,5]), 5 )
  
  def test_five_or_more(self):
    '''Quick test to check for five values, raise error if not five values in list'''
    self.assertRaises(ValueError, amount, [1,2,3])








if __name__ == "__main__":
  unittest.main()

