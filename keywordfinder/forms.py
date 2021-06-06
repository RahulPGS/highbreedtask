from .models import URLKeywords
from django import forms


class URLKeywordform(forms.ModelForm):
    class Meta:
        model = URLKeywords
        fields = ['url']
