from NH054808.settings import (SEARCH_URL, CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET)
from tweet import Tweet
import oauth2 as oauth
import httplib2
import json

#Creates connection to Twitter's API and database
class Twitter:
	#Authorizes connection
	def authorize(self):
		consumer = oauth.Consumer(key=CONSUMER_KEY, secret=CONSUMER_SECRET)
		token = oauth.Token(key=ACCESS_TOKEN_KEY, secret=ACCESS_TOKEN_SECRET)
		
		return oauth.Client(consumer, token)
	#Converts tweet data request into JSON
	def jsonify_tweet(self, user_input):
		authorization = self.authorize()
		response, tweet_data = authorization.request(SEARCH_URL + "?q=" + user_input)
		
		return json.loads(tweet_data)
	#grabs tweets from the Twitter database
	def request_tweets(self, user_input):
		if not user_input:
			return []
		#transforms the tweet into JSON data
		tweet_data = self.jsonify_tweet(user_input)
		if not tweet_data:		
			return []

		tweet_list = []

		for status in tweet_data['statuses']:
			tweet = Tweet(status['user']['screen_name'], status['text'])
			tweet_list.append(tweet)

		return tweet_list
