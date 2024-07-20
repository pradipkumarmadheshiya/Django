from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.contrib.auth.models import User
from .forms import CreateUser, CreatePost, CreateComment
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Post

def home(request):
    return render(request, "authentication/home.html", context=None)

def create_user(request):
    if request.method=="POST":
        form=CreateUser(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form=CreateUser()
    return render(request, "authentication/createUser.html", {"form":form})

def login_user(request):
    if request.method=="POST":
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request, user)
            return redirect("home")
    else:
        form=AuthenticationForm()

    return render(request, "authentication/loginUser.html", {"form":form})

def logout_user(request):
    if request.method=="POST":
        logout(request)
        return redirect("home")
    return render(request, "authentication/logoutUser.html", context=None)

@login_required(login_url="/login/")
def user_profile(request):
    user=get_object_or_404(User, id=request.user.id)
    return render(request, "authentication/user.html", {"user":user})

login_required(login_url="/loginUser/")
def create_post(request):
    if request.method=="POST":
        form=CreatePost(request.POST)
        if form.is_valid():
            post=form.save(commit=False)
            post.author=request.user
            post.save()
            return redirect("home")
    else:
        form=CreatePost()
    return render(request, "authentication/createPost.html", {"form":form})

@login_required(login_url="/login/")
def post_list(request):
    user=get_object_or_404(User, id=request.user.id)
    posts=user.posts.all()
    if len(posts)==0:
        return HttpResponse("No post is avaiblable")
    return render(request, "authentication/postList.html",{'posts':posts})

@login_required(login_url="/login/")
def edit_post(request, id):
    post=get_object_or_404(Post, id=id)
    if request.method=="POST":
        form=CreatePost(request.POST, instance=post)
        if form.is_valid:
            form.save()
            return redirect("postList")
    else:
        form = CreatePost(instance=post)
    return render(request, "authentication/editPost.html", {"form":form})

@login_required(login_url="/login/")
def create_comment(request,id):
    post=get_object_or_404(Post, id=id)
    if request.method=='POST':
        form=CreateComment(request.POST)
        if form.is_valid:
            comment=form.save(commit=False)
            comment.post=post
            comment.author=request.user
            comment.save()
            return redirect("postList")
    else:
        form=CreateComment()
    return render(request, "authentication/createComment.html", {"form":form})