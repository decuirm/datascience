#!/usr/bin/python

################################################################################
#	happiest_state.py
#
#	Created by Matt Decuir
#	Intro to Data Science, Spring 2013
#
#	This script inputs a sentiment and tweet file and outputs the happiest
#	state.
#
#   1) load sentiment file
#   2) load tweet file
#   3) initialize state score dictionary
#   4) calculate sentiment scores
#   5) output top result
#
#	usage: happiest_state.py <sentiment_file> <tweet_file>
################################################################################

import sys
import json

states = {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AS': 'American Samoa',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MP': 'Northern Mariana Islands',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VI': 'Virgin Islands',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'
}

def main():
	if len(sys.argv) !=3:
		print 'usage: happiest_state.py <sentiment_file> <tweet_file>'
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
			if 'place' in line:
				tweets.append(json.loads(line))

	#initialize state score dictionary
	state_scores = {}
	for k in states.keys():
		state_scores[k] = 0
	
	#calculate sentiment scores
	for i in range(len(tweets)):
		place = tweets[i].get('place')
		if place:
			if place['country_code'] == 'US': 
				state = place['full_name'].encode('utf-8').split(',')[1]
				state = state.strip()
				if state in states.keys():
					tweet_score = 0
					for str in tweets[i]['text'].split(): #split tweet into words
						str = str.lower().encode('utf-8') #convert to lowercase and encode
						if str in scores.keys(): #look up word in sentiment file
							tweet_score += scores[str] #increment sentiment score
						else:
							scores[str] = 0
					state_scores[state] += tweet_score
	
	#output top result
	results = sorted(state_scores, key=state_scores.get, reverse=True)
	print results[0]

if __name__ == '__main__':
  main()

