#!/usr/bin/python3

import xml.etree.ElementTree as T

def root_tag_text(doc):				#Returns root tag and root text in a dicionary
  rttd = {}
  r = T.parse(doc)
  t = r.getroot()
  ta = t.text
  tf = ta[:-3]
  rttd.update( {t.tag : tf} )
  return rttd

def artist_loop(doc):				#Returns subtrees (Artists) from root (Musicbox)
  r = T.parse(doc)
  trunk = r.getroot()
  artists = [ x.attrib for x in trunk ]
  return artists

def all_albums(doc):
  r = T.parse(doc)
  trunk = r.getroot()
  albums = [ x.text for x in trunk.iter('Album') ]
  return albums

rtt = root_tag_text('2.xml')
print(rtt)

print("\n")

myartists = artist_loop('2.xml')
for x in myartists:
 print(x)

print("\n")

myalbums = all_albums('2.xml')
for x in myalbums:
  print(x)



