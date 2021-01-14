#!/usr/bin/python3

import json

def json_to_pd(text):
  py_text = json.loads(text)
  return py_text

json_doc = """
	   {
	     "Cars" : { 
		"Makes" : ["Ford", "Toyota", "Nissan"],
		"Makes/Models" : { 
				"Ford" : ["Escort", "Mustang", "Fusion"],
				"Toyota" : ["Prius", "Corolla", "Camry", "Avalon"],
				"Nissan" : ["Versa", "Sentra", "Altima", "Maxima"]
				},
		"Model/Trims/Examples" : {
				"Ford" : { "Escort": "ZX2", "Mustang" : "5.0", "Fusion" : "SE" },
				"Toyota" : { "Prius" : "Prime", "Corolla" : "LE", "Camry" : "LE", "Avalon" : "XLE"},
				"Nissan" : {  "Versa" : "SE", "Sentra" : "SV", "Altima" : "S", "Maxima" : "CVT" }
					}
		      },
	     "Trucks": {
			"Makes" : ["Ford", "Dodge", "Chevy"]		
			
		      }
	    	
	    }
	  """


pt = json_to_pd(json_doc)

for x in pt.keys():
  print(x)  

print("\n")

for x in pt.values():
  print(x)
