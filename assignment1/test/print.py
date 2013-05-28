import urllib
import json

for i in range(1,11): 	
	response = urllib.urlopen("http://search.twitter.com/search.json?q=microsoft&page="+ str(i))
	pyresponse = json.load(response)
	results = pyresponse["results"]

	for j in range(0,10):
		print "p%d; t%d: %s" % (i, j+1, results[j]["text"])
