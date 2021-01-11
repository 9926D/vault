#!/usr/bin/python3

import yaml

testyml = open('1.yml')

ymlfile = yaml.load_all(testyml, Loader=yaml.FullLoader) 

for x in ymlfile:
	print(x)

