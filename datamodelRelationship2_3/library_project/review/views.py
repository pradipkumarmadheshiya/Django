from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import ReviewForm
from .models import ReviewModel
from django.views import View
from django.views.generic.base import TemplateView

# def index(request):
#     if request.method=="POST":
#         form = ReviewForm(request.POST)
#         if form.is_valid():
#             data=ReviewModel(username=form.cleaned_data["username"])
#             data.save()
#             return HttpResponseRedirect("thankYou/")
            
#     form=ReviewForm()


#     return render(request, "review/index.html", {"form":form})
    
# def thankYou(request):
#     return render(request, "review/thankYou.html")

class ReviewView(View):

    def get(self, request):
        form=ReviewForm()
        return render(request, "review/index.html", {"form":form})
    
    def post(self, request):
        form=ReviewForm(request.POST)
        if form.is_valid():
            review=ReviewModel(username=form.cleaned_data["username"])
            review.save()
            return HttpResponseRedirect("thankYou/")
        
        return render(request, "review/index.html", {"form":form})
    
class ReviewViewList(View):
    def get(self, request):
        allreviews=ReviewModel.objects.all()
        return render(request, "review/reviewList.html", {"reviews":allreviews})
    
class ThankYouView(TemplateView):
    template_name="review/thankYou.html"