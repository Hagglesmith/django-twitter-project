from django import forms

#The form allowing users to input and search for a phrase
class PhraseForm(forms.Form):
	phrase = forms.CharField(widget=forms.Textarea(attrs={'class':'special', 'size': '140'}))
	