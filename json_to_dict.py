#!/usr/bin/python3

#Simple comment

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

new_text = j_to_d(test)
print(new_text["I"]["a"][1])	 
