#!/usr/bin/python3

#Added some comments
#And some more comments
#Comments, comments, comments

import yaml

testyml = open('1.yml')

ymlfile = yaml.load_all(testyml, Loader=yaml.FullLoader) 

for x in ymlfile:
	print(x)

