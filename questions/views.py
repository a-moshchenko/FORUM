from django.urls import reverse_lazy
from .models import Question, Answer
from .forms import CreatedQuestionsForm
from django.http import Http404
from django.db.models import F

from django.views.generic import (ListView,
                                  DetailView,
                                  CreateView,
                                  UpdateView,
                                  DeleteView)


class QuestionListView(ListView):
    context_object_name = 'Questions_list'
    template_name = 'questions/forum.html'

    def get_queryset(self):
        tag_slug = self.kwargs.get('slug')
        if not tag_slug:
            return Question.objects.all()
        return Question.objects.filter(tags__slug__in=[tag_slug])


class QuestionDetailView(DetailView):
    model = Question
    pk_url_kwarg = 'id'
    template_name = 'questions/detail.html'
    likes = False

    def get_object(self, queryset=None):
        pk = self.kwargs.get(self.pk_url_kwarg)
        queryset = Question.objects.filter(pk=pk)
        try:
            # Get the single item from the filtered queryset
            obj = queryset.get()
        except queryset.model.DoesNotExist:
            raise Http404(("No %(verbose_name)s found matching the query") %
                          {'verbose_name': queryset.model._meta.verbose_name})
        Question.objects.filter(id=obj.id).update(views=F('views') + 1)
        return obj


class CreateQuestionView(CreateView):
    model = Question
    fields = ['name', 'body', 'tags']
    template_name = 'questions/create_question.html'
    success_url = reverse_lazy('forum')

    def form_valid(self, form):
        obj = form.save(commit=False)
        if not self.request.user.is_authenticated:
            obj.author = self.request.POST.get('author')
        else:
            obj.author = self.request.user.name
        obj.save()
        return super(CreateQuestionView, self).form_valid(form)


class UpdateQuestionView(UpdateView):
    template_name = 'questions/update_question.html'
    model = Question
    form_class = CreatedQuestionsForm
    pk_url_kwarg = 'id'


class DeleteQuestionView(DeleteView):
    model = Question
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('forum')


class CreateAnswerView(CreateView):
    model = Answer
    fields = ['body']
    template_name = 'answer/create_answer.html'
    success_url = reverse_lazy('forum')

    def form_valid(self, form):
        obj = form.save(commit=False)
        id = self.kwargs.get('id')
        if not self.request.user.is_authenticated:
            obj.author = self.request.POST.get('author')
        else:
            obj.author = self.request.user.name
        obj.question = Question.objects.get(id=id)
        obj.save()
        return super(CreateAnswerView, self).form_valid(form)
