from .models import ForumPost, Theme, PostComment
from django.db.models import Q
from django.views.generic import ListView, DetailView, CreateView
from rest_framework import generics
from .serializers import PostSerializer
from django.urls import reverse_lazy


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


class CommentCreateView(CreateView):
    model = PostComment
    fields = ['body']
    template_name = 'blog/add_comment.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        obj = form.save(commit=False)
        slug = self.kwargs.get('slug')
        if not self.request.user.is_authenticated:
            obj.author = self.request.POST.get('author')
        else:
            obj.author = self.request.user.name
        obj.post = ForumPost.objects.get(slug=slug)
        obj.save()
        return super(CommentCreateView, self).form_valid(form)


class ForumPostsApiView(generics.ListAPIView):
    queryset = ForumPost.objects.all()
    serializer_class = PostSerializer
