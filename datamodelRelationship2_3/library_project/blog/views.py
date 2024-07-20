from django.http import HttpRequest
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Post
from .forms import PostForm

class PostList(ListView):
    model=Post
    template_name="blog/postList.html"
    context_object_name="posts"

class PostCreate(CreateView):
    model=Post
    template_name="blog/postCreate.html"
    form_class=PostForm
    reverse_lazy="/list/"

class PostUpdate(UpdateView):
    model=Post
    template_name="blog/postCreate.html"
    fields=["title", "content"]
    success_url="/list/"

class PostDelete(DeleteView):
    model=Post
    template_name="blog/postDelete.html"
    reverse_lazy="/list/"