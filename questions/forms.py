from django import forms
from .models import Question, Answer


class CreatedQuestionsForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['name', 'author', 'body', 'tags']


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['author', 'code', 'image']
