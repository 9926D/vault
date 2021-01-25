#!/usr/bin/python3

import json

def json_to_dict(json_str):
  dict_str = json.loads(json_str)
  return dict_str

json_text = """
	{ "Sneakers" : 
	     {
	    "Sports" : [ 
	      { "Running" : "Asics Saucony Brooks Nike" },
 	      { "Basketball" : "Nike Under Armour Reebok Adidas" },
	      { "Baseball" : "Converse Avia Under Armour Converse"}
			],
	       
	     
	    "Leisure": [
		{ "Walking": "Pro-Keds Saucony Brooks Asics Puma"},
		{ "Traveling": "Pumas Reebok Adidas New Balance" },
		{ "Dating": "Pumas Reebok Adidas New Balance" }
			]	 
		 }
		 	
	     }
	  
	    """

mydict = json_to_dict(json_text)
for x in mydict.keys():
  print(x)

print("\n")

for x in mydict.values():
  print(x)
	   
