from django.urls import path
from . import views


urlpatterns = [
    path('', views.get_book_list, name='books')
]
