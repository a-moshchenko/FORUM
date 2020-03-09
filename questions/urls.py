from django.urls import path
from . import views


urlpatterns = [
    path('', views.QuestionListView.as_view(), name='forum'),
    path('new/', views.CreateQuestionView.as_view(), name="new_question"),
    path('update/<int:id>/', views.UpdateQuestionView.as_view(),
         name="update_question"),
    path('delete/<int:id>/', views.DeleteQuestionView.as_view(),
         name="delete_question"),
    path('<int:id>/create_answer/', views.CreateAnswerView.as_view(),
         name='create_answer'),
    path('<int:id>/', views.QuestionDetailView.as_view(),
         name='detail'),
    path('tag/<slug:slug>/', views.QuestionListView.as_view(),
         name='forum_for_tag'),
]
