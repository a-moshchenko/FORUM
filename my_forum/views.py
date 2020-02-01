from .models import ForumPost, Theme
from django.db.models import Q
from django.views.generic import ListView, DetailView


class PostListView(ListView):
    context_object_name = 'posts'
    template_name = 'blog/post_list.html'

    def get_queryset(self):
        queryset = ForumPost.objects.filter(status=1).order_by('-created')
        theme_slug = self.kwargs.get('slug')
        query = self.request.GET.get('q')
        if query:
            return ForumPost.objects.filter(
                Q(title__icontains=query) | Q(content__icontains=query))
        elif theme_slug:
            theme = Theme.objects.get(slug=theme_slug)
            return queryset.filter(theme=theme)
        return queryset


class PostDetailView(DetailView):
    model = ForumPost
    template_name = 'blog/detail.html'
    slug_field = 'slug'
    context_object_name = 'post'
