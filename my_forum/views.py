from django.shortcuts import render
from .models import ForumPost, Theme
from django.db.models import Q
from django.shortcuts import get_object_or_404


def get_postlist(request, theme_slug=None):
    theme = None
    themes = Theme.objects.all()
    posts = ForumPost.objects.filter(status=1).order_by('-created')
    if theme_slug:
        theme = get_object_or_404(Theme, slug=theme_slug)
        posts = posts.filter(theme=theme)
    return render(request, 'blog/post_list.html', {'posts': posts,
                                                   'themes': themes,
                                                   'theme': theme})


def search_result_view(request):
    query = request.GET.get('q')
    object_list = ForumPost.objects.filter(
        Q(title__icontains=query) | Q(content__icontains=query))
    context = {
        'object_list': object_list
        }

    return render(request, 'blog/search_results.html', context)
