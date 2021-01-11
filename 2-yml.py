#!/usr/bin/python3

import yaml

def yaml_keys_from_all_docs(doc):
	with open(doc) as one:
		ydocs = yaml.load_all(one, Loader=yaml.FullLoader)
		the_keys = []
		for doc in ydocs:  	
			for k in doc.keys():
				the_keys.append(k)
		return the_keys

def yaml_values_from_all_docs(doc):
	with open(doc) as one:
		ydocs = yaml.load_all(one, Loader=yaml.FullLoader)
		the_values = [ v for y in ydocs for v in y.values() ]
		return the_values
		
				
get_yaml_keys = yaml_keys_from_all_docs('2.yml')

for x in get_yaml_keys:
	print(x)
print("\n")

get_yaml_values = yaml_values_from_all_docs('2.yml')

for x in get_yaml_values:
	print(x)
print("\n")



