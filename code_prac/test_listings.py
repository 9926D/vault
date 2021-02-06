#!/usr/bin/python3

import unittest
from listings import mylist

class TestList(unittest.TestCase):
  def test_list_same(self):
    self.assertNotEqual( [4,5,6,7], mylist(4,5,6,7) )
  
  def test_list_sum(self):
    self.assertAlmostEqual( 22, sum(mylist(4,5,6,7)) )

  def test_list_result(self):
    self.assertAlmostEqual( {22:(4,5,6,7)}, mylist(4,5,6,7) )

if __name__ == '__main__':
  unittest.main()

