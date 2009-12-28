#! /usr/bin/env python

import cgi
import cgitb
import glob
import os
import urllib
from xml.dom.minidom import getDOMImplementation
cgitb.enable()

print "Content-Type: text/xml"
print

form = cgi.FieldStorage()



currentPath = os.getcwd()
basePath = os.path.basename(currentPath)
files = []
files.extend(glob.glob('./*.mp3'))
files.extend(glob.glob('./*.MP3'))
files.extend(glob.glob('./*.aac'))
files.extend(glob.glob('./*.AAC'))
files.sort()
files.reverse()

dom = getDOMImplementation()
doc = dom.createDocument(None, 'rss', None)
root = doc.documentElement
root.setAttribute('version', '2.0')
channel = root.appendChild(doc.createElement('channel'))
channel.appendChild(doc.createElement('title')).appendChild(doc.createTextNode(basePath))
channel.appendChild(doc.createElement('description')).appendChild(doc.createTextNode(basePath))
channel.appendChild(doc.createElement('language')).appendChild(doc.createTextNode('en-us'))
channel.appendChild(doc.createElement('link')).appendChild(doc.createTextNode('http://www.google.com'))

for file in files:
	item = doc.createElement('item')
	item.appendChild(doc.createElement('title')).appendChild(doc.createTextNode(os.path.basename(file)))
	enc = doc.createElement('enclosure')
	url = 'http://' + os.environ['HTTP_HOST'] + os.path.dirname(os.environ['SCRIPT_NAME']) + '/' + os.path.basename(file)
	urllib.quote(url)
	enc.setAttribute('url', url)
	enc.setAttribute('type', 'audio/mpeg')
	item.appendChild(enc)
	channel.appendChild(item)

print doc.toprettyxml()

