#!/usr/bin/python

################################################################################
#	frequency.py
#
#	Created by Matt Decuir
#	Intro to Data Science, Spring 2013
#	
#	Determines frequenecy of each term within a set of twitter data
################################################################################

	#1) load tweet file
	#2) loop through tweets, save terms to dictionary
	#3) compute frequency and output results

import sys
import json

def main():
	if len(sys.argv) !=2:
		print 'usage: frequency.py <tweet_file>'
		sys.exit(1)
	
	#load tweet file
	tweet_file = open(sys.argv[1])
	tweets = [] # initialize an empty list
	for line in tweet_file:
		if 'text' in line:
			tweets.append(json.loads(line))

	#loop through tweets, save terms to dictionary
	terms = {} # key = term, value = frequency
	for i in range(len(tweets)):
		tweet = tweets[i]['text']
		for str in tweet.split(): #split tweet into words
			str = str.lower().encode('utf-8') #convert to lowercase and encode
			if str in terms.keys():
				terms[str] += 1
			else:
				terms[str] = 1

	#compute frequency and output results
	termcount = sum(terms.values())
	for k, v in terms.items():
		terms[k] = float(terms[k])/termcount
		#print '%s %.4f' % (k, terms[k])

	#sorting doesn't work
	sortedterms = sorted(terms,key=terms.get, reverse=True)
	for i in range(len(sortedterms)):
		print '%s %.4f' % (sortedterms[])

if __name__ == '__main__':
  main()
