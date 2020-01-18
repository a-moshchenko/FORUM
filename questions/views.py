from django.shortcuts import render, redirect
from .models import Question
from django.shortcuts import get_object_or_404
from django.db.models import F
from .forms import CreatedQuestionsForm


def questions_list(request, tags_name=None):
    tag = None
    question_list = Question.objects.all()
    if tags_name:
        question_list = question_list.filter(tags=tag)
    return render(request, 'questions/forum.html', {'qq': question_list})


def question_detail(request, id):
    question = get_object_or_404(Question, id=id)
    Question.objects.filter(id=question.id).update(views=F('views') + 1)
    return render(request, 'questions/detail.html', {'question': question})


def question_new(request):
    if request.method == 'POST':
        form = CreatedQuestionsForm(request.POST)
        if form.is_valid():
            question = form.save()
        return redirect('detail', question.id)
    else:
        form = CreatedQuestionsForm()
    return render(request, 'questions/new.html', {'form': form})
