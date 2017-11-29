from django.shortcuts import render
from django.views.generic import edit, View
from forms import PhraseForm
from models import Phrase
from twitter_api import Twitter
from tweet import Tweet

#this view that allows the user to input and search a tweet phrase
class SubmitView(edit.FormView):
	template_name = "tweet_finder/submit.html"
	form_class = PhraseForm

#this view returns the search results from Twitter
class ResultsView(View):

	def get(self, request):
		user_input = request.GET['phrase']
		phrase = Phrase.add_phrase(user_input)
		access = Twitter()
		tweet_list = access.request_tweets(user_input)

		context = {'phrase' : phrase,
				   'tweets' : tweet_list,}

		return render(request, 'tweet_finder/results.html', context)
