#!/usr/bin/env python

# noinspection PyUnresolvedReferences
from xml.dom import minidom
import xml.sax

# parse an xml file by name
mydoc = minidom.parse('Ex_6.xml')

items = mydoc.getElementsByTagName('item')

#Change name of first attribute:
items[0].attributes["name"].value="New name"
#Change value of first attribute:
items[1].firstChild.data="New value"


with open("Ex_6_changed.xml", "w") as new_file:
    mydoc.writexml(new_file)