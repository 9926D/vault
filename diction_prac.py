#!/usr/bin/python3

#Testing push 12-31-2020

def dict_examples(stuff):
	
	lc = [x for x in stuff.values() ]
	return lc

testing = { "I":
		{ "one":
			{ "a1":[1,2,3],
			  "b1":[4,5,6],
			  "c1":[7,8,9]
			},			
		  
		  "two":
			{
			  "d1":[1,2,3],
			  "e1":[4,5,6],
			  "f1":[7,8,9]
			},
		 
		  "three":
			{ 
			  "g1":[1,2,3],
			  "h1":[4,5,6],
			  "j1":[7,8,9]
			}
	    	},
	    "II":
		{ "four":
			{ "a2":[1,2,3],
			  "b2":[4,5,6],
			  "c2":[7,8,9]
			}
		}
	}	  
	    
	
comp = dict_examples(testing)
for k in comp:
	print(k)
print("\n")
 
	 
			  

		

