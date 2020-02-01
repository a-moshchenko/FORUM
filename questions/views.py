
from .models import Question
from .forms import CreatedQuestionsForm

from django.shortcuts import render, redirect
from django.views.generic import View, ListView, DetailView


class QuestionListView(ListView):
    context_object_name = 'Questions_list'
    template_name = 'questions/forum.html'

    def get_queryset(self):
        tag_slug = self.kwargs.get('slug')
        if not tag_slug:
            return Question.objects.all()
        return Question.objects.filter(tags__name=tag_slug)


class QuestionDetailView(DetailView):
    model = Question
    pk_url_kwarg = 'id'
    template_name = 'questions/detail.html'


class QuestionNew(View):

    def post(self, request):
        form = CreatedQuestionsForm(request.POST)
        if form.is_valid():
            question = form.save()
        return redirect('detail', question.id)

    def get(self, request):
        form = CreatedQuestionsForm()
        return render(request, 'questions/new.html', {'form': form})
