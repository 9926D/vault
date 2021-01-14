#!/usr/bin/python3

import xml.etree.ElementTree as r

def get_root_tag(xml_file):				#Function for pulling the root tag
	root_tag = xml_file.tag
	return root_tag
	
def get_child_tags(xml_file):				#Function for pulling all the child tags
	child_tag_list = [  x.tag for x in xml_file ]
	return child_tag_list

def get_child_attribs(xml_file):			#Function for pulling all the child attributes
	child_attribs = [ x.attrib for x in xml_file ]    
	return child_attribs
	
def get_author(xml_file):
	auth_list = [ x.text for x in xml_file.iter('author') ]
	return auth_list

rp = r.parse('books.xml')
trunk = rp.getroot()

rt = get_root_tag(trunk)
print("{}\n".format(rt))

children_tag_list = get_child_tags(trunk)
for x in children_tag_list:
	print(x)
print("\n")

children_attrib_list = get_child_attribs(trunk)

for x in children_attrib_list:
	print(x)

print("\n")

authors = get_author(trunk)

for x in authors:
  print("<author>{}</author>".format(x))

