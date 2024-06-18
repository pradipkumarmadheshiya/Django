from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from . import models

# Create your views here.

def blogPage(request):
    blogs=models.posts.objects.all()

    return render(request, "blog/blogList.html", {"blogs":blogs})

def blogDetails(request, postId):

    # blogs=models.posts.objects.all()

    # return render(request, "blog/blogDetails.html", {"blogs":blogs[postId-1]})

    blogDetail = get_object_or_404(models.posts,id=postId)
    return render(request, "blog/blogDetails.html", {"blogs":blogDetail})