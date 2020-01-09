from django.urls import path
from . import views
# from django.views.generic import TemplateView


urlpatterns = [
    path('<slug:tags_slug>/', views.get_quessions_list,
         name='forum_for_tag'),
    path('', views.get_quessions_list, name='forum'),
]
