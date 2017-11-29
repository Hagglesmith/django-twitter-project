from django.test import Client, TestCase
from mock import MagicMock, patch
from models import Phrase
import datetime

class TestPhrase(TestCase):
	###TESTS FOR phrase_text###
	#tests basic phrase creation
	def test_add_phrase(self):
		mock_phrase = MagicMock(spec=Phrase, frequency=1)
		phrase = Phrase.add_phrase('test')
		self.assertEqual(mock_phrase.frequency, phrase.frequency)
	
	#tests a phrase with blank phrase_text
	def test_phrase_text_null(self):
		mock_phrase = MagicMock(spec=Phrase, phrase_text='')
		phrase = Phrase.add_phrase('')
		self.assertEqual(mock_phrase.phrase_text, phrase.phrase_text)
	
	#tests that a phrase can be sliced down to the 140 character tweet limit
	#need to find a way to mock this
	def test_phrase_text_slicing(self):
		phrase = Phrase.add_phrase('!' * 999)
		self.assertEqual(len(phrase.phrase_text), 140)
	

	###TESTS FOR frequency###
	#tests that frequency is 1 on creation
	#need to find a way to mock this
	def test_positive_frequency(self):
		phrase = Phrase.add_phrase('test')
		self.assertEqual(phrase.frequency, 1)
	

	###TESTS FOR last_searched###
	#checks that auto_now time is correct
	#need to find a way to mock this
	def test_auto_now_creation(self):
		phrase = Phrase.add_phrase('test')
		time = str(datetime.datetime.now())
		phrase_time = str(phrase.last_searched)
		phrase_time = phrase_time[:16]
		time = time[:16]
		self.assertEqual(phrase_time, time)
	
	#checks to see if the add_phrase function updates last_searched
	def test_update_phrase(self):
		phrase = Phrase.add_phrase('test')
		Phrase.add_phrase('test')
		self.assertEqual(phrase.frequency, 1)
