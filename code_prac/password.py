#!/usr/bin/python3
import re

def my_pass(stringy):
  if re.search(r'^\d+$', stringy):
    raise ValueError("You can't use numbers for passwords")
  if stringy == "badvalue":
    raise ValueError("Value is no good")
  new_string = stringy
  return new_string
  


#new_pass = my_pass("blah")
