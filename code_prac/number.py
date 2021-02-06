#!/usr/bin/python3
import re

def num(x):
  if type(x) is str:
    raise ValueError("{} is not an integer".format(x))
  elif x >= 20:
    raise ValueError("{} is 20 or greater".format(x))
  mynum = x * x
  return mynum

#x = 'a'
#ret_num = num(x)
#print("{}".format(ret_num))

  
