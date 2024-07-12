from django.shortcuts import render, redirect, get_object_or_404
from .forms import CreateUser, CreatePost
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from .models import Post

def home(request):
    return render(request, "blog/home.html", context=None)

def create_user(request):
    if request.method=="POST":
        form=CreateUser(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form=CreateUser()
    return render(request, "blog/createUser.html", {"form":form})

def login_user(request):
    if request.method=="POST":
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request, user)
            return redirect("home")
    else:
        form=AuthenticationForm()
    return render(request, "blog/loginUser.html", {"form":form})

def logout_user(request):
    if request.method=="POST":
        logout(request)
        return redirect("home")
    return render(request, "blog/logoutUser.html", context=None)

@login_required(login_url="/loginUser/")
def user_profile(request):
    user=get_object_or_404(User, id=request.user.id)
    return render(request, "blog/user.html", {"user":user})

@login_required(login_url="/loginUser")
def create_post(request):
    if request.method=="POST":
        form=CreatePost(request.POST)
        if form.is_valid():
            post=form.save(commit=False)
            post.author=request.user
            post.save()
            return redirect("postList")
    else:
        form=CreatePost()
    return render(request, "blog/createPost.html", {"form":form})

@login_required(login_url="/loginUser/")
def post_list(request):
    user=get_object_or_404(User, id=request.user.id)
    posts=user.posts.all()
    if len(posts)==0:
        return HttpResponse("No post is available!")
    return render(request, "blog/postList.html", {'posts':posts})

@login_required(login_url="/loginUser/")
def edit_post(request, id):
    post=get_object_or_404(Post, id=id)
    if request.method=="POST":
        form=CreatePost(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect("postList")
    else:
        form=CreatePost(instance=post)
    return render(request, "blog/editPost.html", {"form":form})

@login_required(login_url="/loginUser/")
def post_detail(request,id):
    post=get_object_or_404(Post, id=id)
    return render(request, "blog/postDetail.html", {"post":post})

@login_required(login_url="/loginUser/")
def post_delete(request,id):
    post=get_object_or_404(Post, id=id)
    if post.author!=request.user:
        return HttpResponse("You are not allowed to delete this post")
    post.delete()
    return redirect("postList")