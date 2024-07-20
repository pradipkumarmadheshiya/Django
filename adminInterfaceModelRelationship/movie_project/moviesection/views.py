from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from . import models

def movieList(request):

    allMovies=models.Movie.objects.all()
    
    return render(request, "moviesection/movieList.html", {"movies":allMovies})

def heroDetail(request):

    allHeroes=models.Hero.objects.all()

    return render(request, "moviesection/heroDetail.html", {"heroes":allHeroes})

def movieDetail(request, id):

    hero=get_object_or_404(models.Hero, id=id)

    movies=hero.movies.all()

    return render(request, "moviesection/movieDetail.html", {"movies":movies})