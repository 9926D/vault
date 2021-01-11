#!/usr/bin/python3

import yaml

def yaml_keys(doc):
  with open(doc) as y:
    yfile = yaml.load(y, Loader=yaml.FullLoader)
    key_list = [ x for x in yfile.keys() ]
    return key_list

def yaml_values(doc):
  with open(doc) as y:
    yfile = yaml.load(y, Loader=yaml.FullLoader)
    value_list = [ x for x in yfile.values() ]
    return value_list


just_keys = yaml_keys('3.yml')

for x in just_keys:
  print("{} is a key".format(x))

print("\n")

just_values = yaml_values('3.yml')

for x in just_values:
  print("{} is a value".format(x))

print("\n")
	
