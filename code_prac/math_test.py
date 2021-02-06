#!/usr/bin/python3

def square_and_cube(x):
    if x == 0:
      raise ValueError("Number can't be {}".format(x))  
    result = (x ** 2) + (x ** 3)
    return result    



x = 0
mynum = square_and_cube(x)


