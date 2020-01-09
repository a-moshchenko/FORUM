from django.urls import path
from . import views


urlpatterns = [
    path('', views.get_postlist, name='home'),
    path('search_results/', views.search_result_view, name='search'),
    path('<slug:theme_slug>', views.get_postlist, name='list_by_theme')
]
