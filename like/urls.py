from django.urls import path
from . import views


urlpatterns = [
    path('<int:id>/', views.create_like, name='add_like')
]
