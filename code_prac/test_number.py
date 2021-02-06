#!/usr/bin/python3
import re
import unittest
from number import num

class TestingValue(unittest.TestCase):
  def test_value_same(self):
    self.assertAlmostEqual( num(10), 100)

  def test_less_than_twenty(self):
     self.assertRaises(ValueError, num, 20)

  def test_value_is_num(self):
    self.assertRaises(ValueError, num, 'A')

if __name__ == '__main__':
  unittest.main()


