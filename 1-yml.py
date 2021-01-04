#!/usr/bin/python3

import yaml

testyml = open('1.yml')

ymlfile = yaml.load_all(testyml) 

for x in ymlfile:
	print(x)

