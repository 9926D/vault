#!/usr/bin/python3

import xml.etree.ElementTree as R

def root_pull(doc):		#Returns the root tag and root attributes in a dictionary
  rc_ra = {} 
  root = R.parse(doc)
  trunk = root.getroot()
  rc_ra.update( {trunk.tag : trunk.attrib} )
  return rc_ra  

def ssr_ssra_pull(doc):      #Returns the sub-sub-root and the attribute in a dictionary
  ssr_ssra = {}
  r = R.parse(doc)
  t = r.getroot()
  ssr_ssra.update( {t[0][0].tag : t[0][0].attrib} )
  return ssr_ssra


mydoc = '1.xml'
xml_root = root_pull(mydoc)

print(xml_root)

ssroot_text = ssr_ssra_pull(mydoc)

print(ssroot_text)


