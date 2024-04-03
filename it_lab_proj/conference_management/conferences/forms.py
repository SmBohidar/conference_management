from django import forms
from .models import Conference

class ResearchPaperForm(forms.ModelForm):
    class Meta:
        model = Conference
        fields = ['research_paper']

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Conference
        fields = ['review']
