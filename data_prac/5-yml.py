#!/usr/bin/python3

import yaml

def yc(doc):
  y_docs = yaml.load_all(doc, Loader=yaml.FullLoader) 
  y_keys = [ d for doc in y_docs for d in doc.keys() ]
  return y_keys      


f = open('5.yml')
doc_keys = yc(f)
for x in doc_keys:
  print(x)

f.close()



