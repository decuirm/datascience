#!/usr/bin/python

################################################################################
#	term_sentiment.py
#
#	Created by Matt Decuir
#	Intro to Data Science, Spring 2013
#
#	This script inputs a sentiment and tweet file and outputs the sentiment
#	scores for words that do not appear in the sentiment file.  Outputs the 
#	tweet score for each unassigned word, instead of calculating an average.
#
#	1) load sentiment file
#	2) load tweet file
#	3) calculate sentiment score, identify and score unassigned words
#
#	usage: tweet_sentiment.py <sentiment_file> <tweet_file>
################################################################################

import sys
import json

def main():
	if len(sys.argv) !=3:
		print 'usage: term_sentiment.py <sentiment_file> <tweet_file>'
		sys.exit(1)

	#load sentiment file
	sent_file = open(sys.argv[1])
	scores = {} # initialize an empty dictionary
	for line in sent_file:
		term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
		scores[term] = int(score)  # Convert the score to an integer.
	
	#load tweet file
	tweet_file = open(sys.argv[2])
	tweets = [] # initialize an empty list
	for line in tweet_file:
		if 'text' in line:
			tweets.append(json.loads(line))

	#calculate sentiment score, identify and score unassigned words
	for i in range(len(tweets)):
		tweet_score = 0.0
		unassigned_words = []
		tweet = tweets[i]['text']
		for str in tweet.split(): #split tweet into words
			str = str.lower().encode('utf-8') #convert to lowercase and encode
			if str in scores.keys(): #look up word in sentiment file
				tweet_score += scores[str] #increment sentiment score
			else:
				unassigned_words.append(str) # add unassigned word to list
		for str in unassigned_words:
			print '%s %.2f' % (str,tweet_score)

if __name__ == '__main__':
  main()
