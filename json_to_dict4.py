#!/usr/bin/python3

import json

def j_to_p(text):
  p_text = json.loads(text)
  return p_text

json_doc = """
	   { "USA" : { 
		"States" : 
	          [ { "New York" : { 
			"Cities" : [ 
			{ "Manhattan" : {
			   "Districts" : [
  			      { "Harlem" : { 
				"Zipcodes" : [ 10039, 10037, 10030 ] } 
			       		},
			      {	"Hell's Kitchen" : {
				"Zipcodes" : [ 10018, 10019, 10036 ] }
				    		},
			      { "Upper West Side" : {
				"Zipcodes" : [ 10024, 10025, 10023, 10069 ] }
						}
					   ]
				     } 
				},
			
			{ "Brooklyn" : {
			    "Districts" : {
				"Park Slope" : {
				  "Zipcodes" : [ 11215, 11217 ] }
					}
				    }
				},
				
			{ "Queens" : { 
			    "Districts" : {
			     	"Kew Gardens" : {
				  "Zipcodes" : [ 11415, 11418, 11424 ] }
					}
				   }
				}
			    ]
			}	
		    },
			{ "Connecticut" : {
			    "Cities" : [
			     { "Norwalk" : {
			        "Districts" : {
				  "South Norwalk" : {
				  "Zipcodes" : [ "06854", "only one zip" ] }
		  			}
				     }
				}
			    ]
		   	}
		   }, { "Illinois" : {
			  "Cities" : [
			  { "Chicago" : {
			     "Districts" : {
			       "Streeterville" : {
				"Zipcodes" : [ 60611, 60610 ] }
					}
				    }
				}
			   ]
			}
		    }		
	        ]
             }
	}
	  """
	
new_text = j_to_p(json_doc)

for x in new_text["USA"].values():
  print(x)

print("{}".format(new_text["USA"]["States"][0]["New York"]["Cities"][0]["Manhattan"]["Districts"]))

