from django.test import Client, TestCase
from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse
from mock import MagicMock, patch
from tweet import Tweet
from tweet_finder.models import Phrase


"""constructs a mock results view and compares it to the normal view to check if
both are equal"""
class TestResultsView(TestCase):
	@patch('tweet_finder.views.Twitter.request_tweets')
	@patch('tweet_finder.views.Phrase.add_phrase')
	def test_get(self, mock_request_tweets, mock_add_phrase):
		mock_tweet_list = []
		mock_request_tweets.return_value = mock_tweet_list
		mock_phrase = Phrase()
		mock_phrase.phrase = ''
		mock_phrase.frequency = ''
		mock_phrase.last_searched = ''
		client = Client()
		response = self.client.get(reverse('results'), {'phrase':''})

		expected_value = render_to_response('tweet_finder/results.html', {'phrase': mock_phrase, 'tweets': mock_tweet_list})
		self.assertEqual(response.content, expected_value.content)
