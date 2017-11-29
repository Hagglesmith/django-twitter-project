import datetime
from django.db import models
from django.db.models import F
from django.utils import timezone

#This class represents phrases searched by users
class Phrase(models.Model):
	phrase_text = models.CharField(max_length=140, unique=True)
	frequency = models.PositiveIntegerField(default=1)
	last_searched = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.phrase_text

	#updates Phrase.last_searched AFTER displaying it on screen
	def update_last_searched(self, phrase_text):
		phrase_new_date = Phrase.objects.get(phrase_text=phrase_text)
		phrase_new_date.last_searched = timezone.now()
		phrase_new_date.save()

	"""Adds a user inputted phrase into the database, the textArea model 
	requires user input, so it is not necessary to check if the user input 
	phrase_text"""
	@classmethod
	def add_phrase(cls, phrase_text):
		"""if the phrase_text is > 140, then slice it to be within twitter's 140
		character limit"""
		if len(phrase_text) > 140:
			phrase_text = phrase_text[:140]

		#check to see if phrase is already created, else create it
		phrase, got_created = cls.objects.get_or_create(phrase_text=phrase_text)
		if got_created == False:
			cls.objects.filter(phrase_text=phrase_text).update(frequency=F('frequency')+1)

		phrase.update_last_searched(phrase_text)

		return phrase
	