
from django import forms

class plantForm(forms.Form):
	pid = forms.CharField(max_length=100)
	latitude = forms.CharField(max_length=100)
	longitude = forms.CharField(max_length=100)

