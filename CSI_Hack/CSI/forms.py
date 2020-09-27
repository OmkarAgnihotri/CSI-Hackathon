from django import forms
from .models import AUDIO
"""
class BasicForm(forms.Form):
	name = forms.CharField(label='name : ')
"""
class BasicForm(forms.ModelForm):
	class Meta:
		model = AUDIO
		fields = ['name','file']
