#!/usr/bin/python3

import yaml

def y_keys(doc):
  with open(doc) as f:
    fy = yaml.load(f, Loader=yaml.FullLoader)
    ks = [ k for k in fy.keys() ]
    return ks


def y_values(doc):
  with open(doc) as f:
    vy = yaml.load(f, Loader=yaml.FullLoader)
    vl = [ v for v in vy.values() ]
    return vl

 
kl = y_keys('4.yml')
for x in kl:
 print(x)

print("\n")

vl = y_values('4.yml')
for x in vl:
 print(x)




