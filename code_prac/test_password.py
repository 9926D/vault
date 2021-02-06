#!/usr/bin/python3
import re
import unittest
from password import my_pass

class TestPlan(unittest.TestCase):
  def test_good(self):
    self.assertAlmostEqual(my_pass("Welcome123!"), "Welcome123!")
  
  def test_bad_word(self):
    self.assertRaises(ValueError, my_pass, "badvalue")
  
  def test_word_reg(self):
    self.assertRaisesRegex(ValueError, "You can't use numbers for passwords", my_pass, '2323')

 
   

if __name__ == '__main__':
  unittest.main()

