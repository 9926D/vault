#!/usr/bin/python3

def amount(x):
  if len(x) <= 3:
    raise ValueError("List length less three or less") 
  y = len(x)
  return y

a_list = [10,15,20,25,30]
#k = amount(a_list)
#print("{} is the amount.".format(k))

