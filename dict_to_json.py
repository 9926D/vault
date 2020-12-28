#!/usr/bin/python3
import json

def d_to_j(text):
	text_json = json.dumps(text)
	return text_json

dict = 		{ 'I': 
			{ 'abc' : 
				{ 'onetwothree':'123',
				  'fourfivesix':'456'
				},
			
			  'def' :
				{ 'onetwothree':[1,2,3],
				  'fourfivesix':[4,5,6]
				},
			  
			  'ghi' :
				{ 'onetwothree':'1,2,3',
				  'fourfivesix':'4,5,6'
				}
			},
		  'II':
			{ '123':
				'onetwothreefourfivesixseveneightnine'
			},
		
			  '456':
				{ 'abc': 'xyz',
				  'one': 'a',
				  'two': 'b',
				  'three': 'c'	
				}
		}
			

json_done = d_to_j(dict)
print(json_done)		  
		
				
		  
		
