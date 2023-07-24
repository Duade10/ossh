from django.views.generic import ListView, DetailView

from . import models


class PostListView(ListView):
    model = models.Post
    template_name = "blog/post_list.html"
    context_object_name = "posts"


class PostDetailView(DetailView):
    model = models.Post
    template_name = "blog/post_detail.html"
    context_object_name = "post"
