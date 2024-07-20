from typing import Any
from .models import Post, Comment
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.shortcuts import render

class PostList(ListView):
    model=Post
    template_name="blog/postList.html"
    context_object_name="posts"

    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context["comments"]=Comment.objects.all()
        return context


class CommentList(DetailView):
    model=Comment 
    template_name="blog/commentList.html"
    context_object_name="comments"

class PostCreate(CreateView):
    model=Post
    template_name="blog/postCreate.html"
    fields=["title", "content"]
    success_url="/list/"

class PostUpdate(UpdateView):
    model=Post
    template_name="blog/postUpdate.html"
    fields=["title", "content"]
    success_url="/list/"

class PostDelete(DeleteView):
    model=Post
    template_name="blog/postDelete.html"
    success_url="/list/"