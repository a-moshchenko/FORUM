from django.urls import path
from . import views


urlpatterns = [
    path('', views.questions_list, name='forum'),
    path('new/', views.question_new, name="new_question"),
    path('<int:id>/', views.question_detail,
         name='detail'),
    path('<slug:tags_name>/', views.questions_list,
         name='forum_for_tag'),
]
