from django.urls import path
from . import views


urlpatterns = [
    path('', views.postlist, name='home'),
    path('search_results/', views.search_result_view, name='search'),
    path('<slug:theme_slug>', views.postlist, name='list_by_theme'),
    path('post/<slug:slug>/', views.post_detail, name='post_detail'),
]
