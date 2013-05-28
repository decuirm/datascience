#!/usr/bin/python

################################################################################
#	print.py
#
#	Created by Matt Decuir
#	Intro to Data Science, Spring 2013
#
#	This script pulls 10 pages of live twitter search data containing the term 
#	'googleio'
################################################################################

import urllib
import json

for i in range(1,11): 	
	print 	
	print 'Page ' + str(i)	
	response = urllib.urlopen("http://search.twitter.com/search.json?q=googleio&page="+ str(i)) 
	#type 'instance'

	pyresponse = json.load(response)
	#type 'dict'

	results = pyresponse["results"] 
	#type 'list'

	#text = results[i]["text"] 
	#type 'unicode'

	for j in range(0,10):
		print "Tweet %d: %s" % (j+1, results[j]["text"])

