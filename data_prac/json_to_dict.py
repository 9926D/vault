#!/usr/bin/python3

#Simple comment
#12-23-20 Comment to test ssh key

import json

def j_to_d(text):
	dict_text = json.loads(text)
	return dict_text


test = """
{ 
	"I": 	
		{ 
			"a": [1,2,3],
			"b": [4,5,6]
	  	},
	"II":
		{	"c": [7,8,9],
			"d": [10,11,12]
		}
}
      """

print(test)
print('\n')
new_text = j_to_d(test)
print(new_text["I"]["a"][1])	
print('\n')

for x in new_text.keys():
	print(x)
print('\n')

for x in new_text.values():
	print(x)

print(new_text["I"].values())
print('\n')
print(new_text["I"].keys())
 
