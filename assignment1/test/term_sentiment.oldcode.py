#!/usr/bin/python

################################################################################
#	term_sentiment.py
#
#	Created by Matt Decuir
#	Intro to Data Science, Spring 2013
#
#	This script inputs a sentiment and tweet file and outputs the sentiment
#	scores for words that do not appear in he sentiment file.  
#	Can be executed by running the following command:
#
#	tweet_sentiment.py <sentiment_file> <tweet_file>
################################################################################

#1) open and load sentiment file
#2) open and load tweet file
#3) calculate tweet sentiments and identify unassigned words
#4) loop through unassigned words and output sentiment score for entire tweet

#alternative...
#5) lookup unassigned word values in tweet sentiments and calculate sentiment
#6) output unassigned word sentiments

import sys
import json

def main():
	if len(sys.argv) !=3:
		print 'usage: tweet_sentiment.py <sentiment_file> <tweet_file>'
		sys.exit(1)

	#open and load sentiment file
	sent_file = open(sys.argv[1])
	scores = {} # initialize an empty dictionary
	for line in sent_file:
		term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
		scores[term] = int(score)  # Convert the score to an integer.
	
	#open and load tweet file
	tweet_file = open(sys.argv[2])
	tweets = [] # initialize an empty list
	for line in tweet_file:
		if 'text' in line:
			tweets.append(json.loads(line))

	#iterate through tweets, calculate sentiment scores and identify words to score 

	#tweet_scores = {}
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
		#tweet_scores[tweet] = tweet_score # add tweet to tweet_scores dictionary

		#print '%.2f' % (tweet_score) #print sentiment score for tweet
	
	#iterate through unassigned words, assign scores and output values

	#for key in unassigned_words:
	#	count = 0
	#	word_score = 0
	#	dict[(k, v) for k, v in tweet_scores.items() if (key in k)]:
	#	#dict[(k, v) for (k, v) in tweet_scores.items() if key in k]:
	#		count += 1
	#		sum += v
	#	unassigned_words[key] = (float) sum/count
	#	print '%s %f' % (key, unassigned_words[key])

if __name__ == '__main__':
  main()