from django.urls import path
from . import views


urlpatterns = [
    path('', views.QuestionListView.as_view(), name='forum'),
    path('new/', views.QuestionNew.as_view(), name="new_question"),
    path('<int:id>/', views.QuestionDetailView.as_view(),
         name='detail'),
    path('tag/<slug:slug>/', views.QuestionListView.as_view(),
         name='forum_for_tag'),
]
