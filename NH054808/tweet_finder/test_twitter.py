import oauth2 as oauth
from django.test import TestCase
from mock import MagicMock, patch
from twitter_api import Twitter
from tweet import Tweet

class TestTwitter(TestCase):

	authorize = Twitter()

	#tests the case where no tweets are requested
	def test_blank_get_tweets(self):
		tweets = self.authorize.request_tweets(None)
		self.assertEquals(len(tweets), 0)

	#tests the case where there is no json data
	@patch('tweet_finder.twitter_api.Twitter.jsonify_tweet')
	def test_blank_json_data(self, json_data):
		json_data.return_value = None
		tweets = self.authorize.request_tweets('test')
		self.assertEquals(len(tweets), 0)
