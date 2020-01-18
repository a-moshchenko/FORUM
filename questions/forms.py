from django import forms
from .models import Question


class CreatedQuestionsForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['name', 'author', 'body', 'tags']

