from django.shortcuts import render

from django.http import HttpResponse

def blogList(request):
    lists=[
    {"id":1, "title":"first list", "content":"This is the first list of blog"},
    {"id":2, "title":"second list","content":"This is the second list of blog"},
    {"id":3, "title":"third list", "content":"This is the third list of blog"}
        ]
    return render(request, "blog/blogList.html", {"lists":lists})

def blogDetails(request, id):
    lists={
    1 : {"name":"Jimmy", "title":"first list", "content":"This is the first list of blog"},
    2 : {"name":"John", "title":"second list","content":"This is the second list of blog"},
    3 : {"name":"James", "title":"third list", "content":"This is the third list of blog"}
    }
    
    detailedBlog=lists.get(id)

    return render(request, "blog/blogDetails.html", {"detailedBlog":detailedBlog})