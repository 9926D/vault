#!/usr/bin/python3

import yaml

with open('2.yml') as one:
	ydocs = yaml.load_all(one, Loader=yaml.FullLoader)
	
	for doc in ydocs:  	
		for k in doc.keys():
			print("{} is a key".format(k))  

print(type(ydocs))


