#!/usr/bin/python3

def mynum(x):
  if type(x) is not int:
    raise ValueError("{} isn't a number".format(x))
  if x >= 100:
    raise ValueError("{} is too large a number".format(x))
  num = x * 2
  return num

#mynum = my_number(x)
#print("{}".format(mynum))

