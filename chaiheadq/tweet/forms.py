from django import forms 
from .models import Tweet

class TweetForm(forms.ModelForm):
    class Meta:
        Model = Tweet
        fields = ['text','photo']