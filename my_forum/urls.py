from django.urls import path
from . import views


urlpatterns = [
    path('', views.PostListView.as_view(), name='home'),
    path('search_results/', views.PostListView.as_view(), name='search'),
    path('<slug:slug>', views.PostListView.as_view(), name='list_by_theme'),
    path('post/<slug:slug>/', views.PostDetailView.as_view(), name='post_detail'),
]
