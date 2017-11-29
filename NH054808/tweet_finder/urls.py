from django.conf.urls import url
from . import views
from tweet_finder.views import ResultsView, SubmitView

urlpatterns = [
	url(r'^$', SubmitView.as_view()),
	url(r'^results/', ResultsView.as_view(), name='results'),
]