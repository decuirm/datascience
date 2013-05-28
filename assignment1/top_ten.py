#!/usr/bin/python

################################################################################
#	top_ten.py
#
#	Created by Matt Decuir
#	Intro to Data Science, Spring 2013
#
#	This script inputs a tweet file and outputs the top ten hashtags.
#
#   1) load tweet file
#   2) count hashtags
#   3) output top 10 results
#
#	usage: top_ten.py <tweet_file>
################################################################################

import sys
import json

def main():
    if len(sys.argv) !=2:
        print 'usage: top_ten.py <tweet_file>'
        sys.exit(1)

	#load tweet file
    tweet_file = open(sys.argv[1])
    tweets = [] # initialize an empty list
    for line in tweet_file:
        if 'text' in line:
            tweets.append(json.loads(line))

    hashdict = {} #initialize hashtag dictionary
	
	#count hashtags
    for i in range(len(tweets)):
        entities = tweets[i].get('entities')
        hashtags = entities['hashtags']
        if hashtags:
            for tag in hashtags:
                str = tag['text'].lower().encode('utf-8')
                if str in hashdict.keys():
                    hashdict[str] += 1
                else:
                    hashdict[str] = 1
    
    #output top 10 results              
    results = sorted(hashdict, key=hashdict.get, reverse=True)
    for i in range(10):
        print '%s %.1f' % (results[i], hashdict[results[i]])

if __name__ == '__main__':
  main()
