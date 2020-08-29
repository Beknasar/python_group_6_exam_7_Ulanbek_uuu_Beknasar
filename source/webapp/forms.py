from django import forms
from django.core.exceptions import ValidationError

from .models import Poll, Choice

class SearchForm(forms.Form):
    search = forms.CharField(max_length=100, required=False, label="Найти")

class PollForm(forms.ModelForm):
    class Meta:
        model = Poll
        fields = ['question']


class ChoiceForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = ['text']